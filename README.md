# Security Architecture

This repository defines the security architecture, control strategy, and review
criteria for the platform.

It exists to separate security governance and architectural decision-making from
day-to-day delivery work.

## What This Repository Owns

This repository owns:

- security standards
- trust-boundary definitions
- review methodology
- ADRs for security-significant decisions
- findings and remediation direction
- AI governance and model-risk expectations

It does not own:

- rollout implementation
- gateway composition
- Telegram feature work
- host bridge code changes

Those live in delivery repos and should consume the standards and review outputs
from here.

## Workflow Role

1. Security-significant change is proposed in a delivery repo.
2. This repository supplies the review lens:
   - trust boundaries
   - identity and secret impact
   - privileged runtime and AI implications
3. Findings or requirements flow back to the owner repo.
4. Delivery repos implement the control.
5. Standards or ADRs here are updated when the security posture or governance
   model materially changes.

## Audit And Visibility

This repo is the main evidence surface for security governance.

- standards:
  - `docs/standards/`
- architecture and boundary model:
  - `docs/architecture/`
- repeatable review method:
  - `docs/reviews/security-review-checklist.md`
  - `docs/methodology/assessment-method.md`
- durable decisions:
  - `docs/adr/`
- findings and risk tracking:
  - `registers/`

If a control exists only in code and not in these reviewable artifacts, the
security governance story is incomplete.

## Repository Layout

- [`docs/charter.md`](docs/charter.md)
- [`docs/architecture/platform-overview.md`](docs/architecture/platform-overview.md)
- [`docs/architecture/component-inventory.md`](docs/architecture/component-inventory.md)
- [`docs/architecture/trust-boundaries.md`](docs/architecture/trust-boundaries.md)
- [`docs/strategy/target-state.md`](docs/strategy/target-state.md)
- [`docs/strategy/roadmap.md`](docs/strategy/roadmap.md)
- [`docs/strategy/30-60-90-plan.md`](docs/strategy/30-60-90-plan.md)
- [`docs/assessments/platform-security-assessment-2026-04.md`](docs/assessments/platform-security-assessment-2026-04.md)
- [`docs/assessments/platform-security-executive-report-2026-04.md`](docs/assessments/platform-security-executive-report-2026-04.md)
- [`docs/standards/`](docs/standards)
- [`docs/reviews/security-review-checklist.md`](docs/reviews/security-review-checklist.md)
- `registers/`

## Current Priorities

1. remove shared operator passwords and move human access to SSO or OIDC
2. move machine Git access to a governed GitHub App model
3. formalize Vault recovery-material handling and rotation
4. keep host-control and AI-enabled behavior under explicit review and audit
5. make repository governance and evidence expectations durable across the
   delivery repos
