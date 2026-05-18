# PrecodeOS Explainer
<!-- ANCHOR: os-readme -->

> AUTHORITY: Beginner-first canonical explainer for what PrecodeOS is, why it exists, how a non-technical builder should use it, and where to find deeper architecture or maintainer detail.
> NOT_AUTHORITY: Product requirements, active task selection, route structure, schema definitions, pricing decisions, generated progress state, changelog history, or deep architecture ownership.
> LOAD_WHEN: Onboarding a non-technical builder, explaining the PrecodeOS workflow, or choosing which deeper Precode reference to read next.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.8.9
Last updated: 2026-05-18

PrecodeOS is a Builder OS for working with AI coding agents inside a real project folder.

It helps a non-technical builder answer five questions before the project runs away:

- Where am I?
- What happens next?
- What do I approve?
- What proves the work?
- What do I do if something feels broken?

The technical definition is still true: PrecodeOS is a repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift.

In plain English: Precode lives inside your project folder, keeps important project truth in readable Markdown files, and uses small scripts to check whether the agent is staying aligned.

For builders, Precode feels like a small operating system for AI coding work: it shows what matters, what is active, what is proven, and when to stop.

PrecodeOS is open source under Apache-2.0. `NOTICE` preserves creator attribution: Created by Dan Sears / Recode. Canonical site: `https://www.precodeos.org`.

PrecodeOS™ and Precode™ are trademarks of Dan Sears / Recode. All trademark and brand rights are reserved. See `TRADEMARK.md` for brand-use guidance.

## The Short Version

AI coding agents can produce code faster than a new builder can review, direct, and recover from it. That speed is useful only when the project still knows what is true, what is active, what is out of scope, and what evidence proves done.

Precode gives the repo a small operating model:

- tiny active memory
- one current task
- clear owner files for durable facts
- optional discovery before PRD work
- PRDs before feature implementation when intent is fuzzy or risky
- small journey beads for execution
- recorded checks before acceptance
- human approval at task transitions
- recovery paths when state, proof, scope, or generated reports get confusing

The agent can inspect, draft, implement, explain, and propose. The builder still owns intent, approval, risk, and acceptance.

## Why PrecodeOS Matters

PrecodeOS matters because AI coding agents can move faster than a builder can understand, verify, and recover from. It keeps the project human-owned by making intent, scope, approval, proof, and recovery visible inside the repo.

## The Line Precode Holds

Vibe coding is tempting because it makes software development feel like a conversation. The risk is that the conversation moves faster than understanding.

Precode does not try to make the agent autonomous. It makes the project legible:

| Risk | Precode response |
|---|---|
| The agent follows stale chat or old notes. | Active memory stays tiny and current authority wins. |
| A rough idea becomes code too quickly. | Discovery, source intake, alignment, shared language, and PRDs clarify intent first. |
| Scope quietly grows. | One active bead, files in play, stop conditions, and files-in-play checks bound execution. |
| The agent says "done" without proof. | Checks are recorded and review decisions tie acceptance to evidence. |
| Generated summaries start driving work. | Generated reports are useful evidence, never authority. |
| The builder feels lost. | The `next-step` router, session start, recovery, user guide, and handoff surfaces explain what to do next. |

Precode is for builders who want speed without giving up direction, evidence, or the ability to stop.

## Two Core Rules

### 1. Active Memory Stays Tiny

Only three files are active memory:

| File | Job | Current size |
|---|---|---|
| `AGENT.md` | Tells the AI coding agent how to work in this repo. | 95 lines / 4,522 bytes |
| `DECISIONS.md` | Records hard decisions, open questions, and superseded context. | 37 lines / 1,985 bytes |
| `tasks/todo.md` | Points to the active bead and current execution view. | 84 lines / 3,189 bytes |

Everything else is reference, evidence, template, archive, adapter, or generated output. Load it only when the current work needs it.

Do not add a fourth active-memory file.

### 2. Generated Reports Are Evidence, Not Authority

Generated reports help humans see state, warnings, checks, learning, and handoff context. They do not choose tasks, approve PRDs, accept work, or activate the next bead.

Examples:

| Generated surface | Use it for | Do not use it for |
|---|---|---|
| `PRECODE-HELP.md` | Quick next-step, load plan, context-footprint, and warning snapshot. | Active memory, task selection, or transition approval. |
| `OS-HEALTH.md` | Health, warnings, evidence quality, spend, and state snapshots. | Active memory or acceptance by itself. |
| `PROGRESS.md` | Generated progress summary. | Product decisions or current task authority. |
| `logs/*.md`, `logs/*.json`, `logs/*.jsonl` | Evidence, sidecars, handoff, diary, indexes, and check output. | Replacing owner files. |

If a generated report looks wrong, repair the source state first and regenerate the report. Do not hand-edit generated Markdown as if it were truth.

## Why The PrecodeOS Name

“Precode” names the work that must happen before code: clarifying intent, context, decisions, language, proof, and approval. “OS” means Precode is the small operating layer around the agent and the repo, not a replacement for the agent, the app, or the builder’s judgment.

## The Six Rooms Of The Builder OS

Precode has many files and checks, but a builder should not have to memorize the file tree. Think of the surface area as six rooms.

### 1. Orient

Orient answers: "Where am I, and what truth is current?"

Main surfaces:

- `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md` for active memory
- `PRODUCT.md` for product promise, users, strategy, current bets, success signals, design, voice, and durable Goal Frames
- `PROJECT-CONTEXT.md` for app directory, stack, checks, conventions, and integration boundaries
- the user guide when the next kind of work is unclear

Plain-English posture: before asking the agent to build, make sure it can explain the current task, the owner file, the checks, and what needs approval.

### 2. Decide

Decide answers: "Is this idea ready to become planned work?"

Main surfaces:

- `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md` for rough early thinking
- discovery, source-intake, idea-to-PRD, and shared-language protocols when the user guide or active task calls for them

Product Discovery Validation is optional. Use it when an idea is broad, risky, market-facing, paid, evidence-poor, or solution-first. It should produce a short recommendation: `proceed`, `pause`, `narrow`, or `kill`.

Do not use discovery for tiny fixes, clear bugs, or follow-through from an approved PRD.

### 3. Plan

Plan answers: "What exactly should be built, and what is the smallest safe slice?"

Main surfaces:

- `tasks/prds/*.md` for destination PRD shards
- `FEATURES.md` for compiled approved feature inventory
- `tasks/beads/BEAD-SCHEMA.md` for bead shape, delegation mode, test strategy, review context, adaptive-depth fields, and closeout
- PRD, decomposition, and system-design protocols when planning needs them

A PRD is a destination document. It explains what should be true for the product.

A bead is an execution contract. It names one approved unit of work, one primary authority, files in play, checks, stop conditions, and proof needed.

### 4. Build

Build answers: "What may the agent change right now?"

Main surfaces:

- `tasks/todo.md` for the active bead pointer
- `tasks/beads/*.md` for current execution scope
- `modes/NAVIGATOR.md`, `modes/EXPLORER.md`, `modes/BUILDER.md`, and `modes/REVIEW.md` for role posture
- `adapters/*.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` for tool-specific shims
- agent-routing and tool-execution protocols when the task needs model, context, delegation, approval, or tool-call guidance
- Run Contracts in beads when higher-risk or bounded-AFK work needs allowed actions, proof needed, approval gates, and stop conditions

Precode is tool-neutral. It does not replace Codex, Claude, Cursor, Gemini, Antigravity, or future agents. It gives them a shared repo-owned operating model.

### 5. Prove

Prove answers: "What evidence says this is done?"

Main surfaces:

- `bash scripts/record-check.sh -- <command>` to record checks as evidence
- verification and handoff protocols when the task needs risk-based proof, closeout, review decisions, or transition approval
- `scripts/*-check.py` advisory checks for state, context, workflow, decomposition, completion, long-horizon planning, memory, run contracts, and more
- Closeout Evidence in the active bead

The review decision is one of:

- `accepted`
- `revise`
- `split`
- `blocked`

"The agent sounds confident" is not a review decision. Evidence is the review surface.

### 6. Recover

Recover answers: "What do I do when something feels broken or confusing?"

Main surfaces:

- the recovery, state-management, context, local-hygiene, and memory protocols when the user guide or active state calls for them
- `bash scripts/handoff.sh [next-agent]` and generated handoff packets for continuity

Recovery starts by stopping. Identify the symptom, find the owner file, repair source state, validate, and resume only when the next bounded action is clear.

## How Ideas Become Evidence

Precode turns rough ideas into verified work through a repeatable path:

```text
idea or source material
  -> optional product ideation workbook
  -> optional Product Discovery Validation
  -> Local Source Intake
  -> product constitution fit check
  -> alignment / grilling
  -> shared language
  -> destination PRD
  -> feature inventory
  -> journey bead proposal
  -> active bead
  -> implementation
  -> recorded checks
  -> review decision
  -> approved transition, handoff, or stop
```

That means:

- notes, screenshots, GitHub issues, research, and chat summaries start as evidence, not instructions
- durable intent can become a reviewed Goal Frame, but it does not choose work or approve execution
- PRDs propose work, but do not activate it
- beads execute work, but only one bead may be `in_progress`
- checks and manual verification prove what happened
- generated reports summarize state, but owner files and human approval govern action

## Daily Loop

Use this loop for normal work:

1. Start the session.
2. Confirm active memory, the current bead, primary authority, files in play, checks, and stop conditions.
3. Choose the right workflow before coding.
4. Let the agent work only inside the active bead.
5. Run guardrails when scope, files, commands, or risk widen.
6. Record checks as evidence.
7. Review Closeout Evidence and decide `accepted`, `revise`, `split`, or `blocked`.
8. Approve the next bead only when you are ready.

Core commands:

```bash
bash scripts/session-start.sh
bash scripts/checkpoint.sh
bash scripts/record-check.sh -- <command>
bash scripts/session-close.sh
bash scripts/handoff.sh next-agent
python3 scripts/next-step.py
python3 scripts/bead-depth-check.py
python3 scripts/files-in-play-check.py
python3 scripts/files-in-play-check.py --command "<command summary>"
python3 scripts/run-contract-check.py
python3 scripts/bead-transition.py --approve
```

The exact project checks depend on the app. The important habit is that checks are named before work starts and recorded before work is accepted.

## When To Stop The Agent

Stop or checkpoint when:

- the agent cannot name the active bead
- the next workflow is unclear
- product definition starts during implementation
- a task needs a second primary authority file
- more files are changing than the bead allowed
- checks are missing, vague, failing, or not tied to risk
- discovery says `pause`, `narrow`, or `kill` and the agent keeps planning implementation
- sensitive or bounded-AFK work lacks allowed actions, proof needed, approval gates, or rollback path
- the work touches auth, payments, personal data, uploads, deployment, secrets, GitHub mutation, dashboard mutation, or destructive action without approval
- generated reports, source notes, or old artifacts start acting like instructions
- the next task starts before you approve a bead transition

Stopping is not failure. In Precode, stopping is how the builder keeps the project understandable.

## How To Use This Map

This explainer names the six rooms and the Builder OS mental model behind them. It is not the canonical document router and it is not the exhaustive file dictionary.

- Use `README.md` when you need the public document compass.
- Use `docs/PRECODE-USER-GUIDE.md` when you are operating a PrecodeOS repo.
- Use `docs/PRECODE-FILE-INVENTORY.md` when you need every file, protocol, script, and relationship.

## Where To Go Next

For the canonical document compass, use `README.md`. If you are already operating a PrecodeOS repo, use `docs/PRECODE-USER-GUIDE.md` as the day-to-day home base.

## Adapting Precode To Your Project

For first-time setup, use `docs/PRECODE-GUIDED-SETUP.md`. It starts by pulling the public PrecodeOS repo from GitHub, then guides a manual, visible setup into a new or existing project without treating PrecodeOS as an app to run.

Start small:

1. Keep the three active-memory files.
2. Fill in `PRODUCT.md` with your product promise, users, strategy, current bets, success signals, and design or voice pointers.
3. Fill in `PROJECT-CONTEXT.md` with your app directory, stack, conventions, checks, and integration boundaries.
4. Use one starter bead to install or verify the kernel.
5. Use Product Discovery Validation only when the idea's worth-building evidence is uncertain.
6. Align/grill the first real product feature before writing the destination PRD.
7. Clarify shared language when the feature has domain terms, labels, or naming risk.
8. Split the destination into one small vertical journey bead.
9. Record checks before accepting the bead.
10. Add validators, audits, adapters, and integrations only when they solve a real repeated problem.

Do not ask an agent to set up everything in one pass. Ask it to create or adapt the kernel first, explain the files in plain English, and stop for review.

Starter prompt:

```text
I want to adapt PrecodeOS to my project.
Do not write application code yet.
First confirm the active-memory files, the current bead, the app directory, the project checks, and the first safe setup step.
Explain everything in plain English.
```

## Deeper Architecture And Maintainer Notes

Use `docs/PRECODE-ARCHITECTURE-OVERVIEW.md` when you need:

- the full layer-by-layer architecture
- script and validator internals
- generated sidecar and log taxonomy
- trust boundaries and prompt-injection posture
- maintainer procedures
- public fork guidance
- comparison landscape
- limitations and adoption path

This explainer is the conceptual Builder OS map. `README.md` is the public document compass, and the architecture overview is the maintainer and reviewer companion.

Maintainer-local document history for this explainer lives in `_maintainer/CHANGELOG.md`; it is not part of normal public package navigation.
