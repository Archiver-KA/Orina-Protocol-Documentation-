# DAO Fee Governance

---
date: 2026-06-04
status: Public documentation draft
source_baseline: Orina whitepaper DAO fee governance update
---

This page summarizes the intended Hybrid DAO fee governance model for Orina Protocol.

The model separates settlement correctness from fee economics. ATP remains the authority for order state, escrow custody, dispute paths, refunds, seller payout, receipt minting, and final settlement. DAO governance applies around the protocol fee layer after a transaction reaches the completed settlement path.

## Hybrid DAO Model

Orina uses a Hybrid DAO structure:

- Protocol contracts enforce deterministic ATP settlement.
- Fee policy is governed as an economic layer around completed transactions.
- DAO-facing allocation may fund published ecosystem programs where objective eligibility, timing, claim, exclusion, and jurisdiction rules have been approved.
- Platform retained protocol fees remain available for protocol development, infrastructure, operations, security, integrations, and reserves.

The DAO should not be described as a discretionary settlement authority. It does not override user escrow, reverse finalized orders, or decide individual dispute outcomes unless a future contract explicitly grants a narrow scoped role.

## Completed Transaction Fee Schedule

The ATP v3.5 beta completed-transaction fee schedule is based on the selected protocol fee token:

| Fee token | Fee rate | Basis points | Trigger |
| --- | ---: | ---: | --- |
| ORI | 1% | 100 bps | Completed transaction |
| USDT | 2% | 200 bps | Completed transaction |
| USDC | 2% | 200 bps | Completed transaction |
| Supported stablecoins | 2% | 200 bps | Completed transaction |

The `100` bps ORI preset and `200` bps USDT/USDC preset align with the public `FeeManager` source summary in [Contract System](./contract-system.md). ATP v3.5 beta does not route protocol burn fees.

## Protocol Fee Allocation

Protocol fee is expected to split equally between the platform and the DAO allocation layer:

| Allocation | Share of protocol fee | Purpose |
| --- | ---: | --- |
| Platform retained protocol fee | 50% | Protocol development, infrastructure, operations, security, integrations, and reserve needs. |
| DAO ecosystem allocation | 50% | Governance-scoped ecosystem programs, usage incentives, transparency tooling, grants, or other approved ORI-aligned initiatives. |

This allocation is a policy target for fee economics. DAO-facing activation requires published rules for eligibility, timing, claim mechanics, exclusions, jurisdictional limits, and any applicable vesting or lockup conditions. It should not be described as a dividend, revenue share, passive yield, equity interest, or ownership claim in Orina or any operating entity.

## U.S. Securities-Law Boundary

DAO allocation language should be drafted conservatively because U.S. securities analysis may consider whether a crypto-asset transaction includes an investment contract or other securities interest. The relevant reference set includes the Securities Act of 1933 section 2(a)(1), the Securities Exchange Act of 1934 section 3(a)(10), the Howey investment-contract test, the SEC DAO Report of Investigation from 2017, and SEC/CFTC Release No. 33-11412, effective 2026-03-23.

For Orina public materials:

- ORI should be described as a protocol coordination and utility token, not as stock, equity, a profit right, or an ownership interest.
- DAO allocation should be described as a governance-scoped ecosystem allocation, not an automatic holder dividend or revenue-share entitlement.
- Any program funded from the DAO allocation must publish objective participation rules before activation and must avoid promising profit from the managerial or entrepreneurial efforts of others.
- Nothing in this page is legal advice, a registration analysis, or a conclusion that any token sale, DAO program, or secondary-market transaction is outside securities laws.

## Settlement Examples

| Gross transaction | Payment rail | Protocol fee | Platform 50% | DAO allocation 50% | Seller net before other costs |
| ---: | --- | ---: | ---: | ---: | ---: |
| 10,000 ORI | ORI | 100 ORI | 50 ORI | 50 ORI | 9,900 ORI |
| 10,000 USDT | USDT | 200 USDT | 100 USDT | 100 USDT | 9,800 USDT |
| 10,000 USDC | USDC | 200 USDC | 100 USDC | 100 USDC | 9,800 USDC |

These examples illustrate the protocol fee schedule only. They do not include gas costs, third-party payment costs, exchange-rate effects, taxes, off-chain service charges, or jurisdiction-specific withholding rules. Testnet/beta ORI fee quotes assume nominal ORI/payment-token parity; mainnet requires an oracle quote layer.

## Governance Scope

DAO fee governance may cover:

- DAO fee recipient or vault routing where governance-controlled routing is activated.
- Supported fee rails and fee parameter updates within contract constraints.
- ORI holder allocation policy.
- Treasury reporting and DAO fee transparency dashboards.
- Incentive programs tied to verified protocol usage.

Governance actions should be observable, versioned, and applied prospectively. Fee changes should not be represented as retroactive changes to already-finalized order economics unless the relevant contract and disclosure framework explicitly support that behavior.

## Boundary Conditions

- DAO governance does not custody per-order escrow while an order is active.
- DAO governance does not redefine ATP finality.
- DAO governance does not replace `PaymentGateway`, `FeeManager`, `DisputeManager`, or `MarketplaceATP`.
- DAO allocation does not imply equity, dividends, revenue-share entitlement, shareholder rights, creditor rights, or legal ownership of the platform.
- Any DAO-funded program must define eligibility, timing, exclusions, and claim mechanics before launch.

The purpose of the Hybrid DAO model is to preserve ATP as deterministic settlement infrastructure while allowing governance to direct a bounded ecosystem allocation around completed-transaction fees.
