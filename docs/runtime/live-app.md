# Runtime App

---
date: 2026-05-27
status: Public runtime reference
runtime: ATP v3.4.1
network: BSC Testnet
---

The public Orina runtime app is available at:

- https://app.orina.io/

This page documents the current public runtime reference only. It covers ATP v3.4.1 on BSC Testnet. Future runtime migration material and internal deployment procedures are not part of this public documentation set.

## Current Runtime

| Field | Value |
| --- | --- |
| Runtime | ATP v3.4.1 |
| Network | BSC Testnet |
| Chain id | `97` |
| Explorer | https://testnet.bscscan.com |
| Live namespace | `orina-atp-v3.4.1-m2m-bsc-testnet-20260329-r6` |
| Deployment date represented by docs/artifacts | 2026-03-29 |

The live contracts report `VERSION == "3.4"` for `MarketplaceATP`, `FeeManager`, `PaymentGateway`, `DisputeManager`, `AutoTimeManager`, and `OrinaRWA`. `RWAReceiptNFT` reports `3.4-rwa-receipt`, and `UnitRegistry` reports `3.3-final`.

## Core Contracts

| Contract | Address | On-chain version | Runtime role |
| --- | --- | --- | --- |
| `MarketplaceATP` | `0xBc6f46000b2709714C3908BB6b71BAb67A2d1495` | `3.4` | Order state machine and cross-contract coordinator. |
| `OrinaRWA` | `0x72C3477C57097f3791501F3839bB380A019B754f` | `3.4` | Canonical RWA asset registry and lock/consume/finalize ledger. |
| `RWAReceiptNFT` | `0x73719A7364c72cB0Ee77595773E9596976e298d1` | `3.4-rwa-receipt` | Non-transferable post-settlement receipt NFT. |
| `PaymentGateway` | `0xC220B68De5C6A19CfD179a37Ba5F6caE8BC57008` | `3.4` | ERC-20 escrow, fee distribution, release, and refund. |
| `FeeManager` | `0x418de18d1BD72A5Ff7A9470f94043D245C65a67B` | `3.4` | Fee schedule and token-specific platform fee presets. |
| `DisputeManager` | `0x550debf6291a7EA8Aa27aCC9ACa92397972eC47e` | `3.4` | Dispute opening, agreement, arbiter, and stale-dispute split. |
| `AutoTimeManager` | `0xE8d1Ac4463fE0805eB7234ebEe51Dd85d091622C` | `3.4` | Permissionless timeout executor. |
| `UnitRegistry` | `0x07f460A5f3a346e060e3d810821fB020eDDCe718` | `3.3-final` | Unit granularity registry. |
| `ShippingRegistry` | `0xD3c02C986559145AC7f70ccA69b1A2A351810aA2` | `3.4` | Shipping options and max shipping fee bound. |

## M2M Contracts

| Contract | Address | Runtime role |
| --- | --- | --- |
| `DelegationManager` | `0x024478973e3bBD33C85c6A0271DbaCE6608b10dB` | Bounded delegated session policy. |
| `AIWalletFactoryV2` | `0xCFE177c0930eaDDD183262dff5B57E7397d55b7E` | Deterministic AI wallet factory. |

## Payment Tokens

| Symbol | Address |
| --- | --- |
| `USDT` | `0x337610d27c682e347c9cd60bd4b3b107c9d34ddd` |
| `USDC` | `0x64544969ed7ebf5f083679233325356ebe738930` |
| `WBNB` | `0xae13d989dac2f0debff460ac112a837c89baa7cd` |
| `ORI` | `0x093969c2bb194e7424534918eca5119fa72a61d6` |

## EIP-712 Order Domain

```text
name: MarketplaceATP
version: 3.4
chainId: 97
verifyingContract: 0xBc6f46000b2709714C3908BB6b71BAb67A2d1495
```

Order type:

```text
Order(
  uint256 orderId,
  address buyer,
  address seller,
  address paymentToken,
  uint256 assetId,
  uint256 grossPrice,
  uint256 amount,
  uint256 estDeliverySeconds
)
```

Signatures are bound to chain id, verifying contract, payment token, asset id, price, amount, and delivery seconds. Testnet and mainnet signatures are not interchangeable.

## Lifecycle Constants

| Parameter | Value |
| --- | --- |
| Seller confirmation window | 24 hours |
| Buyer re-sign/pay timeout | 24 hours |
| Buyer action window after delivery timer | 3 days |
| Dispute period | 14 days |
| Dispute fee | 5 percent |

## Public Scope

This page is a public runtime reference for users, integrators, and reviewers. It intentionally excludes deployment runbooks, future runtime migration material, private environment values, local broadcast files, admin handoff procedures, and operator-only smoke-test instructions.
