# PrecodeOS -- Hypothesis Review / Learning Loop Protocol
<!-- ANCHOR: hypothesis-review-protocol -->

> AUTHORITY: Advisory review loop for checking whether a hypothesis or learning target was tested, narrowed, killed, promoted, left untested, or made stale across discovery, intake, Candidate Queue, PRD source inputs, and Planning Briefs.
> NOT_AUTHORITY: Active memory, product decisions, PRD approval, Candidate Queue ranking, task selection, bead activation, implementation priority, generated proof, analytics requirements, experiment database, dashboard, route structure, schema definitions, or implementation status.
> LOAD_WHEN: A user asks whether a Discovery Summary, Candidate Queue entry, Local Source Intake summary, PRD Source Inputs section, Product Brief, Conviction Packet, or Planning Brief hypothesis was tested, learned from, narrowed, killed, promoted, left untested, stale, or ready for the next Precode workflow.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## Purpose

Hypothesis Review / Learning Loop helps a builder revisit what was actually learned before a hunch, assumption, hypothesis, or experiment result becomes product-definition momentum.

It connects existing Precode evidence surfaces:

```text
Product Brief / Conviction Packet / Discovery Summary
  -> Local Source Intake / Candidate Queue / PRD Source Inputs
  -> Planning Brief when metric-backed validation is needed
  -> reviewed next workflow or stop decision
```

The loop is advisory and evidence-only. It clarifies learning status and next safe workflow; it does not approve product direction, approve PRDs, rank candidates, activate beads, select tasks, create follow-up work, or make generated status authoritative.

## When To Use

Use this protocol when the user asks:

- Did we test this hypothesis?
- What did we learn from this Discovery Summary or learning step?
- Is this Candidate Queue entry stale, untested, narrowed, killed, or ready for intake?
- Did the Planning Brief produce a hard decision that belongs in `DECISIONS.md`?
- Should this hypothesis proceed to Local Source Intake, Product Discovery, PRD shaping, a PRD amendment, a decision, defer, or kill?

Do not use this protocol as a required gate for every small task, a replacement for Product Discovery Validation, a Review Lane for implementation acceptance, or an analytics workflow.

## Review Status Vocabulary

Use one status when it helps make the review concrete:

| Status | Meaning |
|---|---|
| `untested` | A hypothesis or learning target exists, but no reviewed learning evidence is present. |
| `tested` | Reviewed evidence says the learning step, prototype, interview, rollout, or metric check happened. |
| `narrowed` | Evidence changed the audience, problem, scope, first slice, or assumption being tested. |
| `killed` | The user decided not to pursue the idea or hypothesis now. |
| `promoted` | Reviewed conclusions moved into Local Source Intake, Product Discovery, a PRD, a decision, an authority-file update, or decomposition review. |
| `stale` | The hypothesis may conflict with newer user intent, current owner files, current code, approved PRDs, active beads, or newer evidence. |
| `not applicable` | The source is not hypothesis-shaped or the work does not need hypothesis review. |

These statuses are review labels only. They do not rank Candidate Queue entries, choose work, approve promotion, update owner files, or close candidates by themselves.

## Required Inputs

Load the smallest useful source set:

- the named Discovery Summary, Product Brief, Conviction Packet, Local Source Intake summary, Candidate Queue entry, PRD Source Inputs section, or Planning Brief
- the owner protocol for that source, such as Product Discovery Validation, Local Source Intake, Candidate Queue, PRD, or Planning Protocol
- current owner files only when the review needs to detect stale or conflicting evidence
- recorded checks, manual evidence, user notes, or source references only when the user names them or the source points to them

Stop instead of guessing if the source material is missing, the hypothesis or learning target is unclear, or the review would require secrets, private raw transcripts, dashboard values, production analytics, credentials, or external mutation.

## Output Contract

Return exactly these fields:

```text
Review target:
Authority checked:
Hypothesis or learning target:
Evidence reviewed:
Learning status: untested | tested | narrowed | killed | promoted | stale | not applicable
Learning outcome:
Stale or untested signals:
Recommended next Precode workflow:
User approval needed:
Stop condition:
Generated-report warning:
```

The recommendation is advisory. It may point to Local Source Intake, Product Discovery Validation, Candidate Queue update, PRD draft, PRD amendment, `DECISIONS.md`, owner-file update, Planning Protocol, Decomposition Protocol, defer, kill, or no action. It must not perform those promotions automatically.

## Promotion Path

Promote reviewed learning only through the normal owner path:

| Reviewed learning | Destination |
|---|---|
| Source facts, assumptions, conflicts, open questions, or learning outcome | Local Source Intake summary |
| Product promise, user/job, strategy, current bet, success signal, or non-goal | `PRODUCT.md` after user review |
| Product problem, goals, non-goals, requirements, or source inputs | PRD shard |
| Hard product, technical, rollout, or operating decision | `DECISIONS.md` |
| Parked or revisitable idea | `CANDIDATE-QUEUE.md` after user review |
| Metric-backed rollout plan or result | Planning Brief, then `DECISIONS.md` for hard decisions |
| Executable work | Candidate bead only after PRD or owner-file readiness and Decomposition Protocol review |
| Not worth pursuing | defer, kill, or historical evidence note |

## Guardrails

- Do not approve product direction.
- Do not approve PRDs.
- Do not activate beads.
- Do not choose tasks.
- Do not rank Candidate Queue entries.
- Do not treat `promoted` as permission to implement.
- Do not require analytics, dashboards, external systems, or production metrics.
- Do not create an experiment database, generated report, command wrapper, registry, optional pack, release channel, or package-manager behavior.
- Do not treat generated hypothesis status as source of truth.
- Do not edit files, create follow-up tasks, or promote findings without user review.

## User Prompt

```text
Use Hypothesis Review / Learning Loop on this Discovery Summary, Candidate Queue entry, Local Source Intake summary, PRD Source Inputs section, or Planning Brief.

Tell me what was tested, what was learned, whether the hypothesis is untested, tested, narrowed, killed, promoted, stale, or not applicable, and the next safe Precode workflow.

Treat the output as evidence only. Do not approve product direction, rank candidates, create or activate beads, update owner files, choose tasks, require analytics, create a database, or code.
```
