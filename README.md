# Security Architecture

This repository defines the security architecture, control strategy, and remediation roadmap for the platform.

It exists to separate security governance and architectural decision-making from day-to-day platform delivery work.

## Purpose

- establish the target security architecture for the platform
- maintain the authoritative security roadmap
- track control gaps, risks, and remediation priorities
- define credential, identity, recovery, and secrets standards
- define AI security, AI governance, and model risk standards
- provide review artifacts for platform changes

## Scope

This repository covers:

- identity and access management
- secrets management and credential lifecycle
- recovery material governance
- machine identity and automation trust
- supply chain and repository access
- AI systems, model integrations, and agentic security posture
- platform hardening baselines
- incident response and audit posture

This repository does not replace delivery repos. Platform implementations remain in other repositories, especially [`platform-engineering`](/home/mfshaf7/projects/platform-engineering).

## Operating Model

- `security-architecture` owns standards, decisions, plans, and security review outputs.
- delivery repositories own implementation of approved controls.
- security findings should produce explicit downstream engineering tasks.

## Repository Layout

- [`docs/charter.md`](/home/mfshaf7/projects/security-architecture/docs/charter.md): repository charter and ownership model
- [`docs/architecture/platform-overview.md`](/home/mfshaf7/projects/security-architecture/docs/architecture/platform-overview.md): full platform diagram and review reference
- [`docs/architecture/component-inventory.md`](/home/mfshaf7/projects/security-architecture/docs/architecture/component-inventory.md): component inventory and trust relevance
- [`docs/architecture/trust-boundaries.md`](/home/mfshaf7/projects/security-architecture/docs/architecture/trust-boundaries.md): trust-boundary mapping
- [`docs/strategy/target-state.md`](/home/mfshaf7/projects/security-architecture/docs/strategy/target-state.md): target security architecture
- [`docs/strategy/roadmap.md`](/home/mfshaf7/projects/security-architecture/docs/strategy/roadmap.md): phased remediation plan
- [`docs/strategy/30-60-90-plan.md`](/home/mfshaf7/projects/security-architecture/docs/strategy/30-60-90-plan.md): near-term execution plan
- [`docs/assessments/platform-security-assessment-2026-04.md`](/home/mfshaf7/projects/security-architecture/docs/assessments/platform-security-assessment-2026-04.md): current-state assessment
- [`docs/adr/README.md`](/home/mfshaf7/projects/security-architecture/docs/adr/README.md): architecture decision record index
- [`docs/standards/`](/home/mfshaf7/projects/security-architecture/docs/standards): security standards and control expectations
- [`docs/standards/ai-security-and-governance.md`](/home/mfshaf7/projects/security-architecture/docs/standards/ai-security-and-governance.md): AI security and governance baseline
- [`docs/reviews/security-review-checklist.md`](/home/mfshaf7/projects/security-architecture/docs/reviews/security-review-checklist.md): reusable review checklist
- [`registers/risk-register.md`](/home/mfshaf7/projects/security-architecture/registers/risk-register.md): active security risks
- [`registers/credential-inventory.md`](/home/mfshaf7/projects/security-architecture/registers/credential-inventory.md): credential classes and ownership
- [`registers/ai-system-inventory.md`](/home/mfshaf7/projects/security-architecture/registers/ai-system-inventory.md): AI and agentic system inventory

## First Priorities

1. remove shared operator passwords and move human access to SSO/OIDC
2. move machine Git access to a governed GitHub App model
3. formalize Vault recovery-material handling and rotation
4. establish a repeatable security review process for platform changes
5. define AI security architecture and governance for future agentic systems
