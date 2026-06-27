# Security Status

---
date: 2026-06-27
status: Public internal security status
---

This document summarizes the current public security posture for the Orina ATP protocol stack. It is not an external audit certificate, legal certification, compliance approval, or mainnet launch approval.

## Current Automated Baseline

- Foundry build and the current full protocol test suite pass; the latest dispute hardening pass records 110/110 passing tests.
- Deep Foundry invariant campaigns pass for the current ATP accounting and state harnesses.
- Slither triage has no High or Medium impact findings in the current result set.
- Echidna and Medusa pass against the ATP harness covering escrow conservation, asset conservation, tracked order terminality, and delegated identity properties.
- Mythril runtime-bytecode analysis completed for `FeeManager`, `PaymentGateway`, and `MarketplaceATP`; source triage found no confirmed exploitable issue.
- Certora remote proof passes for the initial `FeeManager` fee-cap scope.
- BSC Testnet and Base Sepolia deployments are reconciled and spot-checked for bytecode plus Marketplace-to-DelegationManager wiring.

## Manual Review Updates

Batch external calls in `AutoTimeManager.batchCheckAndExecute` are treated as a keeper/liveness risk, not a confirmed fund-loss path. The manager holds no funds, is non-reentrant, caps batch size, and calls only configured Marketplace/Governance paths.

Dispute settlement was hardened so dispute state is closed before downstream gateway and Marketplace calls. The dispute resolve paths are non-reentrant, and regression coverage verifies the dispute is inactive during gateway callback execution.

## Remaining Limits

- Broader Certora coverage is pending for Marketplace, Gateway, Dispute, Delegation, and AI wallet contracts.
- Halmos remains a tooling/harness limitation rather than a completed proof.
- 4naly3er Medium/Low/non-critical results still need final triage.
- Human review and/or independent audit are required before production claims.
- Production requires a token allowlist, ORI quote/oracle policy, governance handoff, monitoring, and incident runbooks.

## Public Communication Boundary

The project may be described as internally reviewed and testnet-operated. Do not describe it as externally audited, mainnet certified, or production approved unless a separate third-party report or governance sign-off is published.
