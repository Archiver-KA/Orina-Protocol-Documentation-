-- CTL specifications for the abstract NuSMV model:
-- Use with: formal/atp/nusmv/MarketplaceATP_ExecutableModel.smv

-- Finality is sticky in the abstract model
SPEC AG (finalized -> AX finalized)

-- No seller asset lock before PAID
SPEC AG ((state = pending_confirm) -> !asset_locked)

-- Delegated order creation still preserves canonical root identities
SPEC AG (order_created_via_delegate -> (canonical_buyer_root & canonical_seller_root))

-- If a payer vault is used, refund routing remains root-bound
SPEC AG (payer_is_vault -> refund_to_root)

-- PAID and DISPUTED imply seller asset is locked
SPEC AG ((state = paid | state = disputed) -> asset_locked)

-- Any non-empty, non-terminal order keeps buyer escrow funded
SPEC AG ((state = pending_confirm | state = paid | state = disputed) -> escrow_funded)

-- Delegated same-time sellerConfirm moves directly to PAID
SPEC AG ((state = pending_confirm & seller_window_open & delegate_session_live & cmd = delegated_seller_confirm_same) -> AX state = paid)

-- Delegated revised-time sellerConfirm keeps order pending but activates payDeadline
SPEC AG ((state = pending_confirm & seller_window_open & delegate_session_live & cmd = delegated_seller_confirm_change) -> AX (state = pending_confirm & seller_confirmed & pay_deadline_active))

-- Buyer cancellation exists only on the revised-time pending branch
SPEC EF (buyer_cancel_allowed & EX state = cancelled_state)

-- Root fallback remains available after delegate expiry on the revised-time branch
SPEC AG (root_fallback_available -> EX state = paid)

-- A cooperative path exists to PAID
SPEC EF (state = paid)

-- A cooperative path exists to finalization
SPEC EF (state = finalized_state)
