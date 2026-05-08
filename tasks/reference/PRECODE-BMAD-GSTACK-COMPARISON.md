# Precode OS, BMAD Method, And gStack Comparison
<!-- ANCHOR: precode-bmad-gstack-comparison -->

> AUTHORITY: Research comparison between Precode OS, BMAD Method, and gStack, including strategic implications and roadmap candidates for Precode OS.
> NOT_AUTHORITY: Active task selection, product requirements, implementation status, route structure, schema definitions, or committed roadmap decisions.
> LOAD_WHEN: Evaluating Precode OS positioning, comparing AI-agent workflow systems, or considering roadmap ideas from BMAD Method or gStack.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears
Document version: v0.2.5
Last updated: 2026-05-07

Research date: 2026-05-04
Precode implementation refresh: 2026-05-07

## Executive Summary

Precode OS, BMAD Method, and gStack all respond to the same broad reality: AI coding agents can now move fast enough that ordinary human supervision, ad hoc prompts, and chat memory are not enough. The three systems choose different control points, but Precode starts from a more specific user: the non-technical solo builder who needs guided workflow, translation, scope control, and proof without first becoming a product manager or software engineer.

| System | Short identity | Core answer |
|---|---|---|
| Precode OS | Repo-native guidance, control, and evidence layer for non-technical solo builders | Make the repo know what is active, authoritative, proven, safe to continue, and understandable to the builder. |
| BMAD Method | AI-driven agile development method and module ecosystem | Guide the builder through a staged software lifecycle with agents, workflows, and progressive context. |
| gStack | Opinionated AI software factory for high-throughput builders | Turn Claude Code and other agents into a virtual product, engineering, design, QA, security, and release team. |

The cleanest positioning is:

> BMAD is the method. gStack is the sprint cockpit. Precode is the repo-native control layer.

Precode should not simply copy either one. Its strongest differentiator is still tiny active memory, explicit authority ownership, one current execution unit, recorded evidence, advisory next-step guidance, file-scope guardrails, and human-gated transitions, all shaped for a builder who may not know the usual product, engineering, QA, architecture, or release vocabulary yet. The latest kernel update has already absorbed selected BMAD/gStack lessons: generated next-step help, adaptive bead depth, and files-in-play mutation warnings. The remaining roadmap opportunities are selective: deepen BMAD-style lifecycle clarity and import gStack-style specialist review, browser QA, release ergonomics, and safety lanes while preserving Precode's repo-owned authority model and beginner-safe translation layer.

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
- `tasks/reference/PRECODE-BMAD-GSTACK-COMPARISON.md`
- `tasks/beads/BEAD-SCHEMA.md`
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

Current Precode implementation notes on 2026-05-07:

- Theme 1 has landed as `scripts/next-step.py`, `logs/next-step.json`, and generated `PRECODE-HELP.md`.
- Theme 2 has landed as optional bead fields `complexity`, `required_planning_depth`, and `autonomy_level`, plus `scripts/bead-depth-check.py`.
- Theme 5 has landed as `scripts/files-in-play-check.py`, an advisory changed-path guardrail that allows generated Precode outputs and warns on out-of-scope paths when Git status is available.
- The current hardening pass reframes those three surfaces around plain user decisions: continue, ask for missing info, ask for proof, review, approve transition, repair state, approval needed, or stop.

## One-Line Contrast

| System | Best one-line description |
|---|---|
| Precode OS | A repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift for non-technical solo builders. |
| BMAD Method | A structured agile AI-development lifecycle with generated skills, named agents, workflows, and modules. |
| gStack | A production-speed skill stack that makes an AI coding agent behave like a startup product team. |

## Core Spine

### Precode OS Spine

```text
tiny active memory
  -> authority-owned reference docs
  -> beginner-readable workflow translation
  -> product definition gate
  -> adaptive bead depth
  -> one active bead
  -> files-in-play guardrail
  -> recorded checks
  -> generated next-step guidance
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
- Work happens through one active bead.
- New or amended beads can declare complexity, required planning depth, and autonomy level.
- Changed files can be compared against the active bead's files in play.
- Checks become durable evidence through scripts.
- Generated next-step help can orient the human and reduce process confusion, but it cannot choose work or approve transitions.
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
| Precode OS | Repo files, plain-English generated guidance, and scripts | Markdown authority files, bead files, `next-step.py`, advisory checks, closeout evidence, beginner-facing prompts. |
| BMAD Method | Generated skills and lifecycle artifacts | `bmad-*` skills, named agents, PRD, architecture, stories, sprint status. |
| gStack | Slash commands and workflow skills | `/office-hours`, `/autoplan`, `/review`, `/qa`, `/ship`, `/learn`, browser and release tools. |

Precode makes the repository itself the control plane, with generated next-step help as a non-authoritative human dashboard for a solo builder who needs to know what the workflow means. BMAD makes the lifecycle workflow the control plane. gStack makes the command stack the control plane.

### 2. Memory And Context Model

| System | Context philosophy | Strength | Risk |
|---|---|---|---|
| Precode OS | Minimal context, explicit authority, conditional loading, generated next-step hints. | Low drift, inspectable state, strong handoff, clearer "what now?" guidance for non-technical builders. | Generated hints must remain demoted so they do not become task authority. |
| BMAD Method | Progressive context through artifacts. | Strong planning continuity and phase-to-phase inheritance. | Artifact chain can grow large or become process-heavy if not bounded. |
| gStack | Skill-generated docs, project learnings, browser/domain memory, optional GBrain. | Practical compounding memory and high reuse across sessions. | Memory can become another implicit authority layer unless governed. |

Precode's stance is the strictest: active memory stays tiny, reference docs load only when relevant, and `PRECODE-HELP.md` is generated evidence rather than working memory. This strictness is not just a technical preference; it lowers the cognitive load for non-technical solo builders who cannot audit a sprawling hidden context stack. BMAD and gStack both add more procedural memory. Precode can learn from their affordances, but should route any durable learning through authority ownership, reviewed memory cards, or generated evidence that remains demoted.

### 3. Planning Model

| System | Planning model | Typical output |
|---|---|---|
| Precode OS | Product fit, alignment/grilling, shared language, PRD shard, bead proposals, adaptive bead depth. | Beginner-readable PRD shard, requirement IDs, active bead, complexity/planning/autonomy metadata. |
| BMAD Method | Analysis, PRD, UX, architecture, epics, stories, readiness gate. | Product brief, PRFAQ, PRD, architecture, epics, stories. |
| gStack | Product interrogation and specialist plan reviews. | Design doc, CEO review, engineering plan, design review, DX review. |

BMAD is the broadest upstream planning system. gStack is the most opinionated and founder/product-taste-driven. Precode is narrower: planning exists to help a non-technical builder turn plain intent into verifiable beads without needing formal PM vocabulary, now with advisory depth metadata so tiny fixes stay light while high-risk work gets stronger planning expectations.

### 4. Execution Unit

| System | Main execution unit | Boundary style |
|---|---|---|
| Precode OS | Bead | One logical unit with files in play, authority, checks, stop conditions, adaptive depth, evidence, and review decision. |
| BMAD Method | Story | Agile story generated from PRD/architecture/epic context and implemented by the developer agent. |
| gStack | Skill run / sprint step / PR | Command-mediated work flowing through review, QA, and ship. |

The Precode bead is more governance-heavy than a BMAD story and more durable than an individual gStack command. It is designed to survive handoff and auditing, not just to guide implementation. The new adaptive-depth fields make that governance more proportional instead of uniformly heavy.

### 5. Agent And Role Model

| System | Role model | Active roles |
|---|---|---|
| Precode OS | Lightweight modes | Navigator, Builder, Review. |
| BMAD Method | Named expert agents | Analyst, PM, Architect, Developer, UX Designer, Technical Writer, module-specific agents. |
| gStack | Startup specialist team | CEO, engineering manager, designer, staff reviewer, QA lead, security officer, release engineer, SRE, DX lead, technical writer, performance engineer, memory manager. |

Precode intentionally avoids simulating a full organization. Its user should not have to act like a product manager, engineering manager, architect, QA lead, security reviewer, and release engineer just to operate the system. BMAD and gStack both prove there is user value in role-specific workflows, especially when the role produces a bounded artifact or review. The useful Precode question is not "Which personas should we add?" but "Which missing review or planning boundary deserves a plain-English bead template, mode, prompt, or check?"

### 6. Review And Quality Model

| System | Review posture | Notable mechanics |
|---|---|---|
| Precode OS | Evidence over confidence. | Recorded checks, closeout evidence, manual verification, review decision, next-step/adaptive-depth/files-in-play advisory warnings. |
| BMAD Method | Adversarial and phase-aware review. | Implementation readiness, code review, correction, fresh-context review, false-positive awareness. |
| gStack | Specialist audits and live verification. | `/review`, `/qa`, `/qa-only`, `/cso`, `/benchmark`, `/canary`, `/codex`, `/design-review`, `/devex-review`. |

BMAD's strongest review idea is routing failure back to the layer where it entered: intent, spec, or implementation. gStack's strongest review idea is broad specialist coverage plus live browser verification. Precode's strongest review idea is durable recorded evidence tied to one active unit, with advisory warnings that make next action, bead depth, and file-scope drift visible before a non-technical builder accepts work.

### 7. Automation And Autonomy

| System | Autonomy posture |
|---|---|
| Precode OS | Agents can propose and execute inside a bead; generated helpers can advise; humans approve sensitive transitions. |
| BMAD Method | Adaptive depth and Quick Dev allow longer autonomous runs after intent/spec compression. |
| gStack | High automation across sprint steps, including review, QA fixes, ship, deploy, canary, docs, and retros. |

Precode is deliberately conservative because its target user may not be able to spot hidden technical drift until it becomes expensive. BMAD and gStack show a path to conditional autonomy: autonomy should increase only after intent is compressed, boundaries are explicit, tests/checks are known, review can classify failures without turning everything into a tangent, and the bead's `autonomy_level` supports the risk.

### 8. Packaging And Ecosystem

| System | Packaging |
|---|---|
| Precode OS | Repo-native Markdown, shell/Python scripts, adapters, generated logs, generated help, Apache-2.0 license, `NOTICE`, and SPDX script provenance. |
| BMAD Method | `npx bmad-method install`, generated IDE skills, official modules, roadmap toward universal/adaptive skills and marketplace. |
| gStack | Git clone/setup into skill directories, team mode, host adapters, slash commands, browser tooling, standalone CLIs. |

BMAD is strongest as a packaged ecosystem. gStack is strongest as a practical daily-driver install. Precode is strongest as a repo-native control layer, and its open-source packaging should stay boring, explicit, and attribution-preserving: Apache-2.0 for adoption, `NOTICE` for provenance, SPDX headers for clarity, and no hidden "watermark" mechanics that make the project harder to trust.

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
| Intent shaping | Product Definition Gate | Analysis/planning workflows | `/office-hours`, CEO/design/eng/DX reviews |
| Context | Tiny active memory | Progressive artifacts | Skill docs, learnings, GBrain/browser memory |
| Work breakdown | Beads | Epics/stories | Sprint commands and plans |
| Quality | Recorded evidence plus advisory depth/scope warnings | Readiness/review/correct-course | Review, QA, security, browser, release gates |
| Handoff | Handoff packet and active bead | Phase artifacts | Checkpoint commits, context restore, learnings |

## Where They Differ Most

### Precode vs BMAD

BMAD is broader and more process-complete. It gives builders many paths from idea to implementation, backed by named agents and generated skills. Precode is narrower and stricter. It does not try to be the entire software development lifecycle. It tries to keep a real repo's operating truth small, inspectable, enforceable, and legible to a builder who may not know lifecycle terminology yet.

BMAD asks the builder to trust a structured lifecycle. Precode asks the builder to trust the repo's authority and evidence model, while using beginner-facing docs and generated help to translate that model into "what should I ask, approve, check, or stop now?"

### Precode vs gStack

gStack is optimized for speed, taste, and production throughput. It gives the agent a rich command vocabulary for product challenge, design, review, QA, security, release, browser use, and learning. Precode is optimized for durability, governance, and non-technical control. It is comfortable slowing transitions down so the builder can see what changed, why it changed, what evidence proves it, and whether the next step is still inside the approved scope.

gStack asks the builder to run the right specialist next. Precode assumes the builder may not know which specialist to summon, so it asks whether the next action is still inside the approved bead, whether changed files match `files_in_play`, whether proof exists, and what human decision is required.

### BMAD vs gStack

BMAD is more lifecycle-methodical. gStack is more founder-operator and shipping-oriented. BMAD's default shape is "produce the right artifacts in the right order." gStack's default shape is "run the right specialist workflow to make the product better and ship it."

BMAD is closer to an AI-native agile framework. gStack is closer to an AI-native startup operating cadence.

## Roadmap Candidates For Precode From BMAD

### High-Fit Candidates

| Candidate | Why it fits Precode | Precode-shaped version |
|---|---|---|
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
| Safety guardrails and edit freeze | gStack's `/careful`, `/freeze`, and `/guard` are immediately useful. Precode now has advisory files-in-play warnings, command-risk classification, sensitive-surface prompts, and optional edit-lock guidance. | Keep tuning these as beginner-facing stop signs, not as automatic permission or hidden enforcement. |
| Continuous local checkpointing | gStack's local WIP checkpoints plus context restore directly address crash/context loss. | Add optional Precode local checkpoints that record bead id, decisions, remaining work, failed approaches, and changed files without auto-pushing. |
| Release documentation freshness | gStack's `/document-release` attacks doc drift after shipping. | Add a doc-drift closeout check that compares changed surfaces against `README`, `ARCHITECTURE`, `API`, `DATA-MODELS`, `SECURITY`, and PRD/bead references. |
| Post-deploy canary and benchmark evidence | Precode can currently record commands, but release/runtime evidence is not a visible lane. | Add release bead templates with staging URL, deploy command, smoke tests, browser verification, canary checks, and rollback notes. |

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

Precode should become the repo-native control plane that helps non-technical solo builders safely use workflow systems like BMAD and gStack without needing to absorb their full professional vocabulary or operating complexity.

After the Theme 1, Theme 2, and Theme 5 kernel update, Precode's control plane is no longer only passive evidence. It now has a small generated guidance loop: next-step help, adaptive-depth warnings, files-in-play guardrails, optional command-risk classification, and advisory edit-lock guidance. These are still advisory surfaces. They make the operating model easier for a beginner to operate without expanding active memory, granting automatic command approval, or turning generated reports into authority.

The important synthesis is not "Precode now has more metadata." The important synthesis is "Precode can translate repo state into a small number of human decisions: continue, ask for missing info, ask for proof, review, approve transition, repair state, approval needed, or stop."

The right synthesis is not:

```text
Precode = BMAD + gStack
```

The better synthesis is:

```text
Precode kernel
  -> generated next-step and guardrail surfaces
  -> optional planning packs inspired by BMAD, translated for non-technical builders
  -> optional specialist review packs inspired by gStack, translated into acceptance questions
  -> all outputs routed through authority, beads, checks, evidence, and human gates
```

That preserves the core:

- tiny active memory;
- one owner per fact;
- one active bead;
- generated output demoted;
- generated next-step help is advisory only;
- evidence over confidence;
- human approval at transitions;
- tool-neutral adapters.

## Suggested Precode Roadmap Themes

### Theme 1: Make "What Next?" Obvious

Inspired by BMAD's `bmad-help` and gStack's opinionated quick start.

Already absorbed into the kernel:

- `scripts/next-step.py`
- `logs/next-step.json`
- `PRECODE-HELP.md` as generated output
- beginner-facing `plain_english_summary`, `user_decision`, `stop_if`, and approval prompt fields

Harden next:

- keep the first line focused on "what should I do now?";
- keep warning noise low unless it changes the user's decision;
- improve state-specific decisions for continue, proof, review, transition approval, state repair, and stop;
- keep `PRECODE-HELP.md` clearly demoted from active memory and task authority.

Consider later:

- a more interactive next-step explainer;
- richer examples in generated help;
- adapters that show the same decision language in Claude, Codex, Cursor, Gemini, and other tools.

Do not do:

- do not let generated help choose the next task;
- do not let `PRECODE-HELP.md` become active memory;
- do not turn next-step guidance into autonomous transition approval.

### Theme 2: Add Adaptive Bead Depth

Inspired by BMAD's scale-domain-adaptive claim and Quick Dev routing.

Already absorbed into the kernel:

- `complexity: trivial | narrow | standard | high-risk | multi-system`
- `required_planning_depth: none | brief | PRD | PRD+architecture | PRD+architecture+test-plan`
- `autonomy_level: supervised | bounded-afk | human-only`
- `scripts/bead-depth-check.py`
- inferred defaults when old or simple beads omit optional fields

Harden next:

- add more beginner-facing examples for tiny fixes, normal tasks, risky tasks, multi-system tasks, and human-only work;
- keep warnings quiet for old/simple beads unless risk demands action;
- make high-risk depth warnings point to a concrete user decision: ask for planning, ask for proof, require approval, split, or stop;
- improve migration guidance without forcing immediate metadata churn.

Consider later:

- risk-specific bead templates;
- generated suggestions for depth fields during bead proposal;
- import bridges that translate BMAD/gStack artifacts into Precode bead depth.

Do not do:

- do not make every bead carry PRD ceremony;
- do not break existing beads that omit optional fields;
- do not make adaptive depth a taxonomy the beginner must master before building.

### Theme 3: Build Review Lanes

Inspired by gStack's specialist reviews and BMAD's adversarial review.

Pending to consider after Themes 1, 2, and 5 are quiet and trusted:

- code review;
- product/scope review;
- design review;
- developer-experience review;
- security review;
- performance review;
- docs freshness review;
- release/canary review.

Each lane should define:

- when it is required;
- what evidence it produces;
- where findings are recorded;
- how to decide whether a finding belongs to the current bead.

Each lane should also translate the specialist concern into a plain approval question so the user is not forced to impersonate a designer, security reviewer, QA lead, or release engineer.

Do not do:

- do not add persona sprawl;
- do not make the user manage a fake product/engineering organization;
- do not let specialist reviews override the active bead or owner files.

### Theme 4: Strengthen Verification Evidence

Inspired by BMAD TEA and gStack QA/benchmark/canary.

Pending to consider when risk or release context justifies it:

- risk-based test matrix;
- requirement-to-test traceability;
- manual browser evidence schema;
- screenshot/video/log references;
- deploy and canary closeout sections;
- NFR assessment for security, performance, accessibility, and reliability.

Do not do:

- do not make every small bead produce enterprise-grade evidence;
- do not confuse generated advisory checks with proof of done;
- do not replace human QA for product fit, UX taste, or sensitive approval.

### Theme 5: Add Guardrails Around File Mutation

Inspired by gStack's freeze/guard tools and Precode's existing `files_in_play`.

Already absorbed into the kernel:

- `scripts/files-in-play-check.py`;
- warning when changed files are outside active bead scope;
- command-risk classification with `--command`;
- optional advisory edit-lock view with `--edit-lock`;
- plain decisions: continue, approval needed, or stop.

Harden next:

- tune destructive-command and sensitive-surface patterns against real use;
- make approval prompts more specific for auth, payments, secrets, migrations, deploys, production config, dashboards, and destructive local actions;
- add better examples for when to split, revert, or approve a scope change;
- keep non-git checkout warnings helpful without making them block normal work.

Consider later:

- integration with tool adapters before command execution;
- stronger write-boundary previews;
- optional local checkpoint snapshots for high-risk beads.

Do not do:

- do not silently block normal work;
- do not approve commands automatically;
- do not treat generated reports as scoped implementation files;
- do not hide destructive or sensitive risk behind a green check.

### Theme 6: Package Optional Protocol Packs

Inspired by BMAD modules and gStack host adapters.

Consider later, after kernel behavior and docs are stable:

- `precode-pack-planning`;
- `precode-pack-ui-review`;
- `precode-pack-security`;
- `precode-pack-release`;
- `precode-pack-docs`;
- `precode-pack-existing-repo-intake`.

Rule: packs may add reference docs, templates, scripts, and generated evidence, but may not add active-memory files.

Do not do:

- do not go marketplace-first;
- do not let packs add active memory;
- do not let packs weaken the one-owner-per-fact rule.

## Priority Recommendation

The most valuable roadmap sequence is now:

1. Keep hardening the landed `next-step` helper until the first line reliably tells a non-technical builder what to do now.
2. Keep hardening adaptive bead depth until it feels like proportional guidance, not metadata homework.
3. Keep hardening files-in-play and command guardrails until destructive and sensitive work reliably says approval needed or stop.
4. Add review lanes only after the basic continue/ask/prove/approve/stop loop is quiet and trusted.
5. Add PRD/bead import bridges for BMAD and gStack artifacts only if they preserve Precode authority and do not import process bloat.
6. Add optional protocol packs after the kernel, installer, and beginner docs are stable.

The opinionated line: Precode should not become BMAD-lite, gStack-lite, a PM framework, or an autonomous specialist team. Its job is to keep a non-technical solo builder oriented, protected, and in control.

## Strategic Positioning

For users, the clearest market map is:

| User need | Best fit |
|---|---|
| "I need a full AI-native agile method from idea to implementation." | BMAD |
| "I want my coding agent to plan, review, QA, and ship like a specialist team." | gStack |
| "I am a non-technical solo builder and need my repo to preserve truth, scope, evidence, handoff, and next-step clarity across agents." | Precode |

For Precode's roadmap, the core discipline should be:

> Borrow workflows, not memory bloat. Borrow specialists, not persona sprawl. Borrow automation, not uncontrolled momentum.

Precode wins if it remains the trusted control layer underneath fast AI workflows, especially for builders who need software-development concepts translated into guided decisions they can confidently approve.
