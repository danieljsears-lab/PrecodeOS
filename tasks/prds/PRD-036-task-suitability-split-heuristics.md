---
prd_id: PRD-036
status: approved
owner: user
risk_level: medium
feature_link: TBD
features_status: not compiled
related_prds:
  - PRD-034
  - PRD-035
---

# PRD-036 - Task Suitability And Split Heuristics
<!-- ANCHOR: prd-036-task-suitability-split-heuristics -->

> AUTHORITY: Destination shard for advisory task-suitability and split-readiness guidance before PrecodeOS work starts or a candidate bead is activated.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation approval, review acceptance, generated proof, autonomous execution approval, task scoring, task ranking, command approval, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, package-manager behavior, or external mutation.
> LOAD_WHEN: Reviewing, implementing, or decomposing task-suitability guidance for Workflow Selection, Decomposition, bead activation review, prompt patterns, or advisory suitability checks.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-04

## State

- ID: `PRD-036`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-07-04`

## Source Inputs

- Source type: `maintainer roadmap`
- Source references: `_maintainer/PRECODE-ROADMAP.md` candidate `Task Suitability And Split Heuristics`
- Stable facts: The roadmap identified task suitability as a near-term public package slice because plain pre-task questions can reduce scope bloat, proof ambiguity, and premature agent execution.
- Assumptions: Beginners and agents benefit from one plain suitability frame before work starts, but the output must remain advisory and subordinate to owner files, PRDs, beads, and human gates.
- Candidate requirements: Fold suitability into Workflow Selection and Decomposition; add prompt guidance and a read-only checker; preserve no-authority boundaries.
- Candidate non-goals: New task selector, task score, runtime autonomy, skill surface, command wrapper, generated approval, or package-manager behavior.
- Authority files likely affected: `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`, `tasks/reference/DECOMPOSITION-PROTOCOL.md`, `tasks/beads/BEAD-SCHEMA.md`, `tasks/reference/PROMPT-PATTERNS.md`

## Problem

Beginners and agents can start work before the request is clear enough, small enough, proof-ready enough, or bounded enough. Without a plain suitability check, broad work can look executable even when the destination, owner surface, stop conditions, split point, or proof path is missing.

## User Moment

- Before: The builder or agent is about to plan, decompose, activate, or implement work but cannot tell whether it is one bounded task.
- After: The builder sees whether to continue, clarify, route, split, block, or stop before implementation starts.
- Why now: More capable agents make execution feel easy; PrecodeOS needs the pre-work judgment layer to stay visible without adding runtime autonomy.

## Destination

- Destination statement: PrecodeOS can ask and check whether a task is clear, bounded, proof-ready, and safe to continue before work starts or a candidate bead is activated.
- Definition of done: Workflow Selection, Decomposition, bead guidance, prompts, public docs, and a read-only checker all express the same advisory suitability contract.
- First useful vertical slice: Public protocol/prompt guidance plus `scripts/task-suitability-check.py --check` advisory output.

## Goals

- Goal 1: Make pre-work suitability questions beginner-readable.
- Goal 2: Make split triggers explicit before a broad request becomes an active bead.
- Goal 3: Validate the public contract with deterministic checker and clarity-scenario coverage.

## Non-Goals

- Not doing: task selection, task ranking, task scoring, PRD approval, bead activation, implementation authorization, review acceptance, generated proof, autonomous execution approval, new daily alias, new skill surface, command facade entry, registry, optional pack, install/update behavior, release channel, package-manager behavior, or external mutation.
- Deferred: deeper repo-level heuristics, language-aware analysis, delegation re-entry evidence pack, and engineering-quality review lane expansion.
- Explicitly out of scope: treating suitability output as permission to code or as a replacement for owner-file, PRD, decomposition, transition, review, or human approval gates.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-036-FR01` | Workflow Selection must include advisory task-suitability questions before routing to implementation, decomposition, review, repair, or unblocker work. | P0 | Questions cover destination clarity, owner source, reviewable size, proof, approval gates, stop conditions, and split need. |
| `PRD-036-FR02` | Decomposition must name split triggers when a candidate bead has multiple outcomes, authority owners, proof strategies, risk models, manual gates, broad files in play, or "and then" done-when language. | P0 | Candidate beads remain proposals until normal activation. |
| `PRD-036-FR03` | Prompt Patterns and beginner docs must provide a copyable suitability prompt that returns `continue`, `clarify`, `route`, `split`, `block`, or `stop`. | P0 | The prompt must preserve no-approval boundaries. |
| `PRD-036-FR04` | `scripts/task-suitability-check.py --check` must print advisory JSON for active-bead or current-planning suitability signals. | P0 | No mutation, no task selection, no approval. |
| `PRD-036-FR05` | `scripts/task-suitability-check.py --self-test` must cover continue, clarify, route, split, block, and stop scenarios. | P0 | Deterministic synthetic checks only. |
| `PRD-036-FR06` | Public inventory, AI navigation, and generated reading/review surfaces must mention the checker and its boundaries. | P1 | Discoverability without daily command sprawl. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-036-SEC01` | Suitability guidance must stop or route when sensitive, external, destructive, deployment, secret, auth, payment, migration, or bounded-AFK risk is visible without an approval path. | P0 | Routes to existing owner protocols; does not approve the action. |
| `PRD-036-SEC02` | Suitability output must not inspect secrets, mutate files, run app code, approve commands, or use maintainer-private files as public authority. | P0 | Static source inspection only. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-036-NFR01` | Output must use plain beginner-readable language. | P0 | Avoid numeric scores. |
| `PRD-036-NFR02` | Checker output must remain stable enough for clarity scenarios and adapter diagnostics. | P1 | JSON fields should be additive. |
| `PRD-036-NFR03` | The implementation must preserve existing Workflow Selection, Decomposition, adaptive-depth, and engineering-quality boundaries. | P0 | Suitability is a pre-work routing aid, not a replacement. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Evidence lane | Automated check | Manual check | Fixture or data needed | Recorded source or evidence location | What this does not prove |
|---|---|---|---|---|---|---|---|
| `PRD-036-FR01` | Workflow Selection names task suitability before implementation routing. | `static` | `python3 scripts/clarity-scenario-check.py` | Read protocol wording. | Protocol text | `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` | Does not choose work. |
| `PRD-036-FR02` | Decomposition explains split triggers. | `static` | `python3 scripts/clarity-scenario-check.py` | Read decomposition checklist. | Protocol text | `tasks/reference/DECOMPOSITION-PROTOCOL.md` | Does not activate beads. |
| `PRD-036-FR03` | Prompt guidance returns only advisory suitability decisions. | `static` | `python3 scripts/clarity-scenario-check.py` | Paste prompt review. | Prompt text | `tasks/reference/PROMPT-PATTERNS.md` | Does not approve implementation. |
| `PRD-036-FR04` | Checker emits advisory JSON and no mutation. | `static` | `python3 scripts/task-suitability-check.py --check` | Inspect output boundaries. | Active repo state | stdout JSON | Does not prove the task should be done. |
| `PRD-036-FR05` | Checker self-test covers all suitability decision labels. | `static` | `python3 scripts/task-suitability-check.py --self-test` | Inspect scenario names. | Synthetic fixtures | stdout JSON | Does not test app behavior. |
| `PRD-036-FR06` | Public docs and inventory mention the checker with no-authority boundaries. | `static` | docs and inventory freshness checks | Read rendered docs. | Public docs | `docs-html/`, `tasks/prds-html/` | Does not make generated HTML authority. |
| `PRD-036-SEC01` | Sensitive or approval-gated work routes or stops. | `static` | checker self-test | Inspect route/stop scenario. | Synthetic sensitive fixture | stdout JSON | Does not approve sensitive work. |
| `PRD-036-SEC02` | Checker remains read-only and advisory. | `static` | checker self-test and source review | Inspect script behavior. | Script source | `scripts/task-suitability-check.py` | Does not certify security. |

## Interfaces And Outputs

`scripts/task-suitability-check.py --check` prints JSON with:

- `tool`
- `status`
- `warnings`
- `advisory_only`
- `details.current_bead`
- `details.suitability_decision`
- `details.suitability_questions`
- `details.split_reasons`
- `details.missing_signals`
- `details.route_reasons`
- `details.block_reasons`
- `recommended_next_safe_action`
- `generated_report_warning`

The checker may recommend only `continue`, `clarify`, `route`, `split`, `block`, or `stop`.

## Boundaries

Task suitability is advisory only. It helps a builder decide what to inspect next, but it does not choose tasks, rank work, approve a PRD, activate a bead, update `tasks/todo.md`, authorize implementation, accept review, approve release, approve external mutation, or create generated proof.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B002-task-suitability-split-heuristics` | `PRD-036-FR01` through `PRD-036-FR06`, `PRD-036-SEC01` through `PRD-036-SEC02`, `PRD-036-NFR01` through `PRD-036-NFR03` | PRD shard, protocol guidance, prompt guidance, checker, docs/inventory/navigation, clarity coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-036-task-suitability-split-heuristics.md` | checker self-test, clarity scenario, package/docs/PRD/roadmap checks |

