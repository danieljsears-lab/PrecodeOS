# PrecodeOS Staircase Demo

Prepared VSCode + Claude Code demo package for teaching the PrecodeOS beginner workflow.

## Start Here

From the desktop, open this folder in VSCode:

```bash
code /Users/danielsears/Projects/precode-os/demo/precodeos-staircase-demo
```

If the `code` command is unavailable, open VSCode and choose `File` -> `Open Folder...`, then select:

```text
/Users/danielsears/Projects/precode-os/demo/precodeos-staircase-demo
```

Open Claude Code inside VSCode, then say:

```text
Run bash scripts/session-start.sh and explain the result in plain English.
```

The full recording script is in `DEMO-NARRATION.md`.

The student cheat sheet is:

- `FULL-LOOP-WORKSHEET.md`

## Reference Docs

This demo includes a local copy of the PrecodeOS reference docs in `docs/` so students can see where to look for help.

Good files to show in VSCode:

- `FULL-LOOP-WORKSHEET.md`
- `docs/PRECODE-USER-GUIDE.md`
- `docs/CLAUDE-CODE-FIELD-GUIDE.md`
- `docs/PRECODE-TROUBLESHOOTING.md`
- `docs/PRECODE-GUIDED-SETUP.md`
- `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`

## Backlog And Beads

Show these surfaces in VSCode:

- `tasks/todo.md` points to the active bead.
- `FEATURES.md` holds inactive future feature candidates.
- `tasks/beads/` holds proposed or active execution beads.

Only `tasks/todo.md` selects active work.

## App

This is intentionally the starting state: seeded staircase cards, no filter yet. The difficulty filter is added during Bead 2.

Run checks:

```bash
npm run check
npm run check:docs
npm run check:future
```

Run the static app:

```bash
npm run serve
```

Then open `http://localhost:4173`.
