---
prd_id: PRD-035
status: approved
owner: Dan Sears / Recode
risk_level: medium
feature_link: AFK / Delegation Safety Improvements
features_status: not compiled
related_prds:
  - PRD-020
  - PRD-025
  - PRD-034
created: 2026-06-29
last_updated: 2026-07-27
---

# PRD-035 -- AFK / Delegation Safety Improvements
<!-- ANCHOR: prd-035-afk-delegation-safety-improvements -->

> AUTHORITY: Public requirements for bounded AFK and delegation safety guidance in PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, command approval, autonomous execution approval, parallel execution approval, review acceptance, merge approval, generated proof, command-wrapper behavior, registry behavior, optional-pack behavior, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating AFK-candidate, bounded-AFK, delegated-agent, or small-team re-entry safety guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-07-27

## State

- ID: `PRD-035`
- Status: `approved`
- Owner: Dan Sears / Recode
- Risk level: `medium`
- Last updated: `2026-07-27`

## Feature Link

- Feature: AFK / Delegation Safety Improvements
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-020`, `PRD-025`, `PRD-034`

## Source Inputs

- Source type: maintainer roadmap evidence and delegation safety friction
- Source references: Decomposition, Agent Routing, Tool Execution, Session Completion/Handoff, Team Collaboration, Run Contract guidance
- Stable facts: `afk_candidate`, `bounded-afk`, and `can run in parallel` mean different things and do not approve autonomous execution.
- Assumptions: existing advisory checks can warn on weak delegation metadata without becoming hard enforcement.
- Privacy or secrets redactions: delegated work must preserve existing sensitive/external/destructive approval gates.

## Alignment / Grilling Summary

- Alignment method: maintainer roadmap planning
- Shared design concept: clarify AFK/delegation suitability and re-entry evidence without creating a delegation runtime or approval path.
- Key decisions reached: no new command, dashboard, registry, optional pack, autonomous lane, or hard validator block in v1.
- Remaining implementation-changing questions: none for the approved v1 slice.

## Domain Language

| Term | Status | Plain-English meaning | Aliases | Avoid/confusing terms | UI/code/test examples | Source pointer |
|---|---|---|---|---|---|---|
| `afk_candidate` | reused | Metadata saying a scoped bead may be suitable for agent handoff after context and bounds are loaded. | AFK-suitable | autonomous approval | bead metadata | This PRD |
| `bounded-afk` | reused | Stronger autonomy level requiring explicit allowed actions, proof, stop conditions, approval gates, and re-entry evidence. | bounded AFK | permission to continue indefinitely | Run Contract | This PRD |
| `can run in parallel` | reused | Small-team dependency term for branch/worktree-isolated teammate work after coordinator approval. | parallel work | multiple active beads in one checkout | Team Collaboration | This PRD |

## PRFAQ-Lite

- Press-release claim: PrecodeOS can support scoped delegated work while preserving human review and proof.
- Customer problem: AFK and delegation terms can be mistaken for autonomous execution permission.
- Customer FAQ: Does `bounded-afk` approve risky actions? No; existing approval gates still apply.
- Internal FAQ: Does this add a delegation runtime? No.
- Appetite: protocol, prompt, advisory-check, and re-entry evidence clarity.
- Kill or pause criteria: stop if metadata becomes command approval, autonomous execution approval, parallel activation, or merge/transition approval.

## Summary

PrecodeOS should let a builder step away from a scoped agent task without turning AFK metadata into autonomous execution permission.

This slice clarifies the difference between `afk_candidate`, `bounded-afk`, and small-team parallel work. It strengthens existing advisory checks, prompt language, handoff guidance, and re-entry evidence. It does not add a new command, dashboard, registry, delegation runtime, optional pack, or approval path.

## Problem

Unattended or delegated agent work can drift in scope, proof, or ownership. Existing PrecodeOS surfaces already name `afk_candidate`, `bounded-afk`, Run Contracts, Context Packs, and small-team re-entry review, but the safety expectations are spread across protocols and can be mistaken for permission to let agents continue autonomously.

The package needs clearer criteria before work is delegated and clearer evidence when the builder or coordinator returns.

## Goals

- Clarify that `afk_candidate` means a scoped bead may be safe to hand to an agent after context is loaded.
- Clarify that `bounded-afk` needs tighter advisory Run Contract review before delegation.
- Make solo AFK re-entry and small-team branch/worktree re-entry visibly distinct.
- Strengthen existing advisory checks for missing files-in-play bounds, checks, stop conditions, test strategy, review context, proof, approval gates, and re-entry evidence.
- Preserve human review, recorded proof, and existing approval gates.

## Non-Goals

- No new delegation safety command, dashboard, generated report, registry, command wrapper, optional pack, install/update behavior, package-manager behavior, or autonomous execution lane.
- No automatic activation of parallel work, subagents, branches, worktrees, review acceptance, merge, transition approval, external mutation, or task selection.
- No hard validator block for AFK metadata in v1; warnings remain advisory and require human judgment.
- No change to the one-active-bead rule in a checkout.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-035-FR01` | Decomposition guidance must define the criteria for marking a bead `afk_candidate` and when `bounded-afk` is the stronger autonomy level. | P0 | Primary planning surface. |
| `PRD-035-FR02` | Agent routing and tool-execution guidance must state that delegated work returns evidence to the parent/user and does not approve commands or widen scope. | P0 | Delegation boundary. |
| `PRD-035-FR03` | Session completion and small-team guidance must name re-entry evidence for solo AFK return and branch/worktree teammate return. | P0 | Return path. |
| `PRD-035-FR04` | User-facing docs and prompts must provide copyable AFK-safety and re-entry prompts without implying autonomous execution approval. | P1 | Beginner clarity. |
| `PRD-035-FR05` | Existing advisory checks must warn on weak AFK/delegation metadata: broad files, missing checks, missing stop conditions, missing `test_strategy`, missing `review_context`, missing proof, or missing approval gate. | P1 | No new command. |
| `PRD-035-FR06` | Package inventory and AI-readable navigation must describe affected surfaces only where ownership or navigation changes. | P1 | Reference follow-through. |
| `PRD-035-FR07` | Clarity scenario coverage must protect solo AFK, bounded-AFK Run Contract warnings, small-team re-entry, and the boundary that AFK metadata is not approval. | P1 | Regression coverage. |
| `PRD-035-FR08` | Maintainer changelog, roadmap, roadmap journal, docs HTML, PRD HTML, and roadmap HTML must be updated. | P1 | Maintainer follow-through. |

## Acceptance Oracle Matrix

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-035-FR01` | Decomposition Protocol distinguishes `afk_candidate`, `bounded-afk`, and `can run in parallel` without changing activation rules. | Source review. |
| `PRD-035-FR02` | Agent Routing and Tool Execution preserve Run Contract advisory boundaries and return-to-parent evidence language. | Source review. |
| `PRD-035-FR03` | Completion/Handoff and Team Collaboration name re-entry evidence and keep generated previews non-authoritative. | Source review. |
| `PRD-035-FR04` | Daily Cockpit, User Guide, How-To, and Prompt Patterns include AFK/re-entry prompts and no-autonomy warnings. | Source review and generated docs HTML. |
| `PRD-035-FR05` / `PRD-035-FR07` | Existing advisory check fixtures cover AFK metadata and bounded-AFK warning behavior. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-035-FR06` | Package inventory and `llms.txt` reflect ownership/navigation changes without overexposing AFK as a new workflow. | Source review. |
| `PRD-035-FR08` | Roadmap, journal, changelog, generated PRD/docs/roadmap surfaces are fresh. | Validation commands. |

## Required Validation

```bash
python3 scripts/clarity-scenario-check.py
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/prd-html.py
python3 scripts/prd-html.py --check
python3 _maintainer/scripts/docs-html.py
python3 _maintainer/scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py
python3 _maintainer/scripts/roadmap-html.py --check
python3 _maintainer/scripts/roadmap-maintenance.py
git diff --check
```

## Risk And Permission Model

`afk_candidate` is delegation suitability metadata only. It says a scoped bead may be safe for an agent after context is loaded, files in play are bounded, checks and stop conditions are explicit, and human review remains required.

`bounded-afk` is the stronger autonomy level for work that may continue while the builder is away. It should name allowed actions, proof needed, approval required before risky actions, stop conditions, rollback or blocked escape, and re-entry evidence through the existing Run Contract path.

`can run in parallel` is a small-team dependency term. It means branch/worktree-isolated teammate work after coordinator approval, not multiple active beads in one checkout and not merge approval.

## Architecture / Project Context Impact

- `PROJECT-CONTEXT.md` impact: none.
- Architecture impact: no runtime, delegation subsystem, dashboard, or registry.
- Data model impact: advisory metadata and generated evidence only.
- Security/privacy impact: sensitive, external, and destructive work still requires explicit approval gates.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| AFK/delegation guidance | Decomposition, Agent Routing, Tool Execution, Completion/Handoff, Team Collaboration | Clarifies suitability, allowed actions, stop conditions, and re-entry evidence without approving autonomy. | clarity scenario and source review | This PRD |
| Existing advisory checks | current checker surfaces | Warn on weak AFK/delegation metadata without hard enforcement. | fixture coverage | This PRD |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-035-afk-delegation-safety-improvements.md`
- Owner surfaces likely in play: Decomposition, Agent Routing, Tool Execution, Session Completion/Handoff, Team Collaboration, Daily Cockpit, User Guide, How-To, Prompt Patterns, package inventory, AI navigation, and clarity scenario coverage.
- Forbidden assumptions: do not approve autonomous execution, risky commands, parallel work activation, merge, transition, external mutation, or task selection from AFK metadata.

## Anti-Shallow Checks

- Does `afk_candidate` remain suitability metadata only?
- Does `bounded-afk` name allowed actions, proof needed, approval gates, stop conditions, blocked escape, and re-entry evidence?
- Does small-team parallelism remain branch/worktree-isolated coordinator-approved work, not multiple active beads in one checkout?

## Bead Proposals

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B035-afk-delegation-safety-improvements` | `PRD-035-FR01` through `PRD-035-FR08` | Protocols, prompts, docs, advisory checks, inventory/navigation, clarity coverage, generated surfaces, and maintainer history preserve AFK/delegation boundaries. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | This PRD | clarity and package checks |

## Compilation Notes

- Feature entry: AFK / Delegation Safety Improvements
- Functional requirements to compile: `PRD-035-FR01` through `PRD-035-FR08`
- Acceptance updates needed: AFK metadata remains advisory and non-approval.

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should future Run Contract output expose richer AFK readiness summaries? | Follow-up scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-29
- Approval notes: Approved as AFK/delegation safety guidance and advisory warning coverage, not autonomous execution approval, command approval, parallel activation, merge approval, transition approval, or runtime behavior.
