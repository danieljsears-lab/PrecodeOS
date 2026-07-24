# PrecodeOS Daily Cockpit
<!-- ANCHOR: precode-daily-cockpit -->

> AUTHORITY: Builder-first daily command, prompt, report, recovery, check, and learning reference for operating PrecodeOS during normal work.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, PRD approval, bead activation, implementation acceptance, generated progress state, destructive repair approval, or deep architecture guidance.
> LOAD_WHEN: A builder is starting, steering, checking, closing, recovering, or learning from a PrecodeOS session and needs one practical daily surface.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.44
Last updated: 2026-07-20

Use this cockpit first once PrecodeOS is installed or you are already working inside a PrecodeOS repo. Stop here for normal work unless this page routes you to a specific setup, manual, troubleshooting, or protocol surface. If a first session feels too large, use `../tasks/templates/PRECODE-FIRST-SESSION-CARD.md` as the compact linear builder build-order card, then return here.

PrecodeOS gives you a small daily control surface: prompts to paste, reports to run, checks to understand, recovery paths to use, and learning loops to keep the project improving.

First-reader route:

| Situation | Go here |
|---|---|
| PrecodeOS is not installed in the target project | `PRECODE-GUIDED-SETUP.md` |
| PrecodeOS is installed or work is resuming | Stay in this Daily Cockpit |
| You only have a rough idea | `Ideation: use First PRD Walkthrough for my rough idea.` |
| Setup, state, checks, or generated reports feel broken | `PRECODE-TROUBLESHOOTING.md` or `I am stuck, help me.` |

This page is prompt-first. When a command exists, the command is shown too, but the safest daily habit is to ask the agent to explain what it is doing before it changes anything.

If the optional local `precode` console command is installed, treat it as a shortcut over the shown commands. It prints the underlying script command and does not approve work, transitions, setup mutation, releases, or generated evidence as authority. If the optional npm `precodeos` entry is used, keep it in the setup or existing-Precode refresh lane only; it runs read-only previews and is not the normal cockpit surface.

Generated reports are evidence only. Before work resumes, return to `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, the active bead, the primary authority file, and your explicit approval.

Document roles are intentionally narrow: `../README.md` is the public package compass, `PRECODE-GUIDED-SETUP.md` is setup-only, this cockpit is the beginner-facing operating home base, `PRECODE-USER-GUIDE.md` is the deeper operating manual, `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` is the educational bridge, and `PRECODE-OS-README.md` is the conceptual Builder OS explainer. For Claude Code classroom habits, see `CLAUDE-CODE-FIELD-GUIDE.md`. For symptom lookup, see `PRECODE-TROUBLESHOOTING.md`. For a compact first-session aid, see `../tasks/templates/PRECODE-FIRST-SESSION-CARD.md`. For the full prompt source, see `../tasks/reference/PROMPT-PATTERNS.md`. For recovery details, see `../tasks/reference/RECOVERY-PROTOCOL.md`. For release readiness before user-facing shipping risk, see `../tasks/reference/RELEASE-READINESS-PROTOCOL.md`.

`../tasks/templates/PRECODE-FIRST-SESSION-CARD.md` is a small aid behind this cockpit. It is useful when a new builder needs one page of prompts, checks, and build-order guidance, but it does not become a start page, task selector, approval shortcut, setup guide, router, command wrapper, or protocol replacement.

## Command Surface Triage

Use the smallest command set that matches your moment. Command surface triage is reader guidance only; it does not approve work, change tool-call classes, choose tasks, or make generated reports authoritative.

| Moment | Start here | Deeper commands |
|---|---|---|
| Beginner daily work | `bash scripts/session-start.sh`, `python3 scripts/next-step.py`, `python3 scripts/loop-health.py`, `python3 scripts/os-health.py`, `bash scripts/record-check.sh -- <command>` | Use this cockpit and the active bead before opening support, maintainer, or advanced checks. |
| Setup, support, or recovery | `docs/PRECODE-GUIDED-SETUP.md`, `docs/PRECODE-SUPPORT-RUNBOOK.md`, `docs/PRECODE-TROUBLESHOOTING.md` | `bootstrap-check.py`, `existing-repo-intake.py`, `validate-memory.sh`, `file-inventory.py --check`, `state-check.py`, `files-in-play-check.py`, `completion-check.py`, and `bead-transition.py --json` belong here when the symptom calls for them. |
| Advanced evidence or review | The explicit prompt alias or owner protocol for the stage | Ralph, Candidate Queue, Attribution, Team, PRD handoff, Release, Trace, and review commands are conditional surfaces, not daily starting points. |
| Maintainer validation | Maintainer package work only | Public repo/package checks and generated docs or roadmap checks stay out of the beginner daily loop. |

The optional `precode` facade is only a shortcut over canonical commands. If command output sounds like approval, return to owner files, proof, and explicit user approval.

## Beginner Path

Use this path before opening more documents:

First-product spine: `Idea -> Brief -> Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close`.

- Idea: rough idea or messy notes.
- Brief: Product Brief after at most three high-level questions.
- Packet: reviewed Conviction Packet / Precode Ingestion Packet.
- Packet handoff: reviewed Conviction Packet / Precode Ingestion Packet with Local Source Intake readiness self-check.
- Intake: Local Source Intake summary.
- PRD: human-reviewed PRD shaping and approval.
- Bead: candidate decomposition, then approved active bead.
- Proof: recorded checks and manual evidence.
- Review: human review, with advisory lanes only when needed.
- Close: closeout evidence and explicit Close State.

1. If PrecodeOS is not in the project yet, stop here and use `PRECODE-GUIDED-SETUP.md`.
2. If you only have a rough idea, use `Ideation: use First PRD Walkthrough for my rough idea.` Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and PRD shaping are steps in that path, not separate commands to choose between.
3. If PrecodeOS is set up and work exists, run Start, Check, then use Build, Prove, Review, Close, or Recover from the loop below.
4. If something feels broken or confusing, say `I am stuck, help me.` Use Troubleshooting for symptom lookup and the Recovery Protocol for the full repair contract.

Advanced surfaces are conditional support, not parallel starting points. Review Lanes, Release Readiness, Goal Frames, Ralph, Attribution, Hypothesis Review, Plan Loop, Build-React-Learn, Artifact Chooser, Ask Precode, role lenses, skill-style help, team coordination, reversal, and proof tracing are available only when the current stage, risk, recovery path, support role, stable-docs question, proposed extension, or explicit user question calls for one.

## Plan Mode Candidate Craft Loop

Use this loop when an idea or feature angle should become future work before any build starts:

`Idea -> Plan Mode -> Candidate Queue -> Plan Mode -> Implementation Plan -> Approved Bead -> Build`

Plan Mode is required at two gates:

- Before developing a Candidate Queue entry from an idea, feature angle, not-yet item, or rough implementation thought.
- Before developing an implementation plan for a selected candidate.

Tool notes: in Codex, use `/plan`; in Claude Code, use Plan Mode; in other agents, use an equivalent read-only planning mode.

This loop teaches staged commitment. A Plan Packet, Candidate Queue entry, or implementation plan is evidence only. It does not approve a PRD, rank work for implementation, activate a bead, update `tasks/todo.md`, authorize coding, or skip the normal owner-file, decomposition, proof, review, and transition gates.

## Every-Bead Rhythm

After the first bead, use this small repeated rhythm instead of rereading every surface:

`Active -> Changed -> Proven -> Parked -> Approval -> Next`

- Active: name `tasks/todo.md`, the active bead, and the primary authority file.
- Changed: summarize the changed files or behavior inside the active bead.
- Proven: show recorded checks, manual verification, proof traces, and review evidence.
- Parked: name future intent only when it belongs in `CANDIDATE-QUEUE.md`, PRD amendment, a decision, a follow-up bead proposal, defer, or kill.
- Approval: name review decision, transition proposal, release or merge approval, and any user input still required.
- Next: route to session start, Workflow Selection, `next-step.py`, or an explicit transition proposal without activating anything.

This rhythm is a checklist, not a workflow. It does not choose tasks, rank Candidate Queue items, approve PRDs, activate beads, accept review, approve transition, replace closeout, replace `next-step.py`, or make generated reports authoritative.

## Where Your Work Lives

Use this cockpit to find the right surface before asking an agent to continue.

| Question | Look here | What it decides |
|---|---|---|
| What is active right now? | `tasks/todo.md`, the active bead, and the bead's primary authority file | The current work boundary, files in play, checks, stop conditions, and approval gates. |
| Where do future ideas go? | `CANDIDATE-QUEUE.md` with the Candidate Queue Protocol | Parked intent, evidence, review order, and promotion target. It does not choose the active task or authorize implementation. |
| How do I turn an idea into a candidate? | Plan Mode Candidate Craft Loop | Use Plan Mode first, then propose a Candidate Queue entry for review. Use Plan Mode again before any implementation plan. The loop is evidence only until normal approval gates are satisfied. |
| Where do product or requirement decisions live? | Owner files such as `PRODUCT.md`, `FEATURES.md`, `ACCEPTANCE.md`, and approved PRDs in `tasks/prds/` | Reviewed product truth, requirements, acceptance criteria, and PRD destinations before executable beads. |
| What proof or status exists? | Recorded checks, `PROGRESS.md`, `OS-HEALTH.md`, and `logs/*` | Evidence for review. Generated reports and logs do not approve work, choose tasks, or replace owner files. |
| What if something feels wrong? | `I am stuck, help me`, `PRECODE-TROUBLESHOOTING.md`, and the Recovery Protocol | A stop-and-diagnose path before repair, rollback, overwrite, setup mutation, or transition approval. |
| What did we learn? | The learning diary, bead build journal, Build Attribution Ledger, and reviewed memory | Lessons, path visibility, and who-built-what evidence. These are evidence only until promoted through the right owner file or reviewed closeout. |
| I need a smaller first-session card. | `../tasks/templates/PRECODE-FIRST-SESSION-CARD.md` | A compact builder build-order checklist and prompt card after setup validates. It reinforces this cockpit and does not choose work, approve setup, activate beads, or replace protocols. |
| Where should this answer live? | `Use Question-To-Artifact Filing for this answer.` | A filing recommendation only: stay in chat, Local Source Intake, Candidate Queue, Memory Promotion Review, PRD/owner-file work, `DECISIONS.md`, decomposition review, defer, kill, or maintainer roadmap note. It does not file automatically, approve promotion, choose tasks, or activate beads. |
| Is this source ready to promote? | Source-To-Promotion Hygiene Review in Prompt Patterns | Checks source refs, evidence strength, open conflicts, proposed owner, promotion action, approval required, and stop condition before any promotion. It does not promote files, approve PRDs, choose tasks, or activate beads. |
| Was this hypothesis tested? | Hypothesis Review / Learning Loop | Learning status, outcome, stale or untested signals, and the next safe Precode workflow. It does not approve product direction, rank candidates, activate beads, require analytics, or create a database. |
| Which artifact, idea, or path do I need? | `Ideation: map my current moment to the right Precode path before PRD shaping or coding.` | A mapped workflow, artifact, or rough-idea path. Artifact Chooser remains an index only; use Workflow Selection when the answer depends on current state. |
| I only have a rough idea. | `Ideation: use First PRD Walkthrough for my rough idea.` | The single beginner-facing path through Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and PRD shaping. These are steps in the path, not competing commands. |
| Which skill-style prompt should I use? | `Use Skill Playbook Ergonomics.` | One recommended invocation or owner surface: Ask Precode, Workflow Selection, Ideation, Review / Acceptance, Skill / Extension Review, a normal protocol, a prompt pattern, an adapter note, a script/check, or no new surface. It does not show a skill catalog, install skills, approve extension implementation, add registries, create optional packs, run mutating commands, or replace owner protocols. |
| Which software role should the agent cover? | `Role lens: use the [role] lens and route me to the existing Precode workflow.` | A role-to-workflow mapping for product manager, researcher, designer, architect, developer, QA/reviewer, security, or deployment language. Role lenses are prompt ergonomics only; they do not create role skills, approve work, activate beads, accept review, or authorize coding. |
| What happens before release? | `Release: prepare release evidence without release action.` | Late-stage release-prep evidence, release-quality cues, and approval questions. It does not deploy, configure providers, mutate dashboards, merge, roll back, certify production readiness, or approve release. |

If you only remember three checks, ask: what is active, where should future intent live, and what proof still needs review or approval?

## Quick Daily Loop

These prompt aliases are the lean daily surface. Start, Ask Precode, Ideation, Check, Acceptance, Queue, Build, Prove, Review, Close, and Recover are the normal first-read loop. The expanded prompt wording lives in `../tasks/reference/PROMPT-PATTERNS.md` and the owning protocols.

Advanced aliases are still available, but they are conditional. Skill map is for mapping a confusing skill-style request to the smallest existing invocation, Quality map is for translating named engineering standards into Precode routing questions, Role lens is for translating product manager, researcher, designer, architect, developer, QA/reviewer, security, or deployment language into existing workflows, Hypothesis is for an existing learning target, Build-react-learn is for a tiny approved exploratory prototype bead, Team is for 2-5 person coordination, Release is for user-facing shipping risk, Trace is for unclear proof, Attribution is for accountability review, Reverse is for implemented-bead reversal, and Ralph is for a testable Ralph-enabled bead.

Aliases do not reduce the guardrails: active memory and owner files stay authoritative, generated reports stay evidence only, and explicit approval is still required before PRD approval, bead activation, review acceptance, transition approval, setup/update mutation, destructive commands, external mutation, merge, release, rollback, or scope expansion.

| Moment | Lean prompt alias | What it should produce |
|---|---|---|
| Start | `Start: run the Precode session start and explain the Context Pack before editing.` | Current bead, done-when target, files in play, checks, stop conditions, open questions, generated-report warning. |
| Ask docs | `Ask Precode: answer my stable docs question and cite the source files.` | A cited docs/protocol answer, or a stop-and-route message when the question depends on current project state. |
| Ideation | `Ideation: map my current moment to the right Precode path before PRD shaping or coding.` | Workflow Selection, First PRD Walkthrough, or Artifact Chooser routing without task approval, artifact generation, PRD approval, bead activation, implementation permission, or later human PRD approval. |
| Clarify acceptance | `Acceptance: review vague criteria with optional EARS-style wording.` | Clearer expected behavior for PRD or acceptance review. Do not require EARS syntax, approve the PRD, activate beads, treat wording as proof, or code. |
| Review candidates | `Queue: review Candidate Queue as parked intent.` | Candidate status, evidence, research needs, promotion target, and what cannot be decided from the queue. If the candidate is being developed or turned into an implementation plan, use Plan Mode first. |
| Check | `Check: name the active bead, authority, files, first check, suitability decision, quality risk, vibe-to-agentic boundary, stop conditions, and every-bead rhythm before editing.` | Confirm, Task Suitability, Engineering Quality Floor, Vibe-To-Agentic Boundary, and Every-Bead Rhythm behavior without coding, task selection, Candidate Queue ranking, implementation-plan approval, review acceptance, transition approval, or a new report. |
| Skill map | `Use Skill Playbook Ergonomics.` | One existing invocation or owner surface, owner protocol, stop condition, and approval reminder. Do not create a skill catalog, install skills, add a registry, create optional packs, approve extension implementation, run mutating commands, or treat skill output as authority. |
| Quality map | `Quality map: translate the relevant engineering standard into a Precode routing question.` | Engineering Quality Standards Taxonomy guidance only: owner protocol or continue path, proof needed, and human approval still required. Do not create a scorecard, certify code quality, certify production readiness, approve implementation, approve review, approve release, or add a new command. |
| Build | `Build: work only on the active bead.` | Scoped implementation inside the approved files and task boundary. |
| Prove | `Prove: show recorded evidence and what I should verify.` | Recorded proof, failures or blockers, and any manual verification needed. |
| Review | `Review: check this work or artifact before I accept it.` | Human review guidance; route to Review Lanes, Engineering Quality Review Lane, PRD Handoff Readiness, release review, or proof tracing only when the current artifact or risk calls for it. |
| Close | `Close: run session close, summarize changes, checks, blockers, approvals, learning context, and end with Close State.` | Closeout readiness, health, validation, transition blockers, learning diary update, bead build journal context, attribution evidence when present, and a final `Close State` line saying whether it is safe to close this tab/session or what input is still needed. |
| Recover | `Recover: I am stuck, help me.` | A prescriptive recovery response plus named fallback prompt when a symptom is known: symptom, first safe move, owner surface, up to three read-only checks, next safe action, and forbidden actions before repair. |

If the generated next-step decision is `author next bead`, treat it as an accepted hold: the current bead is accepted, but transition still needs a next bead proposal or authored bead. Do not continue implementation, repeat acceptance review, approve transition, or activate a bead from that generated classification.

### Advanced / Conditional Surfaces

Use these only when the current stage, risk, evidence gap, support role, or explicit question calls for one. They are not daily starting points.

| Moment | Conditional alias | What it should produce |
|---|---|---|
| Review hypothesis | `Hypothesis: use Hypothesis Review / Learning Loop.` | Evidence-only learning status and next workflow, not approval or task selection; status may be untested, tested, narrowed, killed, promoted, stale, or not applicable. |
| Build-react-learn | `Build-react-learn: run one tiny reversible prototype bead.` | A bounded prototype-bead path plus evidence-only learning decision; not PRD approval, implementation acceptance, task selection, or transition approval. |
| Role lens | `Role lens: use the [role] lens and route me to the existing Precode workflow.` | A role-to-workflow map plus owner source, stop condition, proof or approval needed, and forbidden uses. Role lenses are not role skills, persona agents, approval shortcuts, task runners, or coding permission. |
| Team lane | `Team: use the Small Team Collaboration Lane before anyone edits.` | Team coordination guidance without automatic activation, merge, GitHub mutation, or multiple active beads in one checkout. |
| Delegation re-entry | `Re-entry: review delegated work before continuing.` | Evidence-only return review for solo AFK, teammate branch/worktree, or cloud-agent/PR work; not acceptance, merge approval, transition approval, or external mutation. |
| Release prep | `Release: prepare release evidence without release action.` | Shipping evidence, release-quality cues, and approval questions without deployment, merge, rollback, external mutation, certification, or release approval. |
| Trace proof | `Trace: map this requirement or bug behavior to proof.` | A compact proof trace without acceptance or generated-proof authority. |
| Review attribution | `Attribution: review who-built-what evidence.` | A who-built-what evidence review without approval, blame, scoring, telemetry, or registry behavior. |
| Reverse | `Reverse: use the Implemented Bead Reversal Workflow.` | A safe reversal plan or candidate bead shape without rollback automation or history rewriting. |
| Ralph | `Ralph: run a bounded dry run only.` | Retry evidence for one active bead without accepting work or activating anything. |

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

### Check Task Suitability Before Work

Use when the next request may be too vague, broad, proof-unclear, approval-gated, or easy to mistake for one task.

```text
Check task suitability before work starts. Tell me whether this should continue, clarify, route, split, block, or stop.

Explain the destination, owner source, reviewable change size, proof path, approval gates, stop conditions, and split reasons. If useful, run python3 scripts/task-suitability-check.py --check and treat the output as advisory generated evidence only.

Do not choose tasks, approve a PRD, activate a bead, authorize implementation, accept review, approve commands, create proof, or code.
```

Expected output: an advisory recommendation of `continue`, `clarify`, `route`, `split`, `block`, or `stop`, plus the missing signals or split reasons. It does not approve work.

### Ask For The Engineering Quality Floor

Use when the agent is about to code and you want to confirm it is applying practical engineering judgment without starting a full architecture review.

```text
Before coding, show me the engineering quality standard you are applying here.
```

Expected output: quality risk, simplest acceptable shape, boundary or owner file, evidence to prove the work, and what would make the agent stop or ask for approval. For tiny tasks, this should be short. If the answer reveals architecture, security, data, dependency, deployment, external-service, command-risk, release, or multi-system risk, the agent should route to the existing owner protocol before coding.

If the answer sounds vague, use the advisory checker:

```bash
python3 scripts/engineering-quality-check.py --check
```

Expected output: Check quality text contract warnings about missing quality-risk, simplest-shape, boundary, proof, stop-condition, or routing signals. The Engineering Quality Text-Contract Checker is advisory only; it does not approve coding, review, release, or generated proof, does not inspect app code, and does not create a scorecard or checker gate.

If the agent names a professional standard and you need a plain routing map, use the Standards Taxonomy:

```text
Use the Engineering Quality Standards Taxonomy. Translate the relevant standard into a plain Precode routing question, name the owner protocol or continue path, name the proof needed, and say what still needs human approval.
```

Expected output: a plain Precode routing question, owner protocol or continue path, proof needed, and approval still required. The Standards Taxonomy does not make external frameworks public package authority, certify code quality, certify production readiness, approve coding, approve review, approve release, create a scorecard, or add a new command.

If the text contract looks complete but changed files appear broader than the active bead claims, use the repo-shape preview:

```bash
python3 scripts/engineering-quality-check.py --check --repo-heuristics-preview
```

Expected output: advisory only repo-shape warnings about changed files, files in play, checks, config/dependency touches, docs/protocol/PRD touches, script touches, broad cross-surface edits, or explicit git-unavailable status. It does not inspect app code, run tests or linters, approve coding, accept review, certify production readiness, create proof, or create a checker gate.

### Check The Vibe-To-Agentic Boundary

Use this before coding when you are not sure whether a fast AI sketch is still safe or whether it needs the full Precode loop.

```text
Check whether this is safe to keep as exploratory vibe work or whether it needs governed Precode flow.

Name the risk, reversibility, user-facing impact, sensitive surfaces, files or systems likely to change, proof needed, and next safe path.

If it is exploratory, keep it tiny, reversible, and evidence-only. If it is durable, user-facing, sensitive, multi-file, ambiguous, release-relevant, hard to prove, or likely to be revisited, route me through the right Precode owner workflow before coding.

Do not approve a PRD, activate a bead, accept implementation, approve release, mutate files, create generated proof, or code.
```

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

### Review Delegated Re-Entry Evidence

Use when work returns from solo AFK, a teammate branch/worktree, or a cloud-agent/PR context.

```text
Re-entry: review delegated work before continuing. Name the scope returned, changed files, checks and results, manual verification, approval still required, unresolved risks, external status evidence, forbidden actions not taken, and recommended next human action. Recommend only continue, review, split, block, or handoff. Do not accept implementation, approve merge, approve transition, mutate GitHub, deploy, release, or treat agent summaries, PR status, CI, reviews, or generated reports as authority.
```

Expected output: returned scope, changed files, checks, manual verification, approvals still required, unresolved risks, external evidence if any, forbidden actions not taken, and one next human action. This does not approve implementation, merge, transition, GitHub mutation, or external mutation.

### Step Away From A Bounded Agent Task

Use this only when the active bead is already scoped, has files in play, checks, stop conditions, and you want to know whether it is safe to step away.

```text
Before I step away, confirm whether this bead is only afk_candidate or truly bounded-afk. Show allowed actions, proof needed, approval required before risky actions, stop conditions, rollback or blocked escape, and re-entry evidence. Do not treat AFK metadata as autonomous execution approval.
```

When you return:

```text
I am back. Re-enter this bead safely: reload active memory, active bead, primary authority, changed files, recorded checks, Run Contract if present, stop conditions, proof still missing, and approval still required. Recommend only continue, review, split, or block.
```

Expected output: what changed, what was proven, what stopped or should have stopped, what still needs approval, and the next safe decision. This does not accept implementation, approve commands, activate another bead, or approve small-team merge/re-entry.

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
Show candidate label, release target, changed surfaces, affected users or workflows, recorded checks and results, smoke path and result, browser or manual verification status, docs or support freshness, rollback or blocked escape, release quality cues, known risks and remaining uncertainty, approvals still required, and decision state.
For release quality cues, include CI/status checks, logs or observability signal, configuration/environment parity, performance or scalability expectation, data retention/privacy/security expectation, dependency/runtime freshness, and monitoring/support owner. Use recorded evidence or not applicable with a reason.
Use only one decision state: candidate, needs evidence, blocked, or ready for human release decision. Make clear that ready for human release decision is not release approval.
Do not treat release quality cues as a release gate, production-readiness certification, compliance certification, provider checklist, generated proof, checker gate, deployment approval, rollback approval, release-channel behavior, or package-manager behavior.
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
Run session close. Summarize what changed, what checks ran, what remains blocked, and what still requires my approval. End with `Close State: Safe to close this tab/session. Precode state is recorded; next session should start with session start.` or `Close State: Do not close yet. I still need your approval/input for <specific item>.`
```

Command:

```bash
bash scripts/session-close.sh
```

Expected output: closeout refresh, recorded validation, OS Health refresh, transition readiness, completion or handoff warnings, learning diary update, bead build journal update when that generated report is available, and a final `Close State` line. `Safe to close` means Precode session state is recorded and no immediate user action is needed to preserve or clarify it; it does not approve review, transition, commit, push, deploy, release, rollback, external sync, or any other gated action.

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
| `python3 scripts/task-suitability-check.py --check` | A task may be too vague, broad, proof-unclear, approval-gated, or not ready as one bead. | Prints advisory continue/clarify/route/split/block/stop guidance. It does not choose work or approve implementation. |
| `python3 scripts/loop-health.py --verbose` | The compact signal is unclear. | Shows dimension-level warnings, including work-graph warnings, for deeper diagnosis. |
| `python3 scripts/ralph-loop.py --dry-run` | A Ralph-enabled bead needs bounded retry evidence. | Runs the Ralph validator set and returns retry/review/ask/stop guidance. It does not accept work. |
| `python3 scripts/update-learning-diary.py --append` | You need to append a learning entry after closeout evidence. | Updates `logs/learning-diary.md`; the diary is evidence, not active memory. |
| `python3 scripts/update-bead-build-journal.py --append` | You need to append an implemented-bead path entry after closeout evidence. | Updates `logs/bead-build-journal.md/jsonl`; the journal is evidence, not active memory, Candidate Queue authority, or acceptance. |
| `logs/bead-build-journal.md` | You need to understand the path of already-worked beads or what implementation-relevant work changed for a bead. | Generated implemented-bead path and build-change journal; evidence only. Session-close entries do not accept work. |
| `python3 scripts/build-attribution-ledger.py` | You need to inspect who built what across beads. | Prints generated attribution JSON from bead closeout and supporting hints; evidence only, not acceptance, merge approval, blame, scoring, telemetry, or a registry. |
| `logs/build-attribution-ledger.md` | You need a readable who-built-what evidence view. | Generated attribution ledger; closeout-reviewed attribution is strongest, while Git authorship remains a hint. |
| `python3 scripts/update-memory-index.py` | Reviewed memory cards changed. | Refreshes the searchable memory index. Memory remains evidence only. |

## Checks By Builder Question

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
| Recall reviewed memory | `Run python3 scripts/memory-check.py --query "topic words" --recall. Use exact-match snippets only. Treat weak_match_examples as search leads, not memory to load.` | Concise cited snippets, or explicit no-match guidance without forcing weak memory into context. |
| Propose memory | `Turn this diary lesson into a proposed memory card for my approval. Do not write it until I approve, and tell me whether it should stay reviewed memory, become a card, or be promoted to DECISIONS.md, a PRD, a protocol, an approved bead, or another owner file.` | A proposed memory card or promotion recommendation. |
| Review memory promotion | `Review this memory for promotion. Cite the memory claim, source pointers, current status, proposed owner, promotion action, approval required, and stop condition. Do not create cards, edit owner files, approve PRDs, activate beads, choose tasks, accept implementation, or change active memory without my approval.` | A manual promotion review that keeps memory evidence-only until an owner-file change is approved. |
| Check memory quality | `Run the memory index and memory check. Tell me whether any memory is stale, missing source pointers, acting like authority, or needs promotion.` | Memory warnings or confirmation. |

Commands:

```bash
python3 scripts/update-learning-diary.py --append
python3 scripts/update-memory-index.py
python3 scripts/memory-check.py
```

Memory is reviewed evidence. It can help future agents understand lessons, preferences, glossary terms, risks, and source pointers. It does not replace `DECISIONS.md`, PRDs, beads, active memory, or current code. Search results may name a proposed promotion owner, but promotion is manual and requires explicit approval before any card write, owner-file edit, PRD amendment, protocol update, bead change, or active-memory change.

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
