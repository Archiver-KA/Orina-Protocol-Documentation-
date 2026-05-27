<!--
date: 2026-05-27
status: Public documentation baseline
source_status: Curated from Orina protocol, runtime, profile, and whitepaper sources
-->

# Orina Protocol

![Orina Protocol banner](./assets/images/orina-banner-github.jpg)

**Deterministic settlement infrastructure for real-world asset commerce and autonomous transactions.**

Orina Protocol is a settlement-first infrastructure layer for real-world asset commerce. Its Atomic Transaction Protocol (ATP) defines escrow-backed transaction lifecycles, explicit state transitions, timeout paths, dispute handling, and canonical final settlement.

AI and automation may assist sourcing, evaluation, and execution, but they do not define settlement. ATP remains the authority for escrow release, refunds, receipt minting, and final transaction state.

## Official Links

| Channel | Link |
| --- | --- |
| Website | https://www.orina.io/ |
| Runtime app | https://app.orina.io/ |
| Blog | https://orina.io/blog |
| Whitepaper | https://whitepaper.orina.io/ |
| X / Twitter | https://x.com/Orina_io |
| Discord | https://discord.gg/vythc6X9qF |
| Telegram official | https://t.me/orinaofficial |
| Telegram global | https://t.me/orinaglobal |
| Email | info@orina.io |

## What Orina Provides

- Deterministic ATP settlement for RWA commerce.
- Per-order escrow, timeout, dispute, refund, and finalization logic.
- Asset quantity locking and post-settlement receipt minting.
- Formal artifacts for lifecycle and delegated authority checks.
- Bounded M2M delegation for autonomous commerce without making AI the authority.
- Runtime documentation for the public marketplace application and wallet flows.

## Documentation

| Area | Start here |
| --- | --- |
| Project profile | [Project Profile](./docs/project/profile.md) |
| Docs hub | [Docs Hub](./docs/README.md) |
| Protocol | [Protocol Overview](./docs/protocol/overview.md) |
| Contracts | [Contract System](./docs/protocol/contract-system.md) |
| Order lifecycle | [Order Lifecycle](./docs/protocol/order-lifecycle.md) |
| M2M delegation | [M2M Delegation](./docs/protocol/m2m-delegation.md) |
| Runtime | [Runtime Overview](./docs/runtime/overview.md) |
| Live runtime app | [Runtime App](./docs/runtime/live-app.md) |
| Security | [Security Model](./docs/security/security-model.md) |
| Internal audit | [Internal Audit Summary](./docs/security/internal-audit-summary.md) |
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

The ATP contract system and runtime application have completed internal security review passes. See [Internal Audit Summary](./docs/security/internal-audit-summary.md) for scope, results, verification references, and limitations.

This is an internal audit summary, not an external audit certificate.

## Public Scope

Included:

- Project profile and official social links.
- Basic protocol and runtime documentation.
- Public runtime app reference for ATP v3.4.1.
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

## Repository Policy

- [Security Policy](./SECURITY.md)
- [Contributing](./CONTRIBUTING.md)
- [Source Inventory](./docs/reference/source-inventory.md)

## License

No public documentation license was selected in the source repositories. Treat license selection as an owner decision before broad publication or third-party contribution intake.
