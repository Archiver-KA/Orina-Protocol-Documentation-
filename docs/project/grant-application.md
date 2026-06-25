# Orina Protocol: Grant Application
## A Trustless Bilateral Settlement Layer for Any Two-Party Commerce

**Version:** 3.0.0
**Document Type:** General Grant Application
**Protocol Baseline:** ATP v3.5 / MarketplaceATP EIP-712 v3.4
**Status:** Ready for Submission

---

## 1. Project Overview

**Project Name:** Orina Protocol
**Category:** DeFi Infrastructure / Settlement Layer / AI-Native Commerce
**Stage:** Deployed on BSC — Expanding to EVM Ecosystem

Orina Protocol is a **trustless, asset-agnostic bilateral settlement layer** — a composable escrow primitive that enforces structured transaction lifecycles between any two parties, regardless of what they are exchanging.

The protocol does not prescribe what is being traded. It enforces *how* trades settle: with cryptographic escrow, explicit state transitions, time-bound commitments, on-chain dispute resolution, and bounded AI agent delegation. Whether the underlying transaction is an OTC crypto trade, a freelance service agreement, a digital goods delivery, or an autonomous AI agent purchase — Orina provides the same settlement guarantees.

This positioning matters. Orina is not a vertical application for a specific asset class. It is **infrastructure**: a settlement primitive that any marketplace, OTC desk, AI agent system, or two-party application can integrate without rebuilding escrow logic from scratch.

---

## 2. Problem Statement

### The Missing Settlement Primitive

Blockchain has robust infrastructure for token issuance, liquidity provision, lending, and derivatives. What it lacks is a **general-purpose, trustless settlement layer for bilateral commerce** — a primitive that answers the fundamental question every two-party trade faces:

> *How do we ensure both sides fulfill their commitment without trusting each other or a third party?*

This gap manifests across multiple markets today:

**OTC Trading** — billions in daily crypto OTC volume settled through centralized desks, Telegram agreements, and reputation systems. Counterparty risk is managed by trust, not by code. A single failed settlement can wipe out significant capital with no recourse.

**Service Commerce** — freelance platforms extract 10–20% fees precisely because they are the trusted settlement intermediary. The fee is not for matching — it's for enforcement. A trustless settlement layer eliminates the enforcement cost.

**AI Agent Commerce** — autonomous AI systems are beginning to participate in digital marketplaces. They need to create orders, make payments, and manage positions programmatically. No existing protocol provides the cryptographic session binding, spending-cap enforcement, and root-identity preservation required for safe, auditable AI agent commerce.

**Cross-border P2P** — international peer-to-peer transactions have no neutral settlement layer. Traditional escrow requires jurisdiction, legal identity, and banking access. On-chain settlement requires none of these.

### Why Existing Solutions Fall Short

- **Centralized escrow services** — custodial risk, KYC requirements, single jurisdiction, high fees (2–5%)
- **Simple smart contract escrow** — no dispute resolution, no timeout handling, no AI agent support, no structured lifecycle
- **RWA-specific protocols** — vertically scoped, require asset tokenization as a precondition, not composable as general infrastructure

---

## 3. Solution: The ATP Settlement Layer

### 3.1. Core Design Philosophy

Orina's Atomic Transaction Protocol (ATP) is designed around one principle: **the protocol enforces the lifecycle, not the asset.** `MarketplaceATP` stores `paymentToken`, `assetId`, `grossPrice`, and `amount` — it does not care whether `assetId` represents a tokenized property right, an OTC trade reference, a service agreement hash, or an AI agent purchase order. The settlement logic is identical.

This makes Orina genuinely composable. Any application that needs trustless two-party settlement can integrate ATP without modification.

### 3.2. The Contract System

ATP is implemented as a formally verified Solidity contract system (`0.8.24`, Foundry, `via_ir`, `evm_version: cancun`):

**Core Settlement Layer:**

| Contract | Responsibility |
|---|---|
| `MarketplaceATP` | Order state machine, EIP-712 domain, direct and delegated settlement actions |
| `PaymentGateway` | ERC-20 escrow, seller release, buyer refund, fee distribution |
| `OrinaRWA` | Asset supply tracking for sellers (optional — not required for all use cases) |
| `RWAReceiptNFT` | Non-transferable proof-of-settlement NFT for finalized orders |
| `FeeManager` | Fee schedules and token-specific presets |
| `DisputeManager` | Dispute lifecycle: arbiter verdict, agreement, mutual split, stale auto-split |
| `AutoTimeManager` | Permissionless timeout execution across all lifecycle windows |
| `UnitRegistry` | Amount granularity and unit validation |
| `ShippingRegistry` | Delivery option registry and timing bounds |

**M2M Delegation Layer:**

| Contract | Responsibility |
|---|---|
| `DelegationManager` | Session authority, action masks, spend caps, counterparty binding, revocation |
| `AIWalletV2` | Exact-approval payer vault for delegated execution |
| `AIWalletFactoryV2` | Deterministic AI wallet prediction and deployment |
| `IdentityValidator` | EOA and ERC-1271 root signature validation |
| `M2MActions` | Delegated action bit namespace |

### 3.3. Settlement Lifecycle

Every order moves through a deterministic, time-bound state machine with no stuck states:

```
createOrder → [PENDING_CONFIRM] → sellerConfirm → [PAID] → delivery → [terminal]
                    │                   │                        │
               24h timeout         Revised terms          ┌──────┴──────┐
               (auto-cancel)       → buyer 24h        Buyer        Dispute
                                   re-sign window     Confirms     (14 days →
                                                                   auto-split)
                                                          │
                                                    Auto-release
                                                    (3 days after
                                                    delivery window)
```

**On-chain timing constants:**

| Window | Duration | Default Outcome if Missed |
|---|---|---|
| Seller confirmation | 24 hours | Auto-cancel, full refund |
| Buyer re-sign | 24 hours | Auto-cancel, full refund |
| Buyer action after delivery | 3 days | Auto-release to seller |
| Dispute resolution | 14 days | Auto-split |

### 3.4. Dispute Resolution

`DisputeManager` supports four resolution paths covering the full range of real-world dispute outcomes:

- **Arbiter verdict** — designated arbiter issues `FULL_RELEASE`, `FULL_REFUND`, or `SPLIT`
- **Signed agreement** — both parties reach out-of-band agreement and submit jointly
- **Mutual split** — both parties agree on a percentage split on-chain
- **Stale auto-split** — after 14 days without resolution, protocol executes automatic split

No dispute is permanently unresolved. Every path has a defined terminal state.

### 3.5. M2M Delegation — AI-Native Commerce

The M2M delegation layer is Orina's most strategically differentiated feature. It enables AI agents and automated systems to execute orders on behalf of root users — without the agent becoming a protocol party or gaining custody of funds.

**Session binding parameters:**

| Parameter | Purpose |
|---|---|
| Root identity | Canonical buyer/seller — never changes |
| Delegate address | Authorized operator — not the party |
| Payer vault (`AIWalletV2`) | Funds execution without becoming buyer |
| Action mask | Bitfield of permitted actions |
| Per-order spend cap | Maximum per transaction |
| Total spend cap | Lifetime limit across all orders |
| Counterparty binding | Restricts delegate to specific sellers |
| Validity window | Time-bounded or no-expiry with counterparty binding |
| Asset and price bounds | Min/max constraints per session |

**V1 delegated actions:** `createOrderFor`, `payOrderFor`, `mintAssetFor`, `sellerConfirmFor`

**Explicitly excluded from delegation:** `confirmDelivery`, `openDispute`, `cancelByBuyer`, `cancelBySeller` — root direct-action paths always remain available.

This design makes Orina the only escrow protocol with production-grade, cryptographically bounded AI agent delegation where root identity is preserved throughout.

### 3.6. Fee Model

| Settlement Asset | Protocol Fee | Cap |
|---|---|---|
| Stablecoins (USDC, USDT) | 2% (200 bps) | Max total 7% (700 bps) |
| `$ORI` token | 1% (100 bps) | Max referral 2% (200 bps) |

Fees distribute to platform, DAO, and referral components via `PaymentGateway` and `FeeManager`. Fee schedules are governance-configurable within hard-coded maximums.

---

## 4. Target Markets

The asset-agnostic design opens Orina to multiple markets immediately — without protocol modification:

| Market | Current Settlement Method | Orina Advantage |
|---|---|---|
| **Crypto OTC trading** | Centralized OTC desks, Telegram trust | Trustless, non-custodial, auditable |
| **Freelance & service commerce** | Platform intermediaries (10–20% fee) | Protocol fee 1–2%, no platform custodian |
| **Digital goods** | Payment processors, platform refund policies | Delivery-gated release, dispute path |
| **AI agent commerce** | None — unsolved problem | Native M2M delegation with spend caps |
| **Cross-border P2P** | Wire transfer, hawala, informal trust | On-chain finality, no banking required |
| **Any bilateral deal** | Varies — often no trustless option | Composable primitive for any integrator |

Each of these markets can be addressed by Orina as deployed today — no new asset tokenization required, no additional infrastructure prerequisites.

---

## 5. Security & Formal Verification

### 5.1. Internal Audit (May 2026)

| Finding | Severity | Description | Status |
|---|---|---|---|
| M-01 | Medium | Delegated seller-confirm and buyer-pay paths did not fully bind ATP economic terms | ✅ Resolved |
| L-01 | Low | Referral fee retained in `PaymentGateway` if referral vault was zero address | ✅ Resolved |
| L-02 | Low | Buyer dispute and auto-release overlapped at exact boundary timestamp | ✅ Resolved |
| L-03 | Low | `AutoTimeManager.setDisputeManager` could mislead operators about external role grants | ✅ Resolved |

**No confirmed Critical or High findings.** All findings resolved before public baseline.

### 5.2. Formal Verification Artifacts (Published)

Available at `artifacts/formal/atp/` in the public documentation repository:

- NuSMV executable abstraction of the ATP state machine
- CTL, LTL, and ATL temporal logic specifications
- `MarketplaceATP` creation and runtime bytecode with SHA-256 hashes
- Foundry formal-style test suite (`MarketplaceATPFormalVerification.t.sol`)

### 5.3. Canonical Security Properties

- Root buyer and seller identities are immutable after order creation
- Delegate sessions cannot redirect refunds, payouts, or receipts
- Reentrancy guards on all settlement-sensitive paths
- `AIWalletV2` uses exact-approval — no reusable allowance after execution
- Expired or revoked sessions cannot execute delegated actions
- On-chain state is authoritative; runtime is a read-only projection

---

## 6. Current Traction

| Milestone | Status |
|---|---|
| ATP v3.4 deployed on BSC | ✅ Live |
| Internal security audit completed | ✅ May 2026 |
| Formal verification artifacts published | ✅ Public |
| M2M delegation v1 (AI agent support) | ✅ Live |
| Public documentation repository | ✅ Published |
| Arbitrum native deployment (ATP v3.5) | 🔄 In development |
| Base + Coinbase KYC integration | 🗓 Q4 2026 |
| Solana (Rust/Anchor) | 🗓 Q1–Q2 2027 |

---

## 7. Use of Grant Funds

| Priority | Allocation | Deliverable |
|---|---|---|
| Independent third-party audit | 40% | External audit of ATP v3.5 EVM expansion — prerequisite for institutional adoption |
| Protocol development | 35% | Arbitrum native deployment, LayerZero V2 OFT, multichain ATP standardization |
| Developer relations | 15% | SDK, integration guides, OTC and service marketplace partner onboarding |
| Ecosystem grants | 10% | Grants for builders integrating Orina as settlement primitive in their applications |

---

## 8. Deployment Roadmap

| Phase | Timeline | Goal | Audit Milestone |
|---|---|---|---|
| **Phase 1 — EVM Expansion** | Q3 2026 | ATP v3.5 on Arbitrum, LayerZero V2 OFT | Third-party audit of EVM contracts |
| **Phase 2 — Base Deployment** | Q4 2026 | Native instance on Base, Coinbase KYC/AML for enterprise compliance | Identity + escrow flow audit |
| **Phase 3 — SVM Expansion** | Q1–Q2 2027 | Full ATP rewrite in Rust/Anchor for Solana, extended AI agent M2M | Anchor program audit |

---

## 9. Why This Grant

Orina addresses infrastructure that DeFi is missing rather than adding another application on top of existing primitives. A trustless, composable settlement layer with formal verification and AI agent delegation is not a marginal improvement — it is a missing layer that many applications need but none of them want to build themselves.

Grant support at this stage directly funds the independent third-party audit that is the single most critical prerequisite for ecosystem integrators, institutional OTC participants, and AI agent platform operators to adopt Orina as their settlement layer.

We commit to open-sourcing the core contract system, publishing all audit reports publicly, and making the ATP settlement primitive available as composable infrastructure for any builder in this ecosystem.

---

## 10. Team

The Orina Protocol team brings expertise in smart contract engineering, formal verification, DeFi security, and bilateral commerce systems. The ATP contract system was developed using Foundry with formal-style test coverage, Slither static analysis, and an internal audit integrated into the development workflow.

*[Team details to be completed per specific grant submission.]*

---

## 11. Resources

| Resource | Link |
|---|---|
| Public Documentation | https://github.com/Archiver-KA/Orina-Protocol-Documentation- |
| Protocol Overview | https://github.com/Archiver-KA/Orina-Protocol-Documentation-/blob/main/docs/protocol/overview.md |
| Contract System | https://github.com/Archiver-KA/Orina-Protocol-Documentation-/blob/main/docs/protocol/contract-system.md |
| Security Model | https://github.com/Archiver-KA/Orina-Protocol-Documentation-/blob/main/docs/security/security-model.md |
| Formal Verification | https://github.com/Archiver-KA/Orina-Protocol-Documentation-/blob/main/docs/formal/formal-verification.md |
| M2M Delegation | https://github.com/Archiver-KA/Orina-Protocol-Documentation-/blob/main/docs/protocol/m2m-delegation.md |

---

*Full technical architecture and contract specifications are available in the public documentation repository. Third-party audit report will be published upon completion.*
