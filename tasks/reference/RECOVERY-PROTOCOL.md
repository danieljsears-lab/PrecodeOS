# PrecodeOS -- Recovery Protocol
<!-- ANCHOR: recovery-protocol -->

> AUTHORITY: Beginner-safe recovery workflow for damaged Precode structure, stale or misused generated reports, broken active state, missing proof, confused sessions, accidental scope expansion, and approval confusion.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, destructive repair approval, generated progress state, or automatic rollback policy.
> LOAD_WHEN: A user thinks Precode is broken, state is confusing, files were moved or renamed, generated reports were edited or stale, checks are missing, scope widened, approval happened too quickly, or an agent lost context.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-13

## Purpose

This protocol gives beginners a safe first move when something feels broken.

The recovery posture is conservative:

- stop before making the damage larger
- identify the symptom in plain English
- find the owner file
- repair source files, not generated reports
- run validation
- resume only when the next safe action is clear

Recovery is not auto-repair. Do not run destructive commands, overwrite user edits, delete evidence, rewrite logs, or guess from generated reports.

## First Move

When a user says "I think I broke something," do this:

1. Stop implementation.
2. Ask what changed, if the user knows.
3. Re-read active memory: `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
4. Identify the active bead, primary authority, files in play, checks, and stop conditions.
5. Classify the symptom using the recovery table below.
6. Run read-only or advisory checks first.
7. Explain the repair path before editing anything.

Copyable user prompt:

```text
I think I broke something in Precode. Stop work, identify the symptom, name the owner file, explain the safest recovery path, and do not edit, delete, move, overwrite, or regenerate anything until I approve the next step.
```

## Recovery Flows

| Symptom | First check | Safe recovery path | Do not do |
|---|---|---|---|
| File was moved or renamed | Compare the expected path with `PRECODE-FILE-INVENTORY.md` and validation output. | Restore the expected path/name, then run `bash scripts/validate-memory.sh` and `python3 scripts/file-inventory.py --check`. | Do not invent a new path or update references just to match the mistake. |
| Generated report was edited | Identify the source script that owns the report. | Stop using the edited report, restore or regenerate it from source state, then return to owner files. | Do not treat the edited report as authority. |
| Generated report looks stale | Check whether source files, checks, closeout, or transitions changed after the report. | Refresh the report with the owning script after source state is coherent. | Do not hand-edit generated Markdown. |
| Active state is broken | Run `python3 scripts/state-check.py`. | Repair `tasks/todo.md` or the active bead so they agree, then validate memory. | Do not continue implementation while the active bead is unclear. |
| Checks or proof are missing | Run `python3 scripts/completion-check.py` and inspect bead checks. | Run stronger checks through `bash scripts/record-check.sh -- <command>` or record manual verification. | Do not accept work based on confidence. |
| Session or agent is confused | Re-read active memory, active bead, and primary authority. | Run `bash scripts/checkpoint.sh` or prepare a handoff, then continue only with a clear context pack. | Do not continue from chat memory alone. |
| Scope expanded accidentally | Run `python3 scripts/files-in-play-check.py`. | Explain each changed path as generated evidence, current-bead work, or separate follow-up; split or ask for approval when needed. | Do not silently widen the active task. |
| Approval happened too quickly | Review closeout evidence and transition state. | Ask for accepted, revise, split, blocked, or stop; require explicit transition approval before activating the next bead. | Do not let generated next-step help approve work. |

## Generated Reports

Generated reports are evidence only.

Examples include:

- `OS-HEALTH.md`
- `PROGRESS.md`
- `PRECODE-HELP.md`
- `logs/*.md`
- `logs/*.json`
- `logs/*.jsonl`

If generated output is wrong, stale, missing, or confusing, repair the source state first. Regenerate the report after the source files are coherent.

Copyable prompt:

```text
This generated report looks wrong. Tell me which source files and scripts own it, what evidence it summarizes, and how to refresh it without treating the report as authority.
```

## Validation After Recovery

Choose checks that match the symptom:

| Situation | Checks |
|---|---|
| Active memory, bead pointer, or state repair | `bash scripts/validate-memory.sh`; `python3 scripts/state-check.py` |
| File move, rename, missing doc, or inventory confusion | `python3 scripts/file-inventory.py --check`; `python3 scripts/version-check.py` |
| Generated-report confusion | owning refresh script; `python3 scripts/state-check.py`; `python3 scripts/workflow-check.py` |
| Scope expansion | `python3 scripts/files-in-play-check.py` |
| Weak evidence or closeout confusion | `python3 scripts/completion-check.py`; declared bead checks through `record-check.sh` |
| Context loss or handoff risk | `python3 scripts/context-check.py`; `bash scripts/handoff.sh [next-agent]` |

When recovery changes source files, record validation with:

```text
bash scripts/record-check.sh -- <check command>
```

## Resume Rules

Resume only when the agent can say:

- what broke
- which file owns the repair
- what changed
- which checks passed or remain blocked
- whether any user approval is still needed
- why generated reports are evidence, not authority
- the next bounded action

If that explanation is not possible, stop and keep recovery in progress.

Maintainer-local document history for this recovery protocol lives in `_maintainer/CHANGELOG.md`; it is not public package authority.
