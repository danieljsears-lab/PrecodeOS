# PrecodeOS VSCode + Claude Code Demo Narration

This demo starts at the first step of the PrecodeOS process:

- First active bead: `B001 — Validate Precode Readiness`
- Second bead after approval: `B002 — Add Difficulty Filter`
- Future capture surface: `FEATURES.md`
- Proposed next bead only: `B003 — Mark Staircase Cards As Visited`
- Additional proposed beads: `B004` through `B007`

If needed, reset the demo before recording:

```bash
bash scripts/reset-demo.sh
```

## 0. Start From The Desktop

**Action:**

Open VSCode from the command line:

```bash
code /Users/danielsears/Projects/precode-os/demo/precodeos-staircase-demo
```

If the `code` command is not available, open VSCode, choose `File` -> `Open Folder...`, and select:

```text
/Users/danielsears/Projects/precode-os/demo/precodeos-staircase-demo
```

**Narration:**

“I’m starting from the desktop by opening the demo project folder in VSCode.”

“This matters because Claude Code needs to operate inside the project folder where PrecodeOS is installed.”

## 1. Open Claude Code In VSCode

**Action:**

Open the Claude Code panel or Claude Code terminal integration in VSCode.

If you are unsure whether Claude is in the right folder, say:

```text
What folder are you currently working in? Do not edit anything.
```

**Expected result:**

Claude should name:

```text
precodeos-staircase-demo
```

**Narration:**

“Before I ask Claude to do anything, I make sure it is working in the demo folder.”

## 1a. Show The PrecodeOS Reference Docs

**Action:**

In the VSCode Explorer, open `FULL-LOOP-WORKSHEET.md`, then open the `docs/` folder.

Show these files briefly:

- `FULL-LOOP-WORKSHEET.md`
- `docs/PRECODE-USER-GUIDE.md`
- `docs/CLAUDE-CODE-FIELD-GUIDE.md`
- `docs/PRECODE-TROUBLESHOOTING.md`
- `docs/PRECODE-GUIDED-SETUP.md`
- `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`

Optionally say to Claude:

```text
Run npm run check:docs and confirm the PrecodeOS reference docs are available in this demo folder.
```

**Expected result:**

```text
Docs check passed: PrecodeOS reference docs and the full loop worksheet are available.
```

**Narration:**

“Before we start the bead loop, I want students to see where the reference material and cheat sheet live.”

“The `FULL-LOOP-WORKSHEET.md` file is the student cheat sheet. It has the full loop, commands, prompts, review words, and recovery prompts.”

“This demo also includes a local copy of the PrecodeOS `docs` folder. If you forget a command, need the Claude Code field guide, or hit a confusing state, this is where you look.”

“The docs are reference material. They help us understand the workflow, but they do not replace the active bead.”

## 1b. Show The Feature Backlog And Beads

**Action:**

In the VSCode Explorer, show these surfaces:

- `tasks/todo.md`
- `FEATURES.md`
- `tasks/beads/`

Open `FEATURES.md` and briefly point to the inactive future candidates:

- Save Favorite Staircases
- Sort Staircases By Climb Time
- Add Neighborhood Filter
- Add Staircase Detail View
- Share A Staircase Route
- Add Safety Notes

Then open `tasks/beads/` and show the proposed bead files:

- `B003-mark-staircase-visited.md`
- `B004-sort-by-climb-time.md`
- `B005-add-neighborhood-filter.md`
- `B006-add-staircase-detail-view.md`
- `B007-share-staircase-route.md`

Optionally say to Claude:

```text
Run npm run check:future and confirm FEATURES.md contains inactive future candidates without changing the active bead.
```

**Expected result:**

```text
Future work check passed
```

**Narration:**

“This is the backlog view.”

“The important distinction is that `tasks/todo.md` points to what is active now.”

“`FEATURES.md` is a parking lot for future candidates. These are useful ideas, but they are not active work.”

“`tasks/beads/` contains executable units of work, but proposed bead files are still inactive until the transition process approves one.”

“So the student mental model is: docs teach, `tasks/todo.md` selects the active bead, `FEATURES.md` parks future ideas, and `tasks/beads/` holds the work units.”

## 2. Reset To The First Bead

**Say to Claude:**

```text
Run bash scripts/reset-demo.sh.
```

**Expected result:**

```text
Demo reset to first step: B001 readiness validation is active; B002 is proposed.
```

**Narration:**

“Before recording, I reset the demo. This guarantees we start at the first Precode step: the first active bead.”

## 3. Start Bead 1

**Say to Claude:**

```text
Run bash scripts/session-start.sh and explain the result in plain English.
```

**Expected result:**

- Current bead: `tasks/beads/B001-validate-precode-readiness.md`
- State: `in_progress`
- Next bead: `tasks/beads/B002-add-difficulty-filter.md`
- B002 is not active yet

**Narration:**

“I start from repo truth. This should identify B001, the readiness bead.”

“I am checking the active bead, done-when target, files in play, checks, and stop conditions before Claude edits anything.”

## 4. Confirm The First Bead

**Say to Claude:**

```text
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md, and tasks/todo.md. Then tell me the active bead, primary authority, files in play, checks, stop conditions, and anything blocked. Do not start coding yet.
```

**Expected result:**

- Claude names `B001`
- Claude names `tasks/reference/DEMO-WORKFLOW.md`
- Claude confirms no product app files should be edited during B001

**Narration:**

“This prompt prevents the most common beginner mistake: letting the agent code before it can name the task.”

“B001 is not product work. It proves that the Precode loop is ready.”

## 5. Check Health For Bead 1

**Say to Claude:**

```text
Run python3 scripts/loop-health.py and explain the top risk in plain English.
```

**Expected result:**

- Health: `Clear`
- Top risk: jumping to B002 too early

**Narration:**

“Build Loop Health evaluates the loop, not me.”

“Here, the risk is moving to the second bead before the first bead has evidence and review.”

## 6. Prove Bead 1

**Say to Claude:**

```text
Run the checks required for this bead through record-check.sh. Then summarize what passed, what remains uncertain, and whether this bead is ready for review.
```

**Claude should run:**

```bash
bash scripts/record-check.sh -- bash scripts/validate-memory.sh
bash scripts/record-check.sh -- npm run check:docs
bash scripts/record-check.sh -- python3 scripts/next-step.py
bash scripts/record-check.sh -- python3 scripts/loop-health.py
```

**Narration:**

“Precode uses evidence, not confidence. A recorded check is stronger than Claude saying everything looks good.”

## 7. Review Bead 1

**Say to Claude:**

```text
Review this bead against its done-when target, checks, files in play, and closeout evidence. Recommend accepted, revise, split, blocked, or stop.
```

**Expected recommendation:**

```text
accepted
```

**Narration:**

“If the evidence supports the done-when target, I can accept the first bead.”

“If it did not, I would revise, split, block, or stop.”

## 8. Approve Transition To Bead 2

**Say to Claude:**

```text
Show me the proposed next bead, but do not start work until I explicitly approve the transition.
```

**Expected result:**

- Proposed next bead: `B002 — Add Difficulty Filter`
- Claude does not begin coding

**Then say:**

```text
Run python3 scripts/bead-transition.py --approve.
```

**Expected result:**

```text
Transition approved.
Active bead is now: tasks/beads/B002-add-difficulty-filter.md
```

**Narration:**

“This is the gate between the first bead and the second bead. Precode can suggest B002, but only I approve the transition.”

## 9. Confirm Bead 2

**Say to Claude:**

```text
Confirm the new active bead. Explain the done-when target, files in play, checks, stop conditions, and anything out of scope. Do not edit yet.
```

**Expected result:**

- Current bead: `B002 — Add Difficulty Filter`
- Files in play: `index.html`, `src/**`, and inactive future notes in `FEATURES.md`
- Out of scope: maps, geolocation, persistence, accounts, APIs, database, deployment, redesign, and implementation of future `FEATURES.md` items

**Narration:**

“Now we are in B002, the first visible product bead.”

“The task is only to add a difficulty filter to the seeded staircase cards.”

“There is one extra allowed surface: `FEATURES.md`, but only for capturing future ideas as inactive notes.”

## 10. Start The Static App

**Action:**

Open the VSCode terminal and run:

```bash
npm run serve
```

Open this URL in a browser:

```text
http://localhost:4173
```

**Expected result:**

- Staircase cards are visible
- There are no filter controls yet

**Narration:**

“This is the starting app state.”

“There are no onscreen controls yet because the difficulty filter is what Claude will add during B002.”

## 11. Ask Claude To Implement Only B002

**Say to Claude:**

```text
Work only on the difficulty filter for the existing staircase cards. Before editing, tell me which files you expect to change and why. Do not add maps, geolocation, persistence, accounts, APIs, or unrelated design changes.
```

**Expected result:**

- Claude names only `index.html` and/or `src/**`
- Claude does not touch Precode docs or unrelated files

**Narration:**

“A good bead has one visible change, one boundary, and one proof path.”

## 12. Capture Or Point To Future Work In FEATURES.md

**Say to Claude after B002 is underway or after the filter is working:**

```text
I just thought of a future feature: let users save favorite staircases. Do not build it now. Check FEATURES.md. If it is already captured, confirm that it is future work only. If it is missing, add it as a future bead candidate in FEATURES.md for later work. Do not activate it.
```

**Expected behavior:**

- Claude checks or updates `FEATURES.md`
- The future item is clearly marked as later, proposed, future, or not active
- Claude does not edit `tasks/todo.md` to activate it
- Claude does not start implementation

**Narration:**

“Sometimes a good idea appears while I am in the middle of a bead.”

“Precode gives me a safe way to capture it without derailing the current work.”

“If it is already in `FEATURES.md`, I confirm it is parked there. If it is missing, I add it there. Either way, I do not activate it.”

**Then say:**

```text
Confirm the active bead is still B002 and that the new FEATURES.md item is not active work.
```

**Expected result:**

```text
Active bead remains B002.
The FEATURES.md item is future work only.
```

## 13. Scope Drift Recovery

**Required demo moment: if Claude proposes building Save Favorite Staircases, maps, location, APIs, persistence, accounts, redesign, or any future `FEATURES.md` item, say:**

```text
STOP. That is outside this bead. Run python3 scripts/files-in-play-check.py and explain any out-of-scope paths. Restate the active bead and continue only with the difficulty filter. Do not add map, location, API, persistence, account, redesign work, or future FEATURES.md items.
```

**Narration:**

“This is the recovery step.”

“The idea is not bad. It is just not the active bead.”

“Precode lets me capture future work without letting it hijack the current task.”

“The correction is not never build that idea. The correction is not in this bead.”

## 14. False Done Recovery

**If Claude says it is done without proof, say:**

```text
You said this is done. I need evidence, not confidence. Show me the recorded check results and walk me through exactly how I can verify the difficulty filter myself.
```

**Narration:**

“Confidence is not evidence.”

“I need checks, a working app, or exact manual verification steps.”

## 15. Verify The Difficulty Filter

**Say to Claude:**

```text
Run the app checks for this project and then give me manual verification steps for the difficulty filter.
```

**Claude should run:**

```bash
bash scripts/record-check.sh -- npm run check
bash scripts/record-check.sh -- npm run check:future
```

**In the browser, manually verify:**

- `All` shows all staircase cards
- `Easy` shows only easy staircase cards
- `Moderate` shows only moderate staircase cards
- `Hard` shows only hard staircase cards
- Returning to `All` restores the full list

**Narration:**

“Now I verify the actual user behavior.”

“The feature is not accepted until the filter works, checks pass, and the future idea stayed inactive.”

## 16. Check Health Before Closing

**Say to Claude:**

```text
Run python3 scripts/loop-health.py and explain whether we should continue, review, or close.
```

**Expected result:**

- Claude recommends review or close
- Claude does not recommend adding extra features

**Narration:**

“This prevents the classic beginner mistake of adding one more thing after the bead is already ready for review.”

## 17. Close The Session

**Say to Claude:**

```text
Run bash scripts/session-close.sh and summarize what changed, what evidence exists, what remains uncertain, and whether the bead should be accepted, revised, split, blocked, or stopped.
```

**Narration:**

“Session close turns the work into a durable handoff.”

“The next session should not depend on memory or the chat transcript.”

## 18. Review Bead 2

**Say to Claude:**

```text
Review this bead against its done-when target, files in play, checks, manual verification, FEATURES.md future-work note, and closeout evidence. Recommend accepted, revise, split, blocked, or stop.
```

**Expected result if everything passed:**

```text
accepted
```

**Narration:**

“If the filter works, checks passed, files stayed in scope, and the future idea stayed inactive, B002 can be accepted.”

## 19. Show The Next Bead, But Stop

**Say to Claude:**

```text
Show the next proposed bead, including any future candidate in FEATURES.md, but do not activate anything.
```

**Expected result:**

- Claude shows existing proposed beads, such as `B003` through `B007`
- Claude mentions inactive `FEATURES.md` future candidates
- Claude does not activate any of them

**Narration:**

“Now Precode can show future work, but we stop here.”

“Future ideas are captured. They are not active until I approve a later bead.”

## Final Closing Line

**Say:**

```text
Start from repo truth. Confirm the bead. Keep Claude inside the boundary. Capture future ideas without activating them. Ask for evidence. Check health. Close the session. Review the bead. Then, and only then, approve the next bead.
```

## Reset After Practice

To return to the beginning:

```bash
bash scripts/reset-demo.sh
```

Then confirm:

```bash
bash scripts/validate-memory.sh
```

Expected current bead:

```text
tasks/beads/B001-validate-precode-readiness.md
```
