---
prd_id: PRD-000
status: draft
owner: user
risk_level: low
feature_link: TBD
features_status: not compiled
related_prds: []
---

# PRD-000 — Template
<!-- ANCHOR: prd-template -->

> AUTHORITY: Reusable PRD shard template for defining product work before it becomes feature inventory or execution beads.
> NOT_AUTHORITY: A live product commitment, active task selection, route structure, schema field definitions, or implementation status.
> LOAD_WHEN: Starting a new PRD shard or checking whether a PRD has enough definition to compile into `FEATURES.md`.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.7
Last updated: 2026-05-29

## State

- ID: `PRD-000`
- Status: `draft`
- Owner: `user`
- Risk level: `low | medium | high`
- Last updated: `YYYY-MM-DD`

## Feature Link

- Feature: `Feature # or TBD`
- `FEATURES.md` status: `not compiled | compiled | amended`
- Related PRDs: `none`

## Source Inputs

Raw inputs are evidence, not authority. Use `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` for source-heavy work and summarize only what matters for product definition.

- Source type: `notes | docs | screenshot | design | chat summary | issue export | research | customer quote | manual draft | existing feature doc | other`
- Source references:
- Stable facts:
- Assumptions:
- Conflicts or stale inputs:
- Privacy or secrets redactions:
- Candidate requirements:
- Candidate non-goals:
- Authority files likely affected:
- Discarded or stale inputs:

## Product Brief

Use this for net-new, rough product ideas from non-technical builders. It is builder-facing evidence, not approval, and should be produced after at most three high-level product or business questions.

- Product idea:
- Intended user:
- Painful before moment:
- Better after moment:
- Current workaround or evidence:
- Assumptions:
- Not-yet list:
- Smallest useful version:
- Next best question:

## Discovery Evidence

Use when the idea was broad, risky, market-facing, paid, evidence-poor, solution-first, or otherwise needed Product Discovery Validation before PRD shaping. Keep this as a bridge summary, not a full research report.

- Discovery completed: `yes | no | skipped`
- Reason skipped:
- Evidence strength: `very weak | weak | medium | strong | strongest | not assessed`
- Riskiest assumption:
- Discovery recommendation: `proceed | pause | narrow | kill | not assessed`
- Discovery Summary reference:

## Alignment Summary

Use when the idea needed interrogation before requirements. For non-technical builders, summarize the product story before dense requirement or technical sections. Raw transcripts are source evidence, not authority.

- Alignment method: `none | one-question-at-a-time alignment | meeting transcript follow-up | source review | other`
- Shared design concept:
- Key decisions reached:
- Recommended answers accepted:
- Recommended answers rejected or changed:
- Remaining implementation-changing questions:
- Stale or discarded assumptions:

## Domain Language

Use when terms, labels, module/interface names, tests, or source inputs need shared vocabulary. Keep the builder-facing meaning plain; module, code, and test examples are agent-facing translation. Use `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` for domain-heavy work.

| Term | Status | Plain-English meaning | Aliases | Avoid/confusing terms | UI/code/test examples | Source pointer |
|---|---|---|---|---|---|---|
|  | `introduced | reused | rejected | stale` |  |  |  |  |  |

- Module/interface names that should match domain language:
- Glossary-card candidate needed: `yes | no`
- Authority owner if promoted:

## PRFAQ-Lite

Use when the work is new, ambiguous, customer-facing, risky, or easy to overbuild. Keep it short.

- Press-release claim:
- Customer problem:
- Customer FAQ:
- Internal FAQ:
- Appetite:
- Kill or pause criteria:

## Problem

Two sentences max.

Name the user pain, constraint, or opportunity. Include evidence when available.

## User Moment

- Before:
- After:
- Why now:

## Destination

The PRD is the destination document. It defines the intended user-visible arrival point and the acceptance boundaries for journey beads.

- Destination statement:
- Definition of done:
- First useful vertical slice:

## Goal Frame

Use this only when the PRD needs durable outcome orientation before workflow selection or decomposition. See `tasks/reference/GOAL-FRAME-PROTOCOL.md`.

- Status: `draft`
- Last reaffirmed:
- Owner file: `tasks/prds/PRD-000-template.md`
- Horizon: `feature`
- Workflow guidance: `decomposition`
- Goal:
- Why now:
- Success signal:
- Out of scope:
- Approval gates:
- Reaffirmation trigger:

## Product Constitution Fit

Use `PRODUCT.md` when this feature could affect product promise, users and jobs, strategy and non-goals, current bets, success signals, or design and voice direction.

- `PRODUCT.md` loaded: `yes | no | not needed`
- Product promise fit:
- User and job fit:
- Strategy and non-goal fit:
- Current bet or success signal affected:
- Design or voice affected:
- Product constitution update needed:

## Users

- Primary user:
- Secondary user:
- Excluded user:

## Goals

- Goal 1:
- Goal 2:
- Goal 3:

## Non-Goals

- Not doing:
- Deferred:
- Explicitly out of scope:

## Alternatives Considered

| Option | Why rejected or deferred | Decision owner |
|---|---|---|
| Do nothing |  | user |

## Requirements

Agent-facing translation from the builder-approved product story. Use stable IDs. Keep each item observable and small enough to map to beads.

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-000-FR01` |  | P0 |  |

### UX Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-000-UX01` |  | P0 |  |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-000-SEC01` |  | P0 |  |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-000-NFR01` |  | P0 |  |

## Acceptance Oracle Matrix

Agent-facing verification translation. The builder should be able to read the expected behavior and manual check in plain English, but the agent owns the check mapping.

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-000-FR01` |  |  |  |  | bead closeout |

## Risk And Permission Model

Agent-facing risk translation with human approval gates in plain English.

### Sensitive Surfaces

- Auth:
- Payments:
- User data:
- Uploads:
- External services:
- Secrets:
- Destructive actions:

### Human Approval Gates

- Approval required before:
- Stop if:
- Escalate when:

### Tool And Environment Boundaries

- Allowed tools:
- Network needs:
- Dependency changes:
- Dashboard/manual steps:

## Architecture / Project Context Impact

Agent-facing technical translation. Load `PROJECT-CONTEXT.md` when this feature could affect project-wide conventions, stack choices, integration boundaries, or implementation rules. Do not ask the builder to choose architecture internals unless a real tradeoff or approval gate is exposed.

- Project context impact: `none | minor | material`
- `PROJECT-CONTEXT.md` loaded: `yes | no | not needed`
- Architecture Shaping: `needed | completed | skipped`
- Architecture Brief evidence:
- Architecture Shaping skip reason:
- Architecture authority updates needed:
- Route/API authority updates needed:
- Schema authority updates needed:
- Security authority updates needed:
- Decision log updates needed:

## Module / Interface Candidates

Agent-facing implementation-shape translation. Use for code-changing work where the human should approve the plain-English behavior boundary before internals are delegated.

Prefer names that match the PRD `Domain Language` section and current project conventions.

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
|  |  |  |  |  |

## Agent Context Contract

Agent-facing execution context. This section keeps future coding agents bounded; it is not a client interview worksheet.

- Primary authority file:
- Secondary reference files:
- Files or folders likely in play:
- Files or folders out of scope:
- Required checks:
- Manual verification:
- Forbidden assumptions:

## Anti-Shallow Checks

- User problem named:
- Non-goals named:
- Before/after user moment clear:
- Requirements observable:
- Sensitive surfaces identified:
- Authority files identified:
- First bead can be one logical unit:
- Generated text reviewed by user:

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B###-short-name` | `PRD-000-FR01` |  | `human_in_loop | afk_candidate | human_required` | `failing_first | characterization | static_only | manual_only | not_applicable` | `same_session_ok | fresh_context_recommended | fresh_context_required` |  |  |

## Compilation Notes

Describe how this PRD should update `FEATURES.md`.

- Feature entry:
- Functional requirements to add or amend:
- MVP slice notes:
- Acceptance updates needed:

## Open Questions

Only include blockers that can change implementation.

| Question | Affects | Blocking? |
|---|---|---|
|  |  | yes |

## Approval

- Approved by:
- Approved on:
- Approval notes:
