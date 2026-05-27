# Orina Protocol Documentation

---
date: 2026-05-27
status: Public documentation baseline
source_status: Curated from local protocol and runtime repositories
---

Public documentation for Orina Protocol and the ATP contract/runtime stack.

This repository is intentionally documentation-only. It summarizes the protocol, contract system, runtime application, security model, formal verification artifacts, and public bytecode references without publishing operational runbooks, private environment material, deployment checklists, logs, or local build output.

## Documentation

- [Docs Hub](./docs/README.md)
- [Protocol Overview](./docs/protocol/overview.md)
- [Contract System](./docs/protocol/contract-system.md)
- [Order Lifecycle](./docs/protocol/order-lifecycle.md)
- [M2M Delegation](./docs/protocol/m2m-delegation.md)
- [Runtime Overview](./docs/runtime/overview.md)
- [Runtime User Guide](./docs/runtime/user-guide.md)
- [Security Model](./docs/security/security-model.md)
- [Formal Verification](./docs/formal/formal-verification.md)
- [Formal Bytecode](./docs/formal/bytecode.md)
- [Glossary](./docs/reference/glossary.md)
- [Security Policy](./SECURITY.md)
- [Contributing](./CONTRIBUTING.md)
- [Source Inventory](./docs/reference/source-inventory.md)

## Formal Artifacts

Curated formal artifacts are stored under [artifacts/formal/atp](./artifacts/formal/atp/README.md):

- NuSMV executable abstraction
- CTL, LTL, and ATL specifications
- `MarketplaceATP` creation and runtime bytecode exports

The bytecode files were copied from the local Foundry workspace and are documented with SHA-256 hashes in [Formal Bytecode](./docs/formal/bytecode.md).

## Public Scope

Included:

- Basic protocol and runtime documentation
- Contract responsibilities and invariants
- Public security posture and verification summaries
- Formal model/specification references
- Formal bytecode artifacts and hashes

Excluded:

- Deployment runbooks and cutover checklists
- Production environment flip plans
- Internal planning documents
- Operator-only verification scripts and smoke-test procedures
- `.env`, secrets, keys, logs, caches, `node_modules`, and build output
- Internal backlog, local archive, and owner-decision workflow notes

## Source Baseline

This documentation was curated on 2026-05-27 from:

- `C:\ORINA\ATPProtocol2\ATP2\foundry`
- `C:\ORINA\ATPProtocol2\Orina Protocol - Runtime`

See [Source Inventory](./docs/reference/source-inventory.md) for commit references and inclusion decisions.

## License

No public documentation license was selected in the source repositories. Treat license selection as an owner decision before broad publication or third-party contribution intake.
