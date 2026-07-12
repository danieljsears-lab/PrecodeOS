# PrecodeOS
<!-- ANCHOR: readme -->

> AUTHORITY: Public GitHub landing page, beginner-first orientation, quickstart, and curated navigation for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, generated evidence, implementation status, package update behavior, or maintainer-private roadmap authority.
> LOAD_WHEN: A user, contributor, reviewer, or AI assistant needs the public package compass before choosing a more specific PrecodeOS guide or protocol.
> CLASS: reference

[![Precode Validate](https://github.com/danieljsears-lab/PrecodeOS/actions/workflows/precode-validate.yml/badge.svg)](https://github.com/danieljsears-lab/PrecodeOS/actions/workflows/precode-validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

## What It Is

Learn more: `https://www.precodeos.org`.

PrecodeOS is an AI anti-drift "Builder OS" for solo software builders using AI coding agents. 

PrecodeOS brings proven engineering discipline, practices and patterns to AI-assisted building without asking a non-technical builder to become an engineering manager. It keeps the repository clear about intent, scope, proof, approval, and recovery, so any coding agent has safer rails to work inside.

It feels like a small, powerful and opinionated operating system for supporting AI-assisted development workflow: it shows what matters, what is active, what is proven, and when to stop. 

PrecodeOS keeps its active AI-agent context to 219 lines across three files. Yep, it's super tiny.

PrecodeOS cares about:

- stopping shallow "vibe" work from becoming production code
- turning vague intent into explicit artifacts
- preserving parked intent in a Candidate Queue without turning it into active work
- giving the agent bounded context
- making the next safe action legible
- using review as more than rubber-stamping
- preserving cross-session continuity
- making AI development repeatable enough that a non-technical solo builder can trust it

## How It Works

PrecodeOS is a repo-native control layer for AI coding work. 

It uses build loops, bead contracts, recorded checks, advisory loop health, closeout evidence, and human-gated transitions to keep agentic iteration grounded, recoverable, and inspectable.

It lives inside a repository as Markdown owner files, execution contracts, validation scripts, compilers, generated evidence, and thin AI-tool adapters. It does not replace Codex, Claude, Cursor, Copilot, Gemini, or other coding agents, and it does not run the agent; you run the agent.

Taken together, those files form an advisory repo-native harness for agentic work: owner files, protocols, scripts, generated sidecars, recorded checks, adapters, and transparent command facades make the work inspectable without becoming approval authority. The harness is not an agent runtime, sandbox, command approval layer, registry, optional pack, package manager, install/update system, or enforcement layer.

Technically, PrecodeOS is a markdown-canonical, script-enforced governance kernel underneath fast AI workflows. It keeps software work human-owned by making intent, scope, authority, approval, proof, and recovery explicit repo surfaces instead of hidden chat assumptions.

PrecodeOS treats product intent, design judgment, acceptance, and proof as durable repo-owned control surfaces for AI coding work. The agent can move quickly, but the reasons for the work, the bounds of the work, and the evidence for accepting it stay readable in the repository.

## Who It's For

PrecodeOS is for solo builders who want the speed and capability of AI coding agents without relinquishing control of the project to the agent.

It helps builders, especially non-technical builders, create production-grade software by preserving project truth: what is active, what is authoritative, what changed, what was proven, who approved the next step, and how to recover when the thread gets lost through structured context and persistent artifacts.

Its core differentiators are tiny active memory, explicit authority ownership, one current execution unit, recorded evidence, advisory next-step guidance, file-scope guardrails, and human-gated transitions.

## The Problem(s) It Addresses

AI coding agents are fast, powerful and easy to use, but their failure modes are common and predictable:

- scope quietly widens, drift quietly occurs, hallucinations happen
- stale chat or file context overrides current intent
- generated summaries or reports become instructions
- the agent claims work is done without enough proof
- the next task starts before the user approves it
- handoff state gets lost between sessions or tools
- sensitive work gets treated like ordinary implementation

PrecodeOS matters because AI coding agents can move faster than a builder can understand, verify, and recover from (especially a non-technical builder). It addresses those failure modes by making the important boundaries explicit. 

Project intent and truth is fragile. PrecodeOS prevents and controls for quiet unseen AI drift. It is AI anti-drift.

## When To Use PrecodeOS

PrecodeOS is worth it when the cost of getting lost is bigger than the cost of adding structure.

| Use PrecodeOS when...                                        | Skip it when...                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| You are building a real product, multi-page app, or MVP you expect to keep improving. | You are making a quick sketch, tiny demo, or throwaway experiment. |
| The idea is fuzzy and needs to become buildable instructions. | You already know the exact change and it is small, obvious, and low-risk. |
| AI needs to remember decisions across multiple steps, sessions, or files. | You only need one quick task and drift would not really matter. |
| You want checkpoints because mistakes, regressions, or confusion would be painful. | Mistakes are cheap and you are comfortable moving fast without much process. |
| Future-you, another human, a client, or another agent will need to understand what happened. | It is just you for an hour and there is nothing worth preserving. |

**The bright line**: quick sketches, tiny demos, and throwaway experiments can stay loose. Switch to PrecodeOS when the work is durable, user-facing, sensitive, multi-file, hard to prove, or something you expect to revisit. If a mistake would be expensive to understand, undo, explain, or trust later, do not let vibe coding harden into production code.

## Technical Summary

PrecodeOS treats the repository as the control surface for AI-assisted software work. Its core architecture is built around a few invariants:

- **Tiny active memory:** only the minimum files needed to start the current session are always loaded.
- **One active unit of work:** the current task is represented by a bead contract, not by chat momentum.
- **One owner per durable fact:** product, architecture, API, data, security, and acceptance truth live in explicit owner files.
- **Design judgment before code:** product intent, acceptance, and proof expectations are written down before AI speed turns weak understanding into implementation.
- **Evidence over confidence:** checks and closeout evidence matter more than agent claims.
- **Generated output is not authority:** reports summarize state, but they do not choose work or approve completion.
- **Human approval at transitions:** agents can propose; humans approve direction, acceptance, sensitive actions, and task transitions.
- **Tool-neutral core:** AI-tool-specific files are adapters, not separate operating systems.

That is the line PrecodeOS holds: a lightweight governance kernel for agentic development that determines how agents can inspect, draft, build, explain, and propose, while the builder remains the authority for direction, risk, acceptance, and the next approved step.

## How It Works In Practice

PrecodeOS gives AI-assisted work a shared operating model. It uses repeated working "build loops" to keep the agent pointed at one bounded "bead" contract at a time (smallest logical unit of work to prevent scope creep).

It uses tiny active memory to prevent stale context, forces authority into named repo files, records durable evidence as proof (instead of trusting agent claims), and requires the human to approve transitions. It uses generated reports to help the builder see what is going on and to inspect health.

Ralph-style iteration is opt-in and bounded by the active bead. 

`CANDIDATE-QUEUE.md` is the user-facing place for parked intent: ideas, research leads, stale or blocked candidates, PRD candidates, product-value ratings, themes, and near-bead sketches. It says, "Here are intents we have not lost, with enough evidence/status to decide what, if anything, deserves promotion." It is upstream of PRDs and beads. It is not active memory, not a product backlog, not task selection, and not permission to code. `python3 scripts/candidate-queue.py` can preview raw-note import or shaping proposals, but apply requires explicit `--approve-action` and may write only to `CANDIDATE-QUEUE.md`.

When an idea needs shaping into future work, use the Plan Mode Candidate Craft Loop: `Idea -> Plan Mode -> Candidate Queue -> Plan Mode -> Implementation Plan -> Approved Bead -> Build`. In Codex, use `/plan`; in Claude Code, use Plan Mode; in other agents, use an equivalent read-only planning mode. Plan Mode is required before developing a Candidate Queue entry and again before developing an implementation plan for a selected candidate. Plan Packets, queue entries, and implementation plans are evidence only until the normal PRD, owner-file, decomposition, and approval gates are satisfied.

## What You Can Build

- MVPs with clearer product intent before code.
- Existing projects with safer agent boundaries.
- Multi-session agent work with durable handoff.
- Founder or student projects that need structure without heavyweight process.
- Product discovery, PRDs, small execution beads, and recorded proof.

## Why It Exists

| Layer | What it gives you |
|---|---|
| Active Memory | A tiny current starting point. |
| Authority | One owner for each durable fact. |
| Product Context | Product and project truth outside chat. |
| PRDs | A destination before feature work. |
| Beads | One bounded unit of execution. |
| Checks | Proof over agent confidence. |
| Reports | Readable status and graph visibility without authority drift. |
| Recovery | A way to stop, repair, and resume. |

The active-memory kernel limits startup context. Authority contracts show what each file owns and must not own. Beads constrain execution to one current unit of work. Recorded checks turn proof into durable evidence. Generated reports improve visibility without becoming authority. Human gates preserve ownership of risk, acceptance, and transitions.

## Quickstart Install

Clone the public repository and run the first memory check:

```bash
git clone https://github.com/danieljsears-lab/PrecodeOS.git
cd PrecodeOS
bash scripts/validate-memory.sh
```

Optional local command facade:

```bash
python3 scripts/precode_cli.py --help
python3 scripts/precode_cli.py validate
```

For a local editable console command, run `python3 -m pip install -e .` from the package checkout, then use `precode --help`. The `precode` command is only a curated wrapper over documented repo scripts. It prints the underlying command before running it, preserves exit codes, and does not approve tasks, setup, transitions, releases, package updates, or generated evidence as authority.

The optional facade, generated router output, run-contract sidecars, and recorded-check ledger are part of PrecodeOS's advisory harness contract. They make boundaries visible for humans and agents, but Markdown owner files, protocols, active beads, recorded proof, and explicit human gates remain the source of authority.

Before copying PrecodeOS into another project, run Bootstrap Confidence against the package checkout and the target folder. For empty or nearly empty targets, use the supervised setup plan and apply only explicitly approved copy action IDs:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID>
```

The apply mode is deliberately narrow: it copies only approved setup-plan copy actions and does not adapt owner files, overwrite target material, install hooks, change CI, run app commands, write app code, install a CLI, provide package-manager behavior, define release channels, or automate rollback.

For existing projects, run Existing Repo Intake first, then use the adaptation plan only as a non-mutating checklist:

```bash
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <target-project-root>
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --existing-project-adaptation-plan
```

For existing Precode targets, use upgrade preview before any package repair or update copy. Only missing package-owned files marked `review_package_copy_candidate` can be copied, and only by approved action ID:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --upgrade-preview
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>
```

If setup is partial or confusing, use recovery guidance. It is diagnostic only and does not automate rollback, destructive cleanup, dirty-file overwrites, hooks, CI, release channels, or package-manager behavior:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --recovery-guidance
```

To adapt PrecodeOS into a target project, start with these files:

- `docs/PRECODE-GUIDED-SETUP.md` for the step-by-step setup path and copy boundaries.
- `PRODUCT.md` for the product promise, users, strategy, bets, success signals, and voice.
- `PROJECT-CONTEXT.md` for stack, app directory, conventions, checks, and integration boundaries.
- `DECISIONS.md` for hard decisions and open questions.
- `tasks/todo.md` for the active work pointer.

Do not add more active-memory files. If a topic needs durable detail, give it a clear owner file or use the existing reference map.

## Start Here

This README is the public package compass: use it to decide whether PrecodeOS fits, how to adopt it, and which canonical document to open next. It is not the daily operating surface once work has started.

Use this first-reader route and stop at the first surface that matches your situation:

1. If PrecodeOS is not installed in the target project, use [`PRECODE-GUIDED-SETUP.md`](docs/PRECODE-GUIDED-SETUP.md).
2. If PrecodeOS is installed or you are already working in a PrecodeOS repo, use [`PRECODE-DAILY-COCKPIT.md`](docs/PRECODE-DAILY-COCKPIT.md) as the practical first working surface.
3. If you only have a rough idea, still start from the Daily Cockpit and use `Ideation: use First PRD Walkthrough for my rough idea.`
4. If setup, state, checks, or generated reports feel broken or confusing, use [`PRECODE-TROUBLESHOOTING.md`](docs/PRECODE-TROUBLESHOOTING.md) or say `I am stuck, help me.`

Do not read the docs as competing start pages. `README.md` is the compass, Guided Setup is setup only, Daily Cockpit is the normal stop-here operating surface, User Guide is the annex/manual, OS README is the concept explainer, Troubleshooting is symptom lookup, and Support Runbook is helper-facing.

For students, the practical path is the Daily Cockpit path: `Idea -> Brief -> Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close`, then `Active -> Changed -> Proven -> Parked -> Approval -> Next` after the first bead. Use Release Readiness only when user-facing shipping risk appears; it prepares evidence and approval questions, not deployment action.

If you prefer a browseable reading surface with progress cues, section links, and source Markdown links, open [`docs-html/index.html`](docs-html/index.html). The Markdown docs remain canonical.

For PRD review, use [`tasks/prds-html/index.html`](tasks/prds-html/index.html) as a generated scan surface for status, requirements, blockers, risks, and bead proposals. Generated PRD pages may include an export-only Acceptance Oracle Matrix cockpit for drafting a proposed Markdown replacement block, but Markdown PRDs in [`tasks/prds/`](tasks/prds/) remain canonical and must be edited manually. Acceptance criteria may use optional EARS-style wording when it clarifies expected behavior; the syntax is not required and generated HTML does not approve or persist it.

For parked ideas and future candidate visibility, use [`CANDIDATE-QUEUE.md`](CANDIDATE-QUEUE.md) with [`CANDIDATE-QUEUE-PROTOCOL.md`](tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md). A generated reading page is available at [`docs-html/CANDIDATE-QUEUE.html`](docs-html/CANDIDATE-QUEUE.html), and public users can refresh it with `python3 scripts/docs-html.py`, but the Markdown queue remains canonical. Candidate ranking is review order only; it does not choose what the agent builds next, approve PRDs, activate beads, or reserve bead IDs.

For stable documentation questions, ask your agent to `Use Ask Precode.` The prompt lives in [`PROMPT-PATTERNS.md`](tasks/reference/PROMPT-PATTERNS.md) and tells the agent to answer from public docs and relevant protocols with source citations. Ask Precode is conditional docs help, not a start page. If the question depends on current project state, Ask Precode should stop and route you to the right workflow instead.

Begin in the project repo that contains your app and PrecodeOS files. Open the Daily Cockpit, run `bash scripts/session-start.sh`, make the agent check the active bead, and only then approve work. If you only have a rough idea, use `Ideation: use First PRD Walkthrough for my rough idea.` from the Daily Cockpit before PRD shaping or coding. If the idea becomes a future candidate or the candidate needs an implementation plan, enter Plan Mode first; do not let the agent turn a plan, queue entry, or implementation plan into permission to build. PrecodeOS is not an app to launch; it is the operating layer inside the repo you are building from.

If you are helping someone else adopt PrecodeOS, use [`PRECODE-SUPPORT-RUNBOOK.md`](docs/PRECODE-SUPPORT-RUNBOOK.md). It gives support engineers the first-call flow, setup posture, and handoff language.

If you are still learning what PrecodeOS is, use the compass below.

## How PrecodeOS Works

PrecodeOS keeps three small files as active memory:

- `AGENT.md` (99 lines of code)
- `DECISIONS.md` (37 lines of code)
- `tasks/todo.md` (83 lines of code)

Everything else is reference, template, evidence, adapter, archive, or generated output.

Normal work follows a simple path:

```text
orient -> decide -> plan -> build -> prove -> recover when needed
```

For implementation work, PrecodeOS uses beads: small execution contracts that name the current task, primary authority, files in play, checks, stop conditions, and proof needed.

For evidence, use recorded checks:

```bash
bash scripts/record-check.sh -- <command>
```

Generated reports such as `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md`, `logs/work-graph.md`, `logs/build-attribution-ledger.md`, and files under `logs/` are evidence only. They do not choose tasks, approve work, score contributors, or replace owner files. `OS-HEALTH.md` includes a Doctor Dashboard that explains warning sources, plain-English triage labels, owner commands, and repair paths while keeping `scripts/next-step.py` as the next-decision owner.

Raw reference files, notes, documents, screenshots, research, and links belong in `project-evidence/` when the project wants to keep them in the repo. They are evidence only until reviewed conclusions are promoted into owner files through Local Source Intake.

For the immediate "what now?" question, keep the command surface small:

```bash
python3 scripts/precode_cli.py --dry-run next
bash scripts/session-start.sh
python3 scripts/next-step.py
python3 scripts/loop-health.py
python3 scripts/os-health.py
bash scripts/record-check.sh -- <command>
```

Setup, support, and recovery commands such as `bootstrap-check.py`, `existing-repo-intake.py`, `validate-memory.sh`, `file-inventory.py --check`, `state-check.py`, `files-in-play-check.py`, `completion-check.py`, and `bead-transition.py --json` belong in Guided Setup, the Support Runbook, or Troubleshooting when the symptom calls for them. Advanced evidence and review commands such as task suitability, Ralph, Candidate Queue, attribution, team collaboration, PRD handoff, release readiness, proof tracing, and review lanes are conditional surfaces, not the beginner daily loop.

`precode_cli.py` and the optional `precode` console command are local facades over the canonical commands below. They are not required for normal use and do not replace Markdown owner files or underlying scripts. Command maps are reader guidance only; they do not approve work, choose tasks, change tool-call classes, or make generated output authoritative.

`session-start.sh` shows the Context Pack and the same Router Decision that `next-step.py` prints on its own. The router may name one next protocol to load and a rough context footprint, and its JSON shape is regression-covered for adapters and diagnostics, but it is generated guidance only.

`loop-health.py` checks whether the current build loop is focused, stoppable, closeable, evidenced, easy to steer, and free of obvious work-graph drift. It evaluates the loop, not the builder, and gives one advisory next move for reducing drift.

`task-suitability-check.py --check` reports advisory `continue`, `clarify`, `route`, `split`, `block`, or `stop` guidance when a request may be too vague, broad, proof-unclear, approval-gated, or not ready as one bead. It does not choose work, approve PRDs, activate beads, authorize implementation, accept review, approve commands, or create proof.

`os-health.py` refreshes `OS-HEALTH.md` and `logs/os-health.json`, including the Doctor Dashboard diagnostic summary. The dashboard is generated evidence only; it explains which existing warning source matters, gives a plain-English safe ask and do-not-approve warning, and points to the owner command or protocol.

`ralph-loop.py` is a bounded bead-attempt engine for testable work. Use it only when the active bead has clear checks and retry boundaries; its `logs/ralph-attempts.jsonl` and `logs/ralph-summary.md` outputs are generated evidence, not acceptance or transition approval.

## Project Map

| Area | What lives there |
|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` |
| User docs | `docs/*.md` |
| Project truth | `PRODUCT.md`, `PROJECT-CONTEXT.md`, root owner files |
| Work units | `tasks/prds/`, `tasks/prds-html/`, `tasks/beads/`, `tasks/templates/` |
| Protocols | `tasks/reference/`, including skill playbooks |
| Raw project evidence | `project-evidence/` |
| Agent surfaces | `modes/`, `adapters/`, shims, skill playbooks, and `.agents/README.md` for host-skill boundaries |
| Scripts | `scripts/` |
| Evidence | `logs/`, `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md` |

## Docs Compass

| If you need to... | Go to |
|---|---|
| Set up PrecodeOS in a project | [`PRECODE-GUIDED-SETUP.md`](docs/PRECODE-GUIDED-SETUP.md) |
| Help someone else adopt PrecodeOS | [`PRECODE-SUPPORT-RUNBOOK.md`](docs/PRECODE-SUPPORT-RUNBOOK.md) |
| Start or resume daily PrecodeOS work | [`PRECODE-DAILY-COCKPIT.md`](docs/PRECODE-DAILY-COCKPIT.md) |
| Learn the deeper operating manual after the cockpit points you there | [`PRECODE-USER-GUIDE.md`](docs/PRECODE-USER-GUIDE.md) |
| Understand the conceptual Builder OS model | [`PRECODE-OS-README.md`](docs/PRECODE-OS-README.md) |
| Learn how software work maps to AI agents | [`HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`](docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md) |
| Start from a rough idea | [`PRECODE-DAILY-COCKPIT.md`](docs/PRECODE-DAILY-COCKPIT.md), then `Ideation: use First PRD Walkthrough for my rough idea.` |
| Work with an agent right now | [`PRECODE-DAILY-COCKPIT.md`](docs/PRECODE-DAILY-COCKPIT.md) |
| Troubleshoot setup, state, checks, or generated reports | [`PRECODE-TROUBLESHOOTING.md`](docs/PRECODE-TROUBLESHOOTING.md) |
| Recover when state, scope, or proof feels wrong | [`PRECODE-USER-GUIDE.md`](docs/PRECODE-USER-GUIDE.md), then [`PRECODE-TROUBLESHOOTING.md`](docs/PRECODE-TROUBLESHOOTING.md) |
| Use Claude Code in a first-session or bootcamp setting | [`CLAUDE-CODE-FIELD-GUIDE.md`](docs/CLAUDE-CODE-FIELD-GUIDE.md) |
| Review architecture, trust boundaries, or limitations | [`PRECODE-ARCHITECTURE-OVERVIEW.md`](docs/PRECODE-ARCHITECTURE-OVERVIEW.md) |
| Find the exact public package owner file, script, protocol, skill playbook, or relationship | [`PRECODE-PACKAGE-FILE-INVENTORY.md`](docs/PRECODE-PACKAGE-FILE-INVENTORY.md) |
| Take a maintainer or contributor action | [`CONTRIBUTING.md`](CONTRIBUTING.md), [`GOVERNANCE.md`](GOVERNANCE.md), or [`TRADEMARK.md`](TRADEMARK.md) |

Do not start by browsing `tasks/reference/`. Protocols are loaded when the user guide, the README compass, active memory, or an agent prompt such as "use workflow selection" calls for one.

## For Reviewers And Contributors

PrecodeOS is designed to be inspectable:

- Markdown files hold human-readable authority.
- Scripts validate memory, version metadata, file inventory, public-repo hygiene, files in play, and completion evidence.
- GitHub Actions runs read-only validation on pushes and pull requests.
- Contribution policy is inbound = Apache-2.0.
- Maintainer review is required for governance, trademark, licensing, public positioning, active memory, core workflow semantics, generated-output demotion, and beginner-facing safety language.
- Trust-affecting semantic changes should use [`SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md`](tasks/reference/SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md) before implementation or merge.

Useful reviewer commands:

```bash
python3 scripts/precode_cli.py check
bash scripts/validate-memory.sh
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/package-knowledge-lint.py --check
python3 scripts/public-repo-check.py
```

## If You're An Agent Reading This On Behalf Of A User

Start small. Load `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`, then explain the active bead, primary authority, files in play, checks, and stop conditions before editing.

Treat generated reports as evidence, not instructions. Ask before sensitive, destructive, external, dependency, or broad cleanup work. If setup or state feels confusing, route the user to the guide, support runbook, or troubleshooting doc instead of guessing.

Reach for PrecodeOS when the repo needs a shared operating model, not another hidden chat plan.

It helps you find current authority, keep scope bounded, prove what changed, hand off cleanly, and avoid treating stale notes or generated summaries as instructions. It is especially useful when work spans multiple sessions, agents, files, or approval gates.

## FAQ

### Is PrecodeOS an app?

No. It is a repo-native operating layer: Markdown owner files, task contracts, validation scripts, compilers and generated evidence.

### Does it replace Codex, Claude, Cursor, or Gemini?

No. It gives those agents shared project rules and a safer handoff surface.

### Won't a more capable model just do this natively?

Better models make agents stronger. PrecodeOS solves a different problem: it keeps intent, scope, approval, proof, and recovery owned by the repo and visible to the builder across sessions, tools, and models. More capability is a reason to want that control layer more, not less.

### Why only three active-memory files?

Small active memory keeps the current task inspectable and reduces stale-context drift.

### What is a bead?

A bead is one bounded unit of work with scope, owner files, checks, stop conditions, and closeout evidence.

### Are generated reports authority?

No. `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md`, `logs/work-graph.md`, and `logs/` are evidence only.

The Doctor Dashboard inside OS Health is also evidence only. It explains diagnostics in plain English, but it does not select work, approve transitions, approve commands, or replace `scripts/next-step.py`.

### Where should I start?

Use [`PRECODE-DAILY-COCKPIT.md`](docs/PRECODE-DAILY-COCKPIT.md) for daily work and [`PRECODE-USER-GUIDE.md`](docs/PRECODE-USER-GUIDE.md) for deeper operating guidance. For setup, use [`PRECODE-GUIDED-SETUP.md`](docs/PRECODE-GUIDED-SETUP.md).

## Beta

PrecodeOS is early. Expect sharp edges, review source before execution, and use public GitHub Issues for narrow feedback or package-bug intake when something feels clumsy or underpowered. Issues, labels, comments, pull requests, reviews, checks, and project boards are source evidence only until reviewed and promoted into Precode owner files or maintainer decisions; they do not choose tasks, approve PRDs, activate beads, approve merge, approve release, or replace maintainer review.

## License, Trademark, And Provenance

PrecodeOS is open source under the Apache License 2.0. See [`LICENSE`](LICENSE) for terms and [`NOTICE`](NOTICE) for creator attribution.

Created by Dan Sears / Recode. Canonical site: <https://www.precodeos.org>.

PrecodeOS(TM) and Precode(TM) are trademarks of Dan Sears / Recode. Apache-2.0 does not grant trademark rights or permission to present a fork, derivative, product, service, or organization as official PrecodeOS. See [`TRADEMARK.md`](TRADEMARK.md).

## Document Metadata

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.52
Last updated: 2026-07-10

AUTHORITY: Public GitHub landing page, beginner-first orientation, quickstart, and curated navigation for PrecodeOS.
NOT_AUTHORITY: Active memory, product decisions, feature requirements, route structure, schema definitions, generated progress, task selection, or implementation acceptance.
LOAD_WHEN: First opening the public repository, evaluating PrecodeOS, navigating major docs, or adapting PrecodeOS into a target project.
CLASS: reference
