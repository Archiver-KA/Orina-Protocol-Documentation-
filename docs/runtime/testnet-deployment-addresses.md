# Testnet Deployment Addresses

---
date: 2026-06-28
status: Public testnet address sheet
---

These are public testnet addresses only. Do not use testnet tokens, faucets, or deployment admin roles in production.

## BSC Testnet

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

Configured BSC runtime payment tokens: `USDT=0x337610d27c682E347C9cD60BD4b3b107C9d34dDd`, `USDC=0x64544969ED7EBf5f083679233325356EbE738930`, `WBNB=0xae13d989dac2f0debff460ac112a837c89baa7cd`, `ORI=0x093969C2Bb194E7424534918eca5119fa72a61D6`.

Starter-kit faucet assets: `OrinaTestTokenFaucet=0x6527262782C140e0A4724bef06431786556AfDE0`, `USDT.t=0x8800279B4a5528628ef069698169C58B89377809`, `USDC.t=0xbdcA834A71F5BFF1420eb5D1B0491d58a33141E5`.

## Base Sepolia

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

Base Sepolia starter-kit assets: `ORI=0xd87493F4C02AAD2c67Ce12aa534d188Bf44FCCAB`, `USDT.t=0x11E6c8f2806b32DaC427E7dF07F67602647Ef87a`, `USDC.t=0xd6e84789741ea2DE727961CCB383454e4A845035`, `OrinaTestTokenFaucet=0xbBd53C18F4d9fb98aA6c4837Ea0E8F221E1B5F0F`.

## Arbitrum Sepolia

Chain ID: `421614`

| Field | Value |
| --- | --- |
| Status | Contracts broadcast and bytecode spot-checked; runtime writes remain disabled pending Marketplace M2M governance wiring. |
| RPC URL | `https://sepolia-rollup.arbitrum.io/rpc` |
| Explorer | `https://sepolia.arbiscan.io` |
| Namespace | `orina-atp-v3.5-arbitrum-sepolia-20260628` |
| Phase 1 artifact path | `foundry/broadcast/DeployArbitrumSepoliaPhase1.s.sol/421614/run-latest.json` |
| Core artifact path | `foundry/broadcast/DeployFullSystemDirect.s.sol/421614/run-latest.json` |
| M2M artifact path | `foundry/broadcast/DeployM2MSystem.s.sol/421614/run-latest.json` |

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

Arbitrum Sepolia starter-kit assets: `ORI=0xD87493f4C02aad2c67Ce12aa534d188Bf44FCcAB`, `USDT.t=0x11E6c8f2806b32dAC427E7Df07F67602647eF87A`, `USDC.t=0xD6E84789741Ea2DE727961cCB383454E4A845035`, `OrinaTestTokenFaucet=0xbbD53C18F4d9fb98AA6c4837ea0E8F221e1b5F0F`.

Pending governance call: target `0x6d132Ba2327573c4e6f97a2167dCddb8059C4d14`, function `setDelegationManager(address)`, calldata `0x1a8d0de200000000000000000000000052440e44ec34a64e19b92243262fe47819d65539`.

## On-Chain Spot Checks

Checked on 2026-06-28:

- `MarketplaceATP`, `PaymentGateway`, and `DelegationManager` have deployed bytecode on BSC Testnet, Base Sepolia, and Arbitrum Sepolia.
- BSC Testnet and Base Sepolia `MarketplaceATP.delegationManager()` return the listed DelegationManager.
- Arbitrum Sepolia `MarketplaceATP.delegationManager()` is still zero until the pending governance call above is executed.
- Each DelegationManager grants `CONSUMER_ROLE` to its listed Marketplace.
- Arbitrum Sepolia `DelegationManager.DEFAULT_ADMIN_ROLE` is held by its timelock, not the deployer EOA.
