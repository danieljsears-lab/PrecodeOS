# PrecodeOS First Session Card
<!-- ANCHOR: precode-first-session-card -->

> AUTHORITY: Copyable first-session checklist and prompt card for a nontechnical builder starting or resuming one safe PrecodeOS session.
> NOT_AUTHORITY: Active memory, setup approval, task selection, PRD approval, bead activation, implementation acceptance, generated evidence truth, protocol replacement, or permission to code.
> LOAD_WHEN: A new builder has finished setup or is about to start a first working session and needs a compact prompt/checklist without opening the full user guide.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-08-02

## Purpose

Use this card after PrecodeOS is installed or when a first working session feels too heavy.

This card gives a compact build-order path for builders. It is shareable as the builder's official first-session flow when a live call or first solo session needs steps in one place. It reinforces Guided Setup and the Daily Cockpit by pointing to them at the right moment. It is not a new start page, workflow, command wrapper, setup helper, generated report, skill catalog, registry, optional pack, installer, updater, release channel, or package manager.

## What To Open

Open only what matches your moment:

| Moment | Use |
|---|---|
| PrecodeOS is not installed | `docs/PRECODE-GUIDED-SETUP.md` |
| PrecodeOS is installed or work is resuming | `docs/PRECODE-DAILY-COCKPIT.md` |
| You only have a rough idea | `Ideation: use First PRD Walkthrough for my rough idea.` |
| Something feels broken or confusing | `docs/PRECODE-TROUBLESHOOTING.md` or `I am stuck, help me.` |

Do not browse every protocol first. The Daily Cockpit or troubleshooting route will name deeper files only when needed.

## Builder Build Order

Use this order when you need one visible path:

`Setup -> Start -> Idea/Packet -> Intake -> Owner Files? -> PRD -> Architecture? -> Bead -> Proof -> Review -> Close -> Next`

| Stage | What to do | Where it lives |
|---|---|---|
| Setup | Install or refresh PrecodeOS, validate, then stop. | `docs/PRECODE-GUIDED-SETUP.md` |
| Start | Begin the working session and make the agent explain the current state before editing. | `docs/PRECODE-DAILY-COCKPIT.md` |
| Idea/Packet | If the idea is rough, use First PRD Walkthrough; if a packet exists, keep it as evidence for intake. | Daily Cockpit `Ideation: use First PRD Walkthrough for my rough idea.` |
| Intake | Summarize reviewed source material before promoting anything into owner files or PRDs. | Daily Cockpit / Support Runbook route |
| Owner Files? | If intake found stable facts for `PRODUCT.md`, `PROJECT-CONTEXT.md`, `DECISIONS.md`, `tasks/todo.md`, or another owner file, run Source-To-Promotion Hygiene Review, get user approval, apply only approved facts, then re-validate before PRD shaping. If no owner-file facts need promotion, say so and continue to PRD shaping. | Prompt Patterns / Support Runbook route |
| PRD | Shape and review requirements before any build work starts. | Daily Cockpit / How-To route |
| Architecture? | If the approved PRD touches auth, data, APIs, integrations, dependencies, migrations, external services, multi-step workflows, or multi-system behavior, run Architecture Shaping before bead decomposition. If the work is low-risk, proceed to bead decomposition and record the skip reason in the PRD architecture-impact section or bead notes. | Architecture Shaping Protocol / Workflow Selection route |
| Bead | Break approved work into one bounded active slice. | Daily Cockpit route |
| Proof | Record checks and manual evidence for the active bead. | Daily Cockpit `Prove` path |
| Review | Decide accept, revise, split, block, or stop from evidence. | Daily Cockpit `Review` path |
| Close | Record closeout and whether the session is safe to close. | Daily Cockpit `Close` path |
| Next | Start a fresh session or approve the next transition only through the normal gate. | Daily Cockpit / `next-step.py` route |

This table is an index in build order. Read the linked doc for the actual prompt or command. The table does not approve setup, PRDs, beads, review, transition, or coding.

## Linear Setup-To-First-Bead Prompt

Use this during a support call when the builder needs the whole flow stated linearly before opening deeper docs:

```text
Walk me through my first Precode session linearly.

Use the official build order: Setup -> Start -> Idea/Packet -> Intake -> Owner Files? -> PRD -> Architecture? -> Bead -> Proof -> Review -> Close -> Next.

First tell me which stage I am in, which owning doc or prompt to use, and the next one action I should take. Keep the answer short enough to follow on a live call.

If setup is not validated, route me to Guided Setup and stop before product work.
If setup is validated, route me to the Daily Cockpit or First Safe Prompt.
If my idea or source packet is not reviewed, route me to Ideation or Intake before PRD work.
If intake found stable facts that should live in owner files, run Source-To-Promotion Hygiene Review, ask for approval before edits, and re-validate before PRD shaping.
If there is no approved PRD or active bead, stop before coding and tell me what approval is missing.
If the approved PRD touches auth, data, APIs, integrations, dependencies, migrations, external services, multi-step workflows, or multi-system behavior, run Architecture Shaping before bead decomposition.
If the approved PRD is low-risk, continue to bead decomposition and record the Architecture Shaping skip reason in the PRD architecture-impact section or bead notes.

Do not approve setup, choose work, approve a PRD, create or activate beads, approve review or transition, write code, overwrite files, run app commands, or treat this card as a replacement for Guided Setup, Daily Cockpit, or the owning protocols.
```

## Owner-File Promotion Prompt

Use this after Local Source Intake and before PRD shaping when reviewed source facts may belong in owner files:

```text
Run the owner-file promotion check before PRD shaping.

Use only the reviewed Local Source Intake summary and current owner files. Name the exact candidate owner-file updates, source refs, evidence strength, open conflicts, proposed owner, promotion action, approval required, stop condition, and validation command.

If a fact is uncertain, label it as an assumption or open question. If no owner-file facts need promotion, say so and continue to PRD shaping only after I approve the next step.

Do not invent facts, overwrite files, edit owner files without my approval, approve a PRD, create or activate beads, update tasks/todo.md as task approval, write code, or treat this check as automatic owner-file adaptation.
```

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
