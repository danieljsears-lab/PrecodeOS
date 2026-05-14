# PrecodeOS Explainer
<!-- ANCHOR: os-readme -->

> AUTHORITY: Beginner-first canonical explainer for what PrecodeOS is, why it exists, how a non-technical builder should use it, and where to find deeper architecture or maintainer detail.
> NOT_AUTHORITY: Product requirements, active task selection, route structure, schema definitions, pricing decisions, generated progress state, changelog history, or deep architecture ownership.
> LOAD_WHEN: Onboarding a non-technical builder, explaining the PrecodeOS workflow, or choosing which deeper Precode reference to read next.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.8.3
Last updated: 2026-05-13

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
| The builder feels lost. | Next-step, recovery, user guide, and handoff surfaces explain what to do next. |

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
| `PRECODE-HELP.md` | Quick next-step and warning snapshot. | Active memory, task selection, or transition approval. |
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
- `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when the next kind of work is unclear
- `tasks/reference/GOAL-FRAME-PROTOCOL.md` when durable intent needs orientation before workflow selection

Plain-English posture: before asking the agent to build, make sure it can explain the current task, the owner file, the checks, and what needs approval.

### 2. Decide

Decide answers: "Is this idea ready to become planned work?"

Main surfaces:

- `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md` for rough early thinking
- `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` when worth-building uncertainty is high
- `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` for notes, docs, screenshots, issues, and research as evidence
- `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` for alignment, grilling, and destination PRD shaping
- `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` when product terms, UI labels, code names, or test names could drift

Product Discovery Validation is optional. Use it when an idea is broad, risky, market-facing, paid, evidence-poor, or solution-first. It should produce a short recommendation: `proceed`, `pause`, `narrow`, or `kill`.

Do not use discovery for tiny fixes, clear bugs, or follow-through from an approved PRD.

### 3. Plan

Plan answers: "What exactly should be built, and what is the smallest safe slice?"

Main surfaces:

- `tasks/prds/*.md` for destination PRD shards
- `FEATURES.md` for compiled approved feature inventory
- `tasks/reference/PRD-PROTOCOL.md` for the Product Definition Gate
- `tasks/reference/DECOMPOSITION-PROTOCOL.md` for vertical journey beads
- `tasks/beads/BEAD-SCHEMA.md` for bead shape, delegation mode, test strategy, review context, adaptive-depth fields, and closeout
- `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when implementation shape, interfaces, data flows, or strategy boundaries matter

A PRD is a destination document. It explains what should be true for the product.

A bead is an execution contract. It names one approved unit of work, one primary authority, files in play, checks, stop conditions, and proof needed.

### 4. Build

Build answers: "What may the agent change right now?"

Main surfaces:

- `tasks/todo.md` for the active bead pointer
- `tasks/beads/*.md` for current execution scope
- `modes/NAVIGATOR.md`, `modes/BUILDER.md`, and `modes/REVIEW.md` for role posture
- `adapters/*.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` for tool-specific shims
- `tasks/reference/AGENT-ROUTING-PROTOCOL.md` for model tier, context budget, delegation, and tool-routing language
- `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` for risky tool calls, approval-sensitive actions, and tool-run logging
- Run Contracts in beads when higher-risk or bounded-AFK work needs allowed actions, proof needed, approval gates, and stop conditions

Precode is tool-neutral. It does not replace Codex, Claude, Cursor, Gemini, Antigravity, or future agents. It gives them a shared repo-owned operating model.

### 5. Prove

Prove answers: "What evidence says this is done?"

Main surfaces:

- `bash scripts/record-check.sh -- <command>` to record checks as evidence
- `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` for risk-based proof expectations
- `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` for closeout, review decisions, transition proposal, and handoff
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

- `tasks/reference/RECOVERY-PROTOCOL.md` for beginner-safe recovery
- `tasks/reference/STATE-MANAGEMENT-PROTOCOL.md` when active state, precedence, or freshness is unclear
- `tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md` when context is overloaded, stale, or unsafe
- `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md` for advisory cleanup boundaries around logs, caches, generated reports, and protected evidence
- `tasks/reference/MEMORY-PROTOCOL.md` for reviewed memory cards and promotion paths
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

## What The Main Surfaces Do

| Area | Files or families | Plain-English role |
|---|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` | What every agent starts from. |
| Beginner education | `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`, `PRECODE-USER-GUIDE.md`, `CLAUDE-CODE-FIELD-GUIDE.md` | How to work with Precode in practice. |
| Product direction | `PRODUCT.md`, Goal Frames, `tasks/prds/*.md`, `FEATURES.md` | What should exist, for whom, and why. |
| Technical project rules | `PROJECT-CONTEXT.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `CODEBASE-GUIDE.md` | Where implementation facts belong. |
| Current work | `tasks/beads/*.md` | One scoped execution contract at a time. |
| Protocols | `tasks/reference/*.md` | Durable playbooks for discovery, intake, PRDs, planning, routing, execution, proof, recovery, and handoff. |
| Modes and adapters | `modes/*.md`, `adapters/*.md`, shims | Tool-neutral roles plus tool-specific compatibility. |
| Scripts | `scripts/*` | Validation, state compilation, check recording, health, handoff, and advisory guardrails. |
| Reviewed memory | `memory/cards/*.md` | Reusable reviewed lessons, preferences, risks, glossary terms, and source pointers; evidence only. |
| Generated evidence | `PRECODE-HELP.md`, `OS-HEALTH.md`, `PROGRESS.md`, `logs/*` | Snapshots, warnings, output, sidecars, and handoff context; never active memory. |

## Where To Go Next

| Need | Read next |
|---|---|
| "I am new and need to understand how software gets built with agents." | `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` |
| "I am operating a Precode project and need prompts, steps, and stop rules." | `PRECODE-USER-GUIDE.md` |
| "I am using Claude Code in a first session or bootcamp-style setting." | `CLAUDE-CODE-FIELD-GUIDE.md` |
| "I need the full file dictionary and technical map." | `PRECODE-FILE-INVENTORY.md` |
| "I am reviewing architecture, trust boundaries, generated sidecars, validators, limitations, or maintainer detail." | `PRECODE-ARCHITECTURE-OVERVIEW.md` |
| "I need Precode's philosophy and public positioning." | `PRECODE-MANIFESTO.md` |

## Adapting Precode To Your Project

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

Use `PRECODE-ARCHITECTURE-OVERVIEW.md` when you need:

- the full layer-by-layer architecture
- script and validator internals
- generated sidecar and log taxonomy
- trust boundaries and prompt-injection posture
- maintainer procedures
- public fork guidance
- comparison landscape
- limitations and adoption path

This README is the beginner-first map. The architecture overview is the maintainer and reviewer companion.

Maintainer-local document history for this explainer lives in `_maintainer/CHANGELOG.md`; it is not part of normal public package navigation.
