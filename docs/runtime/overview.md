# Runtime Overview

---
date: 2026-05-27
status: Public documentation baseline
source_baseline: Runtime repository commit 67a69e7b37ccd38dc35d005355eccc9f9bf89ff0
---

Orina Protocol Runtime is the production-facing application repository for the Orina marketplace experience. It contains the React frontend, wallet flows, Supabase runtime surfaces, release checks, and current-code runtime documentation.

## Stack

- React
- TypeScript
- Vite
- Tailwind CSS
- Wagmi
- Viem
- Supabase

## Runtime Responsibilities

- Public browsing for marketplace, search, community, asset details, collection details, and profiles.
- Wallet connection and wallet-auth session handling.
- ATP order creation, seller confirmation, buyer pay/re-sign, delivery confirmation, dispute entry, and lifecycle display.
- Seller minting and RWA asset metadata capture.
- Supabase-backed public catalog, profile, community, review, geo, and projection data.
- Local wallet-scoped cache for profile, settings, delivery addresses, orders, minted assets, and runtime preferences.
- AI/M2M configuration surfaces when enabled by runtime configuration.

## Access Modes

| Mode | Trigger | User capability |
| --- | --- | --- |
| Guest disconnected | No wallet connected | Browse public surfaces. |
| Guest forced | Guest mode flag enabled | Browse public surfaces even if a wallet exists. |
| Auth pending | Wallet connected without wallet-auth session | Read broader UI surfaces while sensitive writes remain blocked. |
| User connected | Wallet connected and wallet-auth session valid | Full wallet-scoped app and protocol write actions. |

## Data Model Summary

On-chain state is canonical for:

- ATP assets.
- Orders.
- Escrow.
- Disputes.
- Receipts.
- Role-enforced protocol actions.

Supabase stores:

- Public catalog/profile/community/message/review data.
- Geo data.
- API/AI records.
- Chain projection mirrors such as `protocol_assets` and `protocol_orders`.

Local browser storage can contain:

- Wallet-scoped preferences.
- Profile cache.
- Delivery address cache.
- Order cache.
- Minted asset cache.
- Search history.
- Wallet-auth and Supabase bridge sessions.

## Repository Scripts

The runtime repository exposes common development and verification scripts:

```bash
npm install
npm run dev
npm run test
npm run typecheck
npm run lint:check
npm run security:scan
npm run security:sbom
npm run release:manifest
npm run verify:viewer-release
npm run build
```

These scripts are maintained in the runtime source repository. They are referenced here as public context, not as required commands for this documentation repo.

## Documentation Boundary

This public runtime overview omits production deployment runbooks, environment flip procedures, port-specific Chrome automation guides, Supabase migration drift reconciliation, and owner-governance procedures.
