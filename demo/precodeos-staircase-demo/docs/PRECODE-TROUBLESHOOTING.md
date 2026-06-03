# PrecodeOS Troubleshooting
<!-- ANCHOR: precode-troubleshooting -->

> AUTHORITY: Public symptom-first troubleshooting reference for common first-time PrecodeOS setup, validation, and first-use confusion.
> NOT_AUTHORITY: Active memory, product decisions, task selection, PRD approval, implementation acceptance, destructive repair approval, generated evidence truth, private support operations, or automatic recovery policy.
> LOAD_WHEN: A user, support engineer, or agent is confused by setup state, active memory, current bead, generated reports, copied files, validation output, or first-session behavior.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.5
Last updated: 2026-05-31

## Purpose

Use this guide when PrecodeOS feels confusing or broken.

The safe troubleshooting posture is:

- stop before making the problem larger
- describe the symptom in plain English
- identify the owner file or generated report
- run read-only or advisory checks first
- repair source files, not generated reports
- validate before resuming

This guide helps route common first-time issues. It does not approve destructive commands, broad overwrites, task transitions, app-code changes, external mutations, or edits to secrets and private data.

## First Move

Ask the agent:

```text
Stop implementation. Tell me what symptom we are troubleshooting, which Precode files or generated reports are involved, what read-only checks you will use first, and what you will not change without approval.
```

If the agent cannot explain the current state, reload active memory if it exists:

```text
Load only AGENT.md, DECISIONS.md, and tasks/todo.md. Then explain the active bead, primary authority, files in play, checks, stop conditions, and blockers.
```

## Symptom Lookup

### "I Don't Know What Precode Wants Me To Do Next"

Likely causes:

- session has not been started from active memory
- generated next-step output is being treated as authority
- active bead is unclear or missing
- the user is jumping from setup into implementation too early

First checks:

```bash
bash scripts/session-start.sh
python3 scripts/next-step.py
```

Safe path:

- ask the agent to explain active memory, active bead, primary authority, checks, and stop conditions
- treat `next-step` as generated guidance only
- do not approve a transition or start coding until the active bead is clear

Stop if the agent cannot explain the current bead in plain English.

### Active Bead Or `tasks/todo.md` Is Confusing

Likely causes:

- `tasks/todo.md` does not match the in-progress bead
- more than one bead appears active
- a copied setup left stale task state from another repo
- a generated report is being used instead of active memory

First checks:

```bash
bash scripts/validate-memory.sh
python3 scripts/state-check.py
```

Safe path:

- compare `tasks/todo.md` with the bead it names
- confirm there is only one active bead
- repair source state before refreshing generated reports
- use `tasks/reference/RECOVERY-PROTOCOL.md` if state is broken

Do not continue implementation while the active bead is unclear.

### Generated Reports Are Being Treated As Authority

Likely reports:

- `OS-HEALTH.md`
- `PRECODE-HELP.md`
- `PROGRESS.md`
- `logs/*.md`
- `logs/*.json`
- `logs/*.jsonl`

First checks:

```bash
python3 scripts/state-check.py
python3 scripts/workflow-check.py
```

Safe path:

- identify which source files the report summarizes
- repair source files first if needed
- refresh generated reports only after source state is coherent
- return to active memory and the active bead for decisions

Do not hand-edit generated Markdown to make it look correct.

### Wrong Source Folder Or Target Folder

Likely causes:

- the PrecodeOS package checkout and target project folder were mixed up
- commands were run from the package source instead of the target project
- a user treated PrecodeOS itself as the app to execute

First checks:

```bash
pwd
git status
find . -maxdepth 2 -type f | sort
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>
```

Safe path:

- name the package source and target project explicitly
- stop setup until both folders are clear
- use Bootstrap Confidence output to identify target kind, conflicts, missing dependencies, and the first safe next action
- use `docs/PRECODE-GUIDED-SETUP.md` for copy groups and exclusions

Do not copy files in either direction until source and target are unambiguous.

### "Where Do My Notes, Docs, Or Screenshots Go?"

Likely causes:

- raw reference material is being mixed into active memory or owner files
- users are unsure whether evidence belongs inside the PrecodeOS package source
- screenshots, research, or documents may be private or too bulky to commit casually

Safe path:

- put project-owned raw material in root-level `project-evidence/`
- read `project-evidence/PROJECT-EVIDENCE-GUIDE.md`
- treat the folder as evidence only, not active memory, authority, task approval, or coding permission
- decide per project whether to track or ignore the folder in Git
- use Local Source Intake before promoting stable conclusions into owner files

Do not put raw evidence inside `tasks/todo.md`, PRDs, beads, active memory, or PrecodeOS package-source folders unless a reviewed conclusion belongs there.

### Copied Excluded Files Or Missed Public Files

Likely causes:

- copied `_maintainer/`, generated reports, generated logs, local editor state, caches, or secrets
- missed active memory, scripts, task structure, adapters, or owner files
- used a bulk copy without file-group review

First checks:

```bash
python3 scripts/file-inventory.py --check
bash scripts/validate-memory.sh
```

Safe path:

- compare against `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- remove or ignore excluded material only with user approval
- copy missing public package files by supervised group
- re-run validation before first use

Do not delete files, rewrite history, or overwrite conflicts just to make the inventory quiet.

### `validate-memory` Fails

Likely causes:

- missing active memory file
- broken bead pointer
- malformed bead or active work metadata
- copied stale state from another repo

First check:

```bash
bash scripts/validate-memory.sh
```

Safe path:

- read the failure message
- identify the owner file named by the failure
- repair the source file with the smallest safe edit
- re-run validation

Do not patch generated reports as a substitute for fixing active memory.

### `file-inventory --check` Fails Or Warns

Likely causes:

- new public docs are not listed in the inventory
- file metadata is missing or stale
- generated or private files are being considered public
- expected package files are missing

First check:

```bash
python3 scripts/file-inventory.py --check
```

Safe path:

- decide whether the warning is source truth, generated evidence, or a package-boundary issue
- update `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` when a new public file is intentional
- keep `_maintainer/` and generated reports out of public setup instructions

Do not treat an advisory inventory warning as task selection or transition approval.

### Existing Project Has Conflict Or Overwrite Risk

Likely conflicts:

- `README.md`
- product, architecture, API, security, or data-model docs
- CI files
- package manager files
- app source code
- environment files

First checks:

```bash
git status
find . -maxdepth 2 -type f | sort
```

Safe path:

- name each conflict before editing
- preserve existing project files
- propose how existing facts map into Precode owner files
- stop for approval before changing docs, CI, hooks, package files, or app code

Do not flatten an existing project into the Precode package shape.

### Agent Starts Coding Before Setup Or Orientation Is Complete

Likely causes:

- the user asked for implementation before setup validation
- the agent skipped active memory
- the active bead is setup, but the agent widened scope

First checks:

```bash
bash scripts/validate-memory.sh
python3 scripts/files-in-play-check.py
python3 scripts/workflow-check.py
```

Safe path:

- stop implementation
- ask the agent to restate the active bead and files in play
- finish setup or orientation first
- create or approve an implementation bead only through the normal Precode flow

Do not let early coding become implicit approval.

### Claude Checkpoint Claims The Bead Is Approved

Likely causes:

- Claude treated a checkpoint or completion summary as acceptance
- manual verification was claimed without a human or reproducible check actually verifying it
- the distinction between bead acceptance and next-bead transition was blurred
- chat confidence was treated as recorded evidence

First checks:

```bash
python3 scripts/bead-transition.py --json
python3 scripts/completion-check.py
git status --short
```

Safe path:

- ask for the exact transcript around the checkpoint and claimed approval
- compare the claim with Closeout Evidence and `logs/check-results.jsonl`
- treat invented or overstated manual verification as untrusted evidence
- repair Closeout Evidence with what was actually checked, who checked it, the environment, result, and remaining uncertainty
- use `revise`, `blocked`, or `manual_testing` when proof is missing

Do not activate a next bead, rewrite history, or accept the bead just because Claude says the checkpoint passed. `bash scripts/checkpoint.sh` reports state; only explicit approval of `python3 scripts/bead-transition.py --approve` may promote the next bead.

### Local App Will Not Start Or Loads Too Slowly

Likely causes:

- commands are being run from the wrong folder
- dependencies are missing or stale
- the dev server is already running, hung, or on a different port
- the project has not recorded its real app directory or checks
- support is treating PrecodeOS itself as the app runtime

First checks:

```bash
pwd
git status
ls
```

If the project has known package scripts, inspect them before running anything that installs or rewrites files.

Safe path:

- confirm whether this is the PrecodeOS package source or the student's target app
- identify the app directory and expected dev command from `PROJECT-CONTEXT.md`, package files, or existing docs
- restart or rerun only the narrow local command needed for the student's app
- record any missing setup fact in the proper owner file after user approval

Do not install dependencies, change package files, rewrite configuration, or edit app code unless the user approves a narrow technical fix.

### Auth, Login, Or Onboarding Blocks A Demo

Likely causes:

- test credentials or accounts were not prepared
- onboarding is being shown even though it is not the demo focus
- auth setup depends on secrets, dashboards, or external services
- support is trying to solve a product-flow decision as a technical bug

First checks:

```bash
git status
```

Safe path:

- ask whether auth or onboarding is core to the product being demonstrated
- if not core, help the student reach the value-bearing screen without changing product scope
- if credentials, dashboard setup, or secrets are involved, stop and ask for explicit user-controlled handling
- if the auth flow itself is the feature, route scope and acceptance questions back to the student or instructor

Do not paste secrets into prompts, commit credentials, bypass security casually, or decide that onboarding should be removed from the product.

### Support Is Unsure Who Owns The Blocker

Likely causes:

- the blocker mixes product uncertainty with technical setup
- the student is asking support to choose scope, evidence, or acceptance
- a mentor, instructor, and support engineer are each seeing a different part of the issue
- the agent is widening a support request into implementation

First checks:

```bash
bash scripts/session-start.sh
python3 scripts/next-step.py
```

Safe path:

- if the blocked decision is product direction, scope, user evidence, or acceptance, route back to student-owned product work with instructor support
- if the blocked issue is local setup, repo state, validation, runtime, auth, or a narrow implementation failure, keep it with support
- if the blocked issue is PrecodeOS package behavior or unclear official guidance, escalate rather than inventing policy
- name the route in the support closeout so the student knows where to go next

Do not let technical support become hidden product ownership.

## Process Phase Index

| Phase | Common failure | First guide |
|---|---|---|
| Intent capture | Support starts authoring product truth | `docs/PRECODE-SUPPORT-RUNBOOK.md` |
| Package source setup | Source and target folders are unclear | `docs/PRECODE-GUIDED-SETUP.md` |
| File copy | Excluded files copied or public files missed | `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` |
| Owner-file adaptation | Assumptions are written as settled facts | `docs/PRECODE-USER-GUIDE.md` |
| Validation | Active memory or inventory checks fail | this guide |
| First session | Current bead or next step is unclear | this guide |
| Local runtime | App will not start, reloads slowly, or auth blocks a demo | this guide |
| Repair | Files moved, renamed, overwritten, or generated reports edited | `tasks/reference/RECOVERY-PROTOCOL.md` |

## Script And Check Index

| Command | Use it when | Remember |
|---|---|---|
| `bash scripts/validate-memory.sh` | Active memory, bead pointer, or setup validity is uncertain. | A failure means source state needs attention before work continues. |
| `python3 scripts/file-inventory.py --check` | Public package files, new docs, copied files, or metadata are uncertain. | Inventory findings are advisory; they do not choose tasks. |
| `python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>` | First setup, source/target folder identity, copy groups, exclusions, conflicts, or first safe setup action are uncertain. | Read-only by default; output is evidence only and does not approve mutation. |
| `bash scripts/session-start.sh` | Beginning or resetting a session. | It prints context and generated router guidance. |
| `python3 scripts/next-step.py` | The user asks "what now?" | It is generated guidance, not approval. |
| `python3 scripts/state-check.py` | Active bead or task state looks broken. | Repair source files before generated reports. |
| `python3 scripts/files-in-play-check.py` | Scope may have widened or coding started too early. | It warns; it does not approve edits. |
| `python3 scripts/workflow-check.py` | The path from setup, idea, PRD, bead, or repair is unclear. | Workflow advice is not task activation. |
| `python3 scripts/completion-check.py` | Work sounds done but proof, review, or transition state is unclear. | Completion warnings do not accept work. |
| `python3 scripts/bead-transition.py --json` | A bead sounds accepted or ready to advance, but approval or next-bead state is unclear. | JSON readiness is diagnostic; only explicit `--approve` mutates state. |

## Escalate Or Stop

Stop and ask for explicit user approval before:

- overwriting existing project files
- editing app code during setup
- installing Git hooks
- adding or changing CI
- deleting copied files
- moving or renaming Precode files
- approving a bead transition
- touching secrets, credentials, billing, dashboard values, deployment settings, auth, payments, or private user data

If the next safe action is unclear, keep the state in troubleshooting or recovery. Do not continue from chat confidence alone.
