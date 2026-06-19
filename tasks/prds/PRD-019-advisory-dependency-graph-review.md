---
prd_id: PRD-019
status: approved
owner: user
risk_level: medium
feature_link: Advisory Dependency Graph Review
features_status: not compiled
related_prds:
  - PRD-018
---

# PRD-019 -- Advisory Dependency Graph Review
<!-- ANCHOR: prd-019-advisory-dependency-graph-review -->

> AUTHORITY: Destination shard for the advisory Dependency Graph Review Lane.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, review acceptance, implementation acceptance, generated proof, Work Graph authority, parallel execution approval, follow-up task creation, owner-file rewrite, external mutation, GitHub mutation, package-manager behavior, or a task-runner system.
> LOAD_WHEN: Reviewing, implementing, or decomposing the Advisory Dependency Graph Review package capability.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-19

## State

- ID: `PRD-019`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-19`

## Feature Link

- Feature: `Advisory Dependency Graph Review`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-018`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped Work Graph and Review Lanes guidance`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Advisory Dependency Graph Review`
  - `_maintainer/PRECODE-KIRO-COMPARISON.md` task-wave/dependency-graph research context
  - `tasks/reference/REVIEW-LANES-PROTOCOL.md`
  - `tasks/reference/DECOMPOSITION-PROTOCOL.md`
  - `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
  - `logs/work-graph.md` generated evidence contract
- Stable facts:
  - Work Graph reports already compile bead, PRD, owner-file, check, blocker, follow-up, and transition relationships as generated evidence only.
  - Review Lanes already provide advisory review output fields without acceptance, release, security, or task authority.
  - Decomposition already names dependency terms and protects one active bead per checkout.
  - Small Team Collaboration already limits parallel work to branch/worktree-isolated teammate contexts after coordinator approval.
- Assumptions:
  - The first useful slice should be a review lane over existing graph evidence, not new graph compiler behavior.
  - Text-contract checks are enough for v1.
  - Generated Work Graph output can be stale and must be repaired through owner files and regeneration, not treated as authority.
- Conflicts or stale inputs:
  - Dependency graph language can sound like a project-management tracker or parallel task runner. V1 must explicitly refuse that interpretation.
  - Generated Work Graph warnings may be useful review input, but they are not proof, acceptance, task selection, or transition approval.
- Privacy or secrets redactions:
  - The lane must not require secrets, credentials, private data, dashboard values, production configuration, or external-system access.

## Problem

Related beads, PRDs, owner files, checks, blockers, follow-ups, and transition notes can be hard to inspect from a flat task list.

PrecodeOS needs a small advisory review lane that helps users see blocked, duplicate, out-of-order, broad, stale, or unsafe parallel assumptions before acting.

## User Moment

- Before: A builder or agent sees graph warnings, broad files in play, follow-up notes, or dependency hints and guesses whether work can continue.
- After: The review names relationship risks, missing proof, acceptance questions, approval still required, and the promotion path without choosing work or approving transitions.
- Why now: Work Graph and Review Lanes are shipped, and Decomposition/Team Collaboration boundaries are mature enough to support a narrow dependency-graph review without new automation.

## Destination

- Destination statement: PrecodeOS exposes a Dependency Graph Review Lane that reviews one active bead's relationship evidence before action while preserving owner-file authority and human approval.
- Definition of done:
  - PRD-019 exists as the destination shard.
  - Review Lanes Protocol includes Dependency Graph Review Lane as an optional third lane.
  - Prompt Patterns and User Guide include copyable lane guidance.
  - Package inventory lists PRD-019 and the expanded review-lane behavior.
  - Clarity scenario coverage checks lane name, output fields, evidence-only Work Graph boundary, recommendation values, and forbidden actions.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed.
- First useful vertical slice: protocol/prompt guidance and text-contract checks only.

## Users

- Primary user: Non-technical builder or maintainer reviewing whether one active bead's relationship evidence is coherent enough to continue, review, split, or stop.
- Secondary user: AI coding agent or support helper preparing dependency questions without mutating the repo.
- Excluded user: Project manager, scheduler, deploy bot, graph automation, parallel task runner, or agent platform expecting graph output to choose work.

## Goals

- Goal 1: Make dependency, blocker, follow-up, owner-file, check, and stale-graph risks visible before action.
- Goal 2: Keep Work Graph reports evidence-only and subordinate to owner files.
- Goal 3: Preserve one-active-bead and human transition approval boundaries.
- Goal 4: Avoid new compiler warnings, generated report fields, `next-step.py` routing, or team automation in v1.

## Non-Goals

- Not doing: new command, generated report, compiler integration, `next-step.py` integration, graph tracker, task scheduler, parallel execution system, required bead metadata, project-management layer, GitHub mutation, external mutation, task creation, transition approval, acceptance approval, owner-file rewrite, optional pack, registry, package-manager behavior, or release-channel behavior.
- Deferred: fixture-backed Work Graph warning expansion, small-team scenario integration, richer owner-file overlap detection, generated graph review summaries, and deeper requirement-to-proof traceability.
- Explicitly out of scope: treating Work Graph output as authority, proof, task selection, transition approval, or permission to run parallel work.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-019-FR01` | Add Dependency Graph Review Lane to Review Lanes Protocol as an optional advisory lane for one active bead. | P0 | Owner protocol update. |
| `PRD-019-FR02` | Lane input guidance must include active bead, primary authority, changed-file summary or files in play, Work Graph evidence when available, relevant PRD/bead references, and recorded checks. | P0 | Keeps findings grounded. |
| `PRD-019-FR03` | Lane output must use the existing Review Lanes output fields and recommendation values. | P0 | Stable review shape. |
| `PRD-019-FR04` | Lane focus must include blocked work, missing or non-done dependencies, duplicate or out-of-order work, broad files in play, unsafe parallel assumptions, ambiguous follow-up destination, owner-file overlap, and stale generated graph evidence. | P0 | Review substance. |
| `PRD-019-FR05` | Prompt Patterns and User Guide must include copyable Dependency Graph Review Lane guidance. | P0 | User-facing invocation. |
| `PRD-019-FR06` | Package inventory must list PRD-019 and the expanded Review Lanes Protocol behavior. | P1 | Discoverability. |
| `PRD-019-FR07` | Clarity scenario coverage must check lane name, output fields, evidence-only Work Graph boundary, recommendation values, and forbidden actions. | P1 | Text contract only. |
| `PRD-019-FR08` | Roadmap, roadmap journal, maintainer changelog, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-019-SEC01` | The lane must not require or expose secrets, credentials, private data, dashboard values, provider configuration, production details, or external-system access. | P0 | Sensitive-surface safety. |
| `PRD-019-SEC02` | The lane must not approve edits, PRDs, beads, transitions, review decisions, parallel execution, GitHub mutation, external mutation, or follow-up task creation. | P0 | Approval boundaries. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-019-NFR01` | Lane wording must remain understandable without graph theory or project-management jargon. | P0 | Beginner value. |
| `PRD-019-NFR02` | The protocol must stay independent of private maintainer files. | P0 | Public package completeness. |
| `PRD-019-NFR03` | V1 must not add new generated report fields or warning categories. | P0 | Scope control. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-019-FR01` | Review Lanes Protocol defines Dependency Graph Review Lane. | `python3 scripts/clarity-scenario-check.py` | Read protocol. | Markdown source | check output |
| `PRD-019-FR03` | Lane output uses existing Review Lanes fields and recommendation values. | `python3 scripts/clarity-scenario-check.py` | Review copyable prompt shape. | Markdown source | check output |
| `PRD-019-FR04` | Protocol names dependency, follow-up, owner-file, parallel, stale graph, and broad-scope risks. | `python3 scripts/clarity-scenario-check.py` | Confirm focus stays advisory. | Markdown source | check output |
| `PRD-019-FR05` | Prompt Patterns and User Guide include copyable lane guidance. | docs HTML freshness check | Read prompts for boundary wording. | Markdown docs | generated docs HTML |
| `PRD-019-FR08` | Inventory, roadmap, journal, changelog, and generated surfaces are current. | inventory, docs, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Public protocols and docs: changed to expose the lane.
- PRD shard: added as destination authority for this package capability.
- Generated HTML: regenerated as reading/review surfaces only.
- Work Graph evidence: referenced as generated evidence only; not changed in v1.
- External systems: not touched.

### Human Approval Gates

- The user still owns review acceptance, transition decisions, follow-up bead creation, parallel teammate coordination, owner-file updates, GitHub mutation, external mutation, merge, migration, rollback, and sensitive-surface approval.
- Lane findings may recommend accepted, revise, split, blocked, or stop, but they cannot approve that recommendation.

### Forbidden Actions

- Do not treat Dependency Graph Review Lane as task selection, transition approval, review approval, PRD approval, bead activation, acceptance approval, parallel execution approval, generated proof, Work Graph authority, follow-up task creation, owner-file rewrite, command approval, external mutation, GitHub mutation, registry behavior, optional-pack behavior, package-manager behavior, release-channel behavior, or a task-runner system.
- Do not include secrets, credentials, private data, provider configuration, dashboard values, or sensitive production details in lane output.

## Architecture / Project Context Impact

- No app architecture impact.
- No active-memory change.
- No new command, generated report field, compiler warning, `next-step.py` route, registry, optional pack, package-manager behavior, adapter behavior, or runtime behavior.
- `scripts/clarity-scenario-check.py` gains text-contract checks only.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/REVIEW-LANES-PROTOCOL.md` | Optional Dependency Graph Review Lane shape. | Produces advisory findings and acceptance questions only. | Text-contract and manual review. | `tasks/prds/PRD-019-advisory-dependency-graph-review.md` |
| `tasks/reference/PROMPT-PATTERNS.md` and `docs/PRECODE-USER-GUIDE.md` | Copyable lane prompt. | Invokes dependency graph review without approval, task creation, or mutation. | Text-contract and manual review. | `tasks/prds/PRD-019-advisory-dependency-graph-review.md` |
| `scripts/clarity-scenario-check.py` | Deterministic text-contract check. | Checks wording presence only. | Script run. | `tasks/prds/PRD-019-advisory-dependency-graph-review.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-019-advisory-dependency-graph-review.md`
- Owner protocol: `tasks/reference/REVIEW-LANES-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/DECOMPOSITION-PROTOCOL.md`
  - `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `logs/work-graph.md`
- Files or folders likely in play:
  - listed above
  - `scripts/clarity-scenario-check.py`
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
  - target app code
  - Work Graph compiler behavior
  - generated evidence reports except generated docs/PRD/roadmap HTML
  - `next-step.py`
  - GitHub, deployment, provider dashboards, secrets, or environment files
- Required checks:
  - `bash scripts/validate-memory.sh`
  - `python3 scripts/version-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 scripts/public-repo-check.py`
  - `python3 scripts/clarity-scenario-check.py`
  - `python3 scripts/prd-html.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
- Manual verification:
  - Confirm the lane cannot be mistaken for task selection, transition approval, review acceptance, graph authority, or parallel execution permission.
  - Confirm the lane tells users to repair owner files and regenerate Work Graph evidence when graph output is stale or misleading.

## Anti-Shallow Checks

- If the lane output chooses the next task, it violates the PRD.
- If Work Graph output is treated as authority or proof, it violates the PRD.
- If the lane approves parallel work or transition, it violates the PRD.
- If stale graph evidence is "fixed" by editing generated reports instead of owner files, it violates the PRD.

## Bead Proposals

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B019-advisory-dependency-graph-review` | `PRD-019-FR01` through `PRD-019-FR08`, `PRD-019-SEC01` through `PRD-019-SEC02`, `PRD-019-NFR01` through `PRD-019-NFR03` | PRD shard, review-lane protocol, prompt/user guidance, package inventory, clarity scenario coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-019-advisory-dependency-graph-review.md` | clarity scenario plus package/docs/roadmap checks |

## Compilation Notes

- `FEATURES.md` is not updated in this slice.
- V1 is a public package workflow contract, not a runtime capability.

## Open Questions

- None for v1.

## Approval

- Approval state: approved by maintainer implementation request on 2026-06-19.
