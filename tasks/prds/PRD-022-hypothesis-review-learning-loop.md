---
prd_id: PRD-022
status: approved
owner: user
risk_level: medium
feature_link: Hypothesis Review And Learning Loop v2
features_status: not compiled
related_prds: []
---

# PRD-022 -- Hypothesis Review And Learning Loop v2
<!-- ANCHOR: prd-022-hypothesis-review-learning-loop -->

> AUTHORITY: Public requirements for the Hypothesis Review / Learning Loop advisory protocol and checker coverage across discovery, source intake, Candidate Queue, PRD source inputs, and Planning Briefs.
> NOT_AUTHORITY: Active memory, product decisions, PRD approval, Candidate Queue ranking, task selection, bead activation, implementation priority, generated proof, analytics requirements, experiment database, dashboard, command wrapper, registry, optional pack, package-manager behavior, route structure, schema definitions, or implementation status.
> LOAD_WHEN: Implementing or reviewing Hypothesis Review / Learning Loop v2, `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md`, or `scripts/hypothesis-check.py`.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## State

- ID: `PRD-022`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-23`

## Feature Link

- Feature: `Hypothesis Review And Learning Loop v2`
- `FEATURES.md` status: `not compiled`
- Originating maintainer roadmap candidate: `#11`

## Source Inputs

- Source type: `maintainer roadmap candidate | approved implementation plan | shipped Hypothesis Guidance And Mechanics v1`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` candidate `Hypothesis Review And Learning Loop v2`
  - `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`
  - `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md`
  - `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/reference/PLANNING-PROTOCOL.md`
  - `scripts/hypothesis-check.py`
- Stable facts:
  - Hypothesis Guidance And Mechanics v1 introduced shared hunch, assumption, hypothesis, experiment-hypothesis, and `Primary hypothesis / learning target` language.
  - Discovery Summary, Local Source Intake, Candidate Queue, PRD source inputs, and Planning Briefs already carry the evidence fields needed for a review loop.
  - Existing Review Lanes are scoped to one active bead; hypothesis review must also work before PRD and bead activation.
- Assumptions:
  - The first useful v2 slice is a public advisory protocol plus checker coverage.
  - Generated stale-hypothesis dashboards, analytics integrations, and OS Health routing are premature.
- Conflicts or stale inputs:
  - The roadmap originally deferred v2 until v1 evidence existed. This PRD implements only a quiet review shape after v1 vocabulary/checker coverage is present.
- Privacy or secrets redactions:
  - Hypothesis review must not require raw private transcripts, secrets, credentials, dashboard values, production analytics, billing data, or sensitive personal data.

## Problem

After hypothesis mechanics are visible, users still need a safe way to ask what was actually learned before parked ideas, discovery notes, or planning briefs become product-definition momentum.

Without an explicit review shape, stale or untested hypotheses can look like PRD inputs, while generated summaries or Candidate Queue labels can appear more authoritative than they are.

## User Moment

- Before: A user has a Discovery Summary, Candidate Queue entry, intake summary, PRD source section, or Planning Brief and cannot tell whether the hypothesis was tested, narrowed, killed, promoted, stale, or still just a learning target.
- After: The user can invoke Hypothesis Review / Learning Loop and receive an evidence-only status, learning outcome, stale or untested signals, and next safe Precode workflow.
- Why now: v1 hypothesis vocabulary and checker coverage make the review shape small enough to add without creating product-management machinery.

## Destination

- Destination statement: Precode provides a lightweight advisory hypothesis review loop that works before PRD and bead activation and keeps learning visible without creating authority.
- Definition of done:
  - `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md` defines load conditions, input scope, output contract, status vocabulary, promotion paths, and forbidden actions.
  - `scripts/hypothesis-check.py` checks both v1 hypothesis guidance and v2 review-loop contract coverage.
  - Discovery, intake, Candidate Queue, PRD, and Planning surfaces expose the handoff fields needed for the review loop.
  - Prompt Patterns, User Guide, Daily Cockpit, and Package File Inventory make the loop discoverable.
  - Clarity scenario coverage protects the evidence-only, pre-PRD, no-ranking, no-analytics, no-database boundaries.
  - Maintainer changelog, roadmap, roadmap journal, and generated docs/PRD/roadmap surfaces are refreshed.
- First useful vertical slice: advisory protocol, text-contract checker, copyable prompt, docs, and generated surfaces only.

## Goals

- Goal 1: Let users review whether a hypothesis or learning target is `untested`, `tested`, `narrowed`, `killed`, `promoted`, `stale`, or `not applicable`.
- Goal 2: Keep the loop usable on pre-PRD artifacts, not only active beads.
- Goal 3: Route learning to the next safe owner workflow without approving, ranking, activating, or implementing anything.

## Non-Goals

- Not doing: analytics requirement, generated stale-hypothesis dashboard, experiment database, automatic Candidate Queue ranking, auto-promotion, workflow routing automation, product decision approval, PRD approval, bead activation, task selection, command wrapper, registry, optional pack, package-manager behavior, or generated proof.
- Deferred: richer stale-hypothesis visibility, generated reports, OS Health integration, and additional script parsing only after real review sessions show repeated ambiguity.
- Explicitly out of scope: treating `promoted` as implementation permission or treating generated hypothesis status as source of truth.

Contract phrases for checks: the loop does not approve product direction, does not rank candidates, and does not require analytics.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-022-FR01` | Add a Hypothesis Review / Learning Loop Protocol with pre-PRD and post-planning load conditions. | P0 | Must not require one active bead. |
| `PRD-022-FR02` | Protocol output must include review target, authority checked, hypothesis or learning target, evidence reviewed, learning status, learning outcome, stale or untested signals, recommended next workflow, user approval needed, stop condition, and generated-report warning. | P0 | Stable copyable output shape. |
| `PRD-022-FR03` | Review status vocabulary must be `untested`, `tested`, `narrowed`, `killed`, `promoted`, `stale`, and `not applicable`. | P0 | Review labels only. |
| `PRD-022-FR04` | Discovery, Local Source Intake, Candidate Queue, PRD, and Planning guidance must carry the source fields needed for review. | P0 | Avoid duplicate workflow machinery. |
| `PRD-022-FR05` | Prompt Patterns, User Guide, Daily Cockpit, and Package File Inventory must expose the loop and boundaries. | P1 | Discoverability. |
| `PRD-022-FR06` | `scripts/hypothesis-check.py` must check v1 guidance and v2 review-loop contract coverage without writing files. | P0 | Deterministic advisory checker. |
| `PRD-022-FR07` | Clarity scenario coverage must protect evidence-only, no ranking, no PRD approval, no bead activation, no analytics requirement, no database, no generated status authority, and pre-PRD usability. | P1 | Text-contract regression. |
| `PRD-022-FR08` | Maintainer changelog, roadmap, roadmap journal, generated docs, generated PRD HTML, and generated roadmap HTML must be updated. | P1 | Package-maintenance follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-022-SEC01` | The protocol must stop before requiring secrets, credentials, private raw transcripts, billing data, dashboard values, production analytics, or sensitive personal data. | P0 | Review can cite redacted summaries instead. |
| `PRD-022-SEC02` | The checker must be local, read-only, deterministic, and stdlib-only. | P0 | No network, external systems, or generated evidence writes. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-022-NFR01` | User-facing language must be plain enough for a non-technical builder to distinguish learning status from approval. | P0 | Avoid product-management jargon. |
| `PRD-022-NFR02` | The implementation must reuse existing owner workflows rather than create a dashboard, database, or routing engine. | P0 | Keeps v2 quiet and bounded. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-022-FR01` | Protocol exists and names pre-PRD sources plus Planning Briefs. | `python3 scripts/hypothesis-check.py` | Read protocol. | Markdown source | check output |
| `PRD-022-FR02` | Output contract has all required review fields. | `python3 scripts/clarity-scenario-check.py` | Compare copyable output. | Markdown source | check output |
| `PRD-022-FR03` | Status vocabulary is stable and non-authoritative. | `python3 scripts/hypothesis-check.py` | Read status table. | Markdown source | check output |
| `PRD-022-FR05` | Prompt Patterns, User Guide, Daily Cockpit, and Package Inventory expose invocation and boundaries. | docs HTML freshness check | Read public docs. | Markdown docs | generated docs HTML |
| `PRD-022-FR06` | Checker returns advisory JSON and writes no files. | `python3 scripts/hypothesis-check.py` | Inspect command output. | Markdown source | command output |
| `PRD-022-FR08` | PRD HTML, docs HTML, roadmap HTML, changelog, and journal are current. | PRD/docs/roadmap checks | Read generated surfaces. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before owner-file updates, PRD creation or amendment, PRD approval, Candidate Queue writeback, `DECISIONS.md` updates, bead creation or activation, active-memory edits, implementation, external mutation, release, or package-manager behavior.
- Stop if the source material is missing, the hypothesis or learning target is unclear, learning evidence cannot be inspected, current owner files conflict, or review would require secrets, raw private data, dashboards, production analytics, or external mutation.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md` | User-invoked advisory review. | Produces learning status and next workflow without approval authority. | `scripts/hypothesis-check.py`, clarity scenario. | `tasks/prds/PRD-022-hypothesis-review-learning-loop.md` |
| `scripts/hypothesis-check.py` | Read-only package-contract check. | Checks canonical Markdown terms and guardrails; writes nothing. | Direct command. | `tasks/prds/PRD-022-hypothesis-review-learning-loop.md` |
| Public docs and prompts | Copyable invocation. | Teaches the review loop as evidence-only and pre-PRD-capable. | Docs HTML check. | `tasks/prds/PRD-022-hypothesis-review-learning-loop.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-022-hypothesis-review-learning-loop.md`
- Owner protocol:
  - `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`
  - `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md`
  - `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/reference/PLANNING-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/hypothesis-check.py`
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
  - analytics dashboards
  - generated evidence reports beyond docs/PRD/roadmap HTML
  - GitHub, deployment, provider dashboards, secrets, credentials, or environment files
- Required checks:
  - `python3 scripts/hypothesis-check.py`
  - `python3 scripts/clarity-scenario-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 scripts/public-repo-check.py`
  - `python3 scripts/prd-html.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
  - `python3 scripts/version-check.py`

## Forbidden Assumptions

- A learning status is product approval.
- `promoted` means implementation is approved.
- Hypothesis Review ranks Candidate Queue entries.
- The loop requires analytics, production data, a database, dashboard, or generated stale-hypothesis report.
- Generated hypothesis status can override owner files, current code, approved PRDs, active beads, or user judgment.
