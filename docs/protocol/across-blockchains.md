# Orina Protocol: User Guide
## Trustless Settlement for Any Two-Party Commerce

**Version:** 3.0.0
**Audience:** End Users
**Last Updated:** June 2026

---

## What is Orina Protocol?

Orina Protocol is a **trustless settlement layer** for any bilateral commerce — OTC trades, freelance services, digital goods, physical deliveries, or any deal between two parties who don't fully trust each other.

It doesn't care what you're trading. It cares that both sides are protected.

Funds are locked in a smart contract the moment an order is created. Neither party can touch them until the deal resolves — through delivery confirmation, mutual agreement, or arbiter decision. Everything is enforced by code, on-chain, with no custodian in the middle.

---

## Who Is It For?

| Use Case | How Orina Helps |
|---|---|
| **OTC Trading** | Sell crypto assets, tokens, or stablecoins P2P without relying on a centralized OTC desk |
| **Freelance & Services** | Lock payment before work begins; release only when satisfied |
| **Digital Goods** | Buy software licenses, data, or digital content with delivery protection |
| **Physical Commerce** | Escrow payment while goods are in transit; dispute if delivery fails |
| **AI Agent Commerce** | Let AI agents execute orders autonomously within strict spending limits you define |
| **Any Bilateral Deal** | If it involves two parties exchanging value, Orina can settle it |

---

## The Problem We Solve

Any time two parties who don't know each other try to trade, they face the same dilemma:

- **You pay first** → the other side disappears
- **You deliver first** → the buyer refuses to pay
- **Disputes happen** → no clear, enforceable resolution path

Centralized solutions — escrow services, OTC desks, platforms — solve this by inserting a trusted middleman. That middleman charges high fees, requires identity verification, and is itself a point of failure.

Orina removes the middleman entirely. The smart contract is the escrow agent. The protocol is the arbitration framework. No accounts, no KYC, no custodial risk.

---

## How It Works

### Step 1 — Buyer Creates an Order

The buyer proposes an order. Their payment is immediately locked in the escrow contract. The seller can see the funds are secured before they do anything.

### Step 2 — Seller Confirms

The seller has **24 hours** to confirm. They can accept the terms as-is, or propose revised delivery timing. If revised, the buyer has **24 hours** to accept the new terms or walk away with a full refund.

### Step 3 — Delivery

Once both sides commit, the seller delivers within the agreed timeframe. The buyer can confirm receipt at any point.

### Step 4 — Settlement

```
Buyer confirms delivery?         Something went wrong?
        │                                 │
        ▼                                 ▼
Seller receives payment         Buyer opens a dispute
                                          │
                              ┌───────────┼───────────┐
                              │           │           │
                         Arbiter      Mutual       Mutual
                         Verdict     Agreement      Split
                              │
                         ┌────┴────┐
                         │         │
                    Buyer Wins  Seller Wins
                         │         │
                    Full Refund  Full Payment
```

### What If Nobody Acts?

After the **3-day buyer action window** following delivery, the protocol auto-releases payment to the seller. This protects sellers from buyers who go silent after receiving goods or services.

---

## Order Timeline

| Stage | Time Limit | If Missed |
|---|---|---|
| Seller confirmation | 24 hours | Auto-cancel, full refund to buyer |
| Buyer re-sign (revised terms) | 24 hours | Auto-cancel, full refund to buyer |
| Buyer action after delivery | 3 days | Auto-release payment to seller |
| Dispute resolution | 14 days | Auto-split between parties |

No orders get stuck. Every path has a defined outcome.

---

## Key Features

| Feature | Detail |
|---|---|
| **Asset-agnostic** | Works for any bilateral trade — OTC, services, goods, digital assets |
| **Non-custodial** | Your funds are held by the smart contract, not by Orina |
| **On-chain receipts** | Finalized orders mint a non-transferable proof-of-settlement NFT |
| **Structured dispute resolution** | Arbiter verdict, mutual agreement, split, or auto-split — no undefined outcomes |
| **AI agent support** | Businesses can authorize AI agents to trade on their behalf within strict limits |
| **No bridge risk** | Your escrow funds never leave the chain you chose |

---

## AI Agent Delegation

If you run a business processing many orders, Orina supports **machine-to-machine (M2M) delegation**. You can authorize an AI agent to create orders, make payments, and confirm deliveries on your behalf — automatically.

The agent operates within limits you set:
- Maximum spend per order
- Total spend cap across all orders
- Specific counterparties only
- Time-bounded sessions
- Revocable at any time

**The agent never becomes the buyer or seller.** You remain the canonical party in every order, refund, and receipt. If the agent's session expires or you revoke it, you retain full control instantly.

---

## Fee Structure

| Payment Method | Protocol Fee |
|---|---|
| USDC / USDT | 2% at settlement |
| `$ORI` token | 1% at settlement |

Fees are deducted at settlement, not upfront. No fees on cancelled or refunded orders.

---

## The $ORI Token

`$ORI` is Orina's utility token.

- **Pay fees at half price** — 1% vs 2% for stablecoins
- **Governance** — vote on fee schedules, protocol parameters, and upgrades
- **Cross-chain** — move `$ORI` between any supported chain instantly, without bridges or slippage

---

## Supported Chains

| Blockchain | Payment Assets |
|---|---|
| BNB Smart Chain (BSC) | USDT, USDC |
| Arbitrum | USDC (native), USDT |
| Base | USDC (native) |
| Solana *(coming soon)* | USDC (native) |

Your escrow funds always stay on the chain you choose. Orina does not route settlement funds through cross-chain bridges.

---

## Frequently Asked Questions

**Is Orina only for RWA or tokenized assets?**
No. Orina is a settlement layer for any bilateral trade. The protocol doesn't care what you're exchanging — it cares that both parties fulfill their commitments.

**What if the seller never confirms?**
The order auto-cancels after 24 hours. Your payment is returned in full, automatically.

**Can Orina freeze my funds?**
No. The protocol is non-custodial. Only the smart contract logic — publicly audited — can move funds.

**What if I'm an AI agent operator?**
You can authorize AI wallets with precise spending limits, counterparty restrictions, and time windows. The AI agent never holds custody of your funds or becomes a party to contracts.

**Do I need $ORI to use Orina?**
No. Stablecoin payment is fully supported. `$ORI` gives you a fee discount and governance rights.

**What happens in a dispute if neither party agrees?**
After 14 days without resolution, the protocol executes an automatic split. No order is permanently stuck.
