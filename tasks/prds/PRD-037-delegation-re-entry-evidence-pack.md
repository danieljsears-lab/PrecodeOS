---
prd_id: PRD-037
status: approved
owner: Dan Sears / Recode
created: 2026-07-04
last_updated: 2026-07-04
risk_level: medium
feature_link: Delegation Re-Entry Evidence Pack
features_status: not compiled
related_prds:
  - PRD-025
  - PRD-035
---

# PRD-037 -- Delegation Re-Entry Evidence Pack
<!-- ANCHOR: prd-037-delegation-re-entry-evidence-pack -->

> AUTHORITY: Public requirements for evidence-only re-entry after solo AFK, branch/worktree teammate, or cloud-agent delegated work returns to PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, command approval, autonomous execution approval, branch creation, pull request mutation, review acceptance, merge approval, transition approval, generated proof, command-wrapper behavior, registry behavior, optional-pack behavior, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating delegated-work return evidence, re-entry review, team merge/re-entry review, or cloud-agent/PR return guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-04

## Summary

PrecodeOS needs a compact return packet for delegated work so a builder or coordinator can safely re-enter after an agent, teammate branch/worktree, or cloud-agent/PR has produced changes.

This is a PRD-035 follow-up. PRD-035 defines bounded AFK and delegation suitability; PRD-037 defines the evidence that must come back before anyone continues, reviews, merges, transitions, or accepts work. The implementation extends existing handoff, team collaboration, tool-execution, prompt, and advisory-check surfaces. It does not add a new generated report or delegation runtime.

## Problem

Delegation risk is concentrated at re-entry. A returning agent or external tool may provide summaries, branch status, PR checks, review comments, generated logs, or changed files that sound authoritative. Those materials can be useful evidence, but they do not prove scope control, acceptance, merge readiness, or approval.

Without a shared evidence shape, users can either trust a finished-sounding handback too quickly or spend too much time rediscovering what changed.

## Goals

- Define common delegated-work return fields for solo AFK, branch/worktree teammate, and cloud-agent/PR returns.
- Keep generated reports, tool logs, PR status, review comments, and agent summaries as evidence only.
- Preserve explicit human approval before continuing risky work, accepting implementation, approving merge, external mutation, or transition.
- Extend existing advisory outputs and prompts instead of adding a new command, report, runtime, or registry.

## Non-Goals

- No managed agents, scheduler behavior, API orchestration, automatic branch creation, automatic PR creation, PR mutation, merge approval, review acceptance, transition approval, external mutation approval, or autonomous execution lane.
- No new generated re-entry packet command or dedicated report surface.
- No provider-specific compatibility claim. Cloud-agent guidance remains provider-neutral; optional GitHub evidence is read-only evidence when available.
- No change to the one-active-bead rule in a checkout.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-037-FR01` | Session Completion/Handoff must name delegated re-entry evidence fields for solo AFK or bounded-AFK return. | P0 | Scope returned, changed files, checks, manual verification, stop conditions, approval still required, unresolved risks, and next human action. |
| `PRD-037-FR02` | Team Collaboration must expand merge/re-entry review fields for branch/worktree teammate and delegated-agent return. | P0 | Includes owner-file impacts, integration conflicts, stale branch/evidence signals, external status evidence, forbidden actions not taken, and coordinator decision needed. |
| `PRD-037-FR03` | Cloud-agent/PR return guidance must remain provider-neutral while allowing optional read-only GitHub branch, PR, review, check, and workflow status as evidence. | P0 | GitHub evidence is optional and never approval. |
| `PRD-037-FR04` | Tool Execution must clarify that tool logs, PR status, review comments, checks, workflows, and agent summaries are evidence only. | P0 | They do not approve commands, accept implementation, approve merge, or mutate external systems. |
| `PRD-037-FR05` | Existing advisory JSON outputs must expose a `delegation_reentry` field group where completion or team preview evidence is already emitted. | P1 | No new command or generated report. |
| `PRD-037-FR06` | Prompt Patterns and user-facing docs must include copyable solo, team, and cloud-agent re-entry prompts. | P1 | Beginner-visible only where re-entry is already discussed. |
| `PRD-037-FR07` | Public inventory, AI navigation, generated PRD/docs surfaces, maintainer changelog, roadmap, and roadmap journal must be updated. | P1 | Maintainer follow-through for public package changes. |
| `PRD-037-FR08` | Deterministic checks must protect the advisory-only boundary and required field names. | P1 | Clarity scenario and existing self-test coverage. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-037-FR01` | Completion/Handoff names the delegated re-entry fields and next actions: continue, review, split, block, or handoff. | Source review and `completion-check.py` output shape. |
| `PRD-037-FR02` | Team Collaboration names the branch/worktree delegated-return fields and coordinator review boundary. | Source review and `team-collaboration-check.py --self-test`. |
| `PRD-037-FR03` | Optional GitHub evidence is described as read-only external evidence and no provider-specific compatibility claim is made. | Source review. |
| `PRD-037-FR04` | Tool Execution demotes tool logs, PR status, reviews, checks, workflows, and agent summaries to evidence only. | Source review. |
| `PRD-037-FR05` | Existing JSON payloads include `delegation_reentry` without introducing a new report command. | Script output inspection and self-test coverage. |
| `PRD-037-FR06` | Prompt Patterns, Daily Cockpit, User Guide, and How-To include re-entry prompts without approval language drift. | Source review and generated docs HTML. |
| `PRD-037-FR07` | Package inventory, `llms.txt`, maintainer changelog, roadmap, journal, and generated surfaces are fresh. | Validation commands. |
| `PRD-037-FR08` | Clarity scenarios and team self-test cover required fields and forbidden uses. | `python3 scripts/clarity-scenario-check.py`; `python3 scripts/team-collaboration-check.py --self-test`. |

## Required Validation

```bash
python3 scripts/clarity-scenario-check.py
python3 scripts/team-collaboration-check.py --self-test
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

Delegation re-entry evidence is a checklist shape inside existing handoff, team, and tool-execution surfaces. It is not a new artifact authority.

The next safe action may be `continue`, `review`, `split`, `block`, or `handoff`. Any action that accepts implementation, approves merge, approves transition, mutates GitHub or another external system, deploys, releases, changes scope, or bypasses a human approval gate still requires the existing Precode approval path.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B002-delegation-re-entry-evidence-pack` | `PRD-037-FR01` through `PRD-037-FR08` | PRD shard, protocol guidance, prompt guidance, script payload fields, docs/inventory/navigation, clarity coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-037-delegation-re-entry-evidence-pack.md` | clarity scenario, team self-test, package/docs/PRD/roadmap checks |
