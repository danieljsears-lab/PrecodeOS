# PrecodeOS Daily Cockpit
<!-- ANCHOR: precode-daily-cockpit -->

> AUTHORITY: Builder-first daily loop, next-step, health, diary, prompt-catalog, protocol-catalog, recovery, and reference surface for operating PrecodeOS during normal work.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, PRD approval, bead activation, implementation acceptance, generated progress state, destructive repair approval, protocol authority replacement, prompt authority replacement, generated evidence authority, or deep architecture guidance.
> LOAD_WHEN: A builder is starting, running the daily build loop, choosing the next safe move, checking health, reading the diary, learning the prompt/protocol catalog, recovering, or finding the smallest reference surface during a PrecodeOS session.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.59
Last updated: 2026-08-06

Use this cockpit first once PrecodeOS is installed or you are already working inside a PrecodeOS repo. Stop here for normal work unless this page routes you to a specific setup, manual, troubleshooting, prompt, or protocol surface.

The cockpit has four first-class daily operating sections and two required reference catalogs. The first-class sections are deliberately short: **Daily Loop**, **Next**, **Health**, and **Diary**. The full Prompt Patterns Catalog and full Protocol Catalog are included lower on this page as reference shelves so new users can learn the system without turning the first screen into a manual.

Use this page as the builder's control surface for host-agent work. The Daily Cockpit is where you decide what to ask, what state matters, what proof is missing, and when to stop; Codex, Claude Code, Cursor, Copilot, Gemini, or another host agent is where scoped work happens inside approved Precode boundaries. Before agent work, use Daily Loop and Next to name the active bead, authority, files, approvals, and stop condition. During work, keep the agent inside those bounds and use Agent Access Level Check when risk rises; Tool Execution owns the access ladder, and the cockpit only applies it to the current moment. For proof and review, use Health, Prove, Review, recorded checks, and manual verification before accepting anything. For handoff or stop, use Approved-Bead Handoff only after one bead is approved, or Close/Diary to record what changed, what was proven, what is parked, what approval remains, and the next safe prompt.

For host-agent returns, use the Host-Agent Return Loop inside the same cockpit: `Prepare -> Bound -> Send -> Return -> Prove -> Review -> Close/Next`. Prepare names the active bead, primary authority, files in play, and stop condition. Bound names allowed actions, Tool Execution access level, approval required before risky actions, and forbidden actions. Send gives the host agent one scoped prompt. Return requires changed files, checks and results, manual verification, missing proof, unresolved risks, approval still required, and forbidden actions not taken. Prove and Review happen before acceptance. Close/Next records what changed, what is parked, and the next safe prompt without activating another bead.

Generated reports, generated HTML, logs, sidecars, prompt catalog rows, and protocol catalog rows are evidence or navigation only. Active memory and owner files stay authoritative. Before work resumes, return to `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, the active bead, the primary authority file, and your explicit approval.

First-reader route:

| Situation | Go here |
|---|---|
| PrecodeOS is not installed in the target project | `PRECODE-GUIDED-SETUP.md` |
| PrecodeOS is installed or work is resuming | Stay in this Daily Cockpit |
| You only have a rough idea | `Ideation: use First PRD Walkthrough for my rough idea.` |
| Setup, state, checks, generated reports, or first-session behavior feel broken | `PRECODE-TROUBLESHOOTING.md` or `I am stuck, help me.` |

Document roles are intentionally narrow: `../README.md` is the public package compass, `PRECODE-SUPPORT-RUNBOOK.md` is helper triage and live-call sequencing, `PRECODE-GUIDED-SETUP.md` is setup-only and owns setup mechanics and copy/apply rules, `../tasks/templates/PRECODE-FIRST-SESSION-CARD.md` is compact builder build order after setup validates, this cockpit is the beginner-facing operating home base after validation, `PRECODE-USER-GUIDE.md` is the deeper operating manual, `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` is the educational bridge, and `PRECODE-OS-README.md` is the conceptual Builder OS explainer. For Claude Code classroom habits, see `CLAUDE-CODE-FIELD-GUIDE.md`. For symptom lookup, see `PRECODE-TROUBLESHOOTING.md`. Prompt Patterns supplies copyable prompts; it is not live-call authority.

For the builder journey, the Daily Cockpit owns the operating path; the User Guide explains the same path in more depth.

## Daily Loop

Daily Loop is the build-loop surface. Use it to understand where the work is in the cycle before letting a host agent continue. Repeated bead work uses this rhythm: `Active -> Changed -> Proven -> Parked -> Approval -> Next`.

```text
Active -> Changed -> Proven -> Parked -> Approval -> Next
```

| Loop stage | What to inspect | Go to |
|---|---|---|
| Active | Current bead, primary authority, files in play, done-when target, and stop conditions. | [Health](#health) if state is unclear; [Next](#next) if the action is unclear. |
| Changed | What changed in files, behavior, decisions, scope, or assumptions. | [Diary](#diary). |
| Proven | Recorded checks, manual verification, evidence gaps, and stale generated reports. | [Health](#health). |
| Parked | Candidate Queue items, deferred follow-ups, memory candidates, or explicit defer/kill notes. | [Diary](#diary) for what transpired; [Next](#next) for routing. |
| Approval | PRD approval, bead activation, review acceptance, transition approval, release approval, or repair permission still required. | [Next](#next). |
| Next | The next safe move and stop condition. | [Next](#next). |

Start or resume with this prompt:

```text
Start: run the Precode session start and explain the Context Pack before editing.
```

Command:

```bash
bash scripts/session-start.sh
```

Expected output: active memory reminder, current bead, done-when target, primary authority, files in play, checks, stop conditions, router guidance, and generated-report warning.

The optional local `precode` facade is only a shortcut over canonical commands. It prints the underlying script command and does not approve work, transitions, setup mutation, releases, generated evidence, prompt use, or protocol loading as authority. The optional npm `precodeos` entry stays in setup, fast verified setup, or existing-Precode refresh lanes only; use it on live calls only after `npm view @precodeos/precodeos version` confirms availability, and fall back to the Python/local checkout command if npm is unavailable or unverified. Preview writes nothing, apply requires current `SP-ID` or `UP-ID` approval, and npm availability is not registry freshness, update permission, package-manager behavior, or the normal cockpit surface.

## Next

Next tells you the safest next move. It does not choose tasks, rank Candidate Queue items as implementation priority, approve PRDs, activate beads, accept review, approve transition, approve release, or authorize coding.

I only have a rough idea. Use `Ideation: use First PRD Walkthrough for my rough idea.` The single beginner-facing path through Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and PRD shaping. These are steps in the path, not competing commands.

| Moment | Use | Safe next output |
|---|---|---|
| You only have a rough idea | `Ideation: use First PRD Walkthrough for my rough idea.` | Idea -> Brief -> Packet -> Intake -> PRD path without PRD approval or coding. |
| You need a workflow decision | `Use the Workflow Selection Protocol.` | Recommended workflow, artifact, authority source, approval needed, stop condition. |
| You need to park future intent | `Queue: review Candidate Queue as parked intent.` | Candidate status, evidence, promotion target, what cannot be decided from the queue. |
| Candidate or implementation-plan commitment is at issue | Plan Mode Candidate Craft Loop | `Idea -> Plan Mode -> Candidate Queue -> Plan Mode -> Implementation Plan -> Approved Bead -> Build`. |
| Work may be ready to close | `Close: run session close...` / `bash scripts/session-close.sh` | Work digest, checks, blockers, approvals, learning context, Close State. |
| Transition may be possible | `python3 scripts/bead-transition.py` | Readiness evidence only. Use `--approve` only after explicit approval. |
| Something feels broken or confusing | `Recover: I am stuck, help me.` | Symptom, first safe move, owner surface, up to three read-only checks, next safe action, forbidden actions. |
| A host agent returned work | `Review returned agent work before I accept it.` | Changed files, checks, manual verification, missing proof, approval still required, parked follow-ups, forbidden actions not taken, next safe prompt. |
| You are back after AFK or handoff | `Re-enter after AFK or handoff.` | Reloaded state, changed files, recorded checks, Run Contract if present, proof still missing, approval still required, next action as continue, review, split, block, or handoff. |

If the generated next-step decision is `author next bead`, treat it as an accepted hold: the current bead is accepted, but transition still needs a next bead proposal or authored bead. If output shows next-work source reconciliation, compare the router pointer, Closeout next bead, Handback or Noticed recommendation, and existing bead-file readiness before transition. Do not continue implementation, repeat acceptance review, approve transition, or activate a bead from generated classification.

Use this before letting work continue:

```text
Next: name the safest next Precode move, the owner source, the approval still required, the stop condition, and what generated evidence does not decide.
```

## Health

Health is for health-focused tasks: whether the repo, session, evidence, and loop state are coherent enough to keep operating. It does not decide what to build, approve a PRD, activate a bead, accept review, approve transition, or make generated reports authoritative.

| Moment | Prompt or command | What to inspect | Boundary |
|---|---|---|---|
| Start or reset context | `Start: run the Precode session start and explain the Context Pack before editing.` / `bash scripts/session-start.sh` | Active bead, done-when target, files in play, checks, stop conditions, router guidance. | Orientation only before work. |
| Check loop health | `python3 scripts/loop-health.py` | Focus, stoppability, closeability, evidence, steerability, graph coherence. | Advisory generated evidence only. |
| Refresh health report | `python3 scripts/os-health.py` | `OS-HEALTH.md`, Doctor Dashboard rows, `logs/os-health.json`, work graph reports. | Warnings require source inspection; output is not authority. |
| Record proof | `bash scripts/record-check.sh -- <command>` | Recorded checks, command output, check ledger. | A check is evidence, not review acceptance. |
| Check completion health | `python3 scripts/completion-check.py` | Missing or stale closeout, checks, release-evidence cues, reference follow-through. | Not release approval, acceptance, or transition approval. |
| Diagnose broken or confusing state | `Recover: I am stuck, help me.` | Symptom, first safe move, owner surface, up to three read-only checks. | Not repair, rollback, overwrite, setup mutation, or transition approval. |

If health is unclear, ask:

```text
Health: show active state, current bead, primary authority, files in play, latest checks, generated-report warnings, and what must be inspected before editing.
```

Before accepting returned host-agent work, ask:

```text
Review returned agent work before I accept it. Show the active bead, primary authority, files changed, recorded checks and results, manual verification, proof still missing, unresolved risks, approval still required, parked follow-ups, forbidden actions not taken, and next safe prompt. Do not accept implementation, approve transition, activate another bead, mutate external systems, or treat generated reports, generated HTML, agent confidence, screenshots, PR status, or chat summaries as proof by themselves.
```

Stop if the agent cannot name the active bead, primary authority, files in play, checks, and stop conditions.

## Diary

Diary is for what transpired: what changed, what was proven, what was learned, what was parked, and what may deserve promotion later. It does not replace active memory, owner files, PRDs, beads, closeout evidence, review decisions, or current code.

| Surface | Use it for | Boundary |
|---|---|---|
| `logs/learning-diary.md/jsonl` | Session lessons, user learning, and durable observations. | Generated learning evidence only. |
| `logs/bead-build-journal.md/jsonl` | Implemented-bead path, build-change journal, optional PRD/Candidate Queue provenance, reversal/supersession provenance. | Not active memory, Candidate Queue authority, acceptance, or transition approval. |
| `logs/build-attribution-ledger.md/json` | Who-built-what evidence, contributor role, tool surface, uncertainty, Git hints. | Not blame, scoring, telemetry, merge approval, or release approval. |
| `memory/cards/*.md` and `logs/memory-index.md/json` | Reviewed memory and search/citation aid. | Evidence only until approved owner-file or protocol promotion. |
| Closeout work digest and suggested commit message | Plain-English change summary and advisory commit subject. | Does not stage, commit, push, accept review, approve transition, or approve release. |

Use these prompts:

```text
Diary: read the learning diary, bead build journal, attribution evidence, closeout digest, and reviewed memory relevant to this bead. Tell me what transpired, what changed, what was proven, what was parked, what is uncertain, and what would need explicit promotion approval.
```

```text
Review this memory for promotion. Cite the memory claim, source pointers, current status, proposed owner, promotion action, approval required, and stop condition. Do not create cards, edit owner files, approve PRDs, activate beads, choose tasks, accept implementation, or change active memory without my approval.
```

```text
Search reviewed memory with selective recall. Use compact citation, demotion decision, and filing recommendation fields when present. Treat weak matches as search leads only, not memory to load, and do not file or promote anything automatically.
```

Commands when the owning workflow calls for them:

```bash
python3 scripts/update-learning-diary.py --append
python3 scripts/update-bead-build-journal.py --append
python3 scripts/build-attribution-ledger.py
python3 scripts/update-memory-index.py
python3 scripts/memory-check.py --query "topic words" --recall
```

## Reference And Support

Everything below supports the four first-class cockpit sections. These surfaces help new users learn and look up the system; they are not peer daily operating sections.

| Need | Use | Boundary |
|---|---|---|
| Install or refresh PrecodeOS | `PRECODE-GUIDED-SETUP.md` and setup/upgrade/update-plan previews. | Setup-only; preview is read-only and not copy/update approval. |
| First session feels too large | `../tasks/templates/PRECODE-FIRST-SESSION-CARD.md` | Compact post-setup aid; not a start page, router, task selector, approval shortcut, or protocol replacement. |
| Deeper manual help | `PRECODE-USER-GUIDE.md` | Deeper operating manual behind the Daily Cockpit; not a second start page. |
| Claude Code classroom habits | `CLAUDE-CODE-FIELD-GUIDE.md` | Tool companion; not universal operating authority. |
| Learn software-building concepts | `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` | Educational bridge; not the daily operating surface. |
| Support-assisted adoption or recovery | `PRECODE-SUPPORT-RUNBOOK.md` | Helper-facing companion; not product truth or approval. |
| Symptom lookup | `PRECODE-TROUBLESHOOTING.md` and `../tasks/reference/RECOVERY-PROTOCOL.md` | Diagnose before repair, overwrite, rollback, setup mutation, or transition. |
| Technical file ownership | `PRECODE-PACKAGE-FILE-INVENTORY.md` | Package dictionary; not active memory or task selection. |
| Generated reading aid | `docs-html/*.html` | Easier browsing and copy cards; Markdown, Prompt Patterns, and protocols remain canonical. |
| PRD review reading aid | `tasks/prds-html/*.html` | Review convenience only; Markdown PRDs remain canonical. |
| Host adapters and shims | `adapters/*.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.agents/` | Compatibility surfaces only; not alternate active memory or approval authority. |

### Reference Learning Shortcuts

These notes preserve the common Precode routes as reference material. They are not first-class daily operating sections; Daily Loop, Next, Health, and Diary remain the cockpit surface.

| Learning need | Reference cue | Boundary |
|---|---|---|
| Which artifact, idea, or path do I need? | `Ideation: map my current moment to the right Precode path before PRD shaping or coding.` It should return Workflow Selection, First PRD Walkthrough, or Artifact Chooser routing without task approval, artifact generation, PRD approval, bead activation, implementation permission, or later human PRD approval. | Use Workflow Selection when the answer depends on current state. |
| Where should this answer live? | `Use Question-To-Artifact Filing for this answer.` It recommends stay in chat, Local Source Intake, Candidate Queue, Memory Promotion Review, PRD/owner-file work, `DECISIONS.md`, decomposition review, defer, kill, or maintainer roadmap note. | It does not file automatically, approve promotion, choose tasks, or activate beads. |
| Review candidates | `Queue: review Candidate Queue as parked intent.` Review candidates as parked intent, not task authority. | Do not update active memory, approve a PRD, activate a bead, reserve bead IDs, rank implementation priority, choose next work, or start coding. |
| Is this source ready to promote? | Source-To-Promotion Hygiene Review checks source refs, evidence strength, open conflicts, proposed owner, promotion action, approval required, and stop condition. | It does not promote files, approve PRDs, choose tasks, or activate beads. |
| Which skill-style prompt should I use? | `Use Skill Playbook Ergonomics.` One recommended invocation or owner surface. Skill map output is advisory only. | It does not show a skill catalog, install skills, approve extension implementation, add registries, create optional packs, run mutating commands, or replace owner protocols. Do not treat skill output as authority. |
| Review hypothesis | Hypothesis Review / Learning Loop can report untested, tested, narrowed, killed, promoted, stale, or not applicable. | It does not approve product direction, rank candidates, activate beads, require analytics, or create a database. |
| Clarify acceptance | `Acceptance: review vague criteria with optional EARS-style wording.` Do not require EARS syntax, approve the PRD, activate beads, treat wording as proof, or code. | This is writing guidance only, not PRD approval or proof. |
| Quality map | `Quality map: translate the relevant engineering standard into a Precode routing question.` Use the Engineering Quality Standards Taxonomy when a professional standard needs a plain Precode route. | The taxonomy does not make external frameworks public package authority; the checker is advisory only and does not approve coding, review, release, or generated proof. |
| Check quality text contract | `python3 scripts/engineering-quality-check.py --check` checks quality-floor wording before risk gets hidden. | Advisory only; it does not inspect app code, run lint/tests, approve implementation, accept review, or create proof. |
| Code quality snapshot | `Run Product Code Quality Snapshot for the active bead.` Use this after code changes when you need changed-file, declared-scope, proof, and Project Linter Evidence before accepting work. | Project Linter Evidence is discovery only; the snapshot does not run lint/tests, certify code quality, accept review, approve release, create tasks, or create generated proof. |
| Check task suitability | `python3 scripts/task-suitability-check.py --check` can return continue, clarify, route, split, block, or stop. | It does not approve work, choose tasks, approve PRDs, activate beads, authorize implementation, accept review, approve commands, or create proof. |
| Check The Vibe-To-Agentic Boundary | Ask whether a fast sketch can stay tiny, reversible, and evidence-only, or must route me through the right Precode owner workflow before coding. | It does not approve a PRD, activate a bead, accept implementation, approve release, mutate files, create generated proof, or code. |
| Approved handoff | `Use Approved-Bead Handoff for the current approved bead.` A scoped host-agent build handoff with active bead, authority, files in play, allowed actions, proof, checks, stop conditions, blocked escape, review-return shape, approval gates, and generated-report warning. | It does not activate a bead, choose tasks, accept review, approve transition, or create generated handoff output. |
| Team or delegated work | Multiple people or delegated work may affect one product. Use Team or Re-entry only when the current stage calls for it. | It does not approve merge, re-entry, GitHub mutation, external mutation, review acceptance, or transition. |
| Review attribution | Build Attribution Ledger, build attribution review, and who-built-what evidence belong in Diary and review reference. | Attribution evidence is not blame, scoring, telemetry, implementation acceptance, merge approval, or release approval. |
| Release prep | Release: prepare release evidence without release action. Late-stage release-prep evidence, release-quality cues, and approval questions. It does not deploy, configure providers, mutate dashboards, merge, roll back, certify production readiness, or approve release. | Release Readiness prepares human approval questions only. |

First-product spine: `Idea -> Brief -> Packet -> Intake -> PRD -> Architecture? -> Bead -> Proof -> Review -> Close`. Architecture? is conditional: run Architecture Shaping only for approved PRDs touching auth, data, APIs, integrations, dependencies, migrations, external services, multi-step workflows, or multi-system behavior. For low-risk approved PRDs, proceed to bead decomposition and record the skip reason in the PRD architecture-impact section or bead notes.

- Idea: rough idea or messy notes.
- Brief: Product Brief after at most three high-level questions.
- Packet: reviewed Conviction Packet / Precode Ingestion Packet.
- Packet handoff: reviewed Conviction Packet / Precode Ingestion Packet with Local Source Intake readiness self-check.
- Intake: Local Source Intake summary.
- Owner-file promotion check: if intake found stable facts for owner files, run Source-To-Promotion Hygiene Review, get user approval, apply only approved facts, then re-validate before PRD shaping.
- PRD: human-reviewed PRD shaping and approval.
- Bead: candidate decomposition, then approved active bead.
- Proof: recorded checks and manual evidence.
- Review: human review, with advisory lanes only when needed.
- Close: closeout evidence and explicit Close State.

Command surface triage remains reference guidance: `## Command Surface Triage` means use the smallest command set that matches your moment. Beginner daily work starts with `bash scripts/session-start.sh`, `python3 scripts/next-step.py`, `python3 scripts/loop-health.py`, `python3 scripts/os-health.py`, and `bash scripts/record-check.sh -- <command>`. Setup, support, or recovery commands belong in setup/support/recovery references. Advanced evidence or review and maintainer validation are conditional reference/support surfaces. Command surface triage is reader guidance only; it does not approve work, change tool-call classes, choose tasks, or make generated reports authoritative.

Use the smallest command set that matches your moment. Beginner daily work: `bash scripts/session-start.sh`, `python3 scripts/next-step.py`, `python3 scripts/loop-health.py`, `python3 scripts/os-health.py`, `bash scripts/record-check.sh -- <command>`. Maintainer validation stays out of the normal beginner loop.

Advanced reference cue: Advanced Trigger Summaries, Use An Advanced Owner Surface, stable-docs question, and why this is not a beginner starting route are catalog/reference concepts. Use `../tasks/reference/PROMPT-PATTERNS.md` for copyable advanced prompts and the named owner protocol for detailed rules.

Quality and boundary cue: `Check: name the active bead, authority, files, first check, suitability decision, quality risk, vibe-to-agentic boundary, stop conditions, and every-bead rhythm before editing.` If the quality answer is vague, run `python3 scripts/engineering-quality-check.py --check`. Keep exploratory work tiny, reversible, and evidence-only; if it is not safe, keep it tiny, reversible, and evidence-only only until you route through the right Precode owner workflow before coding.

Recovery cue: when stuck, name the symptom, first safe move, owner surface, up to three read-only or advisory checks, next safe prompt or action, and forbidden actions before repair. Forbidden actions include no delete, overwrite, regenerate, transition approval, rollback, setup/update mutation, or destructive command without explicit approval.

First-session card reminder: use `../tasks/templates/PRECODE-FIRST-SESSION-CARD.md` as a compact linear builder build-order card when the full cockpit catalogs feel too large. It includes the conditional `Owner Files?` gate before PRD shaping, the owner-file promotion check, and the conditional `Architecture?` bridge before bead decomposition. Architecture Shaping is mandatory only for architecture-sensitive approved PRDs; low-risk approved PRDs can proceed to bead decomposition with a recorded skip reason. The card is one page of prompts, checks, and build-order guidance; it does not become a start page, task selector, approval shortcut, setup guide, router, command wrapper, or protocol replacement.

Plan Mode Candidate Craft Loop reminder: in Codex, use `/plan`; in Claude Code, use Plan Mode; in other agents, use an equivalent read-only planning mode. Use it Before developing a Candidate Queue entry and Before developing an implementation plan for a selected candidate. It does not approve a PRD, rank work for implementation, activate a bead, update `tasks/todo.md`, authorize coding, or skip owner-file, decomposition, proof, review, and transition gates.

Review memory promotion cue: Search results may name a proposed promotion owner, but promotion is manual and requires explicit approval before any card write, owner-file edit, PRD amendment, protocol update, bead change, or active-memory change.

## Full Prompt Patterns Catalog

This catalog is complete for the 135 copyable prompt cards extracted from `../tasks/reference/PROMPT-PATTERNS.md`. It is a learning and lookup shelf inside the cockpit. Expanded prompt bodies remain authoritative in Prompt Patterns and in the generated Daily Cockpit HTML cards. Catalog rows do not approve work, choose tasks, activate beads, accept review, approve transition, approve release, mutate files, or make generated evidence authoritative.

### Discovery Prompts

| Prompt | Use | Source | Boundary |
|---|---|---|---|
| [Artifact Chooser](../tasks/reference/PROMPT-PATTERNS.md#artifact-chooser) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Question-To-Artifact Filing](../tasks/reference/PROMPT-PATTERNS.md#question-to-artifact-filing) | a useful answer from chat, planning, review, discovery, source intake, memory recall, or maintainer analysis should not disappear, but its durable destination is unclear. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Product Discovery Interview Skill](../tasks/reference/PROMPT-PATTERNS.md#product-discovery-interview-skill) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Hypothesis Review / Learning Loop](../tasks/reference/PROMPT-PATTERNS.md#hypothesis-review-learning-loop) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Accessibility Advisor Fit Interview](../tasks/reference/PROMPT-PATTERNS.md#accessibility-advisor-fit-interview) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Precode Idea Coach](../tasks/reference/PROMPT-PATTERNS.md#precode-idea-coach) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [First PRD Walkthrough](../tasks/reference/PROMPT-PATTERNS.md#first-prd-walkthrough) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Precode Conviction Handoff](../tasks/reference/PROMPT-PATTERNS.md#precode-conviction-handoff) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Local Source Intake](../tasks/reference/PROMPT-PATTERNS.md#local-source-intake) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Source-To-Promotion Hygiene Review](../tasks/reference/PROMPT-PATTERNS.md#source-to-promotion-hygiene-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Owner-File Promotion Before PRD Shaping](../tasks/reference/PROMPT-PATTERNS.md#owner-file-promotion-before-prd-shaping) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Client Engagement Intake](../tasks/reference/PROMPT-PATTERNS.md#client-engagement-intake) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Product Constitution Review](../tasks/reference/PROMPT-PATTERNS.md#product-constitution-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Founder-Friendly Product Brief](../tasks/reference/PROMPT-PATTERNS.md#founder-friendly-product-brief) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Alignment / Product Brief](../tasks/reference/PROMPT-PATTERNS.md#alignment-product-brief) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Ubiquitous Language Review](../tasks/reference/PROMPT-PATTERNS.md#ubiquitous-language-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Glossary Card Proposal](../tasks/reference/PROMPT-PATTERNS.md#glossary-card-proposal) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Domain Naming Review](../tasks/reference/PROMPT-PATTERNS.md#domain-naming-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |
| [Idea To Evidence Trace](../tasks/reference/PROMPT-PATTERNS.md#idea-to-evidence-trace) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not promote source evidence, approve PRDs, activate beads, choose tasks, or code. |

### Planning Prompts

| Prompt | Use | Source | Boundary |
|---|---|---|---|
| [Skill Playbook Ergonomics](../tasks/reference/PROMPT-PATTERNS.md#skill-playbook-ergonomics) | a beginner or host agent is unsure whether to ask for Ask Precode, Workflow Selection, Ideation, Review, Skill / Extension Review, or no skill style surface at all. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Role Lens Prompt Map](../tasks/reference/PROMPT-PATTERNS.md#role-lens-prompt-map) | Route to Must not decide Product manager / product strategist The idea, user, non goal, first slice, or requirement shape is unclear. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Agent Access Level Check](../tasks/reference/PROMPT-PATTERNS.md#agent-access-level-check) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Every-Bead Rhythm](../tasks/reference/PROMPT-PATTERNS.md#every-bead-rhythm) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Check Task Suitability Before Work](../tasks/reference/PROMPT-PATTERNS.md#check-task-suitability-before-work) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Plan Mode Candidate Craft Loop](../tasks/reference/PROMPT-PATTERNS.md#plan-mode-candidate-craft-loop) | an idea, feature angle, or selected candidate needs staged planning before any active work begins. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Workflow Selection Skill](../tasks/reference/PROMPT-PATTERNS.md#workflow-selection-skill) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Candidate Queue Review](../tasks/reference/PROMPT-PATTERNS.md#candidate-queue-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Add Candidate Queue Entry](../tasks/reference/PROMPT-PATTERNS.md#add-candidate-queue-entry) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Candidate Queue Shaping Proposal](../tasks/reference/PROMPT-PATTERNS.md#candidate-queue-shaping-proposal) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Candidate Queue Import Preview](../tasks/reference/PROMPT-PATTERNS.md#candidate-queue-import-preview) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [PRD Shaping](../tasks/reference/PROMPT-PATTERNS.md#prd-shaping) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Destination PRD Review](../tasks/reference/PROMPT-PATTERNS.md#destination-prd-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [PRD Handoff Readiness Packet](../tasks/reference/PROMPT-PATTERNS.md#prd-handoff-readiness-packet) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Requirements Gap And Conflict Review](../tasks/reference/PROMPT-PATTERNS.md#requirements-gap-and-conflict-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Bugfix Spec Lane](../tasks/reference/PROMPT-PATTERNS.md#bugfix-spec-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Bead Decomposition](../tasks/reference/PROMPT-PATTERNS.md#bead-decomposition) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Vertical-Slice Decomposition](../tasks/reference/PROMPT-PATTERNS.md#vertical-slice-decomposition) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [AFK-Candidate Review](../tasks/reference/PROMPT-PATTERNS.md#afk-candidate-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Architecture Shaping](../tasks/reference/PROMPT-PATTERNS.md#architecture-shaping) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [System Design Shape](../tasks/reference/PROMPT-PATTERNS.md#system-design-shape) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Pattern Fit](../tasks/reference/PROMPT-PATTERNS.md#pattern-fit) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Workflow Selection](../tasks/reference/PROMPT-PATTERNS.md#workflow-selection) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Plan Loop](../tasks/reference/PROMPT-PATTERNS.md#plan-loop) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Routing Check](../tasks/reference/PROMPT-PATTERNS.md#routing-check) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Context Budget Check](../tasks/reference/PROMPT-PATTERNS.md#context-budget-check) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Compact Or Handoff Context Pack](../tasks/reference/PROMPT-PATTERNS.md#compact-or-handoff-context-pack) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Goal Frame Proposal](../tasks/reference/PROMPT-PATTERNS.md#goal-frame-proposal) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Workbook Candidate Goal Frame](../tasks/reference/PROMPT-PATTERNS.md#workbook-candidate-goal-frame) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Goal Frame Reaffirmation](../tasks/reference/PROMPT-PATTERNS.md#goal-frame-reaffirmation) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Goal Frame Fit Check](../tasks/reference/PROMPT-PATTERNS.md#goal-frame-fit-check) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Goal Frame Boundaries](../tasks/reference/PROMPT-PATTERNS.md#goal-frame-boundaries) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Long-Horizon Review](../tasks/reference/PROMPT-PATTERNS.md#long-horizon-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |
| [Ready To Become A Bead](../tasks/reference/PROMPT-PATTERNS.md#ready-to-become-a-bead) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve PRDs, rank implementation priority, activate beads, or authorize build work. |

### Build Prompts

| Prompt | Use | Source | Boundary |
|---|---|---|---|
| [Source And Target Confirmation](../tasks/reference/PROMPT-PATTERNS.md#source-and-target-confirmation) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [One Question At A Time](../tasks/reference/PROMPT-PATTERNS.md#one-question-at-a-time) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Active Bead Before Editing](../tasks/reference/PROMPT-PATTERNS.md#active-bead-before-editing) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Git Hygiene Before New Work](../tasks/reference/PROMPT-PATTERNS.md#git-hygiene-before-new-work) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Repository Topology Migration](../tasks/reference/PROMPT-PATTERNS.md#repository-topology-migration) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Ask Precode](../tasks/reference/PROMPT-PATTERNS.md#ask-precode) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Small Team Collaboration Lane](../tasks/reference/PROMPT-PATTERNS.md#small-team-collaboration-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Small Team Collaboration Preview](../tasks/reference/PROMPT-PATTERNS.md#small-team-collaboration-preview) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Team Assignment Packet Prompts v2](../tasks/reference/PROMPT-PATTERNS.md#team-assignment-packet-prompts-v2) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Teammate Startup In A Team Lane](../tasks/reference/PROMPT-PATTERNS.md#teammate-startup-in-a-team-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Team Merge And Re-entry Review Pack](../tasks/reference/PROMPT-PATTERNS.md#team-merge-and-re-entry-review-pack) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Build Attribution Review](../tasks/reference/PROMPT-PATTERNS.md#build-attribution-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Build-React-Learn Exploratory Prototype Bead](../tasks/reference/PROMPT-PATTERNS.md#build-react-learn-exploratory-prototype-bead) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Session Start](../tasks/reference/PROMPT-PATTERNS.md#session-start) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Task Confirmation](../tasks/reference/PROMPT-PATTERNS.md#task-confirmation) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Engineering Quality Floor](../tasks/reference/PROMPT-PATTERNS.md#engineering-quality-floor) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Product Code Quality Snapshot](../tasks/reference/PROMPT-PATTERNS.md#engineering-quality-floor) | Use after code changed and a builder asks whether the AI wrote decent code for the active bead. | `PROMPT-PATTERNS.md` | Does not run lint/tests, certify code quality, accept work, approve release, create generated proof, or choose tasks. |
| [Vibe-To-Agentic Boundary](../tasks/reference/PROMPT-PATTERNS.md#vibe-to-agentic-boundary) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Engineer Initiation](../tasks/reference/PROMPT-PATTERNS.md#engineer-initiation) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Backend-Only With Existing Frontend](../tasks/reference/PROMPT-PATTERNS.md#backend-only-with-existing-frontend) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Bounded-AFK Re-Entry](../tasks/reference/PROMPT-PATTERNS.md#bounded-afk-re-entry) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Delegation Re-Entry Evidence Pack](../tasks/reference/PROMPT-PATTERNS.md#delegation-re-entry-evidence-pack) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Approved-Bead Handoff](../tasks/reference/PROMPT-PATTERNS.md#approved-bead-handoff) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Classify Tool Call](../tasks/reference/PROMPT-PATTERNS.md#classify-tool-call) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Record Tool Run](../tasks/reference/PROMPT-PATTERNS.md#record-tool-run) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Command Safety](../tasks/reference/PROMPT-PATTERNS.md#command-safety) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Local Hygiene Check](../tasks/reference/PROMPT-PATTERNS.md#local-hygiene-check) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Local Hygiene Dry Run](../tasks/reference/PROMPT-PATTERNS.md#local-hygiene-dry-run) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Implementation](../tasks/reference/PROMPT-PATTERNS.md#implementation) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Failing-First Implementation](../tasks/reference/PROMPT-PATTERNS.md#failing-first-implementation) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |
| [Checkpoint](../tasks/reference/PROMPT-PATTERNS.md#checkpoint) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not widen scope, approve commands, bypass files-in-play, accept work, or mutate external systems. |

### Review Prompts

| Prompt | Use | Source | Boundary |
|---|---|---|---|
| [Review / Acceptance Skill](../tasks/reference/PROMPT-PATTERNS.md#review-acceptance-skill) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Requirement-To-Proof Review](../tasks/reference/PROMPT-PATTERNS.md#requirement-to-proof-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Review Lanes](../tasks/reference/PROMPT-PATTERNS.md#review-lanes) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Multi-Lane Review Invocation](../tasks/reference/PROMPT-PATTERNS.md#multi-lane-review-invocation) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Dependency Graph Review Lane](../tasks/reference/PROMPT-PATTERNS.md#dependency-graph-review-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [PRD Quality Review Lane](../tasks/reference/PROMPT-PATTERNS.md#prd-quality-review-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Engineering Quality Review Lane](../tasks/reference/PROMPT-PATTERNS.md#engineering-quality-review-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Polish / Product-Taste Review Lane](../tasks/reference/PROMPT-PATTERNS.md#polish-product-taste-review-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Cross-Reference / Staleness Review Lane](../tasks/reference/PROMPT-PATTERNS.md#cross-reference-staleness-review-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Completion Check](../tasks/reference/PROMPT-PATTERNS.md#completion-check) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Make Acceptance Criteria Testable](../tasks/reference/PROMPT-PATTERNS.md#make-acceptance-criteria-testable) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Review Acceptance Criteria For Vague Behavior](../tasks/reference/PROMPT-PATTERNS.md#review-acceptance-criteria-for-vague-behavior) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Review](../tasks/reference/PROMPT-PATTERNS.md#review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Review Lane](../tasks/reference/PROMPT-PATTERNS.md#review-lane) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Release Candidate Evidence Profile](../tasks/reference/PROMPT-PATTERNS.md#release-candidate-evidence-profile) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Release Readiness Skill](../tasks/reference/PROMPT-PATTERNS.md#release-readiness-skill) | release-relevant work needs one read-only evidence and approval-question pass before a human release decision. | `PROMPT-PATTERNS.md` | Does not approve release, deploy, mutate GitHub or providers, create proof, or become a command wrapper. |
| [Release Readiness Curated Pack Exemplar](../tasks/templates/RELEASE-READINESS-CURATED-PACK-EXEMPLAR.md) | a maintainer or contributor needs the official non-installable exemplar for pack-shaped extension review. | `EXTENSION-PROTOCOL.md` | Does not install packs or skills, create a registry, approve release, wrap commands, or add package-manager behavior. |
| [Verification And Release Evidence Review](../tasks/reference/PROMPT-PATTERNS.md#verification-and-release-evidence-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Release Candidate Review](../tasks/reference/PROMPT-PATTERNS.md#release-candidate-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Fresh-Context Comprehension Review](../tasks/reference/PROMPT-PATTERNS.md#fresh-context-comprehension-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Fresh-Context Review](../tasks/reference/PROMPT-PATTERNS.md#fresh-context-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Stale Artifact Handling](../tasks/reference/PROMPT-PATTERNS.md#stale-artifact-handling) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Manual Verification](../tasks/reference/PROMPT-PATTERNS.md#manual-verification) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Learning Diary Review](../tasks/reference/PROMPT-PATTERNS.md#learning-diary-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |
| [Reviewed Memory](../tasks/reference/PROMPT-PATTERNS.md#reviewed-memory) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not accept implementation, approve release, activate transitions, create proof, or certify quality. |

### Recovery Prompts

| Prompt | Use | Source | Boundary |
|---|---|---|---|
| [Existing Repo Intake](../tasks/reference/PROMPT-PATTERNS.md#existing-repo-intake) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Supervised Setup Plan](../tasks/reference/PROMPT-PATTERNS.md#supervised-setup-plan) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Supervised Setup Apply](../tasks/reference/PROMPT-PATTERNS.md#supervised-setup-apply) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Existing Project Adaptation Plan](../tasks/reference/PROMPT-PATTERNS.md#existing-project-adaptation-plan) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Existing Precode Refresh](../tasks/reference/PROMPT-PATTERNS.md#existing-precode-refresh) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Package Upgrade Preview](../tasks/reference/PROMPT-PATTERNS.md#package-upgrade-preview) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Package Upgrade Apply](../tasks/reference/PROMPT-PATTERNS.md#package-upgrade-apply) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Bootstrap Recovery Guidance](../tasks/reference/PROMPT-PATTERNS.md#bootstrap-recovery-guidance) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Evidence Is Not Authority](../tasks/reference/PROMPT-PATTERNS.md#evidence-is-not-authority) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Precode Skill Playbook](../tasks/reference/PROMPT-PATTERNS.md#precode-skill-playbook) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Triage GitHub Feedback Or Package Bug](../tasks/reference/PROMPT-PATTERNS.md#triage-github-feedback-or-package-bug) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Session Friction Review](../tasks/reference/PROMPT-PATTERNS.md#session-friction-review) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Local Opt-In Usage Evidence Review](../tasks/reference/PROMPT-PATTERNS.md#local-opt-in-usage-evidence-review) | Use when local usage-learning evidence is explicitly requested. | `PROMPT-PATTERNS.md` | Does not collect telemetry, submit evidence, prove adoption, choose roadmap work, approve PRDs, activate beads, or accept implementation. |
| [Maintainer Package Review Skill](../tasks/reference/PROMPT-PATTERNS.md#maintainer-package-review-skill) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Skill / Extension Review Skill](../tasks/reference/PROMPT-PATTERNS.md#skill-extension-review-skill) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Stop Before Precode Control-Layer Edits](../tasks/reference/PROMPT-PATTERNS.md#stop-before-precode-control-layer-edits) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Close The Session](../tasks/reference/PROMPT-PATTERNS.md#close-the-session) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Implemented Bead Reversal](../tasks/reference/PROMPT-PATTERNS.md#implemented-bead-reversal) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Handoff Packet](../tasks/reference/PROMPT-PATTERNS.md#handoff-packet) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Transition Readiness](../tasks/reference/PROMPT-PATTERNS.md#transition-readiness) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Intent Changed](../tasks/reference/PROMPT-PATTERNS.md#intent-changed) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [State Repair](../tasks/reference/PROMPT-PATTERNS.md#state-repair) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Stuck Recovery](../tasks/reference/PROMPT-PATTERNS.md#stuck-recovery) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Agent Is Lost](../tasks/reference/PROMPT-PATTERNS.md#agent-is-lost) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Checks Failed](../tasks/reference/PROMPT-PATTERNS.md#checks-failed) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [App Will Not Start](../tasks/reference/PROMPT-PATTERNS.md#app-will-not-start) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Approved Too Much](../tasks/reference/PROMPT-PATTERNS.md#approved-too-much) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Copied Wrong Files](../tasks/reference/PROMPT-PATTERNS.md#copied-wrong-files) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Decide Whether To Stop](../tasks/reference/PROMPT-PATTERNS.md#decide-whether-to-stop) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |
| [Handoff](../tasks/reference/PROMPT-PATTERNS.md#handoff) | Use when this workflow moment applies. | `PROMPT-PATTERNS.md` | Does not approve repair, overwrite, rollback, setup mutation, transition, or destructive action. |

## Full Protocol Catalog

This catalog covers every `../tasks/reference/*PROTOCOL.md` owner protocol. Load the smallest protocol whose trigger applies; do not load every protocol by default. Protocol rows do not approve work, choose tasks, activate beads, accept review, approve transition, approve release, approve commands, mutate external systems, or replace owner files.

### Discovery Protocols

| Protocol | Load when | Source | Boundary |
|---|---|---|---|
| [PrecodeOS -- Client Engagement Intake Protocol](../tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md) | A client arrives with an existing project, external PRD, frontend design files, external handoff agent artifacts, backend plans, sprint plans, or an existing codebase that must be adapted into PrecodeOS. | `CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` | Use only when discovery/intake/learning applies; it does not promote facts or approve work. |
| [PrecodeOS -- Hypothesis Review / Learning Loop Protocol](../tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md) | A user asks whether a Discovery Summary, Candidate Queue entry, Local Source Intake summary, PRD Source Inputs section, Product Brief, Conviction Packet, or Planning Brief hypothesis was tested, learned from, narrowed, killed, promoted, left untested, stale, or ready for the next Precode workflow. | `HYPOTHESIS-REVIEW-PROTOCOL.md` | Use only when discovery/intake/learning applies; it does not promote facts or approve work. |
| [PrecodeOS -- Learning Diary Protocol](../tasks/reference/LEARNING-DIARY-PROTOCOL.md) | Creating, reviewing, or changing learner-facing session diary behavior. | `LEARNING-DIARY-PROTOCOL.md` | Use only when discovery/intake/learning applies; it does not promote facts or approve work. |
| [PrecodeOS -- Local Source Intake Protocol](../tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md) | Turning local notes, docs, screenshots, chat summaries, issue exports, research files, diagrams, manual drafts, client handoff artifacts, or existing codebases into PRD-ready source summaries. | `LOCAL-SOURCE-INTAKE-PROTOCOL.md` | Use only when discovery/intake/learning applies; it does not promote facts or approve work. |
| [PrecodeOS -- Filesystem Memory Protocol](../tasks/reference/MEMORY-PROTOCOL.md) | Creating, reviewing, searching, exporting, or changing Precode reviewed memory behavior. | `MEMORY-PROTOCOL.md` | Use only when discovery/intake/learning applies; it does not promote facts or approve work. |
| [PrecodeOS -- Product Discovery Validation Protocol](../tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md) | A product idea is broad, risky, market-facing, paid, evidence-poor, solution-first, or likely to become a PRD before the user problem, current alternatives, assumptions, and smallest learning step are clear. | `PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` | Use only when discovery/intake/learning applies; it does not promote facts or approve work. |
| [PrecodeOS -- Ubiquitous Language Protocol](../tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md) | A feature, PRD, bead, review, source intake, or memory card depends on domain vocabulary, confusing terms, user language, module/interface names, or stale terminology. | `UBIQUITOUS-LANGUAGE-PROTOCOL.md` | Use only when discovery/intake/learning applies; it does not promote facts or approve work. |

### Planning Protocols

| Protocol | Load when | Source | Boundary |
|---|---|---|---|
| [PrecodeOS -- Architecture Shaping Protocol](../tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md) | An approved PRD touches auth, data models, APIs, integrations, dependencies, migrations, external services, multi-step workflows, multi-system changes, or another implementation risk that should be visible before bead proposals. | `ARCHITECTURE-SHAPING-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS -- Candidate Queue Protocol](../tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md) | Capturing parked ideas, reviewing backlog-like requests, ranking candidates for review, deciding whether intent needs research, routing candidates to intake/discovery/PRD/decomposition, or checking candidate bead visibility. | `CANDIDATE-QUEUE-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS -- Decomposition Protocol](../tasks/reference/DECOMPOSITION-PROTOCOL.md) | Turning PRDs, source intake, GitHub issues, rough plans, or review findings into candidate beads; splitting broad work; or reviewing whether a bead is small enough to activate. | `DECOMPOSITION-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS -- Goal Frame Protocol](../tasks/reference/GOAL-FRAME-PROTOCOL.md) | A user wants to persist a durable goal, workflow arc, north-star outcome, or broad intent without creating active work or when `next-step.py` reports Goal Frame warnings. | `GOAL-FRAME-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS -- Intent Orchestration Protocol](../tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md) | Capturing rough intent, promoting source material into PRDs or decisions, changing direction mid-task, reviewing PRD-to-bead traceability, or auditing whether work is ready to proceed. | `INTENT-ORCHESTRATION-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS -- Long-Horizon Planning Protocol](../tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md) | Reviewing future work, deferred ideas, blocked beads, follow-up candidates, PRD-approved but unscheduled work, dependency chains, or long-range planning health. | `LONG-HORIZON-PLANNING-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS — Planning Protocol](../tasks/reference/PLANNING-PROTOCOL.md) | Planning a product experiment, rollout, ambiguous feature bet, or user-facing behavior change whose success needs measurement. | `PLANNING-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [Precode PRD Protocol](../tasks/reference/PRD-PROTOCOL.md) | Turning a product idea into an approved PRD shard, compiling requirements into `FEATURES.md`, or deriving beads from product definition. | `PRD-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS -- Semantic Change Proposal Protocol](../tasks/reference/SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md) | Proposing or reviewing a PrecodeOS package change that may alter active memory, authority ownership, generated-output demotion, package install/update boundaries, governance or contribution semantics, or beginner-facing safety language. | `SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS -- System Design Pattern Protocol](../tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md) | A feature may need architecture shape, external integration boundaries, state flows, interchangeable rules, audit trails, auth/access boundaries, or a plain-English explanation of whether a design pattern is warranted. | `SYSTEM-DESIGN-PATTERN-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |
| [PrecodeOS -- Workflow Selection Protocol](../tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md) | Deciding which Precode workflow to use for a rough idea, local source material, PRD work, bead proposal, blocked task, review, closeout, or state repair. | `WORKFLOW-SELECTION-PROTOCOL.md` | Use only when planning applies; it does not choose active work, approve PRDs, or activate beads. |

### Build Protocols

| Protocol | Load when | Source | Boundary |
|---|---|---|---|
| [PrecodeOS -- Agent Routing Protocol](../tasks/reference/AGENT-ROUTING-PROTOCOL.md) | Choosing an AI coding agent model, reasoning effort, subagent/delegation path, context compaction or handoff point, or tool path for a PrecodeOS task. | `AGENT-ROUTING-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Bead Build Journal Protocol](../tasks/reference/BEAD-BUILD-JOURNAL-PROTOCOL.md) | Creating, reviewing, or changing the generated bead build journal, bead-level build snapshot, code-change report, or related Daily Cockpit status surface. | `BEAD-BUILD-JOURNAL-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Context Engineering Protocol](../tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md) | Starting or handing off a session, writing prompts, reviewing context drift, importing local or external sources, switching agents, or deciding which files an agent should load. | `CONTEXT-ENGINEERING-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Extension Protocol](../tasks/reference/EXTENSION-PROTOCOL.md) | Adding or reviewing a Precode adapter, protocol, skill playbook, importer, audit, generated report, bead template, or external integration. | `EXTENSION-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- External Status Integration Protocol](../tasks/reference/EXTERNAL-STATUS-INTEGRATION-PROTOCOL.md) | Adding, reviewing, configuring, or interpreting read-only external status checks for GitHub, CI, deployment, uptime, monitoring, dependency advisories, issue trackers, or dashboards. | `EXTERNAL-STATUS-INTEGRATION-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- GitHub Integration Protocol](../tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md) | Configuring GitHub, reviewing GitHub audit findings, importing GitHub issues or pull requests as source evidence, or adding GitHub Actions validation for PrecodeOS. | `GITHUB-INTEGRATION-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Local Hygiene Protocol](../tasks/reference/LOCAL-HYGIENE-PROTOCOL.md) | Reviewing local clutter, cache/build outputs, bulky generated logs, unexpected files under `logs/`, protected generated evidence, cleanup candidates, or dry-run cleanup previews. | `LOCAL-HYGIENE-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Ralph Loop Protocol](../tasks/reference/RALPH-LOOP-PROTOCOL.md) | Enabling, running, reviewing, or changing Ralph-style bounded retry loops for one active Precode bead. | `RALPH-LOOP-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Skill Playbook Protocol](../tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md) | Designing, reviewing, invoking, or comparing Precode skill-style prompt playbooks for host agents, beginner workflows, maintainer package review, or extension review. | `SKILL-PLAYBOOK-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Small Team Collaboration Lane](../tasks/reference/TEAM-COLLABORATION-PROTOCOL.md) | A builder says a small team is working on the same product build, asks for Small Team Collaboration Lane, wants 2-5 people to coordinate Precode work, or needs branch/worktree-isolated parallel bead guidance. | `TEAM-COLLABORATION-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Tool Execution Protocol](../tasks/reference/TOOL-EXECUTION-PROTOCOL.md) | Choosing, recording, reviewing, or approving tool calls; adding tool integrations; handling command failures; or distinguishing tool use from verification evidence. | `TOOL-EXECUTION-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |
| [PrecodeOS -- Versioning Protocol](../tasks/reference/VERSIONING-PROTOCOL.md) | Adding, changing, reviewing, or auditing PrecodeOS-owned files that should carry visible version metadata. | `VERSIONING-PROTOCOL.md` | Use only when scoped execution or tool behavior applies; it does not approve commands or widen scope. |

### Review Protocols

| Protocol | Load when | Source | Boundary |
|---|---|---|---|
| [PrecodeOS -- Engineering Quality Standards Protocol](../tasks/reference/ENGINEERING-QUALITY-STANDARDS-PROTOCOL.md) | A user asks what engineering quality standard or standards taxonomy applies before coding, an active bead is about to move into implementation, or a simple implementation request may hide architecture, security, data, dependency, deployment, or multi-system risk. | `ENGINEERING-QUALITY-STANDARDS-PROTOCOL.md` | Use only when proof/review/release evidence applies; it does not accept work or approve release. |
| [PrecodeOS -- Release Readiness Protocol](../tasks/reference/RELEASE-READINESS-PROTOCOL.md) | A completed or nearly completed bead may affect users, production, deployment, external services, documentation needed for use, or post-release support. | `RELEASE-READINESS-PROTOCOL.md` | Use only when proof/review/release evidence applies; it does not accept work or approve release. |
| [PrecodeOS -- Review Lanes Protocol](../tasks/reference/REVIEW-LANES-PROTOCOL.md) | A user asks for a Security Review Lane, Release / Docs Freshness Review Lane, Dependency Graph Review Lane, Engineering Quality Review Lane, Polish / Product-Taste Review Lane, PRD Quality Review Lane, Cross-Reference / Staleness Review Lane, Multi-Lane Review Invocation, or Review Lanes review for one active bead, one draft PRD, or one bounded package documentation/reference surface. | `REVIEW-LANES-PROTOCOL.md` | Use only when proof/review/release evidence applies; it does not accept work or approve release. |
| [PrecodeOS -- Session Completion And Handoff Protocol](../tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md) | Closing a session, checking whether a bead is ready for review, preparing an agent handoff, reviewing completion evidence, or deciding whether a transition proposal is safe to approve. | `SESSION-COMPLETION-HANDOFF-PROTOCOL.md` | Use only when proof/review/release evidence applies; it does not accept work or approve release. |
| [PrecodeOS -- Verification And Guardrail Protocol](../tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md) | Creating, reviewing, or closing beads; choosing checks; working near sensitive surfaces; or evaluating whether evidence is strong enough to accept work. | `VERIFICATION-GUARDRAIL-PROTOCOL.md` | Use only when proof/review/release evidence applies; it does not accept work or approve release. |

### Recovery Protocols

| Protocol | Load when | Source | Boundary |
|---|---|---|---|
| [PrecodeOS -- Bootstrap Closeout Protocol](../tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md) | A user, support engineer, maintainer, or agent needs the final P0 bootstrap lane behavior after Bootstrap Confidence, Existing Repo Intake, manifest preview, supervised setup plan, and supervised setup apply. | `BOOTSTRAP-CLOSEOUT-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- Bootstrap Confidence Protocol](../tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md) | A user, support engineer, or agent is preparing to adopt PrecodeOS into a new or existing project and needs to verify source, target, copy groups, exclusions, conflicts, dependencies, and first safe next action before editing. | `BOOTSTRAP-CONFIDENCE-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- Existing Repo Intake Protocol](../tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md) | A user, support engineer, or agent is adopting PrecodeOS into a repository that already has app code, docs, CI, product history, or active work. | `EXISTING-REPO-INTAKE-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- Install/Update Manifest Protocol](../tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md) | A user, support engineer, or agent needs to preview what PrecodeOS would consider copying, adapting, preserving, excluding, blocking, or deferring after Bootstrap Confidence and before any supervised setup mutation. | `INSTALL-UPDATE-MANIFEST-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- OS Integrity Protocol](../tasks/reference/OS-INTEGRITY-PROTOCOL.md) | Changing PrecodeOS-owned operating files, reviewing protected-source edits, creating an OS checkpoint, restoring from a checkpoint, or diagnosing OS-integrity warnings. | `OS-INTEGRITY-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- Recovery Protocol](../tasks/reference/RECOVERY-PROTOCOL.md) | A user thinks Precode is broken, state is confusing, files were moved or renamed, generated reports were edited or stale, checks are missing, scope widened, approval happened too quickly, or an agent lost context. | `RECOVERY-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- Scheduled Audit Protocol](../tasks/reference/SCHEDULED-AUDIT-PROTOCOL.md) | Adding, reviewing, running, or configuring scheduled audits for PrecodeOS. | `SCHEDULED-AUDIT-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- State Management Protocol](../tasks/reference/STATE-MANAGEMENT-PROTOCOL.md) | Repairing state drift, reviewing state integrity, changing state schemas, investigating stale generated reports, or deciding which file owns a state fact. | `STATE-MANAGEMENT-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- Supervised Setup Apply Protocol](../tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md) | A user, support engineer, or agent has reviewed a supervised setup plan and needs to apply specific safe copy actions into an empty or nearly empty target. | `SUPERVISED-SETUP-APPLY-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |
| [PrecodeOS -- Supervised Setup Plan Protocol](../tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md) | A user, support engineer, or agent needs a setup checklist after Bootstrap Confidence and manifest preview but before any copying, owner-file adaptation, hook installation, CI change, app command, or app-code edit. | `SUPERVISED-SETUP-PLAN-PROTOCOL.md` | Use only when setup/state/recovery applies; it does not approve repair, update, rollback, or mutation. |

## Stop Signals

Stop the agent when:

- it cannot name the active bead, files in play, checks, or stop conditions
- it starts coding from a generated report, diary entry, source note, prompt catalog row, protocol catalog row, or old chat
- it touches files outside the active bead without explaining why
- it says work is done without recorded evidence or manual verification
- it wants to approve the next bead without explicit user approval
- it proposes deleting, overwriting, force-resetting, migrating, deploying, exposing secrets, or changing external services without exact approval
- it keeps asking implementation questions when the product problem, user, scope, or authority file is still unclear

Use this prompt:

```text
STOP. Do not make any more changes. Tell me exactly where we are: active bead, primary authority, files changed, evidence recorded, blockers, and the safest next action.
```

## Approval Gates

You must explicitly approve:

- PRD approval, bead activation, review acceptance, transition approval, release approval, merge approval, and manual verification claims
- `python3 scripts/bead-transition.py --approve`
- destructive commands, broad overwrites, deletes, moves, force resets, migrations, deploys, dashboard changes, secrets, billing, auth, payments, or private data actions
- setup or existing-Precode refresh apply actions
- edits to Precode control-layer files when the active bead does not include them
- memory-card writes or promotion of a lesson into `DECISIONS.md`, a PRD, protocol, approved bead, or another owner file
- external mutation, GitHub mutation, staging, committing, pushing, release, rollback, or package publishing

When in doubt, ask:

```text
Before continuing, show the allowed actions, proof needed, approval required before risky actions, stop conditions, and rollback or blocked escape path. Then run python3 scripts/run-contract-check.py.
```
