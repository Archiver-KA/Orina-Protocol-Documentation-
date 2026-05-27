# Formal Verification

---
date: 2026-05-27
status: Public documentation baseline
source_artifact_date: 2026-05-18
---

The ATP formal artifact set provides model and specification inputs for the current Foundry source candidate after v3.5 fee/delegation hardening.

## Artifact Set

| Artifact type | Path |
| --- | --- |
| NuSMV executable model | `artifacts/formal/atp/nusmv/MarketplaceATP_ExecutableModel.smv` |
| CTL specification | `artifacts/formal/atp/ctl/MarketplaceATP_CTL.spec` |
| LTL specification | `artifacts/formal/atp/ltl/MarketplaceATP_LTL.spec` |
| ATL strategy | `artifacts/formal/atp/atl/MarketplaceATP_ATL.strategy` |
| Creation bytecode | `artifacts/formal/atp/evm/MarketplaceATP.creation.bytecode.hex` |
| Runtime bytecode | `artifacts/formal/atp/evm/MarketplaceATP.runtime.bytecode.hex` |

## Modeled Scope

- Direct root flow for `createOrder`, `sellerConfirm`, `payOrder`, dispute, delivery confirm, and timeout paths.
- Delegated M2M flow for `createOrderFor`, `sellerConfirmFor`, `payOrderFor`, and `mintAssetFor`.
- Root buyer remains the stored buyer.
- Root seller remains the stored seller.
- Payer vault is separated from buyer identity.
- Refund recipient remains bound to the root buyer.
- Delegated path stops when session is expired or revoked.
- No-expiry sessions remain live until root revoke under policy constraints.
- Root fallback remains available.
- Delegated term policy binds payment token, asset id, amount, gross price, and delivery bounds.

## Explicit V1 Exclusions

- Delegated `openDispute`.
- Delegated `confirmDelivery`.
- Delegated `cancelByBuyer`.
- Delegated `cancelBySeller`.
- Generic relayed meta-transactions.

## Formal Property Themes

Safety properties:

- Delegate cannot become stored buyer.
- Delegate cannot become stored seller.
- Final receipt owner is root buyer beneficiary only.
- Seller payout recipient is root seller beneficiary only.
- Delegate cannot execute dispute, cancel, or confirm-delivery in v1.
- Expired or revoked sessions cannot execute delegated flow.
- Refund recipient cannot be redirected by delegate.
- Exact allowance leaves no reusable approval after success or revert.

Liveness properties:

- Valid delegated `createOrderFor` can succeed.
- Valid delegated `payOrderFor` can succeed.
- Valid delegated `mintAssetFor` can succeed.
- Valid delegated `sellerConfirmFor` can succeed.
- Root can continue lifecycle after delegate expiry.
- Parent can sweep expired wallet idle funds.

Non-regression properties:

- Direct root create-order behavior remains compatible with the current direct path.
- Direct root pay-order behavior remains compatible with the current direct path.
- Direct root mint behavior remains compatible with the current direct path.
- Root smart-wallet users can still use direct dispute path after signature abstraction upgrade.

## Interpretation

The NuSMV file is an executable abstraction of lifecycle and delegated authority semantics. It is not a bytecode-level model. Bytecode-level references are provided separately as exported `MarketplaceATP` creation and runtime bytecode files.

Formal artifacts should be refreshed after any `MarketplaceATP` source change.
