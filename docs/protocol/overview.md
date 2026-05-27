# Protocol Overview

---
date: 2026-05-27
status: Public documentation baseline
source_baseline: Public ATP v3.4 runtime and contract documentation
---

Orina ATP is an escrowed bilateral transaction protocol for real-world asset marketplace flows. The protocol coordinates asset inventory, buyer payment escrow, seller confirmation, delivery timing, dispute settlement, receipt minting, fee distribution, and optional delegated machine-to-machine execution.

## Current Public Runtime

The current public runtime reference is ATP v3.4.1 on BSC Testnet. The primary EIP-712 order domain uses `MarketplaceATP` version `3.4`, and the public runtime app is documented in [Runtime App](../runtime/live-app.md).

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
- `RWAReceiptNFT` mints non-transferable receipts after finalized RWA settlement.

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
- Receipts are minted for finalized RWA ownership and are non-transferable.
- Finality is sticky after a terminal finalized or cancelled condition.
- Root direct-action fallback remains available after delegate expiry or revoke.

## Public Documentation Boundaries

This public overview describes protocol behavior and assurance posture. It does not publish operator runbooks, deployment checklists, private environment variables, or internal migration procedures.
