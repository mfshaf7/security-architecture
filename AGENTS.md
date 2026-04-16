# security-architecture Agent Notes

This repository defines the security architecture, control strategy, and review
criteria for the platform.

## What This Repo Owns

- security standards
- trust-boundary and security architecture views
- review methodology and security review outputs
- ADRs for security-significant decisions
- findings, risks, and security inventories
- AI governance and model-risk expectations

It does not own delivery implementation.

## Read First

- `README.md`
- `docs/charter.md`
- `docs/architecture/README.md`
- `docs/architecture/platform/overview.md`
- `docs/architecture/platform/trust-boundaries.md`
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
- Place new content in the correct layer:
  - `docs/standards/` for normative control requirements
  - `docs/adr/` for durable security decisions
  - `docs/architecture/platform|domains|components|products/` for scoped
    security design
  - `docs/reviews/` for review method or review outputs
  - `docs/assessments/` for periodic or event-driven assessment evidence
  - `registers/` for live findings, risks, and inventories
- Keep product ops, rollout steps, and delivery implementation in owner repos.
- After structural changes, run:
  - `python3 scripts/validate_repo_structure.py --repo-root .`
