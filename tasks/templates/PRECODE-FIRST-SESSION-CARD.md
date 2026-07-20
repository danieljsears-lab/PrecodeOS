# PrecodeOS First Session Card
<!-- ANCHOR: precode-first-session-card -->

> AUTHORITY: Copyable first-session checklist and prompt card for a nontechnical builder starting or resuming one safe PrecodeOS session.
> NOT_AUTHORITY: Active memory, setup approval, task selection, PRD approval, bead activation, implementation acceptance, generated evidence truth, protocol replacement, or permission to code.
> LOAD_WHEN: A new builder has finished setup or is about to start a first working session and needs a compact prompt/checklist without opening the full user guide.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-07-20

## Purpose

Use this card after PrecodeOS is installed or when a first working session feels too heavy.

This card gives a compact build-order path for students. It reinforces Guided Setup and the Daily Cockpit by pointing to them at the right moment. It is not a new start page, workflow, command wrapper, setup helper, generated report, skill catalog, registry, optional pack, installer, updater, release channel, or package manager.

## What To Open

Open only what matches your moment:

| Moment | Use |
|---|---|
| PrecodeOS is not installed | `docs/PRECODE-GUIDED-SETUP.md` |
| PrecodeOS is installed or work is resuming | `docs/PRECODE-DAILY-COCKPIT.md` |
| You only have a rough idea | `Ideation: use First PRD Walkthrough for my rough idea.` |
| Something feels broken or confusing | `docs/PRECODE-TROUBLESHOOTING.md` or `I am stuck, help me.` |

Do not browse every protocol first. The Daily Cockpit or troubleshooting route will name deeper files only when needed.

## Student Build Order

Use this order when you need one visible path:

`Setup -> Start -> Idea/Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close -> Next`

| Stage | What to do | Where it lives |
|---|---|---|
| Setup | Install or refresh PrecodeOS, validate, then stop. | `docs/PRECODE-GUIDED-SETUP.md` |
| Start | Begin the working session and make the agent explain the current state before editing. | `docs/PRECODE-DAILY-COCKPIT.md` |
| Idea/Packet | If the idea is rough, use First PRD Walkthrough; if a packet exists, keep it as evidence for intake. | Daily Cockpit `Ideation: use First PRD Walkthrough for my rough idea.` |
| Intake | Summarize reviewed source material before promoting anything into owner files or PRDs. | Daily Cockpit / Support Runbook route |
| PRD | Shape and review requirements before any build work starts. | Daily Cockpit / How-To route |
| Bead | Break approved work into one bounded active slice. | Daily Cockpit route |
| Proof | Record checks and manual evidence for the active bead. | Daily Cockpit `Prove` path |
| Review | Decide accept, revise, split, block, or stop from evidence. | Daily Cockpit `Review` path |
| Close | Record closeout and whether the session is safe to close. | Daily Cockpit `Close` path |
| Next | Start a fresh session or approve the next transition only through the normal gate. | Daily Cockpit / `next-step.py` route |

This table is an index in build order. Read the linked doc for the actual prompt or command. The table does not approve setup, PRDs, beads, review, transition, or coding.

## First Safe Prompt

Paste this before approving any coding:

```text
Start: run the Precode session start and explain the Context Pack before editing.

Name the active bead, primary authority file, files in play, checks, stop conditions, generated-report warning, and what still needs my approval. If the active bead is unclear, stop and tell me the safest next diagnostic step. Do not code yet.
```

If you only have an idea, paste this instead:

```text
Ideation: use First PRD Walkthrough for my rough idea.

Ask only the questions needed to understand the user, problem, evidence, weakest assumption, not-yet scope, and smallest useful first slice. Do not write a PRD, create beads, edit owner files, or code yet.
```

If you feel lost, paste this:

```text
I am stuck, help me.

Tell me the symptom in plain English, the first safe move, the owner surface to inspect, up to three read-only or advisory checks, the next safe action, and what you will not change without my approval.
```

## First Session Checklist

Before work starts:

- The agent named the active bead or said no active bead is clear.
- The agent named the primary authority file.
- The agent named files in play.
- The agent named checks or proof needed.
- The agent named stop conditions.
- You have not approved coding, setup mutation, repair, transition, release, overwrite, or external action by accident.

During work:

- Keep the work inside the active bead.
- Ask for evidence when the agent says something is done.
- Park future ideas instead of widening the current bead.
- Stop if the agent cannot explain scope, proof, or approval.

Before closing:

- Ask what changed.
- Ask what was proven.
- Ask what remains blocked, parked, or uncertain.
- Ask whether review, transition, or next-bead approval is still needed.

## Five Decision Words

Use these when the agent asks what to do next:

| Word | Meaning |
|---|---|
| `accept` | The current review or proposal is good enough to move forward through the normal gate. |
| `revise` | Keep the same direction, but change something before approval. |
| `split` | The work is too large or mixed; make a smaller unit. |
| `block` | Stop because proof, authority, state, or approval is missing. |
| `stop` | Pause before the next action because risk or confusion is too high. |

These words do not bypass normal approval gates. They help you tell the agent what kind of decision you are making.
