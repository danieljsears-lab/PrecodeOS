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
Document version: v0.1.0
Last updated: 2026-04-26

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

Use stable IDs. Keep each item observable and small enough to map to beads.

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

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-000-FR01` |  |  |  |  | bead closeout |

## Risk And Permission Model

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

Load `PROJECT-CONTEXT.md` when this feature could affect project-wide conventions, stack choices, integration boundaries, or implementation rules.

- Project context impact: `none | minor | material`
- `PROJECT-CONTEXT.md` loaded: `yes | no | not needed`
- Architecture authority updates needed:
- Route/API authority updates needed:
- Schema authority updates needed:
- Security authority updates needed:
- Decision log updates needed:

## Agent Context Contract

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

| Proposed bead | Requirement IDs | Done when | Primary authority | Verification |
|---|---|---|---|---|
| `B###-short-name` | `PRD-000-FR01` |  |  |  |

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
