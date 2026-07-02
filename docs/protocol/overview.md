# Protocol Overview

---
date: 2026-06-04
status: Public documentation baseline
source_baseline: Public ATP v3.5 beta runtime and contract documentation
---

Orina ATP is the deterministic settlement core of Orina Protocol. It standardizes how two independent parties move from agreement to commitment, condition verification, and one canonical settlement outcome.

This page describes the current technical implementation of that settlement core. It intentionally treats marketplace surfaces, asset-specific flows, automation, and fee logic as integration or implementation layers around the protocol thesis, not as the definition of Orina itself.

## Current Public Runtime

The current public runtime reference is ATP v3.5 beta on BSC Testnet by default, with Base Sepolia, Arbitrum Sepolia, Ethereum Sepolia, Optimism Sepolia, Avalanche Fuji, and World Chain Sepolia also deployed as write-enabled testnet targets. The primary EIP-712 order domain still uses `MarketplaceATP` version `3.4` for signature compatibility, and the public runtime app is documented in [Runtime App](../runtime/live-app.md).

## Settlement Flow

| Step | Protocol Meaning |
| --- | --- |
| Agreement | Parties accept programmable settlement conditions. |
| Asset Commitment | Payment, asset, or service commitment is bound to the transaction. |
| Condition Verification | Confirmations, deadlines, and dispute paths are evaluated. |
| Deterministic Settlement | ATP resolves the transaction into exactly one final outcome. |

## Main Protocol Roles

| Role | Meaning |
| --- | --- |
| Root buyer | Canonical buyer identity stored on orders and receipt ownership path. |
| Root seller | Canonical seller identity stored on orders and asset ownership path. |
| Delegate | Bounded operator authorized by a root through `DelegationManager`. |
| Payer vault | AI wallet or payer address that funds delegated buy flows without becoming the buyer. |
| Governance | Role holder that configures protocol components, registries, fees, and emergency controls. |
| Arbiter | Role holder that resolves disputes through `DisputeManager`. |

## System Layers

### Core Trade Lifecycle

- `MarketplaceATP` coordinates order creation, seller confirmation, buyer payment acceptance, delivery confirmation, auto-release, cancellation, and dispute entry.
- `OrinaRWA` tracks seller-owned RWA asset supply and order-bound locks.
- `PaymentGateway` escrows ERC-20 payment tokens and routes seller proceeds, refunds, and fees.
- `RWAReceiptNFT` mints non-transferable receipts after finalized RWA settlement and transferable ERC721 tokens after finalized NFT settlement.

### Governance And Automation

- `FeeManager` stores fee schedules and token-specific platform fee presets.
- `DisputeManager` controls dispute state, arbiter verdicts, agreement resolution, mutual split, and stale-dispute settlement.
- `AutoTimeManager` executes permissionless timeout actions.
- `UnitRegistry` validates amount granularity and unit constraints.
- `ShippingRegistry` stores delivery options and bounds.

### M2M Delegation

- `DelegationManager` is the canonical source of delegated session authority.
- `IdentityValidator` validates root signatures for EOA and ERC-1271 roots.
- `AIWalletV2` is the deterministic payer vault for delegated execution.
- `AIWalletFactoryV2` predicts and deploys AI wallets.
- `M2MActions` defines action bits for delegated permissions.

## Canonical Invariants

- Stored order buyer is always the root buyer.
- Stored order seller is always the root seller.
- Delegated funding may use a payer vault, but the payer vault is not the buyer.
- Refund routing remains bound to the root buyer.
- Seller payout routing remains bound to the root seller.
- RWA receipts are minted for finalized RWA ownership and are non-transferable.
- NFT finalization mints transferable ERC721 tokens.
- Finality is sticky after a terminal finalized or cancelled condition.
- Root direct-action fallback remains available after delegate expiry or revoke.

## Public Documentation Boundaries

This public overview describes protocol behavior and assurance posture. It does not publish operator runbooks, deployment checklists, private environment variables, or internal migration procedures.
