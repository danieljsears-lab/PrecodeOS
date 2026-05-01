# How To Build Software Using Precode OS + AI Coding Agents
<!-- ANCHOR: build-software-with-precode -->

> AUTHORITY: Beginner-facing educational bridge explaining how software is traditionally planned, designed, built, verified, deployed, and iterated, and how non-technical users do that work with Precode OS and AI coding agents.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, architecture decisions, deployment policy, or generated progress state.
> LOAD_WHEN: Teaching a new non-technical user how software development works, onboarding someone from idea to first Precode project, or explaining how traditional software roles map to Precode workflows.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-04-27

## Start Here: You Are Not Just Prompting

When you use an AI coding agent, it can feel like software is built by typing an idea in plain english and waiting for code to be generated. This is called vibe-coding and is tempting because it is so easy to do. It is also the version that gets beginners into trouble.

Real software still needs clear intent, scope, design choices, code, checks, deployment, and learning. The AI agent can help with many of those jobs, but it should not quietly decide what product you want, what risks you accept, whether a change is done, or whether the next task should start.

Your new job is not to become a product manager or a software engineer overnight. Your job is to become a good orchestrator of building with an AI assistant:

- explain what you want in plain English
- answer product questions
- approve direction and risk
- keep the agent focused
- ask for evidence before accepting work
- learn from what happened

Precode OS helps by giving the repo a small memory, clear owner files, one active task, recorded checks, generated learning reports, and human approval gates.

**Precode is a repo-native operating layer that makes AI coding agents safer for builders who need steering, proof, memory, and recovery more than they need another autonomous agent.**

For the philosophical anchor behind those choices, read `PRECODE-MANIFESTO.md`.

> Plain-English term: A repo is the project folder that holds your app code and the Precode files that guide the agent.

## The Software-Building Journey In Plain English

Software is usually built through a set of repeatable stages. Teams may use different names, but the work is similar.

| Stage | What it means | Who traditionally helped | What can go wrong if skipped | How Precode helps |
|---|---|---|---|---|
| Idea | A rough thought about something useful to build. | Founder, customer, product manager. | The agent codes a vague idea before the problem is clearly understood and well articulated. | Local Source Intake turns rough notes into facts, questions, and candidate requirements. |
| Product shaping | Deciding who it is for, what problem it solves, and what not to build yet. | Product manager, founder, designer. | Scope grows, the first version gets too big, or the wrong user moment is built. | Idea-to-PRD and PRD protocols force problem, non-goals, risks, and smallest useful version. |
| Requirements | Writing what the software should do in a way that can be checked. | Product manager, engineer, QA. | "Done" becomes a feeling instead of a testable outcome. | PRDs and beads connect requirements to checks and closeout evidence. |
| UX/design | Deciding what the user sees and how the user moves through the experience. | Designer, product manager, frontend engineer. | The feature may technically work but feel confusing or incomplete. | Manual verification, screenshots, browser checks, and review inputs capture what the user actually experiences. |
| Architecture | Choosing the shape of the code, data, integrations, and boundaries. | Architect, senior engineer, security reviewer. | Code becomes tangled, risky, hard to change, or unsafe around data and external services. | Project context, architecture docs, and pattern guidance help the agent propose a simple shape before coding. |
| Implementation | Writing or changing the code. | Engineer. | The agent changes too many files, hides product choices in code, or starts related work without approval. | One active bead names files in play, checks, stop conditions, and primary authority. |
| Testing | Proving the change behaves correctly. | Engineer, QA, product owner. | The agent says "done" without proof, or only tests the easy part. | `record-check.sh`, verification protocols, and manual verification record evidence. |
| Deployment | Putting the software where users can use it. | DevOps, engineer, platform owner. | Production breaks, secrets leak, data changes are unsafe, or a dashboard setting is missed. | Sensitive-surface gates require explicit approval before production, external, or dashboard actions. |
| Monitoring and iteration | Watching what happens after release and deciding what to improve. | Product, support, engineering, operations. | Bugs, costs, or user confusion go unnoticed, and future work gets lost. | Diary, memory cards, OS Health, long-horizon maps, and follow-up beads preserve learning. |

You do not need to memorize these roles. You need to recognize that each stage answers a different question. Precode helps you ask those questions in the right order.

## How The Journey Changes With Precode And AI Agents

Before AI coding agents, a non-technical builder usually needed a team or contractor to translate an idea into product plans, design, architecture, code, tests, and deployment.

With AI agents, much of that translation can happen inside the repo. The agent can:

- summarize notes
- ask clarifying questions
- draft a PRD
- propose implementation slices
- write code
- run checks
- explain tradeoffs
- prepare handoff notes

But the agent should not become the final authority for intent, risk, or acceptance. Precode separates what the agent can propose from what the user must approve.

| The agent can... | You still approve... |
|---|---|
| Draft a product plan. | Whether that plan matches your intent. |
| Recommend the smallest first version. | Whether that version is valuable enough. |
| Propose architecture or design patterns. | Whether the tradeoff is acceptable for your project. |
| Implement the active bead. | Whether the work should be accepted after evidence. |
| Suggest the next bead. | Whether the next bead becomes active. |
| Prepare deployment steps. | Whether production, dashboard, secrets, or external actions are allowed. |

> Plain-English term: Authority means "the place where a fact is allowed to be treated as true." In Precode, facts belong in owner files, not random chat messages.

## Choose Your Path: Different Kinds Of Software Work

Not every software idea needs the same process. Precode is safest when you choose the right path before asking the agent to code.

| Project type | What usually matters most | Early risks | Start with |
|---|---|---|---|
| Personal tool | Speed, usefulness, simple data, low ceremony. | The tool grows into a product before privacy, data, or deployment choices are understood. | Local Source Intake or a small implementation bead. |
| Small SaaS app | Accounts, permissions, database, reliability, support, deployment. | Auth, personal data, billing, emails, and production setup appear quickly. | Idea-to-PRD, then decomposition into small beads. |
| Website or landing page | Clear message, visual polish, mobile behavior, forms, analytics. | The agent builds a generic page, misses the audience, or ships unverified forms. | Local Source Intake, design review, browser verification. |
| Automation or workflow | Inputs, outputs, retries, failure handling, permissions. | It works once but fails quietly later or touches the wrong data. | PRD-lite plus tool execution and verification guidance. |
| Data or dashboard project | Data source, definitions, freshness, privacy, charts, decisions. | Wrong metrics, stale data, or unclear ownership of numbers. | Local Source Intake, data-model notes, verification plan. |
| AI-powered feature | Prompt behavior, costs, safety, evaluation, user trust. | Unbounded spend, hallucinated answers, private data exposure, weak evaluation. | PRD, risk review, verification guardrails, spend visibility. |

If you are unsure, ask for workflow selection before coding.

```text
I have a software idea but I am not sure what path it needs. Use Precode workflow selection and tell me whether this should start as local source intake, a PRD, a bead proposal, a challenge planning bead, or a small active task. Do not code yet.
```

## Your New Role As A Non-Technical Builder

You do not need to know every technical detail. You do need to stay responsible for the project direction.

| You do not need to know... | You do need to decide... |
|---|---|
| The exact programming language syntax. | What problem the software solves. |
| The best database library. | What information the app needs to remember. |
| Every architecture pattern name. | Whether the app should be simple, safe, public, private, paid, or experimental. |
| How to write every test. | What behavior would convince you the feature works. |
| How deployment tools work internally. | Whether you approve a production, dashboard, secret, or billing action. |
| Every file in the repo. | Whether the agent stayed inside the approved task. |

Good non-technical builders ask plain questions:

- Who is this for?
- What should happen first?
- What should not happen?
- What is the smallest useful version?
- What could go wrong?
- How will we prove it works?
- What do I need to approve?

## Traditional Roles, Now Translated

Traditional software teams split work across roles. With Precode and AI agents, those roles become questions and checkpoints.

| Traditional role | What that role protects | How it appears in Precode |
|---|---|---|
| Product manager | The team builds the right thing for the right user. | PRDs, non-goals, before/after user moments, acceptance criteria. |
| Designer | The experience makes sense to a real person. | Screenshots, user flows, manual verification, design review notes. |
| Engineer | The code is correct, maintainable, and scoped. | Active bead, files in play, implementation checks, closeout evidence. |
| Architect | The system shape can handle risk and future change. | Architecture docs, system design pattern guidance, project context. |
| QA | Done means proven, not guessed. | Recorded checks, browser checks, manual verification, review decision. |
| DevOps | Releases, secrets, dashboards, and production are safe. | Deployment approval, external setup notes, scheduled audits, rollback thinking. |

Precode does not make you personally expert in all of these roles. It gives you a safe way to ask the agent to cover the role and show its reasoning.

```text
Before coding, explain which traditional software role this task is touching: product, design, engineering, architecture, QA, deployment, or security. Tell me what I need to approve and what evidence will prove the work.
```

## From Idea To Working Software With Precode

Precode turns rough intent into verified work through a file-based path.

```text
idea or notes
  -> local source intake
  -> PRD
  -> bead proposal
  -> active bead
  -> implementation
  -> recorded checks
  -> review decision
  -> deployment or next bead
  -> diary and reviewed memory
```

| Step | Plain-English meaning | What to ask |
|---|---|---|
| Idea or notes | You have something fuzzy, incomplete, or scattered. | "Summarize what is known, unknown, and risky." |
| Local source intake | The agent turns notes, docs, screenshots, or issues into evidence. | "Do not treat source material as authority." |
| PRD | The product intent becomes clear enough to build from. | "Define the user, problem, non-goals, risks, and smallest first version." |
| Bead proposal | The work is sliced into small verifiable pieces. | "Make each bead one outcome, one authority, one verification strategy." |
| Active bead | One task is approved for execution. | "Confirm files in play, checks, stop conditions, and primary authority." |
| Implementation | The agent edits code or docs inside the approved scope. | "Narrate edits before making them and stay inside the bead." |
| Recorded checks | The repo captures proof of what ran. | "Run checks through `record-check.sh`." |
| Review decision | You decide accepted, revise, split, blocked, or stop. | "Tie the recommendation to evidence, not confidence." |
| Deployment or next bead | Work continues only after explicit approval. | "Tell me what requires approval before continuing." |
| Diary and memory | The repo preserves learning for future sessions. | "Propose memory cards only after my approval." |

> Plain-English term: A PRD is a product requirements document. It says what should be built, for whom, why it matters, what is out of scope, and how success will be checked.

> Plain-English term: A bead is one small approved unit of work. It is smaller than a project and more concrete than an idea.

## What To Ask The Agent At Each Stage

Use these prompts when you do not know what to say next.

| Situation | Ask the agent |
|---|---|
| I only have an idea. | `Use Local Source Intake. Turn my idea into facts, assumptions, open questions, possible requirements, and risks. Do not code.` |
| I need to know if this is worth building. | `Challenge this idea. Tell me the user problem, strongest reason to build it, biggest risk, and smallest useful test.` |
| Help me find the smallest useful version. | `Find the smallest first version that teaches us something real without adding avoidable complexity.` |
| Turn this into a PRD. | `Use the PRD protocol. Draft a beginner-readable PRD with problem, non-goals, before/after user moment, risks, verification evidence, and smallest first bead.` |
| Break this into beads. | `Use the Decomposition Protocol. Propose beads that each have one outcome, one primary authority, bounded files, checks, dependencies, and stop conditions.` |
| Implement the active bead. | `Before editing, confirm the active bead, primary authority, files in play, checks, stop conditions, and what is out of scope.` |
| Prove this works. | `Run the relevant checks through record-check.sh and explain the evidence in plain English.` |
| Help me decide if it is done. | `Run a completion check. Recommend accepted, revise, split, blocked, or stop based on recorded evidence and manual verification.` |
| Prepare this for deployment. | `List the deployment, secret, dashboard, database, rollback, and approval steps. Do not deploy until I explicitly approve.` |
| Record what we learned. | `Summarize learning diary candidates and propose memory cards for my approval. Do not make memory authority.` |

For more prompts, use `tasks/reference/PROMPT-PATTERNS.md`.

## The Mental Models You Need

### Scope: One Thing At A Time

Scope is the boundary around the current work. In Precode, the active bead protects scope. If the agent starts doing adjacent work, checkpoint and split.

```text
Stop and checkpoint. Is this still one bead, or should we split the new work into a separate proposal?
```

### Authority: Facts Live In The Right File

Precode uses owner files so important facts are not scattered across chat. Product intent belongs in PRDs. Hard decisions belong in `DECISIONS.md`. Current execution belongs in `tasks/todo.md` and the active bead.

```text
Which file owns this fact, and should we promote it there before acting on it?
```

### Evidence: Done Means Checked

An agent saying "this should work" is not enough. Evidence is a recorded check, manual verification, screenshot, review decision, or closeout note tied to the bead.

```text
Show me the evidence that proves this bead is complete. If evidence is missing, tell me the next check to run.
```

### Risk: Stronger Changes Need Stronger Approval

Changing text is low risk. Touching auth, payments, data, uploads, deployment, secrets, or external systems is higher risk. Higher risk needs clearer approval and stronger proof.

```text
Classify the risk of this task and tell me what approval gates or rollback notes are required before work continues.
```

### State: The Repo Remembers What Chat Forgets

Chat history is useful, but it is not durable project state. Precode stores durable state in files and generated evidence, so future sessions can recover what happened.

### Handoff: Future Agents Need Durable Context

A handoff is not a new task approval. It is a safe orientation packet for the next session or agent.

> Plain-English term: A check is a command or manual review that proves something about the work. A check should be recorded so the repo remembers it.

> Plain-English term: Deployment means putting software somewhere real users can access it. Deployment is riskier than local coding because it can affect users, data, costs, domains, and production settings.

> Plain-English term: Rollback means the plan for undoing or safely recovering from a bad change.

## Worked Example: Personal Tool vs Simple SaaS

Imagine this idea:

```text
I want an app that helps me track client follow-ups.
```

That could be a small personal tool, or it could become a SaaS product. The difference matters.

| Choice | Personal tool | Simple SaaS app |
|---|---|---|
| Users | Just you. | You and other users or customers. |
| Data | Your own client notes. | Other people's accounts and possibly private data. |
| Login | Maybe none at first. | Usually required. |
| Storage | Local file or simple database may be enough. | Production database, permissions, backups, privacy expectations. |
| Deployment | Optional or simple. | Required if others need access. |
| Risk | Lower if private and local. | Higher because users, auth, email, billing, and support may appear. |
| First good bead | Create a local follow-up list with add/edit/done states. | Define PRD and auth/data boundaries before implementation. |

### Raw Idea

Start by asking for intake:

```text
Use Local Source Intake for this idea: "I want an app that helps me track client follow-ups." Summarize facts, assumptions, open questions, candidate requirements, and whether this should start as a personal tool or SaaS. Do not code.
```

Good intake might reveal:

- The user wants to remember who to contact next.
- The first version may only need name, next follow-up date, status, and notes.
- Unknown: is this private for one person or shared by a team?
- Risk: client notes may contain private information.
- Candidate first bead: build a local list view and add/edit form.

### PRD Question

If it is a personal tool, the PRD can be light:

```text
Draft a lightweight PRD for a private personal follow-up tracker. Keep the first version local and simple. Name what is out of scope, especially accounts, billing, team sharing, and production deployment.
```

If it is SaaS-like, slow down:

```text
Draft a PRD for a simple SaaS follow-up tracker. Include auth, personal data, permissions, deployment, email, and privacy risks. Do not propose implementation beads until those risks are clear.
```

### Smallest First Bead

For the personal tool:

```text
Propose the smallest first bead: a local follow-up list where I can add, edit, mark done, and see next follow-up date. Include files in play, checks, and stop conditions.
```

For the SaaS version:

```text
Before coding, propose planning beads for auth boundary, data model, and deployment assumptions. Keep implementation separate until I approve the product and security direction.
```

### Implementation Request

Once a bead is active:

```text
Implement only the active bead. Confirm the primary authority, files in play, checks, and stop conditions before editing. Stop if this turns into auth, deployment, billing, or team-sharing work.
```

### Verification Request

```text
Run the checks through record-check.sh. Then tell me what manual behavior I should verify: add a client, edit it, mark it done, and confirm the follow-up date displays correctly.
```

### Review Decision

```text
Based on recorded checks and manual verification, recommend accepted, revise, split, blocked, or stop. Do not activate the next bead.
```

### Next Safe Step

If the personal tool works, the next step might be search, filtering, import/export, or persistence. If the SaaS path is chosen, the next step may be auth and data privacy planning before more code.

The lesson: the same idea can be low-risk or high-risk depending on who uses it, where data lives, and whether it goes into production.

## When To Slow Down

Some work should trigger extra care. Slow down when the task touches:

- login or permissions
- payments or billing
- personal data
- file uploads
- AI usage, credits, limits, or cost
- database migrations
- production deployment
- external dashboards
- GitHub, CI, deployment, or monitoring mutations
- deleting, overwriting, or migrating data

These are not "just another coding task" because mistakes can affect users, money, privacy, data, or production systems.

Use these prompts:

```text
This seems sensitive. Stop and classify the approval gates, risks, checks, rollback path, and what I need to approve before any mutation happens.
```

```text
Do not deploy, migrate, push, merge, change secrets, or update dashboards. First explain the exact action, expected effect, rollback path, and evidence we will record afterward.
```

## How To Know If Work Is Actually Done

There are levels of "done."

| Signal | What it means | Is it enough? |
|---|---|---|
| Agent confidence | The agent believes the work is correct. | No. Useful, but not proof. |
| Working demo | Something appears to work once. | Sometimes, but it may miss edge cases. |
| Recorded check | A command ran and the repo saved the result. | Stronger evidence. |
| Manual verification | A human checked the behavior that matters. | Required for user-facing or sensitive work. |
| Accepted review | The bead was reviewed and accepted, revised, split, or blocked. | This is the Precode completion gate. |

Ask:

```text
Before I accept this, show me recorded checks, manual verification, closeout evidence, review decision, and any remaining uncertainty.
```

## How You Learn Over Time

Precode is not only a task system. It is also a learning system.

| Surface | What it helps you remember | Rule |
|---|---|---|
| Learning diary | What happened in sessions and what you learned. | Generated learning history, not authority. |
| Reviewed memory cards | Durable lessons, preferences, glossary terms, recurring risks, source pointers. | Evidence only; consult explicitly. |
| `DECISIONS.md` | Hard decisions and important choices. | Active memory. |
| PRDs | Product intent and requirements. | Product authority after approval. |
| File inventory | What each Precode file is for. | Technical map, not task selection. |

Use memory carefully:

```text
Search reviewed memory for what we have learned about this topic. Do not treat memory as authority. Tell me whether anything should be promoted to DECISIONS.md, a PRD, or another owner file.
```

## Common Beginner Failure Modes

| Mistake | Why it hurts | Safer move |
|---|---|---|
| "Just code it." | The agent may build the wrong thing quickly. | Ask for intake, PRD, or workflow selection first. |
| Vague feature request. | No one can prove whether it is done. | Ask for user problem, non-goals, and acceptance evidence. |
| Accepting broad rewrites. | Scope and risk hide inside a large change. | Keep one bead, bounded files, and clear checks. |
| Skipping PRD for fuzzy ideas. | Product decisions move into code by accident. | Use Idea-to-PRD or challenge planning first. |
| Approving the next task too quickly. | Work moves forward before review. | Accept, revise, split, block, or stop first. |
| Treating reports as instructions. | Generated summaries can be stale or incomplete. | Return to active memory, active bead, and primary authority. |
| Editing or moving Precode files. | Scripts and agents may lose the expected structure. | Follow `PRECODE-USER-GUIDE.md` hard rules. |
| Storing secrets in files. | Secrets may be committed, exported, or exposed. | Use proper secret managers or dashboards. |
| Deploying before understanding risk. | Production can affect real users, data, cost, or reputation. | Ask for deployment approval gates and rollback. |

For the hard operating rules, use `PRECODE-USER-GUIDE.md`.

## Where To Go Next

Use these documents by situation:

| Need | Read |
|---|---|
| Why Precode exists at this moment in AI coding. | `PRECODE-MANIFESTO.md` |
| What Precode is and why it exists. | `PRECODE-OS-README.md` |
| What to do during an actual session. | `PRECODE-USER-GUIDE.md` |
| Deep technical architecture and maintainer framing. | `PRECODE-ARCHITECTURE-OVERVIEW.md` |
| More copyable prompts. | `tasks/reference/PROMPT-PATTERNS.md` |
| Technical map of Precode files. | `PRECODE-FILE-INVENTORY.md` |

## Change Log

| Version | Date | Summary |
|---|---|---|
| v0.1.1 | 2026-04-27 | Added navigation to `PRECODE-MANIFESTO.md` as the philosophical anchor behind Precode's anti-drift, steering, brake, and recovery posture. |
| v0.1.0 | 2026-04-27 | Initial standalone beginner bridge explaining the traditional software-building journey, how it changes with Precode OS and AI coding agents, adaptive project paths, translated software roles, idea-to-evidence flow, prompts by stage, mental models, a personal-tool vs SaaS walkthrough, slow-down triggers, completion evidence, learning surfaces, and common beginner failure modes. |
