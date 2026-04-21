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
- `skills-src/README.md`

## Working Rules

- Return security judgment first and implementation advice second.
- Distinguish between design intent, implemented control, and operating
  evidence.
- Treat security-significant delivery or platform changes as requiring a fresh
  delta review with an explicit decision, not just a baseline reference.
- If a control exists only in code and not in reviewable governance artifacts,
  the control story is incomplete.
- Push requirements back to the owner delivery repo instead of absorbing
  delivery work here.
- Keep reusable security review workflows under `skills-src/` so the workspace
  installer can publish them without copying logic into `workspace-governance`.
- Expect owner repos to reference concrete security artifacts here when they
  cross meaningful trust-boundary review areas.
- Place new content in the correct layer:
  - `docs/standards/` for normative control requirements
  - `docs/adr/` for durable security decisions
  - `docs/architecture/platform|domains|components|products/` for scoped
    security design
- `docs/reviews/` for review method or review outputs
  - `docs/assessments/` for periodic or event-driven assessment evidence
  - `registers/` for live findings, risks, and inventories
- Use `docs/reviews/security-delta-review-process.md` as the primary review
  workflow when a change affects trust boundaries, identity, secrets, delivery,
  privileged runtime, host control, or AI-shaped action paths.
- Keep product ops, rollout steps, and delivery implementation in owner repos.
- After structural changes, run:
  - `python3 scripts/validate_repo_structure.py --repo-root .`
  - `python3 scripts/validate_security_evidence.py --repo-root . --workspace-root /home/mfshaf7/projects`

## Review guidelines

For Codex GitHub review, treat the following as `P1` when they plausibly
regress the security-governance role:

- security claims that are no longer backed by a concrete artifact, review
  output, or evidence linkage
- delivery implementation or operator-runbook content being absorbed here
  instead of pushed back to the owner repo
- changes that blur design intent, implemented control, and operating evidence
  into a single undocumented claim
