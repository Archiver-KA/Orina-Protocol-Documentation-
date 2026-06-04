# Runtime App

---
date: 2026-06-04
status: Public runtime reference
runtime: ATP v3.5 beta
network: BSC Testnet
---

The public Orina runtime app is available at:

- https://app.orina.io/

This page documents the current public runtime reference only. It covers ATP v3.5 beta on BSC Testnet. Operator deployment procedures, private environment values, and local broadcast files are outside this public documentation set.

## Current Runtime

| Field | Value |
| --- | --- |
| Runtime | ATP v3.5 beta |
| Network | BSC Testnet |
| Chain id | `97` |
| Explorer | https://testnet.bscscan.com |
| Live namespace | `orina-atp-v3.5-fee-split-nft-orifee-bsc-testnet-20260604` |
| Deployment date represented by docs/artifacts | 2026-06-04 |

Version notes:

- `FeeManager` and `PaymentGateway` report version `3.5`.
- `MarketplaceATP` keeps EIP-712 order-domain version `3.4` for signature compatibility.
- The March 29, 2026 ATP v3.4.1 testnet deployment is historical and is not the target for new beta traffic.

## Core Contracts

| Contract | Address | Runtime role |
| --- | --- | --- |
| `MarketplaceATP` | `0x18E1C8ab257FAf16Ec8257A9715d07661194150B` | Order state machine and cross-contract coordinator. |
| `OrinaRWA` | `0x3a591AB1aB3A281f999AAD1644b020CbEC463C47` | Canonical asset registry and lock/consume/finalize ledger. |
| `RWAReceiptNFT` | `0x16A35bdD00dCfb9010504FbD1b2B97e26bB315ca` | Post-finalization ERC721 layer for non-transferable RWA receipts and transferable NFT outcomes. |
| `PaymentGateway` | `0x082d75D8cA96C6e97B6b451Ad4857454A53D5C15` | ERC-20 escrow, fee distribution, release, and refund. |
| `FeeManager` | `0xD32fc966835D8eb7D26A12BEcCa86c749A60eFb3` | Token-specific platform and DAO fee presets. |
| `DisputeManager` | `0xCD27B85e7EA6FB1FDC484ae9083286DdCC14DC21` | Dispute opening, agreement, arbiter, and stale-dispute split. |
| `AutoTimeManager` | `0x5639792243617841800df8F1450B86223c3d86f4` | Permissionless timeout executor. |
| `UnitRegistry` | `0x4ea45450064CD5B7c88EcAaE6a145652FEDd5df0` | Unit granularity registry. |
| `ShippingRegistry` | `0x16402c8C883a01dbfD2D7E58A46D3E9434396836` | Shipping options and max shipping fee bound. |
| `TimelockController` | `0x5452CE749EDA1bE82132743AA224e7C86023A7F4` | Governance delay controller. |

## M2M Contracts

| Contract | Address | Runtime role |
| --- | --- | --- |
| `DelegationManager` | `0xb27C8eCc266423dDA3323983Ae3a2eF691ed8a13` | Bounded delegated session policy. |
| `AIWalletFactoryV2` | `0xD838268fa8dF6AFD1Fd79D9C0Fd243A3D23D0441` | Deterministic AI wallet factory. |

## Payment Tokens

| Symbol | Address |
| --- | --- |
| `USDT` | `0x337610d27c682e347c9cd60bd4b3b107c9d34ddd` |
| `USDC` | `0x64544969ed7ebf5f083679233325356ebe738930` |
| `WBNB` | `0xae13d989dac2f0debff460ac112a837c89baa7cd` |
| `ORI` | `0x093969c2bb194e7424534918eca5119fa72a61d6` |

## Fee Model

ATP v3.5 beta removes protocol burn fee from active settlement. Fees are platform and DAO routed:

| Fee token | Total fee | Platform | DAO |
| --- | ---: | ---: | ---: |
| `USDT` | 2% | 1% | 1% |
| `USDC` | 2% | 1% | 1% |
| `ORI` | 1% | 0.5% | 0.5% |

USDT/USDC purchases may pay the protocol fee in ORI through the separate fee-token order path. The beta runtime assumes nominal ORI/payment-token parity; production requires an oracle quote layer before mainnet use.

## EIP-712 Order Domain

```text
name: MarketplaceATP
version: 3.4
chainId: 97
verifyingContract: 0x18E1C8ab257FAf16Ec8257A9715d07661194150B
```

Default order type:

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

Separate fee-token order type:

```text
OrderWithFeeToken(
  uint256 orderId,
  address buyer,
  address seller,
  address paymentToken,
  address feeToken,
  uint256 assetId,
  uint256 grossPrice,
  uint256 amount,
  uint256 estDeliverySeconds
)
```

Signatures are bound to chain id, verifying contract, payment token, asset id, price, amount, delivery seconds, and fee token when separate. Testnet and mainnet signatures are not interchangeable.

## Lifecycle Constants

| Parameter | Value |
| --- | --- |
| Seller confirmation window | 24 hours |
| Buyer re-sign/pay timeout | 24 hours |
| Buyer action window after delivery timer | 3 days |
| Dispute period | 14 days |
| Dispute fee | 5 percent, split 50% platform and 50% DAO |

## Public Scope

This page is a public runtime reference for users, integrators, and reviewers. It intentionally excludes deployment runbooks, private environment values, local broadcast files, admin handoff procedures, and operator-only smoke-test instructions.
