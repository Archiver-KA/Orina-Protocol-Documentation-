# Project Profile

---
date: 2026-06-04
status: Public project profile
source_baseline: Orina profile, protocol spec, and whitepaper sources
---

## One-Liner

Orina is the settlement layer for bilateral commerce.

## Short Introduction

Orina is a decentralized settlement protocol that enables any two independent parties to complete transactions without relying on trust, intermediaries, or platform-controlled enforcement.

Both parties agree to programmable settlement conditions before a transaction begins. Once those conditions are satisfied, Orina executes one canonical settlement outcome.

## Long Introduction

Orina Protocol is designed to solve a core weakness in digital commerce: transaction correctness is often left to platform discretion, participant trust, incentives, or loosely coordinated external workflows.

The Atomic Transaction Protocol (ATP) makes settlement a protocol-level state machine. It defines how transaction states progress, how commitments are evaluated, how disputes and timeouts resolve, and how final settlement becomes canonical.

Orina separates settlement authority from application surfaces and external workflows. Those systems may prepare inputs or present transaction context, but they do not define canonical settlement. The protocol remains the authority for final transaction outcome.

## Core Thesis

Commerce should be settlement-first. A transaction is reliable only when it has a clear, enforceable, auditable, and final outcome.

## Why Orina Exists

Today's digital commerce still depends on trusted intermediaries.

Whether trading digital assets, hiring freelancers, purchasing goods, or coordinating automated agents, both parties usually rely on centralized platforms, escrow providers, or manual dispute resolution.

These approaches increase cost, reduce transparency, and create single points of failure. Orina replaces trust with deterministic settlement rules executed directly by protocol.

## What Orina Does

Orina guarantees one canonical settlement outcome for every bilateral transaction.

Instead of relying on subjective judgment or platform-controlled enforcement, both parties agree to programmable settlement conditions before the transaction begins. Once those conditions are satisfied, settlement is executed deterministically.

## What Orina Is

- A settlement protocol for bilateral commerce.
- A deterministic state machine for transaction finality.
- An infrastructure layer that applications can integrate.
- A programmable settlement core for goods, services, assets, and machine-to-machine commerce.

## What Orina Is Not

- Not a marketplace.
- Not an escrow provider.
- Not a payment gateway.
- Not an AI assistant.
- Not a token wrapper.

## Core Principles

| Principle | Meaning |
| --- | --- |
| Deterministic Settlement | Every transaction reaches exactly one final state. |
| Trust-Minimized | Neither party needs to trust the other. |
| Programmable Conditions | Settlement logic is defined before execution. |
| Composable | Existing marketplaces, wallets, AI systems, and enterprise applications can integrate Orina. |
| Permissionless | Anyone can build on the protocol. |

## How It Works

| Step | Meaning |
| --- | --- |
| Agreement | Parties define transaction terms and settlement conditions. |
| Asset Commitment | Value, asset, or service commitment enters the settlement flow. |
| Condition Verification | Deadlines, confirmations, and dispute paths are evaluated. |
| Deterministic Settlement | The transaction resolves into one canonical outcome. |

## Applications

| Area | Examples |
| --- | --- |
| Commerce | Goods, service payments, procurement, cross-border transactions |
| Financial | OTC trading, escrow, asset exchange |
| AI Economy | AI agent commerce, autonomous payments, machine-to-machine settlement |
| Assets | Digital assets, physical assets, tokenized assets |

## Architecture Summary

ATP is the technical design behind Orina's settlement guarantees. The implementation details below explain how the protocol is currently realized, but they are not the category definition of Orina.

| Layer | Role |
| --- | --- |
| Asset representation | Creates structured on-chain asset identities and quantity state. |
| Transaction and escrow | Handles order state, escrow, payment routing, refunds, timeout logic, disputes, and final settlement. |
| Application context | Lets interfaces and delegated software prepare bounded actions under explicit constraints. |
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
| `RWAReceiptNFT` | Post-finalization ERC721 layer for non-transferable RWA receipts and transferable NFT outcomes. |
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
