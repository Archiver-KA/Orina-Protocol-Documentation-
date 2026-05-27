# Order Lifecycle

---
date: 2026-05-27
status: Public documentation baseline
source_baseline: MarketplaceATP and runtime order semantics
---

ATP orders move through an escrowed lifecycle designed to keep on-chain state authoritative while the runtime application presents normalized business labels.

## Direct Buyer Flow

1. Buyer creates an order through `createOrder`.
2. `PaymentGateway` escrows buyer funds at creation.
3. Seller has 24 hours to call `sellerConfirm`.
4. If seller accepts unchanged terms, the order enters `PAID`.
5. If seller revises delivery timing, the buyer has 24 hours to accept through `payOrder`.
6. The delivery period starts after payment commitment.
7. Buyer can confirm delivery before the delivery timer ends.
8. After the delivery timer ends, the buyer has a 3-day action window to confirm delivery or open dispute.
9. If no buyer action happens after the buyer action window, protocol auto-release can finalize settlement.

## Seller Flow

1. Seller mints or controls an RWA asset in `OrinaRWA`.
2. Seller has a bounded confirmation window after buyer order proposal.
3. Seller confirmation locks the ordered asset amount.
4. Seller fulfillment proceeds under the agreed delivery timing.
5. Seller proceeds are released only through finalized settlement.

## Cancellation Paths

- Seller can cancel during the seller confirmation window.
- Buyer can cancel during the buyer re-sign window if seller revised terms and buyer does not accept.
- After payment is committed, normal resolution moves through delivery confirmation, dispute, or timeout handling rather than ordinary cancellation.

## Dispute Paths

The buyer can open a dispute while the order is paid and inside the allowed buyer action window. Disputes can resolve through:

- Arbiter verdict.
- Signed agreement.
- Mutual split.
- Stale-dispute fallback.

Dispute settlement types are `FULL_RELEASE`, `FULL_REFUND`, or `SPLIT`.

## Runtime Labels

The runtime presents business-oriented labels derived from on-chain state:

- `Waiting Seller Confirm`
- `Seller Confirm Expired`
- `Waiting Buyer Re-Sign`
- `Buyer Re-Sign Expired`
- `Agreed Delivery`
- `Awaiting Auto Finalize`
- `Auto Finalize Ready`
- `Disputed`
- `Finalized`
- `Cancelled`

## Normalized Terminal Semantics

Terminal precedence:

1. `CANCELLED`
2. `DISPUTED`
3. `COMPLETED`
4. `OPEN`

Rules:

- `CANCELLED` is closed but never counted as completed.
- `FINALIZED` with successful settlement is counted as completed.
- Display lifecycle and analytics should read the same normalized semantics.
- Projection rows may cache raw state but must not invent a different business meaning.

## Timing Summary

| Window | Duration | Purpose |
| --- | ---: | --- |
| Seller confirmation | 24 hours | Seller accepts or revises buyer proposal. |
| Buyer pay/re-sign | 24 hours | Buyer accepts revised delivery timing. |
| Buyer action after delivery timer | 3 days | Buyer confirms delivery or opens dispute. |
| Dispute period | 14 days | Standard dispute phase before stale handling. |

## Source Of Truth

On-chain protocol fields remain authoritative for assets, orders, escrow, disputes, receipts, and role-enforced actions. Runtime and Supabase rows are projections or cached views of that state.
