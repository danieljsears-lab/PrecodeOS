# PrecodeOS Staircase Demo — Agent Entry Point

> AUTHORITY: Shared operating model, active-memory contract, demo commands, and verification gate for this PrecodeOS beginner demo repo.
> NOT_AUTHORITY: Production deployment, real user data, external services, or long-term product strategy.
> LOAD_WHEN: Start of every Claude Code session and before beginning any new logical unit.
> CLASS: active-memory

## Project

This is a prepared PrecodeOS demo repository for a beginner video recorded in VSCode with Claude Code.

The app helps users discover staircases to climb. It is intentionally small and static so the demo can focus on the Precode workflow rather than infrastructure.

## Active Memory

Use only these files as active memory:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Generated files under `logs/` are evidence only. Do not use them as active memory.

## Shared Commands

- `bash scripts/session-start.sh`
- `bash scripts/checkpoint.sh`
- `bash scripts/session-close.sh`
- `bash scripts/validate-memory.sh`
- `bash scripts/record-check.sh -- <command>`
- `python3 scripts/next-step.py`
- `python3 scripts/loop-health.py`
- `python3 scripts/files-in-play-check.py`
- `python3 scripts/bead-transition.py [--approve]`

## Verification Gate

Before accepting a bead:

- run the checks listed in the active bead
- verify user-visible behavior when applicable
- summarize closeout evidence
- recommend exactly one review outcome: `accepted`, `revise`, `split`, `blocked`, or `stop`

When a bead is accepted, `python3 scripts/bead-transition.py --approve` is still required before the next bead becomes active.
