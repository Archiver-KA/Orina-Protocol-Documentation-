# License

---
date: 2026-06-03
status: Public repository dual-license terms
---

Copyright (c) 2026 Orina Protocol.

This repository uses different license terms for different material types.

## Public Documentation And Formal Specification Materials

Unless another section of this file says otherwise, public documentation text, public diagrams, public glossary material, public protocol explanations, public security summaries, and public formal specification materials in this repository are dual-licensed under:

- Creative Commons Attribution 4.0 International; or
- Apache License 2.0.

You may choose either license for reuse.

SPDX-License-Identifier: `CC-BY-4.0 OR Apache-2.0`

License references:

- https://creativecommons.org/licenses/by/4.0/
- https://www.apache.org/licenses/LICENSE-2.0

This dual-license grant is intended to make Orina's public ATP documentation and formal settlement specification usable as public-good reference material for builders, auditors, researchers, ecosystem reviewers, and grant programs.

Covered examples:

- Markdown documentation under `docs/`.
- Public protocol diagrams and explanatory material, if present.
- Public formal model/specification files under:
  - `artifacts/formal/atp/atl/`
  - `artifacts/formal/atp/ctl/`
  - `artifacts/formal/atp/ltl/`
  - `artifacts/formal/atp/nusmv/`
- Non-sensitive test vectors, reproducibility notes, and public verification notes, if added later.

This section does not apply to exported EVM bytecode files, brand assets, private repositories, deployment runbooks, operator scripts, secrets, or upstream repositories.

## Code Snippets

Short code snippets, command examples, configuration examples, and illustrative source-code fragments embedded in documentation are licensed under the MIT License or Apache License 2.0, at your option, unless they are copied from another upstream project with its own license notice.

SPDX-License-Identifier: `MIT OR Apache-2.0`

MIT License text:

Permission is hereby granted, free of charge, to any person obtaining a copy of the code snippets and associated documentation files covered by this section, to deal in the code snippets without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the code snippets, and to permit persons to whom the code snippets are furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the code snippets.

THE CODE SNIPPETS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE CODE SNIPPETS OR THE USE OR OTHER DEALINGS IN THE CODE SNIPPETS.

Apache License 2.0 reference:

https://www.apache.org/licenses/LICENSE-2.0

## Exported Bytecode And Deployment Boundaries

Exported EVM bytecode files, artifact hashes for bytecode files, and bytecode metadata are published for public verification, reproducibility, audit reference, and documentation only.

This includes:

- `artifacts/formal/atp/evm/MarketplaceATP.creation.bytecode.hex`
- `artifacts/formal/atp/evm/MarketplaceATP.runtime.bytecode.hex`
- Bytecode hashes and byte-length records in documentation and source inventory files.

Publication of exported bytecode does not grant:

- A deployment license.
- A license to operate, fork, or commercialize Orina Protocol contracts or systems.
- A trademark, brand, or endorsement right.
- A warranty that artifacts are complete, current, or suitable for production use.

Use the artifact source dates, source commits, byte lengths, and SHA-256 hashes recorded in this repository to verify provenance.

## Brand Assets

The Orina name, ORINA mark, ORI mark, logos, visual identity, banner images, social names, and other brand assets are reserved by Orina Protocol unless a separate written permission or brand guideline says otherwise.

You may not use Orina branding in a way that implies sponsorship, endorsement, partnership, official status, token sale authorization, or protocol affiliation without permission.

## Source Repository Boundaries

This license applies only to the material in this documentation repository. It does not change the license status of any source repository, smart contract repository, runtime application repository, private operator repository, or upstream dependency referenced by this documentation.

If a referenced source repository has its own license, that license controls that repository. If a referenced source repository has no selected license, no license is granted by this documentation repository.

## Prior NonCommercial Notice

Earlier versions of this repository described documentation text under `CC-BY-NC-4.0`. As of 2026-06-03, Orina Protocol has relicensed the covered public documentation and covered public formal specification materials in this repository under `CC-BY-4.0 OR Apache-2.0` as stated above.

This relicensing does not apply to excluded material such as brand assets, exported bytecode deployment rights, private runtime/source repositories, private operator material, or third-party content outside Orina Protocol's licensing control.

## No Warranty

This repository is provided for public documentation and verification reference. It is provided without warranties or representations of any kind. Documentation may become outdated as the protocol, runtime application, contracts, governance process, or public interfaces evolve.
