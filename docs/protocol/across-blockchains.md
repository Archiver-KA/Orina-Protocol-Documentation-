# Orina Protocol: User Guide
## The Safer Way to Trade Across Blockchains

**Version:** 1.0.0
**Audience:** End Users
**Last Updated:** June 2026

---

## What is Orina Protocol?

Orina Protocol is a **trustless escrow platform** that protects your money when trading with strangers online — across any blockchain.

Think of it like a neutral middleman that holds your payment until both sides of a deal are satisfied. Except there's no middleman. It's all handled automatically by smart contracts.

---

## The Problem We Solve

When you trade with someone you don't know online, you face two risks:

- **You pay first** → the other person disappears with your money
- **You deliver first** → the buyer refuses to pay

Traditional escrow services are slow, expensive, and only work in one country or on one blockchain. Orina works everywhere.

---

## How It Works

### Step 1 — Create an Escrow Order

The buyer locks their payment into the Orina smart contract on their chosen blockchain. The funds are secured — neither party can touch them until the deal is resolved.

### Step 2 — Seller Delivers

The seller sees the funds are locked and safely delivers the goods or service.

### Step 3 — Release or Dispute

```
Deal goes well?          Something went wrong?
       │                          │
       ▼                          ▼
Buyer confirms        Either party opens a dispute
       │                          │
       ▼                          ▼
Seller receives       Independent arbitration
   payment                        │
                           ┌──────┴──────┐
                           │             │
                      Buyer wins    Seller wins
                           │             │
                      Full refund   Full payment
```

---

## Key Benefits for Users

| Feature | What It Means for You |
|---|---|
| **Non-custodial** | Orina never holds your money — the smart contract does |
| **Multichain** | Trade on BSC, Arbitrum, Base, and more — all with the same protocol |
| **No wrapped tokens** | Your USDC stays USDC. Your USDT stays USDT. No risky conversions |
| **Dispute protection** | Neutral arbitration if something goes wrong |
| **Low fees** | Protocol fees paid in `$ORI` — designed to stay minimal |

---

## Supported Chains & Assets

| Blockchain | Accepted Payment Assets |
|---|---|
| BNB Smart Chain (BSC) | USDT, USDC |
| Arbitrum | USDC (native), USDT |
| Base | USDC (native) |
| Solana *(coming soon)* | USDC (native) |

> **Important:** Your funds never leave the blockchain you choose. If you lock USDC on Arbitrum, it stays on Arbitrum until the deal is complete.

---

## The $ORI Token

`$ORI` is the utility token that powers the Orina ecosystem.

- **Pay protocol fees** at a discount when using `$ORI`
- **Participate in governance** — vote on protocol changes and fee structures
- **Earn rewards** as the protocol grows

`$ORI` works seamlessly across all supported chains. You can move it from BSC to Arbitrum to Base instantly, without using a bridge or worrying about price differences between chains.

---

## Is It Safe?

Orina is built with security as the top priority:

- **Your escrow funds never leave your chosen chain** — no bridge risk
- **Smart contracts are fully audited** before each major deployment
- **No single point of failure** — the protocol runs on decentralized infrastructure
- **Open source** — anyone can review the code

---

## Getting Started

1. Connect your wallet (MetaMask, Rabby, Phantom, etc.)
2. Choose your blockchain
3. Create or accept an escrow order
4. Trade with confidence

> **Need help?** Visit our documentation at [docs.orina.io] or join our community on Discord.

---

## Frequently Asked Questions

**What happens if neither party responds?**
Escrow orders have a configurable timeout. If the deadline passes without confirmation or dispute, funds are automatically returned to the buyer.

**Can Orina freeze my funds?**
No. The protocol is non-custodial. Only the smart contract logic — which is public and audited — can move funds.

**What if I make a mistake and send to the wrong address?**
Always double-check addresses before confirming. Like all blockchain transactions, escrow orders cannot be reversed once confirmed on-chain.

**Do I need $ORI to use Orina?**
No. You can pay fees in the escrow asset (USDC/USDT). Using `$ORI` for fees gives you a discount.
