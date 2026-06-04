# M2M Delegation

---
date: 2026-06-04
status: Public documentation baseline
source_baseline: DelegationManager, AIWalletV2, AI wallet design docs
---

The ATP M2M layer lets a root user authorize a bounded delegate or AI wallet flow without making the delegate the protocol party. The root buyer or seller remains canonical in order, asset, refund, payout, and receipt state.

## Design Goal

The design target is not "AI becomes the protocol party." The design target is:

- Root user remains canonical buyer or seller.
- Machine or delegate acts only as a bounded operator.
- Machine expiry or revocation never locks out the root user.

## Components

| Component | Responsibility |
| --- | --- |
| `DelegationManager` | Stores and validates sessions, action masks, term policy, spend caps, expiry, and revoke status. |
| `IdentityValidator` | Validates root authorization for EOA and ERC-1271 roots. |
| `AIWalletV2` | Payer vault for exact-approval delegated buy flows. |
| `AIWalletFactoryV2` | Predicts and deploys deterministic AI wallets. |
| `M2MActions` | Defines delegated action bits. |

## Supported V1 Delegated Actions

- `MarketplaceATP.createOrderFor`
- `MarketplaceATP.payOrderFor`
- `MarketplaceATP.mintAssetFor`
- `MarketplaceATP.sellerConfirmFor`

## Explicit V1 Exclusions

Delegated execution cannot perform:

- `confirmDelivery`
- `openDispute`
- `cancelByBuyer`
- `cancelBySeller`

Root direct paths remain available for these actions when the root is authorized by the core protocol state machine.

## Action Bit Namespace

The source library defines:

| Action | Bit index |
| --- | ---: |
| `BUY_CREATE_ORDER` | 0 |
| `BUY_PAY_ORDER` | 1 |
| `SELL_MINT_ASSET` | 2 |
| `SELLER_CONFIRM` | 3 |
| `SIGN_BUYER_SIG1` | 4 |
| `SIGN_BUYER_SIG2` | 5 |
| `SIGN_SELLER_SIG` | 6 |

The active v1 execution path supports the first four action categories.

## Session Controls

Delegated sessions bind:

- root
- delegate
- payer vault
- payment token
- action mask
- max amount per order
- max total spend
- validity window or no-expiry policy
- counterparty where required
- asset id where required
- asset amount bounds
- buyer max gross price
- seller min gross price
- max delivery seconds

No-expiry delegated sessions are an explicit ATP v3.5 beta option. They are allowed only when buy/pay/confirm authority is counterparty-bound and remain revocable by the root.

## Funding Model

- A user may prefund the predicted `AIWalletV2` address.
- `AIWalletFactoryV2` deploys the deterministic wallet.
- `AIWalletV2` can execute exact-approval calls against the configured marketplace and spender.
- On expiry or root revoke, idle wallet balance may be swept back to the root.
- The payer vault funds an order but does not become the buyer.

## Security Properties

- Delegate cannot become stored buyer.
- Delegate cannot become stored seller.
- Refund recipient cannot be redirected by delegate.
- Seller payout recipient cannot be redirected by delegate.
- Expired or revoked sessions cannot execute delegated actions.
- Spend accounting is bounded by per-order and total caps.
- Exact approval should leave no reusable allowance after success or revert.
- ERC-1271 validation must fail closed unless the exact magic value is returned through static validation.

## Future Relay Mode

The current source baseline uses direct delegate transactions. Relayed delegated-intent mode is deferred. If relayers are introduced, additional replay protection is required for per-intent nonce, chain, contract, session, action, and params hash binding.
