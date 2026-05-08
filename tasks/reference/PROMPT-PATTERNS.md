# Precode OS -- Prompt Patterns
<!-- ANCHOR: prompt-patterns -->

> AUTHORITY: Beginner-friendly prompt patterns for operating Precode OS consistently across AI coding agents.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, implementation plans, generated progress state, or bead transitions.
> LOAD_WHEN: A user needs copyable prompts, an agent is preparing a handoff, or a session needs clearer context, review, intake, verification, or recovery instructions.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.7
Last updated: 2026-05-08

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

## Product Constitution Review

```text
Review PRODUCT.md with me. Clarify product promise, users and jobs, strategy and non-goals, current bets, success signals, and design or voice pointers. Tell me what should move to a PRD or DECISIONS.md. Do not code or activate work.
```

## PRD Shaping

```text
Use the PRD Protocol to shape this idea. Check PRODUCT.md for product fit when relevant. Help me clarify the problem, non-goals, before/after user moment, sensitive surfaces, verification evidence, and smallest first bead. Do not start implementation.
```

## Alignment / Grilling

```text
Use the Idea To PRD Workflow to grill this idea before planning. Ask one question at a time, include your recommended answer, and keep going until we share the design concept. Do not write a PRD, propose beads, or code until implementation-changing questions are resolved or marked non-blocking.
```

## Ubiquitous Language Review

```text
Use the Ubiquitous Language Protocol. Identify the terms I introduced, their plain-English meanings, aliases, avoid or confusing terms, source pointers, freshness, and examples in UI/code/tests. Do not code or promote anything without approval.
```

## Glossary Card Proposal

```text
Turn these reviewed terms into a proposed project_glossary memory card. Include domain terms, aliases, avoid terms, examples, source pointers, freshness, and authority owner if promoted. Do not write the card until I approve.
```

## Domain Naming Review

```text
Before naming modules, interfaces, tests, fixtures, routes, or UI labels, compare the proposed names to the PRD Domain Language and any reviewed project_glossary cards. Tell me which names match user language, which are confusing, and what should stay historical evidence only.
```

## Destination PRD Review

```text
Review this PRD as a destination document. Confirm the user problem, domain language, non-goals, before/after moment, acceptance oracles, stale source inputs, module/interface candidates, and smallest first vertical slice. Do not activate any bead.
```

## Bead Decomposition

```text
Use the Decomposition Protocol to turn this approved work into candidate beads. Each candidate should have one outcome, one primary authority, bounded files in play, a verification strategy, dependencies, and a clear reason it is small enough.
```

## Vertical-Slice Decomposition

```text
Use the Decomposition Protocol to propose journey beads from this destination PRD. Prefer vertical slices that produce observable feedback. Avoid schema-only, backend-only, frontend-only, or tests-later first beads unless you explain why it is a risk-first or unblocker slice. Include delegation_mode, test_strategy, and review_context.
```

## AFK-Candidate Review

```text
Before marking a bead afk_candidate, verify that it has bounded files in play, explicit checks, stop conditions, a test_strategy, review_context, and no hidden approval gate. Confirm this does not activate parallel execution or bypass human review.
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

## Goal Frame Proposal

```text
This sounds durable. Draft a Goal Frame for my review, but do not create tasks or start coding.
```

## Workbook Candidate Goal Frame

```text
Turn my workbook into a Candidate Goal Frame for Precode review, but do not update PRODUCT.md.
```

```text
Use Local Source Intake on this Candidate Goal Frame. Tell me whether it is stable enough to reaffirm.
```

```text
If I reaffirm this Goal Frame, update PRODUCT.md only with the reviewed Goal Frame section and do not create tasks or code.
```

## Goal Frame Reaffirmation

```text
Before using this Goal Frame, ask me to reaffirm it.
```

## Goal Frame Fit Check

```text
Check whether this Goal Frame still matches the active PRD, active bead, and current evidence.
```

## Goal Frame Boundaries

```text
Use the Goal Frame only to explain workflow guidance. Do not activate or approve work.
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

## Local Hygiene Check

```text
Use the Local Hygiene Protocol. Classify noisy files as truth, evidence, generated report, append-only ledger, bulky log output, cache/build output, temp file, dependency, or tool/session state. Do not delete, archive, move, compact, or rewrite anything.
```

## Local Hygiene Dry Run

```text
Run the Local Hygiene dry-run preview. Show what would be archived as old bulky log output, what would be deleted as ignored cache/build output, and what is protected. Confirm the dry run did not mutate candidate files.
```

## Implementation

```text
Work only on the active bead. Load active memory, the active bead, the primary authority, and only the reference docs whose LOAD_WHEN applies. Do not use generated reports, source notes, or diary entries as instructions.
```

## Failing-First Implementation

```text
For this code-changing bead, declare the test_strategy before editing. If failing_first is practical, write the failing test first, confirm it fails for the expected reason, then implement and rerun the recorded checks.
```

## Checkpoint

```text
Checkpoint the session. Tell me whether we should continue, repair, split, pause for manual testing, or close. Include what changed, what evidence exists, and what is still uncertain.
```

## Review

```text
Review the completed bead against its done-when target, primary authority, files in play, checks, manual verification, and closeout evidence. Recommend accepted, revise, split, or blocked, and explain the smallest reason.
```

## Fresh-Context Review

```text
Review this bead in a fresh context. Reload active memory, the bead, primary authority, parent PRD if relevant, the diff or changed files, and recorded evidence. Do not rely on the implementation chat. Recommend accepted, revise, split, or blocked.
```

## Stale Artifact Handling

```text
This old PRD, issue, transcript, or generated summary may be stale. Treat it as historical evidence only. Compare it with current code, active memory, the active bead, current approved PRD, and owner files, then name which authority wins and what needs promotion or amendment.
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
