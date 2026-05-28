---
prd_id: PRD-002
status: approved
owner: user
risk_level: medium
feature_link: First-Run Confidence + Bootstrap v1
features_status: not compiled
related_prds: []
---

# PRD-002 -- Bootstrap Confidence Lane
<!-- ANCHOR: prd-002-bootstrap-confidence-lane -->

> AUTHORITY: Destination shard for the read-only First-Run Confidence and Bootstrap v1 lane for adopting PrecodeOS into new or existing repositories.
> NOT_AUTHORITY: Active memory, task selection, bead activation, mutating installer behavior, package-manager release channels, generated evidence truth, external publishing, or implementation acceptance.
> LOAD_WHEN: Reviewing, implementing, or decomposing the first-run confidence and read-only bootstrap helper for PrecodeOS package adoption.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-05-28

## State

- ID: `PRD-002`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-05-28`

## Feature Link

- Feature: `First-Run Confidence + Bootstrap v1`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `none`

## Source Inputs

- Source type: `maintainer roadmap | guided setup evidence | support runbook evidence | implementation plan`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
- Stable facts:
  - PrecodeOS is a package source, not an app runtime.
  - First setup must distinguish the package checkout from the target project.
  - Beginner-safe setup starts read-only and names copy groups, exclusions, conflicts, validation, and stop conditions before mutation.
  - Full install/update manifest, release channels, package-manager installation, CLI wrapper, and mutating copy flows are deferred.
- Assumptions:
  - A read-only script plus protocol and docs hooks is enough for v1.
  - Bootstrap confidence and first-run setup trust should be one lane because users experience them as one moment.
- Conflicts or stale inputs:
  - none identified
- Privacy or secrets redactions:
  - none

## Alignment / Grilling Summary

- Alignment method: `guided maintainer discovery interview`
- Shared design concept: Bootstrap Confidence v1 is a read-only preflight lane that tells a beginner whether the package source, target project, public file groups, exclusions, conflicts, dependencies, and first safe next action are clear before any setup mutation.
- Key decisions reached:
  - Pair First-Run Confidence with Installer / Bootstrap v1.
  - Optimize for both new and existing repositories.
  - Ship a script plus docs, not docs only.
  - Default to stdout only.
  - Write generated evidence only with an explicit flag.
  - Include only a thin public package manifest slice.
- Remaining implementation-changing questions:
  - none for v1.

## Domain Language

| Term | Meaning |
|---|---|
| Package source | The local PrecodeOS checkout used as the source for setup inspection and public file groups. |
| Target project | The repository where a builder may adopt PrecodeOS. |
| Bootstrap confidence | Read-only evidence that source, target, expected file groups, exclusions, conflicts, dependencies, and first safe action are visible. |
| Thin manifest | The public file-group and exclusion dictionary needed for bootstrap preview; not release-channel or update metadata. |

## PRFAQ-Lite

- Customer promise: Before copying Precode into a project, a beginner can ask one read-only command what it sees and what must stay untouched.
- Non-obvious constraint: The helper must not install, copy, overwrite, create active memory, edit hooks, change CI, or mutate app code.
- Success signal: The user can name source, target, target kind, conflicts, exclusions, missing dependencies, and first safe next action before setup proceeds.

## Problem

First install or first session can feel unsafe even when the file tree is technically correct. A beginner can confuse the PrecodeOS package checkout with the target project, miss excluded files, overwrite existing docs, or let an agent begin implementation before setup confidence is established.

## User Moment

- Before: A builder asks an agent to adopt PrecodeOS and cannot tell which folder is source, which folder is target, what will be copied, what must be excluded, or whether setup is safe to continue.
- After: The builder receives read-only bootstrap confidence output naming source, target, target kind, public file groups, exclusions, conflicts, missing dependencies, stop conditions, and the first safe next action.
- Why now: The maintainer roadmap ranks First-Run Confidence and Installer / Bootstrap as P0 core improvements after Product Discovery Validation.

## Destination

- Destination statement: PrecodeOS has a beginner-safe, read-only Bootstrap Confidence v1 lane that guides new and existing repository adoption without hiding filesystem changes.
- Definition of done:
  - Bootstrap Confidence protocol exists.
  - `scripts/bootstrap-check.py` inspects source and target without mutation by default.
  - The helper supports human output, `--json`, and explicit `--write-evidence` to source `logs/`.
  - Guided setup, support runbook, troubleshooting, OS README, and file inventory route first-time setup through the helper.
  - Fixture-style checks cover empty target, existing target with conflicts, missing source, missing target, identical source/target, default no-write behavior, JSON output, and explicit evidence writing.
- First useful vertical slice: read-only inspection and docs integration only.

## Product Constitution Fit

- `PRODUCT.md` loaded: `not required for this package-maintenance PRD`
- Product promise fit: Fits PrecodeOS as a repo-native control layer that keeps setup bounded, inspectable, and human-approved.
- User and job fit: Supports solo non-technical builders and support engineers adopting PrecodeOS into a real project folder.
- Strategy and non-goal fit: Avoids autonomous install behavior, hidden mutation, CLI churn, and generated authority.
- Product constitution update needed: `no`

## Users

- Primary user: Solo beginner or non-technical builder adopting PrecodeOS.
- Secondary user: Support engineer or AI coding agent helping a builder through setup.
- Excluded user: Maintainers expecting a full package manager, mutating installer, update channel, or CLI distribution flow in v1.

## Goals

- Goal 1: Make the source package, target project, target kind, public file groups, exclusions, conflicts, and first safe next action visible before setup mutation.
- Goal 2: Keep v1 read-only by default.
- Goal 3: Preserve Precode authority boundaries and generated-output demotion.

## Non-Goals

- Not doing: mutating installer, package manager integration, installable `precode` CLI, Git hook installation, CI mutation, app-code changes, update channels, pinned releases, rollback automation, or full install/update manifest.
- Deferred: mutating setup flow after preview, richer package manifest and dry-run update semantics, future CLI wrapper.
- Explicitly out of scope: Any change that lets bootstrap output approve mutation, create active memory, activate beads, or overwrite target files.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-002-FR01` | Add a Bootstrap Confidence reference protocol with v1 scope, inputs, output fields, stop conditions, evidence rules, and deferred installer boundaries. | P0 | Protocol is the primary artifact. |
| `PRD-002-FR02` | Add `scripts/bootstrap-check.py` with `--source`, `--target`, `--json`, and `--write-evidence`. | P0 | Read-only by default. |
| `PRD-002-FR03` | The checker identifies source validity, target validity, target kind, public file groups, excluded paths, conflicts, missing dependencies, recommended next step, and stop conditions. | P0 | Plain output and JSON. |
| `PRD-002-FR04` | `--write-evidence` writes only `logs/bootstrap-check.json` and `logs/bootstrap-check.md` in the source Precode workspace. | P0 | No target writes. |
| `PRD-002-FR05` | Update guided setup, support runbook, troubleshooting, OS README, and file inventory to route first-time setup through the helper. | P0 | Beginner-facing docs. |
| `PRD-002-FR06` | Add fixture-style checks for the v1 inspection cases and no-write/default behavior. | P0 | Implemented as script self-test fixtures. |

### UX Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-002-UX01` | Human output uses plain language and names the first safe next action. | P0 | Avoid installer jargon. |
| `PRD-002-UX02` | Output clearly says the helper is read-only by default. | P0 | Prevents false confidence. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-002-SEC01` | The checker must not read or print secret file contents. | P0 | Path-level inspection only. |
| `PRD-002-SEC02` | Exclusion guidance must name secret and local-state patterns as do-not-copy material. | P0 | Matches guided setup. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-002-NFR01` | No active-memory changes are required for v1. | P0 | Preserves kernel. |
| `PRD-002-NFR02` | No target-project mutation occurs in any default or JSON mode. | P0 | `--write-evidence` still writes only to source logs. |
| `PRD-002-NFR03` | The thin manifest must not imply update-channel, release, or package-manager semantics. | P0 | Keep P1 manifest work deferred. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-002-FR01` | Protocol file exists with v1 scope, guardrails, and deferred work. | `validate-memory.sh` | Read protocol. | none | bead closeout |
| `PRD-002-FR02` | Checker accepts `--source`, `--target`, `--json`, and `--write-evidence`. | `python3 scripts/bootstrap-check.py --self-test` | Inspect help output if needed. | temp fixtures | check output |
| `PRD-002-FR03` | Checker reports required output fields. | `python3 scripts/bootstrap-check.py --self-test` | Review sample output. | temp fixtures | check output |
| `PRD-002-FR04` | Default writes nothing; explicit evidence writes source logs only. | `python3 scripts/bootstrap-check.py --self-test` | Inspect source logs if run manually. | temp fixtures | check output |
| `PRD-002-FR05` | Public docs and inventory reference bootstrap confidence. | `version-check.py`, `file-inventory.py --check` | Read updated docs. | none | bead closeout |
| `PRD-002-FR06` | Fixture scenarios pass. | `python3 scripts/bootstrap-check.py --self-test` | none | temp fixtures | check output |

## Risk And Permission Model

### Sensitive Surfaces

- Auth: none
- Payments: none
- User data: target projects may contain private files; checker must inspect paths only
- Uploads: none
- External services: none
- Secrets: path patterns are named as exclusions; contents are not read
- Destructive actions: none

### Human Approval Gates

- Approval required before:
  - copying any file group
  - overwriting existing project docs
  - installing Git hooks
  - adding or changing CI
  - editing active memory
  - writing generated evidence with `--write-evidence`
  - touching secrets, env files, dashboards, deployment settings, billing, auth, payments, or app code
- Stop if:
  - source and target are identical
  - source or target is missing
  - source is not a plausible PrecodeOS package checkout
  - target conflicts are present and unnamed
  - generated bootstrap output is treated as permission to mutate

### Tool And Environment Boundaries

- Allowed tools: local file reads, path inspection, git availability check, stdout JSON/plain output, explicit source-log evidence writing.
- Network needs: none.
- Dependency changes: none.
- Dashboard/manual steps: none.

## Architecture / Project Context Impact

- Project context impact: `minor`
- `PROJECT-CONTEXT.md` loaded: `not required`
- Architecture authority updates needed: `no`
- Route/API authority updates needed: `no`
- Schema authority updates needed: `no`
- Security authority updates needed: `no`
- Decision log updates needed: `no`

## Module / Interface Candidates

- `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md` owns the v1 setup-confidence contract.
- `scripts/bootstrap-check.py` owns the read-only inspection command and fixture self-tests.
- Public docs route users to the helper before copy or setup mutation.

## Agent Context Contract

- Primary authority file: `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
- Secondary reference files:
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/bootstrap-check.py`
  - `docs/PRECODE-OS-README.md`
- Files or folders out of scope:
  - target app code
  - package manager files
  - CI mutation
  - hooks installation
  - generated reports except explicit source-log evidence during tests
- Required checks:
  - `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
  - `bash scripts/record-check.sh -- python3 scripts/version-check.py`
  - `bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check`
  - `bash scripts/record-check.sh -- python3 scripts/public-repo-check.py`
  - `bash scripts/record-check.sh -- python3 scripts/bootstrap-check.py --self-test`
- Manual verification:
  - Confirm default bootstrap-check output is read-only and does not imply install permission.
- Forbidden assumptions:
  - A bootstrap confidence `pass` means files may be copied automatically.
  - A thin manifest means update channels or package-manager install semantics exist.
  - Generated bootstrap evidence is authority.

## Anti-Shallow Checks

- User problem named: yes
- Non-goals named: yes
- Before/after user moment clear: yes
- Requirements observable: yes
- Sensitive surfaces identified: yes
- Authority files identified: yes
- First bead can be one logical unit: yes
- Generated text reviewed by user: approved through maintainer implementation request

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B002-bootstrap-confidence-v1` | `PRD-002-FR01` through `PRD-002-FR06` | Protocol, checker, docs hooks, inventory entry, and fixture self-tests are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md` | validation commands plus self-test and manual docs review |

## Compilation Notes

- Feature entry: First-Run Confidence + Bootstrap v1.
- Functional requirements to add or amend: `PRD-002-FR01` through `PRD-002-FR06` after feature compilation.
- MVP slice notes: v1 is read-only setup confidence and docs integration only.
- Acceptance updates needed: none.

## Open Questions

Only include blockers that can change implementation.

| Question | Affects | Blocking? |
|---|---|---|
| Should v2 introduce a mutating copy flow after preview? | Follow-up scope | no |
| Should the thin manifest grow into install/update channel semantics? | P1 manifest scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-05-28
- Approval notes: User asked Codex to implement the P0 plan with B000 assumed accepted, Product Discovery first, and Bootstrap Confidence as read-only script plus docs.
