---
prd_id: PRD-017
status: approved
owner: user
risk_level: medium
feature_link: Bugfix Spec Lane
features_status: not compiled
related_prds:
  - PRD-015
---

# PRD-017 -- Bugfix Spec Lane
<!-- ANCHOR: prd-017-bugfix-spec-lane -->

> AUTHORITY: Destination shard for the compact bugfix spec lane used before narrow stable-fix implementation.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, implementation acceptance, repair approval, generated proof, automatic rollback policy, setup/update mutation, command-wrapper behavior, package-manager behavior, or a parallel bug-tracking system.
> LOAD_WHEN: Reviewing, implementing, or decomposing the Bugfix Spec Lane across stable-fix, recovery, verification, prompt, and public support guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-17

## State

- ID: `PRD-017`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-17`

## Feature Link

- Feature: `Bugfix Spec Lane`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-015`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Bugfix Spec Lane`
  - `tasks/reference/RECOVERY-PROTOCOL.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
- Stable facts:
  - PrecodeOS already has stable-fix eligibility routing through `scripts/next-step.py`.
  - Stable-fix eligibility is advisory only and does not approve mutation, acceptance, release, rollback, setup/update mutation, or transitions.
  - Narrow repairs still need a clearer pre-implementation shape so current behavior, expected behavior, unchanged behavior, and regression proof are explicit before edits.
- Assumptions:
  - The first implementation should update protocols, prompt patterns, public docs, and scenario text-contract checks before adding script behavior.
  - A bugfix spec is useful only when tied to one active bead and normal closeout evidence.

## Problem

Bug fixes can expand from narrow repairs into hidden refactors or regressions when the defect, expected outcome, and behavior that must not change are not named before implementation.

## User Moment

- Before: A user or agent calls work a "small fix" without making the repair boundary, proof path, and unchanged behavior visible.
- After: The agent prepares a compact bugfix spec before editing, then routes the work as current-bead stable fix, needs-evidence, recovery repair, broader PRD/bead work, or release-readiness work.
- Why now: The package already has stable-fix routing and recovery guidance; the missing piece is a lightweight spec shape that keeps surgical repairs from becoming hidden scope.

## Destination

- Destination statement: A narrow repair can use the Bugfix Spec Lane to name current behavior, expected behavior, unchanged behavior, owner file, root cause if known, fix approach, regression proof, and route decision before implementation.
- Definition of done:
  - Recovery Protocol defines the bugfix spec shape inside Stable-Fix Eligibility.
  - Verification Guardrail Protocol names regression-proof expectations for bugfix specs.
  - Prompt Patterns includes a copyable Bugfix Spec Lane prompt that requires no editing until owner file, route, and proof path are clear.
  - Public stable-fix support docs point users to the bugfix spec before small repair edits.
  - Clarity scenario coverage checks the prompt/spec fields and advisory-only guardrails.
  - Package inventory, generated docs/PRD/roadmap surfaces, roadmap history, roadmap journal, and maintainer changelog are current.
- First useful vertical slice: docs/protocol/prompt guidance and text-contract checks only; no new command or classifier output.

## Users

- Primary user: Beginner or non-technical builder asking whether a small repair can proceed safely.
- Secondary user: AI coding agent or support helper preparing a bounded repair.
- Excluded user: Automation expecting the bugfix spec to approve edits, create tasks, accept implementation, release, roll back, or mutate setup/update state.

## Goals

- Goal 1: Make narrow bugfix boundaries visible before implementation.
- Goal 2: Preserve stable-fix routing and Recovery Protocol boundaries.
- Goal 3: Require regression proof that shows the defect is fixed and named unchanged behavior still holds.
- Goal 4: Keep the lane prompt-based and bead-bound for v1.

## Non-Goals

- Not doing: new command, new task system, bug tracker, auto-generated implementation tasks, classifier schema expansion, repair approval, implementation acceptance, PRD approval, bead activation, release approval, rollback, setup/update mutation, destructive commands, generated-proof authority, command-wrapper behavior, package-manager behavior, registry, optional pack, or external mutation.
- Deferred: richer router metadata or recovery scenario fixtures if real usage shows the docs-only lane is insufficient.
- Explicitly out of scope: using a bugfix spec to bypass active memory, the active bead, recorded checks, closeout evidence, review, or user approval.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-017-FR01` | Recovery Protocol must define a compact bugfix spec shape with current behavior, expected behavior, unchanged behavior, owner file, root cause if known, fix approach, regression proof, and route decision. | P0 | Stable-fix refinement. |
| `PRD-017-FR02` | The bugfix spec must require no edits until the owner file, route, and proof path are clear. | P0 | Diagnosis before repair. |
| `PRD-017-FR03` | Verification guidance must require regression proof that shows the defect is fixed and named unchanged behavior still holds. | P0 | Avoid hidden regressions. |
| `PRD-017-FR04` | Code-changing bugfixes should prefer failing-first or characterization checks when practical, and record why not when impractical. | P1 | Risk-based proof. |
| `PRD-017-FR05` | Prompt Patterns must expose a copyable Bugfix Spec Lane prompt. | P0 | User-facing invocation. |
| `PRD-017-FR06` | Public stable-fix support docs must route small repair claims through the bugfix spec without implying approval. | P1 | Discoverability. |
| `PRD-017-FR07` | Scenario coverage must verify the bugfix spec fields and advisory-only forbidden actions. | P1 | Text contract only. |
| `PRD-017-FR08` | Package inventory, roadmap, roadmap journal, generated docs/PRD/roadmap surfaces, and maintainer changelog must be updated. | P1 | Required maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-017-SEC01` | Bugfix spec guidance must not approve destructive commands, overwrites, deletes, rollback, setup/update mutation, transition approval, acceptance, release, generated-report regeneration, external mutation, or secret handling. | P0 | Explicit approval required. |
| `PRD-017-SEC02` | The lane must not require private maintainer files or expose private maintainer roadmap details in public user guidance. | P0 | Public package complete on its own. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-017-NFR01` | The spec must be short enough to use in a live chat before implementation. | P0 | Avoid ceremony. |
| `PRD-017-NFR02` | The lane must remain understandable without engineering vocabulary. | P1 | Beginner value. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-017-FR01` | Recovery Protocol names the compact bugfix spec fields. | `python3 scripts/clarity-scenario-check.py` | Read Stable-Fix Eligibility section. | Markdown source | check output |
| `PRD-017-FR02` | Prompt requires no editing until owner file, route, and proof path are clear. | `python3 scripts/clarity-scenario-check.py` | Review prompt wording. | Markdown source | check output |
| `PRD-017-FR03` | Verification guidance requires fixed defect plus unchanged behavior proof. | `python3 scripts/clarity-scenario-check.py` | Read Verification Guardrail Protocol. | Markdown source | check output |
| `PRD-017-FR05` | Prompt Patterns includes Bugfix Spec Lane. | `python3 scripts/clarity-scenario-check.py` | Review prompt. | Markdown source | check output |
| `PRD-017-FR06` | Public docs route stable-fix claims through bugfix spec guidance. | docs HTML check | Read docs. | Markdown docs | generated docs HTML |
| `PRD-017-FR08` | Inventory, roadmap, journal, changelog, and generated surfaces are current. | inventory, docs, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Public protocols and docs: changed to expose the lane.
- PRD shard: added as destination authority for this package capability.
- Generated HTML: regenerated as reading/review surfaces only.
- Stable-fix classifier: unchanged for v1.
- External systems: not touched.

### Human Approval Gates

- Any actual bugfix implementation still requires the active bead, owner file, files in play, checks, and user approval gates already required by PrecodeOS.
- The bugfix spec may recommend a route, but it cannot approve that route.

### Forbidden Actions

- Do not treat the bugfix spec as repair approval, implementation acceptance, release approval, rollback approval, setup/update permission, transition approval, destructive command approval, generated proof, or a new task system.
- Do not mutate external systems or secrets from this lane.

## Architecture / Project Context Impact

- No app architecture impact.
- No active-memory change.
- No new command, schema, generated report, registry, optional pack, package-manager behavior, or adapter behavior.
- `scripts/clarity-scenario-check.py` gains text-contract checks only.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/RECOVERY-PROTOCOL.md` | Stable-fix bugfix spec shape. | Diagnosis before repair; route remains advisory. | Text-contract and manual review. | `tasks/prds/PRD-017-bugfix-spec-lane.md` |
| `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` | Regression proof expectations. | Proof shows fixed defect and unchanged behavior. | Text-contract and manual review. | `tasks/prds/PRD-017-bugfix-spec-lane.md` |
| `tasks/reference/PROMPT-PATTERNS.md` | Copyable Bugfix Spec Lane prompt. | Produces spec before edits. | Text-contract and manual review. | `tasks/prds/PRD-017-bugfix-spec-lane.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-017-bugfix-spec-lane.md`
- Secondary reference files:
  - `tasks/reference/RECOVERY-PROTOCOL.md`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
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
  - `scripts/os_compiler.py` unless docs-only implementation proves insufficient
  - target app code
  - setup/update scripts
  - deployment scripts
  - generated evidence reports
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
  - Confirm the lane requires current behavior, expected behavior, unchanged behavior, and regression proof.
  - Confirm it does not approve edits, recovery, release, rollback, setup/update mutation, bead transition, acceptance, destructive commands, or generated proof.

## Anti-Shallow Checks

- If the bugfix spec does not name unchanged behavior, it is too weak.
- If the proof does not show both fixed behavior and preserved behavior, it is too weak.
- If the work touches sensitive, release-relevant, setup/update, external, or broad behavior surfaces, do not treat it as a current-bead stable fix.
- If the owner file or route is unclear, stop before editing.

## Bead Proposals

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B017-bugfix-spec-lane` | `PRD-017-FR01` through `PRD-017-FR08`, `PRD-017-SEC01`, `PRD-017-NFR01` | PRD, protocols, prompt, docs, scenario text contract, inventory, roadmap history, and generated surfaces are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-017-bugfix-spec-lane.md` | protocol/docs checks plus manual boundary review |

## Compilation Notes

- `FEATURES.md` remains unchanged for this package maintenance slice.
- `tasks/prds-html/` must be regenerated after this PRD is added.

## Open Questions

- None for v1.

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-17
- Approval notes: User approved implementation of the decision-complete Bugfix Spec Lane plan, explicitly selecting a PRD-backed docs/protocol-first refinement and excluding new commands, task systems, approval paths, generated-proof authority, active-memory changes, setup/update mutation, release approval, rollback, registries, optional packs, and package-manager behavior.
