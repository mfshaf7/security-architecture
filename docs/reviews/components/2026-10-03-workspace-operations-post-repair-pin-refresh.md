# Workspace Operations Post-Repair Pin Refresh

## Summary

- date: 2026-10-03
- owner repo: `security-architecture`
- affected review subject:
  - `repos.platform-engineering`
- predecessor reviews:
  - [`2026-10-03-workspace-intake-inventory-runtime-helper-reacceptance.md`](2026-10-03-workspace-intake-inventory-runtime-helper-reacceptance.md)
  - [`2026-10-03-dev-integration-smoke-distinct-secret-correction.md`](2026-10-03-dev-integration-smoke-distinct-secret-correction.md)
- related improvement candidate:
  `workspace-governance/reviews/improvement-candidates/2026-10-03-post-merge-review-packet-architecture-recovery-regression.yaml`
- decision: `approved`

The existing Workspace Intake and Inventory GitHub App token expired during a
long recovery session and correctly returned `401`. Platform cannot issue a
replacement under stale exact-source pins, because the admitted OOS and
Security revisions have advanced through reviewed repairs. This review accepts
one metadata-only Platform pin refresh to the exact set below and subsequent
normal short-lived token rotation.

The App identity, installation, repository, permissions, branch namespaces,
write paths, runtime mount, caller, and mutation authority do not change.

### Exact Source Binding

| Owner | Accepted revision | Workspace-operations judgment |
| --- | --- | --- |
| Workspace Governance | [`c41724986ca1290029555010d9a252f869434c6c`](https://github.com/mfshaf7/workspace-governance/commit/c41724986ca1290029555010d9a252f869434c6c) | Changes since the prior pin are Delivery ART v5 governance and improvement records; Intake and active-inventory authority files are unchanged. |
| Workspace Governance Control Fabric | [`f296a8bf91bcc22272f0079cf2b0aec6fe431fdf`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/f296a8bf91bcc22272f0079cf2b0aec6fe431fdf) | Changes since the prior pin are Delivery ART v5 custody/readiness; Workspace operations routes and caller boundary are unchanged. |
| Operator Orchestration Service | [`e71de03fa851c94246cc9b8e739cebfd102c8dec`](https://github.com/mfshaf7/operator-orchestration-service/commit/e71de03fa851c94246cc9b8e739cebfd102c8dec) | Includes the separately approved distinct-secret smoke repair; Workspace Intake/Inventory provider, source, route, and mutation contracts are unchanged. |
| Governance Operations Console | [`d17912691a6dd99335c327637eda98c4105d98eb`](https://github.com/mfshaf7/governance-operations-console/commit/d17912691a6dd99335c327637eda98c4105d98eb) | Unchanged from the prior acceptance. |
| Security Architecture | eventual merge containing this review | Supplies the current exact-source acceptance; the review cannot pre-authorize its own future merge commit. |
| Platform Engineering | [`9feeeba3a8c586efe4418b822ae2511c8f361017`](https://github.com/mfshaf7/platform-engineering/commit/9feeeba3a8c586efe4418b822ae2511c8f361017) plus the dependent pin-only update | Adds composition preflight and smoke context without changing the App identity; the dependent commit may update only the accepted source and review references across existing pin surfaces. |

## Scope Delta

### Design Intent

- Keep exact-source issuance fail closed after owner revisions change.
- Rotate the expired one-hour installation token through the existing Platform
  operator surface.
- Preserve one-repository selection and the existing loopback-only
  dev-integration runtime.
- Use authenticated Inventory registry smoke as operating evidence after
  rotation, not as a substitute for source review.

### Implemented Control

The dependent Platform change may update the existing Workspace operations
identity contract, schema constant, Console activation policy, and operator
documentation to the exact accepted revisions above and this review's eventual
merge commit. No other identity field or authority may change.

Platform's existing issuer must still validate the definition, App,
installation, immutable repository id, owner id, exact permissions, no events,
one-repository token scope, selected runtime profile/session, and exact source
set before projecting a short-lived token.

### Operating Evidence

The failed provider call is valid expiry evidence: the mounted token returned
GitHub `401` while OOS preserved a bounded `workspace_inventory_provider_rejected`
response. It is not evidence of source or authority failure.

Positive operating evidence is pending the approved pin refresh, normal token
delivery, composed OOS readiness, and successful composition-aware Inventory
registry smoke. Secret values must remain absent from receipts and logs.

## Review Areas

### Identity

No identity changes. The existing Workspace operations App remains selected to
exactly `mfshaf7/workspace-governance` repository id `1212447211`. The expired
token is replaced, not extended or reused.

### Secrets

No new durable secret or custody path is introduced. Platform reads the
existing private key from its existing Vault path and projects one new
short-lived installation token through the existing Kubernetes Secret volume.
The expired token is invalid and may be replaced by the existing rotation
flow.

### Delivery

Exact-source pinning remains mandatory. Agent Gary must author the Platform pin
refresh, the accountable human must approve and merge it, and only the merged
revision may be treated as durable source. The final live proof may run from
the reviewed Platform branch but must be repeated from merged `main`.

### Runtime

The runtime remains loopback-only dev-integration. Composition preflight and
context-aware smoke add earlier failure and stronger read-only evidence; they
do not add runtime authority. An expired or rejected token continues to fail
closed.

### AI

No model call, prompt boundary, model-selected action, or AI approval authority
is introduced or changed.

## Findings And Activation Conditions

No finding or accepted risk is created. Token delivery and runtime proof require:

1. the dependent Platform source contains only the approved composition
   controls and exact pin/reference refresh;
2. the executing Platform checkout is clean and passed its owner validation;
3. the identity issuer validates the exact owner revision set;
4. the token remains one-repository, short-lived, and secret-free in evidence;
5. OOS readiness and composition-aware Inventory registry smoke pass; and
6. the same proof is repeated from merged Platform `main`.

Any App, installation, repository, permission, path, caller, mutation, custody,
listener, stage, or production change requires another review.

## Decision

`approved`

Approved:

- the exact owner revision set above;
- one dependent Platform pin/reference refresh;
- normal rotation of the expired installation token; and
- loopback dev-integration reconciliation and read-only operating proof.

Not approved:

- bypassing exact-source validation;
- reusing or exposing the expired token;
- changing App permissions, repository scope, write paths, callers, or
  mutation authority; or
- stage or production activation.

## Related Artifacts

- [Workspace operations identity operator surface](https://github.com/mfshaf7/platform-engineering/blob/9feeeba3a8c586efe4418b822ae2511c8f361017/docs/components/operator-orchestration-service/workspace-intake-identity.md)
- [Security delta review process](../security-delta-review-process.md)
- [Distinct-secret correction](2026-10-03-dev-integration-smoke-distinct-secret-correction.md)
