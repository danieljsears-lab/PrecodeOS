---
prd_id: PRD-026
status: approved
owner: user
risk_level: low
feature_link: EARS-Style Acceptance Criteria Guidance
features_status: not compiled
related_prds: []
---

# PRD-026 -- EARS-Style Acceptance Criteria Guidance
<!-- ANCHOR: prd-026-ears-acceptance-guidance -->

> AUTHORITY: Public requirements for optional EARS-style acceptance-writing guidance across acceptance, PRD, prompt, and user docs.
> NOT_AUTHORITY: Active memory, product decisions, PRD approval, bead activation, implementation acceptance, generated proof, required PRD schema, required acceptance syntax, checker gate, command wrapper, registry, optional pack, package-manager behavior, route structure, schema definitions, or implementation status.
> LOAD_WHEN: Implementing or reviewing EARS-style acceptance guidance, PRD acceptance oracles, or acceptance-criteria prompt guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## State

- ID: `PRD-026`
- Status: `approved`
- Owner: `user`
- Risk level: `low`
- Last updated: `2026-06-23`

## Feature Link

- Feature: `EARS-Style Acceptance Criteria Guidance`
- `FEATURES.md` status: `not compiled`
- Originating maintainer roadmap candidate: `EARS-Style Acceptance Criteria Guidance`

## Source Inputs

- Source type: `maintainer roadmap candidate | approved implementation plan | Kiro pattern comparison`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` candidate `EARS-Style Acceptance Criteria Guidance`
  - `_maintainer/PRECODE-KIRO-COMPARISON.md`
  - `ACCEPTANCE.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/prds/PRD-000-template.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
- Stable facts:
  - PRD shards already use an Acceptance Oracle Matrix with an `Expected behavior` column.
  - `ACCEPTANCE.md` owns project-level done checks and acceptance criteria.
  - Requirements Gap And Conflict Review already calls out vague or unverifiable acceptance oracles.
- Assumptions:
  - The first useful slice is writing guidance and text-contract coverage, not a new checker.
  - Optional EARS-style wording can improve clarity without becoming formal requirements syntax.
- Conflicts or stale inputs:
  - The roadmap candidate number may drift after maintenance; the candidate title is the stable source.
- Privacy or secrets redactions:
  - Acceptance examples must not require secrets, credentials, private data, production values, or external systems.

## Problem

Acceptance criteria often stay too vague for agents to test or for builders to review confidently.

Without a lightweight writing pattern, "done" can become a feeling instead of an observable behavior tied to a requirement.

## User Moment

- Before: A builder or agent sees an acceptance criterion such as "works well" or "handles errors" and cannot tell what proof would satisfy it.
- After: The criterion can be rewritten, where helpful, as `WHEN [condition/event] THE SYSTEM SHALL [expected behavior]` while still allowing other clear acceptance wording.
- Why now: PRD and acceptance surfaces already exist, so this can ship as guidance instead of machinery.

## Destination

- Destination statement: Precode offers optional EARS-style acceptance guidance that makes expected behavior easier to verify without making syntax mandatory.
- Definition of done:
  - `ACCEPTANCE.md` explains the optional pattern and examples.
  - PRD protocol/template/schema guidance mentions optional EARS wording for vague acceptance oracles.
  - Prompt Patterns, User Guide, Daily Cockpit, package inventory, and navigation surfaces expose the guidance.
  - `scripts/clarity-scenario-check.py` covers the optional, non-enforcing contract.
  - Maintainer changelog, roadmap, roadmap journal, and generated docs/PRD/roadmap surfaces are refreshed.
- First useful vertical slice: docs, prompt guidance, PRD guidance, and clarity scenario coverage only.

## Goals

- Goal 1: Make vague acceptance criteria easier to turn into observable expected behavior.
- Goal 2: Keep the guidance readable for non-technical builders.
- Goal 3: Preserve valid non-EARS acceptance criteria and human approval gates.

## Non-Goals

- Not doing: required EARS syntax, PRD schema enforcement, dedicated EARS checker, generated report field, PRD approval, implementation acceptance, generated proof, task selection, bead activation, command wrapper, registry, optional pack, package-manager behavior, external mutation, or Kiro integration.
- Deferred: richer requirement-to-proof traceability, property-based test guidance, or stricter acceptance-oracle review after real PRD examples show repeated ambiguity.
- Explicitly out of scope: treating EARS wording as not required syntax in name only while rejecting clear non-EARS acceptance criteria, or treating EARS wording as proof by itself.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-026-FR01` | `ACCEPTANCE.md` must define the optional `WHEN [condition/event] THE SYSTEM SHALL [expected behavior]` pattern with plain examples. | P0 | Acceptance owner surface. |
| `PRD-026-FR02` | PRD protocol/template/schema guidance must mention optional EARS-style phrasing near acceptance oracles without changing table shape. | P0 | No schema change. |
| `PRD-026-FR03` | Prompt Patterns, User Guide, and Daily Cockpit must include copyable guidance for clarifying vague acceptance criteria. | P1 | Discoverability. |
| `PRD-026-FR04` | Clarity scenario coverage must protect optionality, non-enforcement, no checker, no generated proof, no PRD approval, and no implementation authority. | P0 | Text-contract fixture only. |
| `PRD-026-FR05` | Package inventory, README or AI navigation, maintainer changelog, roadmap, roadmap journal, generated docs, generated PRD HTML, and generated roadmap HTML must be updated as needed. | P1 | Package-maintenance follow-through. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-026-NFR01` | Guidance must stay beginner-readable and short. | P0 | Avoid ceremony. |
| `PRD-026-NFR02` | The implementation must not add a dedicated EARS checker, PRD schema enforcement, CLI command, generated report field, or write-back path. | P0 | Preserves roadmap guardrail. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-026-FR01` | WHEN acceptance wording is vague THE SYSTEM SHALL offer optional EARS-style examples without requiring the syntax. | `python3 scripts/clarity-scenario-check.py` | Read `ACCEPTANCE.md`. | Markdown source | check output |
| `PRD-026-FR02` | WHEN PRD acceptance oracles are reviewed THE SYSTEM SHALL allow optional EARS-style phrasing while preserving the existing matrix shape. | `python3 scripts/clarity-scenario-check.py` | Read PRD protocol/template/schema. | Markdown source | check output |
| `PRD-026-FR03` | WHEN a user asks to clarify acceptance criteria THE SYSTEM SHALL provide prompts that do not approve PRDs, activate beads, accept implementation, or code. | `python3 scripts/clarity-scenario-check.py` | Read prompt and user docs. | Markdown source | check output |
| `PRD-026-FR04` | WHEN contract fixtures run THE SYSTEM SHALL fail if EARS is missing from required surfaces or implied as mandatory/enforced/proof. | `python3 scripts/clarity-scenario-check.py` | Inspect fixture terms. | Markdown source | check output |
| `PRD-026-FR05` | WHEN generated surfaces are checked THE SYSTEM SHALL keep docs, PRD HTML, and roadmap HTML fresh from canonical Markdown. | docs/PRD/roadmap checks | Read generated surfaces. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before PRD approval, owner-file updates, bead creation or activation, implementation, review acceptance, generated surface promotion, external mutation, or any new checker/command behavior beyond the approved text-contract fixture.
- Stop if guidance starts requiring EARS syntax, rejecting clear non-EARS criteria, changing PRD table schema, treating wording as proof, or implying Kiro import/runtime behavior.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-026-ears-acceptance-guidance.md`
- Owner/reference files:
  - `ACCEPTANCE.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/prds/PRD-000-template.md`
  - `tasks/prds/PRD-SHARD-SCHEMA.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/clarity-scenario-check.py`
  - `README.md`
  - `llms.txt`
  - `docs-html/`
  - `tasks/prds-html/`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
  - `_maintainer/PRECODE-ROADMAP.html`
- Files or folders out of scope:
  - active memory
  - target app code
  - dedicated EARS checker
  - generated report fields
  - schema enforcement
  - command wrappers
  - external systems
- Required checks:
  - `python3 scripts/clarity-scenario-check.py`
  - `bash scripts/validate-memory.sh`
  - `python3 scripts/prd-html.py --check`
  - `python3 scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`

## Forbidden Assumptions

- EARS-style syntax is required.
- Non-EARS acceptance criteria are invalid.
- EARS wording is proof by itself.
- Generated PRD HTML can persist or approve acceptance wording.
- Guidance imports Kiro specs, hooks, CLI behavior, or runtime authority into Precode.

## Bead Proposals

No active bead is created by this PRD. If decomposed later, use one package-maintenance bead covering acceptance guidance, contract fixture coverage, generated surfaces, and maintainer follow-through together.

## Approval

- Approval status: approved by maintainer implementation request on 2026-06-23.
- Approval notes: implement as optional guidance and clarity fixture coverage only.
