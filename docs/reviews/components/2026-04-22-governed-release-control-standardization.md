# Governed Release Control Standardization Review

## Summary

- date: 2026-04-22
- owner repos:
  - `workspace-governance`
  - `platform-engineering`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.platform-engineering`
- decision: `approved-with-findings`

This delta review covers the new shared release-governance standard that
defines:

- release-governance tiers for products and components
- candidate, verification, readiness, and post-promotion evidence objects
- fail-closed aggregate stage and prod readiness expectations
- the separation between release governance and runtime lifecycle

## Scope Delta

The workspace already had mature governed release behavior for OpenClaw, but it
did not yet have a standardized enterprise model that covered:

- platform-integrated products such as OpenProject
- shared control-plane components such as
  `operator-orchestration-service`
- supporting services whose stale state can invalidate environment readiness

This change turns OpenClaw's strongest release controls into a shared standard
instead of leaving them as a product-specific maturity exception.

That matters to security because:

1. stale release state can keep a workload operationally healthy while leaving
   it functionally behind the approved contract
2. release governance is part of trust-boundary control when shared workflow
   components shape approvals, delivery, or runtime behavior
3. prod attestation becomes weaker if environment readiness does not prove the
   exact contract and verification state for all required workloads

## Review Areas

### Identity

- the standard does not create new human or service identities on its own
- it does increase the accountability expectations for the actors who record
  candidates, verification, and readiness decisions
- later workload-specific rollout must preserve least privilege for these
  release and readiness actions

### Secrets

- no new secret distribution pattern is introduced in this standards tranche
- future workload rollout must still review how evidence recording, readiness
  workflows, or promotion tooling access any required credentials

### Delivery

- this is the correct delivery control direction because it stops stage or prod
  from being treated as ready on health alone
- using one tiered model across products and components reduces silent maturity
  gaps between OpenClaw and the rest of the workspace
- aggregate environment readiness is especially important for supporting
  components because those services can invalidate the whole environment even
  when they are not user-facing releases

### Runtime

- the standard correctly separates release governance from runtime lifecycle
- that separation is important because promotion, deployed contract truth, and
  lifecycle state should not collapse into one ambiguous status
- later rollout must ensure the runtime and operator surfaces expose the same
  release-governance truth they claim to enforce

### AI

- this standard affects AI-shaped delivery and control paths indirectly because
  stale shared workflow services can change how governed workflows behave
- treating `operator-orchestration-service` as a shared control-plane component
  with product-grade release governance is the correct security posture

## Decision

`approved-with-findings`

Approved because the standard closes a real enterprise-control gap: workloads
should not be called ready merely because they are healthy when their release
state or verification truth is stale.

Required findings to carry forward:

- workload-specific rollout must not claim maturity until the actual operator
  surfaces, release objects, and fail-closed checks exist for that workload
- supporting-component readiness should stay explicit; do not let those
  components disappear into aggregate stage or prod language without their own
  verification truth
- any workload that gains a new promotion or verification authority path as a
  result of this standard still requires a workload-specific security delta
  review during implementation

## Related Artifacts

- `workspace-governance/contracts/release-governance.yaml`
- `platform-engineering/docs/standards/governed-release-control-model.md`
- `platform-engineering/docs/standards/release-model.md`
- `platform-engineering/docs/standards/ci-cd.md`
- `platform-engineering/docs/standards/governed-runtime-lifecycle-model.md`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
