# Precode OS Explainer
<!-- ANCHOR: os-readme -->

> AUTHORITY: Beginner-first canonical explainer for what Precode OS is, why it exists, how a non-technical builder should use it, and where to find deeper architecture or maintainer detail.
> NOT_AUTHORITY: Product requirements, active task selection, route structure, schema definitions, pricing decisions, generated progress state, or deep architecture ownership.
> LOAD_WHEN: Onboarding a non-technical builder, explaining the Precode OS workflow, or choosing which deeper Precode reference to read next.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.6.3
Last updated: 2026-04-28

Precode OS is a repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift.

In plain English: Precode lives inside your project folder, keeps important project truth in readable Markdown files, and uses small scripts to check whether the agent is staying aligned.

For Precode's philosophical anchor, values, and principles for the new builder class, read `PRECODE-MANIFESTO.md`.

For deeper architecture, maintainer, validator, script, generated-sidecar, and forking details, read `PRECODE-ARCHITECTURE-OVERVIEW.md`.

For a technical dictionary of Precode OS files and file families, read `PRECODE-FILE-INVENTORY.md`.

For a beginner bridge from "I have an idea" to understanding how software is planned, built, verified, deployed, and learned from with Precode and AI coding agents, read `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`.

---

## 100 / 200 / 300 Explainer

### 100

Precode OS helps a non-technical builder use AI coding agents without losing control of the project. It keeps the agent focused on one approved task, makes every important fact live in the right file, and requires evidence before work is treated as done.

### 200

Precode OS gives AI-assisted software work a tiny active memory, one current task, one primary authority file, and checks that prove whether the work stayed aligned. Instead of asking an agent to remember the whole project, Precode keeps the current truth small, readable, and reviewable. Ideas become PRDs, PRDs become small execution beads, and beads produce recorded evidence.

### 300

Precode OS is a repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift. Its philosophy is that AI work becomes safer when memory is small, authority is explicit, tasks are sliced into verifiable units, generated reports are demoted, and transitions require human approval. Markdown remains the human-readable authority layer, while scripts compile state, validate drift, record checks, refresh health reports, and preserve handoff continuity across sessions and agents.

## Why Precode Exists

AI coding agents are powerful, but they tend to move faster than a solo builder can track. That is especially risky when the builder is non-technical and cannot easily tell whether the agent changed the right thing, proved the change, or quietly expanded the project.

Precode exists to give the repo a simple operating memory:

- what the agent should remember
- what task is active right now
- what file owns the truth for that task
- what the agent must not do yet
- what evidence proves the work is done
- what needs human approval before moving forward

The most important rule is simple:

> Active memory stays tiny.

Only three files are active memory:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Everything else is loaded only when needed.

## Precode Philosophy

Precode OS does not assume the safest AI workflow is more autonomy, more prompt, or more context. It assumes safer AI work comes from smaller active memory, clearer file ownership, one approved task at a time, human approval gates, and recorded evidence.

Other approaches can be useful:

| Approach | What it optimizes for | Precode's stance |
|---|---|---|
| Large prompt files | Give the agent more instructions up front. | Keep always-loaded memory small and load references only when relevant. |
| Chat-only workflows | Move quickly through conversation. | Preserve durable repo-owned state so work survives sessions and tools. |
| Autonomous agents | Let the agent plan and execute more independently. | Let agents propose; humans approve task transitions and sensitive work. |
| Project-management-heavy systems | Coordinate many tasks, roles, and backlogs. | Keep one active bead and avoid turning `tasks/todo.md` into a roadmap. |
| Spec-first systems | Define work before implementation. | Use PRDs when needed, then govern execution with beads, checks, and closeout. |

Precode is for builders who want speed without giving up control of scope, product direction, or proof of done.

## Common Vibe-Coding Failure Modes

These risks come from three places: the AI coding agent, the human operator, and the OS/tooling layer.

### AI Coding Agent Failure Modes

| Failure mode | What it looks like | How Precode addresses it |
|---|---|---|
| Scope creep | The agent adds extra features, rewrites more than asked, or follows an adjacent idea. | One active bead, files in play, out-of-scope rules, checkpoint, and closeout. |
| Stale context | The agent follows old notes, previous chat claims, or outdated plans. | Three active-memory files, authority contracts, and context-loading rules. |
| Hallucinated certainty | The agent says the work is done because it sounds plausible. | Recorded checks, Closeout Evidence, manual verification, and review decision. |
| False done | Tests/checks are skipped, vague, or not tied to the bead. | Verification protocol, `record-check.sh`, OS Health warnings, and stable manual verification format. |
| Generated summaries become instructions | Health reports, diaries, or imported summaries start driving the next task. | `CLASS: generated`, demotion language, reviewed memory cards, and promotion paths into owner files. |
| Too much memory | The agent loads everything and loses the current task. | Tiny active memory and conditional reference loading. |
| Hidden product drift | A small request turns into a product direction change. | PRD gate, intent orchestration, decisions log, and user approval. |
| Multi-agent handoff confusion | A new tool starts with a different understanding. | Shared command surface, thin adapters, handoff script, and generated handoff packet. |
| Blocked work pretends to continue | The agent codes around missing input, dashboard setup, or approval. | Stop conditions, blocked escape, manual testing state, and unblocker paths. |
| Uncontrolled next-task momentum | The agent finishes one task and starts the next without review. | Review decision plus user-approved bead transition only. |

### Human Operator Failure Modes

| Failure mode | What it looks like | How Precode addresses it |
|---|---|---|
| File structure damage | A user moves or renames Markdown files that scripts and agents expect. | File inventory, validation, and user-guide hard rules. |
| Direct generated-report edits | A user edits `OS-HEALTH.md`, `PROGRESS.md`, or `logs/*.md` by hand. | Generated-output demotion and regeneration scripts. |
| Wrong owner-file edits | Decisions, requirements, backlog, or architecture notes land in the wrong file. | Authority contracts and one-owner-per-fact guidance. |
| Casual approvals | Next-bead transitions, sensitive work, or review decisions are approved too quickly. | Explicit human gates and closeout evidence. |
| Secret leakage | Tokens, credentials, dashboard values, or private notes are pasted into docs or logs. | Security and memory protocols prohibit storing secrets. |

For practical beginner rules, including "do not move, rename, or directly edit Precode files," use `PRECODE-USER-GUIDE.md`.

### OS And Tooling Failure Modes

| Failure mode | What it looks like | How Precode addresses it |
|---|---|---|
| Stale generated reports | Health, diary, or audit output lags behind recent evidence. | State freshness checks and scheduled audit refreshes. |
| Missing telemetry | Spend, GitHub, CI, or external status is unavailable. | Unknown is reported as unknown, not guessed. |
| Validator coverage gaps | A rule is documented but not fully enforceable yet. | Advisory checks plus human review. |
| Tool unavailable | `git`, `gh`, CI, deployment, or network access is missing. | Read-only audits degrade to not configured. |
| Non-git checkout limits | Git status and branch checks cannot run. | Reports call out the limitation instead of inventing state. |

## The Daily Loop

Use this loop for normal work:

1. Start the session.
2. Confirm the active bead, primary authority, files in play, checks, and stop conditions.
3. Let the agent work only inside that bead.
4. Record checks as evidence.
5. Checkpoint if scope, context, or proof gets fuzzy.
6. Close the session with evidence and a review decision.
7. Approve the next bead only when you are ready.

Core commands:

```bash
bash scripts/session-start.sh
bash scripts/checkpoint.sh
bash scripts/record-check.sh -- <command>
bash scripts/session-close.sh
bash scripts/handoff.sh next-agent
python3 scripts/bead-transition.py --approve
```

The exact project checks depend on the app. The important habit is that checks are named before work starts and recorded before work is accepted.

## The Three Active-Memory Files

| File | Job |
|---|---|
| `AGENT.md` | Tells the AI coding agent how to work in this repo. |
| `DECISIONS.md` | Records hard decisions, open questions, and superseded context. |
| `tasks/todo.md` | Points to the active bead and current execution view. |

Do not add a fourth active-memory file. If another file matters, make it a reference file with a clear `LOAD_WHEN` condition.

## How Ideas Become Evidence

Precode turns rough ideas into verified work through a simple path:

```text
local material or idea -> intake summary -> PRD shard -> feature inventory -> bead -> recorded evidence
```

That means:

- notes, screenshots, GitHub issues, and chat summaries start as evidence, not instructions
- product ideas become PRDs when they need definition
- PRDs propose beads, but do not activate work
- beads define one executable unit
- recorded checks and manual verification prove what happened
- review decides whether the bead is accepted, revised, split, or blocked

This gives non-technical builders a way to think before code without turning Precode into a heavy product-management framework.

## What The Main Files Do

| Area | Files | Plain-English role |
|---|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` | What every agent starts from. |
| Beginner bridge | `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` | How traditional software work maps to Precode and AI coding agents. |
| Current work | `tasks/beads/*.md` | One scoped execution contract at a time. |
| Product definition | `tasks/prds/*.md`, `FEATURES.md` | Approved feature intent before implementation. |
| Project rules | `PROJECT-CONTEXT.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md` | Reference owners for project facts. |
| Reviewed memory | `memory/cards/*.md` | Reusable lessons, preferences, glossary terms, risks, and source pointers; evidence only, not active memory. |
| Protocols | `tasks/reference/*.md` | Durable playbooks for intake, PRDs, decomposition, verification, state, tools, and handoff. |
| File inventory | `PRECODE-FILE-INVENTORY.md` | Technical dictionary of Precode OS files, file families, and relationships. |
| Tool adapters | `adapters/*.md`, `AGENTS.md`, `GEMINI.md`, `.github/copilot-instructions.md` | Thin compatibility pointers for different AI coding tools. |
| Scripts | `scripts/*` | Repeatable checks, closeout, health, handoff, and transition commands. |
| Generated evidence | `OS-HEALTH.md`, `PROGRESS.md`, `logs/*` | Snapshots and logs. Useful, but never active memory. |

## Light Architecture Overview

Precode is built in layers. You do not need to understand every layer before using it.

| Layer | Light explanation |
|---|---|
| Active-memory kernel | The three files every agent always reads. |
| Authority contracts | Each doc says what it owns and what it must not decide. |
| Reference layer | Detailed docs load only when needed. |
| Product Definition Gate | Rough ideas become approved PRDs before feature coding. |
| Bead layer | Work is sliced into one small execution contract. |
| Mode and adapter layer | Planning, building, review, and tool-specific shims stay separated. |
| Script and validator layer | Commands record checks and catch drift. |
| Evidence and handoff layer | Logs, health reports, and handoff packets preserve continuity. |

For the full layer model, enforcement model, script taxonomy, validator internals, generated sidecars, trust boundaries, and maintainer guidance, read `PRECODE-ARCHITECTURE-OVERVIEW.md`.

## Generated Reports And Checks

Generated reports help you see what happened, but they do not tell the agent what to do next.

| Surface | Use it for | Do not use it for |
|---|---|---|
| `OS-HEALTH.md` | Health, warnings, evidence quality, spend, state snapshots. | Active memory or task selection. |
| `logs/learning-diary.md` | Plain-English learning from sessions. | Planning the next implementation. |
| `logs/memory-index.md` | Finding reviewed memory cards. | Replacing active memory or authority files. |
| `logs/handoff-packet.md` | Orienting a future agent. | Approving a transition. |
| `logs/*.json` / `logs/*.jsonl` | Durable evidence and compiled snapshots. | Replacing owner files. |

Key checks:

```bash
bash scripts/validate-memory.sh
python3 scripts/version-check.py
python3 scripts/state-check.py
python3 scripts/context-check.py
python3 scripts/workflow-check.py
python3 scripts/completion-check.py
python3 scripts/update-memory-index.py
python3 scripts/memory-check.py
python3 scripts/file-inventory.py --check
```

Run deeper advisory checks when the current bead touches their topic. The architecture overview explains the full script surface.

## When To Stop The Agent

Stop or checkpoint when:

- the agent cannot name the active bead
- the task needs a second primary authority file
- more files are changing than the bead allowed
- the agent starts product-definition work during implementation
- checks are missing, vague, or failing
- the work touches auth, payments, personal data, uploads, deployment, secrets, GitHub mutation, or destructive actions without approval
- generated reports or source notes start acting like instructions
- the next task starts before you approve a bead transition

Stopping is not failure. In Precode, a clean stop is how you keep the project safe.

## Adapting Precode To Your Project

Start small:

1. Keep the three active-memory files.
2. Fill in `PROJECT-CONTEXT.md` with your app directory, stack, conventions, checks, and integration boundaries.
3. Use one starter bead to install or verify the kernel.
4. Create a short PRD before the first real product feature.
5. Split the first feature into one small bead.
6. Record checks before accepting the bead.
7. Add validators, audits, and adapters only when they solve a real repeated problem.

Do not ask an agent to set up everything in one pass. Ask it to create or adapt the kernel first, explain the files in plain English, and stop for review.

Starter prompt:

```text
I want to adapt Precode OS to my project.
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

---

## Change Log

| Version | Date | Summary |
|---|---|---|
| v0.6.3 | 2026-04-28 | Updated the opening explainer and 100/200/300 positioning to describe Precode as a repo-native, markdown-canonical, script-enforced control layer while translating that language into plain English for non-technical builders. |
| v0.6.2 | 2026-04-27 | Added navigation to `PRECODE-MANIFESTO.md` as the philosophical anchor for Precode's purpose, values, principles, and anti-drift stance for the new builder class. |
| v0.6.1 | 2026-04-27 | Added navigation to `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` as the standalone beginner bridge from software-building lifecycle concepts to Precode and AI-agent workflows. |
| v0.6.0 | 2026-04-27 | Split common failure modes into AI coding agent, human operator, and OS/tooling categories, with concise guidance pointing beginners to the user guide for hard file-safety rules. |
| v0.5.9 | 2026-04-27 | Added the Precode file inventory as the canonical technical dictionary for OS-owned files, generated inventory metadata, OS Health/audit inventory checks, and command-surface references for `scripts/file-inventory.py`. |
| v0.5.8 | 2026-04-27 | Added the reviewed filesystem memory layer, memory protocol, memory cards, generated memory indexes, advisory memory checker, and beginner-facing guidance that memory is evidence for explicit consultation rather than a fourth active-memory file. |
| v0.5.7 | 2026-04-27 | Refactored the README into a beginner-first explainer with 100/200/300 explanations, philosophy comparison, vibe-coding failure modes, light architecture notes, and pointers to the architecture overview for deeper maintainer and implementation detail. |
| v0.5.5 | 2026-04-26 | Added the System Design Pattern Protocol, advisory pattern checker, generated pattern guidance sidecar, OS Health and scheduled audit pattern warnings, and beginner guidance for choosing direct changes, adapters, state flows, strategy boundaries, auth/access boundaries, and audit trails. |
| v0.5.4 | 2026-04-26 | Added the Session Completion and Handoff Protocol, advisory completion checker, generated handoff packet sidecars, OS Health and scheduled audit completion warnings, and clearer session-close diagnostics. |
| v0.5.3 | 2026-04-26 | Added the Long-Horizon Planning Protocol, advisory long-horizon checker, generated long-horizon map sidecar, OS Health and scheduled audit long-horizon warnings, and user guidance for reviewing future work without expanding active memory. |
| v0.5.2 | 2026-04-26 | Added the Workflow Selection Protocol, advisory workflow checker, generated workflow map sidecar, OS Health and scheduled audit workflow warnings, and beginner guidance for choosing the right Precode path before work starts. |
| v0.5.1 | 2026-04-26 | Added the Tool Execution Protocol, non-check tool-run logging, advisory tool-execution checker, OS Health and scheduled audit tool warnings, and user guidance distinguishing tool use from verification evidence and risky-action approval. |
| v0.5.0 | 2026-04-26 | Added the Intent Orchestration Protocol, advisory orchestration checker, generated orchestration map sidecar, OS Health and scheduled audit intent warnings, and prompt/user guidance for changed intent and idea-to-evidence traceability. |
| v0.4.9 | 2026-04-26 | Added the Context Engineering Protocol, Prompt Patterns reference, compact Context Pack guidance for session start and handoff, source-trust and prompt-injection guardrails, and an advisory context checker. |
| v0.4.8 | 2026-04-26 | Added the State Management Protocol with memory and state ownership, precedence rules, freshness expectations, recovery workflow, log/archive guidance, OS Health state-integrity output, scheduled audit state warnings, and an advisory state checker. |
| v0.4.7 | 2026-04-26 | Added the Decomposition Protocol with bead decomposition tests, not-a-bead-yet criteria, slicing patterns, dependency mapping terms, planning-versus-execution boundaries, appetite guidance, OS Health decomposition quality output, scheduled audit decomposition warnings, and an advisory decomposition checker. |
| v0.4.6 | 2026-04-26 | Added the Verification Guardrail Protocol with verification tiers, evidence-quality expectations, sensitive-surface gates, manual verification format, rollback expectations, false-done warning patterns, OS Health verification quality output, scheduled audit verification warnings, and an advisory verification checker. |
| v0.4.5 | 2026-04-26 | Added the Extension Protocol so adapters, protocols, importers, audits, generated reports, bead templates, and external integrations can be added without expanding active memory. Added a project extension listing area, generated output rules for extension evidence, and an advisory extension-boundary checker. |
| v0.4.4 | 2026-04-26 | Added GitHub as a read-only integration surface with a GitHub protocol, repository and CI audit helper, issue/PR source intake helper, GitHub Actions validation workflow, and generated evidence boundaries for GitHub-derived status and planning inputs. |
| v0.4.3 | 2026-04-26 | Added opt-in scheduled audit guidance for safe local and external read-only status checks, including health refresh, memory validation, stale bead detection, closeout completeness, generated-report demotion, learning diary refresh, spend telemetry, blocked work, GitHub/CI/deployment/monitoring status, and generated audit outputs. |
| v0.4.2 | 2026-04-25 | Added native Local Source Intake guidance so local notes, docs, screenshots, chat summaries, issue exports, research files, diagrams, and manual drafts can feed PRD-ready source summaries without becoming authority or active memory. |
| v0.4.1 | 2026-04-25 | Clarified that `PRECODE-OS-README.md` is the canonical explainer and removed the separate `Explainer.md` so the OS has one narrative entrypoint instead of two overlapping explainer surfaces. |
| v0.4.0 | 2026-04-25 | Shifted the explainer to reflect the next architectural step: markdown stays canonical for intent, decisions, PRDs, and beads, while the highest-churn operational fields move into structured frontmatter, stable section schemas, and generated sidecars. Documented bead and todo frontmatter, compiled readiness (`logs/readiness.json`), a stronger machine-readable authority map (`logs/authority-map.json`), generated adapter and shim indexes, a thin event/state stream (`logs/os-events.jsonl`), and the rule that all generated reports remain non-authoritative. |
| v0.3.1 | 2026-04-18 | Updated the adapter and shim guidance after adding universal/tool auto-discovery surfaces: `AGENTS.md`, `GEMINI.md`, and `.github/copilot-instructions.md`. Clarified that these files are compatibility pointers, not alternate shared operating models. Documented the normalized adapter command surface, the validator's canonical adapter command check, and regression coverage that fails if an adapter drops a required command. |
| v0.3.0 | 2026-04-18 | Updated the explainer to reflect the latest Precode OS loop changes: learning promotion in closeout, generated OS health reports (`OS-HEALTH.md` and `logs/os-health.json`), more diagnostic bead closeout fields, a blocked-bead escape hatch, and loop metrics for checks, session starts, checkpoints, closes, handoffs, and spend. Clarified that health reports and metrics are generated evidence, not active memory. |
| v0.2.0 | 2026-04-16 | Renamed this explainer from `OS-README.md` to `PRECODE-OS-README.md` and added document versioning. Captured the PRD-layer design conversation: deep research pointed toward a Product Definition Gate rather than a giant active-memory PRD; the user clarified that the gate should be public/generic Precode OS first, apply to every feature, serve solo non-technical builders, keep `FEATURES.md` as the compiled inventory, and use adaptive ceremony by risk. Added Layer 3.5, PRD shard rules, PRD protocol, PRD template, PRD-to-`FEATURES.md` compilation, bead `Parent PRD` and `Requirement IDs` traceability, and validator/test coverage. |
| v0.1.0 | 2026-04-15 | Initial Precode OS explainer covering tiny active memory, authority contracts, product and system reference files, execution beads, modes, adapters, safety rules, scripts, validators, logs, handoffs, public fork guidance, and the minimal reusable OS pattern. |
