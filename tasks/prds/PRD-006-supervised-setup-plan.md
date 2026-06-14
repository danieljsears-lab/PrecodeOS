---
prd_id: PRD-006
status: approved
owner: user
risk_level: medium
feature_link: Installer / Bootstrap Experience
features_status: not compiled
related_prds:
  - PRD-002
  - PRD-003
  - PRD-004
---

# PRD-006 -- Supervised Setup Plan
<!-- ANCHOR: prd-006-supervised-setup-plan -->

> AUTHORITY: Destination shard for the non-mutating supervised setup-plan slice of the PrecodeOS Installer / Bootstrap Experience.
> NOT_AUTHORITY: Active memory, task selection, bead activation, target-project mutation, installer behavior, copy permission, package-manager release channels, rollback automation, implementation acceptance, or generated evidence truth.
> LOAD_WHEN: Reviewing, implementing, or decomposing the setup-plan layer after Bootstrap Confidence and install/update manifest preview.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## State

- ID: `PRD-006`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-14`

## Feature Link

- Feature: `Installer / Bootstrap Experience`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-002`, `PRD-003`, `PRD-004`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped bootstrap evidence`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item 1, `Installer / Bootstrap Experience`
  - `tasks/prds/PRD-002-bootstrap-confidence-lane.md`
  - `tasks/prds/PRD-003-existing-repo-intake.md`
  - `tasks/prds/PRD-004-install-update-manifest-preview.md`
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
- Stable facts:
  - Bootstrap Confidence confirms source, target, target kind, conflicts, exclusions, dependencies, and first safe next action.
  - Install/update manifest preview shows non-mutating action categories before any setup mutation.
  - Existing Repo Intake remains the first branch for targets with app code, docs, CI, product history, or active work.
  - The supervised setup plan must not copy files, adapt owner files, install hooks, change CI, create active memory, run app commands, write app code, define release channels, install a CLI, or provide rollback automation.
- Assumptions:
  - A setup-plan object inside `scripts/bootstrap-check.py` is enough for this slice.
  - Fresh or nearly empty targets can receive a non-mutating checklist; existing projects should remain gated behind Existing Repo Intake.
- Privacy or secrets redactions:
  - Setup planning remains path-level and must not read or print secret contents.

## Problem

Bootstrap Confidence and manifest preview show whether setup is inspectable and what categories of actions might be considered. They still leave a beginner or support engineer to translate preview categories into a first supervised setup checklist. That translation is a risk point: users may treat dry-run output as copy permission or skip the explicit approval gates that protect target projects.

## Destination

- Destination statement: PrecodeOS can produce a non-mutating supervised setup plan that lists candidate setup actions, owner-file adaptation prompts, approval gates, exclusions, blockers, and validation steps before any target mutation.
- Definition of done:
  - Supervised Setup Plan Protocol exists.
  - `scripts/bootstrap-check.py --supervised-setup-plan` implies manifest preview and adds a `supervised_setup_plan` payload.
  - Plain output is human-readable and clearly says the plan is evidence only, not copy permission.
  - Empty and nearly empty targets receive candidate setup actions and validation steps.
  - Existing projects are stopped at Existing Repo Intake before copy or adaptation becomes actionable.
  - Existing Precode targets are routed to memory validation, repair, or update decision instead of fresh setup.
  - Public setup, support, troubleshooting, package inventory, and prompt docs describe the plan without implying installer, CLI, release-channel, package-manager, rollback, hook, CI, active-memory, or app-code mutation behavior.
  - Fixture-style checks cover target states, JSON shape, default no-write behavior, source-only evidence writing, and evidence-only wording.
- First useful vertical slice: supervised setup-plan output and docs/protocol integration only.

## Users

- Primary user: Solo beginner or non-technical builder adopting PrecodeOS into a fresh or nearly empty project.
- Secondary user: Support engineer or AI coding agent converting bootstrap evidence into a visible checklist before asking for approval.
- Excluded user: Maintainers expecting automatic copying, update channels, installable CLI behavior, hook installation, CI setup automation, package rollback, or app-code edits.

## Goals

- Goal 1: Make the first supervised setup checklist visible before mutation.
- Goal 2: Preserve every setup step as user-approved manual work.
- Goal 3: Keep existing-project adoption gated behind Existing Repo Intake and conflict review.

## Non-Goals

- Not doing: mutating installer, package manager integration, installable `precode` CLI, release channels, rollback automation, Git hook installation, CI mutation, app-code changes, automatic owner-file adaptation, PRD approval, bead activation, or target writes.
- Deferred: actual supervised setup mutation, owner-file adaptation workflow, richer package-state metadata, version/channel trust language, rollback notes, and CLI wrapper design.
- Explicitly out of scope: Any change that treats setup-plan output as authority or permission to mutate.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-006-FR01` | Add a Supervised Setup Plan Protocol with scope, command contract, output fields, branch rules, approval gates, validation steps, and guardrails. | P0 | Protocol owns the plan contract. |
| `PRD-006-FR02` | Add `--supervised-setup-plan` to `scripts/bootstrap-check.py`; it implies `--preview-manifest`. | P0 | Read-only by default. |
| `PRD-006-FR03` | Setup-plan JSON includes `plan_kind`, `status`, `target_mutation_allowed`, `generated_evidence_only`, `actions`, `approval_gates`, `excluded_paths`, `blockers`, `validation_steps`, and `not_authority_for`. | P0 | Plain output and JSON. |
| `PRD-006-FR04` | Empty and nearly empty targets show candidate file-group setup actions, owner-file adaptation actions, exclusions, approval gates, and validation steps. | P0 | Planning only. |
| `PRD-006-FR05` | Existing projects stop at Existing Repo Intake before copy or owner-file adaptation actions become actionable. | P0 | Protects existing project truth. |
| `PRD-006-FR06` | Existing Precode targets route to memory validation, repair, or update decision rather than fresh setup. | P0 | Avoids accidental reinstall semantics. |
| `PRD-006-FR07` | `--write-evidence` remains source-only and writes no target files. | P0 | No target mutation. |
| `PRD-006-FR08` | Update setup, support, troubleshooting, prompt, and inventory docs to describe setup-plan boundaries. | P0 | Public docs stay aligned. |
| `PRD-006-FR09` | Add fixture-style self-tests for setup-plan target states, JSON shape, default no-write behavior, source-only evidence, and evidence-only wording. | P0 | Implemented in script self-test fixtures. |

## Risk And Permission Model

- Approval required before copying files, adapting owner files, overwriting existing docs, installing hooks, changing CI, editing active memory, running app commands, touching secrets, or writing app code.
- Stop if source and target are unclear, source equals target, target is missing, existing project conflicts are unresolved, Existing Repo Intake has not run for an existing project, or generated setup-plan output is treated as install permission.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.

## Module / Interface Candidates

- `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md` owns the setup-plan contract.
- `scripts/bootstrap-check.py` owns the `--supervised-setup-plan` command interface and fixture self-tests.
- Setup, support, troubleshooting, and prompt docs own the user-facing explanation of when to use the plan.

## Agent Context Contract

- Primary authority file: `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `tasks/reference/PROMPT-PATTERNS.md`
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
  - Confirm setup-plan output says it is evidence only and does not approve copying, overwriting, hooks, CI, active-memory edits, app commands, or app-code edits.
- Forbidden assumptions:
  - Setup-plan output approves setup mutation.
  - Supervised setup plan is an installer, release channel, package-manager contract, rollback plan, or CLI command.
  - Existing Repo Intake can be skipped for existing projects.

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B006-supervised-setup-plan` | `PRD-006-FR01` through `PRD-006-FR09` | Protocol, setup-plan command, docs hooks, inventory entry, and fixture self-tests are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md` | validation commands plus manual setup-plan review |

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should a future setup flow copy files itself or only produce copy commands? | Follow-up mutating setup scope | no |
| What owner-file adaptation workflow should exist for existing projects after intake? | Follow-up setup/adaptation scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-14
- Approval notes: User approved implementation of roadmap rank #1 as a supervised setup-plan layer, explicitly excluding target mutation, CLI/package-manager semantics, release channels, hooks, CI, rollback automation, and app-code edits.
