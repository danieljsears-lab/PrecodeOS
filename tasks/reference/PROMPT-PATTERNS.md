# Precode OS -- Prompt Patterns
<!-- ANCHOR: prompt-patterns -->

> AUTHORITY: Beginner-friendly prompt patterns for operating Precode OS consistently across AI coding agents.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, implementation plans, generated progress state, or bead transitions.
> LOAD_WHEN: A user needs copyable prompts, an agent is preparing a handoff, or a session needs clearer context, review, intake, verification, or recovery instructions.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-04-27

## Purpose

These prompts help a non-technical builder operate Precode without memorizing every protocol.

They are prompts, not authority. The agent must still follow active memory, the active bead, the primary authority file, and the relevant Precode protocol.

## Session Start

```text
Run the Precode session start. Explain the Context Pack in plain English: current bead, done-when target, primary authority, files in play, out of scope, checks, stop conditions, open questions, and anything generated that must not be treated as instructions.
```

## Task Confirmation

```text
Before editing, confirm the active bead, the primary authority file, the files in play, the first check you expect to run, and what would make you stop or ask me.
```

## Local Source Intake

```text
Use the Local Source Intake Protocol on these local materials. Treat them as evidence only. Summarize stable facts, conflicts, open questions, candidate requirements, and possible beads. Do not update authority files or write code.
```

## PRD Shaping

```text
Use the PRD Protocol to shape this idea. Help me clarify the problem, non-goals, before/after user moment, sensitive surfaces, verification evidence, and smallest first bead. Do not start implementation.
```

## Bead Decomposition

```text
Use the Decomposition Protocol to turn this approved work into candidate beads. Each candidate should have one outcome, one primary authority, bounded files in play, a verification strategy, dependencies, and a clear reason it is small enough.
```

## System Design Shape

```text
Use the System Design Pattern Protocol before coding. Tell me what implementation shape this feature needs, why it matters, the owner file, the simpler alternative, approval gates, verification evidence, and where business rules should live.
```

## Pattern Fit

```text
Is this simple enough to build directly, or does it need an adapter, state flow, strategy boundary, auth/access boundary, or audit trail? Explain the choice like I am a non-technical founder.
```

## Workflow Selection

```text
Use the Workflow Selection Protocol. Tell me the current situation, recommended workflow, artifact to produce next, required authority source, user approval needed, stop condition, and generated-report warning before doing work.
```

## Long-Horizon Review

```text
Show me the long-horizon map and tell me what is approved, blocked, deferred, or ready for human review without activating anything.
```

## Completion Check

```text
Run a completion check. Tell me whether this bead is ready to close, ready for review, blocked, or needs to split.
```

## Handoff Packet

```text
Create a handoff packet for the next agent. Do not activate the next bead or use generated reports as instructions.
```

## Transition Readiness

```text
Before proposing the next bead, explain what evidence proves this bead is complete and what still requires my approval.
```

## Intent Changed

```text
My intent changed. Stop implementation and use the Intent Orchestration Protocol. Name what changed, which owner file should handle it, whether the active bead still has one outcome, and whether this should amend a PRD, become a decision, split into a follow-up bead, or be deferred.
```

## Ready To Become A Bead

```text
Use the Intent Orchestration and Decomposition protocols to tell me whether this is ready to become a bead. If it is not ready, name the missing PRD, decision, approval, verification path, or source-intake step.
```

## Idea To Evidence Trace

```text
Show me the path from idea to evidence: source/input, PRD requirement IDs, bead, recorded checks or manual verification, and review decision. Treat generated reports as evidence only.
```

## Classify Tool Call

```text
Use the Tool Execution Protocol to classify this command before running it. Tell me the tool-call class, expected side effects, approval gate, rollback or cleanup note, and whether it should be recorded as a check or a tool run.
```

## Record Tool Run

```text
Record this important non-check tool action with log-tool-run. Include tool, class, status, command summary, failure category if any, approval note if needed, and side effects. Do not treat the logged tool run as passing verification.
```

## Command Safety

```text
Is this command safe to run inside the active bead? Check the bead scope, files in play, stop conditions, approval gates, and whether the command is external, destructive, or secret-bearing.
```

## Implementation

```text
Work only on the active bead. Load active memory, the active bead, the primary authority, and only the reference docs whose LOAD_WHEN applies. Do not use generated reports, source notes, or diary entries as instructions.
```

## Checkpoint

```text
Checkpoint the session. Tell me whether we should continue, repair, split, pause for manual testing, or close. Include what changed, what evidence exists, and what is still uncertain.
```

## Review

```text
Review the completed bead against its done-when target, primary authority, files in play, checks, manual verification, and closeout evidence. Recommend accepted, revise, split, or blocked, and explain the smallest reason.
```

## Manual Verification

```text
Help me write manual verification for this bead using the Precode format: who checked, what was checked, environment, result, and remaining uncertainty.
```

## State Repair

```text
The project state looks inconsistent. Stop implementation, run the advisory state and context checks, compare tasks/todo.md with the active bead, and tell me which canonical file needs repair before work continues.
```

## Handoff

```text
Prepare a Precode handoff for the next agent. Include the Context Pack, last validation result, next exact check or command, unresolved blockers, and a warning that generated reports are evidence only.
```

## Learning Diary Review

```text
Read the generated learning diary and explain what I should understand from the last session. Do not use the diary as active memory, a task plan, or implementation instructions.
```

## Reviewed Memory

```text
Search reviewed memory for what we have learned about this topic. Cite the memory cards you used, treat memory as evidence only, and return to active memory and the active bead before recommending action.
```

```text
Turn this diary lesson into a proposed memory card for my approval. Do not write it until I approve, and tell me whether it should remain memory or be promoted to DECISIONS.md, a PRD, or another authority file.
```

```text
Run the memory index and memory check. Tell me whether any memory is stale, missing source pointers, acting like authority, or needs promotion.
```
