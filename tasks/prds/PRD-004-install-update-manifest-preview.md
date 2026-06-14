---
prd_id: PRD-004
status: approved
owner: user
risk_level: medium
feature_link: Install/Update Manifest And Dry-Run Preview
features_status: not compiled
related_prds:
  - PRD-002
  - PRD-003
---

# PRD-004 -- Install/Update Manifest And Dry-Run Preview
<!-- ANCHOR: prd-004-install-update-manifest-preview -->

> AUTHORITY: Destination shard for the non-mutating install/update manifest and dry-run preview slice of the PrecodeOS Installer / Bootstrap Experience.
> NOT_AUTHORITY: Active memory, task selection, bead activation, mutating installer behavior, package-manager release channels, update permission, target-project truth, implementation acceptance, or generated evidence truth.
> LOAD_WHEN: Reviewing, implementing, or decomposing the manifest + preview layer between Bootstrap Confidence and any future supervised setup mutation.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## State

- ID: `PRD-004`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-14`

## Feature Link

- Feature: `Install/Update Manifest And Dry-Run Preview`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-002`, `PRD-003`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped bootstrap evidence`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item 2, `Installer / Bootstrap Experience`
  - `tasks/prds/PRD-002-bootstrap-confidence-lane.md`
  - `tasks/prds/PRD-003-existing-repo-intake.md`
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
- Stable facts:
  - Bootstrap Confidence is already read-only and source/target oriented.
  - Existing Repo Intake is already the first branch for targets with app code, docs, CI, product history, or active work.
  - Any setup trust layer must not hide filesystem changes or imply install permission.
  - Hooks, CI, app code, active memory edits, package-manager semantics, release channels, and CLI installation remain outside this slice.
- Assumptions:
  - A dry-run manifest preview inside `scripts/bootstrap-check.py` is enough for this slice.
  - Future mutating setup should depend on this preview contract rather than inventing a separate operating model.
- Conflicts or stale inputs:
  - Earlier docs use "install/update manifest" as deferred roadmap language; this PRD narrows the first shipped slice to dry-run preview only.
- Privacy or secrets redactions:
  - Preview must remain path-level and must not read or print secret contents.

## Problem

Bootstrap Confidence tells a builder whether source, target, conflicts, exclusions, dependencies, and next action are visible. It does not yet show the concrete setup-action categories that would make a later supervised setup trustworthy. Without a dry-run manifest, users can still confuse "safe to inspect" with "safe to copy."

## Destination

- Destination statement: PrecodeOS has a non-mutating install/update manifest preview that shows candidate setup actions before any target mutation.
- Definition of done:
  - Install/Update Manifest Protocol exists.
  - `scripts/bootstrap-check.py --preview-manifest` adds a preview payload and plain output.
  - Preview output uses explicit action categories: `copy_candidate`, `adapt_candidate`, `preserve_existing`, `exclude`, `blocked`, and `deferred`.
  - Existing projects are routed through Existing Repo Intake before copy or adaptation becomes actionable.
  - Public setup, support, troubleshooting, and package inventory docs describe the preview without implying installer, CLI, release-channel, package-manager, rollback, hook, CI, active-memory, or app-code mutation behavior.
  - Fixture-style checks cover target kinds, JSON shape, default no-write behavior, and source-only evidence writing.
- First useful vertical slice: dry-run manifest preview and docs/protocol integration only.

## Users

- Primary user: Solo beginner or non-technical builder adopting PrecodeOS into a project.
- Secondary user: Support engineer or AI coding agent explaining setup choices before file mutation.
- Excluded user: Maintainers expecting a package manager, updater, installable CLI, mutating copy flow, hook installer, CI setup automation, release channel, or rollback command.

## Goals

- Goal 1: Make candidate setup actions visible before mutation.
- Goal 2: Preserve Bootstrap Confidence and Existing Repo Intake as read-only evidence workflows.
- Goal 3: Prevent manifest language from implying release, update, package-manager, CLI, or copy approval semantics.

## Non-Goals

- Not doing: mutating installer, package manager integration, installable `precode` CLI, release channels, pinned versions, rollback automation, Git hook installation, CI mutation, app-code changes, automatic owner-file adaptation, PRD approval, bead activation, or target writes.
- Deferred: supervised setup mutation after preview, richer package-state semantics, version/channel trust language, rollback notes, and CLI wrapper design.
- Explicitly out of scope: Any change that treats preview output as authority or permission to mutate.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-004-FR01` | Add an Install/Update Manifest Protocol with scope, command contract, action categories, branch rules, stop conditions, and guardrails. | P0 | Protocol owns the preview contract. |
| `PRD-004-FR02` | Add `--preview-manifest` to `scripts/bootstrap-check.py`. | P0 | Read-only by default. |
| `PRD-004-FR03` | Preview output includes action categories, actions, generated-evidence fields, non-authority fields, and next setup gate. | P0 | Plain output and JSON. |
| `PRD-004-FR04` | Existing project preview defers copying and routes to Existing Repo Intake before adaptation. | P0 | Protects existing project truth. |
| `PRD-004-FR05` | `--write-evidence` remains source-only and writes no target files. | P0 | No target mutation. |
| `PRD-004-FR06` | Update setup, support, troubleshooting, and inventory docs to describe preview boundaries. | P0 | Public docs stay aligned. |
| `PRD-004-FR07` | Add fixture-style self-tests for preview target states, JSON shape, default no-write behavior, and source-only evidence. | P0 | Implemented in script self-test fixtures. |

## Risk And Permission Model

- Approval required before copying files, adapting owner files, overwriting existing docs, installing hooks, changing CI, editing active memory, running app commands, touching secrets, or writing app code.
- Stop if source and target are unclear, source equals target, target is missing, existing project conflicts are unresolved, Existing Repo Intake has not run for an existing project, or generated preview output is treated as install permission.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.

## Module / Interface Candidates

- `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md` owns the dry-run manifest contract.
- `scripts/bootstrap-check.py` owns the `--preview-manifest` command interface and fixture self-tests.
- Setup and support docs own the user-facing explanation of when to run the preview.

## Agent Context Contract

- Primary authority file: `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/bootstrap-check.py`
- Files or folders out of scope:
  - target app code
  - package manager files
  - CI mutation
  - hooks installation
  - generated reports except explicit source-log evidence during tests
- Required checks:
  - `python3 scripts/bootstrap-check.py --self-test`
  - `python3 scripts/existing-repo-intake.py --self-test`
  - `python3 scripts/version-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
- Manual verification:
  - Confirm preview output says it is evidence only and does not approve copying, overwriting, hooks, CI, active-memory edits, app commands, or app-code edits.
- Forbidden assumptions:
  - Manifest preview approves setup mutation.
  - Manifest preview is a release channel, update manifest, package-manager contract, rollback plan, or CLI command.
  - Existing Repo Intake can be skipped for existing projects.

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B004-install-update-manifest-preview` | `PRD-004-FR01` through `PRD-004-FR07` | Protocol, preview command, docs hooks, inventory entry, and fixture self-tests are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md` | validation commands plus manual preview review |

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should a future supervised setup flow copy files itself or only produce copy commands? | Follow-up scope | no |
| Should future package-state metadata include version/channel language? | Follow-up manifest scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-14
- Approval notes: User approved implementation of the roadmap rank #2 Installer / Bootstrap Experience slice as manifest + dry-run preview, explicitly excluding target mutation, CLI/package-manager semantics, release channels, hooks, CI, rollback automation, and app-code edits.
