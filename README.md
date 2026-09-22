# PrecodeOS
<!-- ANCHOR: readme -->

> AUTHORITY: Public GitHub landing page, public positioning, beginner orientation, quickstart, and curated navigation for PrecodeOS.
> NOT_AUTHORITY: Active project state, task selection, product approval, implementation status, generated evidence, or package-release authority.
> CLASS: reference

[![Precode Validate](https://github.com/danieljsears-lab/PrecodeOS/actions/workflows/precode-validate.yml/badge.svg)](https://github.com/danieljsears-lab/PrecodeOS/actions/workflows/precode-validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

## Build With AI Without Losing The Plot

AI coding agents make the first mile of software creation dramatically easier: more people can describe an idea and see prototype software appear. It's fast and easy, but not durable. The second mile to production-grade is a lot harder. That is where intent, scope, proof, maintainability, and recovery begin to drift.

PrecodeOS is an anti-drift operating system for AI-assisted agentic building. It encodes a practical set of proven product, software engineering, quality, collaboration, and agent-operating patterns into one opinionated, repo-native system.

Precode keeps intent, scope, decisions, evidence, approval, and recovery visible while people and AI agents turn ideas into working software. It is designed as an explicit bridge between nontechnical and semitechnical builders and professional software engineering patterns and practices.

PrecodeOS describes **how a builder and agent move from uncertain intent to bounded, evidenced, recoverable software work**.

The promise is human agency and dependable building. Accessibility, maintainability, and unification follow from that operating model.

## Why It Exists

Code generation is becoming cheap and fast. Human judgment, verification, direction, and reliable recovery are becoming the scarce controls. The hardest problem in AI-assisted building is whether the project can remain understandable, bounded, provable, and recoverable as the agent moves quickly.

Without an operating model like Precode:

- intent gets lost in chat conversations;
- scope expands through momentum and invisible model-made "additions";
- stale context competes with current decisions;
- a confident LLM answer gets mistaken for evidence;
- a prototype quietly becomes a system; and
- the builder loses the ability to stop or recover.

Precode gives the project a durable structure for moving from an idea to a reviewed, maintainable slice of software without handing ownership to the agent.

## What PrecodeOS Is

PrecodeOS is a repo-native control layer around the coding agent that supports the builder and the project. Important project truth lives in readable files inside the repository. Structured workflows and small scripts help the agent and builder understand:

- what the project is trying to achieve;
- what is active now;
- what the agent may change;
- what evidence is needed;
- what requires human approval; and
- how to recover when the work becomes unclear.

“OS” describes the operating layer around AI-assisted software work. PrecodeOS is not a replacement operating system, an application runtime, or an autonomous agent.

Precode encodes proven engineering practice into reusable structures and workflows so those practices are available when they matter, including builders with strong ideas, domain knowledge, and motivation who have not previously had technical leverage. It does not remove the need for technical judgment, testing, security review, deployment expertise, or operational responsibility.

## The Core Precode Flow

PrecodeOS’s user journey is a guided loop between human intent, agent execution, evidence, review, and the next safe move:

```text
Understand → Shape → Decide → Bound → Build → Prove → Review → Continue
                                      ↑                         │
                                      └──── Recover ────────────┘
```

The flow is human-directed. It does not assume that every idea should become code, that every planned item should be implemented, or that every completed build should continue to the next one.

1. **Understand** — Start from current project truth, the problem, the user, and what is already known. Load the smallest relevant context and identify uncertainty.
2. **Shape** — Turn a rough idea or request into clearer intent, assumptions, language, evidence, and a smallest useful outcome. A rough idea is not yet a requirement.
3. **Decide** — Decide whether to explore, research, amend product direction, shape architecture, or move toward implementation. A PRD defines an intended destination; it is not yet permission to code.
4. **Bound** — Turn approved intent into one bead: a bounded execution contract with an outcome, authority, files in play, checks, stop conditions, and required proof. A bead is not just a task.
5. **Build** — Let the agent work inside that boundary using the context, prompts, tools, and technical depth appropriate to the risk.
6. **Prove** — Check what changed, perform required verification, record evidence, and identify what remains uncertain. Building is not completion, and agent confidence is not proof.
7. **Review** — A human reviews the result against the intended outcome, scope, evidence, and risks before accepting it or deciding what happens next. Review is part of the work, not an optional afterthought.
8. **Continue or recover** — Close the work, preserve learning, hand off, split, block, or choose the next safe move. If state, scope, proof, or direction becomes unclear, recover to the appropriate earlier stage. Recovery and continuation are part of the method, not exceptions.

The flow is supported by five layers of Precode’s **capability architecture**. The capability architecture describes what Precode provides; the core flow describes how a builder and agent use those capabilities over the life of a piece of work.

## Precode’s Capability Architecture

The five layers below describe Precode’s **capability architecture**. They are distinct from the Core Precode Flow, which describes the builder’s user journey.

```text
Shape the work
        ↓
Prepare the context
        ↓
Govern execution
        ↓
Establish trust
        ↓
Sustain, recover, or continue
```

### 1. Shape The Work

**Plain English:** Decide what is worth building before implementation outruns intent.

Precode supports discovery, hypotheses, shared language, product briefs, PRDs, acceptance criteria, and risk-sensitive architecture shaping. It helps separate a rough idea, a learning question, an approved product direction, and an executable slice.

### 2. Prepare The Context

**Plain English:** Give the agent the right information without asking it to remember everything.

Precode uses repo-native context, tiny active memory, named owner files, source intake, workflow routing, and proven prompt patterns. Durable facts have a home. The current session loads only the context it needs.

### 3. Govern Execution

**Plain English:** Let the agent move quickly inside a boundary the builder can understand.

An approved bead is one bounded unit of work with scope, owner files, files in play, checks, stop conditions, and closeout evidence. A work graph preserves relationships among intent, decisions, dependencies, work, proof, blockers, and follow-up. Adaptive depth adds more planning and review when risk warrants it; bounded loops keep iteration stoppable.

### 4. Establish Trust

**Plain English:** Replace “the agent says it is done” with observable evidence and human review.

Precode connects implementation to recorded checks, manual verification, review decisions, acceptance, and explicit approval at meaningful transitions. Generated reports can summarize state, but they do not become authority or approve work by themselves.

### 5. Sustain The Project

**Plain English:** Keep the project understandable after the current session ends.

Handoff, collaboration, recovery, state repair, release-readiness preparation, tool-neutral adapters, and extension boundaries help the project continue across people, sessions, branches, and coding agents.

## The Engineering Patterns Precode Brings Together

Precode turns mature product and engineering practices into lightweight repo-native capabilities and habits that a builder and agent can use together:

| Pattern | What it means in Precode |
|---|---|
| Product engineering | Clarify users, outcomes, assumptions, evidence, and the smallest valuable slice. |
| Software engineering | Shape architecture, data, APIs, security, acceptance, and maintainability when risk warrants it. |
| Prompt engineering | Improve the instruction and govern what that instruction may cause through context, scope, proof, and approval. |
| Context engineering | Give the agent the right repo-owned information without asking it to remember everything. |
| Harness engineering | Use protocols, scripts, adapters, and checks to shape what the agent can inspect, propose, verify, and report. |
| Loop engineering      | Turn approved intent into a bounded execution contract (a bead), then structure iteration as build, check, review, and recovery. |
| Work graph engineering   | Preserve relationships among intent, decisions, dependencies, beads, checks, and follow-up. |
| Quality engineering | Tie completion claims to checks, verification, review, and known uncertainty. |
| Collaboration and compound engineering | Make ownership, handoffs, re-entry, reusable learning, and cross-tool continuity visible. |
| Safety and control engineering | Keep authority explicit and preserve human approval at consequential transitions. |

These structures make professional practices easier to use. They do not make expertise unnecessary.

## Relationship To The Engineering Lenses

The Core Precode Flow is where the engineering lenses become practical:

| Flow stage | Engineering lenses most visible |
|---|---|
| Understand | Context engineering and product engineering |
| Shape | Product engineering, prompt engineering, language, and discovery |
| Decide | Product engineering, software engineering, risk, and evidence |
| Bound | Harness engineering, beads, work graphs, and scope control |
| Build | Prompt, context, harness, and loop engineering |
| Prove | Quality engineering, verification, and evidence |
| Review | Human control, software engineering, and collaboration |
| Continue or recover | Compound engineering, recovery, handoff, and work graphs |

These lenses are not separate products or academic prerequisites. Precode incorporates their useful practices into one repo-native operating model so the builder does not need to master each discipline before using it.

## How Precode Compares

Precode complements several approaches builders may already know:

| Approach | What it provides | What Precode adds or integrates |
|---|---|---|
| Vibe coding | Fast, conversational exploration | A path from exploration to durable, bounded, reviewable work. |
| Coding agents | Code generation, editing, and iteration | Project context, authority, scope, proof, approval, and recovery. |
| Traditional SDLC | Mature planning, quality, and delivery practices | A lighter, repo-native form adapted to AI speed and individual builders. |
| Project management | Work visibility, assignment, and prioritization | Product-to-code traceability, execution contracts, evidence, and recovery. |
| Prompt engineering | Better instructions and model outputs | A governed context and workflow around the prompt. |
| Agent frameworks | Agent coordination, tools, and automation | Human-owned product judgment, durable project authority, and bounded execution. |

PrecodeOS is the repo-owned control layer around whatever agent you run, not another competing agent.

## What It Makes Possible

| Dimension | Builder outcome |
|---|---|
| Intent | Important decisions survive beyond the conversation that produced them. |
| Context | The agent can work from current, inspectable project truth. |
| Language | Builder language, product language, and implementation language stay aligned. |
| Work graph | Dependencies, evidence, blockers, and follow-up remain visible. |
| Execution | Work happens in one bounded, reviewable slice at a time. |
| Iteration | The agent can try, check, stop, and recover without open-ended drift. |
| Proof | Completion is connected to evidence rather than confidence alone. |
| Control | The builder remains the owner of intent, risk, approval, and acceptance. |
| Recovery | Confusion becomes a route to inspection and repair instead of more guessing. |
| Portability | The operating model persists across sessions, collaborators, and coding agents. |

## Who It Is For

PrecodeOS is for:

- nontechnical builders who want to use AI coding tools without becoming an approval machine for work they cannot understand;
- semi-technical builders who want professional structure without adopting a heavyweight process;
- technical builders who want traceability, bounded execution, evidence, and recovery across sessions and tools; and
- reviewers and collaborators who need to see what was intended, what changed, what was proven, and what remains uncertain.

For a throwaway sketch where mistakes are cheap and nothing needs to survive, the full model may be unnecessary. Use more structure when the work is durable, user-facing, sensitive, multi-file, ambiguous, release-relevant, hard to prove, or likely to be revisited.

## Try PrecodeOS

The npm entry is the shortest setup route. From the project you want to use:

```bash
npx @precodeos/precodeos fast-setup-preview --target <target-project-root>
```

The preview shows what setup proposes before changes are applied. Review the result, then follow [Guided Setup](docs/PRECODE-GUIDED-SETUP.md) for the complete installation, validation, and orientation route.

## Where To Go Next

| Need | Open |
|---|---|
| Install or recover setup | [Guided Setup](docs/PRECODE-GUIDED-SETUP.md) |
| Begin daily work | [Daily Cockpit](docs/PRECODE-DAILY-COCKPIT.md) |
| Understand the operating model | [PrecodeOS Explainer](docs/PRECODE-OS-README.md) |
| Learn the software-building workflow | [How To Build Software With Precode](docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md) |
| Diagnose a confusing state | [Troubleshooting](docs/PRECODE-TROUBLESHOOTING.md) |

## License And Provenance

PrecodeOS is open source under the Apache License 2.0. See [LICENSE](LICENSE), [NOTICE](NOTICE), and [TRADEMARK.md](TRADEMARK.md).

Created by Dan Sears / Recode. Canonical site: <https://www.precodeos.org>.

PrecodeOS™ and Precode™ are trademarks of Dan Sears / Recode. All trademark and brand rights are reserved. See [TRADEMARK.md](TRADEMARK.md) for brand-use guidance.

## Document Metadata

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.3.0
Last updated: 2026-09-17
