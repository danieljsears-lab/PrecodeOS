# PrecodeOS, BMAD Method, And gStack Comparison
<!-- ANCHOR: precode-bmad-gstack-comparison -->

> AUTHORITY: Research comparison between PrecodeOS, BMAD Method, and gStack, including strategic implications for PrecodeOS.
> NOT_AUTHORITY: Active task selection, product requirements, implementation status, route structure, schema definitions, roadmap prioritization, roadmap candidate ownership, or committed roadmap decisions.
> LOAD_WHEN: Evaluating PrecodeOS positioning, comparing AI-agent workflow systems, or researching ideas from BMAD Method or gStack.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.2.9
Last updated: 2026-05-13

Research date: 2026-05-04
Precode implementation refresh: 2026-05-12

## Executive Summary

PrecodeOS, BMAD Method, and gStack all respond to the same broad reality: AI coding agents can now move fast enough that ordinary human supervision, ad hoc prompts, and chat memory are not enough. The three systems choose different control points, but Precode starts from a more specific user: the non-technical solo builder who needs guided workflow, translation, scope control, and proof without first becoming a product manager or software engineer.

| System | Short identity | Core answer |
|---|---|---|
| PrecodeOS | Repo-native guidance, control, and evidence layer for non-technical solo builders | Make the repo know what is active, authoritative, proven, safe to continue, and understandable to the builder. |
| BMAD Method | AI-driven agile development method and module ecosystem | Guide the builder through a staged software lifecycle with agents, workflows, and progressive context. |
| gStack | Opinionated AI software factory for high-throughput builders | Turn Claude Code and other agents into a virtual product, engineering, design, QA, security, and release team. |

The cleanest positioning is:

> BMAD is the method. gStack is the sprint cockpit. Precode is the repo-native control layer.

Precode should not simply copy either one. Its strongest differentiator is still tiny active memory, explicit authority ownership, one current execution unit, recorded evidence, advisory next-step guidance, file-scope guardrails, and human-gated transitions, all shaped for a builder who may not know the usual product, engineering, QA, architecture, or release vocabulary yet.

The May 2026 shape is broader than the first kernel comparison: Precode now has Product Discovery Validation, Goal Frames, Run Contracts, recovery/operator safety guidance, reviewed memory promotion paths, local hygiene, and public package/install-readiness boundaries. That does not make Precode BMAD-lite or gStack-lite. The better frame is that Precode is becoming a repo-native boundary-control system. It may touch discovery, planning, execution, review, release, recovery, memory, and local upkeep only where authority, scope, evidence, approval, or human decision clarity can drift.

The main product risk is not missing another professional workflow. The main risk is hiding too much user-facing complexity inside safeguards meant to help beginners. Every added Precode surface should make one of a small set of human decisions clearer: proceed, pause, prove, approve, split, repair, or stop.

## Strategic Positioning

For users, the clearest market map is:

| User need | Best fit |
|---|---|
| "I need a full AI-native agile method from idea to implementation." | BMAD |
| "I want my coding agent to plan, review, QA, and ship like a specialist team." | gStack |
| "I am a non-technical solo builder and need my repo to preserve truth, scope, evidence, handoff, and next-step clarity across agents." | Precode |

For Precode's strategic posture, the core discipline should be:

> Borrow workflows, not memory bloat. Borrow specialists, not persona sprawl. Borrow automation, not uncontrolled momentum.

Precode wins if it remains the trusted control layer underneath fast AI workflows, especially for builders who need software-development concepts translated into guided decisions they can confidently approve.

## One-Line Contrast

| System | Best one-line description |
|---|---|
| PrecodeOS | A repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift for non-technical solo builders. |
| BMAD Method | A structured agile AI-development lifecycle with generated skills, named agents, workflows, and modules. |
| gStack | A production-speed skill stack that makes an AI coding agent behave like a startup product team. |

## Core Spine

### PrecodeOS Spine

```text
tiny active memory
  -> authority-owned reference docs
  -> beginner-readable workflow translation
  -> product discovery validation when worth-building is uncertain
  -> reviewed Goal Frame when durable intent needs orientation
  -> product definition gate
  -> adaptive bead depth
  -> one active bead
  -> files-in-play guardrail
  -> risk-triggered Run Contract when allowed actions need clarity
  -> recorded checks
  -> generated next-step guidance
  -> recovery / state repair when drift appears
  -> closeout evidence
  -> review decision
  -> human-approved transition
```

The spine is repo governance plus beginner-safe orchestration. Precode asks: "Can this repo preserve intent, scope, evidence, handoff state, and the next safe action across agents and sessions, while helping a non-technical solo builder understand what to ask, approve, verify, and stop?"

Key structural claims:

- Active memory is exactly `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
- Every durable fact needs one owning file.
- Generated reports are evidence, not authority.
- Beginner-facing docs and generated help translate software-development concepts into plain workflow decisions.
- Discovery output is evidence only; it can recommend proceed, pause, narrow, or kill, but it cannot approve PRDs or activate work.
- Goal Frames orient workflow selection only after review and reaffirmation; they do not become backlog, roadmap, or task authority.
- Work happens through one active bead.
- New or amended beads can declare complexity, required planning depth, and autonomy level.
- Changed files can be compared against the active bead's files in play.
- Sensitive, external, destructive, or bounded-AFK work can require a Run Contract that names allowed actions, proof needed, approval required before, and stop conditions.
- Checks become durable evidence through scripts.
- Generated next-step help can orient the human and reduce process confusion, but it cannot choose work or approve transitions.
- Recovery and state repair restore owner-file clarity rather than continuing from stale generated reports.
- The next bead does not activate without human approval.

### BMAD Method Spine

```text
analysis
  -> planning
  -> solutioning
  -> implementation
  -> review / correction / retrospective
```

The spine is staged software development. BMAD asks: "What is the right expert workflow and artifact chain for this kind of work?"

BMAD's workflow map describes four phases:

- Analysis: brainstorming, research, product brief, PRFAQ.
- Planning: PRD and UX spec.
- Solutioning: architecture, ADRs, epics, stories, readiness gate.
- Implementation: sprint planning, story creation, development, code review, correction, sprint status, retrospective.

BMAD also offers a Quick Flow through `bmad-quick-dev` for small or well-understood work. That flow compresses intent, routes to the smallest safe path, lets the model run longer, and uses review to decide whether the failure was in intent, spec, or implementation.

### gStack Spine

```text
think
  -> plan
  -> build
  -> review
  -> test
  -> ship
  -> reflect
```

The spine is a sprint cockpit. gStack asks: "Which specialist should push this work forward or challenge it next?"

The README explicitly presents gStack as a process, not merely a tool collection. Its skills feed one another:

- `/office-hours` reframes the product and writes a design doc.
- planning reviews challenge product, engineering, design, and developer experience.
- implementation is followed by `/review`, `/qa`, `/ship`, deployment, canary, benchmarking, release documentation, and retro.
- `/learn`, GBrain, domain skills, checkpoint commits, and context restore make learnings accumulate.

## Active Dimensions

### 1. Primary Control Surface

| System | Control surface | What the user touches |
|---|---|---|
| PrecodeOS | Repo files, plain-English generated guidance, and scripts | Markdown authority files, Product Discovery summaries, Goal Frames, bead files, Run Contracts when risk rises, advisory checks, closeout evidence, beginner-facing prompts. |
| BMAD Method | Generated skills and lifecycle artifacts | `bmad-*` skills, named agents, PRD, architecture, stories, sprint status. |
| gStack | Slash commands and workflow skills | `/office-hours`, `/autoplan`, `/review`, `/qa`, `/ship`, `/learn`, browser and release tools. |

Precode makes the repository itself the control plane, with generated next-step help as a non-authoritative human dashboard for a solo builder who needs to know what the workflow means. Its newer surfaces are best understood as boundary controls, not as a broader command stack: Product Discovery controls the pre-PRD boundary, Goal Frames control durable intent, Run Contracts control risky execution, and recovery protocols control state drift. BMAD makes the lifecycle workflow the control plane. gStack makes the command stack the control plane.

### 2. Memory And Context Model

| System | Context philosophy | Strength | Risk |
|---|---|---|---|
| PrecodeOS | Minimal context, explicit authority, conditional loading, reviewed memory evidence, generated next-step hints. | Low drift, inspectable state, strong handoff, clearer "what now?" guidance for non-technical builders. | Goal Frames, memory cards, and generated hints must remain demoted so they do not become task authority. |
| BMAD Method | Progressive context through artifacts. | Strong planning continuity and phase-to-phase inheritance. | Artifact chain can grow large or become process-heavy if not bounded. |
| gStack | Skill-generated docs, project learnings, browser/domain memory, optional GBrain. | Practical compounding memory and high reuse across sessions. | Memory can become another implicit authority layer unless governed. |

Precode's stance is the strictest: active memory stays tiny, reference docs load only when relevant, and generated reports are evidence rather than working memory. This strictness is not just a technical preference; it lowers the cognitive load for non-technical solo builders who cannot audit a sprawling hidden context stack. BMAD and gStack both add more procedural memory. Precode can learn from their affordances, but should route any durable learning through authority ownership, reviewed memory cards, Goal Frames in owner files, or generated evidence that remains demoted.

### 3. Planning Model

| System | Planning model | Typical output |
|---|---|---|
| PrecodeOS | Product Discovery when worth-building is uncertain, product fit, alignment/grilling, shared language, Goal Frame orientation, PRD shard, bead proposals, adaptive bead depth. | Discovery Summary, beginner-readable PRD shard, requirement IDs, active bead, complexity/planning/autonomy metadata. |
| BMAD Method | Analysis, PRD, UX, architecture, epics, stories, readiness gate. | Product brief, PRFAQ, PRD, architecture, epics, stories. |
| gStack | Product interrogation and specialist plan reviews. | Design doc, CEO review, engineering plan, design review, DX review. |

BMAD is the broadest upstream planning system. gStack is the most opinionated and founder/product-taste-driven. Precode is narrower: planning exists to prevent upstream intent drift and help a non-technical builder turn plain intent into verifiable beads without needing formal PM vocabulary. Product Discovery is core anti-drift work because building the wrong thing is one of the earliest ways authority can harden around a false target. It remains advisory: `proceed` means ready for the next planning workflow, not approved to build.

### 4. Execution Unit

| System | Main execution unit | Boundary style |
|---|---|---|
| PrecodeOS | Bead | One logical unit with files in play, authority, checks, stop conditions, adaptive depth, evidence, review decision, and a Run Contract when risk rises. |
| BMAD Method | Story | Agile story generated from PRD/architecture/epic context and implemented by the developer agent. |
| gStack | Skill run / sprint step / PR | Command-mediated work flowing through review, QA, and ship. |

The Precode bead is more governance-heavy than a BMAD story and more durable than an individual gStack command. It is designed to survive handoff and auditing, not just to guide implementation. The adaptive-depth fields make that governance more proportional instead of uniformly heavy. Run Contracts should stay even narrower: they are risk-triggered bead clauses for allowed actions, proof needed, approval required before, and stop if. They are not a general runtime permission system.

### 5. Agent And Role Model

| System | Role model | Active roles |
|---|---|---|
| PrecodeOS | Lightweight modes | Navigator, Builder, Review. |
| BMAD Method | Named expert agents | Analyst, PM, Architect, Developer, UX Designer, Technical Writer, module-specific agents. |
| gStack | Startup specialist team | CEO, engineering manager, designer, staff reviewer, QA lead, security officer, release engineer, SRE, DX lead, technical writer, performance engineer, memory manager. |

Precode intentionally avoids simulating a full organization. Its user should not have to act like a product manager, engineering manager, architect, QA lead, security reviewer, and release engineer just to operate the system. BMAD and gStack both prove there is user value in role-specific workflows, especially when the role produces a bounded artifact or review. The useful Precode question is not "Which personas should we add?" but "Which missing review or planning boundary deserves a plain-English bead template, mode, prompt, or check?"

### 6. Review And Quality Model

| System | Review posture | Notable mechanics |
|---|---|---|
| PrecodeOS | Evidence over confidence. | Recorded checks, closeout evidence, manual verification, review decision, verification tiers, next-step/adaptive-depth/files-in-play/run-contract advisory warnings. |
| BMAD Method | Adversarial and phase-aware review. | Implementation readiness, code review, correction, fresh-context review, false-positive awareness. |
| gStack | Specialist audits and live verification. | `/review`, `/qa`, `/qa-only`, `/cso`, `/benchmark`, `/canary`, `/codex`, `/design-review`, `/devex-review`. |

BMAD's strongest review idea is routing failure back to the layer where it entered: intent, spec, or implementation. gStack's strongest review idea is broad specialist coverage plus live browser verification. Precode's strongest review idea is durable recorded evidence tied to one active unit, with advisory warnings that make next action, bead depth, file-scope drift, execution-policy gaps, and proof gaps visible before a non-technical builder accepts work.

### 7. Automation And Autonomy

| System | Autonomy posture |
|---|---|
| PrecodeOS | Agents can propose and execute inside a bead; generated helpers can advise; humans approve sensitive transitions, risky actions, PRD approval, review acceptance, and bead activation. |
| BMAD Method | Adaptive depth and Quick Dev allow longer autonomous runs after intent/spec compression. |
| gStack | High automation across sprint steps, including review, QA fixes, ship, deploy, canary, docs, and retros. |

Precode is deliberately conservative because its target user may not be able to spot hidden technical drift until it becomes expensive. BMAD and gStack show a path to conditional autonomy: autonomy should increase only after intent is compressed, boundaries are explicit, tests/checks are known, review can classify failures without turning everything into a tangent, the bead's `autonomy_level` supports the risk, and any Run Contract has made allowed actions and proof expectations plain.

### 8. Packaging And Ecosystem

| System | Packaging |
|---|---|
| PrecodeOS | Repo-native Markdown, shell/Python scripts, adapters, generated logs, generated help, local hygiene checks, install/update guidance, Apache-2.0 license, `NOTICE`, and SPDX script provenance. |
| BMAD Method | `npx bmad-method install`, generated IDE skills, official modules, roadmap toward universal/adaptive skills and marketplace. |
| gStack | Git clone/setup into skill directories, team mode, host adapters, slash commands, browser tooling, standalone CLIs. |

BMAD is strongest as a packaged ecosystem. gStack is strongest as a practical daily-driver install. Precode is strongest as a repo-native control layer, and its open-source packaging should stay boring, explicit, and attribution-preserving: Apache-2.0 for adoption, `NOTICE` for provenance, SPDX headers for clarity, and no hidden "watermark" mechanics that make the project harder to trust. Users should be able to maintain a local Precode install, understand which reports are generated evidence, and receive or apply PrecodeOS updates without update artifacts becoming authority or silently changing active work.

### 9. Boundary-Control Cluster

The newer Precode surface is easiest to understand as a set of boundary controls rather than as a larger lifecycle suite.

| Boundary | Drift risk | Precode control | Scope limit |
|---|---|---|---|
| Intent admission | A weak idea becomes polished requirements too early. | Product Discovery Validation, Local Source Intake, Product Definition Gate, Goal Frames. | Discovery and Goal Frames are evidence or orientation only; they do not approve PRDs, activate beads, or choose work. |
| Execution policy | The agent touches risky systems, broad paths, or unclear actions. | Files in play, command-risk classification, sensitive-surface prompts, Run Contracts. | Run Contracts are risk-triggered bead clauses, not automatic command approval or a host permission system. |
| Proof and review | Confidence replaces evidence, or review finds problems without routing them. | Verification tiers, recorded checks, closeout evidence, manual verification, fresh-context review, future review lanes. | Review lanes should translate specialist concerns into acceptance questions, not make the builder manage a fake team. |
| Recovery and state repair | Stale generated output, damaged structure, or unclear state starts steering work. | State checks, Recovery Protocol, generated-output demotion, handoff guidance. | Repair restores owner-file clarity; generated reports do not become instructions. |
| Local upkeep and updates | Install drift, generated clutter, or update artifacts confuse the local Precode copy. | Local hygiene guidance, package/install-readiness checks, explicit update boundaries. | Local upkeep supports the user's install; it must not overwrite project authority or active work without review. |

This cluster is the strongest answer to the scope question. Precode can touch discovery, planning, execution, review, release, recovery, memory, and local upkeep only where a boundary decision needs to be made visible. If a new surface does not help the builder decide whether to proceed, pause, prove, approve, split, repair, or stop, it belongs outside the core.

## Where They Overlap

All three systems care about:

- stopping shallow "vibe" work from becoming production code;
- turning vague intent into explicit artifacts;
- giving the agent bounded context;
- making the next safe action legible;
- using review as more than rubber-stamping;
- preserving cross-session continuity;
- making AI development repeatable enough that a non-technical solo builder can trust it.

The overlap is real, but the center of gravity differs:

| Shared concern | Precode center | BMAD center | gStack center |
|---|---|---|---|
| Intent shaping | Product Discovery, Goal Frames, Product Definition Gate | Analysis/planning workflows | `/office-hours`, CEO/design/eng/DX reviews |
| Context | Tiny active memory, owner files, reviewed memory evidence | Progressive artifacts | Skill docs, learnings, GBrain/browser memory |
| Work breakdown | Beads | Epics/stories | Sprint commands and plans |
| Execution policy | Files in play, command guardrails, Run Contracts for risky work | Readiness and story context | Specialist commands, browser tools, release steps |
| Quality | Recorded evidence plus advisory depth/scope/proof warnings | Readiness/review/correct-course | Review, QA, security, browser, release gates |
| Recovery | Recovery Protocol, state repair, generated-output demotion | Correction workflows | Context restore, checkpoint commits, learnings |
| Handoff | Handoff packet and active bead | Phase artifacts | Checkpoint commits, context restore, learnings |

## Where They Differ Most

### Precode vs BMAD

BMAD is broader and more process-complete. It gives builders many paths from idea to implementation, backed by named agents and generated skills. Precode is narrower and stricter, even as it now touches more lifecycle boundaries. It does not try to own the entire software development lifecycle. It tries to keep a real repo's operating truth small, inspectable, enforceable, and legible to a builder who may not know lifecycle terminology yet.

BMAD asks the builder to trust a structured lifecycle. Precode asks the builder to trust the repo's authority and evidence model, while using beginner-facing docs and generated help to translate that model into "should I proceed, pause, prove, approve, split, repair, or stop?"

### Precode vs gStack

gStack is optimized for speed, taste, and production throughput. It gives the agent a rich command vocabulary for product challenge, design, review, QA, security, release, browser use, and learning. Precode is optimized for durability, governance, and non-technical control. It is comfortable slowing transitions down so the builder can see what changed, why it changed, what evidence proves it, and whether the next step is still inside the approved scope.

gStack asks the builder to run the right specialist next. Precode assumes the builder may not know which specialist to summon, so it asks whether the next action is still inside the approved bead, whether changed files match `files_in_play`, whether risky actions have a Run Contract, whether proof exists, and what human decision is required.

### BMAD vs gStack

BMAD is more lifecycle-methodical. gStack is more founder-operator and shipping-oriented. BMAD's default shape is "produce the right artifacts in the right order." gStack's default shape is "run the right specialist workflow to make the product better and ship it."

BMAD is closer to an AI-native agile framework. gStack is closer to an AI-native startup operating cadence.

## Roadmap Candidates For Precode From BMAD

### High-Fit Candidates

| Candidate | Why it fits Precode | Precode-shaped version |
|---|---|---|
| Product Discovery Validation | BMAD's analysis phase shows the value of validating the problem before planning hardens. Precode has added discovery as upstream anti-drift for broad, risky, paid, market-facing, evidence-poor, or solution-first ideas. | Keep discovery short, advisory, and beginner-safe: current workaround, strongest evidence, weakest assumption, smallest non-code learning step, and `proceed`, `pause`, `narrow`, or `kill` recommendation. |
| Adaptive planning depth | BMAD scales from bug fixes to enterprise systems. Precode now has `complexity`, `required_planning_depth`, `autonomy_level`, and `bead-depth-check.py`. | Harden the advisory classifier into beginner-readable defaults, examples, and migration guidance while keeping existing beads backward compatible. |
| Interactive help for "what next?" | BMAD's `bmad-help` lowers process confusion. Precode now has `scripts/next-step.py`, `logs/next-step.json`, and generated `PRECODE-HELP.md`. | Improve the generated next-step model so it distinguishes execute, closeout, review, unblocker, PRD shaping, state repair, and transition approval in language a solo builder can act on. |
| Implementation readiness gate | BMAD makes readiness explicit before coding. Precode has PRD gate and beads but can sharpen readiness as a visible decision. | Add a `readiness_decision` field to PRD or bead proposals: `pass`, `concerns`, `fail`, with plain-English reasons and unblockers. |
| Correct-course workflow | BMAD has a workflow for significant mid-sprint changes. Precode has checkpoint and blocked escape, but product drift recovery could be more explicit. | Add a `correct-course` protocol: classify change as bead-local, PRD amendment, decision log entry, defer note, or new bead, with beginner-facing "what this means" guidance. |
| Adversarial review pattern | BMAD's forced problem-finding can catch shallow acceptance. | Add optional fresh-context review guidance for high-risk beads, with false-positive filtering and "finding belongs to current bead?" triage that does not require the user to think like a QA lead. |
| Test Architect influence | BMAD TEA emphasizes risk-based testing, traceability, NFRs, and release gates. | Extend Precode verification protocol with risk tiers, requirement-to-test matrix, NFR checklist, and release gate evidence translated into approval questions. |
| Module ecosystem concept | BMAD modules let domains extend the core without bloating it. | Introduce "Precode packs" as optional reference/protocol/template bundles that never add active-memory files. |

### Medium-Fit Candidates

| Candidate | Value | Caution |
|---|---|---|
| Named agents/personas | Helps users ask for the right kind of thinking. | Could bloat Precode's simple Navigator/Builder/Review model. Prefer role lenses, bead templates, and copyable prompts that translate the role's job. |
| Party Mode / multi-agent discussion | Useful for ambiguous decisions. | Risk of noisy consensus theater. Keep it optional and bounded to planning/review beads. |
| Generated project context | Helpful for existing repos. | Must not become active memory or duplicate authority files. Route output into `PROJECT-CONTEXT.md` through review. |
| Universal/adaptive skills architecture | Strong packaging and cross-tool story. | Precode should keep tool-neutral contracts first, skill adapters second. |

### Low-Fit Or Reject For Now

| Candidate | Why to avoid |
|---|---|
| Full agile artifact hierarchy as core | Precode's differentiator is not making non-technical builders operate a PM framework. Epics/stories/sprints should remain optional bridges. |
| Always-on persona menus | Too much prompt surface for a tiny-memory OS. |
| Marketplace-first growth | Tempting, but premature before the kernel, installer, and reference contracts are stable. |

## Roadmap Candidates For Precode From gStack

### High-Fit Candidates

| Candidate | Why it fits Precode | Precode-shaped version |
|---|---|---|
| `/office-hours`-style forcing questions | Precode already has alignment/grilling; gStack's framing is concrete and founder-friendly. | Create a `PRECODE-OFFICE-HOURS` planning protocol that asks a small number of high-leverage plain-English questions before PRD/bead creation. |
| Review routing dashboard | gStack tracks which reviews are appropriate before shipping. Precode already has OS Health and readiness sidecars. | Add a review-readiness report that maps bead risk to required checks: code, design, QA, security, docs, release, with "why this matters" guidance for the builder. |
| Browser QA as first-class evidence | gStack treats real browser testing as a major unlock. | Add `manual_browser_evidence` and screenshot/log references to bead closeout schema for UI-facing beads, with beginner-safe prompts for what to inspect. |
| Specialist review lanes | gStack has design, DX, security, benchmark, canary, release, docs. | Add optional review lane templates that attach to beads without changing active memory: design, DX, security, performance, release, docs, each translated into user-facing acceptance questions. |
| Safety guardrails and edit freeze | gStack's `/careful`, `/freeze`, and `/guard` are immediately useful. Precode now has advisory files-in-play warnings, command-risk classification, sensitive-surface prompts, optional edit-lock guidance, and Run Contracts for risky beads. | Keep tuning these as beginner-facing stop signs, not as automatic permission, hidden enforcement, or a general runtime permission system. |
| Continuous local checkpointing | gStack's local WIP checkpoints plus context restore directly address crash/context loss. | Add optional Precode local checkpoints that record bead id, decisions, remaining work, failed approaches, and changed files without auto-pushing. |
| Release documentation freshness | gStack's `/document-release` attacks doc drift after shipping. | Add a doc-drift closeout check that compares changed surfaces against `README`, `ARCHITECTURE`, `API`, `DATA-MODELS`, `SECURITY`, and PRD/bead references. |
| Post-deploy canary and benchmark evidence | Precode can currently record commands, but release/runtime evidence is not a visible lane. | Add release bead templates with staging URL, deploy command, smoke tests, browser verification, canary checks, and rollback notes. |
| Local install upkeep and update ergonomics | gStack is strong as a daily-driver install; Precode needs users to maintain a local OS layer without confusing updates with current project truth. | Add explicit local update and hygiene guidance that explains generated reports, protected evidence, install drift, and update review before local Precode files change authority-bearing state. |

### Medium-Fit Candidates

| Candidate | Value | Caution |
|---|---|---|
| Taste memory | Useful for design-heavy products and non-technical solo builders. | Must remain reviewed memory/evidence, not implicit product authority. |
| GBrain-style persistent knowledge | Could improve retrieval across sessions. | Needs strict trust boundary and authority demotion; otherwise it competes with active memory. |
| Cross-model second opinion | Useful for high-risk reviews. | Should be a recorded check or review artifact, not a default dependency. |
| Domain/browser skills | Helpful for recurring external-site quirks. | Needs privacy and source classification; avoid leaking secrets or making browser quirks authoritative. |
| Autoplan | Strong convenience for multi-review planning. | Should produce candidate PRD/bead artifacts, not directly activate implementation. |

### Low-Fit Or Reject For Now

| Candidate | Why to avoid |
|---|---|
| "Ship like a team of twenty" as Precode's promise | Precode's promise is guided trust and control for non-technical solo builders, not maximal throughput. |
| Automatic doc edits across every project file | Precode should preserve one-owner-per-fact discipline. Auto-doc updates need review and authority routing. |
| Heavy browser stack as core dependency | Valuable as an adapter or optional pack, but too much for the kernel. |
| Persistent agent memory as primary context | Conflicts with tiny active memory unless carefully subordinated. |

## Synthesis: What Precode Should Become

Precode should remain the repo-native control plane that helps non-technical solo builders safely use workflow systems like BMAD and gStack without needing to absorb their full professional vocabulary or operating complexity.

After the May 2026 boundary-control update, Precode's control plane is no longer only passive evidence. It now has a small generated guidance loop plus explicit controls around intent admission, risky execution, state repair, and local upkeep: next-step help, Product Discovery Validation, Goal Frames, adaptive-depth warnings, files-in-play guardrails, optional command-risk classification, Run Contracts, recovery guidance, and advisory edit-lock/local-hygiene views. These are still advisory or owner-file-bound surfaces. They make the operating model easier for a beginner to operate without expanding active memory, granting automatic command approval, or turning generated reports into authority.

The important synthesis is not "Precode now has more metadata." The important synthesis is "Precode can translate repo state into a small number of human decisions: proceed, pause, prove, approve, split, repair, or stop."

The right synthesis is not:

```text
Precode = BMAD + gStack
```

The better synthesis is:

```text
Precode kernel
  -> boundary controls for intent, execution, proof, recovery, and local upkeep
  -> optional planning packs inspired by BMAD, translated for non-technical builders
  -> optional specialist review and release packs inspired by gStack, translated into acceptance questions
  -> all outputs routed through authority, beads, checks, evidence, and human gates
```

That preserves the core:

- tiny active memory;
- one owner per fact;
- one active bead;
- generated output demoted;
- discovery, Goal Frames, Run Contracts, generated next-step help, and update guidance are advisory or owner-file-bound only;
- evidence over confidence;
- human approval at transitions;
- tool-neutral adapters.

## Strategic Implications

The useful lesson from BMAD is lifecycle clarity: rough intent should pass through the right amount of discovery, analysis, planning, readiness, implementation, review, and correction before code becomes trusted. Precode should borrow that clarity without importing a full agile hierarchy into its core. Product Discovery belongs in Precode only because building the wrong thing is upstream intent drift; it must remain short, advisory, and subordinate to user judgment.

The useful lesson from gStack is practical review and shipping ergonomics: product challenge, browser QA, security/release checks, canary thinking, documentation freshness, and local workflow ergonomics all matter. Precode should translate those concerns into plain acceptance questions, optional lanes, and local install/update guidance without making the user manage a fake specialist organization.

The useful lesson from ZYAL-style host contracts is stricter runtime control: autonomous work becomes safer when allowed actions, evidence gates, approval gates, stop conditions, and rollback paths are declarative and inspectable. Precode should express that as risk-triggered Run Contracts inside beads, using plain language: allowed actions, proof needed, approval required before, and stop if. Run Contracts should not become automatic command approval, hidden enforcement, or a general runtime permission system.

The practical product implication is staged expansion: strengthen discovery, next-step clarity, adaptive depth, file/command guardrails, Run Contracts, and recovery before adding heavier review lanes, release evidence, install/update ergonomics, or optional packs. The comparison remains research context and strategic framing; it does not approve roadmap changes or activate work.

## Sources

Precode sources reviewed:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`
- `PRECODE-OS-README.md`
- `PRECODE-ARCHITECTURE-OVERVIEW.md`
- `PRECODE-USER-GUIDE.md`
- `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`
- `PRECODE-HELP.md`
- `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`
- `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`
- `tasks/reference/GOAL-FRAME-PROTOCOL.md`
- `tasks/reference/STATE-MANAGEMENT-PROTOCOL.md`
- `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
- `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
- `tasks/reference/PRECODE-BMAD-GSTACK-COMPARISON.md`
- `tasks/beads/BEAD-SCHEMA.md`
- `scripts/run-contract-check.py`
- `scripts/next-step.py`
- `scripts/bead-depth-check.py`
- `scripts/files-in-play-check.py`

BMAD sources reviewed:

- GitHub repo: <https://github.com/bmad-code-org/BMAD-METHOD>
- README: <https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md>
- Workflow Map: <https://docs.bmad-method.org/reference/workflow-map/>
- Agents: <https://docs.bmad-method.org/reference/agents/>
- Skills: <https://docs.bmad-method.org/reference/commands/>
- Official Modules: <https://docs.bmad-method.org/reference/modules/>
- Quick Dev: <https://docs.bmad-method.org/explanation/quick-dev/>
- Adversarial Review: <https://docs.bmad-method.org/explanation/adversarial-review/>
- Roadmap: <https://docs.bmad-method.org/roadmap/>

gStack sources reviewed:

- GitHub repo: <https://github.com/garrytan/gstack>
- README: <https://raw.githubusercontent.com/garrytan/gstack/main/README.md>
- CONTRIBUTING: <https://raw.githubusercontent.com/garrytan/gstack/main/CONTRIBUTING.md>

Current public-state notes from GitHub on 2026-05-04:

- BMAD GitHub page showed about 46.3k stars, 5.5k forks, and latest release `v6.6.0` dated 2026-04-29.
- gStack GitHub page showed about 89.1k stars, 13.1k forks, no formal GitHub releases, and a README describing 23 opinionated tools plus additional power tools.

Current Precode implementation notes on 2026-05-12:

- Theme 1 has landed as `scripts/next-step.py`, `logs/next-step.json`, and generated `PRECODE-HELP.md`.
- Theme 2 has landed as optional bead fields `complexity`, `required_planning_depth`, and `autonomy_level`, plus `scripts/bead-depth-check.py`.
- Theme 5 has landed as `scripts/files-in-play-check.py`, an advisory changed-path guardrail that allows generated Precode outputs and warns on out-of-scope paths when Git status is available.
- Product Discovery Validation has been added as an advisory pre-PRD path for broad, risky, market-facing, paid, evidence-poor, or solution-first ideas.
- Goal Frames have been added as reviewed durable orientation inside existing owner files, without becoming task selection or active memory.
- Run Contracts have been added as risk-triggered bead clauses for allowed actions, proof needed, approval gates, stop conditions, and rollback or blocked escape.
- Recovery, state repair, memory promotion, local hygiene, and package/install-readiness guidance have been sharpened around generated-output demotion and user-controlled local upkeep.
- The current hardening pass reframes these surfaces around plain user decisions: proceed, pause, prove, approve, split, repair, or stop.
