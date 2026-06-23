# PrecodeOS -- Recovery Protocol
<!-- ANCHOR: recovery-protocol -->

> AUTHORITY: Beginner-safe recovery workflow for damaged Precode structure, stale or misused generated reports, broken active state, missing proof, confused sessions, accidental scope expansion, and approval confusion.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, destructive repair approval, generated progress state, or automatic rollback policy.
> LOAD_WHEN: A user thinks Precode is broken, state is confusing, files were moved or renamed, generated reports were edited or stale, checks are missing, scope widened, approval happened too quickly, or an agent lost context.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.10
Last updated: 2026-06-23

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

When already-implemented bead work later proves wrong, obsolete, harmful, or no longer wanted, use the Implemented Bead Reversal Workflow in `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md`. Diagnose first, preserve the original bead as `done` historical evidence, then create or propose a separate reversal bead. Do not reopen the old bead, delete evidence, rewrite transition logs, or treat Git revert alone as proof.

## Stuck Trigger Response

When the user says `I am stuck`, `I am stuck, help me`, or an equivalent stuck/confused/help-me phrase, the agent must stop implementation and return prescriptive recovery guidance before editing.

Required response:

1. Restate the symptom in plain English, or say the symptom is not yet known.
2. Say the first safe move: stop implementation and diagnose before repair.
3. Name the likely owner surface, or say the owner is unknown until active memory and checks are inspected.
4. Run or recommend no more than three read-only or advisory checks.
5. Give the next safe prompt or action.
6. State forbidden actions: no delete, overwrite, regenerate, transition approval, rollback, setup/update mutation, or destructive command without explicit approval.

Good first checks are usually one to three of:

- `bash scripts/session-start.sh`
- `python3 scripts/next-step.py`
- `python3 scripts/state-check.py`
- `python3 scripts/files-in-play-check.py`
- `python3 scripts/completion-check.py`
- `python3 scripts/os-health.py`

`OS-HEALTH.md`, Doctor Dashboard output, `PRECODE-HELP.md`, `next-step.py`, and stable-fix eligibility are diagnostic evidence only. They can help explain what is wrong, but they do not approve repair, transition, rollback, setup/update mutation, destructive commands, or generated-report regeneration.

The No-Engineer Fallback Prompt Pack in `tasks/reference/PROMPT-PATTERNS.md` is a symptom-specific front door into this protocol. Its prompts help a user name agent-lost, checks-failed, app-will-not-start, approved-too-much, copied-wrong-files, and stop-or-continue moments; they do not approve edits, deletion, overwrite, regeneration, rollback, setup/update mutation, transition approval, app-code changes, secrets handling, external mutation, or destructive commands.

`scripts/clarity-scenario-check.py` includes synthetic recovery scenario fixtures for wrong-folder or partial setup confusion, copied excluded/private/generated files, stale or edited generated reports, missing proof or failed checks, too-fast approval, app-will-not-start blockers, auth/demo/support ownership blockers, and stop-or-continue uncertainty. It also checks that the Bugfix Spec Lane contract stays present in recovery, prompt, verification, and user guidance surfaces. These fixtures are regression tests for this protocol's advisory boundaries. They are not real recovery evidence, repair approval, rollback approval, setup/update approval, transition approval, support-bot authority, or external-system permission.

## Stable-Fix Eligibility

A stable fix is a narrow, evidence-backed repair inside an already named owner file. It is eligible only when:

- the owner file or primary authority is clear
- the files in play are narrow, usually three files or fewer
- the change repairs existing intended behavior instead of creating new product, workflow, schema, authority, setup, release, or integration behavior
- the validation path is explicit and recorded
- the work avoids sensitive, external, destructive, deployment, rollback, secret, auth, billing, data, or migration surfaces

Before editing a repair that looks stable-fix eligible, use the Bugfix Spec Lane:

| Field | Purpose |
|---|---|
| Current behavior | Name the defect or broken behavior in plain English. |
| Expected behavior | Name the intended behavior after the fix. |
| Unchanged behavior | Name the behavior that must keep working and must not be refactored. |
| Owner file | Name the source file or primary authority that owns the repair. |
| Root cause if known | Say what appears to be causing the defect, or say it is not known yet. |
| Fix approach | Describe the smallest repair path without turning it into a new feature or refactor. |
| Regression proof | Name the check or manual verification that proves the defect is fixed and unchanged behavior still holds. |
| Route decision | Choose `current_bead`, `needs_evidence`, `recovery_repair`, `PRD/bead`, or `release_readiness`. |

Do not edit yet if the owner file, route decision, or regression proof is unclear. `eligible_stable_fix` may continue only inside the current active bead after the bugfix spec and recorded proof are clear. The bugfix spec is not repair approval, implementation acceptance, generated proof, release approval, rollback approval, setup/update permission, transition approval, or a substitute for Closeout Evidence.

`scripts/next-step.py --json` includes a `stable_fix_eligibility` advisory payload when a current bead exists. Its classification can help route the next conversation, but it does not approve edits, recovery, release, rollback, transition, setup mutation, package update behavior, or acceptance.

If the classifier says `recovery_repair`, stay in this protocol until the symptom, owner file, safe repair path, and validation are clear. If it says `needs_evidence`, use the Verification Guardrail Protocol. If it says `broader_change`, route to release readiness, PRD, or a normal bead instead of treating the work as a stable fix.

## First Move

When a user says "I think I broke something" or "I am stuck, help me," do this:

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
| File was moved or renamed | Compare the expected path with `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` and validation output. | Restore the expected path/name, then run `bash scripts/validate-memory.sh` and `python3 scripts/file-inventory.py --check`. | Do not invent a new path or update references just to match the mistake. |
| Generated report was edited | Identify the source script that owns the report. | Stop using the edited report, restore or regenerate it from source state, then return to owner files. | Do not treat the edited report as authority. |
| Generated report looks stale | Check whether source files, checks, closeout, or transitions changed after the report. | Refresh the report with the owning script after source state is coherent. | Do not hand-edit generated Markdown. |
| Active state is broken | Run `python3 scripts/state-check.py`. | Repair `tasks/todo.md` or the active bead so they agree, then validate memory. | Do not continue implementation while the active bead is unclear. |
| Checks or proof are missing | Run `python3 scripts/completion-check.py` and inspect bead checks. | Run stronger checks through `bash scripts/record-check.sh -- <command>` or record manual verification. | Do not accept work based on confidence. |
| Session or agent is confused | Re-read active memory, active bead, and primary authority. | Run `bash scripts/checkpoint.sh` or prepare a handoff, then continue only with a clear context pack. | Do not continue from chat memory alone. |
| Scope expanded accidentally | Run `python3 scripts/files-in-play-check.py`. | Explain each changed path as generated evidence, current-bead work, or separate follow-up; split or ask for approval when needed. | Do not silently widen the active task. |
| Approval happened too quickly | Review closeout evidence and transition state. | Ask for accepted, revise, split, blocked, or stop; require explicit transition approval before activating the next bead. | Do not let generated next-step help approve work. |
| Implemented bead needs reversal | Inspect the prior bead, Closeout Evidence, recorded checks, and current owner file. | Create or propose a separate reversal bead that names the superseded bead, reversal target, reversal reason, preserved behavior, checks, manual verification, and approvals still required. | Do not reopen a `done` bead, delete evidence, rewrite transition logs, or treat Git revert as complete proof. |

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
