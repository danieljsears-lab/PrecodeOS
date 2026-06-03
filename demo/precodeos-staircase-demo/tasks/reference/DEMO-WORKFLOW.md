# Demo Workflow Authority

> AUTHORITY: Workflow, scope, success criteria, and recovery moments for the PrecodeOS beginner demo.
> NOT_AUTHORITY: Production app roadmap, deployment setup, real location data, or external integrations.
> LOAD_WHEN: Running the VSCode + Claude Code beginner demo.
> CLASS: reference

## Purpose

Teach a beginner the PrecodeOS survival loop:

1. Start from repo truth.
2. Confirm the active bead.
3. Keep Claude inside the bead boundary.
4. Ask for evidence.
5. Check health.
6. Close and review.
7. Approve the next bead only when ready.

## Demo App

The app is a static staircase discovery prototype with seeded cards.

The first product bead adds a local difficulty filter. It must not add maps, geolocation, accounts, persistence, APIs, database work, deployment, or unrelated redesign.

## Required Recovery Moments

- Scope drift: Claude proposes maps or geolocation during the difficulty-filter bead.
- False done: Claude claims the filter is done without checks or manual verification.

## Review Outcomes

Use exactly one of:

- `accepted`
- `revise`
- `split`
- `blocked`
- `stop`
