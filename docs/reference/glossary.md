# Glossary

---
date: 2026-05-27
status: Public documentation baseline
---

## ATP

Atomic Transaction Protocol. The escrowed order protocol that coordinates buyer proposal, seller confirmation, payment escrow, delivery timing, dispute handling, settlement, and receipt minting.

## RWA

Real-world asset. In this documentation, RWA refers to protocol-tracked assets minted and locked through `OrinaRWA`.

## Root Buyer

The canonical buyer identity stored on an ATP order. Delegates and payer vaults do not replace the root buyer.

## Root Seller

The canonical seller identity stored on an ATP order and RWA asset record.

## Delegate

A bounded operator authorized by a root user through `DelegationManager`. In M2M v1, a delegate can execute only explicitly enabled pre-dispute actions.

## Payer Vault

An AI wallet or configured payer address that funds delegated buy flows. The payer vault does not become the buyer and does not receive the buyer receipt by default.

## Receipt NFT

A non-transferable `RWAReceiptNFT` minted after finalized RWA settlement to represent buyer-side receipt evidence.

## EIP-712

Typed structured-data signing standard used by ATP order and dispute agreement flows.

## NuSMV

A symbolic model checking language/tool used here for an executable abstraction of ATP lifecycle and delegated authority semantics.

## CTL, LTL, ATL

Temporal logic/specification formats used in the ATP formal artifact set:

- CTL: Computation Tree Logic.
- LTL: Linear Temporal Logic.
- ATL: Alternating-time Temporal Logic.

## Bytecode

Compiled EVM code exported from Foundry for `MarketplaceATP`. This repository publishes creation and runtime bytecode artifacts with SHA-256 hashes.
