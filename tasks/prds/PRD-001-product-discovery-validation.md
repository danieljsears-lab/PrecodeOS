---
prd_id: PRD-001
status: approved
owner: user
risk_level: medium
feature_link: Product Discovery Validation
features_status: not compiled
related_prds: []
---

# PRD-001 -- Product Discovery Validation
<!-- ANCHOR: prd-001-product-discovery-validation -->

> AUTHORITY: Draft destination shard for adding Product Discovery Validation to PrecodeOS before PRD shaping.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, route structure, schema definitions, generated progress, or proof that any product idea is worth building.
> LOAD_WHEN: Reviewing, approving, or decomposing the Product Discovery Validation improvement for PrecodeOS.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-28

## State

- ID: `PRD-001`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-05-28`

## Feature Link

- Feature: `Product Discovery Validation`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `none`

## Source Inputs

- Source type: `maintainer roadmap | research | alignment interview`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md`
  - `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`
  - `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md`
  - Product Talk discovery references, Strategyzer value proposition testing, and NN/g research-method framing
- Stable facts:
  - Precode already has Local Source Intake, Idea-to-PRD, Product Definition Gate, PRD shards, and bead decomposition.
  - Roadmap rank 1 names Product Discovery Validation as P0.
  - Discovery must remain advisory and beginner-safe.
- Assumptions:
  - A reference protocol plus docs hooks is enough for v1.
  - No checker script is needed in the first implementation.
- Conflicts or stale inputs:
  - none identified
- Privacy or secrets redactions:
  - none
- Candidate requirements:
  - Add a first-class discovery protocol before PRD shaping.
  - Add lightweight bridge fields and prompts to existing docs.
- Candidate non-goals:
  - Do not make discovery mandatory for tiny tasks.
  - Do not let discovery approve PRDs or activate beads.
- Authority files likely affected:
  - `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`
  - `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`
  - `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`
  - `tasks/prds/PRD-000-template.md`
  - `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`
  - `docs/PRECODE-FILE-INVENTORY.md`
- Discarded or stale inputs:
  - Mandatory scorecard or full product-management framework

## Alignment / Grilling Summary

- Alignment method: `one-question-at-a-time grilling`
- Shared design concept: Product Discovery Validation is an advisory upstream protocol that helps beginners decide whether an idea has enough evidence to enter PRD shaping.
- Key decisions reached:
  - Place the protocol before PRD work.
  - Use advisory `proceed | pause | narrow | kill` language.
  - Use a compact evidence ladder plus assumption categories.
  - Use a short Discovery Summary as the main artifact.
  - Prefer learning before building when evidence is weak.
- Recommended answers accepted:
  - Advisory default, solo beginner audience, Core Four methods, supportive skeptic tone.
- Recommended answers rejected or changed:
  - Mandatory discovery for every PRD.
  - Workbook-only implementation.
  - Validation scorecard as the main output.
- Remaining implementation-changing questions:
  - none for v1 docs/protocol implementation
- Stale or discarded assumptions:
  - That "validation" should mean proof rather than evidence-informed judgment.

## Discovery Evidence

- Discovery completed: `yes`
- Reason skipped: `not skipped`
- Evidence strength: `medium`
- Riskiest assumption: Beginners and agents will use an advisory discovery protocol when it is referenced from the right workflow surfaces.
- Discovery recommendation: `proceed`

## Problem

Precode helps shape ideas into PRDs, but it does not yet fully help builders decide whether an idea is worth defining before feature planning starts. Without a discovery layer, a beginner can produce a plausible PRD for an unproven, too-broad, or solution-first idea.

## User Moment

- Before: A builder asks an agent to turn an exciting idea into a PRD or implementation plan without enough evidence.
- After: The builder can see the strongest evidence, weakest assumption, current workaround, smallest learning step, and advisory recommendation before PRD work.
- Why now: The maintainer roadmap ranks Product Discovery Validation as the next P0 core improvement.

## Destination

- Destination statement: Precode has a beginner-safe Product Discovery Validation protocol and workflow hooks that route broad, risky, market-facing, paid, evidence-poor, or solution-first ideas through advisory discovery before PRD shaping.
- Definition of done:
  - New protocol exists with authority boundaries and guardrails.
  - Workflow docs route appropriate ideas to discovery.
  - PRD template includes a minimal Discovery Evidence bridge.
  - Workbook and user guides teach the path without making it mandatory ceremony.
  - File inventory knows the new protocol.
- First useful vertical slice: Docs/protocol implementation only; no checker script in v1.

## Product Constitution Fit

- `PRODUCT.md` loaded: `yes`
- Product promise fit: Fits PrecodeOS as a repo-native control layer that keeps AI coding work bounded, inspectable, and human-approved.
- User and job fit: Supports solo non-technical builders and agents working as planning collaborators.
- Strategy and non-goal fit: Preserves tiny active memory and avoids becoming a full product-management framework.
- Current bet or success signal affected: Adds a stronger upstream product-shaping guardrail.
- Design or voice affected: Beginner-facing, plain-language, supportive skeptic tone.
- Product constitution update needed: `no`

## Users

- Primary user: Solo beginner or non-technical builder using Precode with an AI coding agent.
- Secondary user: AI agent shaping a rough idea before PRD drafting.
- Excluded user: Teams needing a full research operations or product-management suite.

## Goals

- Goal 1: Help builders judge whether an idea has enough evidence for PRD shaping.
- Goal 2: Keep discovery advisory, short, and beginner-safe.
- Goal 3: Preserve existing Precode authority and approval boundaries.

## Non-Goals

- Not doing: Checker script, scorecard thresholds, research database, mandatory discovery for every PRD.
- Deferred: Advisory detection of risky PRDs missing discovery.
- Explicitly out of scope: Any change that lets generated discovery approve work, activate beads, or update active memory.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-001-FR01` | Add a Product Discovery Validation reference protocol with triggers, non-triggers, methods, evidence ladder, assumptions, interview guidance, Discovery Summary format, recommendations, promotion path, and guardrails. | P0 | Protocol is the primary artifact. |
| `PRD-001-FR02` | Update Workflow Selection and Idea-to-PRD so worth-building uncertainty routes to Product Discovery Validation before PRD shaping. | P0 | Keep advisory. |
| `PRD-001-FR03` | Add a minimal Discovery Evidence bridge to the PRD template. | P0 | Not a full report requirement. |
| `PRD-001-FR04` | Update the workbook and beginner guides to teach discovery validation prompts and boundaries. | P0 | Beginner-facing. |
| `PRD-001-FR05` | Update the file inventory to include the new protocol. | P0 | Maintains discoverability. |

### UX Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-001-UX01` | Use plain language for evidence strength and `proceed | pause | narrow | kill`. | P0 | Avoid PM jargon where possible. |
| `PRD-001-UX02` | Keep prompts supportive but skeptical. | P0 | Challenge assumptions without taking product control. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-001-SEC01` | Warn users not to paste secrets, credentials, private transcripts, billing values, or sensitive personal data into discovery artifacts. | P0 | Matches workbook boundaries. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-001-NFR01` | Do not add active-memory files or generated authority surfaces. | P0 | Preserves kernel. |
| `PRD-001-NFR02` | No new checker script in v1. | P1 | Docs/protocol hooks only. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-001-FR01` | Protocol file exists with required sections and guardrails. | `validate-memory.sh` | Read protocol. | none | bead closeout |
| `PRD-001-FR02` | Workflow docs reference discovery before PRD shaping for worth-building uncertainty. | `workflow-check.py` | Read workflow hooks. | none | bead closeout |
| `PRD-001-FR03` | PRD template has lightweight Discovery Evidence fields. | `validate-memory.sh` | Inspect template. | none | bead closeout |
| `PRD-001-FR04` | Beginner docs include discovery prompts and boundaries. | `version-check.py` | Inspect guide sections. | none | bead closeout |
| `PRD-001-FR05` | File inventory includes new protocol. | `file-inventory.py --check` | Inspect inventory. | none | bead closeout |

## Risk And Permission Model

### Sensitive Surfaces

- Auth: none
- Payments: none
- User data: discovery guidance may mention user interviews and sensitive inputs
- Uploads: none
- External services: research links only
- Secrets: explicit warning required
- Destructive actions: none

### Human Approval Gates

- Approval required before:
  - PRD approval
  - bead activation
  - promoting discovery findings into `PRODUCT.md`, `DECISIONS.md`, or another authority file
- Stop if:
  - discovery output is treated as approval or task selection
  - a tiny task starts requiring heavy discovery ceremony
- Escalate when:
  - discovery touches regulated, financial, medical, legal, safety, personal-data, or sensitive trust surfaces

### Tool And Environment Boundaries

- Allowed tools: local file edits and validation commands
- Network needs: none during implementation
- Dependency changes: none
- Dashboard/manual steps: none

## Architecture / Project Context Impact

- Project context impact: `minor`
- `PROJECT-CONTEXT.md` loaded: `yes`
- Architecture authority updates needed: `no`
- Route/API authority updates needed: `no`
- Schema authority updates needed: `no`
- Security authority updates needed: `no`
- Decision log updates needed: `no`

## Agent Context Contract

- Primary authority file: `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`
  - `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`
  - `tasks/prds/PRD-000-template.md`
  - `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`
  - `docs/PRECODE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
- Files or folders out of scope:
  - scripts, generated reports, app code
- Required checks:
  - `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
  - `bash scripts/record-check.sh -- python3 scripts/version-check.py`
  - `bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check`
  - `bash scripts/record-check.sh -- python3 scripts/workflow-check.py`
- Manual verification:
  - Confirm discovery artifacts remain evidence only.
- Forbidden assumptions:
  - `proceed` means PRD approval.
  - discovery is mandatory for every PRD.

## Anti-Shallow Checks

- User problem named: yes
- Non-goals named: yes
- Before/after user moment clear: yes
- Requirements observable: yes
- Sensitive surfaces identified: yes
- Authority files identified: yes
- First bead can be one logical unit: yes
- Generated text reviewed by user: approved through maintainer implementation request

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B001-product-discovery-validation-docs` | `PRD-001-FR01` through `PRD-001-FR05` | Protocol and docs hooks are added, versioned, validated, and manually reviewed. | `human_in_loop` | `static_only` | `fresh_context_recommended` | `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` | validation commands plus manual docs review |

## Compilation Notes

- Feature entry: Product Discovery Validation.
- Functional requirements to add or amend: `PRD-001-FR01` through `PRD-001-FR05` after approval.
- MVP slice notes: v1 is protocol and docs only.
- Acceptance updates needed: none.

## Open Questions

Only include blockers that can change implementation.

| Question | Affects | Blocking? |
|---|---|---|
| Should a future checker detect risky PRDs without discovery evidence? | Follow-up scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-05-28
- Approval notes: User asked Codex to implement the P0 plan with Product Discovery Validation first, using the existing PRD and protocol surfaces as the v1 implementation baseline.
