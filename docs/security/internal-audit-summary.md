# Internal Audit Summary

---
date: 2026-05-27
status: Public internal audit summary
audit_type: Internal security review
---

Orina Protocol has completed internal security review passes across the ATP contract system and runtime application source. This document is a public summary of that internal work.

This is not an external audit certificate, legal certification, compliance approval, or bug bounty report. It should be read as an internal assurance summary based on repository evidence, targeted review, static checks, focused tests, and documented remediation.

## Review Scope

### ATP Contracts

The internal contract review covered:

- `MarketplaceATP`
- `PaymentGateway`
- `OrinaRWA`
- `RWAReceiptNFT`
- `FeeManager`
- `DisputeManager`
- `AutoTimeManager`
- `UnitRegistry`
- `ShippingRegistry`
- M2M delegation contracts, including `DelegationManager`, `AIWalletV2`, `AIWalletFactoryV2`, `IdentityValidator`, and `M2MActions`
- Formal artifacts and invariant-oriented test coverage
- Existing static-analysis outputs used as review input

Primary review themes:

- Root buyer and root seller identity preservation.
- Payer-vault separation from canonical buyer identity.
- Root-bound refund routing.
- Seller payout routing.
- Escrow release and refund paths.
- Dispute settlement behavior.
- Receipt minting boundaries.
- Time-window and auto-release boundaries.
- M2M delegated authority and spend/term constraints.

### Runtime Application

The internal runtime review covered:

- React/Vite frontend source.
- Supabase Edge Function server code.
- Supabase migrations, RPCs, and security scripts.
- Build, release, and security scripts.
- CI release gate configuration.
- Dependency metadata and lockfile state.
- Runtime security documentation.

Primary review themes:

- Client secret exposure.
- Wallet authentication and session handling.
- Supabase service-role and server-side boundary separation.
- Rate limiting.
- CORS policy.
- Dependency vulnerability posture.
- Runtime route and viewer guards.
- Release verification scripts.

## Summary Result

The internal ATP-specific contract review reported no confirmed Critical or High issue under the reviewed model.

The main confirmed contract finding was a Medium M2M delegated-term binding issue. It was remediated in the reviewed source by binding delegated use to stored ATP economic terms such as payment token, asset id, asset amount, gross price, counterparty, and delivery bounds.

Low-severity contract hardening items were also remediated in the reviewed source:

| ID | Severity | Summary | Status |
| --- | --- | --- | --- |
| `M-01` | Medium | Delegated seller-confirm and buyer-pay paths needed stronger ATP economic term binding. | Resolved in reviewed source |
| `L-01` | Low | Referral fee handling needed a stronger zero-vault guard. | Resolved in reviewed source |
| `L-02` | Low | Buyer dispute and auto-release overlapped at the exact boundary timestamp. | Resolved in reviewed source |
| `L-03` | Low | Dispute manager rotation semantics needed clearer role-boundary handling. | Resolved in reviewed source |

The runtime review fixed or verified hardening across:

| Area | Result |
| --- | --- |
| DOM style injection hardening | Fixed |
| Dependency vulnerabilities | Fixed and rechecked |
| SECURITY DEFINER audit drift | Fixed |
| Rate-limit race condition | Fixed |
| CORS wildcard response handling | Hardened |
| Documentation gaps and stale security guidance | Updated |
| Client secret scan | Checked |
| Release viewer verification | Passed in recorded internal review |

## Verification Evidence

Contract verification references from the internal review include:

- Production contract build passed with test and script folders skipped.
- Focused delegated M2M tests passed.
- Fee, dispute, auto-time, receipt, and formal-style Foundry tests passed in targeted suites.
- Delegated order identity and delegated mint invariants passed under recorded review settings.

Runtime verification references from the internal review include:

- `npm run security:check-client-secrets`
- `npm run security:scan`
- `npm run security:sbom`
- `npm run release:manifest`
- `npm run audit:supabase:data-api-grants`
- `npm run audit:supabase:security-definer`
- `npm run typecheck`
- `npm run lint:check`
- `npm run verify:assurance-invariants`
- `npm run verify:deterministic-build`
- `npm run verify:viewer-release`

## Current Public Posture

- Internal review has been completed for the documented ATP contract and runtime source baseline.
- Public documentation includes formal artifacts, bytecode hashes, contract responsibilities, runtime references, and security assumptions.
- The project should not be represented as externally audited unless an independent third-party report is published.
- Public vulnerability intake remains an owner decision until a dedicated reporting address or process is published.

## Related Documents

- [Security Model](./security-model.md)
- [Formal Verification](../formal/formal-verification.md)
- [Formal Bytecode](../formal/bytecode.md)
- [Runtime App](../runtime/live-app.md)
