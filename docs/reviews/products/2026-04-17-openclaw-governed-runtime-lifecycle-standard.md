# OpenClaw Governed Runtime Lifecycle Standard Review

## Scope

Review the expansion of the OpenClaw prod lifecycle from a bounded
`live`/`suspended` control into the shared runtime lifecycle vocabulary:

- `live`
- `traffic-stopped`
- `suspended`
- `quarantined`

This review covers the platform-level lifecycle standard and the OpenClaw
reference profile that implements `traffic-stopped` at the deployment
boundary.

## Decision

Approved with bounded controls.

The richer lifecycle model is accepted when all of these remain true:

- lifecycle state remains Git-managed in
  `platform-engineering/environments/prod/openclaw-lifecycle.yaml`
- OpenClaw continues to govern only its own prod runtime slice
- `traffic-stopped` cuts product traffic by removing the OpenClaw gateway app
  while leaving only the explicitly retained support surfaces
- `quarantined` requires an incident reference and blocks prod promotion by
  default
- any return to `live` resets prod verification and requires fresh prod smoke
  or UAT

## Review Areas

### Identity

- no new long-lived human or machine identity is introduced
- lifecycle changes still execute through the existing platform repo-write and
  GitHub environment gate identities

### Secrets

- no new secret path is introduced
- retaining `platform-secrets-prod` during `traffic-stopped` does not widen
  credential scope because the state still remains Git-managed and reviewable

### Delivery

- delivery trust expands from a binary prod lifecycle to a shared runtime
  lifecycle vocabulary
- this is accepted because the control remains reviewable in Git and promotion
  behavior is explicit for each state
- promotion while `quarantined` is blocked, which is the correct fail-closed
  posture for incident containment

### Runtime

- `traffic-stopped` intentionally removes the product gateway while retaining a
  narrower support surface
- this is accepted because the traffic cut happens at the deployment boundary
  rather than being hidden inside a channel-specific runtime gate
- `quarantined` remains stronger than ordinary suspension and must not become a
  casual operator quiet-mode

### AI And User-Controlled Input

- user-controlled product traffic no longer reaches the OpenClaw runtime when
  lifecycle is `traffic-stopped` or `quarantined`
- that is a security improvement for incident containment and staged quiet-mode
  operations
- the change must not introduce alternate undocumented user ingress paths

## Residual Risk

- OpenClaw is the reference implementation, but future products or shared
  components could still misuse the shared vocabulary if they copy the state
  names without publishing a real lifecycle profile
- `traffic-stopped` retains selected support surfaces, so operators must still
  review whether any unintended ingress path remains active for the product

## Related Artifacts

- [`../../architecture/platform/trust-boundaries.md`](../../architecture/platform/trust-boundaries.md)
- [`../../domains/gitops-and-machine-trust.md`](../../domains/gitops-and-machine-trust.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
