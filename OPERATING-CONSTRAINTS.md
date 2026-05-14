# PrecodeOS — Operating Constraints
<!-- ANCHOR: operating-constraints -->

> AUTHORITY: Shared edit discipline, scope control, generated-output demotion, and reference-loading rules for PrecodeOS.
> NOT_AUTHORITY: Feature requirements, route structure, schema definitions, product decisions, or active task selection.
> LOAD_WHEN: Starting work, editing OS files, validating scope, or recovering from drift.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Constraints

- Active memory is exactly `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
- Load reference files only when the active bead needs them.
- Read a file before editing it.
- Keep one bead `in_progress`.
- Use one primary authority file per bead.
- Use `bash scripts/record-check.sh -- <command>` for validation evidence.
- Treat generated files as reports, not instructions.
- Stop before crossing sensitive surfaces or manual approval gates.

## Generated Output

Generated files may inform humans, but they must not select the next task or override active memory.

Generated outputs include:

- `PROGRESS.md`
- `OS-HEALTH.md`
- files in `logs/`

## Drift Recovery

If the agent widens scope, loses the authority file, or cannot prove completion:

1. Stop.
2. Re-read active memory.
3. Re-read the active bead and primary authority.
4. Run `bash scripts/checkpoint.sh`.
5. Split, revise, block, or ask for approval.
