<!--
date: 2026-06-04
status: Public documentation baseline
source_status: Curated from Orina protocol, runtime, profile, and whitepaper sources
-->

# Orina Protocol

![Orina Protocol banner](./assets/images/orina-banner-github.jpg)

**The settlement layer for bilateral commerce.**

Orina is a decentralized settlement protocol that enables any two independent parties to complete transactions without relying on trust, intermediaries, or platform-controlled enforcement.

Orina guarantees one canonical settlement outcome for every bilateral transaction. Parties agree to programmable settlement conditions before execution begins; once those conditions are satisfied, settlement executes deterministically.

## Official Links

| Channel | Link |
| --- | --- |
| Website | https://www.orina.io/ |
| Runtime app | https://app.orina.io/ |
| Blog | https://orina.io/blog |
| Whitepaper | https://whitepaper.orina.io/ |
| X / Twitter | https://x.com/Orina_official |
| Discord | https://discord.gg/vythc6X9qF |
| GitHub | https://github.com/Archiver-KA/Orina-Protocol-Documentation- |
| Telegram official | https://t.me/orinaofficial |
| Telegram global | https://t.me/orinaglobal |
| Email | info@orina.io |

## Why Orina Exists

Digital commerce still depends on trusted intermediaries. Whether parties are exchanging assets, paying for services, purchasing goods, or coordinating automated systems, settlement often depends on centralized platforms, escrow providers, or manual dispute resolution.

These approaches increase cost, reduce transparency, and create single points of failure. Orina replaces trust with deterministic settlement rules executed directly by protocol.

## What Orina Does

Orina standardizes the settlement path for bilateral transactions:

- Agreement: both parties accept programmable settlement conditions before execution.
- Asset commitment: the transaction value or deliverable is committed to the flow.
- Condition verification: agreed conditions, deadlines, and dispute paths are evaluated.
- Deterministic settlement: the transaction reaches exactly one canonical final outcome.

## Core Principles

- Deterministic Settlement: every transaction reaches exactly one final state.
- Trust-Minimized: neither party needs to trust the other.
- Programmable Conditions: settlement logic is defined before execution.
- Composable: marketplaces, wallets, AI systems, and enterprise applications can integrate Orina.
- Permissionless: anyone can build on the protocol.

## Where Orina Can Be Used

| Area | Examples |
| --- | --- |
| Commerce | Goods, service payments, procurement, cross-border transactions |
| Financial | OTC trading, escrow, asset exchange |
| AI Economy | AI agent commerce, autonomous payments, machine-to-machine settlement |
| Assets | Digital assets, physical assets, tokenized assets |

## What Orina Is Not

Orina is not a marketplace, escrow provider, or payment gateway. It is a settlement protocol that marketplaces, AI agents, wallets, and commerce platforms can integrate as infrastructure.

## Documentation

| Area | Start here |
| --- | --- |
| Project profile | [Project Profile](./docs/project/profile.md) |
| Tokenomics | [ORI Tokenomics](./docs/project/tokenomics.md) |
| Docs hub | [Docs Hub](./docs/README.md) |
| Protocol | [Protocol Overview](./docs/protocol/overview.md) |
| Contracts | [Contract System](./docs/protocol/contract-system.md) |
| DAO fee governance | [DAO Fee Governance](./docs/protocol/dao-fee-governance.md) |
| Order lifecycle | [Order Lifecycle](./docs/protocol/order-lifecycle.md) |
| M2M delegation | [M2M Delegation](./docs/protocol/m2m-delegation.md) |
| Runtime | [Runtime Overview](./docs/runtime/overview.md) |
| Live runtime app | [Runtime App](./docs/runtime/live-app.md) |
| Security | [Security Model](./docs/security/security-model.md) |
| Internal audit | [Internal Audit Summary](./docs/security/internal-audit-summary.md) |
| Security status | [Security Status](./docs/security/security-status-2026-06-27.md) |
| Testnet addresses | [Testnet Deployment Addresses](./docs/runtime/testnet-deployment-addresses.md) |
| Mainnet checklist | [Mainnet Production Checklist](./docs/security/mainnet-production-checklist.md) |
| Formal methods | [Formal Verification](./docs/formal/formal-verification.md) |
| Bytecode | [Formal Bytecode](./docs/formal/bytecode.md) |
| Glossary | [Glossary](./docs/reference/glossary.md) |
| Official links | [Official Links](./docs/reference/official-links.md) |

## Testnet Networks

These addresses are public testnet deployments only. Do not use testnet tokens, faucets, or deployment admin roles in production. The detailed address sheet is [Testnet Deployment Addresses](./docs/runtime/testnet-deployment-addresses.md).

### BSC Testnet

Chain ID: `97`

| Contract | Address |
| --- | --- |
| `UnitRegistry` | `0x4ea45450064CD5B7c88EcAaE6a145652FEDd5df0` |
| `FeeManager` | `0xD32fc966835D8eb7D26A12BEcCa86c749A60eFb3` |
| `OrinaRWA` | `0x3a591AB1aB3A281f999AAD1644b020CbEC463C47` |
| `MarketplaceATP` | `0x18E1C8ab257FAf16Ec8257A9715d07661194150B` |
| `PaymentGateway` | `0x082d75D8cA96C6e97B6b451Ad4857454A53D5C15` |
| `DisputeManager` | `0xCD27B85e7EA6FB1FDC484ae9083286DdCC14DC21` |
| `AutoTimeManager` | `0x5639792243617841800df8F1450B86223c3d86f4` |
| `RWAReceiptNFT` | `0x16A35bdD00dCfb9010504FbD1b2B97e26bB315ca` |
| `ShippingRegistry` | `0x16402c8C883a01dbfD2D7E58A46D3E9434396836` |
| `TimelockController` | `0x5452CE749EDA1bE82132743AA224e7C86023A7F4` |
| `DelegationManager` | `0xb27C8eCc266423dDA3323983Ae3a2eF691ed8a13` |
| `AIWalletFactoryV2` | `0xD838268fa8dF6AFD1Fd79D9C0Fd243A3D23D0441` |

Runtime payment tokens: `USDT=0x337610d27c682E347C9cD60BD4b3b107C9d34dDd`, `USDC=0x64544969ED7EBf5f083679233325356EbE738930`, `WBNB=0xae13d989dac2f0debff460ac112a837c89baa7cd`, `ORI=0x093969C2Bb194E7424534918eca5119fa72a61D6`.

Starter kit: `OrinaTestTokenFaucet=0x6527262782C140e0A4724bef06431786556AfDE0`, `USDT.t=0x8800279B4a5528628ef069698169C58B89377809`, `USDC.t=0xbdcA834A71F5BFF1420eb5D1B0491d58a33141E5`.

### Base Sepolia

Chain ID: `84532`

| Contract | Address |
| --- | --- |
| `UnitRegistry` | `0x5a709d6F4f0a084315C64272FfC158dc61F0de38` |
| `FeeManager` | `0x51aB383A43d79f4127B7E7dCBcd892164FA2838F` |
| `OrinaRWA` | `0x0a9EfC1fb95be24743B1452Ac4C974E5e925A453` |
| `MarketplaceATP` | `0x6d132Ba2327573c4e6f97a2167dCddb8059C4d14` |
| `PaymentGateway` | `0x1A880Ae46993282dD77C2Ddcc5e36498eb616c92` |
| `DisputeManager` | `0x952ae0562de695C63C1386458db537193CE293b4` |
| `AutoTimeManager` | `0xa12273Ad5B73c5F57139E84aa89db52fe7Af05De` |
| `RWAReceiptNFT` | `0x82D2f4e131D1eB34f9B6ebc8CC37Bdd1CcA84E95` |
| `ShippingRegistry` | `0x50fd56dca706471b7f0aB59051006AA2712C2DF2` |
| `TimelockController` | `0x989b893118237f710b7Efc8820147B61c68DcaEE` |
| `DelegationManager` | `0xFC0038B7CC628966f8a7f14414c9386c2d6cB288` |
| `AIWalletFactoryV2` | `0x0E5E106A7F81233Fe07115Aeb3777e847adB09cB` |

Starter kit: `ORI=0xd87493F4C02AAD2c67Ce12aa534d188Bf44FCCAB`, `USDT.t=0x11E6c8f2806b32DaC427E7dF07F67602647Ef87a`, `USDC.t=0xd6e84789741ea2DE727961CCB383454e4A845035`, `OrinaTestTokenFaucet=0xbBd53C18F4d9fb98aA6c4837Ea0E8F221E1B5F0F`.

### Arbitrum Sepolia

Chain ID: `421614`

| Contract | Address |
| --- | --- |
| `UnitRegistry` | `0x37D917202211492523659e83010300A444D62C91` |
| `FeeManager` | `0x0c4AccB88E2Cc530FEFBAb31Ca77371a2a68Ba20` |
| `OrinaRWA` | `0x0244Ad5ca0BC9Cd8555352Cd53Dc51Fd8eD2f011` |
| `MarketplaceATP` | `0x5863f25A8250EBe20Bd1E3d04FD796081Fc3D72E` |
| `PaymentGateway` | `0x39F539903b75A0bF0FEF16a443904C8c9DF787EE` |
| `DisputeManager` | `0xEE36B67BE61A37672D4ae041A89aEd12B333753E` |
| `AutoTimeManager` | `0x75ac6efE7483c03B971Fb8E635dEE8ed8D527c61` |
| `RWAReceiptNFT` | `0x6A695E8356b6F80664E31402038CbBdBCfffa816` |
| `ShippingRegistry` | `0x63f85795fAc0F76831a3eB14Dc7729A4052fe7F7` |
| `TimelockController` | `0x66Bf76Fdf268976080f119278982B082f417FbAD` |
| `DelegationManager` | `0x56D454f55D5d05b060777F70e653BbBEb1167D2e` |
| `AIWalletFactoryV2` | `0x143519194A9Df4678b602BEE329C1A96381d1CBD` |

Starter kit: `ORI=0x5e41f1155AB4E614037C9C481BB8c1d398915cd0`, `USDT.t=0x279c62C97c6967d0E0F45f9D2460d38E3929c090`, `USDC.t=0x233Fb28c8166807b01DcBE2743bb85cF7cdC8b41`, `OrinaTestTokenFaucet=0xFA37557E4F6D066f6CF4B69BA865837d007c8D1e`.

### Ethereum Sepolia

Chain ID: `11155111`

| Contract | Address |
| --- | --- |
| `UnitRegistry` | `0x5a709d6f4F0a084315C64272FFc158Dc61F0De38` |
| `FeeManager` | `0x51aB383A43d79f4127B7E7dCBcd892164FA2838F` |
| `OrinaRWA` | `0x0a9efc1fb95be24743b1452ac4c974E5E925A453` |
| `MarketplaceATP` | `0x6d132Ba2327573c4e6f97a2167dCddb8059C4d14` |
| `PaymentGateway` | `0x1A880Ae46993282dd77C2dDCc5e36498eB616C92` |
| `DisputeManager` | `0x952aE0562De695c63c1386458DB537193Ce293b4` |
| `AutoTimeManager` | `0xa12273AD5b73c5F57139e84aa89Db52FE7Af05de` |
| `RWAReceiptNFT` | `0x82d2f4e131d1EB34F9B6Ebc8CC37bdD1cca84e95` |
| `ShippingRegistry` | `0x50fD56DcA706471B7f0Ab59051006aA2712c2DF2` |
| `TimelockController` | `0x5C842728C357B9b18eb8A9A7a840499936132e67` |
| `DelegationManager` | `0x52440e44ec34a64e19b92243262fe47819d65539` |
| `AIWalletFactoryV2` | `0x7D6b498eDc3F469ED020116e8892EbB361753bCB` |

Starter kit: `ORI=0xD87493f4C02aad2c67Ce12aa534d188Bf44FCcAB`, `USDT.t=0x11E6c8f2806b32dAC427E7Df07F67602647eF87A`, `USDC.t=0xD6E84789741Ea2DE727961cCB383454E4A845035`, `OrinaTestTokenFaucet=0xbbD53C18F4d9fb98AA6c4837ea0E8F221e1b5F0F`.

### Optimism Sepolia

Chain ID: `11155420`

| Contract | Address |
| --- | --- |
| `UnitRegistry` | `0x5a709d6f4F0a084315C64272FFc158Dc61F0De38` |
| `FeeManager` | `0x51aB383A43d79f4127B7E7dCBcd892164FA2838F` |
| `OrinaRWA` | `0x0a9efc1fb95be24743b1452ac4c974E5E925A453` |
| `MarketplaceATP` | `0x6d132Ba2327573c4e6f97a2167dCddb8059C4d14` |
| `PaymentGateway` | `0x1A880Ae46993282dd77C2dDCc5e36498eB616C92` |
| `DisputeManager` | `0x952aE0562De695c63c1386458DB537193Ce293b4` |
| `AutoTimeManager` | `0xa12273AD5b73c5F57139e84aa89Db52FE7Af05de` |
| `RWAReceiptNFT` | `0x82d2f4e131d1EB34F9B6Ebc8CC37bdD1cca84e95` |
| `ShippingRegistry` | `0x50fD56DcA706471B7f0Ab59051006aA2712c2DF2` |
| `TimelockController` | `0x5C842728C357B9b18eb8A9A7a840499936132e67` |
| `DelegationManager` | `0x52440e44ec34a64e19b92243262fe47819d65539` |
| `AIWalletFactoryV2` | `0x7D6b498eDc3F469ED020116e8892EbB361753bCB` |

Starter kit: `ORI=0xD87493f4C02aad2c67Ce12aa534d188Bf44FCcAB`, `USDT.t=0x11E6c8f2806b32dAC427E7Df07F67602647eF87A`, `USDC.t=0xD6E84789741Ea2DE727961cCB383454E4A845035`, `OrinaTestTokenFaucet=0xbbD53C18F4d9fb98AA6c4837ea0E8F221e1b5F0F`.

### Avalanche Fuji

Chain ID: `43113`

| Contract | Address |
| --- | --- |
| `UnitRegistry` | `0x5a709d6f4F0a084315C64272FFc158Dc61F0De38` |
| `FeeManager` | `0x51aB383A43d79f4127B7E7dCBcd892164FA2838F` |
| `OrinaRWA` | `0x0a9efc1fb95be24743b1452ac4c974E5E925A453` |
| `MarketplaceATP` | `0x6d132Ba2327573c4e6f97a2167dCddb8059C4d14` |
| `PaymentGateway` | `0x1A880Ae46993282dd77C2dDCc5e36498eB616C92` |
| `DisputeManager` | `0x952aE0562De695c63c1386458DB537193Ce293b4` |
| `AutoTimeManager` | `0xa12273AD5b73c5F57139e84aa89Db52FE7Af05de` |
| `RWAReceiptNFT` | `0x82d2f4e131d1EB34F9B6Ebc8CC37bdD1cca84e95` |
| `ShippingRegistry` | `0x50fD56DcA706471B7f0Ab59051006aA2712c2DF2` |
| `TimelockController` | `0x5C842728C357B9b18eb8A9A7a840499936132e67` |
| `DelegationManager` | `0x52440e44ec34a64e19b92243262fe47819d65539` |
| `AIWalletFactoryV2` | `0x7D6b498eDc3F469ED020116e8892EbB361753bCB` |

Starter kit: `ORI=0xD87493f4C02aad2c67Ce12aa534d188Bf44FCcAB`, `USDT.t=0x11E6c8f2806b32dAC427E7Df07F67602647eF87A`, `USDC.t=0xD6E84789741Ea2DE727961cCB383454E4A845035`, `OrinaTestTokenFaucet=0xbbD53C18F4d9fb98AA6c4837ea0E8F221e1b5F0F`.

Governance note: Avalanche Fuji uses deployer EOA as timelock proposer/executor/admin with zero delay for testnet only. Avalanche-C mainnet must redeploy with production multisig/Safe governance, a non-zero timelock delay, and a fresh address set.

### World Chain Sepolia

Chain ID: `4801`

| Contract | Address |
| --- | --- |
| `UnitRegistry` | `0x5a709d6f4F0a084315C64272FFc158Dc61F0De38` |
| `FeeManager` | `0x51aB383A43d79f4127B7E7dCBcd892164FA2838F` |
| `OrinaRWA` | `0x0a9efc1fb95be24743b1452ac4c974E5E925A453` |
| `MarketplaceATP` | `0x6d132Ba2327573c4e6f97a2167dCddb8059C4d14` |
| `PaymentGateway` | `0x1A880Ae46993282dd77C2dDCc5e36498eB616C92` |
| `DisputeManager` | `0x952aE0562De695c63c1386458DB537193Ce293b4` |
| `AutoTimeManager` | `0xa12273AD5b73c5F57139e84aa89Db52FE7Af05de` |
| `RWAReceiptNFT` | `0x82d2f4e131d1EB34F9B6Ebc8CC37bdD1cca84e95` |
| `ShippingRegistry` | `0x50fD56DcA706471B7f0Ab59051006aA2712c2DF2` |
| `TimelockController` | `0x5C842728C357B9b18eb8A9A7a840499936132e67` |
| `DelegationManager` | `0x5e41f1155AB4E614037C9C481BB8c1d398915cd0` |
| `AIWalletFactoryV2` | `0x279c62C97c6967d0E0F45f9D2460d38E3929c090` |

Starter kit: `ORI=0xD87493f4C02aad2c67Ce12aa534d188Bf44FCcAB`, `USDT.t=0x11E6c8f2806b32dAC427E7Df07F67602647eF87A`, `USDC.t=0xD6E84789741Ea2DE727961cCB383454E4A845035`, `OrinaTestTokenFaucet=0xbbD53C18F4d9fb98AA6c4837ea0E8F221e1b5F0F`.

Governance note: World Chain Sepolia uses deployer EOA as timelock proposer/executor/admin with zero delay for testnet only. Its first M2M pair `0x52440e44ec34a64e19b92243262fe47819d65539` / `0x7D6b498eDc3F469ED020116e8892EbB361753bCB` is orphaned and must not be used. World Chain mainnet chain `480` must redeploy with production multisig/Safe governance, a non-zero timelock delay, and a fresh address set.

## Formal Artifacts

Curated ATP formal artifacts are stored under [artifacts/formal/atp](./artifacts/formal/atp/README.md):

- NuSMV executable abstraction.
- CTL, LTL, and ATL specifications.
- `MarketplaceATP` creation and runtime bytecode exports.

The bytecode files are documented with SHA-256 hashes in [Formal Bytecode](./docs/formal/bytecode.md).

## Security And Audit

The ATP contract system and runtime application have completed internal security review passes. See [Internal Audit Summary](./docs/security/internal-audit-summary.md) and [Security Status](./docs/security/security-status-2026-06-27.md) for scope, results, verification references, and limitations.

This is an internal audit summary, not an external audit certificate.

## Public Scope

Included:

- Project profile and official social links.
- Basic protocol and runtime documentation.
- Public runtime app reference for ATP v3.5 beta.
- Contract responsibilities and invariants.
- Public security posture and verification summaries.
- Formal model/specification references.
- Formal bytecode artifacts and hashes.

Excluded:

- Deployment runbooks and operator checklists.
- Production environment flip plans.
- Internal planning documents.
- Future runtime migration material.
- Operator-only verification scripts and smoke-test procedures.
- `.env`, secrets, keys, logs, caches, `node_modules`, and build output.
- Internal backlog, local archive, and owner-decision workflow notes.

## ORI Token Snapshot

| Field | Value |
| --- | --- |
| Token name | ORINA |
| Token symbol | ORI |
| Chain | BNB Smart Chain |
| Standard | BEP-20 |
| Decimals | 18 |
| Total supply | 1,000,000,000 ORI |
| Contract | [`0x093969C2Bb194e7424534918ECa5119FA72a61d6`](https://bscscan.com/token/0x093969c2bb194e7424534918eca5119fa72a61d6) |

ORI is a protocol coordination token used around ecosystem access, fees, participation, and future governance functions. ORI does not replace ATP and does not define transaction correctness; ATP is the settlement logic.

See [DAO Fee Governance](./docs/protocol/dao-fee-governance.md) for the Hybrid DAO fee model: 1% ORI fee-token path, 2% supported stablecoin fee-token path, no protocol burn, a 50% platform / 50% DAO ecosystem allocation target, and securities-law boundary language for DAO programs.

See [ORI Tokenomics](./docs/project/tokenomics.md) for public token supply, allocation, vesting, fee-alignment, and reference valuation formulas.

## Repository Policy

- [License](./LICENSE.md)
- [Notice](./NOTICE.md)
- [Security Policy](./SECURITY.md)
- [Contributing](./CONTRIBUTING.md)
- [Source Inventory](./docs/reference/source-inventory.md)

## License

This documentation repository uses scoped licensing:

- Public documentation text, diagrams, public security summaries, and public formal specification materials: dual-licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) or [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) (`CC-BY-4.0 OR Apache-2.0`).
- Code snippets and command examples: MIT License or Apache License 2.0 (`MIT OR Apache-2.0`).
- Exported EVM bytecode and bytecode hashes: published for verification and reproducibility only; no deployment or commercialization license is implied.
- Orina brand assets: reserved.

See [LICENSE.md](./LICENSE.md) and [NOTICE.md](./NOTICE.md) for the controlling terms and attribution guidance.
