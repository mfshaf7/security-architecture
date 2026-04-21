# Platform Engineering OpenProject Assignable Principal And Operator Contract Review

## Summary

- date: 2026-04-21
- owner repo: `platform-engineering`
- affected review subject: `repos.platform-engineering`
- decision: `approved`

This delta review covers the platform-side contract correction for broker-backed
OpenProject work-item create and update workflows.

## Scope Delta

The OpenProject operator runbooks and contract surfaces were still using
examples that implied arbitrary assignment such as `ASSIGNEE_LOGIN=admin`.
Live revalidation showed that the broker-backed path correctly depends on the
backend's assignable-principal model instead.

This delta tightens the operator surface so the platform docs and helper text
now say what the backend actually guarantees:

- assignee login must be assignable in the target project or work item
- the broker-backed surface is not a generic user-assignment bypass

## Review Areas

### Identity

- the platform operator surface now matches the reviewed machine-identity model
  instead of implying broader human assignment authority than the backend
  grants

### Secrets

- no secret delivery or custody behavior changed

### Delivery

- this is a contract-hardening change for operator guidance on delivery
  mutation surfaces
- it reduces the risk of operators assuming runner-style assignment behavior on
  broker-backed paths

### Runtime

- no new runtime capability is introduced
- the change narrows operator expectations to the true OpenProject form/model
  behavior

### AI

- no AI-shaped control changed in this slice

## Decision

`approved`

Approved because the change removes overstatement from the operator surface and
aligns platform guidance with the reviewed broker and backend boundary.

Required follow-up: None.

## Related Artifacts

- [`../../architecture/products/openproject/README.md`](../../architecture/products/openproject/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
