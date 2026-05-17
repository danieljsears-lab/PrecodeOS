# Claude Code Field Guide For Students
<!-- ANCHOR: claude-code-field-guide -->

## A Bootcamp Companion For Claude Code + PrecodeOS

> AUTHORITY: Beginner-facing public field guide for using Claude Code with PrecodeOS safely and confidently.
> NOT_AUTHORITY: Active memory, product decisions, task selection, PRD approval, bead activation, generated evidence truth, or maintainer-only roadmap planning.
> LOAD_WHEN: A beginner wants a readable companion for Claude Code sessions, prompts, review habits, and PrecodeOS operating confidence.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.5
Last updated: 2026-05-17
Companion to: `docs/PRECODE-USER-GUIDE.md`

---

## How to use this guide

This guide is for first-time students and non-technical builders using Claude Code inside a project that already has PrecodeOS installed. You do not need to understand the codebase before you begin. You do need to know how to slow the agent down, confirm the task, and ask for proof.

Read it once, front to back, before your first session. After that, keep it open alongside your laptop and jump to whatever section you need. The **Prompt Cookbook** and **Quick Reference Card** are the sections you'll reach for most.

This guide assumes your project and Claude Code are already installed. Claude Code may appear as a VS Code panel, a terminal-style chat, or another school-provided surface. If you cannot find Claude Code or open your project folder, ask your instructor or engineer before starting.

---

## The Mental Model

### You are the boss. Precode is your project manager. Claude Code is your contractor.

That's the whole model. Hold onto that.

**Claude Code** is an AI coding agent. It may run inside VS Code or in a terminal-style Claude Code surface, depending on your setup. You talk to it in plain English. It reads your project, writes code, runs checks, and explains what it did. It's very good at doing what you ask — which means you need to be precise about what you ask.

**PrecodeOS** is a set of files that live inside your project folder. Think of it as a job board and rulebook for Claude Code. It tells the agent what the current task is, what files it's allowed to touch, what "done" looks like, and when to stop. Without Precode, Claude Code is a very capable contractor with no job description — it will fill in the blanks itself, and you might not like what it builds.

**You** approve everything. You decide what gets built, when work is done, and when to stop. Claude Code proposes. You approve. That's the deal.

---

### What is "vibe coding"?

Vibe coding means describing what you want to build in plain English and letting an AI agent write the code. You don't need to know how to code. You need to know what you want.

The power is real. The risk is real too. The risk is **drift**: Claude Code moves fast, generates a lot, and sounds confident even when it's going in the wrong direction. PrecodeOS exists to give that momentum a steering wheel.

> **The one rule you must never break:**
> Never let Claude Code start working without a confirmed task card (called a **bead**). A bead is a single, specific job with a clear definition of done. No bead = no work. Full stop.

---

### Key vocabulary (all you need for now)

| Word | Plain English |
|------|--------------|
| **Bead** | One task card. One job at a time. Never two. |
| **Active memory** | The 3 files Precode expects Claude to start from every session. Always the same 3. |
| **Evidence** | Proof that something works — not Claude saying it works. |
| **Checkpoint** | A mid-session check: are we still on track? |
| **Authority file** | The one file that owns a particular fact. If two files disagree, the authority file wins. |

---

### Checkpoint before the chat gets crowded

Long AI coding sessions can get crowded with file reads, command output, screenshots, and decisions. Do not wait until the agent is obviously confused.

When the session feels long or busy, ask for a checkpoint:

```text
Checkpoint before this context gets crowded. Tell me the active bead, primary authority, files in play, what changed, what evidence exists, what is still uncertain, and the next exact check.
```

If Claude needs to compact, restart, or hand off, ask for a Context Pack first. After that, make it reload active memory, the active bead, and the primary authority before continuing.

---

## Before You Open Claude Code

Do this every single session, before you type anything to Claude.

### The Pre-Session Checklist

- [ ] I know which bead (task card) we're working on today
- [ ] I can say in one sentence what "done" looks like for this bead
- [ ] I am not expecting Claude to figure out what to build — I have a specific task
- [ ] I have not asked Claude to work on two things at once

**Fill in before every session:**

> Today's bead (task card name): `_________________________________`
>
> Done looks like: `_________________________________`
>
> What is NOT in scope today: `_________________________________`

---

### The 3 files every session starts from

At the start of every session, Precode expects Claude to orient from exactly these 3 files:

1. **`AGENT.md`** — the shared rulebook for how Claude works in this project
2. **`DECISIONS.md`** — hard decisions that have already been made (Claude respects these)
3. **`tasks/todo.md`** — the pointer to which bead (task card) is currently active

Claude should not treat your whole project as active memory. It should start with these 3 files, then load only the additional files the active bead or authority docs require. This keeps the session focused.

> **Why this matters:** If you skip loading active memory and jump straight to "build X," Claude will try to help but without its bearings. It may code something adjacent to what you want, touch files it shouldn't, or build something that conflicts with decisions already made.

---

## Starting Your Session

### Finding Claude Code

Your course may use Claude Code in VS Code, in a terminal-style surface, or through another approved setup. You do not need to understand every button. You only need to find the project folder and the place where you can type to Claude.

If you are using VS Code:

1. Look for the **Claude icon** in the left sidebar (it looks like a small diamond shape)
2. Click it. A chat panel opens on the left side of your screen.
3. This is where you talk to Claude Code.

> **VS Code feels overwhelming at first.** That's normal. You only need the file explorer (left panel) and the Claude chat (left sidebar). Ignore everything else until your engineer points you to it.

---

### First session script

Use this exact sequence the first time you work with a bead:

1. Run `bash scripts/session-start.sh`.
2. Paste the bead-confirmation prompt below.
3. Read Claude's summary before approving work.
4. If the bead, files, checks, or stop conditions sound wrong, correct them before Claude edits.
5. If they sound right, say `Confirmed. Go ahead.`

### Step 1 — Start the session

Type this command in the Claude Code chat and press Enter:

```
bash scripts/session-start.sh
```

Claude will run the session start script. It prepares the session and helps orient Claude to the Precode files for your project.

---

### Step 2 — Confirm the bead before anything else

Paste this prompt and press Enter:

```
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md,
and tasks/todo.md. Then tell me the active bead, primary authority,
files in play, checks, stop conditions, and anything blocked.
Do not start coding yet.
```

**What a good response looks like:**
- Claude names the active bead
- Claude lists the files it's allowed to touch
- Claude says what "done" means for this bead
- Claude tells you what it will check
- Claude tells you what would make it stop or ask you first

**What a warning sign looks like:**
- Claude can't name the active bead
- Claude starts writing code immediately
- Claude asks a vague question like "what should I build today?"
- Claude lists files you didn't expect

> **If Claude starts coding before you confirmed the bead — type `STOP` and start Step 2 again.** Do not let work proceed without a confirmed bead. This is the most common beginner mistake.

---

### Step 3 — Approve (or adjust) before work begins

After Claude confirms the bead, read its summary. Ask yourself:
- Is this the right task?
- Do the files in play match what I expected?
- Is the definition of done what I had in mind?

If yes: say `Confirmed. Go ahead.`
If no: correct Claude before it writes a single line of code.

---

### When Claude Over-Challenges A 4-Week MVP

Claude is useful when it catches real risks. It becomes unhelpful when it treats a bootcamp MVP like a company-scale product, keeps adding future features, or keeps asking questions after the first version is clear enough.

For a 4-week MVP, your job is not to remove every uncertainty. Your job is to choose a small, safe first version, defer the rest, and keep Precode authority boundaries intact.

Paste this at the start of an ideation, planning, or PRD-shaping session:

```text
Context for this session:
I am a beginner building a 4-week MVP, not a polished company-scale product.

Help me make the idea concrete, small, and safe enough to move forward. Challenge only the issues that would change what I should build or validate in the next 4 weeks. Do not expand the scope, add enterprise features, invent future platform requirements, or keep poking holes after the first version is good enough to define.

Sort concerns into:
- Must decide now:
- Good enough for MVP:
- Defer / Not yet:

Treat workbook notes, chat notes, and generated summaries as evidence, not authority. Do not edit PRODUCT.md, create a PRD, create beads, or write code unless the active Precode workflow explicitly allows it and I approve.
```

Paste this when Claude keeps challenging after the useful decision is clear:

```text
Stop challenging and produce the requested output now.

Only ask another question if the answer would prevent an unsafe, impossible, misleading, or implementation-changing output. Move all non-blocking concerns to Defer / Not yet. Keep the output beginner-safe, concrete, and scoped to a 4-week MVP.

Keep Precode authority boundaries: evidence is not approval, generated output is not authority, and no PRODUCT.md, PRD, bead, or code change happens without the required review and approval.
```

---

## The Daily Loop

Every work session follows the same rhythm. Once this loop feels natural, you'll know exactly what to do at every moment.

```
┌─────────────────────────────────────────────────────────┐
│                     THE DAILY LOOP                      │
│                                                         │
│  1. START          Load context. Confirm the bead.      │
│         │                                               │
│         ▼                                               │
│  2. BUILD          Give Claude one clear instruction.   │
│         │                                               │
│         ▼                                               │
│  3. CHECKPOINT     Review what changed. Ask for proof.  │
│         │                                               │
│         ▼                                               │
│  4. DECIDE         Continue / Ask for proof / Stop      │
│         │                                               │
│         ▼                                               │
│  5. CLOSE          Run session-close. Log what happened.│
└─────────────────────────────────────────────────────────┘
```

---

### The 5 decision words

At every checkpoint, you'll make one of 5 decisions. Memorize these:

| Word | Meaning |
|------|---------|
| **Continue** | Work looks good. Keep going. |
| **Ask for missing info** | Claude needs something before it can proceed. |
| **Ask for proof** | Claude says it's done — but I need to see it working. |
| **Review** | Something needs a closer look before moving forward. |
| **Stop** | Something is wrong. Stop all work now. |

> **"It should work" is not proof.** Ask for evidence: a working demo, a recorded check, something you can see and verify yourself. Confidence is not evidence.

---

### The evidence ladder

Not all proof is equal. From weakest to strongest:

```
Claude says it works   →   weakest, not evidence
Working demo           →   better
Recorded check         →   strong (the script ran and passed)
You verified it        →   strong
Reviewed + accepted    →   strongest
```

Never accept a bead as done based only on Claude saying it works.

**Fill in before each checkpoint:**

> My checkpoint question for today's bead: `_________________________________`

---

### Closing your session

When you're done for the day, run:

```
bash scripts/session-close.sh
```

Then ask Claude:

```
Checkpoint the session. Tell me whether we should continue, repair,
split, pause for manual testing, or close. Include what changed,
what evidence exists, and what is still uncertain.
```

Read the summary. If work is incomplete, that's okay — the bead stays open. Never close a bead just because time ran out.

---

## Prompt Cookbook

Copy and paste these prompts. Each one is annotated with why it works.

---

### STARTING

**Load context and confirm the bead**
```
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md,
and tasks/todo.md. Then tell me the active bead, primary authority,
files in play, checks, stop conditions, and anything blocked.
Do not start coding yet.
```
*Why it works: Anchors Claude to the active task before anything else. Prevents aimless building.*

---

**Scope the session**
```
Run the Precode session start. Explain the Context Pack in plain English:
current bead, done-when target, primary authority, files in play,
out of scope, checks, stop conditions, open questions.
```
*Why it works: Forces Claude to explain the full picture in language you can understand.*

---

### BUILDING

**Give a single, scoped instruction**
```
Work only on [specific thing]. Do not touch any files outside the active
bead's files in play. Show me what you plan to do before you do it.
```
*Why it works: Keeps scope tight. "Show me the plan first" catches misunderstandings before they become code.*

---

**Ask for plain-English explanation**
```
Before you write any code, explain what you're about to do as if I've
never written a line of code. What problem does this solve? What will
change in the project?
```
*Why it works: If Claude can't explain it simply, it may not have the right approach.*

---

**Ask for a plan before code**
```
Don't code yet. Just tell me the steps you would take to accomplish this.
I'll approve the approach before you start.
```
*Why it works: Separates thinking from doing. Catches wrong directions early.*

---

**Keep a 4-week MVP small**
```
Context: I am building a 4-week MVP. Challenge only issues that would
change the next 4-week build decision. Sort concerns into Must decide
now, Good enough for MVP, and Defer / Not yet. Do not expand scope.
```
*Why it works: Keeps useful critique while stopping future-version sprawl.*

---

**Close the loop when the answer is good enough**
```
Stop challenging and produce the requested output now. Only ask another
question if the answer would prevent an unsafe, impossible, misleading,
or implementation-changing output. Move non-blocking concerns to Defer /
Not yet.
```
*Why it works: Gives Claude a clear stop signal without ignoring real blockers.*

---

### CHECKING

**Ask for evidence, not confidence**
```
You said this is done. Show me the evidence. Run the recorded check
and tell me what passed, what failed, and what I should verify myself.
```
*Why it works: Forces the distinction between "I think it works" and "here's proof it works."*

---

**Run a recorded check**
```
bash scripts/record-check.sh -- [your check command here]
```
*Why it works: Records the check as durable evidence — not just a one-time terminal output.*

---

**Review what changed**
```
List every file you touched in this session and summarize what changed
in each one. Do not continue until I've reviewed this list.
```
*Why it works: Keeps you in the loop. You should never be surprised by what changed.*

---

### WHEN SOMETHING SEEMS OFF

**Scope check**
```
Use the files-in-play check to confirm you are only touching files
allowed in the active bead. List anything you touched outside that scope.
```
*Why it works: Catches scope creep before it becomes a problem.*

---

**Stop and reset**
```
STOP. Do not make any more changes. Tell me exactly where we are:
what is the active bead, what was changed, and what should happen next.
```
*Why it works: Immediately halts progress and forces a full state report.*

---

### CLOSING

**Session summary**
```
Checkpoint the session. Tell me whether we should continue, repair,
split, pause for manual testing, or close. Include what changed,
what evidence exists, and what is still uncertain.
```
*Why it works: Gives you a clear status report before you walk away.*

---

**Transition check before closing the bead**
```
Before proposing the next bead, explain what evidence proves this bead
is complete and what still requires my approval.
```
*Why it works: Prevents "false done" — when something feels finished but hasn't been proven.*

---

## Memory Management Best Practices

### How Claude Code "remembers" things

Claude Code is not like a note-taking app. It does not remember everything you've ever said. Each session starts with a **fresh context** — meaning Claude only knows what you explicitly load at the start of the session.

This is actually a feature, not a bug. It means you control what Claude knows.

**What Claude remembers across sessions:**
- The 3 active memory files (AGENT.md, DECISIONS.md, tasks/todo.md) — requested explicitly every session
- Precode memory cards (reviewed and saved by you)
- CLAUDE.md files — automatically loaded when Claude opens your project

**What Claude does NOT remember:**
- Your conversation from yesterday
- Something you mentioned casually mid-session
- Anything that wasn't written into a project file

> **The most common beginner mistake:** Starting a session with "continue from where we left off." Claude has no idea where that was. Always load context explicitly.

---

### The golden rule: one topic per task

**One bead. One topic. One session focus.**

Mixing topics in a single session is the fastest way to lose control. When you ask Claude to work on two things at once:
- It loses track of scope
- Files get touched that shouldn't be
- Evidence becomes muddled
- You can't tell what changed or why

If a new idea comes up mid-session: write it down. Don't ask Claude to switch. Finish the current bead first.

**Fill in when a new idea comes up:**

> New idea to come back to (don't act on it now): `_________________________________`

---

### Starting a session with good context

Never say "continue from yesterday." Instead, use these prompting habits:

**1. Load context explicitly every time**
```
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md,
and tasks/todo.md.
```

**2. Be explicit about scope**
```
Only work on [specific task]. Do not touch [file or feature]. Stay within
the active bead's files in play.
```

**3. Ask Claude to confirm what it understood**
```
Before you start, summarize in plain English what you understand the task
to be, what files you'll touch, and what done looks like.
```
*If Claude's summary doesn't match your expectation — correct it before work begins.*

---

### Slash commands

In many Claude Code setups, you can use slash commands for quick actions:

| Command | What it does |
|---------|-------------|
| `/help` | Shows available commands and how Claude works |
| `/memory` | Adds something to Claude's persistent memory |
| `/clear` | Clears the current conversation (starts fresh context) |
| `/review` | Asks Claude to review recent code changes |
| `/init` | Creates or updates a CLAUDE.md file for your project |

> **When to use `/clear`:** When Claude seems confused, is mixing up different tasks, or is referencing something from earlier in the session that's no longer relevant. `/clear` resets the conversation — then reload context with the session-start prompt.

---

### When to clear context vs. continue a thread

**Clear and restart when:**
- Claude starts referencing the wrong task
- You've switched topics mid-session (you shouldn't, but if you did)
- Claude is repeating the same wrong approach
- The session has gone on a long time and Claude seems to have lost the thread

**Continue the thread when:**
- You're still working on the same bead
- Claude's last response was correct and on-scope
- You're just asking a follow-up question about the current task

---

## When Things Go Sideways

These are the common problems beginners hit. Each one has a name, a 2-sentence description, and a recovery prompt.

---

### 1. Agent Wanders

**What happened:** Claude started working on something adjacent to the bead — touching files it shouldn't, adding features you didn't ask for, or expanding scope without permission.

**Why it happens:** The task description was vague, or Claude filled in gaps with its own judgment.

**Recovery:**
```
STOP. Run the files-in-play check. List every file you touched in this
session. Anything outside the active bead's files in play must be reverted.
Tell me what happened and what needs repair before we continue.
```

---

### 2. False Done

**What happened:** Claude said "done" but the feature doesn't work, or works differently than expected.

**Why it happens:** Claude evaluates completion based on code it wrote, not evidence it verified. It's optimistic.

**Recovery:**
```
You said this is done. I need evidence, not confidence. Show me the
recorded check results. Walk me through exactly how I can verify this
works myself, step by step.
```

---

### 3. Context Lost

**What happened:** Mid-session, Claude seems confused — it's asking questions it already answered, referencing the wrong task, or giving generic responses.

**Why it happens:** The conversation got long, or too many topics got mixed in.

**Recovery:**
```
/clear
```
Then restart from the bead-confirmation prompt in **Starting Your Session**. This reloads clean context.

---

### 4. Too Many Changes

**What happened:** Claude made changes but you can't tell what it actually touched or why.

**Why it happens:** You didn't ask Claude to list files before or after working.

**Recovery:**
```
Before anything else: list every file you touched in this session,
what you changed in each one, and why. Do not make any more changes
until I review this list.
```

---

### 5. Stuck in a Loop

**What happened:** Claude keeps trying the same approach, failing, and trying again — without making progress.

**Why it happens:** Claude has hit an unknown constraint and is cycling rather than escalating.

**Recovery:**
```
Stop the current approach. I want a different strategy. Explain:
what is blocking you, what you've already tried, and what you
would try next if you were starting fresh. Do not continue the
previous approach.
```

---

### 6. Over-Challenged MVP

**What happened:** Claude keeps challenging a small bootcamp idea, adding future features, or asking questions after the first version is good enough to define.

**Why it happens:** Claude is trying to be careful, but it is optimizing for exhaustive product critique instead of a 4-week MVP.

**Recovery:**
```
Stop expanding the critique. List only the concerns that would block a
safe 4-week MVP. Move optional concerns, future features, and polish to
Defer / Not yet. Then produce the requested output now. Do not edit
PRODUCT.md, create a PRD, create beads, or write code unless the active
Precode workflow explicitly allows it and I approve.
```

---

## Quick Reference Card

*Keep this visible while you work.*

---

### Session Commands

```bash
bash scripts/session-start.sh     # Start every session with this
bash scripts/checkpoint.sh        # Mid-session status check
bash scripts/session-close.sh     # End every session with this
```

---

### Key Slash Commands

| `/help` | What can Claude do right now |
|---------|------------------------------|
| `/memory` | Save something to Claude's memory |
| `/clear` | Reset the conversation (then reload context) |
| `/review` | Review recent changes |
| `/init` | Set up or update CLAUDE.md |

---

### The 5 Decision Words

| Word | Use when... |
|------|-------------|
| **Continue** | Work looks right. Keep going. |
| **Ask for missing info** | Claude needs more before proceeding. |
| **Ask for proof** | Claude claims done — I need evidence. |
| **Review** | Pause for a closer look. |
| **Stop** | Something is wrong. Halt all work. |

---

### The Evidence Ladder

```
Claude says it works   ← NOT evidence. Don't accept this.
Working demo           ← Better. You can see it.
Recorded check         ← Strong. Script ran and passed.
You verified it        ← Strong. You saw it work.
Reviewed + accepted    ← Strongest. You signed off.
```

---

### Memory Rules at a Glance

- **One bead. One topic. One session.** Never split your attention.
- **Load context first. Always.** Never "continue from yesterday."
- **Scope explicitly.** Tell Claude what NOT to touch, not just what to build.
- **Ask Claude to confirm** what it understood before it starts.
- **`/clear` when confused.** Reset + reload beats spiraling.

---

### Green Flags — Claude is working well

- Names the active bead without being asked
- Lists specific files in play
- Asks for your approval before big changes
- Offers recorded evidence, not just claims
- Tells you when something is out of scope

### Red Flags — Time to intervene

- Can't name the active bead
- Starts coding before you confirmed the task
- References files you didn't expect
- Says "done" without running a check
- Keeps going after you said stop

---

> **When in doubt: checkpoint.**
> `bash scripts/checkpoint.sh`
> Read the output. Then decide.

---

*For the full document compass, go back to `README.md`. For day-to-day operation, use `docs/PRECODE-USER-GUIDE.md`.*
