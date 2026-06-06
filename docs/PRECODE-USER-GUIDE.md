# How To Use PrecodeOS
<!-- ANCHOR: precode-user-guide -->

> AUTHORITY: Canonical hands-on user playbook for operating PrecodeOS as a non-technical builder.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, route structure, schema definitions, implementation plans, generated progress state, or deep architecture guidance.
> LOAD_WHEN: Onboarding a new user, running a Precode session, deciding what to ask an AI coding agent, or checking whether work is ready to accept.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.7.29
Last updated: 2026-06-06



## What This Guide Helps You Do

Use this guide while you work. It tells you what to ask the agent, what good output looks like, when to stop, and what you must approve.

Precode matters in daily use because AI coding agents can move faster than you can understand, verify, and recover from. This guide helps you keep intent, scope, approval, proof, and recovery visible while the agent works.

Precode lives inside your project folder. It keeps important project truth in readable Markdown files and uses small scripts to check whether the agent is staying aligned.

For builders, Precode feels like a small operating system for AI coding work: it shows what matters, what is active, what is proven, and when to stop.

PrecodeOS™ and Precode™ are trademarks of Dan Sears / Recode. See `NOTICE` and `TRADEMARK.md` for license, attribution, and brand-use guidance.

For the full document compass, go back to `README.md`. This guide is the operational home base: use it when you are about to work with an agent, decide whether to stop, approve risk, or check proof.

If PrecodeOS is not set up in your project yet, start with `docs/PRECODE-GUIDED-SETUP.md`. That guide walks through pulling the public PrecodeOS repo from GitHub, running Bootstrap Confidence, choosing the first adoption fork, copying the public package files into a fresh project or using Existing Repo Intake for an existing app, excluding private and generated material, and validating before work starts.

Put raw reference material for the project in root-level `project-evidence/`: notes, documents, screenshots, research, design exports, and link lists. Treat that folder as evidence only. It is not active memory, not product truth, not task approval, and not permission for the agent to code. Use Local Source Intake before promoting anything from it into owner files.

If you are helping someone else adopt PrecodeOS, use `docs/PRECODE-SUPPORT-RUNBOOK.md`. If setup, active state, validation, or generated reports feel wrong, use `docs/PRECODE-TROUBLESHOOTING.md` before editing files.

Why this matters: This guide is the operating manual. Keep it practical: follow the steps, copy the prompts, and stop when the guide says stop.

## Use The Product Ideation Workbook Before Precode

If you are a non-technical builder with a net-new, rough product idea, start with `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md` before asking Precode to update `PRODUCT.md`, write a PRD, create beads, or code.

Skip the workbook for bugs, maintenance, approved PRD follow-through, narrow feature changes, and other work where the problem and scope are already clear.

Use the workbook with Claude or Codex as a thinking coach. The agent can interview you, help research sources, challenge assumptions, and organize your thoughts. It must not decide the product for you, write code, edit `PRODUCT.md`, or create a PRD from the workbook by itself.

To keep the first session from feeling like a test, ask for a Product Brief after at most three high-level questions.

Say this:

```text
I am a non-technical founder with a rough product idea.

Use the Product Ideation Workbook path first. Ask only high-level product or business questions at the start. After at most three questions, summarize progress as a Product Brief with: product idea, intended user, painful before moment, better after moment, current workaround or evidence, assumptions, not-yet list, smallest useful version, and next best question.

Do not ask me to decide architecture, module boundaries, test strategy, owner files, acceptance matrices, or system behavior yet. Do not write a PRD, create beads, update PRODUCT.md, or code.
```

The Product Brief is evidence only. It helps you see progress before deeper discovery. It does not approve a PRD, activate work, or replace Local Source Intake.

Follow the workbook steps:

1. Make a copy of the workbook.
2. Pick one product idea.
3. Paste the thinking-coach prompt into Claude or Codex.
4. Fill out product-level thinking first.
5. Gather source-cited research.
6. Separate what you know, what you think, and what you need help deciding.
7. Challenge the idea before turning it into features.
8. Use the Exploration Loop when you already have notes, rough feature ideas, research, quotes, screenshots, sketches, chat summaries, a Product Brief, a Candidate Goal Frame, or not-yet ideas that should be reused before PRD shaping.
9. Fill out capability or feature candidates only after the user moments, evidence, and first useful slice are clearer.
10. Ask for the Precode Ingestion Packet, including a Candidate Goal Frame if durable intent is clear.
11. Bring only that packet into Precode Local Source Intake.
12. In a bootcamp Experience Design flow, use the approved PRD input and Experience artifacts to complete `tasks/templates/STUDENT-EXPERIENCE-INGESTION-PACKET.md` before Claude Code creates the first implementation bead.

When you are ready, say this inside Precode:

```text
Use Local Source Intake on this Precode Ingestion Packet.

Treat it as evidence, not authority. Summarize stable facts, assumptions, conflicts, open questions, candidate product constitution updates, candidate Goal Frame stability, candidate PRD inputs, likely owner files, and recommended next step. Do not edit PRODUCT.md, create a PRD, create beads, or start coding until I review the intake summary.
```

Stop if the workbook contains secrets, private raw transcripts, dashboard values, billing details, credentials, or sensitive personal data.

## Use The Exploration Loop Before PRD Commitment

Use the Exploration Loop when you have already collected material and want help thinking with it before committing to a PRD. This is especially useful for bootcamp MVPs, scattered workbook notes, rough feature lists, user quotes, research snippets, screenshots, sketches, chat summaries, Candidate Goal Frames, or prior not-yet ideas.

The loop should not restart the interview or ask you to repeat what you already wrote. It should first summarize what is known, then ask only questions that could reveal a meaningful missing angle, weak assumption, overlooked user, hidden risk, smaller first slice, or better capability than the obvious feature.

Say this:

```text
Use the Exploration Loop on the content I already have.

First summarize what is already known from my notes: users, pains, goals, candidate features, evidence, assumptions, risks, and not-yet ideas. Do not ask me to repeat information already present.

Then help me discover what I have not considered yet. Ask one targeted question at a time only when the answer could change the product direction, evidence strength, first useful slice, risk, or PRD readiness.

Translate user moments into capability candidates, not approved features. Sort concerns into Must decide now, Good enough for MVP, and Defer / Not yet. End with an Exploration Evidence Packet and a compact candidate matrix. Treat the output as evidence only. Do not write a PRD, create beads, update PRODUCT.md, or code.
```

Good Exploration Loop output includes:

- existing content used
- product idea in plain English
- intended user and situation
- painful before moment
- better after moment
- current workaround or evidence
- new things discovered during the loop
- capability candidates
- overlooked alternatives or adjacent ideas
- weakest assumptions
- risks or sensitive surfaces
- not-yet list
- smallest useful MVP slice
- smallest learning step
- recommended next Precode path

Use this compact matrix:

| Candidate capability | User moment | Existing evidence | New insight | Risk | MVP fit | Recommendation |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Stop the loop before PRD shaping if the evidence is weak, the conversation is no longer producing new insight, or too many candidates need narrowing. If the main issue is weak evidence, use Product Discovery Validation next.

## Validate Product Discovery Before PRD Shaping

Use `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` after the workbook or Product Brief when an idea is broad, risky, market-facing, paid, evidence-poor, or sounds like a solution before the problem is clear.

This is not a proof machine. It helps you see:

- who has the problem
- what they do today instead
- what evidence is strong or weak
- which assumption could break the idea
- what non-code learning step should happen first
- whether the safer recommendation is `proceed`, `pause`, `narrow`, or `kill`

Say this:

```text
Use Product Discovery Validation on this idea.
Interview me one question at a time. Challenge assumptions supportively.
Tell me the current workaround, strongest evidence, weakest assumption, smallest non-code learning step, and whether you recommend proceed, pause, narrow, or kill.
Treat the output as evidence only. Do not write a PRD, create beads, update PRODUCT.md, or code.
```

Skip this for tiny fixes, already-approved PRD follow-through, clear bugs, or narrow maintenance work.

## Before You Start

Do this before letting an agent edit files:

- Open the repo or project folder that contains PrecodeOS.
- Confirm the agent is using Precode instructions.
- Ask the agent to load active memory only: `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
- Ask the agent to identify the active bead and primary authority file.
- Work on one feature slice or bead at a time.
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

Stop if: the agent cannot explain the current bead in plain English, or if it tries to work on more than one feature slice at once.

## Check Build Loop Health

Build Loop Health is a quiet Precode signal for whether the current work is focused, stoppable, closeable, evidenced, and easy to steer. It evaluates the loop, not you.

Use it when the session feels busy, when scope starts to grow, at checkpoint, or before closeout:

```bash
python3 scripts/loop-health.py
python3 scripts/loop-health.py --verbose
```

Good output gives one status, one top risk, and one next move. `Clear` means keep going inside the current boundary. `Watch` means one thing needs attention. `Drift Risk` or `Recenter` means the loop is getting hard to steer. `Stop and Review` means the current work is ready or risky enough that evidence should be reviewed before adding more.

If you are exploring before a bead exists, that is allowed. When the exploration starts to matter, ask the agent to create or select a lightweight explorer bead with one question and one stopping condition.

Say this:

```text
Run python3 scripts/loop-health.py and explain the top risk in plain English. If I am exploring without a bead, help me create a lightweight explorer bead with one question and one stopping condition before any implementation.
```

Why this matters: Precode should protect you from accidental sprawl without making creative exploration feel wrong.

## Use Goal Frames For Durable Intent

Use a Goal Frame when your intent is durable enough to guide workflow selection, but not ready to become tasks, a roadmap, or code.

If you started in the Product Ideation Workbook, the safe sequence is:

```text
Initial Direction -> workbook refinement -> Candidate Goal Frame -> Local Source Intake -> reaffirmation -> PRODUCT.md Goal Frame
```

Do this:

- Ask the agent to draft a Goal Frame for review.
- Store it only inside an existing owner file: `PRODUCT.md`, a PRD, a bead, or `DECISIONS.md` when it is tied to a hard decision.
- Reaffirm it before the agent uses it to guide workflow selection.
- Treat stale or conflicting Goal Frames as a reason to pause and ask questions.

Do not use a Goal Frame to approve a PRD, activate a bead, choose the next task, create a backlog, or start coding.

Say this:

```text
This sounds durable. Draft a Goal Frame for my review, but do not create tasks or start coding.
```

Say this for a workbook packet:

```text
Use Local Source Intake on this Candidate Goal Frame. Tell me whether it is stable enough to reaffirm, but do not update PRODUCT.md.
```

Say this after you reaffirm it:

```text
If I reaffirm this Goal Frame, update PRODUCT.md only with the reviewed Goal Frame section and do not create tasks or code.
```

Say this before using one:

```text
Before using this Goal Frame, ask me to reaffirm it. Use it only to explain workflow guidance. Do not activate or approve work.
```

Why this matters: Goal Frames help the repo remember the direction you are aiming at without hiding stale intent inside the agent's next move.

## Do Not Move, Rename, Or Directly Edit Precode Files

Precode works because specific Markdown files have specific names, locations, headings, anchors, and metadata. Moving, renaming, or casually editing those files can break how agents and scripts find the right memory, task, or authority file.

Hard rules:

- Do not rename the project root folder casually. That folder is the repo that mirrors GitHub and contains both the app code and the Precode operating files.
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
| Rename the project folder | Stop and ask an engineer or maintainer how the local folder, Git remote, GitHub repo, and editor workspace should stay connected. |
| Edit a generated report | Regenerate it with the correct script instead of editing it by hand. |
| Record a decision | Put it in `DECISIONS.md` or ask which owner file should hold it. |
| Clarify product direction | Update `PRODUCT.md` or ask whether the fact belongs in a PRD or `DECISIONS.md`. |
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

Say this before renaming the project folder:

```text
I want to rename the project root folder. Stop and tell me what this could break in Git, GitHub, my editor workspace, app paths, and Precode validation before anything is renamed.
```

Say this if something already went wrong:

```text
I accidentally edited, moved, or renamed a Precode file. Help me identify the damage, restore the expected path, name, anchor, authority contract, frontmatter, and headings, then run validation.
```

Why this matters: Precode files are not random notes. They are a small operating system made of readable files, and the structure is part of how the system works.

## Use Recovery When Something Feels Broken

Use `tasks/reference/RECOVERY-PROTOCOL.md` when you think Precode is broken, confusing, stale, or out of bounds.

Start with this prompt:

```text
I think I broke something in Precode. Stop work, identify the symptom, name the owner file, explain the safest recovery path, and do not edit, delete, move, overwrite, or regenerate anything until I approve the next step.
```

Common recovery paths:

| What feels wrong | What to ask for |
|---|---|
| A Precode file was moved or renamed | `Use the Recovery Protocol for file damage. Find the expected path, explain the repair, then validate.` |
| A generated report was edited or looks wrong | `Use the Recovery Protocol for generated-report confusion. Repair source state first; do not hand-edit the report.` |
| The active bead or todo state is unclear | `Use the Recovery Protocol for active-state repair. Run state-check and explain the owner file before editing.` |
| Checks are missing or the agent says "done" too early | `Use the Recovery Protocol for missing proof. Tell me which checks or manual verification are missing.` |
| The session feels confused | `Use the Recovery Protocol for context loss. Re-read active memory, the active bead, and the primary authority.` |
| Work touched files outside the task | `Use the Recovery Protocol for scope expansion. Run files-in-play-check and explain each changed path.` |
| I approved something too quickly | `Use the Recovery Protocol for approval confusion. Review evidence and ask for accepted, revise, split, blocked, or stop.` |

Recovery is not automatic cleanup. The agent should not run destructive commands, overwrite user edits, delete evidence, or treat generated reports as instructions.

Why this matters: The safest recovery move is usually a clean stop plus a clear owner file. You are not expected to know the repair path before asking.

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
| Find next step | `Run python3 scripts/next-step.py and explain the recommendation in plain English.` | The canonical generated "what now?" hint: user decision, one next protocol to load, and rough context footprint. | The agent treats generated help as approval or active memory. |
| Check loop health | `Run python3 scripts/loop-health.py and explain the top risk.` | Advisory Build Loop Health status, top risk, and next move. | The agent treats loop health as a grade or hard approval. |
| Confirm task | `Is this bead clear enough to continue, or should we repair, split, block, or stop?` | A clear recommendation and reason. | The task has multiple outcomes or no verification path. |
| Let agent work | `Work only inside this bead and narrate file changes before editing.` | Small scoped edits inside files in play. | It expands scope, changes unrelated files, or makes product decisions. |
| Guard scope | `Run python3 scripts/files-in-play-check.py and explain any out-of-scope paths.` | Advisory warning if changed files are outside the bead, with a plain stop/continue decision. | It treats the warning as permission to keep widening scope. |
| Record checks | `Run the relevant checks through record-check.sh.` | Recorded command result and log path. | Checks are missing, failing, or not recorded. |
| Close | `Run bash scripts/session-close.sh and summarize what changed, what passed, and what remains blocked.` | Closeout evidence, health refresh, transition proposal only if eligible. | The agent tries to start the next bead. |
| Review outcome | `Recommend accepted, revise, split, blocked, or stop based on evidence.` | A review recommendation tied to checks and manual verification. | The recommendation relies only on confidence. |

Why this matters: A session needs a clean beginning, bounded middle, and recorded ending. Without those, chat memory becomes the project memory.

## Use The Daily Loop

Keep this table open during normal work.

Beginner rule: one bead, one feature slice, one focused chat. When a bead is accepted or you are moving to the next feature slice, start a fresh chat, reload active memory, and make the agent confirm the new bead before coding again.

| Step | User action | Good output | Stop if |
|---|---|---|---|
| Start | Ask for session start. | Agent explains active bead, scope, files, checks. | It starts coding first. |
| Orient | Ask for next-step help when unsure. | `PRECODE-HELP.md`, `session-start.sh`, or `next-step.py` explains the same generated router decision. | The report replaces the active bead. |
| Check loop health | Ask for Build Loop Health when scope or stopping point feels fuzzy. | One status, top risk, and next move. | The signal becomes a score of you instead of the work loop. |
| Confirm | Ask whether to continue, repair, split, block, or stop. | One clear path. | Scope is vague or too broad. |
| Work | Let the agent edit only scoped files. | Small changes tied to the bead. | It touches unrelated files. |
| Check | Ask for recorded checks. | `record-check.sh` output and evidence path. | It says done without evidence. |
| Checkpoint | Pause when confused or scope grows. | Restated task, changed files, next check. | It resists narrowing. |
| Close | Ask for session close. | Closeout evidence and review state. | It starts the next bead. |
| Approve | Approve only after review. | Accepted, revise, split, blocked, or transition. | Manual verification is unclear. |
| Commit | Commit and push each completed, checked slice. | A small commit named for the user-visible slice or repair. | Changes pile up across features or the name is vague, such as `updates` or `fixes`. |

Why this matters: The daily loop is not ceremony. It is how you keep the agent from turning one request into a moving target.

Use this before committing:

```text
Give me a commit-ready summary for this completed slice: files changed, evidence recorded, manual verification still needed, and a concise commit name that describes the user-visible feature or repair.
```

## Checkpoint Before Context Gets Crowded

Long sessions can get fuzzy even when the agent is still trying hard. When the conversation feels crowded, the agent is repeating itself, or a lot of files and tool outputs have passed through the chat, pause before the context gets full.

Say this:

```text
Use the Agent Routing Protocol and Context Engineering Protocol. If this session is near the context pressure point, prepare a Context Pack before compacting, restarting, or handing off. Include the bead, primary authority, files in play, latest evidence, changed files, remaining work, and next exact check.
```

Good output includes:

- the active bead and primary authority
- what changed
- what evidence exists
- what is still uncertain
- the next exact check or question

Why this matters: You are not trying to tune the model. You are making sure the agent has enough clean room to finish, verify, and hand off without losing the task.

## Use The Plain Decision Words

Precode checks should help you choose what to do, not make you learn internal labels. When a script reports a `user_decision`, read it this way:

| Decision | What it means | What to say |
|---|---|---|
| `continue` | The current bead can keep moving inside its named scope. | `Continue inside this bead only, then record the declared checks.` |
| `ask for missing info` | The agent needs an input, owner, manual step, or unblocker before coding. | `Do not work around the blocker. Tell me exactly what is missing.` |
| `ask for proof` | Work may be close, but evidence, checks, or review are not enough yet. | `Show me the missing proof before I accept this.` |
| `review` | The bead needs an acceptance decision. | `Recommend accepted, revise, split, blocked, or stop based on evidence.` |
| `approve transition` | A next bead may be ready, but only the user can activate it. | `Show the transition proposal. Do not activate it until I approve.` |
| `repair state` | Precode cannot safely orient because active state is unclear. | `Repair active state before editing anything.` |
| `stop` | Scope, command risk, sensitive work, or file drift needs human judgment first. | `Stop and explain the risk in plain English.` |

Why this matters: You should not have to sound technical to operate Precode. The scripts should translate risk into a small number of safe decisions.

## Choose What To Ask For

Use this table when you are unsure what kind of request to make.

| Situation | Ask for | Copyable request |
|---|---|---|
| Net-new rough product idea from a non-technical founder | Product Ideation Workbook plus Product Brief | `Use the Product Ideation Workbook path first. Ask only high-level product or business questions. After at most three questions, summarize a Product Brief and one next best question. Do not write a PRD or code.` |
| My PRD input feels thin or scattered | PRD-Ready Context | `Use PRD-Ready Context to organize product context, user and problem, before/after experience, constraints, success signals, risks, and unknowns. Treat the result as evidence for Local Source Intake or PRD shaping, not as an approved PRD, bead, or permission to code.` |
| Existing notes or rough feature ideas need real thinking before PRD commitment | Exploration Loop | `Use the Exploration Loop on the content I already have. Reuse my notes, summarize what is known, ask only targeted questions that could change the product direction, evidence, risk, or first slice, then produce an Exploration Evidence Packet. Do not write a PRD or code.` |
| Starting a new product or checking product drift | Product constitution review | `Review PRODUCT.md with me. Clarify product promise, users, strategy, non-goals, current bets, success signals, and design or voice. Do not code.` |
| Broad, risky, paid, market-facing, or weakly evidenced idea after the first Product Brief | Product Discovery Validation | `Use Product Discovery Validation. Name the current workaround, strongest evidence, weakest assumption, smallest non-code learning step, and recommend proceed, pause, narrow, or kill. Do not write a PRD or code.` |
| I want the smallest safe build to teach me something | Fast Learning Lane | `Use the Fast Learning Lane. Skip discovery ceremony only if this is low or medium risk with no sensitive surfaces, no product-promise drift, and a tiny reversible learning slice. Create a minimal PRD with requirement IDs, acceptance checks, risk flags, and one candidate bead. Do not code or activate the bead until I approve.` |
| Rough idea, notes, screenshot, GitHub issue, research | Local source intake | `Use Local Source Intake. Summarize facts, assumptions, conflicts, open questions, candidate requirements, and possible beads. Do not code.` |
| Feature idea is fuzzy | Alignment / Product Brief | `Use the Idea To PRD Workflow. Ask one high-level product or business question at a time, include your recommended answer, and after at most three questions summarize a Product Brief. Do not plan or code yet.` |
| Terms, labels, or names are confusing | Shared-language review | `Use the Ubiquitous Language Protocol. List the terms I am using, what each means, aliases, avoid terms, source pointers, and UI/code/test examples. Do not code.` |
| Durable intent needs to guide the next workflow | Goal Frame proposal or reaffirmation | `Draft or reaffirm a Goal Frame for my review. Use it only as advisory workflow context. Do not create tasks, activate beads, or code.` |
| Product direction is clear enough | Destination PRD | `Turn the aligned idea into a destination PRD with problem, non-goals, before/after moment, risks, acceptance checks, agent-facing technical translation, and smallest first vertical slice. Do not code.` |
| Approved PRD exists | Bead decomposition | `Use the Decomposition Protocol to propose journey beads small enough to verify. Prefer vertical slices, include delegation_mode, test_strategy, review_context, and do not activate anything.` |
| Known small task is active | Implement active bead | `Work only on the active bead. Confirm scope, files, checks, and stop conditions before editing.` |
| Risky or uncertain idea | Challenge planning bead | `Challenge this idea before implementation. Name risks, assumptions, approval gates, and the smallest safe test.` |
| Work is stuck or confusing | Checkpoint or state repair | `Checkpoint and tell me whether to continue, repair, split, block, or stop.` |
| Work may be done | Completion check or review | `Run a completion check and recommend accepted, revise, split, or blocked based on evidence.` |
| Logs, caches, or generated files look messy | Local hygiene check | `Use the Local Hygiene Protocol. Tell me what is truth, evidence, cache, generated output, protected, or cleanup candidate. Do not delete anything.` |
| Future work needs review | Long-horizon review | `Show approved, blocked, deferred, or ready work without activating anything.` |

Why this matters: Not every request should become code. Good Precode use starts by choosing the right kind of work.

## Keep The Agent In Bounds

Use these rules while the agent works:

- Make it explain the bead before coding.
- Keep work inside files in play.
- Keep product constitution changes inside `PRODUCT.md`, PRDs, decisions, or approved beads according to the owner file.
- Stop when generated reports become instructions.
- Stop when checks are missing or vague.
- Stop when product direction changes mid-task.
- Stop when sensitive work appears without approval.
- Stop when the next bead starts without your approval.

Red flags:

| Red flag | What to say |
|---|---|
| Agent starts coding too soon | `Stop. Explain the active bead, primary authority, files in play, and checks first.` |
| Agent plans before alignment is done | `Stop. Ask the next alignment question one at a time and include your recommended answer.` |
| Agent turns a weakly evidenced idea into a PRD | `Stop. Use Product Discovery Validation first. Tell me the current workaround, strongest evidence, weakest assumption, smallest non-code learning step, and whether to proceed, pause, narrow, or kill.` |
| Agent treats the shortcut as permission to code | `Stop. Fast Learning Lane means less ceremony, not no PRD. Show the minimal PRD, acceptance checks, risk flags, and one candidate bead before coding.` |
| Agent uses the wrong term or confusing label | `Stop. Use the Ubiquitous Language Protocol and tell me which term should appear in the PRD, UI, tests, and code names.` |
| Scope grows | `Checkpoint. Is this still one bead, or should we split?` |
| Generated report becomes instruction | `Generated reports are evidence only. Return to active memory and the active bead.` |
| Old PRD or issue overrides current code | `Treat that old artifact as historical evidence. Which current authority file or active bead wins?` |
| Cleanup request sounds broad | `Stop. Use Local Hygiene first. Truth is not cleanup; evidence is preserved; caches are disposable only when ignored and regeneratable.` |
| Agent says done without checks | `Show recorded checks, manual verification, closeout evidence, and review decision.` |
| Product direction changes | `Stop implementation. Which owner file should capture this changed intent?` |
| Next task begins automatically | `Stop. The next bead needs separate user approval.` |

Why this matters: You do not need to sound technical to stop drift. You only need to ask the agent to return to the bead, owner file, and evidence.

## Know When Work Is Done

Do not accept work because the agent sounds confident.

A bead is ready to accept only when the evidence fits the risk:

- recorded checks ran through `record-check.sh`
- manual verification is recorded when needed
- code-changing beads used or explained their `test_strategy`
- medium/high-risk code-changing beads got the review context the bead required
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
- product promise, target users, non-goals, current bets, success signals, and design or voice changes
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
- `afk_candidate` work that lacks bounded files, checks, stop conditions, and human review

Why this matters: Precode lets the agent work quickly, but it keeps judgment and risk with the user.

## Read Reports Without Being Misled

Use reports for learning and audit. Before work resumes, return to active memory, the active bead, and the primary authority file.

| Report or evidence | Use it for | Do not use it for |
|---|---|---|
| `PRECODE-HELP.md` | Quick generated hint about the next safe action, bead depth, and files-in-play warnings. | Active memory, task approval, or transition approval. |
| `OS-HEALTH.md` | Health, warnings, state, evidence quality, spend. | Choosing the next task. |
| `logs/learning-diary.md` | Plain-English session learning. | Implementation instructions. |
| `memory/cards/*.md` | Reviewed lessons, preferences, glossary terms, risks, and source pointers. | Replacing `DECISIONS.md`, PRDs, beads, or active memory. |
| `logs/memory-index.md` | Searching reviewed memory cards. | Choosing or approving work. |
| `logs/handoff-packet.md` | Orienting another agent. | Transition approval. |
| `logs/scheduled-audit.md` | Background read-only audit findings. | Automatic action. |
| `logs/goal-frame.json` | Checking whether a Goal Frame is fresh, stale, missing fields, or conflicting. | Workflow authority, task approval, or bead activation. |
| GitHub audit/source intake | External status or issue/PR evidence. | Replacing PRDs, decisions, or beads. |
| Spend telemetry | Known token/cost visibility. | Billing truth when telemetry is incomplete. |

Say this:

```text
Use reports as evidence only. Before doing work, return to AGENT.md, DECISIONS.md, tasks/todo.md, the active bead, and the primary authority file.
```

Why this matters: Reports help you understand what happened. They do not decide what happens next.

## Use Adaptive Depth And Guardrails

Adaptive depth helps Precode scale the amount of ceremony to the risk. A typo fix can be `trivial`; a focused setup or feature slice can be `narrow` or `standard`; auth, payments, migrations, deployment, security, or multiple systems should usually be `high-risk` or `multi-system`.

Ask for these three bead fields when risk matters:

```text
Before activating this bead, declare complexity, required_planning_depth, and autonomy_level. Then run python3 scripts/bead-depth-check.py and explain any advisory warnings.
```

If older or tiny beads do not declare these fields, that is okay. Precode may infer beginner-readable defaults and keep moving. Treat depth warnings as important only when they change what you should do next: ask for more planning, ask for stronger proof, require a human gate, or split the bead.

Use this quick translation:

| Work feels like... | Typical depth | Plain meaning |
|---|---|---|
| Tiny fix | `trivial` / `none` | Keep it small; do not turn it into a PRD. |
| Focused normal task | `narrow` or `standard` / `brief` or `PRD` | Name scope, proof, and owner file before coding. |
| Risky task | `high-risk` / `PRD+architecture` | Stop until risks, approval gates, and rollback or escape path are clear. |
| Many systems | `multi-system` / `PRD+architecture+test-plan` | Split or plan carefully; do not let the agent improvise across systems. |
| Human-owned action | `human-only` | The agent may prepare instructions, but the user owns the action or approval. |

If `python3 scripts/files-in-play-check.py` warns about out-of-scope paths, pause and ask whether those changes belong in the active bead, a follow-up bead, or should be reverted by the person who made them. The warning is not permission to keep widening the task.

Say this:

```text
Run the files-in-play guardrail. If any changed path is outside this bead, stop and explain whether it is generated evidence, current-bead work, or a separate follow-up.
```

Before running a risky command, ask the guardrail to classify it:

```text
Run python3 scripts/files-in-play-check.py --command "<command summary>" and explain whether the decision is continue, approval needed, or stop. Do not run the command yet.
```

Use `--edit-lock` for high-risk beads when you want an advisory check against the active bead's files in play:

```text
Run python3 scripts/files-in-play-check.py --edit-lock and explain whether any changed path is outside this bead. Treat the lock as advisory evidence, not permission.
```

For sensitive, external, destructive, or bounded-AFK work, ask for the stricter plain-English contract before work starts:

```text
Before continuing, show the allowed actions, proof needed, approval required before risky actions, stop conditions, and rollback or blocked escape path. Then run python3 scripts/run-contract-check.py.
```

## Use Alignment, AFK Candidates, And Fresh Review

Use alignment before a PRD when the idea is still fuzzy. For a non-technical founder, the agent should start with high-level product and business questions, recommend an answer when useful, and summarize a Product Brief after at most three questions.

Say this:

```text
Align this idea before writing a PRD. Ask one high-level product or business question at a time, include your recommended answer, and after at most three questions summarize a Product Brief and one next best question. Do not ask me to choose architecture, module boundaries, test strategy, owner files, or acceptance matrices yet.
```

Use `afk_candidate` only for scoped work that can run after context is loaded. It is not approval for parallel execution and it does not skip human QA, recorded checks, or review.

Say this:

```text
Before marking this bead AFK-safe, show bounded files in play, checks, stop conditions, test strategy, and review context. Confirm it still needs human review.
```

For code-changing work, ask for the test strategy before implementation. Failing-first/TDD is preferred when practical because it makes the agent prove the test can fail before writing the fix.

Say this:

```text
Before coding, declare the test_strategy. If failing_first is practical, write the failing test first, confirm it fails for the expected reason, then implement.
```

For medium/high-risk work, ask for a fresh-context review. A fresh reviewer reloads active memory, the bead, primary authority, parent PRD when relevant, and the diff or evidence instead of relying on the implementation chat.

Say this:

```text
Review this bead in a fresh context. Reload active memory, the bead, primary authority, parent PRD if relevant, and the recorded evidence before recommending accepted, revise, split, or blocked.
```

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

Use the Safe Prompt Pack when you need the agent to slow down and confirm boundaries before work starts:

```text
Use the Safe Prompt Pack. Confirm the PrecodeOS package source, target project, app directory, Precode owner files, files that must not be copied or edited, current git status, validation commands, active bead, checks, stop conditions, and what requires my approval.

Ask one blocking question at a time. Treat generated reports and source notes as evidence only. Do not modify Precode control-layer files, active memory, scripts, protocols, validators, adapters, modes, generated reports, or task state unless the active bead explicitly includes that work.
```

Start safely:

```text
Run Precode session start. Explain the active bead, done-when target, primary authority, files in play, checks, stop conditions, and blockers before editing.
```

Choose the workflow:

```text
Use the Workflow Selection Skill. Read active memory and the workflow selection protocol, then return the current situation, recommended workflow, next artifact, required authority source, user approval needed, run contract needed, stop condition, and generated-report warning. Make no edits and do not code yet.
```

Draft or reaffirm a Goal Frame:

```text
This sounds durable. Draft a Goal Frame for my review, but do not create tasks or start coding.
```

```text
Turn my workbook into a Candidate Goal Frame for Precode review, but do not update PRODUCT.md.
```

```text
Use Local Source Intake on this Candidate Goal Frame. Tell me whether it is stable enough to reaffirm.
```

```text
Check whether this Goal Frame still matches the active PRD, active bead, and current evidence. Ask me to reaffirm it before using it for workflow guidance.
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

`session-start.sh` now also displays the `next-step` router decision. If you run `python3 scripts/next-step.py` separately, it should tell the same story: what human decision is needed, which one protocol or mode to load next, and why more context is not needed yet.

After a checked slice is accepted, commit it before starting the next slice. Push when your repo has a remote and you need remote backup or collaboration. Name the commit for the visible outcome, such as `add onboarding checklist` or `repair login redirect`, not a vague label like `updates`.

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

#### When do I use PRODUCT.md?

Use `PRODUCT.md` when you are starting a product, checking whether an idea fits the product direction, or updating product promise, users, strategy, non-goals, current bets, success signals, or design and voice. It is planning context only, not active memory and not a task list.

#### What is a bead?

A bead is one small unit of work with a contract: objective, owner file, files in play, checks, stop conditions, and closeout evidence.

#### When do I use a PRD?

Use a PRD when the feature needs a destination before coding: problem, non-goals, user moment, requirements, risks, acceptance checks, and likely journey beads.

#### What is alignment?

It is the conversation before the PRD where the agent helps you share the same design concept before anyone plans or codes. For rough founder ideas, it should start with simple product questions and a Product Brief before technical translation.

#### What is shared language?

It is the small vocabulary you and the agent agree to use for the product. If you call something a "client intake," the PRD, UI, tests, and code should not quietly call it four different things unless there is a reason.

#### What is a project glossary?

It is a reviewed memory card for useful terms, aliases, avoid terms, examples, and source pointers. It helps future agents understand language, but it is evidence only. Current code, active beads, approved PRDs, and owner files still win.

#### What is an AFK candidate?

It is a bead that may be safe for an agent to execute after context is loaded. It still needs bounded scope, checks, stop conditions, manual QA when needed, and review.

#### What is a vertical slice?

It is a small piece of work that crosses enough layers to show real behavior. For user-facing work, prefer that over schema-only, backend-only, frontend-only, or tests-later beads.

#### What should I do with an old PRD or closed issue?

Treat it as historical evidence. Current active memory, current code, the active bead, the current approved PRD, and owner files are stronger than stale artifacts.

#### What should I do with noisy logs or caches?

Use Local Hygiene. The first commands only warn and dry-run. They should never delete, archive, compact, or move files. Evidence is preserved; caches are disposable only when ignored and regeneratable.

#### What if I change direction mid-task?

Stop implementation. Decide whether the change belongs in a PRD amendment, `DECISIONS.md`, an authority file, a follow-up bead, or deferral.

#### What is a Goal Frame?

A Goal Frame is reviewed orientation for a durable goal. It can help guide workflow selection, but it cannot approve work, activate beads, replace a PRD, or become a backlog.

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
