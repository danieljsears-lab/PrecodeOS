---
prd_id: PRD-020
status: approved
owner: user
risk_level: high
feature_link: Verification And Release Evidence
features_status: not compiled
related_prds:
  - PRD-005
  - PRD-009
---

# PRD-020 -- Verification And Release Evidence
<!-- ANCHOR: prd-020-verification-release-evidence -->

> AUTHORITY: Destination shard for advisory verification-to-release evidence traceability in PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, review acceptance, implementation acceptance, release approval, deployment approval, generated proof, package release management, provider checklist, external mutation, GitHub mutation, package-manager behavior, release-channel behavior, or evidence-report authority.
> LOAD_WHEN: Reviewing, implementing, or decomposing verification and release evidence traceability for release-relevant user-project work.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-19

## State

- ID: `PRD-020`
- Status: `approved`
- Owner: `user`
- Risk level: `high`
- Last updated: `2026-06-19`

## Feature Link

- Feature: `Verification And Release Evidence`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-005`, `PRD-009`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped release-readiness lane`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Verification And Release Evidence`
  - `tasks/prds/PRD-005-release-readiness-lane.md`
  - `tasks/prds/PRD-009-release-candidate-evidence-lane.md`
  - `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
- Stable facts:
  - Release Readiness prepares evidence and approval questions only.
  - Release Candidate Evidence Profiles are human-authored and do not approve release.
  - Recorded checks, structured manual verification, Closeout Evidence, and review decisions remain the durable proof surfaces.
  - Screenshots, browser notes, GitHub status, generated reports, and dashboard observations remain review input until recorded, accepted, or promoted through existing evidence paths.
- Assumptions:
  - The first useful slice should strengthen existing protocols and `completion-check.py` output instead of adding a new generated report.
  - Advisory warnings are enough; no release gate should become mandatory.
- Conflicts or stale inputs:
  - "Release evidence" can imply deploy tooling or package release management. This PRD narrows the work to user-project evidence traceability and advisory warnings only.
- Privacy or secrets redactions:
  - Release evidence must not expose secrets, tokens, credentials, personal data samples, private dashboard values, provider configuration, or sensitive production details.

## Problem

PrecodeOS already asks for release-readiness notes and release-candidate profiles, but proof can still drift. A builder may see checks, screenshots, browser notes, generated reports, or GitHub status and still not know which requirement or behavior they prove, whether the release smoke path is covered, or whether missing evidence should block release confidence.

## User Moment

- Before: A release-relevant bead has closeout text and some checks, but the user must infer whether the proof actually traces to the behavior being shipped.
- After: Release evidence names the requirement or behavior proven, the evidence lane, the recorded source, release-specific proof, and remaining approvals, while `completion-check.py` warns when the trace is missing.
- Why now: Release Readiness and Release Candidate Evidence Profile guidance exist, and the next gap is evidence quality around them.

## Destination

- Destination statement: PrecodeOS makes release-relevant proof traceable enough for a human release decision without turning checks, generated output, or profile text into release approval.
- Definition of done:
  - PRD-020 exists and links to PRD-005 and PRD-009.
  - Release Readiness Protocol defines verification and release evidence review fields.
  - Verification Guardrail and Session Completion/Handoff protocols require release-relevant closeout to name the proof path when release confidence depends on it.
  - Bead Schema, Prompt Patterns, User Guide, and package inventory expose the guidance.
  - `completion-check.py` reports advisory release-evidence details through `scripts/os_compiler.py`.
  - Clarity scenario coverage pins complete, incomplete, review-input-only, and non-approval states.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed.
- First useful vertical slice: protocol guidance, prompt guidance, advisory checker warnings, and deterministic fixtures only.

## Users

- Primary user: Non-technical builder deciding whether release-relevant work has enough proof for a human release decision.
- Secondary user: AI coding agent or support helper preparing closeout, release readiness, or profile evidence without mutating external systems.
- Excluded user: Deploy bot, package-release manager, provider automation, CI release gate, or project-management system expecting release execution.

## Goals

- Goal 1: Trace release confidence from requirement or behavior to recorded proof.
- Goal 2: Make missing smoke, docs freshness, rollback or blocked escape, approval, and decision-state evidence visible before release decisions.
- Goal 3: Keep browser notes, screenshots, GitHub status, generated reports, and profile text subordinate to recorded evidence and human review.

## Non-Goals

- Not doing: new command, new generated evidence report, generated proof authority, deployment automation, rollback automation, provider checklist, CI release gate, GitHub mutation, dashboard mutation, package release management, release approval, review acceptance, package-manager behavior, release-channel behavior, registry behavior, optional-pack behavior, or external mutation.
- Deferred: richer provider-specific evidence templates, release-readiness skill invocation, generated release evidence reports, NFR-specific checker families, and stricter requirement-to-proof enforcement.
- Explicitly out of scope: treating `ready for human release decision`, screenshots, browser notes, GitHub status, generated reports, smoke checks, or advisory checker output as release approval.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-020-FR01` | Add verification and release evidence review guidance to Release Readiness Protocol. | P0 | Human-authored traceability fields only. |
| `PRD-020-FR02` | Release evidence should name requirement or behavior proven, evidence lane, recorded check or manual source, smoke path, docs/support freshness, rollback or blocked escape, approvals still required, and decision state. | P0 | Uses existing tier names. |
| `PRD-020-FR03` | Verification Guardrail and Session Completion/Handoff protocols must route release-relevant closeout to this proof path when release confidence depends on it. | P0 | Does not weaken sensitive-surface gates. |
| `PRD-020-FR04` | `completion-check.py` must expose advisory release-evidence details through compiled completion/handoff output. | P0 | No new command or report. |
| `PRD-020-FR05` | Advisory warnings must cover missing release profile fields, missing release-readiness fields, review-input-only evidence claims, and missing requirement/behavior-to-proof trace. | P0 | Warning only. |
| `PRD-020-FR06` | Prompt Patterns, User Guide, Bead Schema, and package inventory must expose copyable guidance and public package ownership. | P1 | User-facing discoverability. |
| `PRD-020-FR07` | Clarity scenarios must pin complete, incomplete, review-input-only, and non-approval behavior. | P1 | Deterministic local regression. |
| `PRD-020-FR08` | Roadmap, roadmap journal, maintainer changelog, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-020-SEC01` | Release evidence must not require or expose secrets, tokens, credentials, personal data samples, private dashboard values, provider configuration, or sensitive production details. | P0 | Evidence can reference redacted/manual observations. |
| `PRD-020-SEC02` | Advisory checker output must not approve release, deployment, rollback, merge, migration, GitHub mutation, dashboard mutation, external mutation, or review acceptance. | P0 | Human approval remains required. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-020-NFR01` | Guidance must stay compact enough for non-technical builders. | P0 | Avoid enterprise ceremony. |
| `PRD-020-NFR02` | Checker warnings must be advisory and avoid false authority. | P0 | Existing `completion-check.py` output only. |
| `PRD-020-NFR03` | The feature must stay independent of private maintainer files. | P0 | Public package completeness. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-020-FR01` | Release Readiness Protocol includes verification and release evidence review fields. | `python3 scripts/clarity-scenario-check.py` | Read protocol. | Markdown source | check output |
| `PRD-020-FR04` | `completion-check.py` exposes `release_evidence` details. | `python3 scripts/clarity-scenario-check.py` and `python3 scripts/completion-check.py` | Inspect JSON shape. | Synthetic bead fixtures and active state | command output |
| `PRD-020-FR05` | Incomplete release profile or review-input-only proof triggers warnings. | `python3 scripts/clarity-scenario-check.py` | Confirm warning wording is advisory. | Synthetic closeout/profile text | check output |
| `PRD-020-FR06` | Prompt Patterns, User Guide, Bead Schema, and inventory include guidance. | docs HTML freshness check | Review copyable prompts. | Markdown docs | generated docs HTML |
| `PRD-020-FR08` | Roadmap, journal, changelog, and generated surfaces are current. | inventory, docs, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before deployment, promotion, rollback, merge, migration, dashboard update, secret change, billing/auth/payment/private-data change, GitHub mutation, external-service mutation, production configuration change, or package release action.
- Stop if the requirement or behavior proven, evidence lane, recorded source, smoke path, docs/support freshness, rollback or blocked escape, decision state, approval owner, or remaining uncertainty is unclear.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/RELEASE-READINESS-PROTOCOL.md` | Verification and release evidence review guidance. | Frames traceability and missing proof only. | Text-contract and manual review. | `tasks/prds/PRD-020-verification-release-evidence.md` |
| `scripts/completion-check.py` via `scripts/os_compiler.py` | Advisory `release_evidence` warnings in completion/handoff output. | Warns without approving release or creating proof. | Clarity scenarios and command run. | `tasks/prds/PRD-020-verification-release-evidence.md` |
| Prompt and user docs | Copyable prompt for release evidence review. | Requests evidence traceability without mutation or approval. | Text-contract and docs freshness. | `tasks/prds/PRD-020-verification-release-evidence.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-020-verification-release-evidence.md`
- Parent PRDs:
  - `tasks/prds/PRD-005-release-readiness-lane.md`
  - `tasks/prds/PRD-009-release-candidate-evidence-lane.md`
- Owner protocol: `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/beads/BEAD-SCHEMA.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/os_compiler.py`
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
  - `python3 scripts/completion-check.py`
  - `python3 scripts/prd-html.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
- Manual verification:
  - Confirm guidance and checker output prepare evidence only.
  - Confirm no wording authorizes deployment, release, rollback, merge, migration, dashboard mutation, secret changes, GitHub mutation, external mutation, package release management, release channels, or package-manager behavior.

## Anti-Shallow Checks

- If a release evidence trace does not identify what behavior or requirement was proven, it is too vague.
- If screenshots, browser notes, GitHub status, or generated reports are treated as proof without recorded evidence, it violates the PRD.
- If `ready for human release decision` is treated as release approval, it violates the PRD.
- If checker warnings block or approve release by themselves, they violate the PRD.

## Bead Proposals

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B020-verification-release-evidence` | `PRD-020-FR01` through `PRD-020-FR08`, `PRD-020-SEC01` through `PRD-020-SEC02`, `PRD-020-NFR01` through `PRD-020-NFR03` | PRD shard, protocol guidance, prompt/user guidance, package inventory, advisory checker warnings, clarity scenario coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-020-verification-release-evidence.md` | clarity scenario, completion-check, package/docs/roadmap checks |

## Compilation Notes

- `FEATURES.md` is not updated in this slice.
- V1 is a public package evidence-quality contract, not a runtime release capability.

## Open Questions

- None for v1.

## Approval

- Approval state: approved by maintainer implementation request on 2026-06-19.
