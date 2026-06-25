# Orina Protocol: Grant Application
## Settlement-First Infrastructure for Real-World Asset Commerce

**Version:** 2.0.0
**Document Type:** General Grant Application
**Protocol Baseline:** ATP v3.5 / MarketplaceATP EIP-712 v3.4
**Status:** Ready for Submission

---

## 1. Project Overview

**Project Name:** Orina Protocol
**Category:** DeFi Infrastructure / RWA Settlement / AI-Native Commerce
**Stage:** Deployed on BSC — Expanding to EVM Ecosystem

Orina Protocol is a **settlement-first, trustless escrow infrastructure layer** for real-world asset marketplace commerce. Built on a formally verified contract system, the protocol defines explicit escrow-backed transaction lifecycles, state-machine-enforced settlement paths, on-chain dispute resolution, and bounded machine-to-machine delegation — enabling both human traders and AI agents to transact with full counterparty safety.

The protocol is not a simple payment wrapper. It is a composable escrow primitive purpose-built for the complexity of real-world commerce: bilateral negotiation, delivery timing, dispute arbitration, RWA asset tracking, and autonomous delegation — all settled on-chain with cryptographic finality.

---

## 2. Problem Statement

### The Settlement Gap in RWA Commerce

Real-world asset transactions on blockchain face a structural problem that simple payment rails cannot solve: **settlement requires coordinated bilateral commitment across time, not just a payment transfer.** A buyer and seller must agree on price, delivery timing, and terms — and each needs assurance that the other cannot defect once committed.

Existing solutions fall into three categories, each with critical gaps:

- **Centralized escrow services** — require KYC, operate within single jurisdictions, carry custodial risk, and charge 2–5% fees
- **Simple smart contract escrow** — lack dispute resolution, timeout handling, RWA asset lifecycle management, and AI agent compatibility
- **Cross-chain bridges used for settlement** — introduce unnecessary bridge risk for funds that never needed to leave their native chain

### The AI Agent Commerce Problem

Emerging AI agent systems need to participate in commerce autonomously — creating orders, paying for goods, and managing marketplace positions — without the AI agent becoming a custodian of user funds or a party to contracts. No existing protocol provides the cryptographic session binding and spending-cap enforcement required for safe, auditable AI agent delegation in a commerce context.

---

## 3. Solution

### 3.1. The ATP Contract System

The Orina Atomic Transaction Protocol (ATP) is implemented as a formally verified Solidity contract system (`0.8.24`, Foundry, `via_ir`, `evm_version: cancun`) consisting of 15 contracts across three functional layers:

**Core Trade Lifecycle:**

| Contract | Responsibility |
|---|---|
| `MarketplaceATP` | Order state machine, EIP-712 order domain, direct and delegated actions |
| `PaymentGateway` | ERC-20 escrow, seller release, buyer refund, fee distribution |
| `OrinaRWA` | Seller asset ledger: mint, lock, consume, unlock |
| `RWAReceiptNFT` | Non-transferable receipt NFT for finalized RWA settlement |
| `FeeManager` | Fee schedules and token-specific fee presets |
| `DisputeManager` | Dispute lifecycle, arbiter verdicts, mutual agreement, stale resolution |
| `AutoTimeManager` | Permissionless timeout execution for all lifecycle windows |

**M2M Delegation Layer:**

| Contract | Responsibility |
|---|---|
| `DelegationManager` | Session authority, action masks, spend caps, counterparty binding, revocation |
| `AIWalletV2` | Exact-approval payer vault for delegated buy execution |
| `AIWalletFactoryV2` | Deterministic AI wallet prediction and deployment |
| `IdentityValidator` | EOA and ERC-1271 root signature validation |

### 3.2. Order Lifecycle

ATP enforces a complete, time-bound escrow lifecycle with no stuck states:

```
createOrder → [PENDING_CONFIRM] → sellerConfirm → [PAID] → delivery → [resolution]
                    │                                              │
               24h timeout                              ┌──────────┼──────────┐
               (auto-cancel)                       Buyer      Dispute    Auto-release
                                                  Confirms    (14 days)  (after 3-day
                                                                          action window)
```

**Timing constants enforced on-chain:**

| Window | Duration |
|---|---|
| Seller confirmation | 24 hours |
| Buyer re-sign (revised terms) | 24 hours |
| Buyer action after delivery | 3 days |
| Dispute resolution | 14 days |

### 3.3. Dispute Resolution

Disputes are resolved through `DisputeManager` via four paths: arbiter verdict, signed agreement between parties, mutual split, or stale-dispute auto-split after 14 days. Settlement types are `FULL_RELEASE`, `FULL_REFUND`, or `SPLIT` — covering the full range of real-world dispute outcomes.

### 3.4. M2M Delegation — AI-Native Commerce

Orina's M2M layer allows root users to authorize bounded AI agents or delegates to operate on their behalf without transferring protocol identity. The root buyer or seller remains canonical in all order, asset, refund, payout, and receipt state.

Delegated sessions bind: root, delegate, payer vault, payment token, action mask, per-order spend cap, total spend cap, validity window, counterparty, asset, price bounds, and delivery timing. Delegates in v1 cannot perform `confirmDelivery`, `openDispute`, `cancelByBuyer`, or `cancelBySeller` — all root direct-action paths remain available.

This design makes Orina the first escrow protocol with production-grade, cryptographically bounded AI agent delegation.

### 3.5. Fee Model

| Settlement Asset | Protocol Fee |
|---|---|
| Stablecoins (USDC, USDT) | 2% (200 bps) |
| `$ORI` token | 1% (100 bps) |
| Maximum total fee cap | 7% (700 bps) |
| Maximum referral fee cap | 2% (200 bps) |

Fee distribution routes to platform, DAO, and referral components via `PaymentGateway` and `FeeManager`.

---

## 4. Security & Formal Verification

### 4.1. Audit Summary (May 2026)

The internal contract audit reviewed all `src/` Solidity contracts, deployment wiring, Slither static analysis, ATP specification, and M2M delegation spec.

| Finding ID | Severity | Description | Status |
|---|---|---|---|
| M-01 | Medium | Delegated seller-confirm and buyer-pay paths did not fully bind ATP economic terms | ✅ Resolved |
| L-01 | Low | Referral fee could be retained if referral vault was zero address | ✅ Resolved |
| L-02 | Low | Buyer dispute and auto-release overlapped at exact boundary timestamp | ✅ Resolved |
| L-03 | Low | `AutoTimeManager.setDisputeManager` could mislead operators about external role grants | ✅ Resolved |

**No confirmed Critical or High findings.** All Medium and Low findings resolved before public documentation baseline.

### 4.2. Formal Verification

Formal verification artifacts are published under `artifacts/formal/atp/` in the public documentation repository:

- NuSMV executable abstraction
- CTL, LTL, and ATL specifications
- `MarketplaceATP` creation and runtime bytecode exports with SHA-256 hashes

Foundry formal-style tests (`MarketplaceATPFormalVerification.t.sol`) cover delegated order identity and delegated mint invariants.

### 4.3. Canonical Security Properties

- Root buyer and seller identities are immutable after order creation
- Delegate sessions cannot redirect refunds, payouts, or receipts
- Reentrancy guards protect all settlement-sensitive paths
- `AIWalletV2` uses exact-approval — no reusable allowance after execution
- On-chain state is the authoritative source of truth; runtime is a read-only projection

---

## 5. Traction & Current Status

| Milestone | Status |
|---|---|
| ATP v3.4 deployed on BSC | ✅ Live |
| Internal security audit completed | ✅ May 2026 |
| Formal verification artifacts published | ✅ Public |
| M2M delegation (AI agent support) | ✅ v1 live |
| Arbitrum expansion (ATP v3.5) | 🔄 In development |
| Base deployment + Coinbase KYC integration | 🗓 Planned Q4 2026 |
| Solana (Rust/Anchor rewrite) | 🗓 Planned Q1–Q2 2027 |

---

## 6. Use of Grant Funds

| Priority | Allocation | Deliverable |
|---|---|---|
| Third-party security audit | 40% | Independent audit of ATP v3.5 EVM expansion contracts |
| Protocol development | 35% | Arbitrum native deployment, LayerZero V2 OFT integration, multichain ATP standardization |
| Developer relations | 15% | SDK, integration guides, ecosystem partner onboarding |
| Community & ecosystem | 10% | Builder grants for projects integrating Orina as escrow primitive |

---

## 7. Deployment Roadmap

| Phase | Timeline | Architecture Goal | Audit Milestone |
|---|---|---|---|
| **Phase 1 — EVM Expansion** | Q3 2026 | ATP v3.5 on Arbitrum, LayerZero V2 OFT, Formal Verification | Third-party audit of EVM contracts |
| **Phase 2 — Base Deployment** | Q4 2026 | Native instance on Base, Coinbase Verifications (KYC/AML) for enterprise RWA | Identity + escrow flow audit |
| **Phase 3 — SVM Expansion** | Q1–Q2 2027 | Full ATP rewrite in Rust/Anchor for Solana, extended AI Agent M2M support | Anchor program audit, Account Model validation |

---

## 8. Market Opportunity

Orina targets the structural gap between blockchain payment infrastructure and real-world commerce settlement:

- **RWA tokenization** — institutional demand for auditable, on-chain settlement infrastructure is growing rapidly, with the tokenized asset market projected to reach significant scale by 2030
- **AI agent commerce** — as autonomous AI systems begin participating in digital marketplaces, demand for cryptographically bounded agent delegation will become a baseline infrastructure requirement
- **Cross-border P2P commerce** — freelance work, OTC trading, and international goods exchange represent billions in annual volume with no trustless settlement layer

Orina is positioned as **foundational infrastructure** — a composable escrow primitive that any dApp, marketplace, or AI agent system can integrate without rebuilding dispute resolution, timeout logic, or asset lifecycle management.

---

## 9. Why This Protocol Warrants Grant Support

Orina addresses a gap that existing DeFi primitives do not: **structured, multi-party bilateral settlement with formal state machine guarantees, on-chain dispute resolution, and AI agent delegation — designed for real-world commerce, not financial speculation.**

The protocol's formal verification artifacts, resolved audit findings, and published security model reflect an unusually mature security posture for an early-stage protocol. Grant support at this stage directly accelerates the independent third-party audit and multichain deployment that are prerequisites for institutional RWA adoption.

We are committed to open-sourcing the core contract system, publishing all audit reports publicly, and making the ATP escrow primitive available as composable infrastructure for other builders.

---

## 10. Team

The Orina Protocol team brings expertise in smart contract engineering, formal verification, DeFi security, and RWA market structure. The ATP contract system was developed using Foundry with formal-style test coverage and Slither static analysis integrated into the development workflow.

*[Team details and prior experience to be completed per specific grant submission.]*

---

## 11. Resources

| Resource | Link |
|---|---|
| Public Documentation Repository | https://github.com/Archiver-KA/Orina-Protocol-Documentation- |
| Protocol Overview | https://github.com/Archiver-KA/Orina-Protocol-Documentation-/blob/main/docs/protocol/overview.md |
| Security Model | https://github.com/Archiver-KA/Orina-Protocol-Documentation-/blob/main/docs/security/security-model.md |
| Formal Verification | https://github.com/Archiver-KA/Orina-Protocol-Documentation-/blob/main/docs/formal/formal-verification.md |
| Contact | info@orina.io |

---

*Full technical architecture and contract specifications are available in the public documentation repository. Third-party audit report will be published upon completion.*
