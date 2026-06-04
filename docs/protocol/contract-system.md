# Contract System

---
date: 2026-06-04
status: Public documentation baseline
source_baseline: Public ATP v3.5 beta runtime contract documentation
---

The ATP contract system is implemented in Solidity `0.8.24` using Foundry. The local `foundry.toml` enables optimizer runs `200`, `via_ir = true`, and `evm_version = "cancun"`.

## Contract Map

| Contract | Version | Responsibility |
| --- | --- | --- |
| `MarketplaceATP` | `3.4` | Order state machine, EIP-712 order domain, direct and delegated order actions. |
| `PaymentGateway` | `3.5` | ERC-20 escrow, seller release, buyer refund, and no-burn fee distribution. |
| `FeeManager` | `3.5` | Token-specific platform and DAO fee presets. |
| `OrinaRWA` | `3.4` | Seller asset ledger, minting, locking, consumption, and unlock paths. |
| `RWAReceiptNFT` | `3.4-rwa-receipt` | Post-finalization ERC721 layer for non-transferable RWA receipts and transferable NFT outcomes. |
| `DisputeManager` | `3.4` | Dispute lifecycle, arbiter verdicts, mutual agreement, stale resolution. |
| `AutoTimeManager` | `3.4` | Permissionless seller timeout, buyer pay timeout, auto-release, stale-dispute execution. |
| `UnitRegistry` | `3.3-final` | Unit definitions and amount validation. |
| `ShippingRegistry` | `3.4` | Shipping option registry and delivery bounds. |
| `Create2Factory` | n/a | Deterministic deployment helper. |
| `DelegationManager` | n/a | M2M session authority, action masks, spend caps, term policy, revoke/expiry. |
| `AIWalletV2` | n/a | Exact-approval payer vault for delegated buy execution. |
| `AIWalletFactoryV2` | factory version `2` | Deterministic AI wallet prediction and deployment. |
| `IdentityValidator` | library | EOA and ERC-1271 root signature validation. |
| `M2MActions` | library | Delegated action bit namespace. |

## MarketplaceATP

`MarketplaceATP` stores the canonical order state. Its order struct separates:

- `buyer`: canonical root buyer.
- `seller`: canonical root seller.
- `payer`: direct buyer or delegated payer vault.
- `refundRecipient`: root-side refund recipient.
- `paymentToken`: ERC-20 payment token.
- `assetId`, `amount`, and `grossPrice`: economic terms.
- `proposedAt`, `paidAt`, `autoReleaseAt`, and `payDeadline`: lifecycle timing.
- `state`, `settlementType`, split settlement, fee snapshots, finality flags, and signatures.

Order states:

- `PENDING_CONFIRM`
- `PAID`
- `DISPUTED`
- `FINALIZED`
- `CANCELLED`

Settlement types:

- `FULL_RELEASE`
- `FULL_REFUND`
- `SPLIT`

The EIP-712 order payload is:

```text
Order(uint256 orderId,address buyer,address seller,address paymentToken,uint256 assetId,uint256 grossPrice,uint256 amount,uint256 estDeliverySeconds)
```

When the fee token differs from the payment token, the buyer signs:

```text
OrderWithFeeToken(uint256 orderId,address buyer,address seller,address paymentToken,address feeToken,uint256 assetId,uint256 grossPrice,uint256 amount,uint256 estDeliverySeconds)
```

Timing constants:

- Seller confirmation window: `24 hours`
- Buyer pay timeout after revised terms: `24 hours`
- Buyer action window after delivery timer: `3 days`

## Payment And Fees

`PaymentGateway` holds escrowed ERC-20 tokens and routes funds according to marketplace decisions. `FeeManager` calculates runtime fee schedules and token-specific fee presets.

Fee constraints from source:

- USDT/USDC fee-token total: `200` bps, split `100` bps platform and `100` bps DAO
- ORI fee-token total: `100` bps, split `50` bps platform and `50` bps DAO
- Protocol burn fee: removed from active ATP v3.5 settlement
- Maximum platform + DAO protocol fee bps: `500`
- Maximum referral fee bps: `200`
- Maximum total fee bps: `700`

The public Hybrid DAO fee model maps these presets to a 2% completed-transaction fee when the fee token is USDT/USDC and a 1% completed-transaction fee when the fee token is ORI. See [DAO Fee Governance](./dao-fee-governance.md) for the current public fee allocation model and governance boundaries.

## RWA Asset And Receipt Flow

`OrinaRWA` records seller-owned asset supply and locks amounts for orders. Finalized RWA orders can mint a receipt through `RWAReceiptNFT`. RWA receipts are non-transferable and reflect finalized ownership evidence rather than freely transferable marketplace tokens.

ATP v3.5 also supports NFT-type asset finalization. Finalized NFT orders mint transferable ERC721 tokens through the same `RWAReceiptNFT` layer while preserving the non-transferable rule for RWA receipts.

## Dispute And Auto-Time Flow

`DisputeManager` opens disputes through the marketplace boundary and supports:

- Arbiter resolution.
- Agreement-based resolution.
- Mutual split.
- One-time extension.
- Stale dispute auto-split after deadline.

`AutoTimeManager` can execute timeout actions when lifecycle windows expire:

- Cancel after seller confirmation timeout.
- Cancel after buyer pay timeout.
- Auto-release after buyer action window.
- Resolve stale disputes through the dispute manager.

## Delegation Contracts

`DelegationManager` validates delegated execution through sessions that bind:

- root
- delegate
- payer vault
- payment token
- action mask
- spend caps
- validity window
- counterparty
- asset id and amount constraints
- gross price bounds
- delivery bounds

`AIWalletV2` performs exact-approval calls for delegated payment flows and sweeps idle funds back to the root after revoke or expiry.

## Build References

Local build command from source repository:

```bash
forge build
```

Focused formal-style test command from source repository:

```bash
forge test --match-path test/MarketplaceATPFormalVerification.t.sol -vv
```

These commands are source-repository commands, not required for reading this public documentation repository.
