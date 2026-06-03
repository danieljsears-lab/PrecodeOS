# Contributing To PrecodeOS
<!-- ANCHOR: contributing -->

> AUTHORITY: Contribution rules for PrecodeOS issues, documentation, code, tests, protocols, provenance, and review expectations.
> NOT_AUTHORITY: Governance ownership, trademark permission, Apache-2.0 license text, active task selection, or implementation acceptance without maintainer review.
> LOAD_WHEN: Preparing a contribution, reviewing an incoming contribution, or deciding what validation evidence a change should include.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-06-02

## Contribution Policy

PrecodeOS welcomes thoughtful contributions that preserve its purpose: keeping AI-assisted software work understandable, scoped, evidence-backed, and human-owned for non-technical solo builders.

By submitting a contribution, you agree that inbound contributions are licensed under Apache-2.0 unless you explicitly state otherwise before submission.

In short: inbound = Apache-2.0.

Submitting a contribution does not grant trademark, brand, governance, roadmap, maintainer, or official-project identity rights. PrecodeOS™ and Precode™ remain trademarks of Dan Sears / Recode; see `TRADEMARK.md`.

## Contribution Rules

Contributions should preserve:

- creator and provenance notices
- authority contracts
- tiny active memory
- generated-output demotion
- one-active-bead workflow
- beginner-safe language
- evidence-before-acceptance behavior
- human approval for sensitive work and task transitions

Do not turn PrecodeOS into an autonomous agent, a PM framework, a hidden-memory system, or a specialist-team simulator.

## Review Expectations

Meaningful changes should include the relevant validation evidence, such as:

- `bash scripts/validate-memory.sh`
- `python3 scripts/version-check.py`
- `python3 scripts/file-inventory.py --check`
- targeted script checks for changed behavior

Maintainer review is required for changes touching governance, trademark, licensing, public positioning, active memory, or core workflow semantics.

## GitHub Workflow

PrecodeOS currently uses a solo-maintainer hybrid GitHub workflow.

Use a branch and pull request for any package-facing or trust-affecting change, including changes to public docs, active memory, workflow protocols, scripts, validation, setup, bootstrap, install/update behavior, GitHub Actions, generated-output policy, release guidance, public positioning, or package boundaries.

Use this branch pattern:

```text
codex/<short-change-name>
```

Pull requests should explain:

- what changed
- why it matters for package trust
- which files or surfaces are affected
- which checks were run
- remaining risk or uncertainty
- whether the change is release-candidate relevant

Direct-to-main is acceptable only for tiny corrections that do not change public meaning, do not affect install/setup/release behavior, do not touch active memory or core workflow semantics, and would not confuse a future adopter if shipped immediately.

Public GitHub Issues are not the primary collaboration path yet. Until the maintainer explicitly changes that policy, issues are closed or treated as unavailable; roadmap, contributor-intake, label, template, and project-board design remains future maintainer-roadmap work.

GitHub Releases are the public checkpoint surface for package baselines and release candidates. Release notes should include what changed, validation evidence, known risks, install/update cautions, and whether the release is install-ready, preview-only, or maintainer-only.

## Not Legal Advice

This contribution guide is project policy, not legal advice.
