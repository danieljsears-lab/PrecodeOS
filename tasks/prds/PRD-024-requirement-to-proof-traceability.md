---
prd_id: PRD-024
status: approved
owner: user
risk_level: medium
feature_link: Requirement-To-Proof Traceability
features_status: not compiled
related_prds:
  - PRD-020
---

# PRD-024 -- Requirement-To-Proof Traceability
<!-- ANCHOR: prd-024-requirement-to-proof-traceability -->

> AUTHORITY: Destination shard for advisory requirement, bug-behavior, and acceptance-criterion proof traceability in PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, review acceptance, implementation acceptance, release approval, generated proof, generated trace report, test-generation authority, package-manager behavior, release-channel behavior, or external mutation.
> LOAD_WHEN: Reviewing, implementing, or decomposing requirement-to-proof traceability guidance for PRDs, beads, bugfixes, closeout evidence, or review prompts.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## State

- ID: `PRD-024`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-23`

## Feature Link

- Feature: `Requirement-To-Proof Traceability`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-020`

## Source Inputs

- Source type: `maintainer roadmap evidence | existing release evidence traceability`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Requirement-To-Proof Traceability`
  - `tasks/prds/PRD-020-verification-release-evidence.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/reference/REVIEW-LANES-PROTOCOL.md`
- Stable facts:
  - PRD-020 already defines release-specific verification and release evidence traceability.
  - PRDs already use stable requirement IDs and an Acceptance Oracle Matrix.
  - Beads already name `requirement_ids`, checks, verification type, closeout evidence, and review decision.
  - Generated tests, screenshots, browser notes, AI critiques, generated reports, and trace tables are review input until recorded, accepted, or promoted through existing evidence paths.
- Assumptions:
  - The first useful slice should generalize guidance and prompts before adding generated reports or broad checker behavior.
  - Deterministic clarity fixtures are enough to protect the advisory boundary in v1.
- Conflicts or stale inputs:
  - "Traceability" can imply enterprise process, mandatory matrices, or generated proof. This PRD narrows the work to compact advisory traces used only when proof drift matters.
- Privacy or secrets redactions:
  - Proof traces must not require secrets, tokens, credentials, personal data samples, private dashboard values, provider configuration, or sensitive production details.

## Problem

Checks can pass without proving the requirement, bug behavior, or acceptance criterion the user cares about. Builders need a compact way to see which claim each recorded check or manual verification step supports, what it does not prove, and what uncertainty remains.

## User Moment

- Before: A bead has requirement IDs, checks, generated tests, browser notes, or manual comments, but the user must infer whether they actually prove the promised behavior.
- After: The closeout, PRD acceptance oracle, or review prompt can name the requirement or behavior, evidence lane, recorded source, proven claim, limits, and remaining uncertainty.
- Why now: Release-specific traceability already exists; the remaining gap is normal PRD, bead, bugfix, and acceptance-review proof drift.

## Destination

- Destination statement: PrecodeOS can show the path from requirement, bug behavior, or acceptance criterion to recorded proof without treating the trace itself as proof.
- Definition of done:
  - PRD-024 exists and links to PRD-020.
  - Verification Guardrail defines a compact generic requirement-to-proof trace shape.
  - PRD Protocol and PRD template clarify Acceptance Oracle Matrix proof mapping.
  - Session Completion/Handoff and Bead Schema route closeout through generic proof traces when requirement IDs, bug behavior, or acceptance claims are central to review confidence.
  - Review Lanes and Prompt Patterns expose proof-trace review questions.
  - User Guide, Daily Cockpit when useful, and package inventory expose the public guidance.
  - Clarity scenario coverage pins advisory traceability and trace-table-not-proof behavior.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed.
- First useful vertical slice: protocol guidance, template guidance, prompt/user guidance, package inventory, and deterministic fixtures only.

## Users

- Primary user: Non-technical builder deciding whether implementation evidence proves the requirement, bug behavior, or acceptance criterion.
- Secondary user: AI coding agent or reviewer preparing closeout, bugfix proof, PRD acceptance mapping, or review-lane findings.
- Excluded user: Enterprise requirements manager, generated proof system, test generator, project-management tracker, release bot, or compliance tool.

## Goals

- Goal 1: Make proof drift visible before confidence outruns evidence.
- Goal 2: Keep requirement, bug behavior, acceptance criterion, evidence lane, recorded source, proven claim, limits, and uncertainty together.
- Goal 3: Preserve recorded checks, structured manual verification, closeout evidence, review decision, and human approval as the durable proof path.

## Non-Goals

- Not doing: new command, new generated report, generated proof authority, enterprise traceability workflow, mandatory trace table for tiny work, test-generation feature, PRD approval, bead activation, review acceptance, release approval, deployment automation, GitHub mutation, external mutation, command wrapper, registry, optional pack, package-manager behavior, or release-channel behavior.
- Deferred: production checker warnings for generic trace fields, richer Review Lane templates, generated diff artifacts, NFR-specific proof families, and stricter requirement-to-proof enforcement.
- Explicitly out of scope: treating a generated test, generated property, trace table, screenshot, browser note, AI critique, external status summary, or generated report as complete proof by itself.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-024-FR01` | Verification Guardrail must define a compact requirement-to-proof trace shape. | P0 | Advisory human-authored evidence framing only. |
| `PRD-024-FR02` | PRD Protocol and PRD template must make Acceptance Oracle Matrix proof mapping explicit without adding enterprise ceremony. | P0 | Uses existing requirement IDs. |
| `PRD-024-FR03` | Session Completion/Handoff and Bead Schema must route closeout through proof traces when requirement IDs, bug behavior, or acceptance claims are central to review confidence. | P0 | Does not require every tiny bead to use a trace. |
| `PRD-024-FR04` | Review Lanes and Prompt Patterns must expose proof-trace review questions and missing-proof wording. | P1 | Review input only. |
| `PRD-024-FR05` | User-facing docs and package inventory must explain the guidance and boundaries. | P1 | Public discoverability. |
| `PRD-024-FR06` | Clarity scenarios must pin advisory-only behavior and refuse trace-table-as-proof wording. | P1 | Deterministic local regression. |
| `PRD-024-FR07` | Roadmap, roadmap journal, maintainer changelog, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-024-SEC01` | Proof traces must not require secrets, tokens, credentials, personal data samples, private dashboard values, provider configuration, or sensitive production details. | P0 | Use redacted/manual references when needed. |
| `PRD-024-SEC02` | Traceability guidance must not approve sensitive actions, release actions, external mutation, review acceptance, PRD approval, or bead transition. | P0 | Human approval remains required. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-024-NFR01` | Guidance must stay compact enough for non-technical builders. | P0 | Avoid enterprise traceability. |
| `PRD-024-NFR02` | The slice must stay independent of private maintainer files. | P0 | Public package completeness. |
| `PRD-024-NFR03` | Script coverage must stay advisory and avoid generated-proof authority. | P0 | No new report or command. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-024-FR01` | Verification Guardrail includes generic requirement-to-proof trace fields and guardrails. | `python3 scripts/clarity-scenario-check.py` | Read protocol. | Markdown source | check output |
| `PRD-024-FR02` | PRD template clarifies proof mapping from requirement to evidence lane and recorded source. | `python3 scripts/prd-html.py --check` | Review template wording. | Markdown source | PRD HTML |
| `PRD-024-FR03` | Closeout and bead guidance name when generic traces are useful and optional. | `python3 scripts/clarity-scenario-check.py` | Review wording. | Markdown source | check output |
| `PRD-024-FR04` | Prompt and review guidance can request a proof trace without approving work. | `python3 scripts/clarity-scenario-check.py` | Review copyable prompt. | Markdown source | check output |
| `PRD-024-FR07` | Roadmap, journal, changelog, and generated surfaces are current. | inventory, docs, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before sensitive mutation, release action, external mutation, PRD approval, review acceptance, bead transition, GitHub mutation, dashboard mutation, provider mutation, or destructive command.
- Stop if the requirement or behavior, evidence lane, recorded source, proven claim, proof limit, or remaining uncertainty is unclear and the trace is needed for acceptance confidence.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` | Generic requirement-to-proof trace shape. | Explains traceability without approving proof. | Text-contract and manual review. | `tasks/prds/PRD-024-requirement-to-proof-traceability.md` |
| `tasks/prds/PRD-000-template.md` | Acceptance Oracle Matrix proof mapping. | Helps agents map requirement IDs to recorded evidence. | PRD HTML check and manual review. | `tasks/prds/PRD-024-requirement-to-proof-traceability.md` |
| `tasks/reference/PROMPT-PATTERNS.md` | Copyable proof-trace prompt. | Requests traceability without mutation or approval. | Clarity scenarios and docs freshness. | `tasks/prds/PRD-024-requirement-to-proof-traceability.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-024-requirement-to-proof-traceability.md`
- Related PRD: `tasks/prds/PRD-020-verification-release-evidence.md`
- Owner protocol: `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/reference/REVIEW-LANES-PROTOCOL.md`
  - `tasks/beads/BEAD-SCHEMA.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
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
  - target app code
  - provider configuration
  - dashboards
  - secrets or environment files
  - GitHub mutation
  - deployment scripts
  - generated evidence reports except generated docs/PRD/roadmap HTML
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
  - Confirm traceability guidance prepares evidence review only.
  - Confirm no wording treats generated tests, generated properties, trace tables, screenshots, browser notes, AI critiques, generated reports, or external status summaries as complete proof.

## Anti-Shallow Checks

- If the proof trace does not say what requirement, bug behavior, or acceptance criterion is being proven, it is too vague.
- If the trace does not point to recorded evidence or structured manual verification, it is review input only.
- If the trace does not name what it does not prove, it can create false confidence.
- If the trace becomes mandatory for tiny docs-only work, it violates the PRD.

## Bead Proposals

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B024-requirement-to-proof-traceability` | `PRD-024-FR01` through `PRD-024-FR07`, `PRD-024-SEC01` through `PRD-024-SEC02`, `PRD-024-NFR01` through `PRD-024-NFR03` | PRD shard, protocol guidance, template guidance, prompt/user guidance, package inventory, clarity scenario coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-024-requirement-to-proof-traceability.md` | clarity scenario, package/docs/roadmap checks |

## Compilation Notes

- `FEATURES.md` is not updated in this slice.
- V1 is a public package evidence-quality contract, not a runtime traceability system.

## Open Questions

- None for v1.

## Approval

- Approval state: approved by maintainer implementation request on 2026-06-23.
