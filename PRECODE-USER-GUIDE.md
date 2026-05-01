# How To Use Precode OS
<!-- ANCHOR: precode-user-guide -->

> AUTHORITY: Canonical hands-on user playbook for operating Precode OS as a non-technical builder.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, route structure, schema definitions, implementation plans, generated progress state, or deep architecture guidance.
> LOAD_WHEN: Onboarding a new user, running a Precode session, deciding what to ask an AI coding agent, or checking whether work is ready to accept.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.6.5
Last updated: 2026-04-28



## What This Guide Helps You Do

Use this guide while you work. It tells you what to ask the agent, what good output looks like, when to stop, and what you must approve.

Precode lives inside your project folder. It keeps important project truth in readable Markdown files and uses small scripts to check whether the agent is staying aligned.

For the bigger "what and why," read `PRECODE-OS-README.md`. For Precode's philosophical anchor, read `PRECODE-MANIFESTO.md`. For the beginner bridge from idea to software-building workflow, read `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`. For deep architecture and maintainer detail, read `PRECODE-ARCHITECTURE-OVERVIEW.md`. For the full prompt catalog, read `tasks/reference/PROMPT-PATTERNS.md`.

Why this matters: This guide is the operating manual. Keep it practical: follow the steps, copy the prompts, and stop when the guide says stop.

## Before You Start

Do this before letting an agent edit files:

- Open the repo or project folder that contains Precode OS.
- Confirm the agent is using Precode instructions.
- Ask the agent to load active memory only: `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
- Ask the agent to identify the active bead and primary authority file.
- Do not approve broad changes, sensitive work, dependency changes, production actions, or the next bead yet.

Say this:

```text
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md, and tasks/todo.md. Then tell me the active bead, primary authority, files in play, checks, stop conditions, and anything blocked. Do not start coding yet.
```

Expect this:

- active bead path
- done-when target
- files in play
- checks to run
- stop conditions
- blockers or open questions

Stop if: the agent cannot explain the current bead in plain English.

## Do Not Move, Rename, Or Directly Edit Precode Files

Precode works because specific Markdown files have specific names, locations, headings, anchors, and metadata. Moving, renaming, or casually editing those files can break how agents and scripts find the right memory, task, or authority file.

Hard rules:

- Do not move Markdown files.
- Do not rename Markdown files.
- Do not directly edit Markdown files until the agent has identified which file owns the fact and what structure must be preserved.
- Do not edit generated Markdown reports such as `OS-HEALTH.md`, `PROGRESS.md`, `logs/learning-diary.md`, `logs/memory-index.md`, `logs/handoff-packet.md`, or `logs/scheduled-audit.md`.
- Do not change frontmatter, anchors, authority contracts, headings, bead state, or Closeout Evidence fields casually.
- Do not add a new active-memory file.
- Do not put backlog, roadmap, someday, or future-work lists into `tasks/todo.md`.
- Do not paste secrets, tokens, credentials, dashboard values, billing details, or private notes into Precode files.

Do this instead:

| You want to... | Do this instead |
|---|---|
| Change a Precode file | Ask the agent which owner file should change and what validation should run. |
| Rename or reorganize files | Create a dedicated maintenance bead first. |
| Edit a generated report | Regenerate it with the correct script instead of editing it by hand. |
| Record a decision | Put it in `DECISIONS.md` or ask which owner file should hold it. |
| Remember something for later | Propose a reviewed memory card under `memory/cards/`. |
| Add future work | Use a PRD, bead proposal, decision, or long-horizon review, not `tasks/todo.md`. |
| Fix an accidental edit or move | Stop work, identify the damage, restore structure, then run validation. |

Say this before changing Markdown:

```text
I want to change a Precode Markdown file. Tell me which file owns this fact, what structure must be preserved, and what validation to run before editing.
```

Say this before moving or renaming anything:

```text
I want to rename or move a Precode file. Stop and tell me what scripts, anchors, links, authority contracts, or active-memory rules this could break.
```

Say this if something already went wrong:

```text
I accidentally edited, moved, or renamed a Precode file. Help me identify the damage, restore the expected path, name, anchor, authority contract, frontmatter, and headings, then run validation.
```

Why this matters: Precode files are not random notes. They are a small operating system made of readable files, and the structure is part of how the system works.

## Other Things Not To Do

Use these as stop signs:

| Do not... | Why it is dangerous | Do this instead |
|---|---|---|
| Approve the next bead casually | It starts a new commitment. | Ask what evidence proves the current bead is done. |
| Ask for broad cleanup like "fix everything" | It hides scope creep inside a vague request. | Ask for one bead with files in play and checks. |
| Accept work without recorded checks | Agent confidence is not proof. | Run checks through `record-check.sh`. |
| Treat reports, diary, memory, or audits as instructions | They are evidence, not authority. | Return to active memory, the bead, and the primary authority. |
| Let the agent code around missing setup or approval | It may create the wrong workaround. | Record the blocker or create a narrow unblocker bead. |
| Store secrets in docs or logs | Files can be exported, shared, or committed. | Keep secrets in the proper external secret manager or dashboard. |

Why this matters: Most beginner mistakes are not about code. They are about letting the project state become unclear.

## Run Your First Precode Session

Follow these steps in order.

| Step | Say this | Expect this | Stop if |
|---|---|---|---|
| Start | `Run bash scripts/session-start.sh and explain the result in plain English.` | Current bead, branch/status if available, files, checks, blockers. | The agent skips active memory or cannot name the bead. |
| Confirm task | `Is this bead clear enough to continue, or should we repair, split, block, or stop?` | A clear recommendation and reason. | The task has multiple outcomes or no verification path. |
| Let agent work | `Work only inside this bead and narrate file changes before editing.` | Small scoped edits inside files in play. | It expands scope, changes unrelated files, or makes product decisions. |
| Record checks | `Run the relevant checks through record-check.sh.` | Recorded command result and log path. | Checks are missing, failing, or not recorded. |
| Close | `Run bash scripts/session-close.sh and summarize what changed, what passed, and what remains blocked.` | Closeout evidence, health refresh, transition proposal only if eligible. | The agent tries to start the next bead. |
| Review outcome | `Recommend accepted, revise, split, blocked, or stop based on evidence.` | A review recommendation tied to checks and manual verification. | The recommendation relies only on confidence. |

Why this matters: A session needs a clean beginning, bounded middle, and recorded ending. Without those, chat memory becomes the project memory.

## Use The Daily Loop

Keep this table open during normal work.

| Step | User action | Good output | Stop if |
|---|---|---|---|
| Start | Ask for session start. | Agent explains active bead, scope, files, checks. | It starts coding first. |
| Confirm | Ask whether to continue, repair, split, block, or stop. | One clear path. | Scope is vague or too broad. |
| Work | Let the agent edit only scoped files. | Small changes tied to the bead. | It touches unrelated files. |
| Check | Ask for recorded checks. | `record-check.sh` output and evidence path. | It says done without evidence. |
| Checkpoint | Pause when confused or scope grows. | Restated task, changed files, next check. | It resists narrowing. |
| Close | Ask for session close. | Closeout evidence and review state. | It starts the next bead. |
| Approve | Approve only after review. | Accepted, revise, split, blocked, or transition. | Manual verification is unclear. |

Why this matters: The daily loop is not ceremony. It is how you keep the agent from turning one request into a moving target.

## Choose What To Ask For

Use this table when you are unsure what kind of request to make.

| Situation | Ask for | Copyable request |
|---|---|---|
| Rough idea, notes, screenshot, GitHub issue, research | Local source intake | `Use Local Source Intake. Summarize facts, assumptions, conflicts, open questions, candidate requirements, and possible beads. Do not code.` |
| Feature idea is fuzzy | Idea-to-PRD | `Use the Idea To PRD Workflow. Clarify the user problem, non-goals, before/after moment, risks, and smallest valuable version. Do not code.` |
| Approved PRD exists | Bead decomposition | `Use the Decomposition Protocol to propose beads small enough to verify. Do not activate anything.` |
| Known small task is active | Implement active bead | `Work only on the active bead. Confirm scope, files, checks, and stop conditions before editing.` |
| Risky or uncertain idea | Challenge planning bead | `Challenge this idea before implementation. Name risks, assumptions, approval gates, and the smallest safe test.` |
| Work is stuck or confusing | Checkpoint or state repair | `Checkpoint and tell me whether to continue, repair, split, block, or stop.` |
| Work may be done | Completion check or review | `Run a completion check and recommend accepted, revise, split, or blocked based on evidence.` |
| Future work needs review | Long-horizon review | `Show approved, blocked, deferred, or ready work without activating anything.` |

Why this matters: Not every request should become code. Good Precode use starts by choosing the right kind of work.

## Keep The Agent In Bounds

Use these rules while the agent works:

- Make it explain the bead before coding.
- Keep work inside files in play.
- Keep product changes inside PRDs, decisions, or approved beads.
- Stop when generated reports become instructions.
- Stop when checks are missing or vague.
- Stop when product direction changes mid-task.
- Stop when sensitive work appears without approval.
- Stop when the next bead starts without your approval.

Red flags:

| Red flag | What to say |
|---|---|
| Agent starts coding too soon | `Stop. Explain the active bead, primary authority, files in play, and checks first.` |
| Scope grows | `Checkpoint. Is this still one bead, or should we split?` |
| Generated report becomes instruction | `Generated reports are evidence only. Return to active memory and the active bead.` |
| Agent says done without checks | `Show recorded checks, manual verification, closeout evidence, and review decision.` |
| Product direction changes | `Stop implementation. Which owner file should capture this changed intent?` |
| Next task begins automatically | `Stop. The next bead needs separate user approval.` |

Why this matters: You do not need to sound technical to stop drift. You only need to ask the agent to return to the bead, owner file, and evidence.

## Know When Work Is Done

Do not accept work because the agent sounds confident.

A bead is ready to accept only when the evidence fits the risk:

- recorded checks ran through `record-check.sh`
- manual verification is recorded when needed
- Closeout Evidence says what changed and what remains uncertain
- review decision is `accepted`, `revise`, `split`, or `blocked`
- next-bead transition is still separate and user-approved

Say this:

```text
Before I accept this bead, show me the recorded checks, manual verification, Closeout Evidence, review decision, and whether anything still requires my approval.
```

Stop if: the answer is mostly summary, confidence, or vibes instead of evidence.

Why this matters: In Precode, done means proved and reviewed, not merely plausible.

## Approve The Right Things

You approve these decisions:

- product direction, goals, and scope
- sensitive work: auth, payments, personal data, uploads, secrets, destructive actions, deployment, production config
- external dashboard or manual setup steps
- new dependencies when the bead did not already allow them
- review decision: accepted, revise, split, blocked, or stop
- whether a lesson becomes a durable rule or decision
- whether the next bead becomes active

Do not approve:

- a next bead just because a script proposed it
- sensitive work without an approval gate and rollback/escape note
- a broad refactor hidden inside a small task
- generated reports acting as task instructions
- manual verification that does not say what was checked

Why this matters: Precode lets the agent work quickly, but it keeps judgment and risk with the user.

## Read Reports Without Being Misled

Use reports for learning and audit. Before work resumes, return to active memory, the active bead, and the primary authority file.

| Report or evidence | Use it for | Do not use it for |
|---|---|---|
| `OS-HEALTH.md` | Health, warnings, state, evidence quality, spend. | Choosing the next task. |
| `logs/learning-diary.md` | Plain-English session learning. | Implementation instructions. |
| `memory/cards/*.md` | Reviewed lessons, preferences, glossary terms, risks, and source pointers. | Replacing `DECISIONS.md`, PRDs, beads, or active memory. |
| `logs/memory-index.md` | Searching reviewed memory cards. | Choosing or approving work. |
| `logs/handoff-packet.md` | Orienting another agent. | Transition approval. |
| `logs/scheduled-audit.md` | Background read-only audit findings. | Automatic action. |
| GitHub audit/source intake | External status or issue/PR evidence. | Replacing PRDs, decisions, or beads. |
| Spend telemetry | Known token/cost visibility. | Billing truth when telemetry is incomplete. |

Say this:

```text
Use reports as evidence only. Before doing work, return to AGENT.md, DECISIONS.md, tasks/todo.md, the active bead, and the primary authority file.
```

Why this matters: Reports help you understand what happened. They do not decide what happens next.

## Use Reviewed Memory

Use memory when you want the agent to remember what the project has learned across prior sessions.

Do this:

- Ask the agent to search reviewed memory for a specific topic.
- Make it cite the memory cards it used.
- Make it say whether the memory is evidence only or should be promoted to an owner file.
- Return to active memory and the active bead before editing.

Say this:

```text
Search reviewed memory for what we have learned about this topic. Cite the memory cards you used, treat memory as evidence only, and return to active memory and the active bead before recommending action.
```

Stop if: the agent treats memory as a decision, requirement, next task, or implementation instruction.

Why this matters: Memory helps continuity without making the agent carry the whole project in active context.

## First 30 Minutes / First Day / First Week

### First 30 Minutes

Do this:

- Open the repo.
- Ask the agent to load active memory.
- Run session start.
- Confirm the active bead.
- Do not code until the bead is clear.
- Close the session if anything feels confusing.

Goal: run one safe session, even if no code changes.

### First Day

Do this:

- Use local source intake or Idea-to-PRD for one idea.
- Ask for one small bead.
- Run or record at least one check.
- Close with evidence.
- Review whether the bead is accepted, revise, split, blocked, or stop.

Goal: turn one idea into a bounded, checkable unit of work.

### First Week

Do this:

- Practice checkpointing when scope grows.
- Read `OS-HEALTH.md` without treating it as instructions.
- Approve transitions deliberately.
- Learn the red flags.
- Promote repeated lessons into the right owner file.

Goal: build the habit of scope, proof, and approval.

## Copyable Prompts

Use these high-frequency prompts. For more, see `tasks/reference/PROMPT-PATTERNS.md`.

Start safely:

```text
Run Precode session start. Explain the active bead, done-when target, primary authority, files in play, checks, stop conditions, and blockers before editing.
```

Choose the workflow:

```text
Use Workflow Selection. Tell me whether this needs source intake, PRD shaping, bead decomposition, implementation, review, unblocker work, or state repair. Do not code yet.
```

Keep context clean:

```text
Confirm the Context Pack: active bead, primary authority, files in play, out of scope, checks, stop conditions, open questions, and generated reports that must not be treated as instructions.
```

Handle changed intent:

```text
My intent changed. Stop implementation. Name what changed, which owner file should handle it, and whether to amend a PRD, record a decision, split a follow-up bead, or defer it.
```

Check done:

```text
Run a completion check. Tell me whether this bead is ready to accept, revise, split, block, or stop, using recorded evidence.
```

Close safely:

```text
Run session close. Summarize what changed, what checks ran, what remains blocked, and what still requires my approval.
```

Search memory:

```text
Search reviewed memory for what we have learned about X. Do not treat memory as authority.
```

Propose a memory card:

```text
Turn this diary lesson into a proposed memory card for my approval. Do not write it until I approve.
```

Check promotion:

```text
Check whether this memory belongs in DECISIONS.md, a PRD, an authority doc, or should remain reviewed evidence.
```

## FAQ

### Getting Started

#### What does Precode help me avoid?

Scope creep, stale context, confident wrong code, vague done, skipped checks, skipped manual verification, and uncontrolled next-task momentum.

#### What habit should I build first?

Start every serious session with `bash scripts/session-start.sh`, then make the agent explain the bead before coding.

#### What if I do not understand a file?

Ask: `What does this file own, what is it not allowed to decide, and when should it be loaded?`

#### What if I want to move fast?

Use smaller beads, not fewer guardrails. Small checked work is usually faster than large vague work that needs cleanup.

### Active Memory And Context

#### Why only three active-memory files?

They keep the agent's starting point small and inspectable. More always-loaded files create more chances for stale context to override the current bead.

#### What is the difference between notes and authority?

Notes are evidence. Authority is an approved Precode file such as a PRD, `DECISIONS.md`, `ARCHITECTURE.md`, or the active bead.

#### What should I do if the agent seems confused?

Checkpoint. Ask it to restate the active bead, primary authority, files in play, next check, and stop conditions.

### Ideas, PRDs, And Beads

#### What is a bead?

A bead is one small unit of work with a contract: objective, owner file, files in play, checks, stop conditions, and closeout evidence.

#### When do I use a PRD?

Use a PRD when the feature needs product clarity before coding: problem, non-goals, user moment, requirements, risks, and acceptance checks.

#### What if I change direction mid-task?

Stop implementation. Decide whether the change belongs in a PRD amendment, `DECISIONS.md`, an authority file, a follow-up bead, or deferral.

### Evidence, Checks, And Done

#### What counts as evidence?

Recorded checks, closeout evidence, manual verification, external read-only status, or accepted review notes. Chat confidence is not evidence.

#### How does Precode stop false done?

It separates implementation from proof, review, and next-task approval.

#### When should I checkpoint?

Checkpoint when the task feels fuzzy, a session gets long, the agent changes several files, an approach fails twice, or scope starts expanding.

### Approvals, Blockers, And Reports

#### Why do I approve the next bead?

The next bead is a new commitment. Precode can propose it, but you decide whether to continue.

#### What if work is blocked by manual setup?

Record the missing input, dashboard step, manual test, or narrower unblocker bead. Do not let the agent code around the blocker.

#### Are token/cost numbers exact?

Only when reliable telemetry exists. Missing spend is unknown, not zero.

#### Does Precode replace judgment?

No. It makes state, scope, evidence, and approvals visible so your judgment is easier to apply.

---

## Change Log

| Version | Date | Summary |
|---|---|---|
| v0.6.5 | 2026-04-28 | Added beginner-facing positioning language explaining that Precode lives inside the project folder, keeps project truth in readable Markdown files, and uses small scripts to check agent alignment. |
| v0.6.4 | 2026-04-27 | Added navigation to `PRECODE-MANIFESTO.md` for Precode's philosophical anchor, values, principles, and anti-drift stance. |
| v0.6.3 | 2026-04-27 | Added navigation to the standalone software-building explainer for non-technical users learning how traditional software work maps to Precode OS and AI coding agents. |
| v0.6.2 | 2026-04-27 | Added beginner-safe hard rules for not moving, renaming, or directly editing Precode Markdown files; added do-this-instead recovery prompts and a prioritized human-safety table for common operator mistakes. |
| v0.6.1 | 2026-04-27 | Added prescriptive reviewed-memory guidance, report-reading rules for memory cards and generated memory indexes, and copyable prompts for searching memory, proposing memory cards, and checking whether memory should be promoted to an authority owner file. |
| v0.6.0 | 2026-04-27 | Refactored the guide into a prescriptive user playbook focused on how to run sessions, choose requests, keep agents bounded, verify done, approve safely, read reports, and follow a first-use progression with only enough what/why context to support action. |
| v0.5.5 | 2026-04-26 | Added beginner-facing system design pattern guidance for choosing direct changes, adapters, state flows, strategy boundaries, auth/access boundaries, and audit trails before coding. |
| v0.5.4 | 2026-04-26 | Added beginner-facing completion and handoff guidance explaining checkpoint, session close, closeout, review, handoff, and next-bead approval, plus prompts for completion checks, handoff packets, and transition readiness. |
| v0.5.3 | 2026-04-26 | Added beginner-facing long-horizon planning guidance explaining where future work belongs, how to read the generated long-horizon map, and how to review approved, blocked, deferred, or ready work without activating anything. |
| v0.5.2 | 2026-04-26 | Added beginner-facing workflow selection guidance, a "Which Workflow Should I Use?" table, a copyable workflow-selection prompt, and notes about workflow planning warnings in generated reports. |
| v0.5.1 | 2026-04-26 | Added beginner-facing tool execution guidance explaining the difference between tool runs, verification checks, and user-approved risky actions, plus prompts for classifying and recording tool calls. |
| v0.5.0 | 2026-04-26 | Added beginner-facing intent orchestration guidance explaining how changed intent is handled, how to ask for an idea-to-evidence trace, and how OS Health can warn when intent promotion or follow-up ownership is unclear. |
| v0.4.5 | 2026-04-26 | Added beginner-facing context engineering guidance explaining how to load the right files, avoid treating generated reports or source notes as instructions, and ask for a compact Context Pack before implementation or handoff. |
| v0.4.4 | 2026-04-26 | Added beginner-facing state integrity guidance explaining that Precode separates current memory, durable task state, historical evidence, and generated reports, and that reports may warn when those layers drift or become stale. |
| v0.4.3 | 2026-04-26 | Added beginner-facing decomposition guidance explaining that good beads are small enough to verify and that OS Health may warn about broad scope, vague done criteria, mixed planning and implementation, or unclear dependencies. |
| v0.4.2 | 2026-04-26 | Added beginner-facing verification quality guidance explaining that stronger work needs stronger proof and that OS Health may warn when evidence is too weak for the bead's risk. |
| v0.4.1 | 2026-04-26 | Added beginner-facing GitHub guidance for read-only audits, issue and pull request source intake, and the rule that GitHub status is evidence rather than Precode authority. |
| v0.4.0 | 2026-04-26 | Added scheduled audit guidance for opt-in background reporting, including `logs/scheduled-audit.md`, quiet-drift warnings, and the rule that audits are evidence, not instructions. |
| v0.3.0 | 2026-04-25 | Added student-facing "Why this matters" explanations and a categorized FAQ for common vibe-coding questions about scope creep, active memory, beads, evidence, checkpoints, generated reports, manual approvals, blocked work, multi-agent continuity, and spend visibility. |
| v0.2.0 | 2026-04-25 | Added the local-source-intake path so non-technical users can turn local notes, docs, screenshots, issue exports, research, diagrams, and drafts into PRD-ready summaries without making those sources active memory. |
| v0.1.0 | 2026-04-25 | Initial beginner-facing guide covering the daily Precode loop, active memory, PRD-to-bead flow, manual approvals, prompts, generated reports, and spend visibility notes. |
