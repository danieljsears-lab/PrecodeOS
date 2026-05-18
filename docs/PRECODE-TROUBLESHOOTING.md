# PrecodeOS Troubleshooting
<!-- ANCHOR: precode-troubleshooting -->

> AUTHORITY: Public symptom-first troubleshooting reference for common first-time PrecodeOS setup, validation, and first-use confusion.
> NOT_AUTHORITY: Active memory, product decisions, task selection, PRD approval, implementation acceptance, destructive repair approval, generated evidence truth, private support operations, or automatic recovery policy.
> LOAD_WHEN: A user, support engineer, or agent is confused by setup state, active memory, current bead, generated reports, copied files, validation output, or first-session behavior.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-05-18

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
```

Safe path:

- name the package source and target project explicitly
- stop setup until both folders are clear
- use `docs/PRECODE-GUIDED-SETUP.md` for copy groups and exclusions

Do not copy files in either direction until source and target are unambiguous.

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

- compare against `docs/PRECODE-FILE-INVENTORY.md`
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
- update `docs/PRECODE-FILE-INVENTORY.md` when a new public file is intentional
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

## Process Phase Index

| Phase | Common failure | First guide |
|---|---|---|
| Intent capture | Support starts authoring product truth | `docs/PRECODE-SUPPORT-RUNBOOK.md` |
| Package source setup | Source and target folders are unclear | `docs/PRECODE-GUIDED-SETUP.md` |
| File copy | Excluded files copied or public files missed | `docs/PRECODE-FILE-INVENTORY.md` |
| Owner-file adaptation | Assumptions are written as settled facts | `docs/PRECODE-USER-GUIDE.md` |
| Validation | Active memory or inventory checks fail | this guide |
| First session | Current bead or next step is unclear | this guide |
| Repair | Files moved, renamed, overwritten, or generated reports edited | `tasks/reference/RECOVERY-PROTOCOL.md` |

## Script And Check Index

| Command | Use it when | Remember |
|---|---|---|
| `bash scripts/validate-memory.sh` | Active memory, bead pointer, or setup validity is uncertain. | A failure means source state needs attention before work continues. |
| `python3 scripts/file-inventory.py --check` | Public package files, new docs, copied files, or metadata are uncertain. | Inventory findings are advisory; they do not choose tasks. |
| `bash scripts/session-start.sh` | Beginning or resetting a session. | It prints context and generated router guidance. |
| `python3 scripts/next-step.py` | The user asks "what now?" | It is generated guidance, not approval. |
| `python3 scripts/state-check.py` | Active bead or task state looks broken. | Repair source files before generated reports. |
| `python3 scripts/files-in-play-check.py` | Scope may have widened or coding started too early. | It warns; it does not approve edits. |
| `python3 scripts/workflow-check.py` | The path from setup, idea, PRD, bead, or repair is unclear. | Workflow advice is not task activation. |
| `python3 scripts/completion-check.py` | Work sounds done but proof, review, or transition state is unclear. | Completion warnings do not accept work. |

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
