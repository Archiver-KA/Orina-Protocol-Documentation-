# Formal Bytecode

---
date: 2026-05-27
status: Public artifact manifest
source_artifact_date: 2026-05-18
contract: MarketplaceATP
---

This page records the public bytecode artifacts copied from the local Foundry formal artifact set.

## Source

- Source commit: `be466831ff367a7891b32b61e6541dc294b2f066`
- Source files:
  - `formal/atp/evm/MarketplaceATP.creation.bytecode.hex`
  - `formal/atp/evm/MarketplaceATP.runtime.bytecode.hex`
- Source artifact timestamp: 2026-05-18 09:21:53 local file time
- Public copy date: 2026-05-27

## Bytecode Artifacts

| Artifact | Hex chars excluding `0x` | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `artifacts/formal/atp/evm/MarketplaceATP.creation.bytecode.hex` | 53096 | 26548 | `13F50B42E9FE19854C62D9EC8FCB6AB5F12F0007B358DBF8036D189917C586BD` |
| `artifacts/formal/atp/evm/MarketplaceATP.runtime.bytecode.hex` | 48962 | 24481 | `B3D45B8AF0973E63F4C008B37C681EDA6D269F654C740A5C50D34D4B368029B4` |

## Export Commands

The source repository documents these export commands:

```bash
forge inspect src/MarketplaceATP.sol:MarketplaceATP bytecode > formal/atp/evm/MarketplaceATP.creation.bytecode.hex
forge inspect src/MarketplaceATP.sol:MarketplaceATP deployedBytecode > formal/atp/evm/MarketplaceATP.runtime.bytecode.hex
```

Re-export bytecode after any `MarketplaceATP` source change before using the artifact set for bytecode-level checks.

## Publication Notes

- The bytecode artifacts are public verification material, not deployment instructions.
- This repository does not publish private keys, RPC URLs, deployment scripts, or deployment transaction runbooks.
- ABI publication is not included in this baseline and remains an owner decision.
