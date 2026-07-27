---
prd_id: PRD-031
status: approved
owner: Dan Sears / Recode
created: 2026-06-24
risk_level: medium
feature_link: First PRD Walkthrough
features_status: not compiled
related_prds:
  - PRD-001
last_updated: 2026-07-27
---

# PRD-031 -- First PRD Walkthrough
<!-- ANCHOR: prd-031-first-prd-walkthrough -->

> AUTHORITY: Public requirements for the First PRD Walkthrough guidance path from rough idea to PRD readiness.
> NOT_AUTHORITY: Active memory, task selection, automatic PRD drafting, PRD approval, bead activation, implementation permission, roadmap or backlog authority, generated progress, external integrations, hosted workspace behavior, command-wrapper behavior, registry behavior, optional-pack behavior, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating the beginner-facing First PRD Walkthrough guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-07-27

## State

- ID: `PRD-031`
- Status: `approved`
- Owner: Dan Sears / Recode
- Risk level: `medium`
- Last updated: `2026-07-27`

## Feature Link

- Feature: First PRD Walkthrough
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-001`

## Source Inputs

- Source type: maintainer roadmap evidence and beginner workflow friction
- Source references: public first-reader route, PRD Protocol, Workflow Selection, Prompt Patterns
- Stable facts: First PRD Walkthrough is discoverability guidance over existing evidence-first workflows.
- Assumptions: beginner builders need one plain-language rough-idea entrypoint before PRD shaping.
- Privacy or secrets redactions: source materials remain evidence and should be reviewed before promotion.

## Alignment / Grilling Summary

- Alignment method: maintainer roadmap planning
- Shared design concept: route rough ideas through Product Brief, Conviction Packet, Local Source Intake, and PRD shaping without approving PRDs or coding.
- Key decisions reached: no new protocol file, command, generated report, hosted workspace, or approval shortcut.
- Remaining implementation-changing questions: none for the approved v1 slice.

## Domain Language

| Term | Status | Plain-English meaning | Aliases | Avoid/confusing terms | UI/code/test examples | Source pointer |
|---|---|---|---|---|---|---|
| First PRD Walkthrough | introduced | Beginner-facing request for the rough-idea-to-PRD-readiness path. | first PRD path | automatic PRD drafting, approval shortcut | `Ideation: use First PRD Walkthrough for my rough idea.` | This PRD |
| Conviction Packet | reused | Evidence packet that should go through Local Source Intake before PRD shaping. | packet | approved PRD | Product Definition Gate wording | PRD Protocol |

## PRFAQ-Lite

- Press-release claim: PrecodeOS gives first-time builders one safe path from rough idea to PRD readiness.
- Customer problem: a builder may not know which product-definition prompt to use first.
- Customer FAQ: Does the walkthrough approve coding? No; human PRD approval remains required.
- Internal FAQ: Does this add a new protocol? No; it routes existing surfaces.
- Appetite: public docs/protocol/prompt discoverability only.
- Kill or pause criteria: stop if the walkthrough becomes automatic PRD drafting, task selection, or implementation permission.

## Summary

PrecodeOS should give first-time non-technical builders one visible path from a rough idea to PRD readiness without pretending the path approves a PRD or authorizes coding.

The First PRD Walkthrough packages existing Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and gentle PRD ramp guidance into a named walkthrough across current public docs and protocols.

## Problem

PrecodeOS already has strong product-definition pieces, but a new builder can miss the shortest safe sequence. That creates two opposite risks: the builder may stall before PRD shaping, or the agent may jump from excitement, research, or workbook evidence directly into requirements or code.

## Goals

- Make the rough-idea-to-PRD-readiness path easy to find from daily and onboarding surfaces.
- Name "First PRD Walkthrough" as a beginner-facing request that routes through existing protocols.
- Preserve Product Brief, Conviction Packet, research notes, and workbook output as evidence only.
- Keep Local Source Intake before PRD shaping when a Conviction Packet or source material is used.
- Keep human PRD approval before feature compilation, decomposition, bead proposal activation, or coding.
- Add narrow text-contract coverage so future edits do not turn the walkthrough into hidden authority.

## Non-Goals

- No new public protocol file.
- No new command, checker command, readiness score, or generated report.
- No automatic PRD drafting or approval.
- No generated PRD authoring surface, export hub, hosted workspace, MCP mutation, SaaS runtime, or external integration.
- No PRD approval shortcut, bead activation path, task selection, roadmap or backlog creation, owner-file mutation, or implementation permission.
- No command-wrapper, registry, optional-pack, install/update, release-channel, or package-manager behavior.
- No edits to active memory or normal task state.

## User Moment

- Before: a builder with a rough idea may browse multiple product-definition surfaces or let an agent jump too quickly.
- After: the builder can ask for the named walkthrough and move through evidence-first product framing.
- Why now: the public docs need a compact beginner-safe entry into the PRD gate.

## Destination

- Destination statement: PrecodeOS provides a named rough-idea walkthrough that leads to PRD readiness while preserving approval gates.
- Definition of done: docs, protocols, prompt patterns, text-contract coverage, generated surfaces, and maintainer history agree.
- First useful vertical slice: named prompt route plus authority-boundary wording.

## Product Constitution Fit

- `PRODUCT.md` loaded: not needed
- Product promise fit: reinforces builder control before coding.
- User and job fit: helps non-technical builders turn rough ideas into approved product definition.
- Strategy and non-goal fit: keeps evidence and approval separate from implementation permission.
- Current bet or success signal affected: beginner PRD readiness.
- Product constitution update needed: no

## Users

- Primary user: first-time non-technical builder with a rough idea.
- Secondary user: support helper or AI assistant routing the builder safely.
- Excluded user: anyone seeking automatic PRD drafting, approval, bead activation, or implementation permission.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-031-FR01` | Public user and daily guide surfaces must include a named First PRD Walkthrough entrypoint. | P0 | The path must be visible without reading the whole PRD protocol first. |
| `PRD-031-FR02` | Idea-to-PRD, PRD, Workflow Selection, and Prompt Patterns surfaces must route the walkthrough through the existing evidence-first sequence. | P0 | No new protocol file for v1. |
| `PRD-031-FR03` | The walkthrough must state that Product Briefs, Conviction Packets, workbook output, and research are evidence only. | P0 | These artifacts do not approve requirements or implementation. |
| `PRD-031-FR04` | The walkthrough must require Local Source Intake before PRD shaping when the builder brings a Conviction Packet, workbook output, notes, research, screenshots, or similar source material. | P0 | Prevents direct packet-to-requirements promotion. |
| `PRD-031-FR05` | The walkthrough must preserve human PRD approval before feature compilation, decomposition, bead activation, or coding. | P0 | PRD approval remains a separate human gate. |
| `PRD-031-FR06` | `scripts/clarity-scenario-check.py` must include text-contract coverage for the walkthrough's authority boundaries. | P1 | Existing checker only; no new command. |
| `PRD-031-FR07` | Package inventory, maintainer changelog, roadmap, roadmap journal, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer-history follow-through is part of done. |

## Acceptance Oracle Matrix

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-031-FR01` / `PRD-031-FR02` | User Guide, Daily Cockpit, How-To guide, Idea-to-PRD, PRD Protocol, Workflow Selection, and Prompt Patterns include the named walkthrough and route it through existing surfaces. | Static review and generated docs. |
| `PRD-031-FR03` / `PRD-031-FR04` / `PRD-031-FR05` | The text-contract fixture fails if required boundary language disappears from owner surfaces. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-031-FR06` | The walkthrough fixture is part of the existing clarity scenario check and adds no standalone command. | Code review and command output. |
| `PRD-031-FR07` | PRD HTML, docs HTML, maintainer roadmap HTML, changelog, and roadmap journal reflect the shipped slice. | Generated surface checks. |

## Required Validation

```bash
python3 scripts/clarity-scenario-check.py
python3 scripts/prd-html.py
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py
python3 _maintainer/scripts/roadmap-html.py --check
```

## Risk And Permission Model

The First PRD Walkthrough is a discoverability and guidance layer over existing PrecodeOS workflows. It can help a builder ask for the right next artifact, but it cannot decide the product, approve a PRD, create or activate beads, mutate owner files, select tasks, or authorize implementation.

## Architecture / Project Context Impact

- `PROJECT-CONTEXT.md` impact: none.
- Architecture impact: none; workflow guidance only.
- Data model impact: none.
- Security/privacy impact: source inputs remain evidence until reviewed and promoted.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| First PRD Walkthrough prompt route | Daily Cockpit and Prompt Patterns wording | Routes rough ideas through existing evidence-first workflow. | clarity scenario and generated docs review | This PRD |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-031-first-prd-walkthrough.md`
- Owner surfaces likely in play: PRD Protocol, Workflow Selection, Idea-to-PRD guidance, Prompt Patterns, Daily Cockpit, User Guide, and generated docs.
- Forbidden assumptions: do not approve PRDs, create beads, mutate owner files, select tasks, or authorize implementation from walkthrough output.

## Anti-Shallow Checks

- Does the walkthrough preserve Local Source Intake before PRD shaping when source material exists?
- Does the text keep Product Briefs and Conviction Packets evidence-only?
- Does human PRD approval remain separate from feature compilation, decomposition, bead activation, and coding?

## Bead Proposals

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B031-first-prd-walkthrough` | `PRD-031-FR01` through `PRD-031-FR07` | Public docs, protocols, prompts, clarity coverage, generated surfaces, and maintainer history expose the named walkthrough without approval shortcuts. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | This PRD | clarity and generated docs checks |

## Compilation Notes

- Feature entry: First PRD Walkthrough
- Functional requirements to compile: `PRD-031-FR01` through `PRD-031-FR07`
- Acceptance updates needed: none beyond preserving approval gates.

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should future tooling generate a PRD-readiness packet from the walkthrough? | Follow-up scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-24
- Approval notes: Approved as discoverability guidance over existing product-definition surfaces, not automatic PRD drafting, PRD approval, bead activation, or implementation permission.
