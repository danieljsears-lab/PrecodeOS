# Product Ideation Workbook
<!-- ANCHOR: product-ideation-workbook -->

> AUTHORITY: Reusable student workbook for gathering product thoughts, research, assumptions, risks, and feature candidates before Precode Local Source Intake.
> NOT_AUTHORITY: Product decisions, approved requirements, active task selection, `PRODUCT.md` content, PRD approval, implementation plans, or generated progress state.
> LOAD_WHEN: A new user or student wants to research, ideate, refine, and package a product idea with Claude or Codex before ingesting it into Precode.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears
Document version: v0.1.1
Last updated: 2026-05-08

## Purpose

Use this workbook before you ask Precode to update `PRODUCT.md`, write a PRD, or create implementation work.

This workbook helps you gather your thoughts offline with Claude or Codex as a thinking coach. It helps you research, explain, challenge, and narrow your idea so Precode can later ingest a clean summary through Local Source Intake.

Important rule: this workbook is evidence, not authority. Nothing in this file becomes true for the project until you review it and Precode promotes stable conclusions into the right owner file.

## How This Workbook Thinks

You do not need product-management vocabulary to use this workbook. You only need to keep asking a few useful questions in plain English:

- Who is this really for?
- What hurts today?
- What do they do instead?
- What changes after?
- What must not be built yet?
- What would prove this is useful?
- What could make this a bad idea?

The workbook includes optional tool cards. Use them when a section feels fuzzy or too broad. Skip them when your answer is already clear.

The tool cards are not extra homework. They are small thinking moves that help you turn a rough idea into a cleaner packet for Precode Local Source Intake.

## Stop Before You Paste Sensitive Information

Do not paste:

- secrets, tokens, passwords, API keys, or credentials
- dashboard values, billing details, payment data, or private customer data
- private raw transcripts unless you are comfortable sharing them
- sensitive personal data
- production configuration values

If something sensitive matters, write a safe placeholder such as:

```text
The app will use a payment provider, but I am not pasting keys or dashboard values here.
```

## How To Use This Workbook

Step 1. Make a copy of this workbook.

Give the copy a simple name, such as:

```text
my-product-idea-workbook.md
```

Step 2. Choose one product idea to explore.

Do not put every possible idea into one workbook. One workbook should cover one product concept or one major product direction.

Step 3. Open Claude or Codex and paste the thinking-coach prompt.

Use the prompt in the next section. Ask the agent to interview you, challenge assumptions, and organize your thinking. Do not let the agent decide the product for you.

Step 4. Fill out product-level sections first.

Start with the product promise, audience, jobs, pains, alternatives, non-goals, success signals, design/voice, and user language.

Follow the main path first. Use optional tool cards only when they help you clarify a real stuck point.

Step 5. Use Claude/Codex to research and cite sources.

Ask for source-cited summaries with links, dates, claims, confidence, and uncertainty. Research should help you think; it should not become authority by itself.

Step 6. Separate facts, assumptions, and open questions.

Use the fields:

- I know
- I think
- I need help deciding

Step 7. Challenge the idea before turning it into features.

Ask Claude or Codex to identify weak assumptions, missing user evidence, risky scope, vague success criteria, and reasons not to build yet.

Step 8. Fill out feature-level candidates.

Only after product framing and research are clear, list candidate features, before/after user moments, acceptance signals, risks, sensitive surfaces, dependencies, and first useful slices.

Step 9. Ask Claude/Codex to create the Precode Ingestion Packet.

Use the ingestion prompt near the end of this workbook. Keep the packet concise. Include a Candidate Goal Frame only when the durable direction is stable enough to review.

Step 10. Bring only the ingestion packet into Precode Local Source Intake.

When you are ready, ask Precode to ingest the packet as local source evidence. Do not ask Precode to edit `PRODUCT.md`, create a PRD, or activate work until you have reviewed the intake summary.

## Initial Direction

Use this section to capture your first plain-English direction before the workbook challenges or refines it.

This is not a Goal Frame yet. It is early evidence that may later become a Candidate Goal Frame for Precode review.

- What I think I want to build:
- Who it might help:
- Why now:
- What would make this useful:
- What I do not want to build yet:

## Copyable Claude/Codex Prompts

### Thinking-Coach Prompt

```text
Act as my product thinking coach for this workbook.

Help me research, ideate, challenge, and refine one product idea. Interview me one question at a time. Give me a recommended answer when useful, but do not decide for me. Use plain language, not product-management jargon. Separate what I know, what I think, and what I need help deciding. Challenge me gently when my idea is vague, too broad, unsupported, or risky. Do not write code. Do not create a PRD. Do not tell me to paste secrets, credentials, private customer data, dashboard values, billing details, or sensitive personal data.

Start by asking me to describe the product idea in plain English.
```

### Research Prompt

```text
Help me research this idea.

Give me source-cited summaries. For each source, include the link, date or recency if available, the claim it supports, confidence, uncertainty, and what question it helps answer. Do not treat research as proof that the idea is good. Help me identify what is evidence, what is assumption, and what still needs user validation.
```

### Challenge Prompt

```text
Challenge this idea before I turn it into features.

Identify weak assumptions, missing user evidence, risky scope, vague success criteria, privacy or safety concerns, sensitive surfaces, and reasons not to build yet. Keep the tone supportive and practical. Then recommend the smallest safe next learning step. Do not make the decision for me.
```

### Refinement Prompt

```text
Help me refine this into product and feature candidates.

Summarize the product promise, intended user, user job, painful before moment, better after moment, non-goals, success signals, design or voice notes, and first feature candidates. Keep product-level ideas separate from feature-level ideas.
```

### Precode Ingestion Packet Prompt

```text
Create a concise Precode Ingestion Packet from this workbook.

Treat the workbook as evidence, not authority. Do not draft PRODUCT.md. Do not create a PRD. Do not propose active work. Summarize only the stable and decision-relevant material.

Use this format:
- Product idea summary:
- Intended user and job:
- Problem or pain evidence:
- Source-cited research summary:
- Strongest evidence:
- Weakest assumption:
- Stable facts:
- Assumptions:
- Open questions:
- Candidate product constitution updates:
- Candidate feature or PRD ideas:
- Candidate non-goals:
- Smallest useful version:
- Not-yet list:
- Success signals:
- Risks and sensitive surfaces:
- Candidate Goal Frame For Precode Review:
  - Goal:
  - Why now:
  - Success signal:
  - Out of scope:
  - Approval gates:
  - Reaffirmation trigger:
  - Suggested owner file:
- PRD bridge notes:
- Likely owner files:
- Recommended Precode next step:

End with: "The Candidate Goal Frame is evidence only. It is not a Goal Frame yet, not a plan, not a task list, and not permission to update PRODUCT.md. Do not edit PRODUCT.md or create a PRD until the user reviews this intake summary."
```

## Product-Level Thinking

Use this section for thoughts that might later affect `PRODUCT.md`.

### Tool Card: The Real Person Test

Use this when your audience sounds broad, such as "small businesses," "students," or "busy people."

Try to describe one real kind of person in a real situation:

- They are:
- They are trying to:
- They are frustrated because:
- They use these words:
- They would care about this now because:

PRD bridge: this later helps a PRD explain the user and the job without guessing.

### Product Promise

What is the product, in plain English?

Examples:

- A scheduling helper for independent tutors.
- A small dashboard for a local nonprofit.
- A checklist app for new Airbnb hosts.
- A tool that helps students turn class notes into study plans.

I know:

- 

I think:

- 

I need help deciding:

- 

### Audience And User Jobs

Who is this for, and what job are they trying to get done?

Examples:

- Busy parents trying to compare after-school programs.
- Solo consultants trying to follow up with leads.
- Teachers trying to see which students need help.
- Hobby sellers trying to track orders without a full ecommerce system.

I know:

- 

I think:

- 

I need help deciding:

- 

Optional Real Person Test:

- The first person I would want to help is:
- The situation they are in is:
- The task they are trying to finish is:
- The reason this matters to them now is:

### Pain, Constraint, Or Opportunity

What is hard, confusing, slow, risky, expensive, or annoying for the user today?

I know:

- 

I think:

- 

I need help deciding:

- 

### Tool Card: The Painful Moment

Use this when the idea sounds useful, but the pain is still vague.

Describe the moment right before the user would want help:

- What just happened?
- What are they trying to finish?
- What is slowing them down?
- What mistake, delay, cost, or stress are they trying to avoid?
- What would they say out loud in that moment?

PRD bridge: this later helps a PRD explain the before moment and why the feature matters.

Painful moment:

- 

What the user says in that moment:

- 

### Current Alternatives

What do users do today instead?

Examples:

- Spreadsheet.
- Notes app.
- Text messages.
- Email threads.
- Expensive software with too many features.
- Manual work.

I know:

- 

I think:

- 

I need help deciding:

- 

### Tool Card: The Current Workaround Map

Use this when you are not sure whether the idea solves a real problem.

List what users do today, even if it is messy:

| Current workaround | What works about it | What breaks, wastes time, or feels painful | Why users still use it |
|---|---|---|---|
|  |  |  |  |

PRD bridge: this later helps a PRD explain alternatives considered and why the product should exist.

### Tool Card: The Before/After Flip

Use this when the product promise feels too abstract.

Write one sentence for each side:

- Before this product, the user:
- After this product, the user:

The after sentence should describe a real outcome, not a feature list.

PRD bridge: this later helps a PRD define what changes for the user.

Before:

- 

After:

- 

### Strategy And Non-Goals

What should this product not become right now?

Examples:

- Not a social network.
- Not a marketplace.
- Not an enterprise admin system.
- Not a mobile app yet.
- Not using payments in the first version.

I know:

- 

I think:

- 

I need help deciding:

- 

### Tool Card: The Not-Yet List

Use this when the idea is starting to grow too many features.

Write down attractive ideas you are intentionally not building first:

| Not yet | Why it is tempting | Why it can wait |
|---|---|---|
|  |  |  |

PRD bridge: this later helps a PRD protect non-goals and keep the first version small.

### Success Signals

What would make you believe this product is useful?

Examples:

- A user comes back twice in one week.
- A user replaces a spreadsheet with the tool.
- A user saves 30 minutes.
- A user can finish the task without asking for help.
- A user says, "This is exactly what I was trying to do."

I know:

- 

I think:

- 

I need help deciding:

- 

### Tool Card: The First Success Signal

Use this when success sounds too big, such as "get users" or "make money."

Choose one early sign that a real person got value:

- A user finishes:
- A user returns to:
- A user replaces:
- A user saves:
- A user says:

PRD bridge: this later helps a PRD define acceptance signals and learning goals.

### Design, Voice, And Feel

What should the product feel like?

Examples:

- Calm and focused.
- Practical and direct.
- Warm and encouraging.
- Professional and quiet.
- Playful but not childish.

What should it not feel like?

Examples:

- Cluttered.
- Corporate.
- Generic.
- Overdesigned.
- Like a complicated dashboard.

I know:

- 

I think:

- 

I need help deciding:

- 

### Words Users Say

Write the words your users would naturally use.

Examples:

- "follow-up" instead of "CRM task"
- "student check-in" instead of "intervention workflow"
- "booking request" instead of "lead intake"
- "trip plan" instead of "itinerary object"

I know:

- 

I think:

- 

I need help deciding:

- 

## Stop Before Continuing: Product Framing Check

Before moving to features, ask Claude or Codex:

```text
Review my product-level answers. Tell me what is clear, what is assumed, what is missing, and what would change the product direction. Do not suggest features yet unless the product framing is clear enough.

Reality check: gently challenge the idea. Name the biggest reason this might not be worth building yet, the clearest user pain, and the one answer that would most improve the idea.
```

Continue only when you can explain:

- who the product is for
- what job or pain it addresses
- what it should not become yet
- what would count as useful

## Research And Evidence

Use this section for research, quotes, observations, links, and uncertainty.

### Tool Card: The Evidence Ladder

Use this to avoid treating every signal as equally strong.

Evidence usually gets stronger as it moves down this ladder:

1. Your personal hunch.
2. Online research or category notes.
3. A user quote or observation.
4. A repeated pattern across several users or sources.
5. A user trying a workaround, paying, returning, or changing behavior.

You do not need perfect proof. You do need to know what kind of evidence you have.

Strongest evidence so far:

- 

Weakest evidence so far:

- 

PRD bridge: this later helps a PRD separate problem evidence from assumptions.

### Source-Cited Research

| Source link or title | Date or recency | Claim or fact | Confidence | Uncertainty |
|---|---|---|---|---|
|  |  |  | high / medium / low |  |

### User Quotes Or Observations

Do not paste private raw transcripts unless you are comfortable sharing them. Short approved summaries are better.

| Source | Quote or summary | What it suggests | Confidence |
|---|---|---|---|
|  |  |  | high / medium / low |

### Competitor Or Context Notes

Examples:

- Existing tools are too expensive.
- Existing tools solve the wrong user job.
- Users already have a workaround.
- The category has trust or privacy concerns.

I know:

- 

I think:

- 

I need help deciding:

- 

### Conflicts And Uncertainty

What evidence points in different directions?

I know:

- 

I think:

- 

I need help deciding:

- 

### Tool Card: The Must-Be-True List

Use this before you turn research into conclusions.

For this idea to be worth building, what must be true?

Examples:

- Users have this problem often enough.
- The current workaround is painful enough.
- Users trust a tool with this information.
- The first version can help without a complicated integration.
- A user would try this before it is perfect.

| Must be true | What evidence supports it? | What could prove it wrong? | Confidence |
|---|---|---|---|
|  |  |  | high / medium / low |

PRD bridge: this later helps a PRD name risks, assumptions, and open questions.

## Stop Before Continuing: Research Check

Before turning research into conclusions, ask Claude or Codex:

```text
Review the research. Separate source-supported claims from assumptions. Name the weakest evidence, the biggest uncertainty, and the claims I should not treat as true yet.

Reality check: gently challenge my confidence. What am I treating as proven that is still only a guess? What is the smallest next step that would reduce the biggest uncertainty?
```

Continue only when you know which claims are supported, which are assumptions, and which questions still need validation.

## Feature-Level Thinking

Use this section for ideas that might later become PRD inputs. Do not treat them as approved features yet.

### Candidate Features

| Feature idea | User before moment | User after moment | Why it might matter | Confidence |
|---|---|---|---|---|
|  |  |  |  | high / medium / low |

### First Useful Slice

What is the smallest version that could teach you something real?

Examples:

- A local checklist before accounts.
- One upload flow before a full file library.
- Manual export before automated integrations.
- Read-only dashboard before editable settings.
- One role before role-based permissions.

I know:

- 

I think:

- 

I need help deciding:

- 

### Tool Card: The Smallest Useful Version

Use this when the first version feels too big.

Make the first version smaller without making it pointless:

- One user type before many user types.
- One workflow before the whole system.
- One manual step before automation.
- One useful result before a full dashboard.
- One narrow data type before every possible data type.

The smallest useful version should still create a real before/after change for the user.

PRD bridge: this later helps a PRD propose the first narrow implementation slice.

Smallest useful version:

- 

What it intentionally leaves out:

- 

### Candidate Acceptance Signals

How would you know a feature works?

Examples:

- A user can create, edit, and delete one item.
- A user can complete the flow without help.
- The page works on mobile.
- The form prevents missing required information.
- The result can be checked manually.

I know:

- 

I think:

- 

I need help deciding:

- 

### Tool Card: The Skeptical Friend Check

Use this when the idea feels exciting but untested.

Imagine a thoughtful friend wants to protect your time and money. What would they ask?

- Who exactly needs this?
- What do they already do?
- Why would they switch?
- What is the riskiest part?
- What would make you pause?
- What is the smallest thing you can test first?

Your answers:

- 

PRD bridge: this later helps a PRD name reasons not to build yet and unresolved questions.

### Risks And Sensitive Surfaces

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

Notes:

- 

### Tool Card: The Trust Surface Check

Use this when the product touches accounts, money, personal data, files, outside services, or important decisions.

Ask:

- What information would users trust this product with?
- What could go wrong if the product is confusing or wrong?
- What should require a human approval before implementation?
- What should not be included in the first version?

Trust notes:

- 

PRD bridge: this later helps a PRD name sensitive surfaces and approval gates.

### Dependencies And Unknowns

What might block implementation?

Examples:

- Need a design decision.
- Need dashboard setup.
- Need sample data.
- Need permission to use an API.
- Need to decide whether this requires accounts.
- Need a manual test path.

I know:

- 

I think:

- 

I need help deciding:

- 

## Stop Before Continuing: Feature Shaping Check

Before creating the ingestion packet, ask Claude or Codex:

```text
Review the feature candidates. Tell me which are product-level ideas, which are feature-level ideas, which are too broad, which touch sensitive surfaces, and which could be the smallest first useful slice.

Reality check: gently challenge the scope. What would make this first version too large, too risky, or too hard to verify? What should move to the not-yet list?
```

Continue only when the first useful slice is narrow enough to explain in plain English.

## Precode Ingestion Packet

Ask Claude or Codex to produce the final packet with the prompt above, then paste the result here.

### Final Packet

```text
Product idea summary:

Intended user and job:

Problem or pain evidence:

Source-cited research summary:

Strongest evidence:

Weakest assumption:

Stable facts:

Assumptions:

Open questions:

Candidate product constitution updates:

Candidate feature or PRD ideas:

Candidate non-goals:

Smallest useful version:

Not-yet list:

Success signals:

Risks and sensitive surfaces:

Candidate Goal Frame For Precode Review:
- Goal:
- Why now:
- Success signal:
- Out of scope:
- Approval gates:
- Reaffirmation trigger:
- Suggested owner file:

PRD bridge notes:

Likely owner files:

Recommended Precode next step:

The Candidate Goal Frame is evidence only. It is not a Goal Frame yet, not a plan, not a task list, and not permission to update PRODUCT.md. Do not edit PRODUCT.md or create a PRD until the user reviews this intake summary.
```

## Stop Before Continuing: Precode Ingestion Check

Before bringing the packet into Precode, confirm:

- The packet is shorter than the full workbook.
- The packet separates facts, assumptions, and open questions.
- Research claims include source links when available.
- Product-level candidates and feature-level candidates are separated.
- The strongest evidence and weakest assumption are named.
- The smallest useful version and not-yet list are included.
- The Candidate Goal Frame is clearly marked as evidence only and does not read like a task list.
- PRD bridge notes explain what a future PRD may need, without drafting the PRD.
- Sensitive information has been removed.
- You are ready for Precode to treat the packet as local source evidence, not authority.

When ready, ask Precode:

```text
Use Local Source Intake on this Precode Ingestion Packet.

Treat it as evidence, not authority. Summarize stable facts, assumptions, conflicts, open questions, candidate product constitution updates, Candidate Goal Frame stability, candidate PRD inputs, likely owner files, and recommended next step. Do not edit PRODUCT.md, create a PRD, create beads, or start coding until I review the intake summary.
```
