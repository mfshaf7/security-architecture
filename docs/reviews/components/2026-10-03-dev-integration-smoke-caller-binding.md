# Dev-Integration Smoke Caller Binding Security Delta

## Summary

- date: 2026-10-03
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `components.operator-orchestration-service`
- predecessor reviews:
  - [`2026-10-03-delivery-art-architecture-v5-evidence-ownership.md`](2026-10-03-delivery-art-architecture-v5-evidence-ownership.md)
  - [`2026-10-03-workspace-intake-inventory-runtime-helper-reacceptance.md`](2026-10-03-workspace-intake-inventory-runtime-helper-reacceptance.md)
- owner change:
  [operator-orchestration-service#273](https://github.com/mfshaf7/operator-orchestration-service/pull/273),
  merged as [`9ee6d3517124f3ba2ddfe51b97a40bc2345a5348`](https://github.com/mfshaf7/operator-orchestration-service/commit/9ee6d3517124f3ba2ddfe51b97a40bc2345a5348)
- related improvement candidate:
  `workspace-governance/reviews/improvement-candidates/2026-10-03-post-merge-review-packet-architecture-recovery-regression.yaml`
- decision: `approved`

The exact OOS revision above is approved for the existing loopback-only
`accepted-idea-delivery` dev-integration profile. It binds the already allowed
`accepted-idea-delivery-smoke` caller to its existing profile-private secret so
the caller can use the read-only Workspace Inventory registry route.

This is a caller-binding correction, not a new caller, credential, route,
permission, mutation capability, or control plane. The registry continues to
reject callers that have only the compatibility shared secret and no bound
caller identity.

## Scope Delta

### Design Intent

- Preserve caller-specific authentication for Workspace Inventory registry
  reads.
- Keep the existing `accepted-idea-delivery-smoke` caller bounded to the
  profile's existing private credential.
- Let composition-aware smoke exercise the real authenticated route instead
  of reporting the profile inactive and skipping the check.
- Preserve invalid and unbound caller denial without adding a compatibility
  bypass.

### Implemented Control

OOS now includes `caller_id: caller_secret` in the generated
`CALLER_AUTH_SECRETS_JSON` for the accepted-delivery host service. The same
secret remains the profile's existing `CALLER_AUTH_SHARED_SECRET` for
compatibility with routes that still accept that mode; no second secret is
created or projected.

The profile regression test requires the caller-specific mapping. The focused
profile and Inventory route tests passed seven of seven tests. The full OOS
suite completed 1,195 tests with 1,193 passes, no failures, and two intentional
skips. The required GitHub validation passed on exact pull-request head
`4e84c914a4400142c48dc6e2b185115ef3d670d4`, and the accountable human
approved that exact head before merge.

### Operating Evidence

The pre-fix composed smoke is valid negative evidence: with matching secret
digests in OOS and WGCF, the registry returned `403 caller_identity_unbound`.
That proves the route failed closed rather than accepting the shared secret as
a caller identity.

Positive operating evidence remains a post-review activation step. Platform
must reconcile the exact merged OOS revision into the existing composition and
the composition-aware smoke must pass without weakening the registry policy.

## Review Areas

### Identity

No identity is added. The existing smoke caller moves from allowed-but-unbound
configuration to an exact caller-to-secret binding. The registry's
`assertCallerIdentityBound` control remains unchanged and continues to reject
unbound callers.

### Secrets

No secret, Vault path, file path, projection, lifetime, or custody boundary is
added or changed. The profile reuses its existing private caller secret in the
caller-specific map. Secret values remain absent from source and evidence.

### Delivery

Agent Gary authored OOS PR #273, the accountable human approved the exact
head, the required check passed, and the change was squash-merged to protected
`main`. Platform may activate only the exact merged revision identified above.

### Runtime

The change affects only the existing loopback dev-integration host service.
It does not add an endpoint, mutation path, namespace, external listener,
deployment lane, or production posture. The expected post-activation proof is
an authenticated read-only registry response plus continued denial for an
invalid or unbound caller.

### AI

No model call, prompt path, model-selected action, or AI approval authority is
introduced or changed.

## Threat And Control Mapping

| Threat | Reviewed control | Judgment |
| --- | --- | --- |
| Shared-secret possession is mistaken for caller identity | registry still requires a caller-specific binding | sufficient |
| Smoke bypasses the real route because composition context is missing | Platform's composition-aware smoke must exercise the existing authenticated registry route | required activation evidence |
| Repair broadens caller or route authority | only the existing smoke caller is mapped to its existing secret; route policy and permissions are unchanged | sufficient |
| Secret material leaks into source or evidence | source records only the environment-variable relationship; no value is recorded | sufficient |

## Residual Risk And Activation Conditions

No security finding or accepted risk is created by this delta. Activation is
conditional on all of the following:

1. the composition uses OOS merge `9ee6d3517124f3ba2ddfe51b97a40bc2345a5348`;
2. the existing private runtime credential is reused without value exposure;
3. the composition-aware smoke successfully reads the Inventory registry; and
4. invalid or unbound caller denial remains covered by the existing route
   tests.

A change to caller identity, secret custody, route authorization, mutation
scope, listener exposure, or runtime lane requires another delta review.

## Decision

`approved`

Approved:

- OOS merge `9ee6d3517124f3ba2ddfe51b97a40bc2345a5348`;
- caller-specific binding for the existing
  `accepted-idea-delivery-smoke` caller;
- reuse of the existing profile-private secret for that exact binding; and
- reconciliation into the existing loopback-only dev-integration composition
  followed by positive smoke evidence.

Not approved:

- treating the shared compatibility secret as caller identity;
- adding callers, secrets, permissions, routes, mutations, or deployment
  lanes;
- bypassing the registry's caller-binding requirement; or
- claiming operating readiness from source and CI evidence alone.

## Related Artifacts

- [OOS owner change record](https://github.com/mfshaf7/operator-orchestration-service/blob/9ee6d3517124f3ba2ddfe51b97a40bc2345a5348/docs/records/change-records/2026-10-03-devint-smoke-caller-binding.md)
- [Security delta review process](../security-delta-review-process.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Secrets and recovery architecture](../../architecture/domains/secrets-and-recovery.md)
