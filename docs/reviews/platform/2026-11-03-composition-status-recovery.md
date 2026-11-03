# Composition status recovery

## Summary

Review the operator-authorized repair of a stale degraded status after all
participant health checks recovered. Platform retains the existing shared
runner, private record and operator commands. This review extends the
[local lane boundary](2026-04-18-dev-integration-local-k3s-lane.md) and inherits
unchanged controls from the [account reader review](../components/2026-11-03-account-repository-reader.md).
The main agent retains Security closure and final source judgment; the delegated
accountable human identity reviews and merges. This is not independent attestation.

## Scope Delta

### Design intent

An observation that temporarily fails must not permanently mislabel a completed
activation. Conversely, healthy components alone cannot complete an interrupted
startup/shutdown or resume suspended state. Workspace admission and profile-owned
readiness remain authoritative.

### Implemented control

- Preserve the last explicit lifecycle result separately from status results.
  Write incomplete intent before the first profile call, so interruption leaves
  a blocked result rather than reusing a previous successful activation.
- Restore active after status only when every participant passes, the current
  lifecycle is degraded and the retained result is a completed `up`. Failure
  of any participant still reports degraded and returns failure.
- Incomplete or failed startup/shutdown, suspended/unknown state and ambiguous
  legacy degraded state cannot acquire active context from health checks.
  Existing active records may retain their known completed activation. A legacy
  degraded record requires a normal completed `up`; deployment supplies that
  through the accepted operator workflow, without manual metadata edits.
- Preserve composition identity checks, existing credential projection and
  missing-credential denial. Status creates or rotates no credential, invokes
  no lifecycle mutation and preserves the existing binding values.
- Use a short private metadata lock and re-read current lifecycle metadata at
  status completion. An earlier status call must not erase a newer interrupted
  shutdown/startup intent. Profile calls execute outside the metadata lock.
- Keep the same operator surface and state schema version. The additional
  private lifecycle-result field is not an approval, remote control API, new
  service or alternate admission mechanism. Existing profile/lifecycle owners
  retain their operation boundaries.

### Operating evidence boundary

Pre-fix native evidence showed a background sync exit139, a successful normal
retry, all five current profile checks passing and a retained degraded label.
No cause of the segfault is accepted by this review. Runtime recovery, hardware
health and status presentation remain distinct claims.

Source regression covers partial/repeated health failure, recovery without
credential replacement, failed and interrupted up/down, overlapping status and
new shutdown intent, pending startup, suspended/unknown/legacy states and record
disappearance. Local runner, structure, governance and operational checks pass.
Hosted checks, exact source acceptance and normal runtime producer verification
remain required before operating closure. No live process fault is required to
test these state transitions; native current health is verified separately.

## Review Areas

- **Delivery:** active composition context must follow a completed activation
  and current participant readiness. A healthy observation cannot approve an
  unfinished lifecycle action or restore a removed binding.
- **Runtime:** interrupted mutation remains blocked; status preserves newer
  lifecycle intent and does not hold its metadata lock across profile execution.
  Native data and existing retry/service behavior are unchanged.
- **Inherited identity/secrets/AI:** prior reviews remain in force. This repair
  adds no identity, secret scope, provider access, profile admission or model
  authority; credential values remain absent from the private state projection.

## Decision

Approve source landing within these boundaries. Before selecting the changed
shared runner in the Console runtime, bind the actual reviewed Platform source
and tree in the existing composed decision. Index the merged owner change record
before final closure. Use the normal accepted activation/status path; do not
hand-edit the live lifecycle field, bypass health checks, recreate credentials
from status or claim a hardware fault was repaired by this status correction.
This is local dev-integration acceptance, not stage/production qualification.
