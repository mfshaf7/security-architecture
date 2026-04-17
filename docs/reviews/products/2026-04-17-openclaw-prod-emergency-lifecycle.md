# OpenClaw Prod Emergency Lifecycle Review

## Scope

Review the introduction of a bounded governed prod lifecycle for OpenClaw that
allows prod OpenClaw to be deliberately suspended and later returned to `live`
without pruning unrelated prod services.

## Decision

Approved with bounded controls.

The governed prod lifecycle is accepted when all of these remain true:

- the lifecycle source of truth stays in Git under
  `environments/prod/openclaw-lifecycle.yaml`
- lifecycle changes remain gated by the protected `prod` environment and normal
  Git review
- the control affects only the OpenClaw prod runtime slice
- promotion may update the prod contract while prod remains suspended, but
  promotion alone must not reactivate prod
- returning prod to `live` resets prod verification and requires fresh prod
  smoke or UAT

## Review Areas

### Identity

- no new human identity is introduced
- no new long-lived machine identity is introduced
- the existing GitHub workflow and repository write identities remain the
  acting delivery identities

### Secrets

- no new secret path is introduced
- the control does not widen operator secret access beyond the existing
  protected GitHub environment and repo-write path

### Delivery

- delivery trust changes because prod runtime activity is now gated by a
  product-scoped lifecycle contract in addition to the normal prod version
  contract
- this is accepted because the control remains Git-managed, reviewable, and
  auditable
- the ability to promote while suspended is accepted only because lifecycle
  state still prevents accidental runtime reactivation

### Runtime

- the control may deliberately prune the OpenClaw prod runtime slice
- it must not prune unrelated prod applications such as OpenProject or shared
  observability
- no host-control, bridge, or Telegram privilege boundary is widened by this
  change alone

### Visibility

- operators must be able to identify current lifecycle state from:
  - `environments/prod/openclaw-lifecycle.yaml`
  - `environments/prod/argocd/openclaw-prod-lifecycle-configmap.yaml`
  - `environments/prod/verification.yaml`
- product access and platform access docs must explain that prod OpenClaw may
  be deliberately suspended

## Residual Risk

- the bounded initial lifecycle does not yet implement finer modes such as
  `traffic-stop` or `quarantined`
- incorrect future expansion of the managed resource slice could widen the
  blast radius of prod suspension if not reviewed explicitly

## Related Artifacts

- [`../../architecture/platform/trust-boundaries.md`](../../architecture/platform/trust-boundaries.md)
- [`../../domains/gitops-and-machine-trust.md`](../../domains/gitops-and-machine-trust.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
