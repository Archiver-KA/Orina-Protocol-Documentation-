# Orina Protocol: User Guide
## The Safer Way to Trade Real-World Assets On-Chain

**Version:** 2.0.0
**Audience:** End Users
**Last Updated:** June 2026

---

## What is Orina Protocol?

Orina Protocol is a **trustless escrow platform** built specifically for real-world asset (RWA) commerce on blockchain. It lets buyers and sellers transact securely — no intermediary, no custodian, no trust required.

Think of it as a neutral, automated settlement layer: funds are locked in a smart contract until both sides of a deal are satisfied. If something goes wrong, a neutral arbiter steps in. Everything is enforced by code, on-chain, with no single party in control.

---

## The Problem We Solve

Trading real assets on-chain — goods, property rights, tokenized commodities — carries real risks:

- **You pay first** → the seller disappears with your money
- **You deliver first** → the buyer refuses to pay
- **Disputes drag on** → no clear resolution path

Orina eliminates all three with a structured, time-bound escrow lifecycle that keeps every party accountable.

---

## How It Works

### Step 1 — Buyer Creates an Order

The buyer proposes an order and their payment is immediately escrowed. Funds are locked in the smart contract — neither party can touch them.

### Step 2 — Seller Confirms

The seller has **24 hours** to confirm the order. They can accept the terms as-is, or propose revised delivery timing. If the seller revises, the buyer has **24 hours** to accept the new terms.

### Step 3 — Delivery

Once confirmed, the seller delivers within the agreed timeframe. The buyer can confirm receipt at any time during delivery.

### Step 4 — Settlement

```
Delivery confirmed?              Something went wrong?
        │                                 │
        ▼                                 ▼
Seller receives payment         Buyer opens a dispute
                                          │
                              ┌───────────┼───────────┐
                              │           │           │
                         Arbiter      Agreement    Mutual
                         Verdict       Between      Split
                              │         Parties       │
                         ┌────┴────┐                  │
                         │         │                  │
                    Buyer Wins  Seller Wins     Split Released
                         │         │
                    Full Refund  Full Payment
```

### What Happens If Nobody Acts?

After the buyer action window (3 days after delivery), the protocol can automatically finalize in the seller's favor. This protects sellers from buyers who go silent after receiving goods.

---

## Key Features

| Feature | What It Means for You |
|---|---|
| **Non-custodial** | Orina never holds your money — the smart contract does |
| **RWA Receipts** | Finalized RWA orders mint a non-transferable on-chain receipt as proof of ownership |
| **AI Agent Support** | Businesses can authorize AI agents to execute orders on their behalf — securely and within strict limits |
| **Dispute Protection** | Multiple resolution paths: arbiter verdict, mutual agreement, or split settlement |
| **Time-bound lifecycle** | Every stage has clear deadlines — no orders stuck in limbo indefinitely |
| **Low fees** | 2% on stablecoin rails, 1% when paying in `$ORI` |

---

## Order Timeline at a Glance

| Stage | Time Limit | What Happens If Missed |
|---|---|---|
| Seller confirmation | 24 hours | Order auto-cancels, buyer refunded |
| Buyer re-sign (if terms revised) | 24 hours | Order auto-cancels, buyer refunded |
| Buyer action after delivery | 3 days | Protocol auto-releases payment to seller |
| Dispute resolution | 14 days | Stale dispute resolved via auto-split |

---

## RWA Receipts — Proof of Ownership

When a Real World Asset transaction is finalized, Orina mints a **non-transferable receipt NFT** to the buyer. This receipt serves as on-chain evidence of finalized ownership — it cannot be sold or transferred, making it a clean ownership record rather than a tradeable token.

---

## AI Agent Delegation (For Businesses)

If you run a business that processes many orders, Orina supports **machine-to-machine (M2M) delegation**. You can authorize an AI agent to:

- Create orders on your behalf
- Pay for orders automatically
- Confirm seller delivery

The agent operates within strict limits you define — including spending caps, counterparty restrictions, and time bounds. Critically, **the agent never becomes the buyer or seller**. You remain the canonical owner. If the agent's session expires or is revoked, you retain full access to your orders, assets, and funds.

---

## Fee Structure

| Payment Method | Protocol Fee |
|---|---|
| USDC / USDT (stablecoins) | 2% of transaction value |
| `$ORI` token | 1% of transaction value |

Fees are deducted at settlement, not upfront.

---

## The $ORI Token

`$ORI` is the utility token of the Orina ecosystem.

- **Pay protocol fees at a discount** — 1% vs 2% for stablecoins
- **Governance** — vote on protocol parameters, fee schedules, and upgrades
- **Works across all chains** — move `$ORI` between BSC, Arbitrum, Base, and more without bridges or price slippage

---

## Is It Safe?

Orina's security posture is grounded in formal verification and internal audit:

- **No confirmed Critical or High findings** in the internal contract audit (May 2026)
- **All Medium and Low findings resolved** before the public baseline
- **Reentrancy guards** on all settlement-sensitive code paths
- **On-chain state is authoritative** — runtime applications are read-only projections of contract state
- **AI delegate sessions are strictly bounded** — delegates cannot redirect refunds, dispute outcomes, or payouts

---

## Supported Chains & Assets

| Blockchain | Accepted Payment Assets |
|---|---|
| BNB Smart Chain (BSC) | USDT, USDC |
| Arbitrum | USDC (native), USDT |
| Base | USDC (native) |
| Solana *(coming soon)* | USDC (native) |

> Your funds always stay on the chain you choose. Orina does not route escrow funds through bridges.

---

## Frequently Asked Questions

**What happens if the seller never confirms?**
The order auto-cancels after 24 hours and your payment is returned in full.

**Can Orina freeze or seize my funds?**
No. The protocol is non-custodial. Only the smart contract logic — publicly audited — can move funds.

**What if I'm an AI agent operator?**
You can authorize AI wallets with precise spending limits, counterparty restrictions, and time windows. See the M2M Delegation documentation for technical details.

**Can I use Orina for non-RWA trades?**
The protocol is designed for RWA commerce but the escrow logic works for any bilateral exchange of value requiring trustless settlement.

**Do I need $ORI to use Orina?**
No. Stablecoin payment is fully supported. `$ORI` gives you a 1% fee discount and governance rights.
