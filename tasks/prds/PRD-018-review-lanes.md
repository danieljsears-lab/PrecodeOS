---
prd_id: PRD-018
status: approved
owner: user
risk_level: medium
feature_link: Review Lanes
features_status: not compiled
related_prds:
  - PRD-005
  - PRD-009
---

# PRD-018 -- Review Lanes
<!-- ANCHOR: prd-018-review-lanes -->

> AUTHORITY: Destination shard for optional advisory review lanes attached to active beads.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, review acceptance, implementation acceptance, release approval, security certification, compliance approval, generated proof, command approval, follow-up task creation, external mutation, GitHub mutation, package-manager behavior, or a persona system.
> LOAD_WHEN: Reviewing, implementing, or decomposing the Review Lanes v1 package capability.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-18

## State

- ID: `PRD-018`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-18`

## Feature Link

- Feature: `Review Lanes`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-005`, `PRD-009`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped review and release-readiness guidance`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Review Lanes`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `tasks/beads/BEAD-SCHEMA.md`
- Stable facts:
  - Review / Acceptance Skill already helps users decide whether one active bead is ready for an evidence-based acceptance decision.
  - Release Readiness and Release Candidate Evidence Profile already prepare shipping evidence and approval questions without release authority.
  - Security-sensitive work already requires owner-file, verification, approval, and manual-review discipline.
  - Review Lanes should translate specialist judgment into acceptance questions without adding persona sprawl.
- Assumptions:
  - V1 should ship exactly two concrete optional lanes: Security Review Lane and Release / Docs Freshness Review Lane.
  - A dedicated protocol is justified because Review Lanes are broader than one skill prompt but should remain prompt/protocol-only.
  - Text-contract checks are enough for v1; generated reports and checker gates are deferred.
- Conflicts or stale inputs:
  - "Security review" can sound like certification. V1 must clearly say it is advisory review input, not security sign-off, compliance approval, or legal assurance.
  - "Release/docs freshness" can overlap with Release Readiness. V1 must prepare acceptance questions and missing-proof findings without approving release.
- Privacy or secrets redactions:
  - Review lane outputs must not include secrets, tokens, credentials, dashboard values, personal data samples, production configuration, private customer data, or sensitive provider details.

## Problem

Specialist checks can catch quality, security, release, and documentation drift, but making builders manage fake specialist personas adds ceremony and hidden authority.

PrecodeOS needs small review templates that attach to one active bead and turn specialist concerns into evidence questions without bypassing normal review, proof, owner-file, or approval paths.

## User Moment

- Before: A builder or agent asks for "security review" or "release/docs review" and gets broad advice, confidence, or unactionable summaries.
- After: The review produces a bounded lane result tied to the active bead, primary authority, recorded evidence, missing proof, acceptance questions, approvals still required, and promotion path.
- Why now: Review / Acceptance, Release Readiness, Release Candidate Evidence, and verification guidance are mature enough to support two concrete review templates without adding automation.

## Destination

- Destination statement: PrecodeOS exposes optional Review Lanes for Security and Release / Docs Freshness that help review one active bead without granting approval or creating tasks.
- Definition of done:
  - PRD-018 exists and is linked to related release/readiness surfaces.
  - Review Lanes Protocol defines when to use lanes, required inputs, stable output fields, two v1 lane templates, promotion paths, and forbidden actions.
  - Bead Schema names Review Lanes as optional body/closeout guidance only.
  - Prompt Patterns and User Guide include copyable lane prompts.
  - Package inventory lists the PRD and protocol.
  - Clarity scenario coverage checks lane names, output fields, and forbidden actions.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed.
- First useful vertical slice: prompt/protocol guidance and text-contract checks only.

## Users

- Primary user: Non-technical builder reviewing a completed or near-complete bead with security, release, or docs freshness risk.
- Secondary user: AI coding agent or support helper preparing review questions without mutating the project.
- Excluded user: Security auditor, compliance certifier, release manager, deploy bot, task planner, or automation expecting review output to approve work, create tasks, release, or mutate external systems.

## Goals

- Goal 1: Make specialist review questions easier to ask inside one active bead.
- Goal 2: Keep findings tied to evidence, missing proof, and acceptance questions.
- Goal 3: Preserve human approval for acceptance, release, security-sensitive work, external mutation, and follow-up promotion.
- Goal 4: Avoid persona sprawl, checker gates, generated reports, or required bead metadata in v1.

## Non-Goals

- Not doing: new command, checker gate, generated report, registry, optional pack, persona system, security certification, compliance approval, acceptance approval, release approval, follow-up task creation, owner-file rewrite, GitHub mutation, external mutation, package-manager behavior, release-channel behavior, app-runtime behavior, or required bead frontmatter.
- Deferred: more lane templates, generated review artifacts, stricter router/checker integration, requirement-to-proof traceability, accessibility advisory integration, performance review, QA review, design review, and dependency graph review.
- Explicitly out of scope: using lane findings to override active memory, the active bead, primary authority, owner files, PRDs, Closeout Evidence, Review mode, Release Readiness, or human approval.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-018-FR01` | Add a Review Lanes Protocol that defines advisory lane use, required inputs, output fields, lane templates, promotion paths, and forbidden actions. | P0 | Owner protocol. |
| `PRD-018-FR02` | V1 must include exactly two lane templates: Security Review Lane and Release / Docs Freshness Review Lane. | P0 | Avoid lane sprawl. |
| `PRD-018-FR03` | Lane output must include lane, review target, authority checked, evidence reviewed, findings, missing proof, acceptance questions, recommendation, approval still required, and promotion path. | P0 | Stable review shape. |
| `PRD-018-FR04` | Bead Schema must describe Review Lanes as optional bead-body or closeout guidance only, not required frontmatter. | P0 | Backward compatibility. |
| `PRD-018-FR05` | Prompt Patterns and User Guide must include copyable prompts for invoking and reviewing the two lanes. | P0 | User-facing invocation. |
| `PRD-018-FR06` | Package inventory must list the new PRD and protocol as public package surfaces. | P1 | Discoverability. |
| `PRD-018-FR07` | Clarity scenario coverage must check lane names, output fields, and forbidden actions. | P1 | Text contract only. |
| `PRD-018-FR08` | Roadmap, roadmap journal, maintainer changelog, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-018-SEC01` | Security Review Lane output must not claim certification, compliance approval, legal assurance, penetration-test completion, vulnerability absence, or security sign-off. | P0 | Advisory only. |
| `PRD-018-SEC02` | Review lane prompts must forbid secrets, credentials, private data, dashboard values, provider configuration, and external mutation unless a separate owner-approved path explicitly applies. | P0 | Sensitive-surface safety. |
| `PRD-018-SEC03` | Review lanes must not approve edits, acceptance, PRDs, beads, release, rollback, merge, migration, GitHub mutation, external mutation, or follow-up task creation. | P0 | Approval boundaries. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-018-NFR01` | Lane prompts must stay short enough to use during live review. | P0 | Avoid ceremony. |
| `PRD-018-NFR02` | Lane language must remain understandable without specialist vocabulary. | P1 | Beginner value. |
| `PRD-018-NFR03` | The lane protocol must stay independent of private maintainer files. | P0 | Public package completeness. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-018-FR01` | Review Lanes Protocol defines purpose, inputs, outputs, templates, and promotion paths. | `python3 scripts/clarity-scenario-check.py` | Read protocol. | Markdown source | check output |
| `PRD-018-FR02` | Protocol and prompts name only Security and Release / Docs Freshness as v1 templates. | `python3 scripts/clarity-scenario-check.py` | Confirm no extra lane template is introduced. | Markdown source | check output |
| `PRD-018-FR03` | Output fields are present in protocol and prompt surfaces. | `python3 scripts/clarity-scenario-check.py` | Review copyable prompt shape. | Markdown source | check output |
| `PRD-018-FR04` | Bead Schema describes Review Lanes as optional body/closeout guidance only. | source inspection | Confirm no required frontmatter field was added. | Bead Schema | manual review |
| `PRD-018-FR05` | User Guide and Prompt Patterns include copyable lane prompts. | docs HTML freshness check | Read prompts for brevity and boundary wording. | Markdown docs | generated docs HTML |
| `PRD-018-FR08` | Inventory, roadmap, journal, changelog, and generated surfaces are current. | inventory, docs, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Public protocols and docs: changed to expose the lane.
- PRD shard: added as destination authority for this package capability.
- Generated HTML: regenerated as reading/review surfaces only.
- Existing review, release-readiness, and verification behavior: not replaced.
- External systems: not touched.

### Human Approval Gates

- The user still owns review acceptance, release decisions, sensitive-surface approval, external mutation, merge, migration, rollback, GitHub mutation, owner-file updates, and follow-up bead creation.
- Lane findings may recommend accepted, revise, split, blocked, or stop, but they cannot approve that recommendation.

### Forbidden Actions

- Do not treat Review Lanes as acceptance approval, review approval, PRD approval, bead activation, release approval, security certification, compliance approval, follow-up task creation, owner-file rewrite, generated proof, command approval, external mutation, GitHub mutation, registry behavior, optional-pack behavior, package-manager behavior, release-channel behavior, or a persona system.
- Do not include secrets, credentials, private data, provider configuration, dashboard values, or sensitive production details in lane output.

## Architecture / Project Context Impact

- No app architecture impact.
- No active-memory change.
- No new command, schema, generated report, registry, optional pack, package-manager behavior, adapter behavior, or runtime behavior.
- `scripts/clarity-scenario-check.py` gains text-contract checks only.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/REVIEW-LANES-PROTOCOL.md` | Optional Security and Release / Docs Freshness lane review shapes. | Produces advisory findings and acceptance questions only. | Text-contract and manual review. | `tasks/prds/PRD-018-review-lanes.md` |
| `tasks/beads/BEAD-SCHEMA.md` | Optional bead-body or closeout guidance. | Review lanes may attach to a bead without required metadata. | Source inspection. | `tasks/prds/PRD-018-review-lanes.md` |
| `tasks/reference/PROMPT-PATTERNS.md` and `docs/PRECODE-USER-GUIDE.md` | Copyable lane prompts. | Invokes or reviews lanes without approval or mutation. | Text-contract and manual review. | `tasks/prds/PRD-018-review-lanes.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-018-review-lanes.md`
- Owner protocol: `tasks/reference/REVIEW-LANES-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `tasks/beads/BEAD-SCHEMA.md`
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
  - `AGENT.md`
  - `DECISIONS.md`
  - `tasks/todo.md`
  - target app code
  - setup/update scripts
  - deployment scripts
  - generated evidence reports
  - provider dashboards
  - secrets or environment files
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
  - Confirm both lane prompts stay short, require evidence, name missing proof, preserve approval gates, and cannot be mistaken for acceptance, release approval, security certification, compliance approval, or task creation.

## Anti-Shallow Checks

- If lane output mostly summarizes confidence instead of evidence, missing proof, and acceptance questions, it is too weak.
- If Security Review Lane implies security sign-off, it violates the PRD.
- If Release / Docs Freshness Review Lane approves release or replaces Release Readiness, it violates the PRD.
- If findings create tasks without user review, the lane has become hidden authority.
