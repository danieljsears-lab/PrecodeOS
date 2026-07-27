---
prd_id: PRD-028
status: approved
owner: Dan Sears / Recode
created: 2026-06-23
risk_level: medium
feature_link: Build Attribution Ledger
features_status: not compiled
related_prds:
  - PRD-025
last_updated: 2026-07-27
---

# PRD-028 -- Build Attribution Ledger
<!-- ANCHOR: prd-028-build-attribution-ledger -->

> AUTHORITY: Public requirements for generated Build Attribution Ledger evidence, reviewed human contributor and agent/tool attribution fields, confidence states, and accountability boundaries.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, merge approval, release approval, contributor scoring, blame assignment, telemetry, GitHub mutation, package registry, optional-pack behavior, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating build attribution, contributor accountability, agent/tool traceability, or the generated Build Attribution Ledger.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-07-27

## State

- ID: `PRD-028`
- Status: `approved`
- Owner: Dan Sears / Recode
- Risk level: `medium`
- Last updated: `2026-07-27`

## Feature Link

- Feature: Build Attribution Ledger
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-025`

## Source Inputs

- Source type: maintainer roadmap evidence and existing bead closeout evidence needs
- Source references: maintainer roadmap candidate and shipped implementation history
- Stable facts: attribution belongs in reviewed bead closeout and generated ledger evidence, not task authority.
- Assumptions: Git and journal hints are useful only after review into closeout evidence.
- Privacy or secrets redactions: do not collect telemetry, private dashboard data, or unrelated contributor identity data.

## Alignment / Grilling Summary

- Alignment method: maintainer roadmap planning
- Shared design concept: generated attribution evidence should help reviewers answer who contributed to a bead without becoming blame, scoring, telemetry, or task assignment.
- Key decisions reached: closeout-reviewed attribution is the strongest source; Git and journal data remain evidence hints.
- Remaining implementation-changing questions: none for the approved v1 slice.

## Domain Language

| Term | Status | Plain-English meaning | Aliases | Avoid/confusing terms | UI/code/test examples | Source pointer |
|---|---|---|---|---|---|---|
| Build Attribution Ledger | introduced | Generated evidence that summarizes contributor and agent/tool attribution by bead. | attribution ledger | task registry, people registry, blame ledger | `logs/build-attribution-ledger.md` | This PRD |
| Git author hint | introduced | Git-derived evidence that may inform attribution review but does not prove contributor identity by itself. | authorship hint | contributor identity proof | `git_author_hint` | This PRD |

## PRFAQ-Lite

- Press-release claim: PrecodeOS can show reviewed who-built-what evidence without turning collaboration into scoring or blame.
- Customer problem: a future reviewer needs compact attribution context after handoffs or team work.
- Customer FAQ: Does the ledger decide who owns the work? No; it is generated evidence only.
- Internal FAQ: Does Git authorship prove attribution? No; reviewed closeout evidence wins.
- Appetite: narrow generated evidence and protocol integration.
- Kill or pause criteria: stop if the ledger becomes a task tracker, scoring layer, telemetry surface, or package registry.

## Summary

PrecodeOS should help a builder answer "who built what?" without turning attribution into task authority, blame, scoring, telemetry, or a package registry.

The Build Attribution Ledger compiles reviewed attribution evidence from beads and supporting Git/journal hints. Closeout-reviewed attribution is the strongest source. Git authorship, generated journal entries, branch names, tool logs, and teammate notes are evidence hints only until reviewed into bead Closeout Evidence.

## Problem

Existing Precode surfaces show what bead changed, what evidence exists, and what branch/worktree context may matter. They do not preserve a compact shared view of human contributor, contributor role, agent/tool surface, reviewer, and attribution uncertainty by bead.

That gap matters more once Small Team Collaboration Lane, handoffs, fresh-context review, and generated build journal evidence are used together. A future reviewer should be able to trace who contributed the work and which agent/tool surface helped, without relying on chat memory.

## Goals

- Add reviewed build attribution fields to bead closeout.
- Add generated ledger JSON and Markdown views for attribution by bead.
- Preserve human contributor and agent/tool surface separately.
- Label missing, partial, reviewed, and Git-hint-only attribution clearly.
- Keep the ledger generated evidence only.
- Record the shipped feature in maintainer roadmap history as an implemented candidate.

## Non-Goals

- No task assignment or task selection.
- No PRD approval, bead activation, implementation acceptance, merge approval, or release approval.
- No contributor scoring, blame assignment, productivity ranking, telemetry, analytics, dashboard backend, or external tracking system.
- No GitHub mutation, PR approval, label/comment mutation, workflow mutation, or project-board behavior.
- No package registry, plugin registry, optional-pack behavior, install/update behavior, release channel, command wrapper, or package-manager behavior.
- No new active-memory file.

## User Moment

- Before: a reviewer can see what changed but may need to reconstruct who contributed from scattered closeout, Git, and journal hints.
- After: a reviewer has a compact generated attribution view while source authority stays in reviewed closeout evidence.
- Why now: collaboration, delegation, and review surfaces make attribution context more useful.

## Destination

- Destination statement: PrecodeOS provides generated build-attribution evidence that is subordinate to reviewed bead closeout.
- Definition of done: attribution fields, ledger output, public guidance, generated surfaces, and maintainer history are updated and validated.
- First useful vertical slice: read-only JSON/Markdown ledger plus closeout field preservation.

## Product Constitution Fit

- `PRODUCT.md` loaded: not needed
- Product promise fit: supports bounded, evidence-backed agent collaboration.
- User and job fit: helps builders and reviewers understand implementation provenance.
- Strategy and non-goal fit: preserves evidence-first review without telemetry or scoring.
- Current bet or success signal affected: stronger handoff and review clarity.
- Product constitution update needed: no

## Users

- Primary user: builder or reviewer checking who contributed to a bead.
- Secondary user: maintainer inspecting package collaboration evidence.
- Excluded user: anyone seeking scoring, blame, task assignment, telemetry, or registry behavior.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-028-FR01` | Add closeout fields for human contributor, contributor role, agent/tool surface, attribution reviewer, and attribution uncertainty. | P0 | Existing reviewed values must be preserved by closeout refresh. |
| `PRD-028-FR02` | Add `scripts/build-attribution-ledger.py` as a read-only checker that prints JSON by default. | P0 | Default command writes no files. |
| `PRD-028-FR03` | Add `--self-test` deterministic fixtures for reviewed closeout, partial closeout, missing attribution, generated warning, and forbidden uses. | P0 | No network or external dependency. |
| `PRD-028-FR04` | Expose `build_attribution` in compiled state and generated OS Health sidecars. | P1 | Sidecars are generated evidence only. |
| `PRD-028-FR05` | Generate `logs/build-attribution-ledger.json` and `logs/build-attribution-ledger.md`. | P1 | Markdown must carry generated authority demotion. |
| `PRD-028-FR06` | Ledger entries must include bead identity, status, primary authority, human contributor, role, agent/tool surface, reviewer, uncertainty, source, confidence, Git author hint, journal timestamp, changed-path hints, and warnings. | P1 | Git hints must not become contributor identity. |
| `PRD-028-FR07` | Protocols, prompts, user docs, package inventory, maintainer changelog, roadmap, roadmap journal, and generated surfaces must be updated. | P1 | Maintainer-history follow-through is part of done. |

## Acceptance Oracle Matrix

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-028-FR01` | `scripts/update-bead-closeout.py` preserves attribution fields and fills explicit missing values. | Code review and closeout refresh behavior. |
| `PRD-028-FR02` | `python3 scripts/build-attribution-ledger.py` prints JSON and writes no files. | Command output. |
| `PRD-028-FR03` | `python3 scripts/build-attribution-ledger.py --self-test` passes. | Command output. |
| `PRD-028-FR04` / `PRD-028-FR05` | `python3 scripts/os-health.py` refreshes attribution sidecars. | `logs/build-attribution-ledger.json/md`. |
| `PRD-028-FR06` | Ledger entries expose attribution identity, source, confidence, hints, changed-path context, and warnings without treating Git hints as contributor identity. | Source review and generated ledger review. |
| `PRD-028-FR07` | Scenario, inventory, docs, PRD HTML, roadmap HTML, memory, and version checks pass. | Validation commands. |

## Required Validation

```bash
python3 scripts/build-attribution-ledger.py --self-test
python3 scripts/clarity-scenario-check.py
python3 scripts/file-inventory.py --check
python3 scripts/public-repo-check.py
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
bash scripts/validate-memory.sh
python3 scripts/version-check.py
PYTHONPYCACHEPREFIX=/private/tmp/precode-pycache python3 -m py_compile scripts/build-attribution-ledger.py scripts/os_compiler.py scripts/os-health.py scripts/precode_outputs.py scripts/update-bead-closeout.py scripts/clarity-scenario-check.py
```

## Risk And Permission Model

The ledger answers attribution questions only as evidence. It must route any durable correction back to bead Closeout Evidence, owner files, recorded checks, coordinator review, or maintainer history. It must not become a second tracker, task registry, people registry, plugin registry, package registry, or authority surface.

## Architecture / Project Context Impact

- `PROJECT-CONTEXT.md` impact: none.
- Architecture impact: generated evidence and closeout field preservation only.
- Data model impact: generated ledger fields only; no telemetry store or external database.
- Security/privacy impact: avoid private identity, secrets, telemetry, or external mutation.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| Build attribution ledger script | `python3 scripts/build-attribution-ledger.py` | Read-only generated attribution evidence. | self-test and generated output review | This PRD |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-028-build-attribution-ledger.md`
- Owner surfaces likely in play: closeout update script, OS compiler/health output, attribution ledger output, public docs/protocol references, and generated surfaces.
- Forbidden assumptions: do not treat generated ledger output as task assignment, contributor scoring, blame, telemetry, merge approval, or implementation acceptance.

## Anti-Shallow Checks

- Does attribution source distinguish reviewed closeout from Git or journal hints?
- Does the ledger avoid scoring, blame, telemetry, people registry, and package registry behavior?
- Does any durable correction route back to closeout evidence or owner files?

## Bead Proposals

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B028-build-attribution-ledger` | `PRD-028-FR01` through `PRD-028-FR07` | Closeout attribution fields, generated ledger, docs/protocol references, generated surfaces, and maintainer history are updated and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | This PRD | attribution self-test and package checks |

## Compilation Notes

- Feature entry: Build Attribution Ledger
- Functional requirements to compile: `PRD-028-FR01` through `PRD-028-FR07`
- Acceptance updates needed: generated evidence remains evidence only.

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should future attribution evidence include richer external provider hints? | Follow-up scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-23
- Approval notes: Approved as a read-only generated attribution evidence slice with no scoring, blame, telemetry, task authority, registry behavior, or package-manager behavior.
