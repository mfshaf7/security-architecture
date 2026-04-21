# Security Delta Review Process

Use this workflow when a change crosses a meaningful security boundary and the
baseline review is no longer enough by itself.

This is the primary operating surface for fresh security review on:

- identity changes
- secret custody or delivery changes
- GitOps or machine-trust changes
- privileged runtime or host-control changes
- AI-shaped action or approval-path changes
- workflow automation that mutates canonical backends

## Trigger Model

A delta review is required when a security-significant owner-repo change matches
the repo-rule `security_requirements.delta_review_triggers` contract in
`workspace-governance`.

The delta review must update:

- the concrete dated review artifact in this repo
- `registers/review-inventory.yaml`
- the latest decision for the affected review subject

## Required Structure

Every fresh delta review should include these sections:

1. `## Summary`
2. `## Scope Delta`
3. `## Review Areas`
4. `## Decision`

The review may add more sections, but it should not omit those four.

## Decision States

Use exactly one of these outcomes:

- `approved`
- `approved-with-findings`
- `blocked`
- `accepted-risk`

If the decision is not `approved`, route the outcome back into the owning
delivery workflow or remediation inventory as concrete follow-up, not a vague
warning.

## Review Discipline

The review should distinguish:

- design intent
- implemented control
- operating evidence

It should also answer:

- what changed
- which trust boundary moved
- which review areas were implicated
- which residual risk remains
- what has to be fixed or accepted before the change is considered safe

## Inventory Update Rules

Update `registers/review-inventory.yaml` in the same work:

- set `latest_change_review.status: current`
- set `latest_change_review.decision`
- set `latest_change_review.review_areas`
- set `latest_change_review.review_trigger_ids`
- update `latest_change_review.path` or the referenced review artifact content

When the latest review simply inherits the baseline, use
`status: baseline-current` and keep the baseline decision mirrored there.

## Routing Of Findings

Security review outputs do not close the loop by themselves.

Route findings into one or more of:

- owner-repo implementation work
- OpenProject ART risks or blockers
- `security-architecture/registers/remediation-inventory.yaml`
- explicit accepted-risk documentation
