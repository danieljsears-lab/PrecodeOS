---
prd_id: PRD-016
status: approved
owner: user
risk_level: high
feature_link: Installer / Bootstrap Experience
features_status: not compiled
related_prds:
  - PRD-002
  - PRD-003
  - PRD-004
  - PRD-006
  - PRD-010
  - PRD-013
---

# PRD-016 -- Installer / Bootstrap Experience Whole-Lane Closeout
<!-- ANCHOR: prd-016-installer-bootstrap-closeout -->

> AUTHORITY: Destination shard for closing the P0 Installer / Bootstrap Experience as staged, approval-gated bootstrap behavior.
> NOT_AUTHORITY: Active memory, broad installer behavior, target-project truth, owner-file adaptation approval, dirty package-file replacement, hook installation, CI mutation, app-code edits, release channels, package-manager behavior, rollback automation, implementation acceptance, or generated evidence truth.
> LOAD_WHEN: Reviewing, implementing, validating, or maintaining the final staged bootstrap lane closeout.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-15

## State

- ID: `PRD-016`
- Status: `approved`
- Owner: `user`
- Risk level: `high`
- Last updated: `2026-06-15`

## Feature Link

- Feature: `Installer / Bootstrap Experience`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-002`, `PRD-003`, `PRD-004`, `PRD-006`, `PRD-010`, `PRD-013`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped bootstrap evidence`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item 1, `Installer / Bootstrap Experience`
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md`
  - `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
- Stable facts:
  - Bootstrap Confidence, manifest preview, supervised setup plan, supervised setup apply, Existing Repo Intake, and the optional CLI wrapper already exist.
  - Setup behavior must remain source/target visible and must not hide filesystem changes.
  - Existing projects preserve project truth before owner-file adaptation or package copy decisions.
  - Dirty package-owned files are not safe automatic update candidates.
- Assumptions:
  - Whole-lane closeout means staged gates, not a broad installer.
  - Missing package-owned files in an existing Precode target are the only upgrade-copy mutation safe enough for this closeout slice.

## Problem

PrecodeOS has a safe fresh-target setup path, but the full bootstrap lane still needs a visible closeout for existing-project adaptation planning, package upgrade preview, partial setup recovery, and narrowly approved package-file copy gates. Without that closeout, support and agents can still confuse setup preview with install/update permission or recommend reinstall before narrow repair.

## Destination

- Destination statement: PrecodeOS closes the P0 bootstrap lane with non-mutating adaptation, upgrade, and recovery previews plus explicit action-ID mutation gates for the narrow cases that are safe.
- Definition of done:
  - PRD-016 exists and links the previously shipped bootstrap PRDs.
  - Bootstrap Closeout Protocol exists.
  - `scripts/bootstrap-check.py` supports `--existing-project-adaptation-plan`, `--upgrade-preview`, `--recovery-guidance`, and `--apply-upgrade-preview --approve-action <UP-ID>`.
  - Upgrade preview classifies existing Precode targets as `clean`, `dirty_package_edits`, `dirty_project_or_owner_edits`, `mixed_or_unknown`, or `blocked`.
  - Upgrade apply copies only explicitly approved missing package-owned files and refuses dirty/unknown package states, overwrites, owner-file adaptation, hooks, CI, app commands, app-code edits, release channels, package-manager behavior, and rollback automation.
  - Public setup, support, troubleshooting, architecture, prompt, protocol, package-inventory, README, changelog, roadmap, journal, and generated HTML surfaces are refreshed.
- First useful vertical slice: closeout behavior inside `scripts/bootstrap-check.py` with self-test coverage and docs/protocol follow-through.

## Semantic Change Proposal

Semantic boundary changed: package bootstrap closeout from fresh-target setup into existing-project adaptation planning, existing-Precode upgrade preview, and recovery guidance.

Affected owner files: `scripts/bootstrap-check.py`, `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md`, setup/intake protocols, setup/support/troubleshooting docs, package inventory, prompt patterns, README, roadmap, roadmap journal, and `_maintainer/CHANGELOG.md`.

Current authority: earlier bootstrap layers either inspect, preview, plan, or copy approved fresh-target setup actions.

Proposed change: add the final staged closeout modes while keeping dirty-package replacement, owner-file adaptation, hooks, CI, release channels, package-manager behavior, rollback automation, and broad installer semantics out of scope.

Preserved non-authority boundaries: no target-project truth from generated output, no automatic owner-file rewriting, no dirty package overwrite, no broad update command, no hook/CI mutation, no app commands, no app-code edits, no release-channel metadata, no package-manager behavior, no rollback automation, no PRD approval, no bead activation, no implementation acceptance, and no generated-evidence authority.

Validation evidence: bootstrap self-test, existing-repo-intake self-test, file inventory check, PRD HTML check, docs HTML check, roadmap HTML check, roadmap maintenance preview, and manual boundary review.

Rollback or reversal path: remove the new bootstrap-check flags and closeout protocol references while leaving PRD-002, PRD-003, PRD-004, PRD-006, PRD-010, and PRD-013 behavior intact.

Maintainer decision state: approved to implement.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-016-FR01` | Add Bootstrap Closeout Protocol. | P0 | Owns final lane boundary. |
| `PRD-016-FR02` | Add existing-project adaptation planning mode. | P0 | Non-mutating and intake-first. |
| `PRD-016-FR03` | Add package upgrade preview mode and classification. | P0 | Existing Precode targets only. |
| `PRD-016-FR04` | Add recovery guidance mode. | P0 | Support-assisted, non-mutating. |
| `PRD-016-FR05` | Add upgrade apply for approved missing package-owned files only. | P0 | Refuses dirty/unknown package states and overwrites. |
| `PRD-016-FR06` | Preserve existing bootstrap defaults and fresh-target apply behavior. | P0 | Backward compatibility. |
| `PRD-016-FR07` | Update public docs, protocols, inventory, prompt patterns, maintainer changelog, roadmap history, roadmap journal, and generated HTML. | P0 | Required follow-through. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-016-FR02` | Existing-project adaptation plan names owner adaptation candidates and remains non-mutating. | `python3 scripts/bootstrap-check.py --self-test` | Review output wording. | temp existing-project fixture | check output |
| `PRD-016-FR03` | Upgrade preview classifies clean, dirty owner, dirty package, mixed, and blocked states. | `python3 scripts/bootstrap-check.py --self-test` | Review JSON/plain output. | temp existing-Precode fixtures | check output |
| `PRD-016-FR04` | Recovery guidance names support steps and forbidden actions without rollback automation. | `python3 scripts/bootstrap-check.py --self-test` | Read recovery output. | temp fixtures | check output |
| `PRD-016-FR05` | Upgrade apply copies approved missing package-owned files and refuses dirty/unknown package states. | `python3 scripts/bootstrap-check.py --self-test` | Inspect target fixture after apply. | temp existing-Precode fixture | temp target |
| `PRD-016-FR07` | Docs, inventory, PRD HTML, roadmap, journal, and generated HTML stay fresh. | docs/PRD/roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Agent Context Contract

- Primary authority file: `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md`
- Parent PRDs: `PRD-002`, `PRD-003`, `PRD-004`, `PRD-006`, `PRD-010`, `PRD-013`
- Secondary reference files:
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md`
  - `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md`
  - `tasks/reference/SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/bootstrap-check.py`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `README.md`
  - `docs/PRECODE-ARCHITECTURE-OVERVIEW.md`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
- Files or folders out of scope:
  - target app code
  - package manager files
  - release-channel metadata
  - hooks and CI mutation
  - dirty package-file overwrite
  - automatic owner-file adaptation
  - rollback automation
- Required checks:
  - `python3 scripts/bootstrap-check.py --self-test`
  - `python3 scripts/existing-repo-intake.py --self-test`
  - `python3 scripts/file-inventory.py --check`
  - `python3 scripts/prd-html.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
  - `python3 _maintainer/scripts/roadmap-maintenance.py`
- Manual verification:
  - Confirm preview modes write no target files.
  - Confirm mutation requires explicit action IDs and refuses dirty/unknown package states.
  - Confirm docs do not imply installer, updater, release-channel, package-manager, rollback, hook/CI, or owner-file adaptation authority.

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B016-installer-bootstrap-closeout` | `PRD-016-FR01` through `PRD-016-FR07` | Protocol, script modes, self-tests, docs/protocol/inventory updates, changelog, roadmap history, generated PRD/docs/roadmap HTML, and validation are complete. | `human_in_loop` | `fixture_self_test` | `same_session_ok` | `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md` | bootstrap self-test plus static freshness checks |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-15
- Approval notes: User approved implementation of the P0 Installer / Bootstrap Experience whole-lane closeout as staged gated behavior, explicitly not a broad installer.
