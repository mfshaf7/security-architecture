# security-architecture Agent Notes

This repository defines the security architecture, control strategy, and review
criteria for the platform.

## What This Repo Owns

- security standards
- trust-boundary definitions
- review methodology
- ADRs for security-significant decisions
- findings and remediation direction
- AI governance and model-risk expectations

It does not own delivery implementation.

## Read First

- `README.md`
- `docs/charter.md`
- `docs/architecture/platform-overview.md`
- `docs/architecture/trust-boundaries.md`
- `docs/strategy/target-state.md`
- `docs/reviews/security-review-checklist.md`

## Working Rules

- Return security judgment first and implementation advice second.
- Distinguish between design intent, implemented control, and operating
  evidence.
- If a control exists only in code and not in reviewable governance artifacts,
  the control story is incomplete.
- Push requirements back to the owner delivery repo instead of absorbing
  delivery work here.
