-- LTL specifications for the abstract NuSMV model:
-- Use with: formal/atp/nusmv/MarketplaceATP_ExecutableModel.smv

-- Finality latch: once terminal, always terminal
LTLSPEC G (finalized -> X finalized)

-- Pre-PAID orders never have seller assets locked
LTLSPEC G ((state = pending_confirm) -> !asset_locked)

-- Delegated order creation keeps canonical buyer/seller root-bound
LTLSPEC G (order_created_via_delegate -> (canonical_buyer_root & canonical_seller_root))

-- Payer vault usage never redirects refunds away from root
LTLSPEC G (payer_is_vault -> refund_to_root)

-- buyer pay window requires revised-time sellerConfirm
LTLSPEC G (buyer_pay_window_open -> (seller_confirmed & pay_deadline_active))

-- Asset lock starts only at PAID boundary and persists until terminal/dispute resolution
LTLSPEC G ((state = paid | state = disputed) -> asset_locked)

-- Escrow exists from create through non-terminal lifecycle states
LTLSPEC G ((state = pending_confirm | state = paid | state = disputed) -> escrow_funded)

-- Delegated same-time sellerConfirm enters PAID immediately
LTLSPEC G ((state = pending_confirm & seller_window_open & delegate_session_live & cmd = delegated_seller_confirm_same) -> X (state = paid & asset_locked))

-- Delegated revised-time sellerConfirm keeps state pending and opens buyer pay window
LTLSPEC G ((state = pending_confirm & seller_window_open & delegate_session_live & cmd = delegated_seller_confirm_change) -> X (state = pending_confirm & seller_confirmed & buyer_pay_window_open & !asset_locked))

-- Root direct pay remains available after delegate expiry on the revised-time branch
LTLSPEC G ((root_fallback_available & cmd = root_buyer_pay) -> X (state = paid))

-- Expired or revoked delegate cannot advance pay from the revised-time branch
LTLSPEC G ((state = pending_confirm & seller_confirmed & !delegate_session_live & cmd = delegated_buyer_pay) -> X state = pending_confirm)

-- If order is PAID, seller had already confirmed
LTLSPEC G ((state = paid) -> seller_confirmed)
