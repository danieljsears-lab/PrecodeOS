# PrecodeOS Architecture Overview
<!-- ANCHOR: architecture-overview -->

> AUTHORITY: Reviewer-facing architecture, layer model, principles, failure-mode analysis, enforcement model, trust boundaries, human control surface, comparison framing, evaluation criteria, adoption path, and limitations for PrecodeOS itself.
> NOT_AUTHORITY: Target-project app architecture, active memory, task selection, product requirements, implementation status, route structure, schema definitions, or generated progress state.
> LOAD_WHEN: Evaluating, explaining, positioning, or reviewing PrecodeOS.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.3.27
Last updated: 2026-06-18

## Executive Summary

PrecodeOS is a repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift. It is designed for builders using coding agents over many sessions, where the core risk is not whether an agent can produce code, but whether the repo can preserve intent, scope, authority, evidence, handoff state, and the next safe action as the work moves from idea to implementation.

PrecodeOS is not a code generator, IDE agent, model router, autonomous software engineer, application runtime, installer, or full software development lifecycle framework. It can work with those tools, but it does not replace them. Its job is to make AI-assisted work bounded, inspectable, recoverable, and reviewable inside a real repository.

PrecodeOS matters because AI coding agents can move faster than a builder can understand, verify, and recover from. Architecturally, it keeps the project human-owned by making intent, scope, authority, approval, proof, and recovery explicit repo surfaces rather than hidden chat assumptions.

The core claim is simple:

> Vibe coding becomes safer when the repo has a tiny active memory, explicit authority ownership, one current execution unit, recorded evidence, and human gates at task transitions.

Markdown files own durable intent and contracts. Python and shell scripts compile state, validate invariants, record checks, generate evidence reports, and support handoff. Generated reports inform humans, but they do not become authority.

PrecodeOS™ and Precode™ are trademarks of Dan Sears / Recode. `NOTICE` and `TRADEMARK.md` preserve attribution and brand-use boundaries while `LICENSE` preserves Apache-2.0 reuse terms.

## Category And Problem

PrecodeOS sits in the category of repo-control and evidence-governance systems for vibe coding. It is closest to spec-driven and AI-SDLC frameworks in spirit, but its center of gravity is different.

Spec-driven frameworks ask: "What should we specify before the AI builds?"

Agent workflow frameworks ask: "Which agent or role should perform the next phase?"

Project-management workflows ask: "How do we turn requirements into coordinated tasks?"

Precode asks: "How does this repo know what is active, what is authoritative, what was proven, and whether it is safe to continue?"

That category matters because vibe coding has a characteristic failure pattern: the agent can move faster than the user's ability to track project truth. This is especially painful for solo builders and non-technical founders, but it also appears in mature codebases when generated work spans many files, sessions, tools, or branches.

### Common Vibe-Coding Failure Modes

| Failure mode | What usually happens | Precode response |
|---|---|---|
| Scope widening | The agent adds adjacent features or refactors while implementing one request. | One active bead, files in play, one primary authority, explicit stop conditions, and advisory files-in-play guardrails. |
| Stale context | Old notes, chat summaries, generated reports, completed PRDs, closed issues, or previous journey notes override the current task. | Tiny active memory and a context loading order that demotes generated, source, and stale historical material. |
| False done | The agent says work is complete without evidence strong enough for the risk. | Recorded checks, closeout evidence, manual verification, and review decisions. |
| Vague product intent | A rough idea becomes code before the user, painful before moment, current workaround, strongest evidence, weakest assumption, product fit, non-goals, and acceptance oracles are stable. | Product Ideation Workbook, Product Brief, Conviction Packet, optional Product Discovery Validation, `PRODUCT.md`, alignment/grilling, Goal Frames when durable intent needs review, Product Definition Gate, destination PRD shards, requirement IDs, and PRD-to-bead compilation. |
| Language drift | Product docs, UI labels, tests, module names, and old artifacts use different words for the same concept. | Ubiquitous language protocol, PRD domain-language sections, reviewed glossary memory, and stale-vocabulary demotion. |
| Authority confusion | Product, architecture, schema, security, and acceptance facts are duplicated across docs. | Authority contracts and one owner per fact. |
| Generated summaries become instructions | Status reports or imported evidence start choosing next work. | Generated-output demotion and promotion paths into owned docs. |
| Uncontrolled momentum | The agent finishes one task and rolls into the next. | Review decisions and user-approved bead transitions. |
| Tool lock-in | Each AI coding tool develops its own project memory, model-routing habits, and command style. | Tool-neutral core with thin adapters, shared scripts, and Agent Routing discipline for model tier, context budget, delegation, and tool choice. |
| Lost handoff state | A new session or tool cannot reconstruct current scope, blockers, or evidence. | Context Packs, handoff scripts, active bead pointer, and generated handoff reports. |
| Hidden sensitive work | Auth, payments, secrets, external systems, or destructive operations get folded into normal implementation. | Sensitive-surface stop conditions, approval gates, and tool-execution classification. |
| Unsafe cleanup | Broad cleanup treats authority, evidence, caches, generated files, private-local material, and public-package boundaries as the same kind of clutter. | Local Hygiene categorization, public-repo hygiene checks, advisory checks, dry-run previews, protected generated evidence, v2 preview classifications, and no cleanup mutation. |
| OS-owned file damage | Active memory, protocols, scripts, hooks, adapters, or public/private package boundaries are edited without a pre-mutation recovery point. | OS Integrity protocol, protected-source surface classes, strict staged checkpoint checks, and explicit scoped checkpoint restore. |

Precode does not claim to eliminate these risks. It makes them visible early and gives the repo a repeatable recovery path.

### Failure Mode Categories

Precode separates failures into three categories because each one needs a different response.

| Category | Definition | Examples | Precode posture |
|---|---|---|---|
| AI coding agent failure | The agent misunderstands, overreaches, skips proof, or follows stale context. | Scope widening, false done, hidden product drift, uncontrolled next-task momentum. | Bound the agent with active memory, beads, checks, stop conditions, and review. |
| Human operator failure | The user damages structure, approves too quickly, stores unsafe information, or puts facts in the wrong owner file. | Moving Markdown files, renaming docs, editing generated reports, adding a fourth active-memory file, approving the next bead casually, pasting secrets into docs. | Make rules explicit, validate what can be validated, and require human recovery when structure or approval discipline breaks. |
| OS/tooling failure | The local environment, integrations, scripts, or generated state cannot provide a complete signal. | Stale generated reports, missing telemetry, unavailable `git` or `gh`, non-git checkout, validator coverage gaps. | Report uncertainty as evidence, degrade gracefully, and avoid guessing or mutating state. |

The user guide owns beginner-facing hard rules for human behavior. This document explains the architecture boundary: Precode can detect some structural mistakes, warn about many drift patterns, and still depends on human care around file moves, renames, approvals, and secrets.

## Core Design Principles

### Tiny Active Memory

Only three files are active memory:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Everything else is conditional reference, generated evidence, or archive. This keeps the startup context small enough for humans and agents to inspect.

### One Owner Per Fact

Every durable fact needs an owning file. Product constitution facts belong in `PRODUCT.md`. Product decisions belong in `DECISIONS.md`. Target-project route structure belongs in root `ARCHITECTURE.md`. Schema semantics belong in `DATA-MODELS.md`. Current execution state belongs in `tasks/todo.md` and the active bead.

This prevents a common AI failure mode where the agent patches contradictions by duplicating more text.

Root `ARCHITECTURE.md` is a target-project template shipped with the package. This document, `docs/PRECODE-ARCHITECTURE-OVERVIEW.md`, explains PrecodeOS itself as a public package and reviewer surface.

### One Bead At A Time

A bead is the smallest durable journey unit for one logical unit of work. Only one bead may be `in_progress`. The active bead names its primary authority, files in play, checks, stop conditions, closeout evidence, and optionally its delegation mode, test strategy, review context, complexity, required planning depth, and autonomy level.

### Evidence Over Confidence

The OS does not accept "it should work" as completion. Checks should be run through `bash scripts/record-check.sh -- <command>` so exit codes, logs, branch, bead, and timing become durable evidence.

### Generated Output Is Not Authority

`OS-HEALTH.md`, `PROGRESS.md`, log summaries, imported sources, and generated handoff packets can inform humans. They must not choose tasks, approve transitions, or override active memory.

Maintainer-local history can explain how surfaces changed, but it does not select work, approve decisions, or replace the current owner file.

### Human Approval At Transitions

Agents can propose next work. Humans approve task activation, PRD approval, sensitive-surface work, external mutation, review decisions, and bead transitions.

### Tool-Neutral Core, Thin Adapters

Precode is designed to work across Codex, Claude, Cursor, Gemini, Antigravity, GitHub Copilot, and other coding tools. Tool-specific files are compatibility shims or adapters. The shared command surface and operating model stay in the repo.

## System Architecture

### System Shape

PrecodeOS lives mostly at the repo root. In an adopted project, it surrounds application code with a governance layer. In this repository, PrecodeOS is the maintained package itself, so package maintenance is source/document/script review and static validation rather than launching an app.

```text
repo/
  AGENT.md                 active memory
  DECISIONS.md             active memory
  PRODUCT.md               product constitution, reference
  project-evidence/        target-project source evidence guide
  tasks/todo.md            active memory, active bead pointer
  tasks/beads/*.md         execution contracts
  tasks/prds/*.md          product definition shards
  tasks/reference/*.md     protocols and playbooks
  tasks/templates/*.md     reusable evidence and student/workflow templates
  modes/*.md               navigator, explorer, builder, review roles
  adapters/*.md            tool-specific shims
  AGENTS.md, CLAUDE.md,
  GEMINI.md, .github/*     compatibility shims and GitHub surfaces
  scripts/*                validators, recorders, compilers, audits
  docs/*.md                public reader and reviewer docs
  docs-html/*.html         generated public reading surface
  logs/*                   generated evidence and sidecars
  app/ or project code     target application
```

The application can use any framework. Precode's architecture overview is not the target app architecture and should not be used as a route map or module-placement guide for product code.

### Layer Model

This architectural layer model explains how PrecodeOS fits together. For operational context-loading discipline across active memory, owner files, protocols, adapters, skill playbooks, generated reports, reviewed memory, raw evidence, and maintainer-local context, use the Context Layer Matrix in `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`.

| Layer | Purpose | Main surfaces |
|---|---|---|
| Repo boundary | Separate operating model from app code and distinguish package maintenance from app execution. | Repo root, target app directory, public package boundary. |
| Active-memory kernel | Define the minimal always-loaded context. | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`. |
| Authority contracts | Declare what each file owns and must not own. | `AUTHORITY`, `NOT_AUTHORITY`, `LOAD_WHEN`, `CLASS`. |
| Reference layer | Hold product constitution, architecture, schema, API, security, and workflow rules. | `PRODUCT.md`, root reference docs, `tasks/reference/`. |
| Source-evidence layer | Keep raw notes, documents, screenshots, research, and links evidence-only until reviewed conclusions are promoted. | `project-evidence/PROJECT-EVIDENCE-GUIDE.md`, Local Source Intake. |
| Discovery validation layer | Test worth-building uncertainty before product definition hardens into tasks. | `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`, Discovery Summary, proceed/pause/narrow/kill recommendation. |
| Goal-frame layer | Preserve reviewed durable intent without turning it into backlog or active work. | `PRODUCT.md`, PRDs, beads, or `DECISIONS.md` `Goal Frame` sections, `tasks/reference/GOAL-FRAME-PROTOCOL.md`, `scripts/goal-frame-check.py`, `logs/goal-frame.json`. |
| Product Definition Gate | Prevent vague ideas from becoming implementation beads. | `PRODUCT.md` fit check, alignment/grilling, destination PRD protocol, PRD shards, `FEATURES.md`. |
| Shared-language layer | Keep user terms, aliases, avoid terms, UI labels, code/test names, and stale vocabulary visible without expanding active memory. | `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md`, PRD `Domain Language`, `memory/cards/` category `project_glossary`. |
| Workflow-selection layer | Route rough ideas, source intake, PRDs, architecture shaping, review, repair, and closeout to the right protocol before work starts. | `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`, `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md`, `tasks/reference/PLANNING-PROTOCOL.md`. |
| Setup-intake layer | Keep first-run confidence and existing-repo intake read-only until a user explicitly chooses a setup path. | `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`, `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md`, `scripts/bootstrap-check.py`, `scripts/existing-repo-intake.py`. |
| Architecture-shaping layer | Make auth, data, API, integration, dependency, migration, workflow, or multi-system risk visible before beads are derived. | `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md`, `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md`. |
| Execution bead layer | Bound one journey unit of work. | `tasks/beads/*.md`, bead frontmatter and sections, delegation mode, test strategy, review context. |
| Adaptive-depth layer | Scale planning, proof, autonomy, and human-gate expectations to the bead's risk while giving beginners a plain continue, ask-for-proof, approval-needed, or stop signal. | `complexity`, `required_planning_depth`, `autonomy_level`, inferred defaults, `scripts/bead-depth-check.py`, generated Help and Health summaries. |
| Run-contract layer | Tighten high-risk execution policy without burdening ordinary beads. | bead `Run Contract` sections, `scripts/run-contract-check.py`, `logs/run-contract.json`, `logs/run-contract.yaml`. |
| Ralph attempt layer | Run opt-in bounded retry attempts for one active bead and record validator-backed attempt evidence. | `tasks/reference/RALPH-LOOP-PROTOCOL.md`, optional bead Ralph frontmatter, `scripts/ralph-loop.py`, `logs/ralph-attempts.jsonl`, `logs/ralph-summary.md`. |
| Mode layer | Separate planning, exploration, building, and review behavior with compact role contracts. | `modes/NAVIGATOR.md`, `modes/EXPLORER.md`, `modes/BUILDER.md`, `modes/REVIEW.md`. |
| Adapter layer | Normalize tool-specific entrypoints. | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `adapters/*.md`. |
| Agent-routing layer | Keep model tier, context budget, delegation, and tool choice proportional to the bead. | `tasks/reference/AGENT-ROUTING-PROTOCOL.md`, `adapters/ADAPTER-INDEX.md`, tool-specific adapters. |
| Skill-playbook layer | Keep optional prompt-playbook and skill-style workflows subordinate to owner protocols. | `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`, package skill playbooks when present. |
| Safety layer | Add constraints for scope, sensitive surfaces, and verification. | `OPERATING-CONSTRAINTS.md`, security and verification protocols. |
| Script layer | Turn conventions into repeatable commands. | Session, checkpoint, close, record-check, transition scripts. |
| Validator layer | Catch structural drift and advisory guardrail gaps. | `validate-memory.sh`, advisory checks, files-in-play guardrail, command classification, advisory edit lock, write guard, pre-commit hook. |
| Next-step layer | Give humans the canonical generated "what now?" decision without choosing work for them. | `scripts/next-step.py`, `logs/next-step.json`, `PRECODE-HELP.md`, `user_decision`, `single_next_protocol`, `load_plan`, and `context_footprint`. |
| Completion and handoff layer | Keep closeout, review posture, and next-session context explicit. | `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`, `completion-check.py`, `session-close.sh`, `handoff.sh`. |
| Evidence layer | Preserve what happened without making it authority. | `logs/*.json`, `logs/*.jsonl`, generated reports. |
| Public docs layer | Provide committed reader-facing HTML without replacing canonical Markdown. | `docs/*.md`, `docs-html/*.html`, maintainer-only docs generation. |
| Provenance layer | Keep open-source use permissive while preserving clear creator attribution, canonical site, governance, contribution policy, and trademark/brand boundaries. | `LICENSE`, `NOTICE`, `GOVERNANCE.md`, `CONTRIBUTING.md`, `TRADEMARK.md`, `https://www.precodeos.org`, Markdown provenance metadata, SPDX headers in core scripts. |
| Public-package hygiene layer | Keep private local material out of the reusable public package. | `.gitignore`, `scripts/public-repo-check.py`, package inventory checks. |
| Local hygiene layer | Classify local clutter without deleting evidence or project truth. | `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md`, `scripts/local-hygiene-check.py`, `scripts/local-hygiene-dry-run.py`, and protected generated evidence handling for `logs/os-checkpoints/*`. |
| Handoff layer | Orient the next session or agent safely. | Handoff script, Context Pack, handoff packet. |

### Artifact Lifecycle

Precode's intended flow is:

```text
idea or source material
  -> optional product ideation workbook
  -> Product Brief
  -> Conviction Packet when a first-time rough idea needs MVP-ready clarity
  -> optional Product Discovery Validation when worth-building risk is high
  -> source intake
  -> product constitution fit check
  -> Goal Frame proposal and reaffirmation when durable intent needs orientation
  -> alignment/grilling
  -> shared-language check when terms matter
  -> destination PRD shard
  -> feature inventory
  -> journey bead proposal
  -> active bead
  -> recorded checks
  -> closeout evidence
  -> review decision
  -> user-approved transition
```

Workbook packets, Discovery Summaries, imported notes, GitHub issues, screenshots, generated reports, completed PRDs, archived beads, old alignment transcripts, changelog entries, and glossary memory are evidence or history. They become authority only after promotion into the correct Precode-owned file.

### Runtime Loop

The normal loop is:

1. Start session with `bash scripts/session-start.sh`.
2. Load active memory, active bead, and primary authority.
3. Work inside the active bead.
4. Run checks through `bash scripts/record-check.sh -- <command>`.
5. For Ralph-enabled, testable beads, optionally run `python3 scripts/ralph-loop.py` against one explicit attempt command and validator set.
6. Checkpoint when scope, context, or evidence becomes unclear.
7. Close with `bash scripts/session-close.sh`.
8. Review closeout evidence and decide `accepted`, `revise`, `split`, or `blocked`.
9. Approve transition with `python3 scripts/bead-transition.py --approve` only when safe.

## Control And Safety Model

### Enforcement Model

Precode uses four enforcement levels:

| Level | Examples | Strength |
|---|---|---|
| Convention | Design principles, best practices, mode guidance. | Useful but human/agent disciplined. |
| Structured markdown | Bead frontmatter, authority contracts, stable sections. | Machine-readable enough to validate. |
| Script enforcement | Validation, check recording, closeout updating, transition assessment. | Repeatable local enforcement. |
| Human gate | PRD approval, sensitive work, review decision, transition approval. | Final authority for intent and risk. |

The core validator currently checks required docs, authority contracts, active-memory discipline, `tasks/todo.md` frontmatter, bead structure, closeout markers, and the one-in-progress-bead invariant.

Advisory checks extend the model across context, decomposition, verification, state, orchestration, workflow selection, long-horizon planning, completion, files in play, run contracts, goal frames, public-package hygiene, local hygiene, and tool execution.

Generated sidecars such as `logs/readiness.json`, `logs/next-step.json`, `logs/authority-map.json`, `logs/file-inventory.json`, `logs/handoff-packet.json`, `logs/run-contract.json`, and `logs/workflow-map.json` make current state easier to inspect, but they remain evidence, not authority.

Ralph attempt outputs such as `logs/ralph-attempts.jsonl` and `logs/ralph-summary.md` are generated evidence in the same trust boundary. They can show what was tried, what validators said, and whether another attempt is allowed, but they cannot accept work, approve commands, choose the next bead, or replace human review.

`next-step.py` is the canonical generated router for the next human decision. `session-start.sh` displays the same decision inside the session Context Pack so the first command and the standalone router do not compete.

`PRECODE-HELP.md` is the human-readable generated next-step snapshot. It can explain blockers, adaptive-depth warnings, files-in-play warnings, the one next protocol to load, and rough context footprint, but it cannot select work, approve review, or activate a bead.

Context-footprint fields are intentionally approximate. They show active memory, active bead, primary authority, conditional references, generated reports touched, and rough document lines so agents avoid loading every protocol when one owner file is enough.

For a public package file-by-file technical dictionary and relationship map, use `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`. This architecture overview explains why the layers exist; the package inventory explains what each public package file owns and how the surfaces connect. Generated `docs-html/*.html` files are a committed reading surface generated from public Markdown; they do not replace the Markdown authorities.

### Human Control Surface

Precode deliberately keeps several decisions human-gated:

- PRD approval before product-feature implementation.
- Sensitive-surface approval for auth, payments, secrets, personal data, uploads, external systems, destructive actions, and production configuration.
- Review decision after work is closed out.
- Bead transition approval before next work becomes active.
- External mutation approval when tools touch GitHub, CI, deployments, dashboards, or third-party systems.
- Blocked-work escape decisions, such as creating an unblocker bead or pausing for manual setup.

This is not accidental friction. It is the safety model.

### Threat Model And Trust Boundaries

Precode assumes that AI coding sessions can be confused by untrusted or stale material. Its trust model separates authority from evidence.

| Surface | Trust boundary |
|---|---|
| Active memory | Authoritative for current operating state. |
| Active bead | Authoritative for current execution contract. |
| Bead Run Contract | Risk-triggered allowed actions, proof needed, approval gates, and stop conditions inside the active bead. |
| Primary authority | Authoritative for the topic the bead is changing. |
| Reference docs | Authoritative only for their declared topic. |
| Goal Frames | Reviewed durable orientation only; never backlog, roadmap, task selection, PRD approval, or bead activation. |
| Discovery Summaries | Advisory pre-PRD evidence only; proceed means ready for the next planning workflow, not approved to build. |
| Generated reports | Evidence only; never task instructions. |
| Generated public HTML docs | Reader convenience only; Markdown in `docs/` remains canonical. |
| Imported issues, PRs, notes, screenshots | Source material only until promoted. |
| Private maintainer-local history | Human-readable history only; not public package authority, current authority, generated evidence, or transition approval. |
| Private maintainer-local files | Maintainer planning and package-boundary context; not active memory, public package authority, or normal user workflow instructions. Public package docs, scripts, shims, tasks, demos, and generated reading surfaces must remain complete when maintainer-local files are absent. |
| Public-repo checks | Advisory public/private boundary findings only; not cleanup approval or a publishing action. |
| Completed PRDs, archived beads, closed issue imports, old transcripts | Historical evidence only; current authority wins on conflict. |
| Tool shims and adapters | Compatibility surfaces; not separate operating systems. |
| External systems | Read-only by default unless an approved bead permits mutation. |
| Secrets and credentials | Never stored in Precode docs or logs. |

The main prompt-injection defense is procedural: source material is summarized and promoted through owned docs before it can steer work. Precode does not rely on the agent to distinguish every malicious or stale instruction in raw context.

### Failure And Recovery Model

Precode treats a clean stop as successful behavior when continuing would widen risk.

`tasks/reference/RECOVERY-PROTOCOL.md` is the canonical beginner-safe recovery workflow. This section summarizes the architecture boundary: recovery preserves state, identifies the owner file, records evidence, and resumes only inside a bounded task.

| Failure | Expected recovery |
|---|---|
| Human moved or renamed a Precode Markdown file | Stop work, identify the expected path/name from `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` or validation output, restore the file, then validate. |
| Human directly edited generated output | Stop using that output, restore or regenerate it with the owning script, then return to source files. |
| Human changed anchors, authority contracts, frontmatter, headings, bead state, or closeout structure | Restore the expected structure, run `bash scripts/validate-memory.sh`, then run relevant advisory checks. |
| Human put facts in the wrong owner file | Move the fact to `DECISIONS.md`, a PRD, a bead, or the correct authority doc; do not duplicate it across files. |
| Human approved too much too quickly | Stop, review recorded evidence, identify the approval scope, and split or block work before continuing. |
| Human stored secrets or private dashboard values | Stop, remove the secret from files/logs where possible, rotate the credential if exposed, and record only a non-secret setup note. |
| Active state drift | Run `python3 scripts/state-check.py`, repair `tasks/todo.md` or bead state, then validate. |
| Context overload | Re-read active memory, active bead, and primary authority; run `python3 scripts/context-check.py`. |
| Scope widening | Stop, split work into a follow-up bead, or revise the current bead after approval. |
| Weak evidence | Run stronger checks or record manual verification using the verification protocol. |
| Implementation context too full for review | Use fresh-context review: reload active memory, active bead, primary authority, parent PRD when relevant, and the diff/evidence. |
| Blocked bead | Set status to `needs_info` or `manual_testing`, record escape path, and create/note an unblocker. |
| Unsafe handoff | Run `bash scripts/handoff.sh [next-agent]`; do not continue from generated reports alone. |
| Generated-output confusion | Move any real instruction into the owning authority file or bead, then regenerate reports. |
| Sensitive approval gap | Stop before mutation and ask for explicit user approval. |

The recovery posture is conservative: preserve state, identify the owner file, record evidence, and resume only inside a bounded bead.

### Accidental File Damage Recovery

If a Precode file was moved, renamed, or directly edited by mistake:

1. Stop implementation.
2. Identify the affected file and expected owner from `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`.
3. Restore the expected path, filename, anchor, authority contract, frontmatter, headings, and required sections.
4. Regenerate generated reports instead of hand-editing them.
5. Run `bash scripts/validate-memory.sh`, then `python3 scripts/file-inventory.py --check`, `python3 scripts/state-check.py`, and any relevant advisory check.
6. Continue only after the active bead, primary authority, files in play, and checks are clear again.

Use the Recovery Protocol for the full beginner-facing triage table covering file damage, generated-report confusion, stale reports, active-state drift, missing proof, context loss, accidental scope expansion, and approval confusion.

## Operating Patterns

### Best Practices

- Start every serious session with session start.
- Keep beads boring, small, and reviewable.
- Load the active bead and primary authority before changing files.
- Prefer one observable outcome per bead.
- Prefer vertical journey beads for user-facing work.
- Use `afk_candidate` only as advisory delegation metadata; it does not activate parallel work or bypass review.
- Use Small Team Collaboration Lane only through explicit coordinator invocation and branch/worktree isolation. It does not activate multiple beads in one checkout, turn GitHub into authority, or make teammate handoff packets acceptance evidence.
- For code-changing beads, declare test strategy and prefer failing-first when practical.
- Use Ralph only when a bead is testable, bounded, and opted in or explicitly requested for a one-off run.
- For medium/high-risk code-changing beads, prefer or require fresh-context review.
- Own deep-module interfaces, behavior contracts, and test boundaries before delegating internals.
- Use stop conditions as guardrails, not as failure labels.
- Run meaningful checks through `record-check.sh`.
- Treat generated tests, screenshots, and AI critiques as review inputs until recorded.
- Close sessions before switching agents or changing direction.
- Keep generated reports out of active memory.
- Promote repeated lessons into the owning protocol or rule, not into a diary.

### Proven Patterns

| Pattern | Why it works |
|---|---|
| Alignment before PRD | Creates a shared design concept before polished text hides open questions. |
| Destination PRD to journey bead compilation | Turns product intent into traceable execution slices. |
| Vertical slices | Give feedback across enough layers before the agent builds too far horizontally. |
| Deep modules | Let humans own code shape while agents implement internals behind a clear interface. |
| Source intake before promotion | Prevents raw notes or issues from becoming hidden instructions. |
| Discovery before PRD when evidence is weak | Keeps solution-first ideas from becoming polished requirements too early. |
| Goal Frame reaffirmation | Lets durable intent orient workflow selection without becoming a hidden task list. |
| Stop-if gates | Makes risky expansion visible before implementation. |
| Review inputs vs evidence | Separates helpful observations from proof of completion. |
| Generated health reports | Gives humans status without expanding active memory. |
| Ralph attempt logs | Preserve bounded retry history so failed attempts do not disappear into chat. |
| Adapter shims | Lets different AI tools enter the same operating model. |
| Agent routing | Keeps model depth, context, delegation, and tool use proportional to risk. |
| Advisory validators | Surfaces drift without letting automation choose work. |
| Public-repo hygiene checks | Keeps private or maintainer-local material from leaking into the reusable package. |
| Blocked-bead escape paths | Prevents stuck work from pretending to be active progress. |

### Evidence Model

Precode evidence has a hierarchy:

1. Recorded verification checks with command, exit code, and output log.
2. Manual verification with who checked, what was checked, environment, result, and remaining uncertainty.
3. Closeout evidence that summarizes checks, changed files, review decision, drift, lessons, and follow-up.
4. Ralph attempt evidence that summarizes explicit attempts, validators, failure category, and next recommended move.
5. Generated sidecars and reports that summarize state for humans.
6. Review inputs such as Discovery Summaries, Goal Frame fit notes, screenshots, external QA notes, AI critiques, or generated tests.
7. Human-readable maintainer-local history.

Only the first three should drive acceptance. Ralph attempt evidence, generated reports, review inputs, and history help review, but they do not prove completion by themselves.

### Handoff And Interoperability Model

Precode treats coding agents as replaceable execution surfaces. The repo contract persists across tools. Compatibility shims and adapters should point back to the shared operating model instead of becoming separate tool-specific memories.

For small teams, interoperability extends to people as well as agents: each contributor works from the shared repo contract in a branch or worktree, returns recorded evidence, and re-enters through coordinator review. The integration branch still preserves one active bead and one authority chain.

### Router-First Modularity

Precode's current architecture direction is router-first externally and modular internally.

- Externally, `next-step.py` owns the generated "what now?" decision; `session-start.sh` presents it; future diagnostic wrappers may explain warnings after the router is trusted.
- Internally, compiler domains move behind small service modules such as `scripts/precode_state.py`, `scripts/precode_outputs.py`, and `scripts/precode_routing.py`, while `scripts/os_compiler.py` remains the stable facade for existing commands, imports, and generated JSON shapes.
- Role contracts stay compact: Navigator, Explorer, Builder, and Review define what to load, decide, avoid, and return. They do not become extra active memory or an autonomous specialist organization.
- Ralph stays a bounded attempt engine for one active bead, not a multi-bead scheduler or autonomous agent platform.
- Bootstrap now has staged setup gates: read-only source/target confidence, manifest preview, supervised setup plan, narrow fresh-target apply, existing-project adaptation planning, existing-Precode upgrade preview, recovery guidance, and explicit action-ID copy gates for safe missing package-owned files.
- A broad `precode doctor` command, broad mutating installer/update flow, release-channel behavior, rollback automation, and package-manager semantics remain deferred. The optional `precode` CLI is only a local facade over documented commands.

Handoff should include:

- current bead
- done-when target
- primary authority
- files in play
- out of scope
- required checks
- stop conditions
- open questions
- forbidden assumptions
- generated-report warning

This lets Codex, Claude, Cursor, Gemini, Antigravity, or another agent enter the same repo state without inheriting an unreliable chat transcript.

## Technical Reviewer Evaluation Framework

A technical reviewer can evaluate PrecodeOS against these criteria:

| Criterion | Reviewer question |
|---|---|
| Context discipline | Does the system keep default context small and inspectable? |
| Authority clarity | Can a reviewer tell which file owns each fact? |
| Task boundedness | Is there exactly one active execution unit? |
| Verification quality | Are completion claims backed by recorded evidence? |
| Human gate clarity | Are product, risk, review, and transition decisions visibly human-gated? |
| Handoff safety | Can another agent resume without trusting chat memory? |
| Recovery behavior | Does the system have a path for drift, blockers, weak evidence, and stale reports? |
| Interoperability | Can it work across coding tools without duplicating operating rules? |
| Adoption overhead | Can teams adopt a small kernel first, or must they absorb the whole system? |
| Maintainability | Can new protocols, adapters, and reports be added without expanding active memory? |

The strongest evidence for Precode is not a single impressive demo. It is repeated work where beads remain bounded, checks are recorded, generated reports stay demoted, and handoffs continue to be safe across sessions and tools.

## Comparison Landscape

### Category Fit

| Category | Primary focus | Examples | Relationship to Precode |
|---|---|---|---|
| Spec-driven frameworks | Define specs before AI implementation. | GitHub Spec Kit, OpenSpec, Spec Kitty. | Complementary; Precode can govern execution and evidence around specs. |
| AI SDLC frameworks | Provide roles, phases, workflows, and lifecycle artifacts. | BMAD Method, KubeRocketAI. | Adjacent; Precode is narrower and more repo-state focused. |
| AI delivery workflows | Add ordered specialist commands for planning, review, browser QA, release, and retrospective discipline. | gStack. | Complementary; Precode can provide repo-owned authority, evidence, scope, and transition control under or beside delivery workflows. |
| Project-management workflows | Turn PRDs into issues, work packages, or parallel execution streams. | Claude Code PM. | Complementary; Precode is more conservative about one active bead and human transitions. |
| Repo-control and evidence governance | Preserve current truth, authority, scope, checks, and handoff state. | PrecodeOS. | Precode's core category. |
| Code-editing agents | Generate and edit code through an IDE or CLI. | Cline, Roo Code, Aider, Claude Code, Codex. | Surfaces that Precode can coordinate; not direct alternatives. |

### Open-Source Comparison Matrix

| System | Center of gravity | Strongest fit | Precode difference |
|---|---|---|---|
| [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) | AI-native SDLC with specialized agents, planning, stories, QA, and modules. | Teams or builders who want guided product and software lifecycle workflows. | Precode is less persona/workflow heavy and more focused on repo truth, evidence, and transition control. |
| [gStack](https://github.com/garrytan/gstack) | Opinionated software delivery workflow for Claude Code, Codex, and compatible agents. | Founders, technical leads, and agent users who want ordered planning, review, QA, and shipping loops. | Precode is the repo-owned authority, evidence, and control layer; gStack is a specialist workflow stack that can run above or alongside it. |
| [GitHub Spec Kit](https://github.github.io/spec-kit/) | Specification-driven development where specs become executable implementation inputs. | Teams that want formal specs and plans before AI implementation. | Precode treats specs as one authority input, then governs active memory, beads, checks, and handoff. |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | Lightweight spec-driven proposal, specs, design, tasks, apply, and archive workflow. | Brownfield-friendly agreement-before-build workflows across AI tools. | Precode is stricter about active-memory limits, generated-output demotion, and human-approved transitions. |
| [Claude Code PM](https://github.com/automazeio/ccpm) | PRD-to-epic-to-GitHub-Issue workflow for parallel Claude Code execution. | Coordinating multiple Claude Code agents through issues and worktrees. | Precode favors one active bead and repo-owned authority before scaling parallel work. |
| [Spec Kitty](https://github.com/Priivacy-ai/spec-kitty) | Spec -> plan -> tasks -> agent loop -> review -> merge workflow. | Teams that want spec-driven work packages, lanes, review, and merge flow. | Precode emphasizes tiny active memory, evidence demotion, and conservative task activation. |
| [KubeRocketAI SDLC Framework](https://krci-ai.kuberocketci.io/architecture) | AI-as-code SDLC framework with agents, rules, templates, and CLI. | Teams standardizing AI agent management across a full SDLC. | Precode is smaller, repo-native, and optimized for solo or small-team control before broad orchestration. |

The deeper BMAD and gStack research comparison is maintainer-local material, not part of public package navigation. This architecture overview keeps only the reviewer-facing landscape summary.

### Why Code-Editing Agents Are Not Direct Alternatives

Cline, Roo Code, Aider, Claude Code, Codex, Cursor, and similar tools are code execution and editing surfaces. They answer: "How does an AI agent inspect and modify code?"

Precode answers a different question: "What repo-owned contract tells any agent what is active, what is authoritative, what proof is required, and when to stop?"

That distinction is important for evaluation. A code-editing agent can be excellent and still drift if the repo has no durable operating model. Precode can make several code-editing agents safer without competing with their editing mechanics.

## Limitations And Adoption

### Known Limitations

- Precode is not a code generator or implementation engine.
- Precode is not a complete test-generation or QA framework.
- Precode does not replace senior engineering review for architecture, security, performance, or maintainability.
- Precode's current packaging is less polished than mature installable OSS frameworks.
- The system depends on disciplined use of active memory, beads, checks, and human gates.
- Validators can catch structural drift, but they cannot prove product correctness.
- Manual gates can feel slow to users who want fully autonomous coding.
- The current scaffold is more transparent than ergonomic; onboarding can be improved.

### Adoption Path

Adopt Precode in tiers:

| Tier | What it adds | Best for |
|---|---|---|
| Kernel | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, one starter bead. | First use, small projects, learning the pattern. |
| Loop | Kernel plus session start, checkpoint, closeout, record-check, and handoff scripts. | Active AI coding with repeated sessions. |
| Guarded | Loop plus validators, generated health, PRD gate, transition approval, adapters, and advisory checks. | Long-running repos, sensitive work, multi-tool workflows. |

The recommended adoption strategy is not to copy every file at once. Start with the kernel, then add scripts and validators when the repeated failure modes become visible.

### Planned Roadmap Improvements

This public architecture overview previews direction without depending on private roadmap or prioritization material:

- improve onboarding and bootstrap so builders can adopt the smallest useful Precode tier first
- keep sharpening next-step clarity around continue, ask, prove, approve, repair, and stop
- keep adaptive depth and file/command guardrails quiet, specific, and advisory before adding heavier layers
- add risk-triggered run contracts for allowed actions, proof needed, approval gates, and stop conditions only where they prove value
- strengthen evidence, release readiness, and review lanes without turning Precode into a specialist-team simulator
- add import bridges and optional packs later, after the kernel remains quiet and trusted
- keep public package docs independent from maintainer-local planning surfaces while package adoption and update paths mature

## Reviewer Takeaway

PrecodeOS is strongest when evaluated as a control layer for AI-assisted repo work, not as a coding agent, app runtime, installer, or broad SDLC suite. Its distinctive contribution is the combination of tiny active memory, authority contracts, one active bead, recorded evidence, generated-output demotion, and human-approved transitions.

Compared with spec-driven and AI-SDLC systems, Precode is narrower but more pessimistic about drift. It assumes that momentum is dangerous unless bounded by repo-owned state and evidence. That makes it especially relevant for vibe coding, where speed is abundant but durable project truth is scarce.

The system still needs better packaging, examples, and onboarding. But its architectural idea is coherent: give any AI coding agent a repo-owned memory, a scope boundary, an evidence trail, and a brake pedal.

For the public document compass, read `README.md`. This architecture overview is the reviewer and maintainer companion, not the beginner navigation surface.


## Deep Maintainer And Forking Notes

This section owns the detail that the beginner README now points away from: full implementation surfaces, maintainer procedures, public fork guidance, and the reusable minimal pattern.

### Detailed Layer Responsibilities

The layer model is intentionally explicit because each layer prevents a different drift mode.

| Layer | Deep responsibility |
|---|---|
| Repo boundary | Separate the operating layer from application code so app churn does not rewrite the OS, and so package maintenance does not become app execution. |
| Active-memory kernel | Keep startup context to `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`. |
| Authority contracts | Make every AI-facing doc declare what it owns, what it must not decide, when to load it, and its class. |
| Reference layer | Hold product, architecture, API, schema, security, context, workflow, setup-intake, skill-playbook, and protocol detail outside active memory. |
| Source-evidence layer | Keep user-provided project evidence raw and evidence-only until Local Source Intake promotes reviewed conclusions. |
| Discovery validation layer | Keep broad, risky, market-facing, paid, evidence-poor, or solution-first ideas as evidence until the builder chooses the next workflow. |
| Goal-frame layer | Store durable orientation only inside existing owner files after review and reaffirmation, while preventing it from becoming backlog, roadmap, or task authority. |
| Product Definition Gate | Route rough ideas and source material through intake, PRD shards, requirements, and candidate beads before implementation. |
| Execution bead layer | Make one logical unit executable, reviewable, closable, and handoff-safe. |
| Mode layer | Separate navigator, explorer, builder, and review behavior so planning, inspection, implementation, and critique do not blur together. |
| Adapter layer | Keep tool-specific entrypoints thin while preserving one shared command surface across Codex, Claude, Cursor, Gemini, Antigravity, Copilot, and future tools. |
| Agent-routing layer | Choose model depth, context budget, delegation, and tool route without overriding active bead scope, files in play, approvals, or review. |
| Skill-playbook layer | Keep optional skill-style workflows subordinate to public protocols, not hidden authority. |
| Safety layer | Add stop conditions for scope, sensitive surfaces, destructive operations, generated-output demotion, and approval gates. |
| Script layer | Turn repeated operating habits into commands with stable output and logs. |
| Validator layer | Enforce structural invariants and expose drift before continuing implementation. |
| Public docs layer | Keep public Markdown canonical while committed generated HTML improves readability and navigation. |
| Evidence layer | Preserve check results, loop events, spend, handoff state, generated maps, and health snapshots without making them authority. |
| Public-package hygiene layer | Check private, maintainer-local, ignored, and public-package candidate files without publishing, deleting, or mutating the package. |
| Handoff layer | Let a future session or different agent reconstruct scope, blockers, checks, and next safe action. |

### Script And Generated Sidecar Taxonomy

The script layer has these families:

| Family | Examples | Purpose |
|---|---|---|
| Session loop | `session-start.sh`, `checkpoint.sh`, `session-close.sh`, `handoff.sh` | Orient, pause, close, and transfer work safely. |
| Evidence and state | `record-check.sh`, `update-bead-closeout.py`, `execution-state.py`, `log-loop-event.sh`, `log-tool-run.sh`, `log-agent-spend.sh`, `import-agent-spend.py` | Record what happened without relying on chat memory. |
| Compilation and reports | `os_compiler.py`, `precode_state.py`, `precode_outputs.py`, `precode_routing.py`, `os-health.py`, `progress.py`, `next-step.py`, `update-learning-diary.py`, `update-memory-index.py`, `scheduled-audit.py` | Compile markdown/log state into generated evidence, render sidecars, and route the next human decision behind stable command paths. |
| Advisory checks | `context-check.py`, `state-check.py`, `workflow-check.py`, `goal-frame-check.py`, `completion-check.py`, `files-in-play-check.py`, `run-contract-check.py`, `public-repo-check.py`, `local-hygiene-check.py`, and related checkers | Surface likely drift without mutating active memory. |
| Setup and intake checks | `bootstrap-check.py`, `existing-repo-intake.py`, `github-audit.py`, `import-github-sources.py` | Inspect adoption targets or external source material while keeping mutation explicit and gated. |
| Maintenance helpers | `validate-memory.sh`, `version-check.py`, `file-inventory.py`, `pre-commit-validate.sh`, `install-git-hooks.sh`, `write-guard.sh`, `os-integrity-check.py`, `os-checkpoint.py` | Protect package structure, provenance, inventory, scoped writes, protected OS-owned source surfaces, and explicit restore points. |

Generated sidecars should stay under `logs/` unless an existing generated report or committed docs-reading surface owns the output. Important sidecars include readiness, authority, adapter, shim, orchestration, workflow, goal-frame, long-horizon, handoff, pattern, run-contract, file-inventory, local-hygiene, bootstrap, existing-repo intake, scheduled-audit, progress, next-step, and health outputs. They are evidence only.

### Validator And Hook Detail

The core validator should protect invariants that are easy to explain:

- required authority contracts and anchors
- exactly three active-memory files
- valid `tasks/todo.md` frontmatter
- one `in_progress` bead
- required bead sections and closeout markers
- generated reports demoted from active memory
- canonical adapter command surface
- advisory version metadata coverage

Good validators catch structural drift. Bad validators try to interpret every sentence. Add stricter validation only after a drift pattern repeats and can be checked reliably.

### Maintainer Procedures

When changing the OS itself:

1. Identify the owner file or protocol first.
2. Keep active memory unchanged unless explicitly changing the kernel.
3. Use `tasks/reference/SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md` before implementation or merge when a change may alter active memory, authority ownership, generated-output demotion, package install/update boundaries, governance or contribution semantics, or beginner-facing safety language.
4. Update version metadata on touched OS-owned files.
5. Keep generated outputs demoted.
6. Add or update advisory checks only when they can report clear, actionable warnings.
7. Use static validation and docs generation for package review; do not treat this repository as an app to launch unless a task explicitly says so.
8. Run `bash scripts/validate-memory.sh` and `python3 scripts/version-check.py`.
9. Regenerate public `docs-html/` when public docs change, and regenerate health/audit outputs when reporting surfaces changed.

Common maintenance moves:

| Maintenance task | Owner |
|---|---|
| Add a protocol | `tasks/reference/EXTENSION-PROTOCOL.md` plus the new protocol file. |
| Change semantic package boundaries | `tasks/reference/SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md` plus the affected owner files. |
| Add a checker | The checker script, command surfaces, README pointer, and generated report only if useful. |
| Add a bead template | `tasks/beads/BEAD-SCHEMA.md`. |
| Add an integration | Integration protocol, `PROJECT-CONTEXT.md` boundaries, read-only audit/importer scripts. |
| Add or change setup intake | Bootstrap, Existing Repo Intake, or Bootstrap Closeout protocol plus checker behavior, public setup docs, and explicit mutation boundaries. |
| Change generated report behavior | Compiler/report script plus generated-output demotion check. |
| Change public docs rendering | Public Markdown docs plus regenerated `docs-html/` using the maintainer-only docs generator. |
| Change version policy | `tasks/reference/VERSIONING-PROTOCOL.md` and `scripts/version-check.py`. |
| Change public package boundary | `.gitignore` and `scripts/public-repo-check.py`. |

### Public Forking Guidance

For a public-facing fork, keep the operating pattern and remove project-specific facts.

Recommended public name:

> PrecodeOS

Useful naming pattern:

- `PrecodeOS` = the generic public system
- `YourProject OS Profile` = one project's implementation
- `Precode Beads` = the execution units
- `Precode Kernel` = the three-file active memory set

A generic public repo can keep:

```text
precode-os/
  AGENT.md
  DECISIONS.md
  tasks/todo.md
  tasks/beads/
  tasks/prds/
  tasks/reference/
  modes/
  adapters/
  scripts/
  logs/
  .github/
  examples/
```

Generalize product-specific docs into templates. Remove business details, personal names, local paths, secrets, environment values, and domain-specific assumptions that do not belong in a reusable OS.

Position Precode as:

> A repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift.

Avoid positioning it as a prompt library, project-management app, fully autonomous engineer, or replacement for technical judgment.

### Minimal Reusable Pattern

If the full scaffold is too much, keep the smallest useful pattern:

1. Three active-memory files.
2. Authority contracts.
3. A current-task pointer.
4. One bead/task contract format.
5. One primary authority per task.
6. Generated-output demotion.
7. Session start, checkpoint, closeout, and handoff commands.
8. Recorded checks.
9. Closeout evidence and review decision.
10. Manual approval before the next task becomes active.
11. A validator for the core invariants.

Everything else can be added after the user sees a real failure mode that the extra layer would prevent.
