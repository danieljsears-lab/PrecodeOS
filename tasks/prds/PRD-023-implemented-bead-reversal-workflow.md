---
prd_id: PRD-023
status: approved
owner: user
risk_level: medium
feature_link: Implemented Bead Reversal Workflow
features_status: not compiled
related_prds:
  - PRD-017
  - PRD-020
---

# PRD-023 -- Implemented Bead Reversal Workflow
<!-- ANCHOR: prd-023-implemented-bead-reversal-workflow -->

> AUTHORITY: Destination shard for reversing or superseding already-implemented Precode beads through a separate normal bead.
> NOT_AUTHORITY: Active memory, task selection, bead activation, transition approval, implementation acceptance, Git history truth, rollback automation, evidence deletion, transition-log mutation, generated-output authority, package-manager behavior, release-channel behavior, or a runtime reversal command.
> LOAD_WHEN: Reviewing, implementing, or decomposing the workflow for undoing, reversing, or superseding an already-implemented bead.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## State

- ID: `PRD-023`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-23`

## Feature Link

- Feature: `Implemented Bead Reversal Workflow`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-017`, `PRD-020`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Implemented Bead Reversal Workflow`
  - `tasks/beads/BEAD-SCHEMA.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/RECOVERY-PROTOCOL.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/BEAD-BUILD-JOURNAL-PROTOCOL.md`
- Stable facts:
  - A completed bead is historical evidence and should not be reopened to hide that it happened.
  - Reversal work must happen through a separate bead with its own scope, checks, closeout, review, and generated evidence.
  - Git operations can be part of implementation, but Git history alone is not proof that the user-visible or package behavior is correct.
- Assumptions:
  - V1 should update protocols, docs, advisory checker output, generated journal rendering, and deterministic fixtures.
  - V1 should not add a command that performs reversal.

## Problem

Implemented beads can later prove wrong, obsolete, or harmful. Without a reusable workflow, agents may casually reopen a done bead, delete evidence, rewrite transition history, or treat `git revert` as a complete recovery.

## User Moment

- Before: The user says an already-implemented bead needs to be undone, and the agent has no stable path that preserves history and requires fresh proof.
- After: The agent diagnoses the issue, creates or proposes a separate reversal bead, preserves the original bead as historical evidence, and proves the reversal with normal checks, closeout, review, and journal evidence.
- Why now: PrecodeOS already has closeout, review, recovery, verification, and implemented-bead path surfaces; the missing piece is the explicit reversal pattern.

## Destination

- Destination statement: PrecodeOS reverses or supersedes implemented work through a separate normal bead, preserving prior evidence while requiring fresh proof for the reversal.
- Definition of done:
  - This PRD exists and owns the workflow.
  - Bead Schema defines reversal/supersession vocabulary and the required reversal bead fields.
  - Completion/Handoff, Recovery, Verification Guardrail, and Bead Build Journal protocols explain the workflow and non-authority boundaries.
  - Public user, daily cockpit, troubleshooting, support, inventory, and log-taxonomy docs expose the guidance.
  - `completion-check.py` exposes advisory reversal-workflow warnings through `scripts/os_compiler.py`.
  - `update-bead-build-journal.py` renders reversal/supersession provenance when a reversal bead records it.
  - Clarity scenarios cover complete, incomplete, Git-revert-only, done-bead-reopen, evidence-deletion, transition-log-rewrite, and non-approval behavior.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed.
- First useful vertical slice: workflow guidance, advisory checker warnings, journal provenance rendering, and deterministic fixtures only.

## Domain Language

| Term | Meaning |
|---|---|
| `reversal bead` | A separate normal bead that undoes, removes, replaces, or supersedes already-implemented work. |
| `superseded bead` | The prior implemented bead whose outcome is being reversed or replaced. It remains historical evidence. |
| `reversal target` | The exact prior bead, behavior, files, docs, or package surface being undone or superseded. |
| `reversal reason` | The evidence-backed reason the prior implementation is now wrong, obsolete, harmful, or no longer wanted. |
| `preserved behavior` | Behavior, evidence, logs, docs, or state that must not be damaged by the reversal. |

## Goals

- Preserve original implemented beads, logs, journal entries, and transition evidence as history.
- Make the reversal target, reason, preserved behavior, checks, manual verification, and approval status visible before acceptance.
- Keep reversal inside the existing one-active-bead, closeout, review, and transition model.
- Prevent Git history operations from becoming completion proof by themselves.

## Non-Goals

- Not doing: new bead state, reopening `done` beads, deleting evidence, rewriting transition logs, automatic Git revert, runtime reversal command, rollback automation, cleanup apply, package update behavior, release channels, package-manager behavior, registry behavior, optional-pack behavior, PRD approval, bead activation, implementation acceptance, transition approval, or external mutation.
- Contract wording: do not reopen done beads, do not delete evidence, do not rewrite transition logs, and add no runtime reversal command.
- Deferred: richer generated relationship graphs, dedicated reversal templates, stricter parser fields, or script-assisted bead proposal generation.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-023-FR01` | A reversal must be represented as a separate normal bead, not by reopening the prior `done` bead. | P0 | Existing bead states stay unchanged. |
| `PRD-023-FR02` | The reversal bead must name the superseded bead, reversal target, reversal reason, preserved behavior, checks, manual verification, and approvals still required. | P0 | Human-readable fields may live in bead body or Closeout Evidence. |
| `PRD-023-FR03` | Completion/Handoff and Recovery guidance must route bad implemented work into diagnosis followed by a new reversal bead. | P0 | No destructive repair by default. |
| `PRD-023-FR04` | Verification guidance must state that Git revert alone is review input, not proof. | P0 | Fresh recorded checks are required. |
| `PRD-023-FR05` | `completion-check.py` must expose advisory reversal-workflow details through existing compiled completion/handoff output. | P1 | No new command or report. |
| `PRD-023-FR06` | The bead build journal must render reversal/supersession provenance when recorded by a reversal bead. | P1 | Generated evidence only. |
| `PRD-023-FR07` | Public user, troubleshooting, support, daily cockpit, inventory, and log-taxonomy guidance must expose the reversal path. | P1 | Discoverable without maintainer files. |
| `PRD-023-FR08` | Clarity scenarios must pin advisory-only and forbidden-action boundaries. | P1 | Deterministic local regression. |
| `PRD-023-FR09` | Roadmap, roadmap journal, maintainer changelog, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-023-SEC01` | Reversal guidance must not approve destructive commands, rollback, evidence deletion, transition-log rewrite, setup/update mutation, GitHub mutation, external mutation, secrets handling, or deployment changes. | P0 | Explicit user approval remains required. |
| `PRD-023-SEC02` | Reversal guidance must not make generated evidence, Git history, or maintainer-private roadmap files authoritative for public package work. | P0 | Markdown owner files remain canonical. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-023-NFR01` | The workflow must be short enough for a non-technical builder to ask for in live chat. | P0 | Avoid heavy ceremony. |
| `PRD-023-NFR02` | The implementation must not add new active memory or new state vocabulary. | P0 | Existing states remain stable. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-023-FR01` | Reversal guidance says the prior bead remains `done` and a separate reversal bead does the work. | `python3 scripts/clarity-scenario-check.py` | Read Bead Schema and protocols. | Markdown source | check output |
| `PRD-023-FR04` | Git-revert-only closeout produces advisory warning. | `python3 scripts/clarity-scenario-check.py` | Inspect warning. | Synthetic bead fixture | check output |
| `PRD-023-FR05` | `completion-check.py` exposes `reversal_workflow` details. | `python3 scripts/clarity-scenario-check.py`; `python3 scripts/completion-check.py` | Inspect JSON shape. | Synthetic and active state | command output |
| `PRD-023-FR06` | Journal rendering includes reversal/supersession provenance when recorded. | `python3 scripts/clarity-scenario-check.py` | Review generated Markdown sample if needed. | Synthetic entry | check output |
| `PRD-023-FR07` | Public docs expose copyable guidance without automation claims. | docs HTML check | Read user/support docs. | Markdown docs | generated docs HTML |
| `PRD-023-FR09` | Inventory, roadmap, journal, changelog, and generated surfaces are current. | inventory, docs, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before destructive local commands, GitHub mutation, external mutation, deployment, migration, setup/update mutation, evidence deletion, transition-log editing, or package release action.
- Stop if the superseded bead, reversal target, reversal reason, preserved behavior, proof path, manual verification, or approval owner is unclear.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| Bead and completion protocols | Reversal bead field expectations. | Separate bead, original history preserved. | Text-contract and manual review. | `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md` |
| `scripts/completion-check.py` via `scripts/os_compiler.py` | Advisory `reversal_workflow` warnings. | Warns without approving reversal or mutation. | Clarity scenarios. | `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md` |
| `scripts/update-bead-build-journal.py` | Reversal provenance in generated journal entries. | Renders recorded provenance only. | Clarity scenario render check. | `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md`
- Secondary reference files:
  - `tasks/beads/BEAD-SCHEMA.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/RECOVERY-PROTOCOL.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/BEAD-BUILD-JOURNAL-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/os_compiler.py`
  - `scripts/update-bead-build-journal.py`
  - `scripts/clarity-scenario-check.py`
  - `logs/LOG-EVIDENCE-TAXONOMY.md`
  - `tasks/prds-html/`
  - `docs-html/`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
  - `_maintainer/PRECODE-ROADMAP.html`
- Files or folders out of scope:
  - `AGENT.md`
  - `DECISIONS.md`
  - `tasks/todo.md`
  - transition logs
  - generated evidence ledgers
  - target app code
  - setup/update scripts
  - deployment scripts
  - GitHub resources
  - external systems
- Required checks:
  - `bash scripts/validate-memory.sh`
  - `python3 scripts/version-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 scripts/public-repo-check.py`
  - `python3 scripts/clarity-scenario-check.py`
  - `python3 scripts/completion-check.py`
  - `python3 scripts/prd-html.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`

## Anti-Shallow Checks

- If the reversal does not name the superseded bead, it is too vague.
- If the reversal does not name preserved behavior, it is too risky.
- If a Git revert is treated as proof without recorded checks and manual verification, it violates this PRD.
- If the workflow deletes evidence, rewrites logs, reopens a `done` bead, or mutates transition history, it violates this PRD.

## Bead Proposals

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B023-implemented-bead-reversal-workflow` | `PRD-023-FR01` through `PRD-023-FR09`, `PRD-023-SEC01` through `PRD-023-SEC02`, `PRD-023-NFR01` through `PRD-023-NFR02` | PRD shard, protocol guidance, public docs, advisory checker warnings, journal provenance rendering, clarity scenario coverage, maintainer history, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md` | clarity scenario, completion-check, package/docs/roadmap checks |

## Open Questions

- None for v1.

## Approval

- Approval state: approved by maintainer implementation request on 2026-06-23.
