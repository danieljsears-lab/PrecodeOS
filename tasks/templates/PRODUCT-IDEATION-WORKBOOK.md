# Product Ideation Workbook
<!-- ANCHOR: product-ideation-workbook -->

> AUTHORITY: Reusable student workbook for gathering product thoughts, research, assumptions, risks, and feature candidates before Precode Local Source Intake.
> NOT_AUTHORITY: Product decisions, approved requirements, active task selection, `PRODUCT.md` content, PRD approval, implementation plans, or generated progress state.
> LOAD_WHEN: A new user or student wants to research, ideate, refine, and package a product idea with Claude or Codex before ingesting it into Precode.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears
Document version: v0.1.6
Last updated: 2026-05-19

## Purpose

Use this workbook before you ask Precode to update `PRODUCT.md`, write a PRD, or create implementation work for a net-new, rough product idea.

This workbook helps you gather your thoughts offline with Claude or Codex as a thinking coach. It helps you research, explain, challenge, and narrow your idea so Precode can later ingest a clean summary through Local Source Intake.

Important rule: this workbook is evidence, not authority. Nothing in this file becomes true for the project until you review it and Precode promotes stable conclusions into the right owner file.

Bypass this workbook for bugs, maintenance, approved PRD follow-through, narrow feature changes, and other work where the product problem and scope are already clear.

## How This Workbook Thinks

You do not need product-management vocabulary to use this workbook. You only need to keep asking a few useful questions in plain English:

- Who is this really for?
- What hurts today?
- What do they do instead?
- What evidence says this problem is real?
- What changes after?
- What must not be built yet?
- What would make this worth defining, testing, or building?
- What could make this a bad idea?

The workbook includes optional tool cards. Use them when a section feels fuzzy or too broad. Skip them when your answer is already clear.

The tool cards are not extra homework. They are small thinking moves that help you turn a rough idea into a cleaner packet for Precode Local Source Intake.

## Three Questions, Then A Product Brief

To reduce overwhelm, the first pass should not feel like a long interview or technical test. After at most three high-level product or business questions, ask the agent to summarize progress as a Product Brief and ask one next best question.

The Product Brief is evidence only. It does not approve a PRD, create beads, update `PRODUCT.md`, or permit coding.

Product Brief:

- Product idea:
- Intended user:
- Painful before moment:
- Better after moment:
- Current workaround or evidence:
- Assumptions:
- Not-yet list:
- Smallest useful version:
- Next best question:

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

Use the prompt in the next section. Ask the agent to interview you, challenge assumptions, and organize your thinking. After at most three high-level questions, make it produce a Product Brief so you can see progress before deeper discovery. Do not let the agent decide the product for you.

If you are in a bootcamp or sprint setting, paste the Bootcamp MVP Context Preamble first. It tells the agent to keep useful challenge, but stop expanding the idea beyond a small first version.

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

Ask Claude or Codex to identify weak assumptions, missing user evidence, risky scope, vague success criteria, current alternatives, demand or pricing signals, and reasons not to build yet. For a 4-week MVP, ask it to separate blockers from concerns that can move to the not-yet list.

Step 8. Use the Exploration Loop when you already have notes to reuse.

The Exploration Loop is for Product Briefs, workbook notes, rough feature lists, research snippets, user quotes, chat summaries, screenshots, sketches, Candidate Goal Frames, or not-yet ideas that should shape the next question. It should help you notice missing angles, weak assumptions, overlooked users, hidden risks, smaller slices, and capability ideas you had not considered. It should not ask you to repeat content already present.

Step 9. Use Purposeful Ideation tool cards when the idea still feels fuzzy, too broad, too obvious, or too large.

Paste your rough idea into the `Context` line. Let the agent ask questions. You choose the direction.

Step 10. Fill out feature-level candidates.

Only after product framing and research are clear, list candidate features, before/after user moments, acceptance signals, risks, sensitive surfaces, dependencies, and first useful slices.

Step 11. Ask Claude/Codex to create the Precode Ingestion Packet.

Use the ingestion prompt near the end of this workbook. Keep the packet concise. Include a Candidate Goal Frame only when the durable direction is stable enough to review.

Step 12. Bring only the ingestion packet into Precode Local Source Intake.

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

### Bootcamp MVP Context Preamble

Paste this before a workbook, ideation, challenge, refinement, or ingestion prompt when you are trying to shape a small first version for a 4-week bootcamp project.

```text
Context for this session:
I am a beginner building a 4-week MVP, not a polished company-scale product.

Help me make the idea concrete, small, and safe enough to move forward. Challenge only the issues that would change what I should build or validate in the next 4 weeks. Do not expand the scope, add enterprise features, invent future platform requirements, or keep poking holes after the first version is good enough to define.

Sort concerns into:
- Must decide now:
- Good enough for MVP:
- Defer / Not yet:

Treat this workbook as evidence, not authority. Do not edit PRODUCT.md, create a PRD, create beads, or write code. Recommend, but do not decide for me.
```

### Close-The-Loop Prompt

Use this when Claude or Codex keeps challenging, widening scope, or asking questions after the useful decision is clear enough.

```text
Stop challenging and produce the requested output now.

Only ask another question if the answer would prevent an unsafe, impossible, misleading, or implementation-changing output. Move all non-blocking concerns to Defer / Not yet. Keep the output beginner-safe, concrete, and scoped to a 4-week MVP.

Remember: this workbook is evidence, not authority. Do not edit PRODUCT.md, create a PRD, create beads, or write code.
```

### Thinking-Coach Prompt

```text
Act as my product thinking coach for this workbook.

Help me research, ideate, challenge, and refine one product idea. Interview me one question at a time. Give me a recommended answer when useful, but do not decide for me. Use plain language, not product-management jargon. Separate what I know, what I think, and what I need help deciding. Challenge me gently when my idea is vague, too broad, unsupported, or risky. Do not write code. Do not create a PRD. Do not tell me to paste secrets, credentials, private customer data, dashboard values, billing details, or sensitive personal data.

After at most three high-level product or business questions, summarize progress as a Product Brief with: product idea, intended user, painful before moment, better after moment, current workaround or evidence, assumptions, not-yet list, smallest useful version, and next best question.

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

Identify weak assumptions, missing user evidence, risky scope, vague success criteria, privacy or safety concerns, sensitive surfaces, and reasons not to build yet. Sort them into Must decide now, Good enough for MVP, and Defer / Not yet. Keep the tone supportive and practical. Then recommend the smallest safe next learning step. Do not make the decision for me.
```

### Exploration Loop Prompt

Use this when you already have content from this workbook, a Product Brief, rough feature list, research, user quotes, screenshots, sketches, chat summaries, a Candidate Goal Frame, or not-yet ideas.

```text
Use the Exploration Loop on the content I already have.

First summarize what is already known from my notes: users, pains, goals, candidate features, evidence, assumptions, risks, and not-yet ideas. Do not ask me to repeat information already present.

Then help me discover what I have not considered yet. Ask one targeted question at a time only when the answer could change the product direction, evidence strength, first useful slice, risk, or PRD readiness.

Look especially for:
- a user or situation I have overlooked
- a painful before moment that is still vague
- a current workaround or competing behavior
- a trust, privacy, cost, effort, or safety risk
- a smaller first slice
- a reason this may not be worth building yet
- a capability that supports the user outcome better than the obvious feature

Translate user moments into capability candidates, not approved features. Sort concerns into Must decide now, Good enough for MVP, and Defer / Not yet.

End with an Exploration Evidence Packet:
- Existing content used:
- Product idea in plain English:
- Intended user and situation:
- Painful before moment:
- Better after moment:
- Current workaround or evidence:
- New things discovered during the loop:
- Capability candidates:
- Overlooked alternatives or adjacent ideas:
- Weakest assumptions:
- Risks or sensitive surfaces:
- Not-yet list:
- Smallest useful MVP slice:
- Smallest learning step:
- Recommended next Precode path:

Then include this compact matrix:

| Candidate capability | User moment | Existing evidence | New insight | Risk | MVP fit | Recommendation |
|---|---|---|---|---|---|---|

Treat the output as evidence only. Do not call it a feature list, roadmap, backlog, requirements, or PRD. Do not write a PRD, create beads, update PRODUCT.md, or code.
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
- Current alternatives or workarounds:
- Evidence strength:
- Demand or pricing signal:
- Smallest non-code learning step:
- What would change my mind:
- Exploration Loop summary:
- New things discovered during exploration:
- Capability candidates:
- Overlooked alternatives or adjacent ideas:
- Stable facts:
- Assumptions:
- Open questions:
- Candidate product constitution updates:
- Candidate feature or PRD ideas:
- Candidate non-goals:
- Smallest useful version:
- Not-yet list:
- Success signals:
- Purposeful ideation tools used:
- Constraint chosen:
- Main contradiction or tradeoff:
- Lateral move or surprising connection:
- Riskiest hypothesis:
- Options intentionally not pursued:
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

### Tool Card: The Demand Signal Check

Use this when the idea might become a business, paid feature, public product, or significant time investment.

Look for evidence that costs the user something: time, money, switching effort, signup intent, repeated return, referral, or willingness to pay.

| Possible demand signal | What happened? | What it suggests | Confidence |
|---|---|---|---|
| User spends time on a workaround |  |  | high / medium / low |
| User pays for a partial solution |  |  | high / medium / low |
| User signs up, joins a waitlist, or asks for access |  |  | high / medium / low |
| User changes behavior after seeing a prototype or promise |  |  | high / medium / low |

PRD bridge: this later helps a PRD explain whether the idea has demand evidence or only interest.

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

Evidence strength:

- `very weak | weak | medium | strong | strongest`

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

### Tool Card: The Smallest Non-Code Learning Step

Use this when you are tempted to build before you know whether the idea is worth defining.

Choose the smallest way to learn without writing product code:

- interview three people who recently had the problem
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

PRD bridge: this later helps Precode decide whether to run Product Discovery Validation, Local Source Intake, or Idea-to-PRD.

## Stop Before Continuing: Research Check

Before turning research into conclusions, ask Claude or Codex:

```text
Review the research. Separate source-supported claims from assumptions. Name the weakest evidence, the biggest uncertainty, and the claims I should not treat as true yet.

Reality check: gently challenge my confidence. What am I treating as proven that is still only a guess? What is the smallest next step that would reduce the biggest uncertainty?
```

Continue only when you know which claims are supported, which are assumptions, and which questions still need validation.

## Exploration Loop

Use this when you already have material and want the agent to think with it before you commit to PRD shaping. The loop can use Product Briefs, workbook notes, rough feature lists, research snippets, user quotes, chat summaries, screenshots, sketches, Candidate Goal Frames, and prior not-yet ideas.

The agent should not ask you to repeat what is already in the notes. It should summarize the current shape, then ask only questions that could reveal a meaningful missing angle, weak assumption, overlooked user, hidden risk, smaller first slice, or better capability than the obvious feature.

Existing content used:

- 

What the idea seems to be becoming:

- 

New things discovered:

- 

Overlooked alternatives or adjacent ideas:

- 

Weakest assumptions:

- 

Must decide now:

- 

Good enough for MVP:

- 

Defer / Not yet:

- 

### Capability Candidate Matrix

These are candidate capabilities, not approved features, a backlog, requirements, or permission to code.

| Candidate capability | User moment | Existing evidence | New insight | Risk | MVP fit | Recommendation |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### Stop Before Continuing: Exploration Check

Before turning exploration into feature candidates, ask Claude or Codex:

```text
Review the Exploration Loop output. Tell me what reused prior content, what was newly discovered, what still feels like a guess, which capability candidates are strongest, and which ones should move to Defer / Not yet.

Reality check: was this loop actually useful, or did it only restate what I already knew? Name the one new insight, risk, narrowing move, or assumption that most changes what I should do next.
```

Continue only when the loop has produced at least one useful new insight, risk, narrowing move, or assumption. If it has not, close the loop and package the existing evidence instead of continuing to ask questions.

## Purposeful Ideation Tool Cards

Use these optional cards when you want Claude, Claude Code, ChatGPT, Codex, Gemini, or another agent to act as a thought partner before you turn the idea into features.

Paste your rough idea into the `Context` line. Let the agent ask questions. You choose the direction.

These cards guide ideation only. They do not create authority, approve PRDs, activate beads, or start implementation.

### Prompt Pattern

Use this reusable shape when you want a general-purpose prompt instead of a specific tool card.

```text
Act as my product thought partner.

Context:
[Paste my rough idea, notes, audience, or uncertainty.]

Task:
[Use this thinking tool to help me clarify the idea.]

Rules:
- Ask one question at a time if you need more information.
- Separate facts, assumptions, and open questions.
- Recommend, but do not decide for me.
- Do not write code, a PRD, or an implementation plan.
- Keep the output practical and beginner-friendly.

Output:
- What is clear:
- What is assumed:
- Best next question:
- Recommended direction:
- Smallest next step:
```

### Tool Card: Constraint Box

Purpose: Reduce overwhelm by choosing one useful limit.

Role: Student chooses the constraint; agent suggests tradeoffs.

Type: Narrowing / anti-overbuild.

Starting prompt:

```text
Act as my product thought partner.

Context:
[Paste my rough idea.]

Task:
Use a constraint lens to narrow this idea into a clearer first version.

Rules:
- Suggest 3 useful constraints, such as audience, deadline, platform, budget, workflow, data type, privacy boundary, or non-goal.
- Explain how each constraint changes the product.
- Recommend one constraint, but do not decide for me.
- Do not write a PRD or code.

Output:
- Constraint options:
- Recommended constraint:
- What this removes:
- What this makes clearer:
- Smallest useful first version:
```

### Tool Card: Jobs To Be Done

Purpose: Identify what progress the user is trying to make.

Role: Student describes the user; agent uncovers situation, job, workaround, and switching reason.

Type: User/job discovery.

Starting prompt:

```text
Act as my Jobs to Be Done coach.

Context:
[Paste my idea and who I think it is for.]

Task:
Help me understand the user's real job, not just the product idea.

Rules:
- Ask one question at a time if needed.
- Focus on a real situation, current workaround, desired progress, and reason to switch.
- Separate facts from assumptions.
- Do not suggest features yet.

Output:
- Target user:
- Situation that triggers the need:
- Job they are trying to do:
- Current workaround:
- Why they might switch:
- Biggest assumption:
- Best next question:
```

### Tool Card: Double Diamond

Purpose: Stop premature feature generation.

Role: Student provides the rough idea; agent separates problem discovery from solution shaping.

Type: Problem framing / diverge-converge.

Starting prompt:

```text
Act as my product discovery partner.

Context:
[Paste my rough idea.]

Task:
Use the Double Diamond to help me explore the problem before jumping to solutions.

Rules:
- First explore possible users, pains, causes, and current alternatives.
- Then narrow to one clear problem statement.
- Do not suggest product features until the problem is defined.
- Keep the language plain and practical.

Output:
- Possible users:
- Possible pains:
- Current alternatives:
- Strongest problem candidate:
- One clear problem statement:
- What we should not solve yet:
- Next question:
```

### Tool Card: SIT Remix

Purpose: Generate variations from existing components.

Role: Student names the current product/workflow pieces; agent remixes them.

Type: Structured creative remixing.

Starting prompt:

```text
Act as my product remix partner.

Context:
[Paste my idea and list any parts, pages, workflows, or user actions it might include.]

Task:
Use Systematic Inventive Thinking to create practical variations of this idea.

Rules:
- Try subtraction, division, multiplication, task unification, and attribute dependency.
- For each variation, explain what user problem it might solve better.
- Avoid random feature lists.
- Do not write a PRD or code.

Output:
- Subtraction idea:
- Division idea:
- Multiplication idea:
- Task unification idea:
- Attribute dependency idea:
- Most promising variation:
- Why it is promising:
```

### Tool Card: TRIZ Contradiction

Purpose: Make tradeoffs explicit.

Role: Student names what they want to improve; agent finds the tension.

Type: Contradiction / tradeoff thinking.

Starting prompt:

```text
Act as a TRIZ-inspired product thought partner.

Context:
[Paste my idea and any tradeoff I am worried about.]

Task:
Help me find the main contradiction in this idea.

Rules:
- Phrase the contradiction as: "We want more X, but that makes Y worse."
- Suggest ways to improve both sides or avoid the tradeoff.
- Keep this at the product level unless I ask for technical details.
- Do not write implementation steps.

Output:
- Main contradiction:
- Why it matters:
- Possible resolution 1:
- Possible resolution 2:
- Possible resolution 3:
- Best next question:
```

### Tool Card: OODA Loop

Purpose: Move through uncertainty with a small learning cycle.

Role: Student shares what is known/confusing; agent organizes the next decision loop.

Type: Adaptive decision-making.

Starting prompt:

```text
Act as my decision-making coach.

Context:
[Paste my idea, what I know, and what feels uncertain.]

Task:
Use an OODA loop to help me decide what to do next.

Rules:
- Observe only what is known or reasonably evidenced.
- Orient around user, problem, constraints, and uncertainty.
- Recommend one decision.
- Suggest one small action to learn more.
- Do not write a PRD or code.

Output:
- Observe:
- Orient:
- Decide:
- Act:
- What would change the decision:
```

### Tool Card: Lean Startup

Purpose: Convert risky assumptions into small tests.

Role: Student identifies what must be true; agent recommends the smallest test.

Type: Hypothesis testing / validated learning.

Starting prompt:

```text
Act as my Lean Startup coach.

Context:
[Paste my idea and why I think it might work.]

Task:
Treat this idea as a set of hypotheses and find the riskiest one.

Rules:
- Identify assumptions about desirability, viability, feasibility, usability, or trust.
- Recommend the smallest credible test.
- Define what result would mean proceed, pause, narrow, or kill.
- Do not suggest building a full product.

Output:
- Riskiest hypothesis:
- Why it is risky:
- Smallest test:
- Proceed signal:
- Pause or narrow signal:
- Kill signal:
- Next step:
```

### Tool Card: de Bono Lateral Move

Purpose: Escape obvious ideas.

Role: Student says where they are stuck; agent challenges assumptions and creates practical alternatives.

Type: Lateral thinking / pattern break.

Starting prompt:

```text
Act as my lateral thinking partner.

Context:
[Paste my idea and where my thinking feels stuck.]

Task:
Use Edward de Bono-style lateral thinking to find a fresh angle.

Rules:
- Challenge one hidden assumption.
- Create one provocative "what if."
- Use one random input or analogy.
- Then translate only the useful parts into practical product options.
- Do not turn this into a feature dump.

Output:
- Hidden assumption:
- Provocation:
- Random input or analogy:
- Practical option 1:
- Practical option 2:
- What to test or ask next:
```

### Tool Card: Six Hats Mini-Review

Purpose: Evaluate an idea from several thinking modes without muddled debate.

Role: Student provides candidate direction; agent reviews it from distinct angles.

Type: Structured review.

Starting prompt:

```text
Act as my balanced product reviewer.

Context:
[Paste my idea or candidate direction.]

Task:
Use a Six Thinking Hats mini-review to evaluate this idea.

Rules:
- Keep each hat short.
- Separate facts, instincts, benefits, risks, creative alternatives, and process.
- End with the next best question or action.
- Do not decide for me.

Output:
- White hat, facts:
- Red hat, instincts:
- Yellow hat, benefits:
- Black hat, risks:
- Green hat, alternatives:
- Blue hat, next process step:
```

### Tool Card: Connections Map

Purpose: Find useful analogies and cross-domain links.

Role: Student provides idea and inspirations; agent maps useful adjacent patterns.

Type: Analogy / synthesis.

Starting prompt:

```text
Act as my connections-mapping partner.

Context:
[Paste my idea, audience, and any inspirations.]

Task:
Find useful connections between this idea and adjacent domains, existing tools, user habits, everyday analogies, or constraints.

Rules:
- Look for practical connections, not trivia.
- Explain why each connection matters.
- Separate interesting-but-distracting links from useful product insight.
- Do not write a PRD or code.

Output:
- Useful connection 1:
- Useful connection 2:
- Useful connection 3:
- Distracting connection to ignore:
- Product insight:
- Next question:
```

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

Reality check: gently challenge the scope. What would make this first version too large, too risky, or too hard to verify? Sort concerns into Must decide now, Good enough for MVP, and Defer / Not yet.
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

Current alternatives or workarounds:

Evidence strength:

Demand or pricing signal:

Smallest non-code learning step:

What would change my mind:

Exploration Loop summary:

New things discovered during exploration:

Capability candidates:

Overlooked alternatives or adjacent ideas:

Stable facts:

Assumptions:

Open questions:

Candidate product constitution updates:

Candidate feature or PRD ideas:

Candidate non-goals:

Smallest useful version:

Not-yet list:

Success signals:

Purposeful ideation tools used:

Constraint chosen:

Main contradiction or tradeoff:

Lateral move or surprising connection:

Riskiest hypothesis:

Options intentionally not pursued:

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
