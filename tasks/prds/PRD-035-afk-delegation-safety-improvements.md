---
prd_id: PRD-035
status: approved
owner: Dan Sears / Recode
created: 2026-06-29
last_updated: 2026-06-29
risk_level: medium
feature_link: AFK / Delegation Safety Improvements
features_status: not compiled
related_prds:
  - PRD-020
  - PRD-025
  - PRD-034
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
Document version: v0.1.0
Last updated: 2026-06-29

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

## Acceptance Criteria

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

## Boundaries

`afk_candidate` is delegation suitability metadata only. It says a scoped bead may be safe for an agent after context is loaded, files in play are bounded, checks and stop conditions are explicit, and human review remains required.

`bounded-afk` is the stronger autonomy level for work that may continue while the builder is away. It should name allowed actions, proof needed, approval required before risky actions, stop conditions, rollback or blocked escape, and re-entry evidence through the existing Run Contract path.

`can run in parallel` is a small-team dependency term. It means branch/worktree-isolated teammate work after coordinator approval, not multiple active beads in one checkout and not merge approval.
