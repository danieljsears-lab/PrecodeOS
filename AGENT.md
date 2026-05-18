# PrecodeOS — AI Coding Agent Entry Point
<!-- ANCHOR: agent -->

> AUTHORITY: Shared AI coding agent operating model, active-memory contract, execution-layer entrypoints, shared commands, adapter handoff surface, and verification gate for a PrecodeOS repo.
> NOT_AUTHORITY: Product requirements, route structure, schema field definitions, business policy, or app-specific implementation status.
> LOAD_WHEN: Start of every coding session and before beginning any new logical unit.
> CLASS: active-memory

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears
Document version: v0.1.11
Last updated: 2026-05-17

## Project

This repository is PrecodeOS itself: a repo-native control layer for AI coding agents that is markdown-canonical, script-enforced, and built to prevent quiet drift.

For builders, Precode functions as a small operating system for AI coding work: it shows what matters, what is active, what is proven, and when to stop.

The project workspace is the repository root. PrecodeOS-owned work is primarily Markdown authority/reference docs, Python and Bash support scripts, generated evidence under `logs/`, GitHub Actions validation, adapters, shims, modes, memory-card templates, PRDs, and execution beads.

## Active Memory

Use only these files as active memory:

- `AGENT.md` — entrypoint, guardrails, and shared operating model
- `DECISIONS.md` — hard decisions in force now, unresolved open questions, and historical context
- `tasks/todo.md` — current-bead pointer for the active build

`PRECODE-HELP.md`, `PROGRESS.md`, `OS-HEALTH.md`, and files in `logs/` are generated output only. Do not use them as working memory. Reviewed memory in `memory/` is evidence for explicit consultation, not active memory.

## Always-Loaded Rules

- `OPERATING-CONSTRAINTS.md` — shared constraints for any AI coding agent
- Load deeper reference docs only when the current bead actually needs them

## Execution Layer

- `tasks/beads/` — one durable execution contract per logical unit
- `tasks/prds/` — product definition shards used before feature work becomes beads
- `modes/` — navigator, explorer, builder, and review role guidance
- `tasks/reference/` — durable specs and playbooks outside active memory
- `tasks/archive/` — historical task docs that do not drive active work

## Shared Commands

- `bash scripts/session-start.sh`
- `bash scripts/checkpoint.sh`
- `bash scripts/session-close.sh`
- `bash scripts/handoff.sh [next-agent]`
- `bash scripts/validate-memory.sh [--strict|--session-start|--json|changed-path]`
- `bash scripts/record-check.sh -- <command>`
- `bash scripts/log-tool-run.sh --tool <tool> --class <class> --status <pass|fail|blocked> --command "<summary>"`
- `python3 scripts/bead-transition.py [--approve]`
- `python3 scripts/next-step.py [--json]`
- `python3 scripts/os-health.py`
- `python3 scripts/import-agent-spend.py [--tool agent] [--source path] [--dry-run]`
- `python3 scripts/github-audit.py`
- `python3 scripts/import-github-sources.py [--issue n|--pr n|--source path] [--dry-run]`
- `python3 scripts/extension-check.py`
- `python3 scripts/verification-check.py`
- `python3 scripts/decomposition-check.py`
- `python3 scripts/state-check.py`
- `python3 scripts/context-check.py`
- `python3 scripts/orchestration-check.py`
- `python3 scripts/tool-execution-check.py`
- `python3 scripts/bead-depth-check.py`
- `python3 scripts/files-in-play-check.py [--command "<summary>"] [--edit-lock]`
- `python3 scripts/run-contract-check.py`
- `python3 scripts/clarity-scenario-check.py`
- `python3 scripts/workflow-check.py`
- `python3 scripts/goal-frame-check.py`
- `python3 scripts/long-horizon-check.py`
- `python3 scripts/completion-check.py`
- `python3 scripts/pattern-check.py`
- `python3 scripts/update-memory-index.py`
- `python3 scripts/memory-check.py`
- `python3 scripts/file-inventory.py`
- `python3 scripts/file-inventory.py --check`
- `python3 scripts/version-check.py`
- `bash scripts/scheduled-audit.sh`

Tool-specific notes live in `adapters/ADAPTER-INDEX.md`.

## Verification Gate

Before accepting a bead:

- run `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
- run the project-specific lint/test/build checks listed in the active bead
- update Closeout Evidence
- set review decision to `accepted`, `revise`, `split`, or `blocked`

When session close finds an accepted bead, it may propose the next bead. Do not initiate the next bead until the user approves `python3 scripts/bead-transition.py --approve`.
