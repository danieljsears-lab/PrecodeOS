# PrecodeOS Daily Cockpit
<!-- ANCHOR: precode-daily-cockpit -->

> AUTHORITY: Builder-first daily loop, next-step, health, diary, recovery, and reference routing for normal PrecodeOS work.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, PRD approval, bead activation, implementation acceptance, generated evidence truth, destructive repair approval, or protocol authority replacement.
> LOAD_WHEN: A builder is starting or resuming work, choosing the next safe move, checking health, capturing learning, recovering, or finding the smallest relevant reference.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.2.0
Last updated: 2026-09-06

Use this cockpit after setup validates. Stop here for normal work unless it routes you to one specific setup, troubleshooting, prompt, or protocol surface.

The first-class sections are deliberately short: **Daily Loop**, **Next**, **Health**, and **Diary**. The complete prompt and protocol catalogs live in their owner files, not on this daily surface. This reduces what a builder must scan without removing capability.

Use the cockpit as the human control surface for Codex, Claude Code, Cursor, Gemini, or another host agent. The agent performs scoped mechanics; the builder approves direction, risky actions, acceptance, and transitions. Generated reports, HTML, logs, sidecars, and catalog rows are evidence or navigation only. Active memory and owner files stay authoritative.

First-reader route:

| Situation | Go here |
|---|---|
| PrecodeOS is not installed | `PRECODE-GUIDED-SETUP.md` |
| Setup has validated | Stay in this cockpit |
| You only have a rough idea | `Ideation: use First PRD Walkthrough for my rough idea.` |
| State or setup feels broken | `PRECODE-TROUBLESHOOTING.md` or `I am stuck, help me.` |
| You want the complete prompt catalog | `../tasks/reference/PROMPT-PATTERNS.md` |
| You need a protocol | Let `Next` name one protocol, then open that owner file |

## Daily Loop

Daily Loop is the build-loop surface. Repeated bead work uses this rhythm:

```text
Active -> Changed -> Proven -> Parked -> Approval -> Next
```

| Stage | Inspect | Stop when |
|---|---|---|
| Active | Current bead, primary authority, files in play, done-when target, stop conditions | Any item is unclear |
| Changed | Files, behavior, decisions, scope, assumptions | Work exceeded the bead |
| Proven | Recorded checks, manual verification, evidence gaps | The claim exceeds the evidence |
| Parked | Candidate Queue, deferred follow-ups, memory candidates | Parked intent starts driving current work |
| Approval | PRD, activation, review, transition, release, or risky action still requiring a human | Approval is missing or ambiguous |
| Next | One safe move and its stop condition | The agent starts a second move |

Start or resume:

```text
Start: run the Precode session start and explain the Context Pack before editing.
```

```bash
bash scripts/session-start.sh
```

The result should name the active bead, authority, files in play, checks, stop conditions, and approval still required. If it cannot, stop before editing.

For returned agent work, use:

```text
Review returned agent work before I accept it. Show changed files, checks and results, manual verification, missing proof, unresolved risks, approval still required, parked follow-ups, forbidden actions not taken, and the next safe prompt.
```

## Next

Next identifies one safe move. It does not choose tasks, rank parked ideas as implementation priority, approve a PRD, activate a bead, accept review, approve transition, or authorize code.

| Moment | Use | Expected result |
|---|---|---|
| Rough idea | `Ideation: use First PRD Walkthrough for my rough idea.` | Idea -> Brief -> Packet -> Intake -> PRD, without approval or coding |
| Workflow unclear | `Use the Workflow Selection Protocol.` | One route, owner, approval, and stop condition |
| Future idea | `Queue: review Candidate Queue as parked intent.` | Parked evidence, not active work |
| Work may be complete | `Close: run session close and show Close State.` | Digest, proof, gaps, approvals, and next-safe-action evidence |
| Something is wrong | `I am stuck, help me.` | Symptom, owner surface, up to three safe checks, recovery route, forbidden actions |
| Returning after handoff | `Re-enter after AFK or handoff.` | Reloaded state and one continue, review, split, block, or handoff recommendation |

Use this before continuing:

```text
Next: name the safest next Precode move, the owner source, the approval still required, the stop condition, and what generated evidence does not decide.
```

The first-product spine is:

```text
Idea -> Brief -> Packet -> Intake -> Owner Files? -> PRD -> Architecture? -> Bead -> Proof -> Review -> Close
```

`Owner Files?` is an explicit source-promotion check. `Architecture?` is conditional for work touching auth, data, APIs, integrations, dependencies, migrations, external services, or multi-system behavior. Neither gate can be skipped because an agent is confident.

## Health

Health asks whether state and evidence are coherent enough to continue. It does not decide what to build or accept work.

| Need | Command | Boundary |
|---|---|---|
| Start or reset context | `bash scripts/session-start.sh` | Orientation only |
| Choose the next route | `python3 scripts/next-step.py` | Advisory; not task authority |
| Check loop health | `python3 scripts/loop-health.py` | Generated evidence only |
| Refresh OS health | `python3 scripts/os-health.py` | Inspect source when warnings appear |
| Record a check | `bash scripts/record-check.sh -- <command>` | Evidence, not acceptance |
| Check completion | `python3 scripts/completion-check.py` | Not release or transition approval |

Prompt:

```text
Health: show active state, current bead, primary authority, files in play, latest checks, generated-report warnings, and what must be inspected before editing.
```

## Diary

Diary records what transpired. It does not replace active memory, owner files, PRDs, beads, closeout evidence, or current code.

| Surface | Use | Boundary |
|---|---|---|
| `logs/learning-diary.md/jsonl` | Session lessons and durable observations | Generated learning evidence |
| `logs/bead-build-journal.md/jsonl` | Bead-level path, changes, and provenance | Not task or transition authority |
| `logs/build-attribution-ledger.md/json` | Who-built-what evidence and uncertainty | Not scoring, blame, merge, or release approval |
| `memory/cards/*.md` | Reviewed memory | Requires explicit promotion before changing owner truth |

Prompt:

```text
Diary: read the learning diary, bead build journal, attribution evidence, closeout digest, and reviewed memory relevant to this bead. Tell me what changed, what was proven, what was parked, what is uncertain, and what needs explicit promotion approval.
```

## Reference And Support

Everything below supports the four first-class cockpit sections. Do not browse it all before working.

| Need | Open | Boundary |
|---|---|---|
| Install, refresh, or recover setup | `PRECODE-GUIDED-SETUP.md` | Setup only; approval IDs do not authorize owner-file changes |
| One-page first session | `../tasks/templates/PRECODE-FIRST-SESSION-CARD.md` | Post-setup aid, not a task selector |
| Deeper manual | `PRECODE-USER-GUIDE.md` | Annex, not a second start page |
| Symptom lookup | `PRECODE-TROUBLESHOOTING.md` | Diagnose before repair |
| Copyable prompts | `../tasks/reference/PROMPT-PATTERNS.md` | Complete catalog; prompts do not approve work |
| Protocol selection | `../tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` | Select one owner protocol when needed |
| Package ownership | `PRECODE-PACKAGE-FILE-INVENTORY.md` | Technical dictionary, not active memory |
| Generated reading aid | `../docs-html/index.html` | Markdown remains authoritative |
| Adapter contract | `../adapters/ADAPTER-INDEX.md` | Compatibility and conformance, not alternate authority |

### Prompt And Protocol Reference

Expanded prompt bodies remain authoritative in Prompt Patterns. Protocol details remain authoritative in their named `tasks/reference/*PROTOCOL.md` files. The generated Daily Cockpit HTML provides copyable cards sourced from those owner files. Catalog rows do not approve work, choose tasks, activate beads, accept review, approve transition, approve release, mutate files, or make generated evidence authoritative.

Use `Workflow Selection` when you do not know which surface applies. It should name one next protocol instead of loading every protocol.

Beginner daily commands are limited to:

```bash
bash scripts/session-start.sh
python3 scripts/next-step.py
python3 scripts/loop-health.py
python3 scripts/os-health.py
bash scripts/record-check.sh -- <command>
```

Setup, recovery, advanced evidence, review, and maintainer validation commands remain conditional references.

## Stop Signals

Stop the agent when:

- it cannot name the active bead, authority, files in play, checks, or stop conditions
- it starts coding from a generated report, source note, catalog row, or old chat
- it touches files outside the active bead without explaining why
- it claims completion without recorded evidence and manual verification
- it starts another bead without explicit approval
- it proposes overwrite, delete, reset, migration, deployment, secret exposure, or external mutation without exact approval
- the product problem, user, scope, or authority file is still unclear

```text
STOP. Do not make any more changes. Tell me exactly where we are: active bead, primary authority, files changed, evidence recorded, blockers, and the safest next action.
```

## Approval Gates

Explicit human approval is required for:

- PRD approval, bead activation, review acceptance, transition approval, release approval, merge approval, and manual-verification claims
- setup or package-refresh apply actions
- owner-file adaptation and source promotion
- destructive commands, broad overwrites, deletes, moves, force resets, migrations, deploys, secrets, billing, auth, payments, or private-data actions
- external mutation, GitHub mutation, staging, committing, pushing, rollback, or publishing

```text
Before continuing, show the allowed actions, proof needed, approval required before risky actions, stop conditions, and blocked escape path. Then run python3 scripts/run-contract-check.py.
```
