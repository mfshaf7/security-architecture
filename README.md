# Security Architecture

This repository is the security governance backbone for the platform.

It separates security standards, architecture judgment, assessment evidence, and
durable decisions from day-to-day delivery repos.

## What This Repository Owns

This repository owns:

- security standards and control expectations
- trust-boundary and security architecture views
- ADRs for security-significant decisions
- repeatable review and assessment methodology
- security review outputs and assessment evidence
- findings, risks, and security inventories
- AI governance and model-risk posture
- repo-owned skill source for reusable security review workflows

It does not own:

- rollout implementation
- product packaging or release assembly
- product feature development
- host bridge or application code changes
- operator access runbooks

Those stay in the owning delivery and platform repos.

Key related owner repos:

- `platform-engineering`
  - shared platform and release authority
- `openclaw-host-bridge`
  - host-control enforcement runtime
- `openclaw-runtime-distribution`
  - active OpenClaw runtime composition

## Repository Model

This repo uses a hybrid enterprise structure:

- governance artifacts by type:
  - [`docs/standards/`](docs/standards)
  - [`docs/adr/`](docs/adr)
  - [`docs/methodology/`](docs/methodology)
- architecture by scope:
  - [`docs/architecture/platform/`](docs/architecture/platform)
  - [`docs/architecture/domains/`](docs/architecture/domains)
  - [`docs/architecture/components/`](docs/architecture/components)
  - [`docs/architecture/products/`](docs/architecture/products)
- evidence by artifact class:
  - [`docs/reviews/`](docs/reviews)
  - [`docs/assessments/`](docs/assessments)
  - [`registers/`](registers)
- repo-owned workflow skills:
  - [`skills-src/`](skills-src)

That structure is deliberate:

- standards stay cross-cutting
- security design is described at the right scope
- review and assessment evidence remain auditable
- findings and risk tracking stay centralized

## Workflow Role

1. A security-significant change is proposed in a delivery repo.
2. This repository supplies the review lens:
   - trust boundaries
   - identity and secret impact
   - machine-trust and GitOps impact
   - privileged runtime and host-control implications
   - AI and agentic risk
3. Requirements or findings flow back to the owner repo.
4. Owner repos should link concrete security artifacts from this repository,
   not only the repo name.
5. Delivery repos implement the control.
6. This repository is updated only when the security posture, control model, or
   evidence base materially changes.

## Audit And Visibility

This repo is the main evidence surface for security governance:

- normative controls:
  - [`docs/standards/`](docs/standards)
- architecture and trust-boundary models:
  - [`docs/architecture/`](docs/architecture)
- review method and review outputs:
  - [`docs/reviews/`](docs/reviews)
  - [`docs/methodology/assessment-method.md`](docs/methodology/assessment-method.md)
- durable decisions:
  - [`docs/adr/`](docs/adr)
- point-in-time assessment evidence:
  - [`docs/assessments/`](docs/assessments)
- findings, risks, and security inventories:
  - [`registers/`](registers)

If a control exists only in code and not in these reviewable artifacts, the
security governance story is incomplete.

## Read First

- [`docs/charter.md`](docs/charter.md)
- [`docs/architecture/README.md`](docs/architecture/README.md)
- [`docs/architecture/platform/overview.md`](docs/architecture/platform/overview.md)
- [`docs/architecture/platform/trust-boundaries.md`](docs/architecture/platform/trust-boundaries.md)
- [`docs/strategy/target-state.md`](docs/strategy/target-state.md)
- [`docs/reviews/security-review-checklist.md`](docs/reviews/security-review-checklist.md)
- [`skills-src/README.md`](skills-src/README.md)

## Validation

Run the structure validator after significant documentation or taxonomy changes:

```bash
python3 scripts/validate_repo_structure.py --repo-root .
python3 scripts/validate_security_evidence.py --repo-root . --workspace-root /home/mfshaf7/projects
```

## Current Priorities

1. remove shared operator passwords and move human access to SSO or OIDC
2. move machine Git access to a governed GitHub App model
3. formalize Vault recovery-material handling and rotation
4. keep host-control and AI-enabled behavior under explicit review and audit
5. make repository governance and evidence expectations durable across the
   delivery repos
