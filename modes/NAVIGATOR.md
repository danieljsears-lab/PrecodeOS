# Precode OS Mode — Navigator
<!-- ANCHOR: mode-navigator -->

> AUTHORITY: Navigator mode for selecting the next bead, setting context, scope shaping, and handoff discipline.
> NOT_AUTHORITY: Direct implementation details, feature requirements, schema definitions, or pricing policy.
> LOAD_WHEN: Choosing the next logical unit, reshaping scope, or handing work to an AI coding agent.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Responsibilities

- pick the next bead
- shape rough ideas through `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` before implementation
- confirm the parent PRD and requirement IDs for product-feature work
- define or refine the done-when target
- confirm the primary authority file
- shape the Context Pack before handoff
- keep scope bounded
- decide when to split or pause work

## Navigator Checklist

1. Confirm the current active bead in `tasks/todo.md`.
2. Check whether the bead still has one clear logical unit.
3. For product-feature work, verify the PRD shard is approved and the bead cites requirement IDs.
4. Verify the primary authority file is the right owner for the work.
5. Load `PROJECT-CONTEXT.md` only when project-wide conventions, architecture, stack, dependencies, or integration boundaries matter.
6. Use `tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md` when source material, generated reports, or too many references could confuse the next agent.
7. Add missing context before handing the bead to a builder.
8. Use `bash scripts/handoff.sh [next-agent]` before switching tools.

## Workflow Lenses

Use these lenses as prompts, not as new modes or agents:

- Analyst lens: clarify the real problem, evidence, assumptions, and alternatives.
- Product Manager lens: turn the problem into goals, non-goals, requirements, and acceptance oracles.
- Architect lens: check project context, stack fit, integration boundaries, and implementation risk.
- Reviewer lens: challenge shallow artifacts before code starts.

## Tired-Builder Prompts

When the builder is tired, context is heavy, or the next step is unclear, use direct guidance:

- Pause here: the current idea is not ready for code because the user problem, non-goals, or verification path is unclear.
- Answer this before code: name the one decision or missing fact that can change implementation.
- Split this: the current task touches more than one authority file or more than one logical outcome.
- Do this next: run the smallest safe workflow step, such as drafting PRFAQ-lite, approving a PRD, creating one bead, or recording one check.

Navigator should make the next safe action obvious without activating the next bead automatically.

## Worktree Guidance

If planning and implementation start colliding, prefer separate worktrees for navigator work and builder work rather than mixing both roles in one dirty tree.
