# Project Profile

---
date: 2026-05-27
status: Public project profile
source_baseline: Orina profile, protocol spec, and whitepaper sources
---

## One-Liner

Orina Protocol is deterministic settlement infrastructure for real-world asset commerce and autonomous transactions.

## Short Introduction

Orina Protocol is a settlement-first infrastructure layer for real-world asset commerce and autonomous transactions. Its Atomic Transaction Protocol (ATP) defines escrow-backed transaction lifecycles, explicit state transitions, timeout paths, dispute handling, and canonical final settlement.

## Long Introduction

Orina Protocol is designed to solve a core weakness in digital commerce, marketplace, escrow, and RWA systems: transaction correctness is often left to platform discretion, participant trust, incentives, or loosely coordinated off-chain workflows.

ATP makes settlement a protocol-level state machine. It defines how value is escrowed, how assets are locked or consumed, how transaction states progress, how disputes and timeouts resolve, and how final settlement becomes canonical.

Orina separates settlement authority from surrounding systems. Marketplaces, AI tools, logistics software, IoT signals, analytics modules, and user interfaces can operate around the protocol, but they do not define canonical settlement. The protocol remains the authority for escrow release, refunds, state transitions, receipt minting, and finalization.

## Core Thesis

Commerce should be settlement-first. A transaction is reliable only when it has a clear, enforceable, auditable, and final outcome.

## What Orina Is

- A deterministic settlement layer for real-world asset commerce.
- A protocol core for escrow-backed transactions.
- A state machine for bounded execution, timeout paths, disputes, and finality.
- A foundation for autonomous commerce where AI can generate structured intent but cannot override settlement rules.

## What Orina Is Not

- Not only a marketplace UI.
- Not an AI assistant.
- Not a generic DeFi primitive.
- Not a logistics oracle.
- Not a price discovery engine.

## Architecture Summary

| Layer | Role |
| --- | --- |
| Asset representation | Creates structured on-chain asset identities and quantity state. |
| Transaction and escrow | Handles order state, escrow, payment routing, refunds, timeout logic, disputes, and final settlement. |
| Intelligence and verification | Lets AI, analytics, logistics, or delegated software assist execution under explicit constraints. |
| Application and interface | Provides marketplace, dashboard, partner, and user workflows around the settlement core. |

## Core Smart Contract Modules

| Module | Role |
| --- | --- |
| `MarketplaceATP` | Central order-state coordinator. |
| `PaymentGateway` | Escrow, fee routing, settlement, and refund authority. |
| `OrinaRWA` | Asset representation and quantity lifecycle management. |
| `FeeManager` | Fee calculation and token-specific fee presets. |
| `AutoTimeManager` | Time-based executor for cancellation, auto-release, and stale state handling. |
| `DisputeManager` | Dispute opening, state, and binding resolution paths. |
| `RWAReceiptNFT` | Post-finalization non-transferable receipt issuance. |
| `DelegationManager` | Bounded autonomous execution layer for delegated actions and M2M commerce. |

## ORI Token Snapshot

| Field | Value |
| --- | --- |
| Token name | ORINA |
| Token symbol | ORI |
| Token type | Utility / protocol coordination token |
| Chain | BNB Smart Chain |
| Standard | BEP-20 |
| Decimals | 18 |
| Total supply | 1,000,000,000 ORI |
| Contract | [`0x093969C2Bb194e7424534918ECa5119FA72a61d6`](https://bscscan.com/token/0x093969c2bb194e7424534918eca5119fa72a61d6) |

ORI is associated with ecosystem access, fees, participation, discount tiers, staking or incentive systems where activated, and future governance functions. ORI does not define transaction correctness; ATP is the settlement logic.

## Official Links

See [Official Links](../reference/official-links.md).
