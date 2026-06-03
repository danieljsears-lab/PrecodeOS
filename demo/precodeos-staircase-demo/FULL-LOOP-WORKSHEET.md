# PrecodeOS Full Loop Worksheet

Use this as the student cheat sheet during the demo.

## The Full Loop

```text
1. Open project in VSCode
2. Open Claude Code
3. Reset to first bead
4. Start session
5. Confirm active bead
6. Check health
7. Work inside the bead
8. Capture future ideas without activating them
9. Recover if the agent drifts
10. Ask for evidence
11. Close session
12. Review bead
13. Approve next bead only when ready
```

## Start From The Desktop

Open the demo folder:

```bash
code /Users/danielsears/Projects/precode-os/demo/precodeos-staircase-demo
```

If `code` is unavailable, open VSCode and choose `File` -> `Open Folder...`.

## Reset To The First Bead

Say to Claude Code:

```text
Run bash scripts/reset-demo.sh.
```

Expected:

```text
Demo reset to first step: B001 readiness validation is active; B002 is proposed.
```

## Start Session

Say to Claude Code:

```text
Run bash scripts/session-start.sh and explain the result in plain English.
```

Look for:

- active bead
- done-when target
- files in play
- checks
- stop conditions
- proposed next bead

## Confirm The Active Bead

Say to Claude Code:

```text
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md, and tasks/todo.md. Then tell me the active bead, primary authority, files in play, checks, stop conditions, and anything blocked. Do not start coding yet.
```

Stop if Claude cannot name the active bead.

## Check Health

Say to Claude Code:

```text
Run python3 scripts/loop-health.py and explain the top risk in plain English.
```

Remember:

- `Clear` means continue inside the boundary.
- `Watch` means pay attention to one risk.
- `Drift Risk` or `Recenter` means slow down.
- `Stop and Review` means review evidence before adding work.

## Record Checks

Use `record-check.sh` for evidence:

```bash
bash scripts/record-check.sh -- bash scripts/validate-memory.sh
bash scripts/record-check.sh -- npm run check:docs
bash scripts/record-check.sh -- python3 scripts/next-step.py
bash scripts/record-check.sh -- python3 scripts/loop-health.py
```

For the app bead:

```bash
bash scripts/record-check.sh -- npm run check
bash scripts/record-check.sh -- npm run check:future
```

## Approve Transition

Ask first:

```text
Show me the proposed next bead, but do not start work until I explicitly approve the transition.
```

Then approve:

```text
Run python3 scripts/bead-transition.py --approve.
```

Do not approve transition until the current bead is reviewed.

## Work Inside B002

Say to Claude Code:

```text
Work only on the difficulty filter for the existing staircase cards. Before editing, tell me which files you expect to change and why. Do not add maps, geolocation, persistence, accounts, APIs, or unrelated design changes.
```

Expected files:

- `index.html`
- `src/**`
- `FEATURES.md` only for inactive future notes

## Capture A Future Idea

Say to Claude Code:

```text
I just thought of a future feature: let users save favorite staircases. Do not build it now. Check FEATURES.md. If it is already captured, confirm that it is future work only. If it is missing, add it as a future bead candidate in FEATURES.md for later work. Do not activate it.
```

Then confirm:

```text
Confirm the active bead is still B002 and that the new FEATURES.md item is not active work.
```

## Recovery: Scope Drift

Use this when Claude starts building the wrong thing:

```text
STOP. That is outside this bead. Run python3 scripts/files-in-play-check.py and explain any out-of-scope paths. Restate the active bead and continue only with the difficulty filter. Do not add map, location, API, persistence, account, redesign work, or future FEATURES.md items.
```

## Recovery: False Done

Use this when Claude says done without proof:

```text
You said this is done. I need evidence, not confidence. Show me the recorded check results and walk me through exactly how I can verify the difficulty filter myself.
```

## Manual Verification For B002

In the browser, verify:

- `All` shows all staircase cards.
- `Easy` shows only easy cards.
- `Moderate` shows only moderate cards.
- `Hard` shows only hard cards.
- Returning to `All` restores the full list.

## Close Session

Say to Claude Code:

```text
Run bash scripts/session-close.sh and summarize what changed, what evidence exists, what remains uncertain, and whether the bead should be accepted, revised, split, blocked, or stopped.
```

## Review Outcome Words

Use exactly one:

- `accepted`
- `revise`
- `split`
- `blocked`
- `stop`

## Show Future Work Without Activating It

Say to Claude Code:

```text
Show the next proposed bead, including any future candidate in FEATURES.md, but do not activate anything.
```

## Key Rule

```text
Start from repo truth. Confirm the bead. Keep Claude inside the boundary. Capture future ideas without activating them. Ask for evidence. Check health. Close the session. Review the bead. Then, and only then, approve the next bead.
```
