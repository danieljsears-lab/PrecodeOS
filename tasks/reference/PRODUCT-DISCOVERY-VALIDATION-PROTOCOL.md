# PrecodeOS -- Product Discovery Validation Protocol
<!-- ANCHOR: product-discovery-validation-protocol -->

> AUTHORITY: Advisory product-discovery validation workflow, evidence-strength language, assumption identification, current-alternative analysis, beginner interview guidance, smallest learning-step framing, and proceed/pause/narrow/kill recommendations before PRD shaping.
> NOT_AUTHORITY: Active memory, product decisions, PRD approval, task selection, bead activation, route structure, schema definitions, implementation plans, generated progress state, or proof that an idea is worth building.
> LOAD_WHEN: A product idea is broad, risky, market-facing, paid, evidence-poor, solution-first, or likely to become a PRD before the user problem, current alternatives, assumptions, and smallest learning step are clear.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-06-23

## Purpose

Product Discovery Validation helps a solo builder decide whether an idea is ready for product definition, needs more evidence, should be narrowed, or should be dropped for now.

It sits before PRD shaping:

```text
rough idea or source evidence
  -> Product Discovery Validation when worth-building is uncertain
  -> Local Source Intake or Idea-to-PRD
  -> destination PRD shard
  -> candidate beads
```

The protocol does not validate an idea in the strong sense. It produces evidence and an advisory recommendation. The user still owns judgment, product direction, PRD approval, and task activation.

For first-time non-technical builders and bootcamp students, discovery often aims for MVP-ready conviction rather than validated demand. MVP-ready conviction means the builder can define a small, safe first version while naming the weak evidence, riskiest assumption, current workaround, not-yet scope, and smallest learning step. It does not prove that users will adopt, pay, return, switch, or change behavior.

## When To Use

Use this protocol when the main uncertainty is whether the problem, user, demand, alternative, or smallest learning step is real enough to justify PRD work.

Good triggers:

- new product direction
- market-facing feature
- paid, pricing, or revenue assumption
- broad audience such as "everyone", "small businesses", or "students"
- weak or mostly internal evidence
- no named current workaround
- solution-first request with unclear pain
- sensitive trust surface such as personal data, files, money, advice, auth, or external services
- first slice that is too large to throw away
- repeated excitement but no behavior evidence

## When Not To Use

Do not add discovery ceremony for:

- typo fixes, copy edits, or narrow polish
- known defects with a clear reproduction path
- implementation follow-through from an approved PRD
- internal repo maintenance where the user problem and acceptance evidence are already clear
- tiny personal tools where the builder is the only user and the risk is low

For narrow work, use Workflow Selection, Local Source Intake, PRD shaping, or the active bead directly.

## Core Four Methods

Use the smallest method set that can change the builder's decision.

| Method | Use it to learn | Beginner-safe question |
|---|---|---|
| Customer/problem interviews | Whether real people have the problem in a specific situation. | "Tell me about the last time this happened." |
| Current-workaround analysis | What users do today, what works, what breaks, and why they keep doing it. | "How do they solve this now, even messily?" |
| Assumption tests | Which belief must be true before the idea can work. | "What is the riskiest thing we are assuming?" |
| Demand or pricing signals | Whether people show costly interest, budget, switching effort, signup intent, or willingness to pay. | "What would they give up, pay, try, or change?" |

Prefer learning before building when evidence is weak. A tiny reversible build can be a learning step only when it is the fastest credible way to test behavior and it does not cross sensitive surfaces.

## Evidence Ladder

Use plain evidence-strength language. Do not treat all signals as equal.

| Evidence | Strength | How to treat it |
|---|---|---|
| Founder hunch or agent suggestion | very weak | Useful starting point only. |
| Online research, guided research, or category notes | weak | Context, not user proof. |
| User quote about a real past moment | medium | Evidence of pain or language. |
| Repeated pattern across users or sources | stronger | Candidate problem evidence. |
| Existing workaround, spend, or switching effort | strong | Behavioral evidence that the problem costs something. |
| User tries a prototype, signs up, pays, returns, or changes behavior | strongest | Demand or value evidence, depending on the action. |

Name the primary hypothesis or learning target, strongest evidence, and weakest assumption in every Discovery Summary.

Treat source-cited guided research as helpful context unless it is paired with behavior. Research can show market language, categories, competitors, rough demand signals, or risks, but it is not validation by itself. Evidence becomes stronger when it shows a real current workaround, repeated user behavior, spend, switching effort, signup intent, prototype use, payment, return visits, or another costly action.

## Hypothesis Mechanics

Use one shared vocabulary before PRD shaping:

- A `hunch` is an early belief or idea worth exploring.
- An `assumption` is an unproven dependency that must be true for the idea to work.
- A `hypothesis` is a testable belief about a specific user or situation, expected behavior, supporting evidence, weakest assumption, and falsifier.
- An `experiment hypothesis` is a metric-backed rollout bet. Use `tasks/reference/PLANNING-PROTOCOL.md` when success metrics, exposure, monitoring, and kill criteria are needed.

Plain hypothesis shape:

```text
Primary hypothesis / learning target:
- User or situation:
- Pain or current workaround:
- Expected behavior or change:
- Supporting evidence:
- Weakest assumption:
- Falsifier or what would change our mind:
```

Do not treat a hunch, assumption, or hypothesis as product approval. Weak or research-only hypotheses should route to the smallest learning step, Product Discovery Validation, Candidate Queue review, defer, narrow, or kill before PRD or implementation momentum starts.

Use `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md` when a user later asks whether the hypothesis or learning target was tested, narrowed, killed, promoted, left untested, made stale, or ready for the next workflow. The review is evidence only and does not approve product direction, approve a PRD, rank candidates, activate beads, choose tasks, require analytics, or create a database.

## Assumption Categories

When choosing what to test, identify assumptions in these categories:

- Desirability: users want this enough to act.
- Viability: the idea can support the builder's product, pricing, trust, or operating model.
- Feasibility: the product can be built and operated with acceptable cost and complexity.
- Usability: users can understand and complete the key workflow.
- Ethical: the product does not create unacceptable harm, manipulation, privacy risk, or false confidence.

Make assumptions specific. "Users will like it" is too vague. "A solo tutor will replace a spreadsheet if follow-ups take under two minutes to capture" is testable.

## Interview Guidance

Ask about the user's life, not the builder's idea.

Prefer:

- "Walk me through the last time this problem happened."
- "What triggered it?"
- "What did you do first?"
- "What did you try before?"
- "What worked about the workaround?"
- "What broke, wasted time, cost money, or created stress?"
- "What happened when it did not get solved?"
- "Who else was affected?"
- "What would make you switch from the current way?"
- "What would make this not worth changing?"

Avoid:

- "Do you like this idea?"
- "Would you use this?"
- "Would you pay for this?"
- "Is this frustrating?"
- "Should I build feature X?"

Compliments are not evidence. If a user compliments the idea, return to behavior:

```text
Set my idea aside for a moment. Tell me about the last time this problem came up and what you actually did.
```

## Discovery Summary

Use this format as the main artifact. Keep it short enough to paste into Local Source Intake or a PRD `Discovery Evidence` section.

```text
Discovery Summary:
- Idea:
- Target user and situation:
- User problem:
- Current alternatives or workarounds:
- Primary hypothesis / learning target:
- Strongest evidence:
- Weakest assumption:
- Evidence strength: very weak | weak | medium | strong | strongest
- Assumption categories in play: desirability | viability | feasibility | usability | ethical
- Demand or pricing signal:
- Smallest non-code learning step:
- What would change our mind:
- Hypothesis review status: `untested | tested | narrowed | killed | promoted | stale | not applicable`
- Learning outcome:
- Sensitive surfaces:
- Recommendation: proceed | pause | narrow | kill
- Reason:
- Recommended next Precode workflow:
- Authority files likely affected:
- Guardrail reminder: discovery is evidence only, not PRD approval, task activation, or permission to code.
```

## Recommendation Language

Use plain advisory decisions:

| Recommendation | Meaning | Typical next step |
|---|---|---|
| `proceed` | Evidence is good enough to shape a PRD or source summary. | Local Source Intake or Idea-to-PRD. |
| `pause` | A missing answer could change whether the idea is worth defining. | Run the smallest learning step first. |
| `narrow` | The idea may be promising, but the audience, problem, or first slice is too broad. | Reframe around one user, one painful moment, one workaround, or one assumption. |
| `kill` | Evidence suggests this is not worth pursuing now. | Record as no action, defer, or keep only as historical source evidence. |

Do not let `proceed` mean "approved." It only means the idea is ready for the next planning workflow.

## Promotion Path

Discovery findings are evidence. Promote only reviewed conclusions:

| Discovery finding | Destination |
|---|---|
| Product promise, user, job, strategy, non-goal, current bet, success signal | `PRODUCT.md` after user review |
| Source facts, assumptions, conflicts, open questions | Local Source Intake summary |
| Product problem, users, goals, non-goals, requirement candidates | PRD shard |
| Hard product or technical decision | `DECISIONS.md` |
| Security, privacy, trust, or sensitive-surface concern | `SECURITY.md` or PRD risk model |
| Work to execute | Candidate bead only after PRD readiness and user approval |
| Not worth pursuing now | No action, defer note, or historical evidence pointer |

## Guardrails

- Discovery output is evidence only.
- It must not approve a PRD.
- It must not create or activate beads.
- It must not update `tasks/todo.md`.
- It must not select the next task.
- It must not treat generated research summaries as user proof.
- It must not ask the builder to paste secrets, credentials, private transcripts, billing data, or sensitive personal data.
- It must not make discovery mandatory ceremony for tiny tasks.

## Builder Prompt

```text
Use Product Discovery Validation on this idea.
Interview me one question at a time. Challenge assumptions supportively.
Tell me the current workaround, primary hypothesis or learning target, strongest evidence, weakest assumption, smallest non-code learning step, and whether you recommend proceed, pause, narrow, or kill.
Treat the output as evidence only. Do not write a PRD, create beads, update PRODUCT.md, or code.
```
