---
prd_id: PRD-009
status: approved
owner: user
risk_level: high
feature_link: Release Candidate Evidence Lane
features_status: not compiled
related_prds:
  - PRD-005
---

# PRD-009 -- Release Candidate Evidence Lane
<!-- ANCHOR: prd-009-release-candidate-evidence-lane -->

> AUTHORITY: Destination shard for the user-project release-candidate evidence profile within the Release Readiness lane.
> NOT_AUTHORITY: Active memory, task selection, bead activation, deployment approval, release approval, provider configuration, external mutation, rollback execution, implementation acceptance, generated report truth, package release management, or release-channel behavior.
> LOAD_WHEN: Reviewing, implementing, or decomposing the release-candidate evidence profile for nearly shippable user-project work.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## State

- ID: `PRD-009`
- Status: `approved`
- Owner: `user`
- Risk level: `high`
- Last updated: `2026-06-14`

## Feature Link

- Feature: `Release Candidate Evidence Lane`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-005`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped release-readiness lane`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Release Candidate Evidence Lane`
  - `tasks/prds/PRD-005-release-readiness-lane.md`
  - `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/beads/BEAD-SCHEMA.md`
- Stable facts:
  - Release Readiness / Shipping Lane v1 already prepares evidence and approval questions for user-project shipping decisions.
  - Release readiness does not deploy, approve release, mutate external systems, accept review, or activate the next bead.
  - Closeout Evidence, recorded checks, manual verification, smoke evidence, rollback or blocked escape, and explicit approval gates remain the proof and decision sources.
  - Generated reports, screenshots, browser notes, GitHub status, and profile text remain review input until recorded or accepted through existing evidence paths.
- Assumptions:
  - V1 should be profile-and-prompts only.
  - The owner surface is user-project shipping readiness, not PrecodeOS package release management.
  - PRD-005 and the Release Readiness Protocol remain the parent authority surfaces.
- Conflicts or stale inputs:
  - "Release candidate" can imply package release management or deployment automation. This PRD narrows the term to user-project evidence framing only.
- Privacy or secrets redactions:
  - Release-candidate evidence must not include secrets, tokens, private dashboard values, personal data samples, production credentials, or sensitive provider configuration.

## Problem

Release readiness names the shipping checklist, but nearly shippable work still lacks a compact candidate state that says what changed, what proof exists, what risk remains, and whether the work is ready for a human release decision.

Without that profile, a builder or agent can treat a loose release-readiness note as approval to ship, or can bury missing evidence inside long closeout text.

## User Moment

- Before: A completed bead has some checks and closeout evidence, but the user has to infer whether it is a release candidate, still missing evidence, blocked, or ready for a release decision.
- After: The agent prepares a release-candidate evidence profile that lists changed surfaces, proof, gaps, rollback or blocked escape, known risks, and approvals still required.
- Why now: Release Readiness v1 exists and explicitly deferred release-candidate evidence automation until a recurring evidence pattern was visible enough to name.

## Destination

- Destination statement: PrecodeOS gives release-relevant user-project work a named release-candidate evidence profile that prepares a human release decision without granting release authority.
- Definition of done:
  - PRD-009 exists and is linked to PRD-005.
  - Release Readiness Protocol defines the Release Candidate Evidence Profile fields and decision states.
  - Bead Schema includes optional release-candidate evidence guidance for release-relevant beads without adding required fields for ordinary beads.
  - Prompt Patterns and user-facing docs include copyable prepare/review prompts.
  - Package inventory lists PRD-009 and clarifies the profile is not generated proof or release approval.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed as needed.
- First useful vertical slice: human-authored evidence profile plus copyable prompts only.

## Users

- Primary user: Non-technical builder deciding whether nearly completed user-project work is ready for a release decision.
- Secondary user: AI coding agent or support helper preparing evidence without mutating external systems.
- Excluded user: Maintainer, deploy bot, release manager, or provider automation expecting package release management, release channels, deployment execution, rollback automation, GitHub mutation, generated reports, CLI wrappers, or provider-specific checklists.

## Goals

- Goal 1: Make release-candidate state explicit before shipping confidence outruns evidence.
- Goal 2: Keep missing evidence, blocked state, and remaining approvals visible.
- Goal 3: Preserve human authority over deployment, release, rollback, merge, migration, dashboard, secret, external, and post-release actions.

## Non-Goals

- Not doing: new checker, generated report, compiler output, release command, provider-specific checklist, deployment automation, rollback automation, CI release gate, GitHub mutation, dashboard mutation, package release management, CLI wrapper, package-manager behavior, release-channel behavior, or Release Readiness Skill behavior.
- Deferred: release-candidate evidence automation, richer release evidence reports, provider-specific release checklists, Verification And Release Evidence, and Release Readiness Skill.
- Explicitly out of scope: Any workflow that treats profile text, generated reports, screenshots, browser notes, GitHub status, or release-readiness notes as release approval.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-009-FR01` | Define a Release Candidate Evidence Profile inside the Release Readiness Protocol. | P0 | Human-authored profile only. |
| `PRD-009-FR02` | Include fields for candidate label, release target, changed surfaces, affected users/workflows, checks, smoke path, manual/browser verification, docs/support freshness, rollback or blocked escape, known risks, remaining uncertainty, and approvals still required. | P0 | Mirrors the approved plan. |
| `PRD-009-FR03` | Define decision states: `candidate`, `needs evidence`, `blocked`, and `ready for human release decision`. | P0 | These are framing states, not release approval. |
| `PRD-009-FR04` | Add optional bead-schema guidance for release-candidate evidence on release-relevant beads. | P0 | No new required field for ordinary beads. |
| `PRD-009-FR05` | Add copyable prepare/review prompts to prompt and user docs. | P0 | Prompts must prepare/review evidence, not approve release. |
| `PRD-009-FR06` | Update package inventory and generated public docs/PRD review surfaces. | P0 | Markdown remains canonical. |
| `PRD-009-FR07` | Record roadmap implemented history, roadmap journal card, and maintainer changelog follow-through. | P0 | Private maintainer history only. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-009-FR01` | Release Readiness Protocol includes a Release Candidate Evidence Profile section. | `python3 scripts/version-check.py` and docs freshness checks | Confirm profile fields are present and human-authored. | Protocol Markdown | protocol review |
| `PRD-009-FR03` | Decision states are framed as evidence status only. | source inspection | Confirm no state approves deployment, release, merge, migration, rollback, dashboard, secret, GitHub, or external mutation. | Protocol and prompts | manual boundary review |
| `PRD-009-FR05` | User-facing prompts prepare or review evidence without granting release authority. | docs HTML freshness check | Confirm prompts say prepare/review evidence and preserve explicit approval gates. | User docs and Prompt Patterns | manual boundary review |

## Risk And Permission Model

- Approval required before deployment, promotion, rollback, merge, migration, dashboard update, secret change, billing/auth/payment/private-data change, GitHub mutation, external-service mutation, production configuration change, or post-release owner action.
- Stop if the release target, affected users, changed surfaces, recorded checks, smoke path, manual/browser verification, docs/support freshness, rollback or blocked escape, known risks, approval owner, or post-release follow-up is unclear.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/RELEASE-READINESS-PROTOCOL.md` | Human-authored Release Candidate Evidence Profile. | Prepares evidence and approval questions only. | Source inspection and docs freshness checks. | `tasks/prds/PRD-009-release-candidate-evidence-lane.md` |
| User prompts | Copyable prepare/review profile prompts. | Ask agents for evidence framing without release action. | Manual boundary review. | `tasks/reference/PROMPT-PATTERNS.md` |

## Agent Context Contract

- Primary authority file: `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
- Parent PRD: `tasks/prds/PRD-005-release-readiness-lane.md`
- Secondary reference files:
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/beads/BEAD-SCHEMA.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `tasks/prds/PRD-009-release-candidate-evidence-lane.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
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
  - target app code
  - provider configuration
  - dashboards
  - secrets or environment files
  - GitHub mutation
  - deployment scripts
  - generated evidence reports
- Required checks:
  - `bash scripts/validate-memory.sh`
  - `python3 scripts/version-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
  - `python3 scripts/prd-html.py --check`
- Manual verification:
  - Confirm the profile prepares or reviews evidence only and does not authorize deployment, release, rollback, merge, migration, dashboard mutation, secret changes, GitHub mutation, provider automation, package release management, CLI wrapper behavior, package-manager behavior, release-channel behavior, or external mutation.
- Forbidden assumptions:
  - A release-candidate profile is release approval.
  - `ready for human release decision` means released, accepted, deployed, or merged.
  - A smoke path replaces manual approval.
  - Generated reports, screenshots, browser notes, GitHub status, or profile text are proof unless recorded or accepted through existing evidence paths.
  - PrecodeOS package releases define user-project release behavior.

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B009-release-candidate-evidence-lane` | `PRD-009-FR01` through `PRD-009-FR07` | PRD shard, protocol profile, bead guidance, user prompts, inventory, changelog, roadmap history, generated PRD/docs/roadmap HTML, and validation are complete. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/reference/RELEASE-READINESS-PROTOCOL.md` | static validation plus manual boundary review |

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should a future helper compile a release-candidate profile from Closeout Evidence? | Follow-up automation scope | no |
| Should provider-specific release checklists exist after the profile proves useful? | Follow-up release evidence scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-14
- Approval notes: User approved implementation of Release Candidate Evidence Lane v1 as a conservative user-project release-candidate evidence profile and prompts only, explicitly excluding a new checker, generated report, deployment helper, provider checklist, CLI, package-manager behavior, release-channel behavior, GitHub mutation, package release management, external-system mutation, and active-memory changes.
