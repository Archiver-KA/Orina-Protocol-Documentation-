# Security Model

---
date: 2026-05-27
status: Public documentation baseline
source_audit_dates: Contracts 2026-05-16; runtime 2026-05-14
---

This page summarizes the public security posture for Orina Protocol based on the local contract and runtime documentation reviewed on 2026-05-27.

## Contract Audit Summary

The source contract audit dated 2026-05-16 reviewed:

- `src/` Solidity contracts.
- Deployment wiring scripts.
- Existing Slither reports.
- ATP and M2M specs.
- Cutover checklist as source context only.

No confirmed Critical or High issue was reported under the ATP-specific model. The main confirmed M2M term-binding risk and low-severity hardening items were marked resolved in the local source baseline.

## Resolved Findings

| ID | Severity | Summary | Status |
| --- | --- | --- | --- |
| `M-01` | Medium | Delegated seller-confirm and buyer-pay paths did not fully bind ATP economic terms. | Resolved |
| `L-01` | Low | Referral fee could be retained in `PaymentGateway` if referral vault was zero. | Resolved |
| `L-02` | Low | Buyer dispute and auto-release overlapped at exact boundary timestamp. | Resolved |
| `L-03` | Low | `AutoTimeManager.setDisputeManager` could mislead operators about external role grants. | Resolved |

## Contract Security Properties

- Root buyer and root seller remain canonical identities.
- Delegates cannot perform dispute, cancellation, or delivery confirmation in M2M v1.
- Delegated sessions bind action, counterparty, token, price, amount, delivery bounds, expiry, and spend caps.
- Refund recipient remains root-bound.
- Seller payout recipient remains root-bound.
- Final receipt owner is tied to finalized buyer-side ownership.
- Payment gateway uses role-constrained escrow paths.
- Auto-release is separated from the buyer dispute boundary.
- Reentrancy guards are used on settlement-sensitive paths.

## Runtime Security Assumptions

- Browser-exposed `VITE_*` values may contain only public configuration.
- Supabase service-role keys, JWT secrets, delegate encryption keys, private keys, and generated API keys must stay server-side, CI-secret-side, Edge Function-side, or local-only.
- Wallet auth and Supabase bridge sessions are sensitive browser state and must be protected from same-origin XSS.
- Protected Edge Function writes must require wallet claims and wallet-address matching.
- Public marketplace browse RPCs may be readable by anonymous and authenticated users, but authorization still depends on explicit RLS and function review.
- Edge CORS should allow only approved origins in production.
- AI M2M delegate invite ids require cryptographic randomness, expiry, replay rejection, and rate limiting.
- Server-managed AI M2M delegate private keys must remain server-side only.

## Verification References

Contract source verification notes include:

- Production contract build passed with test and script folders skipped.
- Focused delegated M2M tests passed.
- Fee, dispute, auto-time, receipt, and formal-style Foundry tests passed in targeted suites.
- Delegated order identity and delegated mint invariants passed under the recorded local settings.
- Full script compile with `via_ir` timed out after 5 minutes in the source audit environment.

Runtime source verification references include:

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

## Public Reporting

The runtime source documentation did not define a dedicated public vulnerability intake address. Until one is selected, security reports should use the maintainer channel approved by the project owner and must not include raw secrets, private keys, service-role keys, JWT signing secrets, or generated API keys in issue text or logs.

## Out Of Scope For Public Docs

This page intentionally omits:

- Private deployment runbooks.
- Production migration steps.
- CI secret names and values.
- Local audit database URLs.
- Operator-only smoke-test instructions.
- Raw Slither JSON reports.
