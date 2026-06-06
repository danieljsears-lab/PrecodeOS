---
prd_id: PRD-003
status: approved
owner: user
risk_level: medium
feature_link: Existing Repo Intake
features_status: not compiled
related_prds:
  - PRD-002
---

# PRD-003 -- Existing Repo Intake
<!-- ANCHOR: prd-003-existing-repo-intake -->

> AUTHORITY: Destination shard for the read-only Existing Repo Intake branch at the first PrecodeOS adoption fork.
> NOT_AUTHORITY: Active memory, task selection, bead activation, mutating installer behavior, target-project truth, product decisions, implementation acceptance, generated evidence truth, or release status.
> LOAD_WHEN: Reviewing, implementing, or decomposing the existing-repo intake workflow for adopting PrecodeOS into an app repository that already has code, docs, CI, product history, or active work.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-06

## State

- ID: `PRD-003`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-06`

## Feature Link

- Feature: `Existing Repo Intake`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-002`

## Source Inputs

- Source type: `roadmap evidence | guided discovery interview | setup/support evidence`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` candidate 4
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
- Stable facts:
  - Many builders will bring an existing app rather than start from an empty scaffold.
  - Bootstrap Confidence should remain the universal source/target preflight.
  - Existing repo adoption needs a first fork before file copying, owner-file adaptation, PRD shaping, bead creation, or app work.
  - V1 should report likely checks as future hints but not run them.
  - Explicit evidence writing should go only to the PrecodeOS source workspace.
- Assumptions:
  - A protocol plus read-only helper is enough for v1.
  - Existing Repo Intake should preserve project conventions rather than impose a Precode layout.
- Conflicts or stale inputs:
  - Existing setup docs treat existing projects as a setup variant; this PRD promotes it to a first adoption branch.
- Privacy or secrets redactions:
  - Helper must inspect sensitive paths only and must not read or print secret file contents.

## Alignment / Grilling Summary

- Alignment method: `guided maintainer discovery interview`
- Shared design concept: Existing Repo Intake is the existing-app branch immediately after Bootstrap Confidence confirms source and target.
- Key decisions reached:
  - Create a dedicated reference protocol.
  - Keep Bootstrap Confidence as the universal preflight.
  - Add a read-only helper script.
  - Report likely checks as future hints without running them.
  - Write generated evidence only to source-side logs when explicitly requested.
- Remaining implementation-changing questions:
  - none for v1.

## Domain Language

| Term | Meaning |
|---|---|
| Existing repo intake | Read-only app-understanding branch for a target repository that already has project material. |
| First adoption fork | The early choice between fresh install and existing repo intake after Bootstrap Confidence confirms source and target. |
| Likely checks | Commands inferred from manifests or config files as future verification hints; not executed during intake and not proof. |
| Owner-file adaptation | User-reviewed promotion of stable repo facts into Precode owner files without overwriting existing project material. |

## Problem

Existing app repositories are where beginners and agents are most likely to damage project history, conventions, docs, CI, package files, or active work. The current setup path names existing projects but does not provide a first-class intake branch or helper evidence before Precode files are copied and adapted.

## User Moment

- Before: A builder asks to add PrecodeOS to an existing app, and the agent may treat setup like a fresh install or start coding from incomplete repo understanding.
- After: The builder sees a read-only intake report naming current repo shape, app directories, stack, docs, likely checks, sensitive surfaces, conflicts, owner-file gaps, and the first safe next action.
- Why now: Roadmap candidate 4 ranks Existing Repo Intake as a P1 operating-loop improvement after Bootstrap Confidence makes source/target setup safer.

## Destination

- Destination statement: PrecodeOS has a first-class existing-repo adoption branch that preserves existing app conventions and produces read-only setup/adaptation evidence before mutation or implementation.
- Definition of done:
  - Existing Repo Intake protocol exists.
  - `scripts/existing-repo-intake.py` inspects source and target without target mutation by default.
  - The helper supports human output, `--json`, `--write-evidence`, and `--self-test`.
  - Guided setup and support docs present the first adoption fork.
  - Local Source Intake, Client Engagement Intake, Workflow Selection, Prompt Patterns, Troubleshooting, User Guide, and Package File Inventory reference the branch where appropriate.
  - Fixture checks cover missing source, missing target, same source/target, empty target, Node app, Python app, monorepo-like app, docs, CI hints, secret/env redaction, default no-write behavior, JSON shape, and explicit evidence writing.
- First useful vertical slice: read-only existing-repo intake and docs integration only.

## Users

- Primary user: Solo beginner or non-technical builder adopting PrecodeOS into an existing app.
- Secondary user: Support engineer or AI coding agent helping a builder preserve current repo conventions.
- Excluded user: Maintainers expecting app diagnostics, package-manager migration, mutating install, CI setup automation, or a project doctor command in v1.

## Goals

- Goal 1: Make the existing repo shape, app boundaries, conventions, likely checks, conflicts, and first safe next action visible before mutation.
- Goal 2: Keep v1 read-only and evidence-only.
- Goal 3: Preserve user ownership over product direction, topology decisions, owner-file facts, PRD approval, acceptance, and bead activation.

## Non-Goals

- Not doing: mutating installer, app-code edits, dependency installation, test/lint/build execution, CI mutation, Git hook installation, deployment, project doctor dashboard, package-manager migration, PRD approval, bead activation, or automatic owner-file adaptation.
- Deferred: richer install/update manifest integration, optional mutating setup after preview, and future CLI wrapper.
- Explicitly out of scope: Any change that treats generated intake as authority or permission to mutate.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-003-FR01` | Add an Existing Repo Intake reference protocol with first-fork scope, command contract, output fields, promotion path, stop conditions, and guardrails. | P0 | Protocol is the primary artifact. |
| `PRD-003-FR02` | Add `scripts/existing-repo-intake.py` with `--source`, `--target`, `--json`, `--write-evidence`, and `--self-test`. | P0 | Read-only by default. |
| `PRD-003-FR03` | The helper identifies repo topology, likely app directories, package managers, frameworks, runtimes, build tools, docs, CI/deploy hints, generated/ignored surfaces, sensitive path patterns, owner-file gaps, likely checks, conflicts, stop conditions, and recommended next step. | P0 | Plain output and JSON. |
| `PRD-003-FR04` | `--write-evidence` writes only `logs/existing-repo-intake.json` and `logs/existing-repo-intake.md` in the source Precode workspace. | P0 | No target writes. |
| `PRD-003-FR05` | Update setup, support, intake, workflow, prompt, troubleshooting, user, and inventory docs to route existing apps through the first adoption fork. | P0 | Beginner and support-facing. |
| `PRD-003-FR06` | Add fixture-style self-tests for v1 inspection, redaction, JSON shape, and no-write behavior. | P0 | Implemented as script self-test fixtures. |

### UX Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-003-UX01` | User-facing docs present a simple early choice: fresh install or existing app. | P0 | Avoid making users understand internals first. |
| `PRD-003-UX02` | Human output clearly says existing project files are preserved unless the user approves a narrow adaptation. | P0 | Reassurance is part of safety. |
| `PRD-003-UX03` | Output names likely checks as future hints, not completed verification. | P0 | Prevent false proof. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-003-SEC01` | The helper must not read or print secret file contents. | P0 | Path-level redaction only. |
| `PRD-003-SEC02` | Stop before setup mutation when secrets, auth, payments, deployment settings, private dashboards, CI mutation, or unclear ownership appear. | P0 | Support-safe. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-003-NFR01` | No active-memory changes are required for v1. | P0 | Preserves kernel. |
| `PRD-003-NFR02` | No target-project mutation occurs in any default, JSON, self-test, or source evidence mode. | P0 | Evidence writes source logs only. |
| `PRD-003-NFR03` | The helper must not execute app commands. | P0 | Intake is inspection only. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-003-FR01` | Protocol file exists with v1 scope, guardrails, adoption fork, and promotion path. | `validate-memory.sh` | Read protocol. | none | bead closeout |
| `PRD-003-FR02` | Helper accepts required flags. | `python3 scripts/existing-repo-intake.py --self-test` | Inspect help output if needed. | temp fixtures | check output |
| `PRD-003-FR03` | Helper reports required output fields and future-only likely checks. | `python3 scripts/existing-repo-intake.py --self-test` | Review sample output. | temp fixtures | check output |
| `PRD-003-FR04` | Default writes nothing; explicit evidence writes source logs only. | `python3 scripts/existing-repo-intake.py --self-test` | Inspect source logs if run manually. | temp fixtures | check output |
| `PRD-003-FR05` | Public docs and inventory reference existing-repo intake. | `version-check.py`, `file-inventory.py --check` | Read updated docs. | none | bead closeout |
| `PRD-003-FR06` | Fixture scenarios pass. | `python3 scripts/existing-repo-intake.py --self-test` | none | temp fixtures | check output |

## Risk And Permission Model

### Sensitive Surfaces

- Auth: may be detected by path/config hints only
- Payments: may be detected by path/config hints only
- User data: target repos may contain private files; helper must inspect paths and selected non-secret metadata only
- Uploads: path/config hints only
- External services: CI/deploy/config hints only
- Secrets: path patterns are named as sensitive; contents are not read
- Destructive actions: none

### Human Approval Gates

- Approval required before:
  - copying any Precode file group
  - overwriting or adapting existing project docs
  - installing Git hooks
  - adding or changing CI
  - editing active memory
  - writing generated evidence with `--write-evidence`
  - running inferred lint, test, build, typecheck, install, migration, or deployment commands
  - touching secrets, env files, dashboards, deployment settings, billing, auth, payments, or app code
- Stop if:
  - source and target are identical
  - source or target is missing
  - target is empty and should use fresh install path
  - existing project conflicts are unresolved
  - generated intake output is treated as permission to mutate

### Tool And Environment Boundaries

- Allowed tools: local path inspection, selected manifest/config metadata reads, stdout JSON/plain output, explicit source-log evidence writing.
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

- `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md` owns the v1 existing-repo intake contract.
- `scripts/existing-repo-intake.py` owns the read-only inspection command and fixture self-tests.
- Setup and support docs own the visible first adoption fork.

## Agent Context Contract

- Primary authority file: `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/existing-repo-intake.py`
  - `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md`
  - `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md`
  - `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
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
  - `bash scripts/record-check.sh -- python3 scripts/existing-repo-intake.py --self-test`
- Manual verification:
  - Confirm existing-repo docs present the first fork and do not imply install permission.
  - Confirm likely checks are future hints, not executed proof.
- Forbidden assumptions:
  - Existing Repo Intake approves file copying.
  - Likely checks have passed.
  - Generated intake evidence is authority.
  - Support can decide product direction, topology, PRD approval, acceptance, or bead activation.

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
| `B003-existing-repo-intake-v1` | `PRD-003-FR01` through `PRD-003-FR06` | Protocol, helper, docs hooks, inventory entry, and fixture self-tests are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md` | validation commands plus self-test and manual docs review |

## Compilation Notes

- Feature entry: Existing Repo Intake.
- Functional requirements to add or amend: `PRD-003-FR01` through `PRD-003-FR06` after feature compilation.
- MVP slice notes: v1 is read-only existing-repo intake and docs integration only.
- Acceptance updates needed: none.

## Open Questions

Only include blockers that can change implementation.

| Question | Affects | Blocking? |
|---|---|---|
| Should future setup support allow a mutating owner-file adaptation preview? | Follow-up scope | no |
| Should the helper integrate with future install/update manifest semantics? | P1 manifest scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-06
- Approval notes: User asked Codex to implement Existing Repo Intake as the first adoption fork after Bootstrap Confidence, with a dedicated protocol, read-only helper, source-side evidence, and support/user guidance.
