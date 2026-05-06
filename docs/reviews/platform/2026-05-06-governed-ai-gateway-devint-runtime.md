# Governed AI Gateway Dev-Integration Runtime Review

## Summary

- date: 2026-05-06
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.platform-engineering`
  - `components.governed-ai-gateway`
- decision: `approved-with-findings`

This review covers the platform-owned `governed-ai-gateway` local
dev-integration runtime profile. It approves using the local profile to prove
gateway readiness, caller identity capture, gateway-owned provider custody,
audit emission, and provider-egress denial.

It does not approve governed workspace consumption or direct provider use.
`intake-classifier-v1` must remain unavailable for live governed use until the
remaining activation gates pass.

## Scope Delta

### Design Intent

- create a concrete gateway boundary for bounded AI consumers instead of
  allowing repo-local provider clients
- prove provider credentials stay in platform gateway custody
- prove caller identity reaches the access-plane boundary
- prove audit events are emitted before model output can influence workspace
  intake records
- prove a governed consumer can reach the gateway but cannot bypass it through
  direct provider egress

### Implemented Control

- `platform-engineering` adds a `governed-ai-gateway` dev-integration profile
  with read-only smoke
- the gateway runtime stores a local provider token in a gateway namespace
  Secret and reports custody metadata without returning the token value
- the gateway emits local PVC-backed audit ledger events with caller identity,
  operator identity, profile id, schema ref, policy decision, and outcome
- the consumer probe namespace applies default-deny egress plus explicit
  allow-to-gateway and DNS policy
- the provider sentinel namespace gives dev-integration a local direct-provider
  bypass target before any real provider route is enabled

### Operating Evidence

- local operating evidence is produced by:
  - `make devint-up PROFILE=governed-ai-gateway`
  - `make devint-smoke PROFILE=governed-ai-gateway`
- smoke must prove:
  - gateway runtime readiness
  - consumer gateway reachability
  - audit event emission
  - caller identity capture
  - provider Secret custody without token projection
  - direct-provider sentinel denial from the consumer probe
- `intake-classifier-v1` remains suspended until workspace consumer activation
  and model/provider selection are complete

## Review Areas

### Identity

The gateway requires caller identity fields at the access-plane request
boundary. Smoke must prove the emitted audit event carries
`workspace-governance/intake-assist` caller identity before the workspace
consumer can use the path.

### Secrets

Provider credentials are allowed only in the gateway namespace Secret. They are
not allowed in workspace-governance, consumer probe namespaces, or intake
contracts. The gateway custody endpoint may report the Secret reference and
custody state, but must not return the provider token value.

### Delivery

The runtime is local `dev-integration` only. Stage and production remain
blocked behind reviewed source changes, platform release authority, and current
security acceptance.

### Runtime

The provider sentinel is acceptable as a dev-integration proof target because
it validates the egress boundary without introducing a real provider dependency
before provider and model selection are approved. If the sentinel is reachable
from the consumer probe, activation must remain blocked.

### AI

The gateway must not let model output mutate canonical workspace truth. Future
workspace consumption must remain suggestion-only and operator-accepted.

## Decision

`approved-with-findings`

Approved for local dev-integration runtime proof because the implementation
creates the missing access-plane operating boundary without activating live
workspace AI consumption.

Findings and residual risk:

1. Live governed intake-assist remains blocked until `intake-classifier-v1` is
   active with a selected upstream model and the workspace consumer contract is
   explicitly opened.
2. Dev-integration provider-sentinel proof is not a substitute for later stage
   provider-route review when a real provider adapter is selected.
3. Any smoke result where the consumer reaches the provider sentinel is a
   blocker, not an accepted-risk posture.

## Related Artifacts

- `platform-engineering/dev-integration/profiles/governed-ai-gateway/profile.yaml`
- `platform-engineering/docs/components/governed-ai-gateway/README.md`
- `platform-engineering/security/governed-ai-access-plane.yaml`
- `platform-engineering/security/governed-ai-devint-egress-policy.yaml`
- `platform-engineering/security/governed-ai-runtime-assist-contract.yaml`
- `platform-engineering/docs/records/change-records/2026-05-06-governed-ai-gateway-devint-runtime.md`
- `workspace-governance/contracts/developer-integration-profiles.yaml`
- `workspace-governance/contracts/governed-intake-assist.yaml`
- `security-architecture/docs/standards/ai-security-and-governance.md`
