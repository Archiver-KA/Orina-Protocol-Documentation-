# Mainnet Production Checklist

---
date: 2026-06-27
status: Pre-mainnet checklist
---

This checklist is the public production-readiness summary. It intentionally excludes private operator commands, secrets, RPC URLs, and testnet faucet assumptions.

## Security Gates

- Full Foundry suite passes from a clean build.
- Deep invariants, Echidna, Medusa, Slither, Mythril, and 4naly3er outputs are current and triaged.
- Certora or comparable formal coverage extends beyond `FeeManager` to core settlement and delegation contracts.
- Human review or independent audit covers business logic, governance assumptions, dispute policy, oracle assumptions, delegated sessions, and operational abuse paths.
- Accepted residual risks are explicitly signed off by protocol owner/governance.

## Governance And Keys

- Production governance safe exists on target chain with the intended threshold.
- Timelock delay and role assignments are documented.
- Deployer EOAs do not retain unexpected admin/governance roles.
- Arbiter, emergency, treasury/vault, and M2M admin roles are held by approved governance actors.
- Private keys, Certora keys, explorer keys, RPC URLs, service-role keys, and JWT secrets are stored only outside the repository.

## Economic Policy

- Production payment-token allowlist is final.
- Fee caps, vaults, referral policy, and DAO/platform split are confirmed.
- ORI separate fee-token mode has an approved quote/oracle design before launch.
- Non-standard ERC20s are excluded unless their behavior is explicitly accepted and monitored.

## Deployment And Operations

- Mainnet chain id, compiler version, optimizer settings, deployment scripts, and namespace are frozen.
- Broadcast artifacts and constructor arguments are archived.
- Contract verification is complete.
- On-chain wiring and roles are read back after deployment.
- Frontend, backend, indexer, docs, and deployment artifacts agree.
- Production smoke covers order, payment, delivery, dispute, auto-time, M2M, receipt, and event-indexing flows.
- Monitoring and incident runbooks are live.

## No-Go Conditions

- Untriaged High/Medium security finding.
- Human review missing.
- Testnet faucet token in production env.
- Deployer EOA retains unexpected production admin authority.
- ORI separate fee mode enabled without quote/oracle policy.
- Docs, app config, backend config, and broadcast artifacts disagree.
