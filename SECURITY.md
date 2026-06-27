# Security Policy

---
date: 2026-06-27
status: Public repository policy
---

This repository contains public documentation and formal artifacts for Orina Protocol. It must not contain private keys, service-role keys, JWT signing secrets, generated API keys, raw `.env` files, private RPC URLs, local audit database URLs, or operator-only deployment logs.

## Reporting

No dedicated public vulnerability intake address has been selected yet. Until the project owner publishes one, report security issues through the maintainer channel approved for this repository.

Do not include secrets, private keys, service-role keys, JWT signing secrets, generated API keys, or exploitable private infrastructure details in public issues, pull requests, comments, or logs.

## Scope

In scope for this documentation repository:

- Public documentation correctness issues that could mislead users about security-sensitive behavior.
- Accidental publication of sensitive material.
- Incorrect formal artifact hashes or bytecode metadata.
- Broken security references that affect public verification.

Out of scope for this documentation repository:

- Private deployment procedures.
- Operator runbooks.
- Production infrastructure configuration.
- Requests for private keys, secrets, or live credentials.

## Source Security Model

See [Security Model](./docs/security/security-model.md) for the public contract and runtime security assumptions, [Security Status](./docs/security/security-status-2026-06-27.md) for the current internal assurance status, and [Mainnet Production Checklist](./docs/security/mainnet-production-checklist.md) for production-readiness gates.
