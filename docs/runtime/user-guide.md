# Runtime User Guide

---
date: 2026-06-04
status: Public documentation baseline
source_baseline: Summarized from runtime user guide and FAQ
---

This guide describes the user-facing Orina Protocol Runtime experience at a high level.

Public app:

- https://app.orina.io/

## Browsing

Guest users can view public marketplace and community surfaces without connecting a wallet:

- Home
- Marketplace
- Search
- Asset details
- Collection details
- Profiles
- Public community content

Writes and protocol actions require a connected wallet and, for sensitive actions, a valid wallet-auth session.

## Wallet Setup

Users need an injected EIP-1193 wallet. MetaMask is the primary tested browser wallet in the source runtime docs.

For BNB Chain Testnet usage:

- Chain id: `97`
- Hex chain id: `0x61`
- Gas token: testnet BNB
- Payment flow: ERC-20 payment tokens such as WBNB, USDT, USDC, or ORI according to runtime configuration

Native BNB is used for gas. Protocol payment flows use configured ERC-20 payment tokens.

## Profile And Settings

After connecting a wallet, users should configure:

- Display name.
- Avatar and public profile fields.
- Delivery address.
- Preferred/default delivery address.
- Theme and notification preferences.
- Optional AI/agent settings when enabled.

Profile and preference data is wallet-scoped. Delivery and location snapshots used for RWA listings should be reviewed before minting because later setting changes do not automatically rewrite already minted asset snapshots.

## Marketplace And Search

The runtime marketplace catalog hydrates from Supabase and protocol projection data when configured. Search and marketplace use the same active catalog path so users see consistent asset and seller data.

Marketplace views may include:

- Grid view.
- List view.
- Map/location view.
- Seller/profile discovery.

Map markers depend on asset location snapshots with valid coordinates.

## Buying Flow

1. Connect wallet.
2. Select the configured live network.
3. Open an asset detail page.
4. Review seller, unit, quantity, payment token, price, delivery terms, and configurable attributes.
5. Select the protocol fee token when the UI exposes a separate fee-token option.
6. Select or confirm delivery address when required.
7. Sign the buyer order request.
8. Wait for seller confirmation.
9. If seller revises delivery time, accept through buyer re-sign/pay flow within the allowed window.
10. Confirm delivery when the asset is received, or open a dispute during the allowed review window.

The ATP order signing payload is:

```text
Order(orderId,buyer,seller,paymentToken,assetId,grossPrice,amount,estDeliverySeconds)
```

When the fee token differs from the payment token, the buyer signs:

```text
OrderWithFeeToken(orderId,buyer,seller,paymentToken,feeToken,assetId,grossPrice,amount,estDeliverySeconds)
```

In ATP v3.5 beta, USDT/USDC purchases may pay protocol fee in the payment token at total 2%, or in ORI at total 1%. The ORI beta path assumes nominal ORI/payment-token parity; production requires oracle pricing.

Users should not send payment outside the protocol escrow flow.

## Selling And Minting Flow

Before minting:

1. Connect seller wallet.
2. Set profile identity.
3. Add and review default delivery address.
4. Prepare media, description, category, unit, quantity, price, and delivery settings.

RWA minting snapshots delivery and asset location metadata. Incorrect settings can produce incorrect listing metadata.

RWA orders finalize into non-transferable receipt NFTs. NFT-type orders finalize into transferable ERC721 tokens.

## Orders And Disputes

Main lifecycle labels:

- `Waiting Seller Confirm`
- `Waiting Buyer Re-Sign`
- `Agreed Delivery`
- `Awaiting Auto Finalize`
- `Auto Finalize Ready`
- `Disputed`
- `Finalized`
- `Cancelled`

Dispute evidence may include:

- Tracking numbers.
- Courier status.
- Packaging media.
- Inspection media.
- Communication records.
- Documents proving shipment, delivery, damage, authenticity, or non-delivery.

## Data Safety

Only browser-safe public configuration belongs in frontend environment variables. Supabase service-role keys, JWT secrets, delegate encryption keys, Pinata credentials, private keys, and generated API keys must not be exposed in browser code, issue text, logs, or public documentation.
