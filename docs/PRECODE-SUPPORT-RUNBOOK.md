# PrecodeOS Support Runbook
<!-- ANCHOR: precode-support-runbook -->

> AUTHORITY: Public-safe support-engineer field guide for helping a new user capture initial intent, adopt PrecodeOS into a new or existing project, reach a valid first session, and learn the safe operating loop.
> NOT_AUTHORITY: Active memory, product truth, PRD approval, task selection, implementation acceptance, bead transition approval, private support operations, customer records, credentials, dashboard operations, or maintainer roadmap tactics.
> LOAD_WHEN: Supporting a first-time PrecodeOS adoption, guiding a user from idea capture into setup, helping a user run their first safe session, or coaching an agent that is assisting support.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-20

## Purpose

Use this runbook when you are helping someone else adopt PrecodeOS.

The support posture is:

- the user owns product facts, approvals, and risk decisions
- support asks, reflects, challenges, and routes
- the agent may inspect, summarize, propose, and validate
- durable state belongs in Precode owner files, beads, recorded checks, and generated evidence
- no separate support handoff artifact is required

PrecodeOS is not an app to launch. It is a repo-native operating layer: Markdown authority files, task contracts, adapters, scripts, and generated-evidence rules that live inside a project folder.

## Case Priority

Support usually sees these cases in this order:

| Case | Default posture |
|---|---|
| New project | Mainline walkthrough. Capture enough user-owned intent, then set up Precode before product implementation. |
| Existing project | Variant. Preserve existing code, docs, checks, and conventions; adapt Precode around them. |
| First-use operation | Always included. Setup is not done until the user can run a first safe session. |
| Incorrect copy or damaged setup | Rare repair path. Stop, identify the symptom, consult troubleshooting, and validate before resuming. |

## Non-Negotiables

Do not paste or store secrets, credentials, billing details, customer records, private dashboard values, private transcripts, or sensitive personal data in Precode files or prompts.

Do not run broad overwrite commands, install Git hooks, change CI, edit app code, approve a bead transition, or mutate external systems during first setup unless the user explicitly approves a narrow action and the active setup work allows it.

Do not create product truth for the user. If the product is fuzzy, help the user capture a Precode Ingestion Packet or PRD-ready source summary. That packet is evidence only until it is reviewed and placed in the right Precode owner file after setup.

Do not treat `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md`, or files under `logs/` as authority. Generated reports are evidence only.

## Mainline Walkthrough: New Project

### 1. Frame The Session

Start by naming what will and will not happen.

Support can say:

```text
We are going to capture enough of your intent to set up Precode safely. You will own the product facts and approvals. I will help organize them, point out gaps, and stop before anything risky. We are not coding the product yet.
```

Agent guardrail:

```text
Treat this as PrecodeOS support setup, not app implementation. Ask for user-owned facts, summarize them as evidence, and do not edit, copy, overwrite, install hooks, run setup scripts, or write app code until the user approves a narrow setup step.
```

### 2. Capture User-Owned Intent

Ask for enough context to seed owner files later:

- product promise
- intended user
- painful before moment
- better after moment
- smallest useful version
- known constraints
- obvious risks or unknowns

Use plain language. Challenge gently when the answer is broad, solution-first, or unsupported.

Support can say:

```text
I am not going to decide the product for you. I am going to reflect what you said, name assumptions, and ask which parts feel true enough to carry into setup.
```

The output at this point is a Precode Ingestion Packet or PRD-ready source summary in the conversation. It is not a durable PRD yet and does not approve implementation.

### 3. Confirm Source And Target

Before copying anything, identify:

- the clean PrecodeOS package checkout
- the target project folder
- whether the target is empty, nearly empty, or already has project material
- the public file groups that may be copied
- private, generated, local, and secret material that must not be copied
- the validation commands to run after setup

Safe inspection commands:

```bash
git status
find . -maxdepth 2 -type f | sort
```

Stop if the source package and target project are unclear. Mixing them up is the easiest first-time failure.

### 4. Set Up By Supervised File Group

Use `docs/PRECODE-GUIDED-SETUP.md` as the setup guide and `docs/PRECODE-FILE-INVENTORY.md` as the file dictionary.

For a new project, copy public package files by supervised group, not by blind overwrite:

- active memory: `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`
- product and project owner files
- public orientation docs
- agent shims and adapters
- tasks, modes, memory templates, and reference protocols
- scripts, hooks, and workflows only when approved for the target repo
- `logs/LOG-EVIDENCE-TAXONOMY.md`

Exclude `_maintainer/`, generated reports, generated logs, local agent/editor state, caches, virtual environments, env files, secrets, credentials, keys, and certificates.

### 5. Adapt Owner Files

Use the captured user-owned facts to propose minimal setup adaptations:

- `PRODUCT.md`: product promise, users, smallest useful version, success signals, and voice
- `PROJECT-CONTEXT.md`: app directory, stack if known, checks, conventions, integrations, and sensitive boundaries
- `DECISIONS.md`: hard decisions already known
- `tasks/todo.md`: first setup or orientation bead and current state

Support may draft, but the user approves the facts. If a fact is uncertain, mark it as an assumption or open question in the proper owner file rather than presenting it as settled.

### 6. Validate Before First Use

From the target project root, run:

```bash
bash scripts/validate-memory.sh
python3 scripts/file-inventory.py --check
```

If the full script set was not copied, explain which validation is unavailable and why. Do not treat missing validation as success.

### 7. Guide The First Safe Session

Run or ask the agent to run:

```bash
bash scripts/session-start.sh
python3 scripts/next-step.py
```

Then ask the agent to explain:

- active memory
- current bead
- primary authority
- files in play
- checks
- stop conditions
- blockers
- generated-report warning

First safe prompt:

```text
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md, and tasks/todo.md. Then tell me the active bead, primary authority, files in play, checks, stop conditions, and anything blocked. Do not start coding yet.
```

Setup is not complete until the user can explain what the active bead is and when they should stop.

## Existing Project Variant

For an existing project, preserve the project before adapting Precode.

Inspect first:

- current `git status`
- existing README and docs
- package manager and framework files
- real app directory
- test, lint, build, and typecheck commands
- CI and GitHub Actions
- generated folders and ignored paths
- secrets and environment boundaries

Do not overwrite existing project docs or app files. Instead, propose how existing facts should be reflected in Precode owner files.

Support can say:

```text
I found existing project material. I will not overwrite it automatically. I will name each conflict, propose where the fact belongs in Precode, and stop for your approval before changing anything.
```

If the project already has active work, make the first Precode bead setup or orientation. Do not turn setup into product implementation.

## First-Use Coaching

Teach the user this loop:

```text
orient -> decide -> plan -> build -> prove -> stop or approve the next transition
```

Key ideas to reinforce:

- active memory is only `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`
- one bead is active at a time
- generated reports are evidence only
- recorded checks are stronger than agent confidence
- the user approves risk and task transitions
- unclear state is a reason to stop, not push through

If the user feels lost, use `docs/PRECODE-TROUBLESHOOTING.md` before editing files.

## Bootcamp Role Boundaries

Use this section when PrecodeOS adoption is happening inside a guided bootcamp, workshop, or cohort.

Instructors own the learning and product-thinking layer:

- help students move from rough ideas to prototype progress
- ask clarifying and challenging questions
- help the student summarize evidence
- explain PrecodeOS concepts in plain language
- protect student ownership of product decisions, approvals, and acceptance
- preserve the distinction between "prototype works" and "idea is validated"

The Student owns the product direction, decisions, approvals, and acceptance for their prototype.

The Student should:

- explain the intended user, painful before moment, better after moment, and first useful slice in plain language
- make and approve product decisions, scope tradeoffs, non-goals, and acceptance calls
- use PrecodeOS prompts and evidence gates to stay oriented, bounded, and able to verify progress
- summarize what evidence supports continuing, narrowing, pausing, or changing direction
- ask instructors for product-thinking help when the idea, scope, or evidence is unclear
- ask support engineers for technical help when system setup, troubleshooting, or implementation blockers stop progress
- avoid treating "the prototype works" as proof that the idea is validated

Mentors are past bootcamp students who help first-time students navigate the cohort as guides, advisors, connectors, peers, and role models.

Mentors should:

- help students build confidence by sharing lived experience from the bootcamp
- provide light product idea support without owning product direction, scope, approval, acceptance, or evidence interpretation
- help students understand which role to ask for help: instructor for product thinking, support engineer for technical unblocking
- encourage students through uncertainty, stuck points, and normal first-time-builder discomfort
- model good PrecodeOS habits such as asking clarifying questions, keeping scope small, and separating working prototypes from validated ideas
- connect students to relevant cohort resources, examples, instructors, support engineers, or peers
- avoid replacing instructors, performing technical troubleshooting, or becoming the hidden product owner

Support engineers own technical support and unblocking when needed:

- help students with system requirements installation and maintenance
- perform technical troubleshooting and diagnosis
- implement narrow technical fixes when a student is blocked
- manage the escalation workflow, ensuring that issues are resolved promptly and efficiently
- explain the technical change plainly
- avoid owning product direction, scope, acceptance, or evidence interpretation

Mentor involvement may be lightly noted when it materially affects student confidence, navigation, or routing. Do not turn mentorship into heavy evidence overhead.

For cohort completion, do not count a working prototype as strong PrecodeOS evidence by itself. The Student should also be able to explain the problem, user, narrowed first useful slice, at least one non-goal, what was verified or demoed, and what evidence supports continuing, narrowing, pausing, or changing direction.

## Repair Path For Incorrect Setup

If files were copied incorrectly, overwritten, moved, renamed, or edited casually:

1. Stop implementation.
2. Identify the symptom in plain English.
3. Re-read active memory if it exists.
4. Compare expected files against `docs/PRECODE-FILE-INVENTORY.md`.
5. Use `docs/PRECODE-TROUBLESHOOTING.md` and `tasks/reference/RECOVERY-PROTOCOL.md`.
6. Explain the repair path before editing anything.
7. Validate before resuming.

Repair is not auto-repair. Do not delete evidence, reset the repo, or rewrite generated reports to make the state look clean.

## Close The Support Session

Do not create a separate support artifact by default. End by orienting the user to existing Precode surfaces:

- what was set up or adapted
- which checks passed or remain blocked
- the current bead
- the next safe prompt
- what not to approve yet
- where to go for troubleshooting

Support can say:

```text
Your durable project state is in the Precode files, not in my notes. Start next time with session-start, ask the agent to explain the active bead, and stop if generated reports or chat confidence start acting like authority.
```

## Related Guides

- `docs/PRECODE-GUIDED-SETUP.md` for the public setup path
- `docs/PRECODE-TROUBLESHOOTING.md` for symptom lookup
- `docs/PRECODE-USER-GUIDE.md` for day-to-day use
- `docs/PRECODE-FILE-INVENTORY.md` for the canonical file dictionary
- `tasks/reference/RECOVERY-PROTOCOL.md` for conservative repair
