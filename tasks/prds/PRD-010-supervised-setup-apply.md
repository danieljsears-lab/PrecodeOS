---
prd_id: PRD-010
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
---

# PRD-010 -- Supervised Setup Apply v1
<!-- ANCHOR: prd-010-supervised-setup-apply -->

> AUTHORITY: Destination shard for the narrowly mutating, approval-gated setup apply slice of the PrecodeOS Installer / Bootstrap Experience.
> NOT_AUTHORITY: Active memory, task selection, bead activation, existing-repo mutation, owner-file adaptation approval, hook installation, CI mutation, app-code edits, release channels, package-manager behavior, rollback automation, implementation acceptance, or generated evidence truth.
> LOAD_WHEN: Reviewing, implementing, or decomposing the fresh/nearly-empty target setup apply layer after Bootstrap Confidence, manifest preview, and supervised setup plan.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## State

- ID: `PRD-010`
- Status: `approved`
- Owner: `user`
- Risk level: `high`
- Last updated: `2026-06-14`

## Feature Link

- Feature: `Installer / Bootstrap Experience`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-002`, `PRD-003`, `PRD-004`, `PRD-006`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped bootstrap evidence`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item 1, `Installer / Bootstrap Experience`
  - `tasks/prds/PRD-002-bootstrap-confidence-lane.md`
  - `tasks/prds/PRD-003-existing-repo-intake.md`
  - `tasks/prds/PRD-004-install-update-manifest-preview.md`
  - `tasks/prds/PRD-006-supervised-setup-plan.md`
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
- Stable facts:
  - Bootstrap Confidence, manifest preview, and supervised setup plan already keep setup inspection non-mutating by default.
  - The setup plan has stable action IDs and marks copy, adaptation, preserve, exclude, blocked, and deferred actions separately.
  - Existing projects must run Existing Repo Intake before any Precode copy or owner-file adaptation becomes actionable.
  - Hooks, CI, owner-file adaptation, app commands, app code, update channels, package-manager behavior, rollback automation, and CLI wrapper behavior remain deferred.
- Assumptions:
  - Fresh or nearly empty targets are enough for the first mutating setup slice.
  - Per-action approval is safer than one broad `--yes` or package-manager-style install command.
- Privacy or secrets redactions:
  - Setup apply must copy only approved package paths and must not read, print, or copy secret, credential, environment, local-agent, local-editor, cache, or generated-evidence paths.

## Problem

PrecodeOS can now explain setup, preview setup categories, and generate a supervised checklist, but a beginner still has to translate approved copy actions into manual filesystem work. That manual step is error-prone: a user or agent can copy too broadly, overwrite target material, include generated output, or confuse owner-file adaptation with safe package-file copying.

## Destination

- Destination statement: PrecodeOS can apply explicitly approved setup-plan copy actions into an empty or nearly empty target while refusing every broader installer, updater, owner-file adaptation, hook, CI, existing-repo, and app-code mutation.
- Definition of done:
  - PRD-010 exists and is linked to the earlier bootstrap PRDs.
  - Supervised Setup Apply Protocol exists.
  - `scripts/bootstrap-check.py --supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID>` applies only approved `review_copy_candidate` actions.
  - Apply mode refuses missing targets, same source/target, existing projects, existing Precode targets, blockers, unknown action IDs, unapproved actions, adaptation actions, deferred actions, excluded paths, hooks, CI, existing target paths, generated evidence, local state, secrets, and app code.
  - Default, JSON, manifest preview, and supervised setup-plan modes remain non-mutating unless apply mode is explicitly requested.
  - Apply output includes copied, skipped, blocked, and validation next-step fields.
  - Public setup, support, troubleshooting, package inventory, prompt, and protocol docs explain the apply command without implying package-manager, release-channel, rollback, CLI, hook, CI, owner-file adaptation, existing-repo mutation, app-command, or app-code behavior.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed as needed.
- First useful vertical slice: approved copy actions for fresh/nearly-empty targets only.

## Semantic Change Proposal

Semantic boundary changed: package setup mutation after non-mutating bootstrap evidence.

Affected owner files: `scripts/bootstrap-check.py`, `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md`, `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md`, `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`, setup/support/troubleshooting docs, package inventory, prompt patterns, README, roadmap, roadmap journal, and `_maintainer/CHANGELOG.md`.

Current authority: Bootstrap Confidence, manifest preview, and supervised setup plan are generated evidence only and do not copy files.

Proposed change: add an explicitly approved apply mode that copies only setup-plan `review_copy_candidate` paths into empty or nearly empty targets.

Preserved non-authority boundaries: no owner-file adaptation approval, existing-repo mutation, hooks, CI, app commands, app code, active-memory expansion, release channels, package-manager behavior, rollback automation, installable CLI, task selection, PRD approval, bead activation, implementation acceptance, or generated-evidence authority.

Validation evidence: embedded bootstrap self-tests, file inventory check, docs HTML freshness check, roadmap HTML check, and manual boundary review.

Docs/protocol/inventory follow-through: update setup protocols, public setup/support/troubleshooting docs, prompt patterns, package inventory, README setup pointers, generated docs HTML, generated PRD HTML, roadmap history, roadmap journal, and maintainer changelog.

Rollback or reversal path: remove the apply flags and apply helper from `scripts/bootstrap-check.py`, revert docs/protocol references to non-mutating setup-plan guidance, and leave Bootstrap Confidence, manifest preview, and setup-plan behavior intact.

Maintainer decision state: approved to implement.

## Users

- Primary user: Solo beginner or non-technical builder adopting PrecodeOS into a fresh or nearly empty project.
- Secondary user: Support engineer or AI coding agent applying approved safe copy actions after a human reviews the setup plan.
- Excluded user: Maintainer, package manager, updater, release-channel operator, CLI installer, hook installer, CI configurator, existing-repo migration tool, app-code generator, or rollback automation.

## Goals

- Goal 1: Make the safest first setup mutation visible, narrow, and reversible by ordinary Git inspection.
- Goal 2: Keep user approval attached to specific setup-plan action IDs.
- Goal 3: Preserve non-mutating defaults and existing-repo intake boundaries.

## Non-Goals

- Not doing: installable `precode` CLI, package manager, release channel, pinned version, update flow, rollback automation, registry, optional pack, hook installer, CI installer, app command runner, owner-file adaptation engine, existing-repo mutation, app-code mutation, or broad overwrite command.
- Deferred: existing-repo owner-file adaptation workflow, hook/CI setup, richer rollback notes, CLI wrapper, release-channel behavior, and package update semantics.
- Explicitly out of scope: treating generated setup-plan output as approval or treating apply output as proof that setup is valid without validation.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-010-FR01` | Add `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md`. | P0 | Owns mutation boundary. |
| `PRD-010-FR02` | Add `--apply-supervised-setup` and repeatable `--approve-action` to `scripts/bootstrap-check.py`. | P0 | Requires `--supervised-setup-plan`. |
| `PRD-010-FR03` | Apply only approved `review_copy_candidate` actions for `empty` or `nearly_empty` targets. | P0 | No owner-file adaptation. |
| `PRD-010-FR04` | Refuse blockers, unknown IDs, non-copy actions, existing targets, existing projects, existing Precode targets, same source/target, hooks, CI, app code, excluded paths, generated evidence, local state, and secrets. | P0 | No silent fallback. |
| `PRD-010-FR05` | Preserve non-mutating behavior for default, JSON, preview, plan, and source-side evidence modes unless apply is explicitly requested. | P0 | Backward compatibility. |
| `PRD-010-FR06` | Output copied, skipped, blocked, and validation next-step fields in plain text and JSON. | P0 | Inspectable result. |
| `PRD-010-FR07` | Update setup docs, protocols, prompt patterns, package inventory, README, maintainer changelog, roadmap history, roadmap journal, and generated HTML surfaces. | P0 | Follow-through required. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-010-FR02` | Apply mode requires supervised setup plan and explicit action approval. | `python3 scripts/bootstrap-check.py --self-test` | Inspect CLI help and error behavior. | temp fixtures | check output |
| `PRD-010-FR03` | Approved copy action copies only the named safe path. | `python3 scripts/bootstrap-check.py --self-test` | Inspect target fixture after apply. | empty target fixture | temp target |
| `PRD-010-FR04` | Existing projects, adaptation actions, missing approval, and overwrite attempts are blocked. | `python3 scripts/bootstrap-check.py --self-test` | Confirm blocked reasons are plain. | temp fixtures | check output |
| `PRD-010-FR05` | Non-apply modes remain non-mutating. | `python3 scripts/bootstrap-check.py --self-test` | Confirm default output still says read-only. | temp fixtures | check output |
| `PRD-010-FR07` | Docs, inventory, roadmap, and generated HTML stay fresh. | docs/roadmap/html checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before any setup apply action, owner-file adaptation, overwrite, hook installation, CI change, active-memory edit, app command, app-code edit, package update, rollback, release-channel change, or CLI installation.
- Stop if source, target, target kind, action ID, path safety, existing target material, excluded-path boundary, or validation next step is unclear.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `scripts/bootstrap-check.py` | `--supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID>` | Copies only approved safe setup-plan copy actions into empty/nearly empty targets. | self-test fixtures | `tasks/prds/PRD-010-supervised-setup-apply.md` |
| `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md` | Public mutation contract. | Names allowed actions, refusals, approvals, and validation. | source inspection and docs checks | PRD-010 |

## Agent Context Contract

- Primary authority file: `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md`
- Parent PRDs: `PRD-002`, `PRD-003`, `PRD-004`, `PRD-006`
- Secondary reference files:
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md`
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
  - `docs-html/`
  - `tasks/prds-html/`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
  - `_maintainer/PRECODE-ROADMAP.html`
- Files or folders out of scope:
  - `AGENT.md`
  - `DECISIONS.md`
  - `tasks/todo.md`
  - existing target app code
  - package manager files
  - hooks and CI mutation
  - generated setup logs except explicit source-side evidence
  - provider configuration, dashboards, secrets, credentials, environment files, billing, auth, payments, or private data
- Required checks:
  - `python3 scripts/bootstrap-check.py --self-test`
  - `python3 scripts/file-inventory.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
  - `python3 scripts/prd-html.py --check`
- Manual verification:
  - Confirm apply mode copies only approved setup-plan copy actions and cannot be mistaken for owner-file adaptation, package update, release, rollback, hooks, CI, CLI, package-manager, or existing-repo migration.
- Forbidden assumptions:
  - A setup plan is copy approval.
  - A broad `--yes` is acceptable.
  - Existing projects can be mutated before Existing Repo Intake.
  - Owner files can be adapted automatically.
  - A copied Precode layer is valid without memory validation.

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B010-supervised-setup-apply-v1` | `PRD-010-FR01` through `PRD-010-FR07` | PRD shard, apply protocol, bootstrap apply mode, self-tests, docs/protocol/inventory updates, changelog, roadmap history, generated PRD/docs/roadmap HTML, and validation are complete. | `human_in_loop` | `fixture_self_test` | `same_session_ok` | `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md` | bootstrap self-test plus static freshness checks |

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should a later command approve file groups instead of action IDs? | Follow-up ergonomics | no |
| Should existing-repo owner-file adaptation get its own separate apply protocol? | Follow-up existing-project setup | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-14
- Approval notes: User approved implementation of Supervised Setup Apply v1 as a narrow approval-gated mutation slice for fresh or nearly empty targets only, explicitly excluding existing-repo mutation, owner-file adaptation, hooks, CI, app code, release channels, package-manager behavior, rollback automation, installable CLI, and broad overwrite behavior.
