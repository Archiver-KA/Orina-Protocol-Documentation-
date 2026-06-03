# Contributing

---
date: 2026-06-03
status: Public contribution guidance
---

This repository is a curated public documentation repository. Contributions should improve clarity, correctness, structure, or public verification material without adding private operational content.

By contributing to this repository, you agree that your contribution may be published under this repository's license terms:

- Public documentation text, diagrams, public security summaries, and public formal specification material under `CC-BY-4.0 OR Apache-2.0`.
- Code snippets and command examples under `MIT OR Apache-2.0`.
- Exported EVM bytecode and bytecode hashes as verification-only publication material with no deployment or commercialization license implied.
- Brand assets reserved by Orina Protocol.

See [LICENSE.md](./LICENSE.md) and [NOTICE.md](./NOTICE.md).

## Documentation Rules

- Add `date: YYYY-MM-DD` metadata to every Markdown file.
- Keep language precise and source-backed.
- Do not add `.env` files, credentials, private RPC URLs, service-role keys, JWT secrets, generated API keys, local logs, or screenshots containing sensitive data.
- Do not copy deployment runbooks, operator checklists, production environment flip steps, or operator-only smoke-test procedures into this public repo.
- When adding formal or bytecode artifacts, include byte length, source date, source commit, and SHA-256 hash.
- Prefer concise public summaries over verbatim copies of internal working notes.

## Review Checklist

Before submitting documentation changes:

- Confirm all relative links resolve.
- Confirm all Markdown files include a date.
- Confirm artifact hashes match the files in `artifacts/`.
- Confirm no operational specs or secrets were added.
- Confirm source commit and path references are updated when source material changes.
- Confirm contributed material is original, project-owned, or otherwise permitted for publication under this repository's license scope.
- Confirm any new formal specification or test-vector material can be published under `CC-BY-4.0 OR Apache-2.0`.

## Owner Decisions

The following remain project-owner decisions:

- Public vulnerability intake address.
- ABI publication policy.
- Signed release provenance policy.
- Whether older testnet contract addresses should remain in public user docs.
