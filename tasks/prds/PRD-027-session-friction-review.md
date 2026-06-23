---
prd_id: PRD-027
status: approved
owner: user
risk_level: medium
feature_link: Session Friction Review
features_status: not compiled
related_prds:
  - PRD-020
  - PRD-024
---

# PRD-027 -- Session Friction Review
<!-- ANCHOR: prd-027-session-friction-review -->

> AUTHORITY: Public requirements for the Session Friction Review read-only advisory checker, cited failure-pattern findings, proposed destinations, and generated-evidence boundaries.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, command approval, review acceptance, memory promotion, owner-file edits, generated proof, telemetry, runtime compression, command-wrapper behavior, registry behavior, optional-pack behavior, install/update behavior, package-manager behavior, or implementation status.
> LOAD_WHEN: Implementing, reviewing, or interpreting `scripts/session-friction-check.py`, session-friction findings, tool-run failure patterns, or protocol follow-up candidates.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## State

- ID: `PRD-027`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-23`

## Feature Link

- Feature: `Session Friction Review`
- `FEATURES.md` status: `not compiled`
- Originating maintainer roadmap candidate: `Session Friction Review`

## Source Inputs

- Source type: `maintainer roadmap candidate | Headroom-inspired context lesson | existing tool execution and memory protocols`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` candidate `Session Friction Review`
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `tasks/reference/MEMORY-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
- Stable facts:
  - `logs/tool-runs.jsonl` records important non-check tool runs and failure categories.
  - `logs/check-results.jsonl` records verification evidence.
  - `completion-check.py`, `tool-execution-check.py`, and memory summaries already expose stale evidence, missing failure categories, and context-pressure warnings.
  - Reviewed memory is evidence only and promotion is manual.
- Assumptions:
  - The first useful slice is a cited local review, not telemetry, runtime learning, semantic memory, or automatic writeback.
  - A new checker is clearer than overloading `memory-check.py` because the source evidence spans tool runs, checks, closeout, and memory signals.
- Conflicts or stale inputs:
  - "Failure learning" can imply automatic memory or host runtime behavior. This PRD narrows the feature to read-only generated evidence.
- Privacy or secrets redactions:
  - Findings must cite safe ledger references and must not store secrets, credentials, raw private transcripts, long command output, dashboard values, or sensitive local state.

## Problem

Agents can repeat wrong-path attempts, unavailable commands, stale-evidence assumptions, over-broad context loading, or missing-proof patterns across sessions. Those repeated frictions are useful review evidence, but only if they stay cited, demoted, and manually promoted.

## User Moment

- Before: A user sees repeated command failures or stale evidence warnings, but the lesson is trapped in chat or scattered logs.
- After: The user can run a read-only review that lists cited friction findings, confidence, freshness, proposed destination, and the next human review step.
- Why now: Tool-run logging, memory-search boundaries, retrieval-readiness review, and completion/handoff checks already exist; the gap is a bounded review over those safe sources.

## Destination

- Destination statement: PrecodeOS can review local session-friction evidence and recommend path corrections, command-pattern notes, reviewed memory candidates, or protocol follow-ups without writing or approving anything.
- Definition of done:
  - `scripts/session-friction-check.py` prints read-only advisory JSON and writes nothing.
  - `--self-test` covers deterministic fixture categories and generated-evidence boundaries.
  - `scripts/os_compiler.py` exposes `session_friction_review` for OS Health sidecars.
  - `logs/session-friction-review.json` is emitted only through existing generated sidecar refresh.
  - Protocols, prompt patterns, user docs, package inventory, maintainer changelog, roadmap, roadmap journal, and generated surfaces are refreshed.
- First useful vertical slice: local checker, compiler payload, OS Health row, text-contract fixtures, docs/protocol propagation, and maintainer history.

## Goals

- Goal 1: Identify repeated friction from safe local ledgers and compiled advisory summaries.
- Goal 2: Require cited source references, confidence, freshness, proposed destination, and next human review step.
- Goal 3: Preserve manual promotion into memory cards, protocols, adapter notes, owner files, PRDs, or beads.
- Goal 4: Make missing memory-search evidence explicit instead of inferring a lesson.

## Non-Goals

- Not doing: telemetry, runtime compression, agent proxying, semantic memory, memory-card creation, owner-file edits, generated report authority, command approval, task selection, PRD approval, bead activation, review acceptance, external mutation, command wrapper, registry, optional pack, install/update behavior, package-manager behavior, or host-specific integration.
- Deferred: richer source-specific fixture packs, trend reports, UI/dashboard views, or any optional backend.
- Explicitly out of scope: auto-editing `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, root shims, reviewed memory cards, generated reports, owner files, command wrappers, or maintainer-private files.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-027-FR01` | Add `scripts/session-friction-check.py` as a read-only advisory checker. | P0 | Default command writes nothing. |
| `PRD-027-FR02` | Output must include `status`, `warnings`, `generated_report_warning`, and `details.findings`. | P0 | JSON stdout. |
| `PRD-027-FR03` | Each finding must include `category`, `source_refs`, `confidence`, `freshness`, `recommended_destination`, `suggested_next_step`, and `forbidden_uses`. | P0 | Findings are review input only. |
| `PRD-027-FR04` | V1 categories must cover repeated failure category, missing failure category, unavailable command/dependency, sandbox or approval block, stale check/closeout evidence, generated refresh without verification, memory/context pressure, and no safe evidence found. | P0 | No inferred memory-search friction without source evidence. |
| `PRD-027-FR05` | `--self-test` must cover deterministic fixture categories and boundary fields. | P0 | No external dependencies. |
| `PRD-027-FR06` | `scripts/os_compiler.py`, OS Health, and generated sidecars must expose `session_friction_review` as generated evidence only. | P1 | No `next-step.py` routing or command facade. |
| `PRD-027-FR07` | Protocols, prompts, user docs, package inventory, maintainer changelog, roadmap, roadmap journal, and generated surfaces must be updated. | P1 | Maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-027-SEC01` | Findings must not include secrets, credentials, private transcripts, dashboard values, sensitive local state, or long raw command output. | P0 | Cite safe ledger references and summaries. |
| `PRD-027-SEC02` | The checker must not mutate files, memory, owner files, generated reports, external systems, branches, worktrees, or task state. | P0 | Sidecar writes happen only through existing OS Health generation. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-027-FR01` | Default checker prints advisory JSON and writes no files. | `python3 scripts/session-friction-check.py` | Inspect output. | Current repo ledgers | command output |
| `PRD-027-FR04` | Categories are cited and no-safe-evidence is explicit. | `python3 scripts/session-friction-check.py --self-test` | Review fixture failures if any. | Synthetic rows | command output |
| `PRD-027-FR06` | Compiled state and OS Health sidecars include `session_friction_review`. | `python3 scripts/os-health.py` | Inspect `logs/session-friction-review.json`. | Current repo | generated sidecar |
| `PRD-027-FR07` | Docs, protocols, inventory, roadmap, changelog, and generated surfaces are current. | docs, PRD, inventory, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before memory-card creation, owner-file promotion, protocol edits outside an approved bead, PRD approval, bead activation, command approval, review acceptance, external mutation, destructive action, install/update behavior, or package-manager behavior.
- Stop if a finding lacks source evidence, includes sensitive raw output, implies automatic promotion, or tries to use generated friction output as proof.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: `logs/session-friction-review.json` through existing sidecar generation only.

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-027-session-friction-review.md`
- Owner protocol: `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/MEMORY-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-ARCHITECTURE-OVERVIEW.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/session-friction-check.py`
  - `scripts/os_compiler.py`
  - `scripts/precode_outputs.py`
  - `scripts/precode_doctor.py`
  - `scripts/os-health.py`
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
  - root shims
  - reviewed memory cards
  - command wrappers
  - external systems
  - package-manager files
- Required checks:
  - `python3 scripts/session-friction-check.py --self-test`
  - `python3 scripts/session-friction-check.py`
  - `python3 scripts/clarity-scenario-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 scripts/public-repo-check.py`
  - `python3 scripts/prd-html.py --check`
  - `python3 scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
  - `bash scripts/validate-memory.sh`
