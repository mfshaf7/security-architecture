# OpenClaw Stage Bridge Persistence And Status Truth Review

## Summary

- date: 2026-04-21
- owner repo: `platform-engineering`
- affected review subject: `products.openclaw`
- decision: `approved`

This delta review covers the change that makes the stage host bridge persist
while stage is intentionally active and makes stage status fail closed when the
bridge path is degraded.

## Scope Delta

The earlier OpenClaw lifecycle model already treated stage as a meaningful
governed rehearsal environment. The new change tightens the live control model:

- stage resume now enables and starts the stage host bridge service
- stage suspend now disables it again
- stage status now reports bridge readiness and treats a missing bridge path as
  degraded state instead of silently claiming the environment is simply active

This is a runtime and control-plane improvement, but it touches a privileged
host-control dependency and therefore still requires fresh review.

## Review Areas

### Identity

- no new human or machine identity is introduced
- the change does strengthen the standing importance of the stage bridge
  identity while the environment is active, so enable/disable discipline must
  stay explicit

### Secrets

- no new secret path is introduced
- existing bridge or gateway credentials do not widen in scope from this change

### Delivery

- the status surface is materially more truthful now because stage no longer
  hides a missing host-control half behind a partially active verdict
- stage lifecycle remains Git-managed and operator-visible, which is the right
  delivery posture for this control

### Runtime

- persisting the bridge while stage is intentionally active is acceptable for a
  long-lived stage environment
- disabling the bridge on suspend is essential and remains part of the
  approval condition

### AI

- no new AI-shaped action path is introduced

## Decision

`approved`

Approved because the change reduces hidden drift and strengthens fail-closed
status truth without widening the runtime in an uncontrolled way.

The approval depends on these remaining true:

- stage suspend disables the bridge again
- stage status continues to require bridge readiness for a healthy active state
- later changes to privileged host-control or agentic action paths still route
  through fresh security delta review

## Related Artifacts

- [`../../architecture/products/openclaw/README.md`](../../architecture/products/openclaw/README.md)
- [`../../architecture/products/openclaw/required-controls.md`](../../architecture/products/openclaw/required-controls.md)
- [`../../architecture/domains/host-control.md`](../../architecture/domains/host-control.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
