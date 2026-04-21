# Operator Orchestration Service Broker Create Repair And Role Alignment Review

## Summary

- date: 2026-04-21
- owner repo: `operator-orchestration-service`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `products.openproject`
- decision: `approved`

This delta review covers the broker create-path repair after live devint
revalidation exposed two issues:

- the accepted-idea-delivery devint profile was still provisioning the broker
  identity without `Work package structure editor`
- the broker create adapter needed to preserve formattable custom-field payloads
  and treat assignee selection as an assignable-principal contract

## Scope Delta

The earlier delivery-workflow broker expansion review approved the first create
surface, but live proof showed the current lane could still drift into a weaker
role set and a partially-correct create payload.

This delta is not a new workflow family. It is a hardening slice that restores
the intended bounded create authority:

- the machine identity now carries the reviewed subtask/move permissions in the
  devint profile that actually provisions the lane
- the broker adapter keeps markdown-backed SAFe fields intact on create
- assignee resolution is now explicitly bounded to principals that OpenProject
  exposes as assignable in the target project or work-item form

## Review Areas

### Identity

- adding `Work package structure editor` to the devint provisioning path is
  acceptable because the delivery create path already depends on subtask
  management semantics
- the permission growth remains bounded to work-package structure operations and
  does not create admin-equivalent authority

### Secrets

- no secret class changed
- the existing broker token and caller-auth boundary remain the relevant secret
  controls

### Delivery

- preserving formattable SAFe fields on create is required for operator truth
  and does not widen authority
- the assignable-principal rule is the correct boundary because it keeps the
  broker aligned with the backend's project membership model instead of
  reintroducing runner-only bypass behavior

### Runtime

- the devint profile now provisions the same reviewed role set that the broker
  contract assumes
- this reduces the chance of a lane-local privilege mismatch surviving until
  live create proof

### AI

- no AI-shaped control changed in this slice

## Decision

`approved`

Approved because the change restores least-privilege correctness and removes a
real lane-drift condition without broadening the broker into a generic admin
surface.

Required follow-up: None beyond continuing the existing per-slice delta-review
discipline for later brokerized delivery commands.

## Related Artifacts

- [`../../architecture/components/operator-orchestration-service/README.md`](../../architecture/components/operator-orchestration-service/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
