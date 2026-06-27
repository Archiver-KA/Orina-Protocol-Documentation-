<!--
date: 2026-06-04
status: Public documentation baseline
source_status: Curated from Orina protocol, runtime, profile, and whitepaper sources
-->

# Orina Protocol

![Orina Protocol banner](./assets/images/orina-banner-github.jpg)

**The settlement layer for bilateral commerce.**

Orina is a decentralized settlement protocol that enables any two independent parties to complete transactions without relying on trust, intermediaries, or platform-controlled enforcement.

Orina guarantees one canonical settlement outcome for every bilateral transaction. Parties agree to programmable settlement conditions before execution begins; once those conditions are satisfied, settlement executes deterministically.

## Official Links

| Channel | Link |
| --- | --- |
| Website | https://www.orina.io/ |
| Runtime app | https://app.orina.io/ |
| Blog | https://orina.io/blog |
| Whitepaper | https://whitepaper.orina.io/ |
| X / Twitter | https://x.com/Orina_official |
| Discord | https://discord.gg/vythc6X9qF |
| GitHub | https://github.com/Archiver-KA/Orina-Protocol-Documentation- |
| Telegram official | https://t.me/orinaofficial |
| Telegram global | https://t.me/orinaglobal |
| Email | info@orina.io |

## Why Orina Exists

Digital commerce still depends on trusted intermediaries. Whether parties are exchanging assets, paying for services, purchasing goods, or coordinating automated systems, settlement often depends on centralized platforms, escrow providers, or manual dispute resolution.

These approaches increase cost, reduce transparency, and create single points of failure. Orina replaces trust with deterministic settlement rules executed directly by protocol.

## What Orina Does

Orina standardizes the settlement path for bilateral transactions:

- Agreement: both parties accept programmable settlement conditions before execution.
- Asset commitment: the transaction value or deliverable is committed to the flow.
- Condition verification: agreed conditions, deadlines, and dispute paths are evaluated.
- Deterministic settlement: the transaction reaches exactly one canonical final outcome.

## Core Principles

- Deterministic Settlement: every transaction reaches exactly one final state.
- Trust-Minimized: neither party needs to trust the other.
- Programmable Conditions: settlement logic is defined before execution.
- Composable: marketplaces, wallets, AI systems, and enterprise applications can integrate Orina.
- Permissionless: anyone can build on the protocol.

## Where Orina Can Be Used

| Area | Examples |
| --- | --- |
| Commerce | Goods, service payments, procurement, cross-border transactions |
| Financial | OTC trading, escrow, asset exchange |
| AI Economy | AI agent commerce, autonomous payments, machine-to-machine settlement |
| Assets | Digital assets, physical assets, tokenized assets |

## What Orina Is Not

Orina is not a marketplace, escrow provider, or payment gateway. It is a settlement protocol that marketplaces, AI agents, wallets, and commerce platforms can integrate as infrastructure.

## Documentation

| Area | Start here |
| --- | --- |
| Project profile | [Project Profile](./docs/project/profile.md) |
| Tokenomics | [ORI Tokenomics](./docs/project/tokenomics.md) |
| Docs hub | [Docs Hub](./docs/README.md) |
| Protocol | [Protocol Overview](./docs/protocol/overview.md) |
| Contracts | [Contract System](./docs/protocol/contract-system.md) |
| DAO fee governance | [DAO Fee Governance](./docs/protocol/dao-fee-governance.md) |
| Order lifecycle | [Order Lifecycle](./docs/protocol/order-lifecycle.md) |
| M2M delegation | [M2M Delegation](./docs/protocol/m2m-delegation.md) |
| Runtime | [Runtime Overview](./docs/runtime/overview.md) |
| Live runtime app | [Runtime App](./docs/runtime/live-app.md) |
| Security | [Security Model](./docs/security/security-model.md) |
| Internal audit | [Internal Audit Summary](./docs/security/internal-audit-summary.md) |
| Security status | [Security Status](./docs/security/security-status-2026-06-27.md) |
| Testnet addresses | [Testnet Deployment Addresses](./docs/runtime/testnet-deployment-addresses.md) |
| Mainnet checklist | [Mainnet Production Checklist](./docs/security/mainnet-production-checklist.md) |
| Formal methods | [Formal Verification](./docs/formal/formal-verification.md) |
| Bytecode | [Formal Bytecode](./docs/formal/bytecode.md) |
| Glossary | [Glossary](./docs/reference/glossary.md) |
| Official links | [Official Links](./docs/reference/official-links.md) |

## Formal Artifacts

Curated ATP formal artifacts are stored under [artifacts/formal/atp](./artifacts/formal/atp/README.md):

- NuSMV executable abstraction.
- CTL, LTL, and ATL specifications.
- `MarketplaceATP` creation and runtime bytecode exports.

The bytecode files are documented with SHA-256 hashes in [Formal Bytecode](./docs/formal/bytecode.md).

## Security And Audit

The ATP contract system and runtime application have completed internal security review passes. See [Internal Audit Summary](./docs/security/internal-audit-summary.md) and [Security Status](./docs/security/security-status-2026-06-27.md) for scope, results, verification references, and limitations.

This is an internal audit summary, not an external audit certificate.

## Public Scope

Included:

- Project profile and official social links.
- Basic protocol and runtime documentation.
- Public runtime app reference for ATP v3.5 beta.
- Contract responsibilities and invariants.
- Public security posture and verification summaries.
- Formal model/specification references.
- Formal bytecode artifacts and hashes.

Excluded:

- Deployment runbooks and operator checklists.
- Production environment flip plans.
- Internal planning documents.
- Future runtime migration material.
- Operator-only verification scripts and smoke-test procedures.
- `.env`, secrets, keys, logs, caches, `node_modules`, and build output.
- Internal backlog, local archive, and owner-decision workflow notes.

## ORI Token Snapshot

| Field | Value |
| --- | --- |
| Token name | ORINA |
| Token symbol | ORI |
| Chain | BNB Smart Chain |
| Standard | BEP-20 |
| Decimals | 18 |
| Total supply | 1,000,000,000 ORI |
| Contract | [`0x093969C2Bb194e7424534918ECa5119FA72a61d6`](https://bscscan.com/token/0x093969c2bb194e7424534918eca5119fa72a61d6) |

ORI is a protocol coordination token used around ecosystem access, fees, participation, and future governance functions. ORI does not replace ATP and does not define transaction correctness; ATP is the settlement logic.

See [DAO Fee Governance](./docs/protocol/dao-fee-governance.md) for the Hybrid DAO fee model: 1% ORI fee-token path, 2% supported stablecoin fee-token path, no protocol burn, a 50% platform / 50% DAO ecosystem allocation target, and securities-law boundary language for DAO programs.

See [ORI Tokenomics](./docs/project/tokenomics.md) for public token supply, allocation, vesting, fee-alignment, and reference valuation formulas.

## Repository Policy

- [License](./LICENSE.md)
- [Notice](./NOTICE.md)
- [Security Policy](./SECURITY.md)
- [Contributing](./CONTRIBUTING.md)
- [Source Inventory](./docs/reference/source-inventory.md)

## License

This documentation repository uses scoped licensing:

- Public documentation text, diagrams, public security summaries, and public formal specification materials: dual-licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) or [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`CC-BY-4.0 OR Apache-2.0`).
- Code snippets and command examples: MIT License or Apache License 2.0 (`MIT OR Apache-2.0`).
- Exported EVM bytecode and bytecode hashes: published for verification and reproducibility only; no deployment or commercialization license is implied.
- Orina brand assets: reserved.

See [LICENSE.md](./LICENSE.md) and [NOTICE.md](./NOTICE.md) for the controlling terms and attribution guidance.
