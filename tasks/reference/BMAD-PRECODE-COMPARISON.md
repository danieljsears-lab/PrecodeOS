# BMAD Method And Precode OS Comparison
<!-- ANCHOR: bmad-precode-comparison -->

> AUTHORITY: Research comparison between BMAD Method and Precode OS, with development guidance for future Precode OS work.
> NOT_AUTHORITY: Active task selection, target-project product requirements, current bead state, architectural decisions, schema definitions, or implementation status.
> LOAD_WHEN: Evaluating Precode OS direction, comparing AI-agent workflow systems, planning Precode OS packaging, or deciding what BMAD concepts to adopt or reject.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

Research date: 2026-04-25

This document compares BMAD Method with Precode OS and captures implications for future Precode OS development.

BMAD Method and Precode OS are solving the same broad problem: AI coding agents need structured context, staged work, and verification, or they drift. The systems differ most in where each puts its center of gravity.

BMAD is an installable agent-and-workflow product: named expert agents, guided skills, PRD and architecture workflows, story workflows, Quick Dev, testing modules, and an extensible module ecosystem.

Precode OS is a repo-native operating layer: tiny active memory, explicit authority contracts, one current bead, generated health and evidence, validators, and user-gated transitions.

Short judgment:

> BMAD is stronger as a "how do we create and run the software planning process?" framework. Precode OS is stronger as a "how do we keep one real repo trustworthy across many AI sessions?" control system.

---

## Sources

BMAD sources reviewed:

- BMAD docs home: https://docs.bmad-method.org/
- Getting Started: https://docs.bmad-method.org/tutorials/getting-started/
- Workflow Map: https://docs.bmad-method.org/reference/workflow-map/
- Agents: https://docs.bmad-method.org/reference/agents/
- Skills: https://docs.bmad-method.org/reference/commands/
- Core Tools: https://docs.bmad-method.org/reference/core-tools/
- Quick Dev: https://docs.bmad-method.org/explanation/quick-dev/
- Project Context: https://docs.bmad-method.org/explanation/project-context/
- Testing Options: https://docs.bmad-method.org/reference/testing/
- Official Modules: https://docs.bmad-method.org/reference/modules/
- BMAD GitHub repo: https://github.com/bmad-code-org/BMAD-METHOD
- BMAD Code site: https://www.bmadcode.com/
- PRFAQ article: https://www.bmadcode.com/blog/your-ai-should-be-arguing-with-you-and-making-you-sweat/
- AI-native article: https://www.bmadcode.com/blog/what-does-going-ai-native-mean/
- BMAD Method v6.2.1 changelog: https://www.bmadcode.com/bmad-method-v6-2-1-rebuilt-code-review-smarter-quick-dev-and-a-growing-global-community/
- BMAD Builder v1.5.0 changelog: https://www.bmadcode.com/bmad-builder-v1-5-0-agents-that-remember-evolve-and-wake-on-their-own/

Precode sources reviewed:

- `PRECODE-OS-README.md`
- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Important BMAD current-state note:

- BMAD GitHub listed `v6.4.0` as latest on 2026-04-25.
- BMAD docs describe V6, skills architecture, BMad Builder, and dev-loop automation as active directions.

---

## Core Identity

| Dimension | BMAD Method | Precode OS |
|---|---|---|
| Primary identity | AI-native development framework with agents, workflows, skills, and modules | Tiny-memory repo operating system for solo builders using AI coding agents |
| Main object | Workflow artifacts: PRD, architecture, epics, stories, sprint status, specs | Active-memory kernel, beads, authority files, validators, logs, readiness, OS health |
| User posture | "Guide me through a professional software lifecycle" | "Keep my agent scoped, grounded, and verifiable in this repo" |
| Packaging | Installed via `npx bmad-method install`; creates `_bmad/` and `_bmad-output/` | Lives inside the repo as markdown contracts, scripts, adapters, validators, and logs |
| Scaling story | Solo developer to enterprise teams; official modules for testing, game development, creative work, and builder tooling | Solo and non-technical builder first; can be forked project to project as a memory/control pattern |

BMAD's docs present it as a framework that helps build software from ideation through planning and implementation, using specialized agents and guided workflows. Its public repo and docs show a mature open-source ecosystem with installable modules.

Precode OS defines itself around "tiny memory" and repo control. It declares only three files as active memory: `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`. Everything else is loaded only when needed. That is stricter and more repo-governance-oriented than BMAD's broader artifact pipeline.

---

## Workflow Philosophy

BMAD uses a staged software-development lifecycle:

| BMAD phase | Purpose | Typical outputs |
|---|---|---|
| Analysis | Brainstorm, research, product brief, PRFAQ | Briefs, research, PRFAQ |
| Planning | Define what to build | PRD, UX spec |
| Solutioning | Define how to build | Architecture, ADRs, epics, stories |
| Implementation | Build story by story | Code, tests, review decisions, sprint status |

That maps closely to professional agile and product practice. BMAD also offers Quick Flow / Quick Dev for smaller work, where the system clarifies intent, chooses the smallest safe path, lets the model run longer, and routes review findings back to the correct layer.

Precode OS has a different loop:

| Precode stage | Purpose | Main artifact |
|---|---|---|
| Session start | Validate current state and load only the kernel | Active memory plus current bead |
| Bead execution | Work on one bounded logical unit | `tasks/beads/*.md` |
| Recorded checks | Turn claims into evidence | `logs/check-results.jsonl`, bead closeout |
| Session close | Refresh health, compile readiness, propose next work | `OS-HEALTH.md`, `logs/readiness.json` |
| User approval | Prevent automatic momentum | `bead-transition.py --approve` |

BMAD says: move through the right product/software workflow.

Precode says: keep one repo from lying to you while an agent works.

That difference matters. BMAD's process creates better plans. Precode's process creates stronger state discipline.

---

## Context Management

This is the deepest overlap between the systems.

BMAD's context strategy:

- Build context progressively.
- PRD informs architecture.
- Architecture informs epics and stories.
- Stories inform implementation.
- `project-context.md` acts like a project constitution for stack choices, conventions, and implementation rules.
- Fresh chats are recommended for each workflow to avoid context-limit issues.
- Document sharding is available, though current docs describe it as a fallback for tool/model combinations that struggle with large docs.

Precode's context strategy:

- Keep active memory tiny.
- Load only `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md` by default.
- Treat all other docs as reference files with narrow ownership.
- Use authority contracts to say what each file owns and does not own.
- Demote generated files so status reports cannot accidentally become instructions.
- Compile operational state into structured sidecars instead of trusting prose summaries.

| Context problem | BMAD answer | Precode answer |
|---|---|---|
| Agent needs product intent | Generate/load PRD, brief, PRFAQ, stories | Load current bead and primary authority only |
| Agent needs project conventions | `project-context.md` loaded by implementation workflows | `AGENT.md`, authority contracts, adapter rules, validators |
| Large docs | Optional sharding / workflow discovery | Reference files loaded only when bead requires them |
| Old/generated docs becoming authority | Output folders separate artifacts; less central emphasis | Explicit generated-output demotion rule |
| Too much context | Fresh chats per workflow, artifacts per phase | Tiny active-memory kernel enforced by validator |

BMAD is progressive-context engineering.

Precode is minimal-context governance.

Development implication for Precode OS:

- Keep the tiny-memory claim central. It is the clearest differentiator.
- Do not drift toward "BMAD but with different filenames."
- If adopting BMAD-like planning artifacts, route them through authority ownership and active-memory limits.
- Treat generated planning outputs as candidates until promoted into a Precode authority file or PRD shard.

---

## Agent Model

BMAD has named role agents:

- Analyst
- Product Manager
- Architect
- Developer
- UX Designer
- Technical Writer
- Additional module-specific agents

BMAD agents are invoked through skills and triggers such as:

- `bmad-help`
- `bmad-create-prd`
- `bmad-create-architecture`
- `bmad-create-epics-and-stories`
- `bmad-dev-story`
- `bmad-code-review`
- `bmad-quick-dev`
- `bmad-qa-generate-e2e-tests`

Precode has lighter modes:

- Navigator
- Builder
- Review

Precode also uses thin adapters for tool-specific surfaces such as Claude, Codex, Cursor, Gemini, and others. The point is not to simulate a full cross-functional team. The point is to keep any coding agent following the same repo contract.

| Dimension | BMAD | Precode |
|---|---|---|
| Agent roles | Rich named personas and workflows | Minimal role modes |
| Invocation | Skills, triggers, installer-generated commands | Repo scripts and active-memory instructions |
| Multi-agent support | Party Mode, specialized agents, module agents | Tool-neutral adapters and handoff scripts |
| Main risk handled | Agent lacks the right expert workflow | Agent loses repo truth, scope, or evidence |

BMAD feels like an AI product organization in a box.

Precode feels like a flight recorder plus operating manual for a real repo.

Development implication for Precode OS:

- Avoid over-investing in named personas unless they enforce a concrete repo invariant.
- Preserve the simple mode model.
- Add richer workflows as task/bead templates rather than permanent always-loaded agent identities.
- If "Precode Navigator" becomes public terminology, define it as a scope-shaping role, not a full PM persona.

---

## Planning And Product Definition

BMAD is stronger and broader upstream. It has explicit workflows for:

- Brainstorming
- Market research
- Domain research
- Technical research
- Product brief
- PRFAQ
- PRD
- UX design
- Architecture
- Epics and stories
- Implementation readiness

The BMAD PRFAQ article is especially revealing. BMAD's creator argues that AI should challenge assumptions, not simply generate polished artifacts. The PRFAQ process is described as adversarial: it pushes the user away from shallow solution-first thinking and toward customer pain, market reality, internal feasibility, and hard tradeoffs.

That philosophy is close to Precode, but BMAD applies it through guided agent workflows.

Precode added a Product Definition Gate and PRD shards, but its core concern is not ideation breadth. Its PRD system exists to prevent feature beads from starting without approved product definition and traceability. In the minimal Precode pattern, product-feature beads include approved PRD shards, compiled feature inventory, requirement IDs, and one primary authority file per task.

| Product planning capability | BMAD | Precode |
|---|---|---|
| Brainstorming | Strong, dedicated workflows | Not core |
| Market/domain/technical research | Built in | Possible as reference/planning beads, but not central |
| PRFAQ challenge | Built in and philosophically important | Compatible, not native core |
| PRD | Central workflow artifact | Gate/shard layer before beads |
| Architecture | Dedicated Architect workflow | Authority/reference doc owned by repo |
| Story/task breakdown | Epics and stories | Beads with primary authority and closeout evidence |

Development implication for Precode OS:

- Add optional Precode planning protocols only when they feed the bead system.
- Do not make Precode an all-purpose product ideation framework unless that is a deliberate product expansion.
- A strong near-term improvement would be a "Precode Product Definition Gate" that can ingest artifacts from BMAD, chat, notes, or manual drafts and normalize them into PRD shards plus requirement IDs.
- Consider a PRFAQ-compatible planning bead type, but keep it optional.

---

## Execution Discipline

BMAD's implementation cycle is story-based:

1. Create story.
2. Implement story.
3. Code review.
4. Generate tests after epic completion or through TEA.
5. Track sprint status.
6. Run retrospective.

Quick Dev compresses this for smaller work. It clarifies intent, routes to the smallest safe path, lets the model work longer with less supervision, then uses review to diagnose whether failures came from intent, spec, or implementation.

Precode's execution unit is the bead. A bead is more operationally strict than a BMAD story. It includes:

- Current-state metadata.
- One primary authority file.
- Files in play.
- Stop conditions.
- Checks to run.
- Closeout evidence.
- Manual verification.
- Review decision.
- Drift observed.
- Lessons to promote.
- Follow-up bead need.
- Blocked-bead escape path.
- Transition safety.

| Execution concern | BMAD | Precode |
|---|---|---|
| What to build next | Sprint/story workflows and `bmad-help` | `tasks/todo.md` current bead pointer |
| Scope control | Story/spec boundaries | One bead, one primary authority, files-in-play limits |
| Mid-course change | `bmad-correct-course` | Stop conditions, split/revise/blocked decisions |
| Completion | Code review / workflow completion | Recorded checks plus closeout plus manual review plus user approval |
| Next task | Workflow guidance | Proposed by script, activated only by user approval |

Precode is more pessimistic, in a useful way. It assumes momentum is dangerous unless gated.

Development implication for Precode OS:

- Beads are the core object. Keep improving bead ergonomics.
- Add templates for different bead types instead of weakening the bead contract.
- Preserve "one current bead" as a hard invariant.
- Add migration paths from BMAD stories or GitHub issues into bead format.
- Make closeout easier to read and harder to fake.

---

## Verification, Testing, And Review

BMAD has a substantial review/testing story:

- Built-in QA workflow detects frameworks.
- It generates API and E2E tests.
- It runs tests and fixes failures.
- TEA adds risk-based testing, quality gates, requirements traceability, ATDD, NFR testing, and enterprise-grade test strategy.
- BMAD v6.2.1 described layered code review: Blind Hunter, Edge Case Hunter, and Acceptance Auditor.

Precode's verification is less about generating tests and more about preserving evidence:

- `record-check.sh` records command text, exit code, branch, bead, duration, and output log path.
- `update-bead-closeout.py` normalizes closeout evidence.
- `os-health.py` compiles state into generated sidecars.
- Validators catch active-memory drift, missing authority blocks, wrong document classes, bead errors, feature-window drift, adapter command drift, route/API parity drift, schema/type convention drift, and authority collisions.

| Verification type | BMAD | Precode |
|---|---|---|
| Test generation | Strong built-in QA; TEA module for advanced strategy | Not a generator by default |
| Code review | Dedicated workflow, layered review system | Review mode plus closeout fields |
| Evidence logging | Less central in public docs | Central: check logs, health reports, readiness JSON |
| System validation | Skill validator exists for BMAD framework quality | Repo-specific doc/memory validator is core |
| Traceability | Stronger with TEA and planning artifacts | Strong in bead-to-PRD requirement IDs and closeout evidence |

BMAD asks: Did we build and test this well?

Precode asks: Can we prove what happened, what authority controlled it, and whether it is safe to proceed?

Development implication for Precode OS:

- Precode should not try to beat BMAD as a test generator first.
- Precode should make test generation pluggable as recorded evidence.
- A useful future bead field: `external_review_inputs`, where BMAD code review, TEA, Playwright screenshots, or human QA can be attached.
- Keep the distinction between "test was generated" and "recorded check passed."

---

## Human Control

BMAD tries to reduce user burden by using guided agents and `bmad-help`. It recommends fresh chats per workflow and has workflows that prompt the user at important moments. Quick Dev explicitly reduces human-in-the-loop turns by clarifying intent early, then letting the model run longer.

Precode intentionally keeps some gates manual. The user chooses product goals, approves sensitive changes, confirms external dashboard setup, reviews closeout evidence, decides whether work is accepted/revise/split/blocked, and approves the next bead transition.

This is not accidental friction. It is the safety model.

| Human role | BMAD | Precode |
|---|---|---|
| Main human value | Product judgment, workflow answers, reviews | Authority, approvals, external secrets, acceptance decisions |
| AI autonomy | Higher during guided workflows and Quick Dev | High inside a bead, low at transitions |
| Philosophy | Save human attention by structuring workflows | Preserve human control at state-changing gates |

For a non-technical solo builder, Precode's manual gates are especially protective. BMAD may be friendlier to start. Precode may be safer to live with over months.

Development implication for Precode OS:

- Keep manual approval for bead transitions.
- Make approval screens/proposals clearer rather than removing gates.
- Distinguish "agent can propose" from "agent can perform."
- Design for the tired solo builder who needs the system to say, "pause here."

---

## Extensibility And Ecosystem

BMAD wins on ecosystem:

- Open source.
- Installable.
- Module-based.
- Public docs.
- Active community.
- Translations.
- BMad Builder.
- TEA.
- Game Dev Studio.
- Creative Intelligence Suite.

Precode wins on forkability as operating model:

- It is not trying to be a marketplace of agents.
- It is a small, auditable repo discipline.
- It can be copied into a project and evolved.
- The explainer explicitly says not to copy everything first; copy the pattern: tiny memory, authority contracts, beads, checks, drift recovery.

| Extensibility | BMAD | Precode |
|---|---|---|
| Adding new roles | BMad Builder agents/workflows/modules | Add mode/adapters/scripts/bead templates |
| Community modules | Strong direction | Not currently the focus |
| Project specificity | Configured per project | Deeply embedded in repo |
| Tool portability | Supports AI IDEs via generated skills | Tool-neutral core plus thin adapters |

Development implication for Precode OS:

- Precode's public package should likely start as a template/scaffold, not a large plugin marketplace.
- The most valuable public offering may be `precode init`, `precode validate`, `precode checkpoint`, and `precode close`.
- A later ecosystem can grow around bead templates, validators, adapters, and planning gates.

---

## Shared Principles

The systems agree on several deep principles.

| Shared principle | BMAD expression | Precode expression |
|---|---|---|
| AI needs structure | Workflows, agents, artifacts | Active memory, authority files, beads |
| Planning matters | PRD, architecture, stories | Product Definition Gate, primary authority |
| Context must be engineered | Progressive phase artifacts, `project-context.md` | Tiny kernel, references on demand |
| Review should route correction | Quick Dev diagnoses intent/spec/code layer | Closeout/review decisions: accepted, revise, split, blocked |
| AI should not replace judgment | Agents guide and challenge | User approves transitions and sensitive changes |
| Process should be reusable | Installer and modules | Forkable OS pattern |

The philosophical overlap is real. BMAD's PRFAQ material argues against shallow artifact generation and for harder thinking before code. Precode makes a similar move operationally: it prevents agents from converting confidence into progress without evidence.

---

## Key Divergences

| Divergence | BMAD | Precode |
|---|---|---|
| Starting point | "Install this framework and run workflows" | "Create a tiny repo memory kernel" |
| Process style | Guided professional lifecycle | Repo governance and drift control |
| Artifact trust | Workflow outputs become inputs to next phase | Only owner files have authority; generated outputs are demoted |
| Agent abstraction | Named specialists | Tool-neutral agents constrained by repo contracts |
| Completion model | Workflow/story/review completion | Evidence, closeout, health, readiness, user-approved transition |
| Best user | Developer/team wanting an AI-native SDLC | Solo builder who needs guardrails stronger than memory |
| Failure it fears most | Underplanned or poorly reviewed AI development | Drift, stale context, false done, uncontrolled momentum |

---

## Strengths

BMAD strengths:

- Easier to adopt from scratch.
- Better upstream ideation, PRFAQ, PRD, architecture, UX, and story generation.
- Strong named-agent experience.
- Mature public ecosystem and installer.
- Stronger built-in testing generation and optional enterprise testing module.
- Better for teams that already understand agile and product roles.

Precode OS strengths:

- Stronger active-memory discipline.
- Better authority ownership and generated-output demotion.
- Stronger evidence trail for real repo work.
- Better protection for non-technical solo builders.
- More explicit stop conditions and manual approval gates.
- Tool-neutral by design; less dependent on one agent ecosystem.
- Stronger answer to "what is the actual current state?"

---

## Weaknesses

BMAD weaknesses:

- More process surface area to learn.
- Can produce many artifacts that may become stale unless actively governed.
- Public docs emphasize workflow progression more than hard repo-state invariants.
- Its agent/persona model may be overkill for a solo builder who mostly needs "do not drift."
- Generated/planning artifacts can create a false sense of rigor if not tied to actual repo evidence.

Precode OS weaknesses:

- Harder to adopt because it is a system of conventions, scripts, validators, and repo discipline.
- Less polished as a packaged product.
- Less upstream creative/product facilitation than BMAD.
- Validator/script layer can become intimidating if introduced too early.
- It relies on the builder accepting manual gates; users who want fast autonomous coding may feel slowed down.

---

## Best Use Cases

Use BMAD when:

- You are at idea, product, architecture, or story-definition stage.
- You want structured help creating PRDs, architecture, epics, stories, tests, or reviews.
- A team wants a common AI-native software lifecycle.
- You want installable tooling and community-supported modules.
- You need richer agent personas and guided workflows.

Use Precode OS when:

- You already have a repo that must stay coherent over many AI sessions.
- You are a solo or non-technical builder and need guardrails.
- You care deeply about evidence, current task state, and controlled transitions.
- You switch between tools like Codex, Claude, Cursor, Gemini, or others.
- You need generated status reports to inform, not instruct.

Use both when:

- BMAD creates or challenges upstream artifacts.
- Precode governs what becomes active work.
- BMAD stories are converted into Precode beads.
- Precode validators and recorded checks become the acceptance layer.
- BMAD QA or review workflows feed Precode closeout evidence.

---

## Recommended Hybrid

The clean hybrid:

1. Use BMAD Analysis, Planning, and Solutioning to generate or refine product brief, PRFAQ, PRD, architecture, UX, epics, and stories.
2. Import approved outputs into Precode as reference files, not active memory.
3. Compile BMAD stories into Precode beads with one primary authority file, requirement IDs, files in play, stop conditions, and checks.
4. Execute inside Precode's bead loop.
5. Optionally call BMAD QA or code review as recorded checks or review inputs.
6. Let Precode decide readiness and require user approval before the next bead starts.

This gives a builder BMAD's richer "thinking before building" and Precode's stronger "do not lose the thread while building."

---

## Concrete Precode OS Development Opportunities

### 1. BMAD Artifact Ingestion

Build a script or protocol that converts BMAD artifacts into Precode-owned docs.

Possible inputs:

- `_bmad-output/planning-artifacts/PRD.md`
- `_bmad-output/planning-artifacts/architecture.md`
- `_bmad-output/planning-artifacts/epics/`
- BMAD Quick Dev specs
- BMAD PRFAQ distillates

Possible outputs:

- `tasks/prds/*.md`
- `FEATURES.md`
- `tasks/beads/*.md`
- Requirement IDs
- Bead frontmatter
- Primary authority pointers

Important rule:

> BMAD artifacts should not become active memory by default. They should be imported, normalized, and assigned authority.

### 2. Precode Product Definition Gate

Strengthen the existing Product Definition Gate as a generic public capability.

It should answer:

- Has this feature been defined enough to become beads?
- Which PRD shard owns it?
- Which requirements are traceable?
- Which decisions are unresolved?
- Which risks require manual approval?
- What is the smallest first bead?

This is where Precode can absorb BMAD's planning strength without becoming BMAD.

### 3. PRFAQ-Compatible Planning Bead

Add an optional bead type for idea hardening:

- Problem
- Customer
- Press release claim
- Customer FAQ
- Internal FAQ
- Kill criteria
- Decision: proceed / revise / reject
- Distillate for PRD shard

This should remain optional and upstream of implementation.

### 4. External Review Evidence Field

Add or standardize bead closeout fields for external review artifacts.

Examples:

- BMAD code review result
- TEA quality gate
- Playwright screenshot path
- Browser verification result
- Human review note
- Security review note

The key distinction:

> External reviews can inform closeout, but Precode readiness should still depend on recorded evidence and explicit review decision.

### 5. Precode Public CLI Surface

If Precode becomes a public tool, start with a small CLI surface:

```bash
precode init
precode session-start
precode checkpoint
precode record-check -- <command>
precode close
precode validate
precode transition --approve
```

Avoid starting with a large agent marketplace.

The first product promise should be:

> Bring repo memory, scope control, evidence, and safe handoffs to any AI coding agent.

### 6. Easier Onboarding Tiers

BMAD is easier to try because `npx bmad-method install` gives users a clear start.

Precode should consider three setup tiers:

| Tier | Files/scripts | Audience |
|---|---|---|
| Kernel | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, one bead | First-time solo builder |
| Loop | Kernel plus session/checkpoint/close scripts | Builder actively using agents |
| Guarded | Loop plus validators, logs, health, transition model | Long-running repo |

This would preserve Precode's discipline without overwhelming new users.

### 7. Bead Template Library

Create templates rather than personas.

Useful templates:

- Feature implementation bead
- Scaffold/setup bead
- Bugfix bead
- Refactor bead
- Planning bead
- Experiment bead
- Rollout bead
- External integration bead
- Security-sensitive bead
- Manual-dashboard bead
- Blocked-unblocker bead

Each template should preserve:

- One primary authority.
- Files in play.
- Stop conditions.
- Checks.
- Closeout evidence.
- Manual verification.
- Review decision.

### 8. "Generated Is Not Authority" As Public Differentiator

This is one of Precode's strongest ideas.

BMAD and other systems generate useful artifacts. Precode should loudly clarify:

- Generated summaries are reports, not instructions.
- Generated health is evidence, not task selection.
- Generated progress points back to active memory.
- Generated planning becomes authority only after promotion.

This is a clean public contrast with artifact-heavy AI workflows.

### 9. Cross-Tool Handoff As Product Surface

BMAD is strong inside its installed ecosystem. Precode can be strong across tools.

Precode should make this easy:

```bash
precode handoff claude
precode handoff codex
precode handoff cursor
```

The handoff should print:

- Current branch.
- Current bead.
- Done-when.
- Primary authority.
- Files in play.
- Last recorded checks.
- Blockers.
- Manual gates.
- Next safe action.

### 10. Readiness Model As Core IP

Precode's readiness model is more distinctive than its markdown files.

Readiness should answer:

- Can a session start safely?
- Can this bead close?
- Can the next bead be proposed?
- Can the next bead be activated?
- Are generated files trying to become authority?
- Is there more than one active bead?
- Is there closeout evidence?
- Is manual verification clear?
- Is the review decision accepted?

This should remain deterministic and inspectable.

---

## Positioning Statement

Possible public positioning:

> BMAD helps AI agents plan and build through a professional software lifecycle. Precode OS keeps any AI coding agent grounded in a real repo by enforcing tiny memory, authority ownership, recorded evidence, and human-approved task transitions.

Alternative:

> BMAD is an AI-native SDLC framework. Precode OS is a repo-native control layer for AI coding sessions.

Sharper:

> BMAD gives your agent a team. Precode gives your repo a memory and a brake pedal.

Use the last line carefully. It is memorable, but the public product language should probably stay more precise.

---

## Strategic Recommendation

Do not compete with BMAD head-on as an end-to-end AI SDLC framework.

Compete on the layer BMAD does not primarily own:

- active-memory minimalism
- authority ownership
- generated-output demotion
- deterministic readiness
- recorded evidence
- cross-tool handoff
- solo-builder safety
- user-approved transitions
- drift recovery

Precode OS should be able to consume BMAD output, Cursor chats, Codex plans, Claude sessions, GitHub issues, Linear tickets, or hand-written notes. Its job is to normalize that input into a repo-owned execution contract.

The central product line:

> Precode OS is the trust layer between AI planning and code changes.

---

## Bottom Line

BMAD Method is a strong AI-native SDLC framework. It gives users roles, workflows, planning tracks, guided artifacts, review, testing, and extensibility.

Precode OS is a stronger repo-control system. It gives users tiny active memory, authority ownership, one current bead, evidence logs, generated health, validators, stop conditions, learning promotion, and manual transition gates.

If BMAD is the AI project team, Precode OS is the operating discipline that keeps the project team honest once the work hits a real repository.
