# DAO Fee Governance

---
date: 2026-06-02
status: Public documentation draft
source_baseline: Orina whitepaper DAO fee governance update
---

This page summarizes the intended Hybrid DAO fee governance model for Orina Protocol.

The model separates settlement correctness from fee economics. ATP remains the authority for order state, escrow custody, dispute paths, refunds, seller payout, receipt minting, and final settlement. DAO governance applies around the protocol fee layer after a transaction reaches the completed settlement path.

## Hybrid DAO Model

Orina uses a Hybrid DAO structure:

- Protocol contracts enforce deterministic ATP settlement.
- Fee policy is governed as an economic layer around completed transactions.
- ORI holders may participate in the DAO allocation side where an active distribution or incentive mechanism is published.
- Platform retained profit remains available for protocol development, infrastructure, operations, security, integrations, and reserves.

The DAO should not be described as a discretionary settlement authority. It does not override user escrow, reverse finalized orders, or decide individual dispute outcomes unless a future contract explicitly grants a narrow scoped role.

## Completed Transaction Fee Schedule

The intended completed-transaction fee schedule is:

| Payment rail | Fee rate | Basis points | Trigger |
| --- | ---: | ---: | --- |
| ORI | 1% | 100 bps | Completed transaction |
| USDT | 2% | 200 bps | Completed transaction |
| USDC | 2% | 200 bps | Completed transaction |
| Supported stablecoins | 2% | 200 bps | Completed transaction |

The `100` bps ORI preset and `200` bps stablecoin preset align with the public `FeeManager` source summary in [Contract System](./contract-system.md).

## Fee Profit Allocation

Fee profit is expected to split equally between the platform and the DAO allocation layer:

| Allocation | Share of fee profit | Purpose |
| --- | ---: | --- |
| Platform retained profit | 50% | Protocol development, infrastructure, operations, security, integrations, and reserve needs. |
| ORI holder DAO allocation | 50% | DAO-directed distribution, staking rewards, holder incentives, or other approved ORI-aligned programs. |

This allocation is a policy target for fee economics. Final activation requires published rules for eligibility, timing, claim mechanics, exclusions, jurisdictional limits, and any applicable vesting or lockup conditions.

## Settlement Examples

| Gross transaction | Payment rail | Protocol fee | Platform 50% | DAO / ORI holder 50% | Seller net before other costs |
| ---: | --- | ---: | ---: | ---: | ---: |
| 10,000 ORI | ORI | 100 ORI | 50 ORI | 50 ORI | 9,900 ORI |
| 10,000 USDT | USDT | 200 USDT | 100 USDT | 100 USDT | 9,800 USDT |
| 10,000 USDC | USDC | 200 USDC | 100 USDC | 100 USDC | 9,800 USDC |

These examples illustrate the protocol fee schedule only. They do not include gas costs, third-party payment costs, exchange-rate effects, taxes, off-chain service charges, or jurisdiction-specific withholding rules.

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
- DAO allocation does not imply equity, dividends, or legal ownership of the platform.
- Any holder distribution mechanism must define eligibility, timing, exclusions, and claim mechanics before launch.

The purpose of the Hybrid DAO model is to let ORI holders participate in protocol economics while preserving ATP as deterministic settlement infrastructure.
