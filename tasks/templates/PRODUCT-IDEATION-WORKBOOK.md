# Product Ideation Workbook
<!-- ANCHOR: product-ideation-workbook -->

> AUTHORITY: Reusable student and builder workbook for gathering product thoughts, research, assumptions, risks, capability candidates, and Conviction Packet evidence before Precode Local Source Intake.
> NOT_AUTHORITY: Product decisions, approved requirements, active task selection, `PRODUCT.md` content, PRD approval, implementation plans, bead activation, generated progress state, or permission to code.
> LOAD_WHEN: A new user, student, founder, operator, or creator wants to research, challenge, narrow, and package one rough product idea with Claude, Claude Code, Codex, or another agent before ingesting it into Precode.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears
Document version: v0.2.5
Last updated: 2026-06-29

## Purpose

Use this workbook before you ask Precode to update `PRODUCT.md`, write a PRD, create beads, or implement a net-new rough product idea.

The dominant outcome is a reviewed Conviction Packet / Precode Ingestion Packet ready for Precode Local Source Intake. This workbook tightens the handoff; it does not create a second workflow, a readiness gate, a PRD shortcut, a backlog, a bead, or permission to code.

This workbook is the default PrecodeOS beginner idea path. It can be invoked directly, through Precode Idea Coach, or as the start of First PRD Walkthrough. First PRD Walkthrough is a plain-language entrypoint, not a new protocol, PRD shortcut, backlog, bead approval, or coding permission.

The path is:

```text
Idea -> Guided interview -> Product Brief -> Challenge And Clarity -> Evidence check -> optional learning/MVE framing -> Conviction Packet -> Local Source Intake
```

Important rule: this workbook is evidence, not authority. Nothing in it becomes true for the project until you review it and Precode promotes stable conclusions into the right owner file through Local Source Intake, PRD shaping, `PRODUCT.md`, `DECISIONS.md`, or another owner file.

Build-React-Learn happens later, after the workbook has been reviewed, the packet has gone through Local Source Intake, and Precode has enough PRD or approved exploratory scope to create a normal bead. In this workbook, use sketches, visible iteration, and non-code learning to prepare the path; do not treat workbook output as an exploratory prototype bead or permission to code.

Bypass this workbook for bugs, maintenance, approved PRD follow-through, narrow feature changes, and other work where the product problem and scope are already clear.

## How This Workbook Thinks

You do not need product-management vocabulary. You only need to keep asking plain questions:

- Who is this really for?
- What hurts today?
- What do they do instead?
- What evidence says this problem is real?
- What changes after?
- What must not be built yet?
- What would make this worth defining, testing, or building?
- What could make this a bad idea?

The goal is MVP-ready conviction, not proof that the idea is validated. Conviction means you can name the user, painful before moment, current workaround or evidence, primary hypothesis or learning target, strongest evidence, weakest assumption, smallest complete useful payoff, not-yet scope, and smallest learning step.

Before handoff, run a compact readiness self-check. The packet should name the user, painful moment, current workaround or evidence, primary hypothesis or learning target, strongest evidence, weakest assumption, MVP-ready first slice, not-yet scope, sensitive surfaces, and recommended next Precode path. This self-check is advisory only. It does not approve a PRD, owner-file edit, roadmap, backlog, bead, or coding.

## Choose Your Builder Lens

Choose the lens that best matches why you are building. The lens helps the agent ask better questions; it does not create a separate workflow.

### Problem-Rich Operator Or PM

Use this lens if you understand a painful workflow, product surface, internal process, stakeholder need, customer support pattern, consulting opportunity, or career-relevant business problem.

Default question:

```text
What painful workflow or product surface do I understand well enough to improve?
```

Look for repeated manual work, stakeholder friction, missed follow-up, slow handoffs, unclear ownership, product or customer pain you have seen directly, or work/career ROI from learning to build better with AI.

### Solo B2B Founder

Use this lens if you are trying to turn a customer problem into a usable first product.

Default question:

```text
What customer problem am I trying to turn into a customer-ready first product?
```

Look for a reachable customer segment, a painful current workaround, urgency, budget, switching effort, willingness to try, or a first value moment small enough to test.

### AI-Curious Creator Or Broad Builder

Use this lens if your main goal is learning, experimentation, or making a useful experience visible.

Default question:

```text
What do I want to learn or make useful by building with AI?
```

Look for a personal workflow, an audience or community you understand, a creative tool, a guide, a helper, a clear learning goal, or a small complete experience you can show and improve.

## Guided Interview Process

Run this workbook as a guided interview inside Claude Code, Claude, Codex, ChatGPT, or another agent. Claude Code Plan Mode or an equivalent planning mode is useful when available because it keeps the session exploratory and non-mutating.

The stages are:

1. Orientation: confirm one idea, builder lens, likely user type, and that you are not pasting sensitive information.
2. First Three Questions: answer at most three high-level product or business questions, then get a Product Brief.
3. Challenge And Clarity: push back on broad users, vague pain, missing workaround, weak evidence, feature piles, oversized MVPs, and sensitive surfaces.
4. Evidence And Assumption Check: rate evidence strength, name the primary hypothesis or learning target, strongest evidence, weakest assumption, what would change your mind, and smallest non-code learning step.
5. Optional Learning/MVE Framing: when useful, define the smallest complete useful payoff, visible iteration, and core workflow spine.
6. Candidate Capability Matrix: translate possible features into candidate capabilities, not approved requirements.
7. Handoff: produce the reviewed Conviction Packet / Precode Ingestion Packet, Local Source Intake readiness self-check, and the exact Local Source Intake handoff prompt.

Stop the interview when the idea is clear enough for the next Precode step. Move unresolved but non-blocking concerns into `Not yet`, `Needs discovery`, or `Open questions`.

## Stop Before You Paste Sensitive Information

Do not paste secrets, credentials, billing or dashboard values, private customer records, raw private transcripts, sensitive personal data, or production configuration values.

If something sensitive matters, use a safe placeholder:

```text
The app will use a payment provider, but I am not pasting keys or dashboard values here.
```

## Copyable Guided Product-Coach Prompt

```text
Act as my guided PrecodeOS product coach for the Product Ideation Workbook. If Claude Code Plan Mode or an equivalent planning mode is available, use it.

Help me research, ideate, challenge, and refine one product idea. Interview me one question at a time. Give me a recommended answer when useful, but do not decide for me. Use plain language, not product-management jargon. Separate what I know, what I think, and what I need help deciding.

First ask me to choose the builder lens that best fits this session:
- Problem-rich operator or PM
- Solo B2B founder
- AI-curious creator or broad builder

Follow the workbook stages: Orientation, First Three Questions, Challenge And Clarity, Evidence And Assumption Check, optional Learning/MVE Framing, Candidate Capability Matrix, and Handoff.

After at most three high-level product or business questions, summarize progress using the Product Brief fields in this workbook. Challenge broad users, vague pain, missing current workaround, weak evidence, solution-first framing, feature piles, oversized MVP slices, and sensitive surfaces. Rate evidence strength as very weak, weak, medium, strong, or strongest. Treat online research as weak evidence unless it is paired with behavior, a current workaround, spend, switching effort, prototype use, payment, return visits, or another costly action.

When the idea is clear enough, produce a reviewed Conviction Packet / Precode Ingestion Packet, Local Source Intake readiness self-check, and Local Source Intake handoff prompt. If worth-building uncertainty is the main issue, recommend Product Discovery Validation instead of forcing a Conviction Packet.

Evidence only; no PRD, beads, owner-file edits, roadmap or backlog, or code.

Start by asking me to describe the product idea in plain English and choose the closest builder lens.
```

## Product Brief

After at most three high-level questions, ask the agent to summarize progress. Evidence only; no PRD, beads, owner-file edits, or code.

Product Brief:

- Product idea:
- Builder lens:
- Intended user:
- Painful before moment:
- Better after moment:
- Current workaround or evidence:
- Assumptions:
- Primary hypothesis / learning target:
- Not-yet list:
- Smallest useful version:
- Next best question:

## Initial Direction

Capture the first plain-English direction before the workbook challenges or refines it.

- What I think I want to build:
- Builder lens:
- Who it might help:
- Why now:
- What would make this useful:
- What I do not want to build yet:

## Product-Level Thinking

Use this section for thoughts that might later affect `PRODUCT.md`.

### Real Person Test

Use this when your audience sounds broad, such as "small businesses," "students," or "busy people."

- They are:
- They are trying to:
- They are frustrated because:
- They use these words:
- They would care about this now because:

### Painful Moment

Describe the moment right before the user would want help.

- What just happened?
- What are they trying to finish?
- What is slowing them down?
- What mistake, delay, cost, or stress are they trying to avoid?
- What would they say out loud in that moment?

### Current Workaround Map

List what users do today, even if it is messy.

| Current workaround | What works about it | What breaks, wastes time, or feels painful | Why users still use it |
|---|---|---|---|
|  |  |  |  |

### Before/After Flip

The after sentence should describe a real outcome, not a feature list.

- Before this product, the user:
- After this product, the user:

### Strategy And Non-Goals

What should this product not become right now?

| Not yet | Why it is tempting | Why it can wait |
|---|---|---|
|  |  |  |

### Success Signals

Choose one early sign that a real person got value.

- A user finishes:
- A user returns to:
- A user replaces:
- A user saves:
- A user says:

## Challenge And Clarity

Ask the agent to challenge the idea before it becomes features.

```text
Challenge this idea before I turn it into features.

Identify weak assumptions, missing user evidence, risky scope, vague success criteria, privacy or safety concerns, sensitive surfaces, and reasons not to build yet. Push back on broad users, vague pain, missing current workaround, research-only proof, premature feature lists, and oversized MVP slices.

Force plain-English answers for:
- intended user
- painful before moment
- better after moment
- current workaround or evidence
- primary hypothesis or learning target
- weakest assumption
- first useful slice
- what would change my mind
- smallest non-code learning step

Sort concerns into Must decide now, Good enough for MVP, and Defer / Not yet. Keep the tone supportive and practical. Then recommend the smallest safe next learning step. Do not make the decision for me.
```

Continue only when you can explain:

- who the product is for
- what painful moment it addresses
- what users do today instead
- what should not be built yet
- what would count as useful

## Research And Evidence

Use this section for research, quotes, observations, links, and uncertainty.

### Evidence Ladder

Use this to avoid treating every signal as equally strong.

| Evidence | Strength | How to treat it |
|---|---|---|
| Founder hunch or agent suggestion | very weak | Useful starting point only. |
| Online research or category notes | weak | Context, not user proof. |
| User quote about a real past moment | medium | Evidence of pain or language. |
| Repeated pattern across users or sources | stronger | Candidate problem evidence. |
| Existing workaround, spend, or switching effort | strong | Behavioral evidence that the problem costs something. |
| User tries a prototype, signs up, pays, returns, or changes behavior | strongest | Demand or value evidence, depending on the action. |

Strongest evidence so far:

-

Weakest assumption:

-

Evidence strength:

- `very weak | weak | medium | strong | strongest`

### Source-Cited Research

| Source link or title | Date or recency | Claim or fact | Confidence | Uncertainty |
|---|---|---|---|---|
|  |  |  | high / medium / low |  |

### User Quotes Or Observations

Do not paste private raw transcripts unless you are comfortable sharing them. Short approved summaries are better.

| Source | Quote or summary | What it suggests | Confidence |
|---|---|---|---|
|  |  |  | high / medium / low |

### Must-Be-True List

| Must be true | What evidence supports it? | What could prove it wrong? | Confidence |
|---|---|---|---|
|  |  |  | high / medium / low |

### Smallest Non-Code Learning Step

Choose the smallest way to learn without writing product code:

- interview people who recently had the problem
- map the current workaround from start to finish
- show a sketch or clickable prototype
- run a landing-page, waitlist, or fake-door test
- ask for budget, switching effort, or current spend evidence
- manually perform the service once before automating it

Smallest non-code learning step:

-

What result would make me proceed:

-

What result would make me pause, narrow, or kill:

-

## Optional Learning/MVE Framing

Use this section when the idea is still too abstract, too large, or too feature-shaped. It imports the useful parts of the older Student Idea To MVE path without creating a separate workflow.

### Visible Iteration

Make the idea visible before defining the core workflow. Use a sketch, rough screen, clickable mockup, storyboard, spreadsheet, paper flow, or throwaway prototype. The goal is not polish. The goal is to see what changes when the idea becomes visible.

- What did I make visible?
- What did I notice only after seeing it?
- What confused me or someone else?
- What became smaller, simpler, or more important?
- What should move to Not yet?
- What should stay in the first version?

Self-check: continue only when you have changed at least one product decision because the idea became visible. If nothing changed, name that honestly and move on.

### Core Workflow Spine

The spine is the smallest meaningful path through the experience, not the whole product.

| Spine step | User action | Product response | What value or confidence this creates |
|---|---|---|---|
| Trigger |  |  |  |
| First action |  |  |  |
| Key step 1 |  |  |  |
| Key step 2 |  |  |  |
| Completion |  |  |  |
| Return path |  |  |  |

Self-check: continue when the spine can be completed by a real user without needing the whole imagined product. Pause if it depends on too many integrations, roles, dashboards, admin tools, or future features.

### Smallest Complete Useful Payoff

This is the smallest end-to-end experience that gives one real user one useful payoff. It is not a full MVP, a PRD, a bead, or implementation approval.

- The user is:
- It helps them when:
- The complete value moment is:
- The first version includes:
- The first version excludes:
- The success signal is:
- The main risk is:
- The smallest safe build boundary is:

Self-check: continue when this names one user, one complete value moment, explicit non-goals, one success signal, and the main risk.

## Exploration Loop

Use this when you already have material and want the agent to think with it before you commit to PRD shaping. The loop can use Product Briefs, workbook notes, rough feature lists, research snippets, user quotes, chat summaries, screenshots, sketches, Candidate Goal Frames, and prior not-yet ideas.

```text
Use the Exploration Loop on the content I already have.

First summarize what is already known from my notes: users, pains, goals, candidate features, evidence, assumptions, risks, and not-yet ideas. Do not ask me to repeat information already present.

Then help me discover what I have not considered yet. Ask one targeted question at a time only when the answer could change the product direction, evidence strength, first useful slice, risk, or PRD readiness.

Translate user moments into capability candidates, not approved features. Sort concerns into Must decide now, Good enough for MVP, and Defer / Not yet.

End with an Exploration Evidence Packet and a compact capability-candidate matrix.

Evidence only; no feature list, roadmap, backlog, requirements, PRD, beads, owner-file edits, or code.
```

## Candidate Capability Matrix

These are candidate capabilities, not approved features, a backlog, requirements, or permission to code. Reviewed not-yet ideas or capability candidates may become Candidate Queue entries later, but the queue is not task authority.

| Candidate capability | User moment | Existing evidence | New insight | Risk | MVP fit | Recommendation |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Risks And Sensitive Surfaces

Check any that might appear:

- [ ] Auth or user accounts
- [ ] Payments or billing
- [ ] Personal data
- [ ] Uploads or files
- [ ] Secrets, API keys, or credentials
- [ ] External services
- [ ] Database migrations
- [ ] Production deploys
- [ ] Destructive actions
- [ ] Legal, medical, financial, or safety-sensitive advice

Trust notes:

-

## Conviction Packet / Precode Ingestion Packet

Ask the agent to produce the final packet only when the idea is clear enough for the next Precode step.

Before creating the packet, check the idea against PRD-ready context. This prepares evidence for a future PRD; it is not a PRD, approval, bead, or implementation plan.

```text
Create a concise Conviction Packet / Precode Ingestion Packet from this workbook.

Treat the workbook as evidence, not authority. Do not draft PRODUCT.md. Do not create a PRD. Do not propose active work. Summarize only the stable and decision-relevant material, using PRD-ready context to find gaps without expanding the packet.

Use this format:
- Idea:
  - Product idea summary:
  - Builder lens:
- User / problem:
  - Intended user and job:
  - Painful before moment:
  - Better after moment:
  - Current alternatives or workarounds:
- Evidence:
  - Problem or pain evidence:
  - Evidence strength:
  - Primary hypothesis / learning target:
  - Hypothesis review status, only if already reviewed:
  - Strongest evidence:
  - Weakest assumption:
  - What would change my mind:
  - Demand or pricing signal:
  - Source-cited research summary:
- Scope:
  - Optional visible iteration summary:
  - Optional core workflow spine:
  - Smallest complete useful payoff:
  - MVP-ready first slice:
  - Smallest non-code learning step:
  - Capability candidates:
  - Not-yet list:
- Risks:
  - Assumptions:
  - Open questions:
  - Risks and sensitive surfaces:
- Promotion candidates:
  - Stable facts:
  - Candidate product constitution updates:
  - Candidate feature or PRD ideas:
  - Candidate non-goals:
  - Success signals:
  - Candidate Goal Frame For Precode Review, only if durable intent is clear:
    - Goal:
    - Why now:
    - Success signal:
    - Out of scope:
    - Approval gates:
    - Reaffirmation trigger:
    - Suggested owner file:
- Next Precode step:
  - Local Source Intake readiness self-check:
  - PRD-ready context notes:
  - Likely owner files:
  - Recommended Precode next step:
  - Local Source Intake handoff prompt:

End with: "This Conviction Packet is evidence only. It is not a PRD, not a backlog, not product approval, not a bead, and not permission to code. Candidate Queue entries and Hypothesis Review status are evidence and review mechanics only; they do not rank work, approve product direction, or authorize implementation. The Candidate Goal Frame is evidence only. It is not a Goal Frame yet, not a plan, not a task list, and not permission to update PRODUCT.md. Do not edit PRODUCT.md or create a PRD until the user reviews this intake summary."
```

## Recommended Next Precode Step

Use this chooser after the Conviction Packet:

| If the packet shows... | Recommend... |
|---|---|
| Reviewed packet with enough stable source material | Local Source Intake |
| Weak, broad, paid, market-facing, evidence-poor, or solution-first idea | Product Discovery Validation |
| Useful not-yet idea or capability that should not be lost | Candidate Queue proposal after review |
| Post-intake or post-PRD feature-angle uncertainty | Plan Loop |
| Need to learn from a tiny real-repo prototype | Build-React-Learn later, through a normal approved bead |

Do not route directly from the workbook to PRD approval, feature compilation, bead activation, `tasks/todo.md`, or code.

## Product Discovery Validation Fallback

If worth-building uncertainty is the main issue, do not force a Conviction Packet. Run Product Discovery Validation first.

Use Product Discovery Validation when the idea is broad, risky, market-facing, paid, evidence-poor, solution-first, lacks a named current workaround, touches sensitive trust surfaces, or has a first slice too large to throw away. The detailed rules live in `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`.

```text
Use Product Discovery Validation on this idea.

Interview me one question at a time. Challenge assumptions supportively. Tell me the current workaround, primary hypothesis or learning target, strongest evidence, weakest assumption, smallest non-code learning step, and whether you recommend proceed, pause, narrow, or kill.

Evidence only; no PRD, beads, owner-file edits, or code.
```

## Local Source Intake Handoff

When the packet is ready, bring only the reviewed packet into Precode with this prompt. The readiness self-check is advisory only; it does not approve a PRD, owner-file edit, roadmap, backlog, bead, or coding:

```text
Use Local Source Intake on this Conviction Packet / Precode Ingestion Packet.

Treat the packet as source evidence only. Summarize stable conclusions, assumptions, primary hypothesis or learning target, Hypothesis review status if already reviewed, open questions, risks, Local Source Intake readiness self-check, Candidate Goal Frame status if present, and likely owner files. Do not update PRODUCT.md, draft a PRD, create beads, activate work, or write code until I review the intake summary.
```

## Close-The-Loop Prompt

Use this when Claude or Codex keeps challenging, widening scope, or asking questions after the useful decision is clear enough.

```text
Stop challenging and produce the requested output now.

Only ask another question if the answer would prevent an unsafe, impossible, misleading, or implementation-changing output. Move all non-blocking concerns to Defer / Not yet. Keep the output beginner-safe, concrete, and scoped to the first useful version.

Evidence only; no PRD, beads, owner-file edits, or code.
```
