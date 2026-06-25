---
prd_id: PRD-030
status: approved
owner: user
risk_level: medium
feature_link: PRD Quality Review Lane
features_status: not compiled
related_prds:
  - PRD-018
  - PRD-024
  - PRD-026
---

# PRD-030 -- PRD Quality Review Lane
<!-- ANCHOR: prd-030-prd-quality-review-lane -->

> AUTHORITY: Destination shard for the advisory PRD Quality Review Lane.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, review acceptance, implementation acceptance, generated proof, scorecard authority, checker gate, follow-up task creation, owner-file rewrite, external mutation, GitHub mutation, SaaS workspace behavior, export automation, MCP mutation, package-manager behavior, or a persona system.
> LOAD_WHEN: Reviewing, implementing, or decomposing the PRD Quality Review Lane package capability.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-24

## State

- ID: `PRD-030`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-24`

## Feature Link

- Feature: `PRD Quality Review Lane`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-018`, `PRD-024`, `PRD-026`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped PRD and Review Lanes guidance`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `PRD Quality Review Lane`
  - `tasks/reference/REVIEW-LANES-PROTOCOL.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `tasks/prds/PRD-024-requirement-to-proof-traceability.md`
  - `tasks/prds/PRD-026-ears-acceptance-guidance.md`
- Stable facts:
  - Review Lanes already provide advisory output fields without acceptance, release, security, graph, task, or approval authority.
  - PRD Protocol already requires clear goals, non-goals, user moments, acceptance oracles, risk gates, architecture impact, and decomposition readiness before approval.
  - Requirements Gap And Conflict Review already catches ambiguous requirements, conflicts, missing edge cases, unstated assumptions, stale source inputs, weak acceptance oracles, and owner-file follow-ups.
  - Requirement-To-Proof Traceability and EARS-style guidance already help make acceptance and proof expectations inspectable without making syntax or generated output authoritative.
- Assumptions:
  - The first useful slice should be protocol, prompt, and user guidance only.
  - The lane should complement Requirements Gap And Conflict Review by reviewing product-quality and handoff readiness, not by duplicating the requirement gap/conflict contract.
  - Text-contract checks are enough for v1.
- Conflicts or stale inputs:
  - "PRD quality" can sound like an approval score, generated PRD rewrite, or implementation-readiness certification. V1 must explicitly refuse those interpretations.
  - ChatPRD-inspired workflow pressure should be adopted as a low-authority review pattern only, not as SaaS workspace, export, MCP-mutation, or automatic PRD-generation behavior.
- Privacy or secrets redactions:
  - The lane must not require secrets, credentials, private data, dashboard values, provider configuration, production details, customer records, or external-system access.

## Problem

PRD drafts can look complete while still hiding vague user moments, weak strategy fit, missing assumptions, incomplete acceptance, unresolved open questions, or weak handoff readiness.

PrecodeOS needs a small advisory review lane that helps users inspect a draft PRD before approval without turning review output into PRD approval, implementation permission, task creation, or owner-file mutation.

## User Moment

- Before: A builder or agent has a draft PRD and guesses whether it is clear enough to approve, decompose, or hand off.
- After: The review names product-quality and handoff-readiness findings, missing proof, acceptance questions, approval still required, and promotion path without approving the PRD or creating work.
- Why now: PRD Protocol, Requirements Gap And Conflict Review, Review Lanes, Requirement-To-Proof Traceability, and optional EARS-style acceptance guidance are mature enough to support a narrow PRD-quality lens without new automation.

## Destination

- Destination statement: PrecodeOS exposes a PRD Quality Review Lane for draft PRDs before approval, preserving owner-file authority and human PRD approval.
- Definition of done:
  - PRD-030 exists as the destination shard.
  - Review Lanes Protocol includes PRD Quality Review Lane as an optional advisory lane for draft PRDs.
  - Prompt Patterns and User Guide include copyable lane guidance.
  - PRD Protocol points to the lane without replacing Requirements Gap And Conflict Review.
  - Package inventory lists PRD-030 and the expanded Review Lanes behavior.
  - Clarity scenario coverage checks lane name, output fields, PRD-approval boundary, no task creation, no owner-file rewrite, no scorecard authority, and no generated proof.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed.
- First useful vertical slice: protocol/prompt guidance and text-contract checks only.

## Users

- Primary user: Non-technical builder or maintainer reviewing whether a draft PRD is clear enough for human approval review.
- Secondary user: AI coding agent or support helper preparing product-quality and handoff-readiness questions without mutating the repo.
- Excluded user: Hosted PRD workspace, automated PRD generator, product-management scorecard, task planner, design or engineering handoff bot, or agent platform expecting review output to approve PRDs or create work.

## Goals

- Goal 1: Make draft PRD quality easier to review before approval.
- Goal 2: Keep findings tied to product clarity, proof expectations, open questions, handoff readiness, and acceptance questions.
- Goal 3: Preserve human PRD approval, owner-file authority, and separate bead activation.
- Goal 4: Avoid checker gates, scorecards, generated reports, generated PRD rewrites, PRD HTML behavior, task creation, or SaaS/import/export semantics in v1.

## Non-Goals

- Not doing: new command, checker, scorecard, generated report, generated PRD rewrite, PRD HTML behavior, PRD approval, implementation permission, bead activation, task creation, owner-file rewrite, implementation acceptance, design or engineering handoff approval, SaaS workspace, export automation, MCP mutation, registry, optional pack, package-manager behavior, or release-channel behavior.
- Deferred: richer PRD HTML review cues, generated diff artifacts, stricter acceptance-oracle review, handoff readiness packets, score-like summaries, and any checker behavior after real PRD review examples justify it.
- Explicitly out of scope: replacing Requirements Gap And Conflict Review, PRD approval, Architecture Shaping, Decomposition Protocol, Review mode, or human approval.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-030-FR01` | Add PRD Quality Review Lane to Review Lanes Protocol as an optional advisory lane for draft PRDs before approval. | P0 | Owner protocol update. |
| `PRD-030-FR02` | Lane input guidance must include the draft PRD, PRD Protocol, relevant source inputs, authority files when needed, acceptance oracles, open questions, proof expectations, and handoff context when present. | P0 | Keeps findings grounded. |
| `PRD-030-FR03` | Lane output must use the existing Review Lanes output fields and recommendation values. | P0 | Stable review shape. |
| `PRD-030-FR04` | Lane focus must include user problem clarity, before/after moment, strategy fit, non-goals, assumptions, stale or conflicting inputs, acceptance quality, requirement-to-proof readiness, open questions, handoff readiness, and smallest first slice. | P0 | Review substance. |
| `PRD-030-FR05` | Prompt Patterns and User Guide must include copyable PRD Quality Review Lane guidance. | P0 | User-facing invocation. |
| `PRD-030-FR06` | PRD Protocol must reference the lane as optional PRD-quality review without replacing Requirements Gap And Conflict Review. | P1 | Workflow fit. |
| `PRD-030-FR07` | Package inventory must list PRD-030 and the expanded Review Lanes Protocol behavior. | P1 | Discoverability. |
| `PRD-030-FR08` | Clarity scenario coverage must check lane name, output fields, PRD-approval boundary, no task creation, no owner-file rewrite, no scorecard authority, and no generated proof. | P1 | Text contract only. |
| `PRD-030-FR09` | Roadmap, roadmap journal, maintainer changelog, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-030-SEC01` | The lane must not require or expose secrets, credentials, private data, dashboard values, provider configuration, production details, customer records, or external-system access. | P0 | Sensitive-surface safety. |
| `PRD-030-SEC02` | The lane must not approve PRDs, edits, beads, review decisions, implementation, handoff, GitHub mutation, external mutation, or follow-up task creation. | P0 | Approval boundaries. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-030-NFR01` | Lane wording must remain understandable without product-management jargon. | P0 | Beginner value. |
| `PRD-030-NFR02` | The protocol must stay independent of private maintainer files. | P0 | Public package completeness. |
| `PRD-030-NFR03` | V1 must not add new generated report fields, PRD HTML behavior, scorecards, or checker categories. | P0 | Scope control. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-030-FR01` | Review Lanes Protocol defines PRD Quality Review Lane. | `python3 scripts/clarity-scenario-check.py` | Read protocol. | Markdown source | check output |
| `PRD-030-FR03` | Lane output uses existing Review Lanes fields and recommendation values. | `python3 scripts/clarity-scenario-check.py` | Review copyable prompt shape. | Markdown source | check output |
| `PRD-030-FR04` | Protocol names product clarity, assumptions, acceptance quality, proof readiness, handoff readiness, and smallest first slice. | `python3 scripts/clarity-scenario-check.py` | Confirm focus stays advisory. | Markdown source | check output |
| `PRD-030-FR05` | Prompt Patterns and User Guide include copyable lane guidance. | docs HTML freshness check | Read prompts for boundary wording. | Markdown docs | generated docs HTML |
| `PRD-030-FR06` | PRD Protocol references optional PRD Quality Review Lane without replacing Requirements Gap And Conflict Review. | source inspection | Confirm both reviews remain distinct. | PRD Protocol | manual review |
| `PRD-030-FR09` | Inventory, roadmap, journal, changelog, and generated surfaces are current. | inventory, docs, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Public protocols and docs: changed to expose the lane.
- PRD shard: added as destination authority for this package capability.
- Generated HTML: regenerated as reading/review surfaces only.
- PRD approval: explicitly unchanged and still human-owned.
- External systems: not touched.

### Human Approval Gates

- The user still owns PRD approval, owner-file updates, PRD amendments, Architecture Shaping decisions, Decomposition, bead activation, implementation, GitHub mutation, external mutation, merge, migration, rollback, and sensitive-surface approval.
- Lane findings may recommend accepted, revise, split, blocked, or stop, but they cannot approve that recommendation.

### Forbidden Actions

- Do not treat PRD Quality Review Lane as PRD approval, task selection, bead activation, review approval, implementation acceptance, generated proof, scorecard authority, checker authority, follow-up task creation, owner-file rewrite, command approval, external mutation, GitHub mutation, registry behavior, optional-pack behavior, SaaS workspace behavior, export automation, MCP mutation, package-manager behavior, release-channel behavior, or a persona system.
- Do not include secrets, credentials, private data, provider configuration, dashboard values, customer records, or sensitive production details in lane output.

## Architecture / Project Context Impact

- No app architecture impact.
- No active-memory change.
- No new command, generated report field, compiler warning, PRD HTML behavior, scorecard, checker gate, registry, optional pack, package-manager behavior, adapter behavior, or runtime behavior.
- `scripts/clarity-scenario-check.py` gains text-contract checks only.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/REVIEW-LANES-PROTOCOL.md` | Optional PRD Quality Review Lane shape. | Produces advisory findings and acceptance questions only. | Text-contract and manual review. | `tasks/prds/PRD-030-prd-quality-review-lane.md` |
| `tasks/reference/PROMPT-PATTERNS.md` and `docs/PRECODE-USER-GUIDE.md` | Copyable lane prompt. | Invokes draft-PRD quality review without approval, rewrite, task creation, or mutation. | Text-contract and manual review. | `tasks/prds/PRD-030-prd-quality-review-lane.md` |
| `tasks/reference/PRD-PROTOCOL.md` | Optional pre-approval review routing. | Preserves Requirements Gap And Conflict Review and human PRD approval. | Source inspection. | `tasks/prds/PRD-030-prd-quality-review-lane.md` |
| `scripts/clarity-scenario-check.py` | Deterministic text-contract check. | Checks wording presence only. | Script run. | `tasks/prds/PRD-030-prd-quality-review-lane.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-030-prd-quality-review-lane.md`
- Owner protocol: `tasks/reference/REVIEW-LANES-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `tasks/prds/PRD-024-requirement-to-proof-traceability.md`
  - `tasks/prds/PRD-026-ears-acceptance-guidance.md`
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
  - generated PRD rewrite behavior
  - generated evidence reports except generated docs/PRD/roadmap HTML
  - PRD HTML feature changes
  - checker behavior beyond text-contract coverage
  - GitHub, deployment, provider dashboards, secrets, or environment files
- Required checks:
  - `python3 scripts/version-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 scripts/public-repo-check.py`
  - `python3 scripts/clarity-scenario-check.py`
  - `python3 scripts/prd-html.py --check`
  - `python3 scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
- Manual verification:
  - Confirm the lane cannot be mistaken for PRD approval, owner-file rewrite, implementation permission, task creation, scorecard authority, checker gate, or generated proof.
  - Confirm the lane complements Requirements Gap And Conflict Review instead of replacing or duplicating it.

## Anti-Shallow Checks

- If the lane output approves the PRD, it violates the PRD.
- If the lane rewrites the PRD or owner files from review output, it violates the PRD.
- If the lane creates implementation tasks or activates beads, it violates the PRD.
- If a score, grade, generated report, PRD HTML cue, or AI confidence becomes quality authority, it violates the PRD.

## Bead Proposals

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B030-prd-quality-review-lane` | `PRD-030-FR01` through `PRD-030-FR09`, `PRD-030-SEC01` through `PRD-030-SEC02`, `PRD-030-NFR01` through `PRD-030-NFR03` | PRD shard, review-lane protocol, prompt/user/PRD guidance, package inventory, clarity scenario coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-030-prd-quality-review-lane.md` | clarity scenario plus package/docs/roadmap checks |

## Compilation Notes

- `FEATURES.md` is not updated in this slice.
- V1 is a public package workflow contract, not a runtime capability.

## Open Questions

- None for v1.

## Approval

- Approval state: approved by maintainer implementation request on 2026-06-24.
