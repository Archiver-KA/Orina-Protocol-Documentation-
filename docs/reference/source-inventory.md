# Source Inventory

---
date: 2026-06-03
status: Public curation manifest
---

## License Scope

This inventory records provenance for public documentation material. It is not a license grant for upstream source repositories.

Repository license scope:

- Public documentation text, diagrams, public security summaries, and public formal specification materials: `CC-BY-4.0 OR Apache-2.0`.
- Code snippets and command examples in this repository: `MIT OR Apache-2.0`.
- Exported EVM bytecode and bytecode hashes: verification-only publication; no deployment or commercialization license implied.
- Orina brand assets: reserved.

See [License](../../LICENSE.md) and [Notice](../../NOTICE.md) for controlling terms.

## Source Repositories

### ATP Contracts

- Git branch: `main`
- Git commit: `be466831ff367a7891b32b61e6541dc294b2f066`
- Remotes:
  - `origin`: `https://github.com/Archiver-KA/contract-atp-protocol.git`
  - `atp-protocol`: `https://github.com/Archiver-KA/ATP-Protocol.git`

Public material used:

- `README.md`
- `CONTRACT_SYSTEM_SPEC.md`
- `ATP_SECURITY_AUDIT_2026-05-16.md`
- `formal/atp/README.md`
- `formal/atp/ATP_Formal_Verification_Checklist.md`
- `formal/atp/ATP_Findings_Audit_Mapping.md`
- `ai_wallet/AI_WALLET_DOCS_INDEX.md`
- `ai_wallet/AI_WALLET_THREAT_MODEL.md`
- `ai_wallet/AI_WALLET_INVARIANTS.md`
- `ai_wallet/AI_WALLET_FORMAL_PROPERTY_MATRIX.md`
- `src/*.sol`
- `src/m2m/*.sol`
- `formal/atp/{atl,ctl,evm,ltl,nusmv}`

Material excluded from public docs:

- `.env`
- `.audit-venv`
- `cache`
- `broadcast`
- `out` except the curated bytecode exported under `formal/atp/evm`
- `slither-*.json`
- `CUTOVER_CHECKLIST.md`
- deployment scripts as operator documentation
- tests and smoke scripts as operational procedures
- archived legacy contracts except where mentioned as not active

### Runtime Application

- Git branch: `main`
- Git commit: `67a69e7b37ccd38dc35d005355eccc9f9bf89ff0`
- Remotes:
  - `origin`: `https://github.com/Archiver-KA/Orina-Protocol-Runtime`
  - `origin-app`: `https://github.com/Archiver-KA/Orina-Protocol-App`

Public material used:

- `README.md`
- `SECURITY.md`
- `docs/README.md`
- `docs/system-user-guide.md`
- `docs/system-faq.md`
- `docs/order-state-semantics.md`
- `docs/release-provenance.md`
- `package.json`
- Current ATP v3.4.1 runtime verification notes
- Runtime internal audit report

Material excluded from public docs:

- `.env`
- `.env.*`
- `node_modules`
- `dist`
- `.wrangler`
- `temp`
- local Vite logs
- `docs/spec/*`
- runtime/deploy runbooks
- governance owner-decision documents
- port-specific operator verification guides
- Supabase migration drift and production deployment procedures
- future runtime migration material

### Project Profile And Whitepaper Sources

Whitepaper repository:

- Git commit: `208b8f66de55c979fe387c39fc714e77963cdb28`
- Remote:
  - `origin`: `https://github.com/Archiver-KA/WhitepaperOrinaio.git`

Public material used:

- `ORINA_WHITEPAPER_v2.md`
- `src/app/pages/DAOPage.tsx`
- `src/app/pages/TokenomicsPage.tsx`

Additional owner-provided project profile sources:

- `SocialNetwork.md`
- `Orina_Protocol_Spec.md`

Material excluded from public docs:

- Content prompt packs.
- Internal editorial prompts.
- Confidential labels and internal source paths.
- Investor-only or owner-decision planning notes.

## Artifact Manifest

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `artifacts/formal/atp/atl/MarketplaceATP_ATL.strategy` | 1322 | `3CAC52D5413CADC6F2030CEC3BFFE8CA8053FED60B64D23A9DB3C4662166AC9C` |
| `artifacts/formal/atp/ctl/MarketplaceATP_CTL.spec` | 1704 | `1F4DE6D4C49A18807965AD0E5F2DDF1833140FE8A208EA6BB94A92C4B6C864E3` |
| `artifacts/formal/atp/evm/MarketplaceATP.creation.bytecode.hex` | 53098 | `13F50B42E9FE19854C62D9EC8FCB6AB5F12F0007B358DBF8036D189917C586BD` |
| `artifacts/formal/atp/evm/MarketplaceATP.runtime.bytecode.hex` | 48964 | `B3D45B8AF0973E63F4C008B37C681EDA6D269F654C740A5C50D34D4B368029B4` |
| `artifacts/formal/atp/ltl/MarketplaceATP_LTL.spec` | 2025 | `EB1FCF22181410D6A0922A60C7C5143714CCA59A9D8BF3E09198304E3910F221` |
| `artifacts/formal/atp/nusmv/MarketplaceATP_ExecutableModel.smv` | 9741 | `2E5F97BE18533A9FB69E20AEF4CF240FEA5FDA3F759627960068818E491C4F04` |
| `assets/images/orina-banner-github.jpg` | 121528 | `8A057049E1D3058C36EEF94AA35021433EBD1FFA10BDB1386F4821924C385260` |
