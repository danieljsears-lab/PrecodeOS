# PrecodeOS Daily Cockpit
<!-- ANCHOR: precode-daily-cockpit -->

> AUTHORITY: Student-first daily command, prompt, report, recovery, check, and learning reference for operating PrecodeOS during normal work.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, PRD approval, bead activation, implementation acceptance, generated progress state, destructive repair approval, or deep architecture guidance.
> LOAD_WHEN: A student is starting, steering, checking, closing, recovering, or learning from a PrecodeOS session and needs one practical daily surface.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.20
Last updated: 2026-06-26

Use this cockpit while you work with an AI coding agent.

PrecodeOS gives you a small daily control surface: prompts to paste, reports to run, checks to understand, recovery paths to use, and learning loops to keep the project improving.

This page is prompt-first. When a command exists, the command is shown too, but the safest daily habit is to ask the agent to explain what it is doing before it changes anything.

If the optional local `precode` console command is installed, treat it as a shortcut over the shown commands. It prints the underlying script command and does not approve work, transitions, setup mutation, releases, or generated evidence as authority.

Generated reports are evidence only. Before work resumes, return to `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, the active bead, the primary authority file, and your explicit approval.

For the deeper operating manual, see `PRECODE-USER-GUIDE.md`. For Claude Code classroom habits, see `CLAUDE-CODE-FIELD-GUIDE.md`. For symptom lookup, see `PRECODE-TROUBLESHOOTING.md`. For the full prompt source, see `../tasks/reference/PROMPT-PATTERNS.md`. For recovery details, see `../tasks/reference/RECOVERY-PROTOCOL.md`. For release readiness before user-facing shipping risk, see `../tasks/reference/RELEASE-READINESS-PROTOCOL.md`.

## Where Your Work Lives

Use this cockpit to find the right surface before asking an agent to continue.

| Question | Look here | What it decides |
|---|---|---|
| What is active right now? | `tasks/todo.md`, the active bead, and the bead's primary authority file | The current work boundary, files in play, checks, stop conditions, and approval gates. |
| Where do future ideas go? | `CANDIDATE-QUEUE.md` with the Candidate Queue Protocol | Parked intent, evidence, review order, and promotion target. It does not choose the active task or authorize implementation. |
| Where do product or requirement decisions live? | Owner files such as `PRODUCT.md`, `FEATURES.md`, `ACCEPTANCE.md`, and approved PRDs in `tasks/prds/` | Reviewed product truth, requirements, acceptance criteria, and PRD destinations before executable beads. |
| What proof or status exists? | Recorded checks, `PROGRESS.md`, `OS-HEALTH.md`, and `logs/*` | Evidence for review. Generated reports and logs do not approve work, choose tasks, or replace owner files. |
| What if something feels wrong? | `I am stuck, help me`, `PRECODE-TROUBLESHOOTING.md`, and the Recovery Protocol | A stop-and-diagnose path before repair, rollback, overwrite, setup mutation, or transition approval. |
| What did we learn? | The learning diary, bead build journal, Build Attribution Ledger, and reviewed memory | Lessons, path visibility, and who-built-what evidence. These are evidence only until promoted through the right owner file or reviewed closeout. |
| Was this hypothesis tested? | Hypothesis Review / Learning Loop | Learning status, outcome, stale or untested signals, and the next safe Precode workflow. It does not approve product direction, rank candidates, activate beads, require analytics, or create a database. |

If you only remember three checks, ask: what is active, where should future intent live, and what proof still needs review or approval?

## Quick Daily Loop

These prompt aliases are the lean daily surface. The expanded prompt wording lives in `../tasks/reference/PROMPT-PATTERNS.md` and the owning protocols. Aliases do not reduce the guardrails: active memory and owner files stay authoritative, generated reports stay evidence only, and explicit approval is still required before PRD approval, bead activation, review acceptance, transition approval, setup/update mutation, destructive commands, external mutation, merge, release, rollback, or scope expansion.

| Moment | Lean prompt alias | What it should produce |
|---|---|---|
| Start | `Start: run the Precode session start and explain the Context Pack before editing.` | Current bead, done-when target, files in play, checks, stop conditions, open questions, generated-report warning. |
| Ask docs | `Ask Precode: answer my stable docs question and cite the source files.` | A cited docs/protocol answer, or a stop-and-route message when the question depends on current project state. |
| Choose path | `Choose: use Workflow Selection before work starts.` | A workflow recommendation without coding or task activation. |
| First PRD walkthrough | `First PRD: use First PRD Walkthrough for my rough idea.` | A beginner path from rough idea to PRD readiness; the expanded prompt says `Use First PRD Walkthrough for my rough idea`, summarizes a Product Brief, produces a Conviction Packet, and prepares a Local Source Intake handoff. Evidence only until Local Source Intake and later human PRD approval. |
| Review candidates | `Queue: review Candidate Queue as parked intent.` | Candidate status, evidence, research needs, promotion target, and what cannot be decided from the queue. |
| Review hypothesis | `Hypothesis: use Hypothesis Review / Learning Loop.` | Evidence-only learning status and next workflow, not approval or task selection; status may be untested, tested, narrowed, killed, promoted, stale, or not applicable. |
| Build-react-learn | `Build-react-learn: run one tiny reversible prototype bead.` | A bounded prototype-bead path plus evidence-only learning decision; not PRD approval, implementation acceptance, task selection, or transition approval. |
| Clarify acceptance | `Acceptance: review vague criteria with optional EARS-style wording.` | Clearer expected behavior for PRD or acceptance review. Do not require EARS syntax, approve the PRD, activate beads, treat wording as proof, or code. |
| Confirm | `Confirm: name the active bead, authority, files, first check, and stop conditions before editing.` | A bounded task explanation before implementation begins. |
| Team lane | `Team: use the Small Team Collaboration Lane before anyone edits.` | Team coordination guidance without automatic activation, merge, GitHub mutation, or multiple active beads in one checkout. |
| Build | `Build: work only on the active bead.` | Scoped implementation inside the approved files and task boundary. |
| Prove | `Prove: show recorded evidence and what I should verify.` | Recorded proof, failures or blockers, and any manual verification needed. |
| Release prep | `Release: prepare release evidence without release action.` | Shipping evidence and approval questions without deployment, merge, rollback, external mutation, or release approval. |
| Trace proof | `Trace: map this requirement or bug behavior to proof.` | A compact proof trace without acceptance or generated-proof authority. |
| Review attribution | `Attribution: review who-built-what evidence.` | A who-built-what evidence review without approval, blame, scoring, telemetry, or registry behavior. |
| Reverse | `Reverse: use the Implemented Bead Reversal Workflow.` | A safe reversal plan or candidate bead shape without rollback automation or history rewriting. |
| Ralph | `Ralph: run a bounded dry run only.` | Retry evidence for one active bead without accepting work or activating anything. |
| Learn | `Learn: explain the learning diary, bead journal, and attribution evidence.` | A lesson summary plus implemented-bead path, build-change context, and attribution evidence that stays evidence-only. |
| Close | `Close: run session close and summarize changes, checks, blockers, and approvals.` | Closeout readiness, health, validation, transition blockers, learning diary update, bead build journal context, and attribution evidence when present. |
| Recover | `I am stuck, help me.` | A prescriptive recovery response: symptom, first safe move, owner surface, up to three read-only checks, next safe action, and forbidden actions before repair. |
| Named fallback | `Fallback: use the No-Engineer Fallback Prompt Pack for this symptom.` | A symptom-specific recovery prompt for agent-lost, checks-failed, app-will-not-start, approved-too-much, copied-wrong-files, or stop-or-continue moments. |

## Core Prompts

### Ask A Stable Docs Question

Use when you need to understand a PrecodeOS concept, find the right guide, or ask a stable documentation question.

```text
Use Ask Precode.

Answer my stable PrecodeOS documentation question from README.md, docs/*.md, and relevant tasks/reference/*.md. Cite the source files.

If my question depends on current project state, active memory, generated reports, local errors, private maintainer context, or what to do next, stop and route me to the right Precode workflow instead.

Return: Short answer, Sources, What this does not decide, and Next safe prompt.
```

Expected output: a cited docs/protocol answer, plus a clear warning when the question should move to Session Start, Workflow Selection, Troubleshooting, or another current-state workflow.

### Start The Session

Use when you begin or need to reset the working context.

```text
Run the Precode session start. Explain the Context Pack in plain English: current bead, done-when target, primary authority, files in play, out of scope, checks, stop conditions, open questions, and anything generated that must not be treated as instructions.
```

Command:

```bash
python3 scripts/precode_cli.py start
bash scripts/session-start.sh
```

Expected output: the active memory reminder, current bead, done-when target, files in play, checks, stop conditions, Goal Frame status if present, router guidance, and generated-report warning.

### Confirm The Task Before Editing

Use when the agent looks ready to code but has not explained the boundary.

```text
Before editing, confirm the active bead, the primary authority file, the files in play, the first check you expect to run, and what would make you stop or ask me.
```

Expected output: a plain-English boundary for the current task. If the agent cannot name the bead, owner file, files in play, and checks, do not let implementation continue.

### Choose The Right Workflow

Use when you are not sure whether the next move is intake, PRD work, bead work, review, recovery, or handoff.

```text
Use the Workflow Selection Protocol. Tell me the current situation, recommended workflow, artifact to produce next, required authority source, user approval needed, stop condition, and generated-report warning before doing work.
```

Command:

```bash
python3 scripts/workflow-check.py
```

Expected output: advisory workflow warnings or confirmation. Workflow guidance does not approve work, activate a bead, or replace the active bead.

### Review Parked Candidates

Use when you want to inspect ideas, not-yet items, research leads, or possible future beads without turning them into active work.

```text
Use the Candidate Queue Protocol.

Review CANDIDATE-QUEUE.md as parked intent, not task authority. Tell me what ideas are parked, which need research, which are worth shaping, which are blocked or stale, which might become PRDs, which approved PRDs have candidate beads, and which reviewed candidates have product-value ratings, themes, or near-bead sketches.

Also tell me what the Candidate Queue cannot answer: the active task, what the agent should build next, whether a PRD is approved, whether a bead is active, or whether a ranked item is authorized for implementation.

Do not update active memory, approve a PRD, activate a bead, reserve B### bead IDs, treat product-value rating as implementation priority, choose next work, or start coding.
```

Expected output: candidate status, evidence used, recommended next path, promotion target, user approval needed, stop condition, and generated-report warning.

### Coordinate A Small Team

Use when 2-5 people need to work on the same product build.

```text
Use the Small Team Collaboration Lane.

We have [2-5] people working on this product. Help us define the coordinator, product decision owner, contributor roles, branch/worktree rules, candidate parallel beads, review gates, merge/re-entry rules, and forbidden actions before anyone edits.
```

Expected output: the team situation, coordinator and decision owner, branch/worktree rule, candidate parallel beads, teammate startup prompt, review and merge evidence, approval gates, stop conditions, promotion path, and generated-report warning. The lane does not activate multiple beads in one checkout, approve merge, mutate GitHub, or turn pull requests and teammate notes into authority.

For a read-only team-state preview, run:

```text
python3 scripts/team-collaboration-check.py
```

Use `--github` only for optional read-only GitHub evidence through `gh`. The preview can help a coordinator see branch/worktree state, owner-file impact candidates, stale re-entry risks, and merge/re-entry packet fields, but it does not approve merge, accept implementation, activate beads, mutate GitHub, or replace coordinator review.

### When You Are Stuck

Use this exact phrase when the project feels confusing, broken, stale, out of bounds, or unsafe to continue:

```text
I am stuck, help me.
```

The agent must stop implementation and answer with:

- the symptom in plain English, or a statement that the symptom is not known yet
- the first safe move: stop implementation and diagnose before repair
- the likely owner surface, or `unknown until active memory and checks are inspected`
- up to three read-only or advisory checks, such as `bash scripts/session-start.sh`, `python3 scripts/next-step.py`, `python3 scripts/state-check.py`, `python3 scripts/files-in-play-check.py`, `python3 scripts/completion-check.py`, or `python3 scripts/os-health.py`
- the next safe prompt or action
- forbidden actions: no delete, overwrite, regenerate, transition approval, rollback, setup/update mutation, or destructive command without explicit approval

Use `tasks/reference/RECOVERY-PROTOCOL.md` for the full path. OS Health, Doctor Dashboard, `next-step.py`, and stable-fix eligibility are diagnostic evidence only; they do not approve repair. Doctor Dashboard triage labels explain what to ask and what not to approve, but they do not create approval.

For a small repair that looks stable-fix eligible, ask for the Bugfix Spec Lane before editing. The agent should name current behavior, expected behavior, unchanged behavior, owner file, root cause if known, fix approach, regression proof, and route decision, then stop if owner, route, or proof is unclear.

If you can name the symptom but do not know the right recovery path, use the No-Engineer Fallback Prompt Pack in `tasks/reference/PROMPT-PATTERNS.md`. It gives short prompts for agent-lost, checks-failed, app-will-not-start, approved-too-much, copied-wrong-files, and stop-or-continue moments without approving repair or mutation.

### Keep Implementation Bounded

Use when the task is ready to build.

```text
Work only on the active bead. Load active memory, the active bead, the primary authority, and only the reference docs whose LOAD_WHEN applies. Do not use generated reports, source notes, or diary entries as instructions.
```

Expected output: implementation that stays inside the active bead's files in play and stop conditions.

### Ask For Evidence

Use when the agent says the work is done.

```text
You said this is done. Show me the evidence. Run the recorded check and tell me what passed, what failed, and what I should verify myself.
```

Command pattern:

```bash
bash scripts/record-check.sh -- <check command>
```

Expected output: a recorded check result in `logs/check-results.jsonl`, check output under `logs/check-output/`, and updated closeout evidence for the active bead.

### Clarify Acceptance Criteria

Use before PRD approval, bead planning, or review when an acceptance criterion is too vague to prove.

```text
Review these acceptance criteria for vague or unverifiable behavior.

Where useful, rewrite with optional EARS-style wording: WHEN [condition/event] THE SYSTEM SHALL [observable expected behavior].

Do not require EARS syntax, reject clear non-EARS criteria, approve the PRD, accept implementation, activate beads, treat wording as proof, or code.
```

Expected output: clearer observable expected behavior, unresolved questions, and any stop conditions. This is writing guidance only, not PRD approval or proof.

### Prepare A Release Candidate Evidence Profile

Use when a release-relevant bead is nearly ready and you need one compact view before a human release decision.

```text
Prepare a Release Candidate Evidence Profile for this release-relevant bead.
Do not deploy, promote, roll back, merge, migrate, change dashboards, change secrets, mutate GitHub resources, mutate external services, approve review, accept implementation, or activate the next bead.
Show candidate label, release target, changed surfaces, affected users or workflows, recorded checks and results, smoke path and result, browser or manual verification status, docs or support freshness, rollback or blocked escape, known risks and remaining uncertainty, approvals still required, and decision state.
Use only one decision state: candidate, needs evidence, blocked, or ready for human release decision. Make clear that ready for human release decision is not release approval.
```

Expected output: a human-authored evidence profile. It prepares a release decision; it does not approve release, deploy, merge, roll back, or mutate external systems.

### Run A Bounded Ralph Attempt

Use when the active bead is testable, has clear checks, and you want bounded retry evidence instead of a disappearing chat attempt.

```text
Run a bounded Ralph dry run for this bead. Show the attempt budget, validator set, decision, failure category, and whether another attempt is allowed. Do not treat Ralph as acceptance or transition approval.
```

Command:

```bash
python3 scripts/ralph-loop.py --dry-run
```

Expected output: a Ralph decision such as `retry`, `ask`, `review`, or `stop`. Without `--dry-run`, Ralph writes `logs/ralph-attempts.jsonl` and `logs/ralph-summary.md` as generated evidence only.

### Checkpoint Mid-Session

Use when context feels crowded, the task got fuzzy, or you may need to pause.

```text
Checkpoint the session. Tell me whether we should continue, repair, split, pause for manual testing, or close. Include what changed, what evidence exists, and what is still uncertain.
```

Command:

```bash
bash scripts/checkpoint.sh
```

Expected output: current bead state, done-when target, files in play, blockers, Build Loop Health, and a handback-style summary.

### Close The Session

Use when work is done for now or you need a clean stop.

```text
Run session close. Summarize what changed, what checks ran, what remains blocked, and what still requires my approval.
```

Command:

```bash
bash scripts/session-close.sh
```

Expected output: closeout refresh, recorded validation, OS Health refresh, transition readiness, completion or handoff warnings, learning diary update, and bead build journal update when that generated report is available.

## Runnable Reports

Only use these as evidence. They help you understand the project; they do not choose tasks or approve work.

| Report or command | Run it when | What the output means |
|---|---|---|
| `bash scripts/session-start.sh` | Starting or resetting daily work. | Shows the context pack and router guidance. Treat it as orientation before work. |
| `python3 scripts/next-step.py` | You ask "what now?" | Shows generated next-step guidance. It is not transition approval. |
| `python3 scripts/os-health.py` | You need a refreshed health report. | Writes `OS-HEALTH.md`, `logs/os-health.json`, the Doctor Dashboard diagnostic summary with plain-English triage labels, and the generated work graph reports; warnings mean inspect source state and evidence. |
| `bash scripts/checkpoint.sh` | Context is long, fuzzy, or ready to hand back. | Prints a checkpoint and Build Loop Health. Use it to pause or regain clarity. |
| `bash scripts/session-close.sh` | Ending work or preparing review. | Refreshes closeout, validation, health, transition readiness, learning diary, and bead build journal when available. |
| `bash scripts/handoff.sh [next-agent]` | Switching tools or handing work to another agent. | Produces a context pack for the next agent. It does not activate the next bead. |
| `python3 scripts/loop-health.py` | You want a compact loop-health signal. | Shows whether the current build loop is focused, stoppable, closeable, evidenced, and graph-coherent. |
| `python3 scripts/loop-health.py --verbose` | The compact signal is unclear. | Shows dimension-level warnings, including work-graph warnings, for deeper diagnosis. |
| `python3 scripts/ralph-loop.py --dry-run` | A Ralph-enabled bead needs bounded retry evidence. | Runs the Ralph validator set and returns retry/review/ask/stop guidance. It does not accept work. |
| `python3 scripts/update-learning-diary.py --append` | You need to append a learning entry after closeout evidence. | Updates `logs/learning-diary.md`; the diary is evidence, not active memory. |
| `python3 scripts/update-bead-build-journal.py --append` | You need to append an implemented-bead path entry after closeout evidence. | Updates `logs/bead-build-journal.md/jsonl`; the journal is evidence, not active memory, Candidate Queue authority, or acceptance. |
| `logs/bead-build-journal.md` | You need to understand the path of already-worked beads or what implementation-relevant work changed for a bead. | Generated implemented-bead path and build-change journal; evidence only. Session-close entries do not accept work. |
| `python3 scripts/build-attribution-ledger.py` | You need to inspect who built what across beads. | Prints generated attribution JSON from bead closeout and supporting hints; evidence only, not acceptance, merge approval, blame, scoring, telemetry, or a registry. |
| `logs/build-attribution-ledger.md` | You need a readable who-built-what evidence view. | Generated attribution ledger; closeout-reviewed attribution is strongest, while Git authorship remains a hint. |
| `python3 scripts/update-memory-index.py` | Reviewed memory cards changed. | Refreshes the searchable memory index. Memory remains evidence only. |

## Checks By Student Question

### Is My State Okay?

Commands:

```bash
bash scripts/validate-memory.sh
python3 scripts/state-check.py
```

Green means active memory and current bead state look coherent. Warnings or failures mean repair source files before coding. Do not trust generated reports more than active memory.

### Is Scope Widening?

Commands:

```bash
python3 scripts/files-in-play-check.py
python3 scripts/files-in-play-check.py --command "<command summary>"
python3 scripts/files-in-play-check.py --edit-lock
```

Green means changed paths fit the current bead or generated evidence. Warnings mean stop and classify each path as generated evidence, current-bead work that needs explicit scope approval, follow-up work, or user-owned revert work. A command classification of `approval needed` or `stop` means do not run the command yet. A `continue` classification for local mutation still has to stay inside `files_in_play`.

### Is This Done?

Commands:

```bash
python3 scripts/completion-check.py
bash scripts/record-check.sh -- <declared bead check>
```

Green means recorded evidence and closeout are closer to review-ready. Missing or failing checks mean the bead is not accepted yet. Completion output does not accept work by itself.

### Should Ralph Retry?

Command:

```bash
python3 scripts/ralph-loop.py --dry-run
```

Use Ralph only for one active bead with clear checks and retry boundaries. A `review` decision means evidence may be ready for human review; it does not mean accepted.

### Is The Workflow Right?

Commands:

```bash
python3 scripts/workflow-check.py
python3 scripts/orchestration-check.py
python3 scripts/decomposition-check.py
```

Green means the current path appears aligned with the active workflow. Warnings may mean the work needs intake, PRD shaping, decomposition, review, repair, or a narrower bead before implementation.

### Can I Transition?

Command:

```bash
python3 scripts/bead-transition.py
```

Green readiness may show a next bead proposal. Transition still requires explicit approval:

```bash
python3 scripts/bead-transition.py --approve
```

Do not approve transition until review is accepted, manual verification is clear, and latest recorded checks pass.

### What Does This Warning Mean?

Commands:

```bash
python3 scripts/context-check.py
python3 scripts/run-contract-check.py
python3 scripts/tool-execution-check.py
python3 scripts/memory-check.py
python3 scripts/pattern-check.py
python3 scripts/long-horizon-check.py
```

Warnings are advisory evidence. They tell you what to inspect, split, repair, approve, or defer. They do not give the agent permission to widen scope.

## Recovery Methods

Use recovery when something feels wrong. The first move is always to stop implementation and make the state visible.

| Symptom | Prompt | First check |
|---|---|---|
| Active state is confusing | `Stop implementation. Compare tasks/todo.md with the active bead and tell me which canonical file needs repair before work continues.` | `python3 scripts/state-check.py` |
| Generated report looks wrong | `This generated report looks wrong. Tell me which source files and scripts own it, what evidence it summarizes, and how to refresh it without treating the report as authority.` | `python3 scripts/state-check.py` |
| Proof is missing | `Run a completion check and show which declared checks are missing, failing, or stale. Do not recommend acceptance from confidence.` | `python3 scripts/completion-check.py` |
| Implemented bead needs reversal | `This already-implemented bead may need to be reversed or superseded. Use PRD-023. Preserve the old bead as history and propose a separate reversal bead with proof.` | `python3 scripts/completion-check.py` |
| Scope expanded | `Run the files-in-play guardrail. If any changed path is outside this bead, stop and explain whether it is generated evidence, current-bead work, or a separate follow-up.` | `python3 scripts/files-in-play-check.py` |
| Context is lost | `Prepare a compact Context Pack before continuing. Reload active memory, the active bead, and the primary authority before recommending action.` | `python3 scripts/context-check.py` |
| Approval happened too quickly | `Before proposing or activating the next bead, explain what evidence proves this bead is complete and what still requires my approval.` | `python3 scripts/bead-transition.py` |

Do not repair by deleting files, overwriting user edits, hand-editing generated reports, force-resetting git, or approving transitions unless the user explicitly approves that exact action.

## Daily Learning Loop

Learning matters because Precode should make you more capable over time, not just move the repo forward.

| Learning action | Prompt | Output |
|---|---|---|
| Read the lesson | `Read the generated learning diary and explain what I should understand from the last session. Do not use the diary as active memory, a task plan, or implementation instructions.` | A plain-English session lesson from `logs/learning-diary.md`. |
| Understand build changes | `Read the generated bead build journal if it exists. Tell me the path of already-worked beads, what changed for the current bead, what evidence supports it, and what remains uncertain. Do not use the journal as active memory, Candidate Queue authority, or acceptance.` | A plain-English implemented-bead path and build-change summary from `logs/bead-build-journal.md` when available. |
| Search reviewed memory | `Search reviewed memory for what we have learned about this topic. Cite the memory cards you used, treat memory as evidence only, and return to active memory and the active bead before recommending action.` | Relevant reviewed memory cards with source pointers. |
| Propose memory | `Turn this diary lesson into a proposed memory card for my approval. Do not write it until I approve, and tell me whether it should remain memory or be promoted to DECISIONS.md, a PRD, or another authority file.` | A proposed memory card or promotion recommendation. |
| Check memory quality | `Run the memory index and memory check. Tell me whether any memory is stale, missing source pointers, acting like authority, or needs promotion.` | Memory warnings or confirmation. |

Commands:

```bash
python3 scripts/update-learning-diary.py --append
python3 scripts/update-memory-index.py
python3 scripts/memory-check.py
```

Memory is reviewed evidence. It can help future agents understand lessons, preferences, glossary terms, risks, and source pointers. It does not replace `DECISIONS.md`, PRDs, beads, active memory, or current code.

## Appendix: Stop Signals

Stop the agent when:

- it cannot name the active bead, files in play, checks, or stop conditions
- it starts coding from a generated report, diary entry, source note, or old chat
- it touches files outside the active bead without explaining why
- it says work is done without recorded evidence or manual verification
- it wants to approve the next bead without explicit user approval
- it proposes deleting, overwriting, force-resetting, migrating, deploying, exposing secrets, or changing external services without exact approval
- it keeps asking implementation questions when the product problem, user, scope, or authority file is still unclear

Use this prompt:

```text
STOP. Do not make any more changes. Tell me exactly where we are: active bead, primary authority, files changed, evidence recorded, blockers, and the safest next action.
```

## Appendix: Approval Gates

You must explicitly approve:

- starting a new bead or transition with `python3 scripts/bead-transition.py --approve`
- destructive commands, broad overwrites, deletes, moves, force resets, migrations, deploys, dashboard changes, secrets, billing, auth, payments, or private data actions
- edits to Precode control-layer files when the active bead does not include them
- PRD approval, review acceptance, manual verification claims, and changes that widen task scope
- memory-card writes or promotion of a lesson into `DECISIONS.md`, a PRD, or another authority file

When in doubt, ask:

```text
Before continuing, show the allowed actions, proof needed, approval required before risky actions, stop conditions, and rollback or blocked escape path. Then run python3 scripts/run-contract-check.py.
```
