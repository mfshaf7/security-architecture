# Platform Engineering OpenProject And Stage Control Delta Review

## Summary

- date: 2026-04-21
- owner repo: `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `products.openproject`
  - `products.openclaw`
- decision: `approved-with-findings`

This delta review covers the recent platform-owned control changes that moved
security-sensitive workflow and runtime behavior:

- OpenProject delivery wrappers now route more execution work through the broker
- OpenProject automation identity and ART operating model were expanded
- the OpenClaw stage host bridge now persists intentionally while stage stays
  active, and stage status truth includes bridge readiness
- production OpenProject activation now allows a vetted seeded ART baseline
  rather than requiring an empty plane

## Scope Delta

The April 18 platform baseline approved the general platform control model. The
new tranche changes how two live products rely on that control plane:

1. OpenProject now depends more heavily on a broker-owned workflow seam
2. OpenProject prod hygiene now distinguishes allowed seeded baseline history
   from forbidden rehearsal noise
3. OpenClaw stage now depends on an intentionally persistent host-bridge
   service when the environment is active

These are not cosmetic edits. They change how identity, delivery, and runtime
control are exercised in the live platform.

## Review Areas

### Identity

- the broker automation identity for OpenProject remains acceptable when
  permissions stay bounded to delivery workflow intent
- the stage host bridge should only be enabled while stage is intentionally
  active; persistence must not become a silent standing privilege

### Secrets

- no new secret classes are introduced
- the controls remain dependent on Vault-delivered custody and explicit owner
  paths
- OpenProject prod seeding must not smuggle unreconciled credentials or hidden
  rehearsal state into the promoted plane

### Delivery

- moving platform wrappers onto broker-owned workflow APIs is the correct
  design because it consolidates audit and validation
- permitting a vetted seeded ART baseline in production is acceptable only when
  provenance review is explicit and rehearsal-only data stays excluded
- stage status truth is materially stronger now that the bridge path is part of
  the active-state verdict

### Runtime

- stage bridge persistence improves resilience for an intentionally long-lived
  stage, but it also means host-control readiness must remain visible and
  reviewable
- OpenProject remains platform-integrated rather than a fully separate governed
  product lane, so platform controls still carry a large part of its security
  posture

### AI

- no new governed AI execution path is introduced in this tranche
- OpenClaw and OpenProject still require later review if model-shaped action or
  approval paths widen

## Decision

`approved-with-findings`

Approved because the changes improve control-plane clarity and operating truth.
The approval depends on these constraints:

- seeded OpenProject prod baselines must remain explicitly vetted and
  provenance-reviewed
- stage bridge persistence must continue to fail closed when stage is
  suspended
- platform wrappers must keep broker-owned workflow APIs as the durable seam
  instead of drifting back to direct backend mutation

Findings requiring continued attention:

- later broker migration slices still need fresh security delta review
- stage status truth should continue to treat missing host-control readiness as
  a degraded active state, not a cosmetic warning

## Related Artifacts

- [`../../architecture/platform/trust-boundaries.md`](../../architecture/platform/trust-boundaries.md)
- [`../../architecture/domains/gitops-and-machine-trust.md`](../../architecture/domains/gitops-and-machine-trust.md)
- [`../../architecture/domains/secrets-and-recovery.md`](../../architecture/domains/secrets-and-recovery.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
