# Student Idea To MVE Workbook
<!-- ANCHOR: student-idea-to-mve-workbook -->

> AUTHORITY: Experimental student-facing workbook for shaping a rough idea into a Minimum Valuable Experience and Precode ingestion packet.
> NOT_AUTHORITY: Product decisions, approved requirements, active task selection, `PRODUCT.md` content, PRD approval, implementation plans, bead activation, generated progress state, or permission to code.
> LOAD_WHEN: A student, instructor, mentor, or support engineer wants an alternative idea-to-product workbook for assessing product judgment before Precode Local Source Intake.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-30

## Purpose

This workbook is an experimental alternative to `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md`.

Use it when you want a student-friendly path from rough idea to a buildable **Minimum Valuable Experience**: the smallest complete experience that gives a real user one useful payoff.

The promise is simple:

> Learn to vibe code with product judgment, so the thing you build has a better chance of being useful.

Important rule: this workbook is evidence only. It is not a PRD, not product approval, not task activation, not an implementation plan, and not permission to code. Bring the final packet into Precode Local Source Intake before asking Precode to update `PRODUCT.md`, draft a PRD, propose beads, or implement anything.

This version is under assessment. It does not replace the existing Product Ideation Workbook and is not the default PrecodeOS workflow.

## The Path

Use one shared path, then choose the branch prompts that match why you are building.

```text
Idea
  -> Light Discovery
  -> 4Ps Hypothesis
  -> Context Selection
  -> Positioning
  -> Visible Iteration
  -> Core Workflow Spine
  -> Minimum Valuable Experience
  -> Conviction Packet / Precode Ingestion Packet
  -> Experience design canvas when a visual core spine is needed
  -> Student Experience Ingestion Packet before Claude Code implementation
```

Each stage has a one-page canvas:

- purpose
- prompts
- `I know / I think / I need help deciding`
- branch prompts for the three student lenses
- self-check
- Precode translation notes

## Choose Your Lens

Choose the lens that best matches why you are here. You can change it later if the work reveals a better fit.

### Lens 1: Problem-Rich Operator Or PM

Use this lens if you already understand a painful workflow, product surface, internal process, stakeholder need, customer support pattern, consulting opportunity, or career-relevant business problem.

Default question:

```text
What painful workflow or product surface do I understand well enough to improve?
```

Look for:

- repeated manual work
- stakeholder friction
- missed follow-up
- slow handoffs
- unclear ownership
- product or customer pain you have seen directly
- company, consulting, or career ROI from learning to build better with AI

### Lens 2: Solo B2B Founder

Use this lens if you are trying to turn a customer problem into a usable MVP.

Default question:

```text
What customer problem am I trying to turn into a customer-ready first product?
```

Look for:

- agency quotes that are too expensive
- slow development timelines
- lack of a technical cofounder
- a reachable B2B customer segment
- a painful current workaround
- urgency to test a customer-ready MVP

### Lens 3: AI-Curious Creator Or Broad Builder

Use this lens if your main goal is learning, experimentation, or making a useful experience visible.

Default question:

```text
What do I want to learn or make useful by building with AI?
```

Look for:

- a personal workflow you want to improve
- an audience or community you understand
- a creative tool, guide, helper, or prototype idea
- a clear learning goal
- a small complete experience you can show and improve

## How To Work With An AI Thinking Coach

Paste this prompt into Claude, Codex, ChatGPT, or another AI assistant when you want guided help.

```text
Act as my product thinking coach for this Student Idea To MVE Workbook.

Help me move from rough idea to Minimum Valuable Experience. Interview me one question at a time. Use plain language. Challenge assumptions supportively when my idea is vague, too broad, unsupported, or risky. Separate what I know, what I think, and what I need help deciding.

My lens is:
[Operator/PM | Solo B2B founder | Creator/broad builder]

Rules:
- Do not write code.
- Do not create a PRD.
- Do not create tasks or implementation plans.
- Do not tell me to paste secrets, credentials, private customer data, billing details, or sensitive personal data.
- Treat this workbook as evidence only.
- Recommend, but do not decide for me.

Start by asking me to describe the idea in plain English and why I want to build it.
```

## Stop Before You Paste Sensitive Information

Do not paste:

- secrets, tokens, passwords, API keys, or credentials
- dashboard values, billing details, payment data, or private customer data
- private raw transcripts unless you are comfortable sharing them
- sensitive personal data
- production configuration values

If something sensitive matters, use a safe placeholder:

```text
The product may use customer files, but I am not pasting real files here.
```

## Stage 1: Idea Canvas

Purpose: capture what you want to build and why you are motivated before the AI turns it into features.

### Prompts

- What do I think I want to build?
- Why do I care about this now?
- Who might benefit first?
- What would make this useful?
- What do I not want to build yet?

I know:

- 

I think:

- 

I need help deciding:

- 

### Lens Prompts

Operator/PM:

- The workflow or product surface I understand is:
- The business, team, customer, or career value might be:

Solo B2B founder:

- The customer I want to help is:
- The customer-ready outcome I want to reach is:

Creator/broad builder:

- The skill or product sense I want to practice is:
- The useful experience I want to show is:

### Self-Check

Continue when you can say the idea in one plain sentence and name why it matters to you.

Do not continue if the idea is only a feature list with no person, situation, or motivation.

### Precode Translation Notes

- Product idea summary:
- Chosen lens:
- Motivation:
- Not-yet list:

## Stage 2: Light Discovery Canvas

Purpose: find the real person, painful moment, current alternative, and riskiest assumption before writing a hypothesis.

Light discovery is not market proof. It is just enough reality to stop the idea from floating.

### Prompts

- Who is the real person or group in a real situation?
- What just happened before they need help?
- What do they do today instead?
- What works about the current way?
- What breaks, wastes time, costs money, creates stress, or blocks progress?
- What is the riskiest thing I am assuming?

I know:

- 

I think:

- 

I need help deciding:

- 

### Lens Prompts

Operator/PM:

- The internal workflow, product surface, stakeholder, or customer moment is:
- The current workaround inside the team or company is:
- The ROI might be time saved, fewer errors, better handoff, better customer experience, consulting value, or career edge:

Solo B2B founder:

- The reachable customer segment is:
- The current workaround, substitute, or "do nothing" behavior is:
- The strongest sign of urgency is:

Creator/broad builder:

- The audience, community, or personal situation is:
- The current way people learn, create, decide, or complete this task is:
- The learning or usefulness assumption is:

### Optional Tool Card: Last-Time Question

Use this when the pain is vague.

```text
Ask me about the last time this problem happened. Focus on what triggered it, what the person did first, what they tried, what broke, and what happened next. Do not ask whether they like my idea.
```

### Self-Check

Continue when you can name:

- the person or context
- the painful moment
- the current alternative
- the riskiest assumption

Pause if your strongest evidence is only "I think this would be cool" and you cannot name a current alternative.

### Precode Translation Notes

- Target user and situation:
- Painful moment:
- Current alternative or workaround:
- Strongest evidence:
- Weakest assumption:

## Stage 3: 4Ps Hypothesis Canvas

Purpose: turn the idea into one testable bet.

The 4Ps are plain-language product scaffolding:

- Persona: who this is for
- Problem: what painful moment they face
- Promise: what gets better
- Product: the smallest product shape that could deliver the promise

### Prompts

Persona:

- 

Problem:

- 

Promise:

- 

Product:

- 

One-sentence hypothesis:

```text
For [persona] who struggle with [problem], this product promises [better outcome] by giving them [small product shape].
```

### Lens Prompts

Operator/PM:

- Persona may be a role, team, stakeholder, customer type, or operator you understand.
- Product may be a workflow helper, dashboard, triage tool, internal assistant, decision aid, or customer-facing improvement.

Solo B2B founder:

- Persona should be a reachable buyer, user, or champion.
- Product should be narrow enough to become a customer-ready MVP.

Creator/broad builder:

- Persona may be an audience, peer group, creator type, or yourself as a first user.
- Product should still deliver a complete useful moment, not only a demo of technology.

### Optional Tool Card: Make It Testable

Use this when the 4Ps sound too broad.

```text
Review my 4Ps. Make each one more specific without adding new features. Name the part that is still too vague, the assumption I am making, and one better version of the hypothesis.
```

### Self-Check

Continue when the 4Ps describe one bet. Do not continue if they describe three different products, audiences, or promises.

### Precode Translation Notes

- Persona:
- Problem:
- Promise:
- Product shape:
- Riskiest hypothesis:

## Stage 4: Context Selection Canvas

Purpose: understand the real-world context where the first version has to make sense.

This is not investor market sizing. It is context for better product judgment.

### Prompts

- What category, workflow, market, organization, audience, or community does this live inside?
- What do people use today instead?
- Who decides whether the product is worth trying?
- Who actually uses it?
- What would make this context hard to enter?
- What makes this context a good first place to learn?

I know:

- 

I think:

- 

I need help deciding:

- 

### Lens Prompts

Operator/PM: organization or workflow context

- Team, department, client, or product area:
- Stakeholders affected:
- Existing tools or process:
- Approval, data, privacy, compliance, or adoption concerns:
- Business or career ROI:

Solo B2B founder: market context

- B2B segment:
- Buyer, user, and champion:
- Current solutions or competitors:
- Budget, urgency, switching effort, or willingness-to-try signal:
- First reachable customer path:

Creator/broad builder: audience or category context

- Audience, community, or category:
- Current tools, habits, or content formats:
- Why this group would care:
- What would make it shareable, useful, or worth returning to:
- What is enough for a learning-first build:

### Optional Tool Card: Alternatives Map

| Current alternative | What works | What breaks | Why people keep using it |
|---|---|---|---|
|  |  |  |  |

### Self-Check

Continue when you can name the context and at least one current alternative. Do not continue if the context is "everyone" or "any company" without a narrower first arena.

### Precode Translation Notes

- Context type:
- Current alternatives:
- User/buyer/stakeholder notes:
- Adoption or switching concern:

## Stage 5: Positioning Canvas

Purpose: focus the product before defining workflows.

Positioning answers:

- who it is for
- what it replaces or improves
- why this first version deserves to exist
- what it should not claim yet

### Prompts

- This is for:
- It helps them when:
- It replaces or improves:
- It is different because:
- It is not:
- The first version deserves to exist because:

I know:

- 

I think:

- 

I need help deciding:

- 

### Lens Prompts

Operator/PM:

- Career-edge claim I should be careful with:
- Business/workflow value I can credibly claim:

Solo B2B founder:

- Customer-ready promise I can credibly test:
- Claim I should avoid until I have more evidence:

Creator/broad builder:

- Learning or usefulness promise:
- Claim I should avoid because this is still a learning build:

### Optional Tool Card: One-Line Positioning

```text
Help me write three plain-language positioning lines for this idea. Each line should name who it is for, what situation it helps with, and what better outcome it creates. Do not use hype or unsupported claims.
```

### Self-Check

Continue when the positioning makes the product smaller and clearer. Pause if it makes the product sound bigger, more polished, or more validated than the evidence supports.

### Precode Translation Notes

- For:
- Replaces/improves:
- First-version reason:
- Claims to avoid:
- Non-goals:

## Stage 6: Visible Iteration Canvas

Purpose: make the idea visible before defining the core workflow.

Use a sketch, rough screen, clickable mockup, AI-generated concept, storyboard, spreadsheet, paper flow, or throwaway prototype. The goal is not polish. The goal is to see what changes when the idea becomes visible.

### Prompts

- What did I make visible?
- What did I notice only after seeing it?
- What confused me or someone else?
- What became smaller, simpler, or more important?
- What should move to not-yet?
- What should stay in the first version?

I know:

- 

I think:

- 

I need help deciding:

- 

### Lens Prompts

Operator/PM:

- Which workflow step became clearer?
- Which stakeholder concern appeared?
- Which internal adoption or handoff risk appeared?

Solo B2B founder:

- Which customer value moment became clearer?
- Which feature now feels unnecessary for the first customer-ready version?
- Which trust or credibility concern appeared?

Creator/broad builder:

- Which part became more fun, useful, or understandable?
- Which part is only showing off technology?
- Which part teaches the skill I came to practice?

### Optional Tool Card: Three Directions

```text
Give me three rough directions for making this idea visible. For each direction, name the main user action, the layout or flow idea, one thing that might be confusing, and what I would learn by trying it.
```

### Self-Check

Continue when you have changed at least one product decision because the idea became visible. If nothing changed, name that honestly and move on instead of forcing more iteration.

### Precode Translation Notes

- Visible artifact:
- Feedback or critique used:
- Decision changed:
- Defer / not-yet items:

## Stage 7: Core Workflow Spine Canvas

Purpose: define the few essential user actions required to receive value.

The spine is not the whole product. It is the smallest meaningful path through the experience.

### Prompts

- Trigger: what makes the user start?
- First action: what do they do first?
- Key steps: what must happen next?
- Feedback: how does the product show progress, confidence, or next action?
- Completion: what tells the user they got value?
- Return path: why or when would they come back?

### Workflow Spine

| Spine step | User action | Product response | What value or confidence this creates |
|---|---|---|---|
| Trigger |  |  |  |
| First action |  |  |  |
| Key step 1 |  |  |  |
| Key step 2 |  |  |  |
| Completion |  |  |  |
| Return path |  |  |  |

### Lens Prompts

Operator/PM:

- The workflow starts when:
- The handoff, decision, or internal output must be:
- The stakeholder needs confidence because:

Solo B2B founder:

- The customer starts when:
- The value moment they would pay, switch, or return for is:
- The first version must feel trustworthy because:

Creator/broad builder:

- The experience starts when:
- The useful or delightful payoff is:
- The thing I want to demonstrate or learn is:

### Optional Tool Card: Remove One Step

```text
Review my workflow spine. Find one step that may be unnecessary for the first version, one missing feedback moment, and one place the user might get stuck.
```

### Self-Check

Continue when the spine can be completed by a real user without needing the whole imagined product.

Pause if the spine depends on too many integrations, roles, dashboards, admin tools, or future features.

### Precode Translation Notes

- Trigger:
- Core user actions:
- Completion moment:
- Return path:
- Likely screens or surfaces:

## Stage 8: Minimum Valuable Experience Canvas

Purpose: define the smallest complete value experience worth building first.

An MVE is not the tiniest demo and not the whole MVP. It is the smallest end-to-end experience that delivers one real payoff.

### Prompts

- The MVE user is:
- The MVE helps them when:
- The complete value moment is:
- The first version includes:
- The first version excludes:
- The success signal is:
- The main risk is:
- The smallest safe build boundary is:

I know:

- 

I think:

- 

I need help deciding:

- 

### Lens Prompts

Operator/PM:

- Smallest workflow improvement someone at work could evaluate:
- Business, team, consulting, or career ROI signal:
- Stakeholder, data, privacy, or approval risk:

Solo B2B founder:

- Smallest customer-ready value path:
- Customer validation or willingness-to-try signal:
- Trust, payment, data, or adoption risk:

Creator/broad builder:

- Smallest complete useful experience:
- Learning or audience signal:
- Scope risk that would make this stop being a learning build:

### Optional Tool Card: MVE Skeptical Friend Check

```text
Challenge my MVE. Tell me whether it is too big, too small to be valuable, too vague to build, or too risky for a first version. Sort concerns into Must decide now, Good enough for first build, and Defer / Not yet.
```

### Self-Check

Continue when the MVE names one user, one complete value moment, explicit non-goals, one success signal, and the main risk.

Do not continue if the MVE is only a feature list or if it requires the full imagined product to be useful.

### Precode Translation Notes

- MVE statement:
- Included:
- Excluded:
- Success signal:
- Risk or sensitive surface:

## Stage 9: Conviction Packet / Precode Ingestion Packet

Purpose: package the stable, decision-relevant material for Precode Local Source Intake.

This packet is not a PRD, feature list, roadmap, backlog, or implementation plan. It helps Precode understand the product intent before shaping requirements. In beginner and bootcamp contexts, it should show MVP-ready conviction: intended user, current workaround or evidence, strongest evidence, weakest assumption, smallest first slice, not-yet scope, and smallest learning step.

### Final Packet

Product idea summary:

- 

Chosen lens:

- `operator_pm | solo_b2b_founder | creator_builder`

Motivation:

- 

Persona:

- 

Problem:

- 

Promise:

- 

Product shape:

- 

Context:

- 

Current alternatives or workarounds:

- 

Strongest evidence:

- 

Weakest assumption:

- 

Visible iteration summary:

- 

Core workflow spine:

- Trigger:
- First action:
- Key steps:
- Feedback:
- Completion:
- Return path:

Minimum Valuable Experience:

- 

Included in the first version:

- 

Explicitly not included yet:

- 

Success signal:

- 

Risks or sensitive surfaces:

- 

Open questions:

- 

Recommended next Precode path:

- `Local Source Intake`

Guardrail reminder:

```text
This Conviction Packet is evidence only. It is not a PRD, not a task list, not approval to update PRODUCT.md, and not permission to code. Use Local Source Intake before PRD shaping or implementation.
```

## Handoff Prompt

When the packet is ready, bring it into Precode with this prompt:

```text
Use Local Source Intake on this Student Idea To MVE Workbook packet.

Treat the packet as source evidence only. Summarize stable conclusions, assumptions, open questions, risks, and likely owner files. Do not update PRODUCT.md, draft a PRD, create beads, activate work, or write code until I review the intake summary.
```

## Experience Design Handoff

In a bootcamp flow, this workbook or the approved bootcamp PRD input usually feeds an Experience design step before Claude Code implementation.

Use Claude Design, Ember UI Builder, or another AI-assisted UI/UX canvas to make the core spine visible: the primary workflow that delivers the minimum value moment to the target user.

Use `tasks/templates/STUDENT-EXPERIENCE-INGESTION-PACKET.md` after the Experience artifact exists. That packet combines the approved PRD input and Experience artifacts so Claude Code can create one bounded Precode bead before coding begins.
