# Dev-Integration Smoke Distinct Secret Correction

## Summary

- date: 2026-10-03
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `components.operator-orchestration-service`
- superseded review:
  [`2026-10-03-dev-integration-smoke-caller-binding.md`](2026-10-03-dev-integration-smoke-caller-binding.md)
- owner changes:
  - [operator-orchestration-service#273](https://github.com/mfshaf7/operator-orchestration-service/pull/273), merge `9ee6d3517124f3ba2ddfe51b97a40bc2345a5348`
  - [operator-orchestration-service#274](https://github.com/mfshaf7/operator-orchestration-service/pull/274), merge [`e71de03fa851c94246cc9b8e739cebfd102c8dec`](https://github.com/mfshaf7/operator-orchestration-service/commit/e71de03fa851c94246cc9b8e739cebfd102c8dec)
- related improvement candidate:
  `workspace-governance/reviews/improvement-candidates/2026-10-03-post-merge-review-packet-architecture-recovery-regression.yaml`
- decision: `approved`

The prior review correctly required caller-specific identity but incorrectly
accepted reuse of the compatibility shared-secret value. Exact-source
reconciliation proved that OOS rejects this ambiguity at startup. Its activation
conditions were not met, so that revision is not approved for activation.

The exact corrected OOS revision above is approved for the existing
loopback-only `accepted-idea-delivery` dev-integration profile. It retains the
existing smoke identity and creates one separate, locally generated
compatibility secret so the caller-specific credential is unambiguous.

## Scope Delta

### Design Intent

- Preserve the registry's caller-bound identity requirement.
- Preserve compatibility for existing local routes without allowing the
  compatibility secret to identify a caller.
- Generate both values inside the existing private profile state boundary.
- Reject empty, duplicate, or shared caller credentials before the profile's
  first Helm or Kubernetes mutation.

### Implemented Control

`BROKER_CALLER_SECRET` remains the existing smoke caller's private credential.
The profile now generates `BROKER_SHARED_SECRET` separately and supplies it
only as `CALLER_AUTH_SHARED_SECRET`. A pre-mutation profile check proves that
all caller-specific credentials are non-empty, mutually distinct, and
different from the compatibility secret. OOS retains its independent runtime
configuration rejection as defense in depth.

OOS PR #274 passed the focused identity, configuration, and Inventory tests,
the complete 1,195-test suite with 1,193 passes and two intentional skips, the
required GitHub check, and exact-head human approval before merge.

### Operating Evidence

The failed exact-source rollout of merge `9ee6d3517124f3ba2ddfe51b97a40bc2345a5348`
is valid negative evidence: OOS entered `CrashLoopBackOff` with the explicit
distinct-secret validation error before serving requests. This demonstrates
that the runtime failed closed.

Positive evidence remains required after this review: Platform must reconcile
merge `e71de03fa851c94246cc9b8e739cebfd102c8dec`, observe OOS readiness, and
complete the composition-aware Inventory registry smoke.

## Review Areas

### Identity

No caller or authority is added. The existing smoke caller now has one exact
caller-specific credential, and the compatibility secret cannot satisfy
caller-bound routes.

### Secrets

One new local-only generated secret value separates compatibility from caller
identity. It uses the existing `0600` profile state file and existing
Kubernetes Secret projection, does not enter source or evidence, and follows
the profile's existing reset lifecycle. No Vault path, external credential,
provider identity, or durable cross-environment secret is added.

### Delivery

Agent Gary authored both repair PRs; the accountable human reviewed and merged
them through protected `main`. Only OOS merge
`e71de03fa851c94246cc9b8e739cebfd102c8dec` is approved for activation. The
pre-mutation check prevents a repeated ambiguous projection from reaching the
cluster.

### Runtime

The change remains limited to the loopback dev-integration host service. It
adds no endpoint, permission, mutation, namespace, listener, stage posture, or
production posture. OOS startup and the profile pre-mutation check both reject
secret ambiguity.

### AI

No model call, prompt path, model-selected action, or AI approval authority is
introduced or changed.

## Threat And Control Mapping

| Threat | Reviewed control | Judgment |
| --- | --- | --- |
| Compatibility secret impersonates a bound caller | distinct generated values plus OOS runtime rejection | sufficient |
| Bad local state reaches the cluster | profile validates all projected caller secrets before Helm or Kubernetes mutation | sufficient |
| Repair silently widens authority | caller id, routes, permissions, and mutation boundaries remain unchanged | sufficient |
| New local secret leaks | existing private file and Kubernetes Secret custody; values excluded from source and evidence | sufficient |

## Residual Risk And Activation Conditions

No finding or accepted risk remains for this bounded correction. Activation
requires:

1. exact OOS merge `e71de03fa851c94246cc9b8e739cebfd102c8dec`;
2. successful pre-mutation distinct-secret validation;
3. a ready OOS deployment; and
4. successful composition-aware Inventory registry smoke.

Any broader secret custody, caller, authorization, listener, or environment
change requires another delta review.

## Decision

`approved`

Approved:

- OOS merge `e71de03fa851c94246cc9b8e739cebfd102c8dec`;
- one separate locally generated compatibility secret;
- the existing smoke caller's distinct caller-specific credential;
- pre-mutation and runtime ambiguity rejection; and
- exact-revision loopback dev-integration reconciliation and smoke.

Not approved:

- activation of the superseded reused-secret revision;
- using the compatibility secret as caller identity;
- exposing either value in source or evidence; or
- any new caller, route, permission, mutation, listener, stage, or production
  authority.

## Related Artifacts

- [Corrective OOS change record](https://github.com/mfshaf7/operator-orchestration-service/blob/e71de03fa851c94246cc9b8e739cebfd102c8dec/docs/records/change-records/2026-10-03-devint-smoke-distinct-caller-secret.md)
- [Security delta review process](../security-delta-review-process.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Secrets and recovery architecture](../../architecture/domains/secrets-and-recovery.md)
