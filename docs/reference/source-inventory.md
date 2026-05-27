# Source Inventory

---
date: 2026-05-27
status: Public curation manifest
---

## Source Repositories

### ATP Contracts

- Local path: `C:\ORINA\ATPProtocol2\ATP2\foundry`
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

- Local path: `C:\ORINA\ATPProtocol2\Orina Protocol - Runtime`
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

## Artifact Manifest

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `artifacts/formal/atp/atl/MarketplaceATP_ATL.strategy` | 1322 | `3CAC52D5413CADC6F2030CEC3BFFE8CA8053FED60B64D23A9DB3C4662166AC9C` |
| `artifacts/formal/atp/ctl/MarketplaceATP_CTL.spec` | 1704 | `1F4DE6D4C49A18807965AD0E5F2DDF1833140FE8A208EA6BB94A92C4B6C864E3` |
| `artifacts/formal/atp/evm/MarketplaceATP.creation.bytecode.hex` | 53098 | `13F50B42E9FE19854C62D9EC8FCB6AB5F12F0007B358DBF8036D189917C586BD` |
| `artifacts/formal/atp/evm/MarketplaceATP.runtime.bytecode.hex` | 48964 | `B3D45B8AF0973E63F4C008B37C681EDA6D269F654C740A5C50D34D4B368029B4` |
| `artifacts/formal/atp/ltl/MarketplaceATP_LTL.spec` | 2025 | `EB1FCF22181410D6A0922A60C7C5143714CCA59A9D8BF3E09198304E3910F221` |
| `artifacts/formal/atp/nusmv/MarketplaceATP_ExecutableModel.smv` | 9741 | `2E5F97BE18533A9FB69E20AEF4CF240FEA5FDA3F759627960068818E491C4F04` |

## Notes

The source Foundry workspace contains a malformed `.gitignore` glob in the parent path that can make `rg` emit parsing warnings unless run with `--no-ignore`. The public documentation repository does not copy that ignore file.
