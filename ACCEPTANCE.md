# PrecodeOS — Acceptance Template
<!-- ANCHOR: acceptance -->

> AUTHORITY: Done checks, verification criteria, and feature completion gates for the target project.
> NOT_AUTHORITY: New product behavior, route design, schema changes, or pricing decisions.
> LOAD_WHEN: Defining or reviewing acceptance criteria for a PRD, feature, or bead.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-23

## Acceptance Criteria

Add project acceptance criteria here after PRD approval.

## Optional EARS-Style Pattern

When an acceptance criterion is vague, you may rewrite it in an EARS-style shape:

```text
WHEN [condition or event] THE SYSTEM SHALL [observable expected behavior].
```

Examples:

- WHEN a signed-out visitor opens the dashboard URL THE SYSTEM SHALL redirect them to the sign-in page.
- WHEN a user submits an invalid email address THE SYSTEM SHALL show a plain error and keep the form values intact.
- WHEN an import file is missing a required column THE SYSTEM SHALL stop the import and explain which column is missing.

Use this pattern only when it makes the expected behavior easier to verify. Clear non-EARS acceptance criteria remain valid when they are observable and testable. EARS-style wording is not required schema, proof by itself, PRD approval, implementation authority, or a reason to reject otherwise clear acceptance criteria.
