# Governed AI Gateway Component Security Baseline

## Summary

- date: 2026-05-06
- owner repo: `security-architecture`
- affected review subjects:
  - `components.governed-ai-gateway`
  - `repos.platform-engineering`
- related platform review:
  - [`../platform/2026-05-06-governed-ai-gateway-devint-runtime.md`](../platform/2026-05-06-governed-ai-gateway-devint-runtime.md)
- decision: `approved-with-findings`

This component baseline records `governed-ai-gateway` as an active shared
platform component in the workspace security review inventory. The platform
review remains the detailed delta review for the dev-integration runtime
implementation. This component review binds that decision to the component
coverage model required by workspace governance.

The approval is limited to local `dev-integration` runtime proof. It does not
approve live governed workspace AI consumption, direct provider access by
workspace consumers, stage promotion, production promotion, or autonomous
mutation of workspace truth.

## Component Boundary

`governed-ai-gateway` is the platform-owned access-plane component that
constrains bounded AI consumers before any model or provider interaction is
allowed to affect operator workflows.

The component boundary is:

- caller identity admission at the gateway request boundary
- provider credential custody inside the gateway runtime namespace
- local audit event emission for each admitted or denied request
- consumer network path through the gateway only
- direct-provider egress denial from governed consumer namespaces

The component must not become:

- a workspace-governance contract owner
- a Workspace Delivery ART mutation authority
- a security approval authority
- a custom model provider
- a bypass path around governed model profiles

## Implemented Control

The approved local dev-integration implementation provides:

- a `governed-ai-gateway` dev-integration profile owned by
  `platform-engineering`
- gateway readiness and custody endpoints
- provider token custody through a gateway-only Kubernetes Secret
- PVC-backed local audit ledger events
- caller identity capture in the audit event
- a consumer probe namespace with default-deny egress plus gateway/DNS allow
- a provider sentinel namespace used only to prove direct-provider bypass denial

The component is active in workspace inventory only as a profile-gated external
owner. Active component status does not mean live model consumption is active.

## Operating Evidence

Accepted dev-integration evidence is produced by the shared platform runner:

- `make devint-up PROFILE=governed-ai-gateway`
- `make devint-smoke PROFILE=governed-ai-gateway`
- `make devint-status PROFILE=governed-ai-gateway`
- `make devint-promote-check PROFILE=governed-ai-gateway`

Required smoke evidence:

- gateway runtime is ready
- governed consumer can reach the gateway
- gateway policy decision is recorded
- caller identity is captured
- provider Secret exists in gateway custody
- provider token is not projected to consumers
- direct provider sentinel is not reachable from the consumer probe

## Findings

1. Live governed intake-assist remains blocked until `intake-classifier-v1`
   has an active approved model profile and a reviewed workspace consumer
   contract.
2. The provider sentinel proves the local network boundary only. A real
   provider route still requires a later security review before stage or
   production use.
3. Any evidence showing consumer reachability to the provider sentinel is an
   activation blocker.

## Related Artifacts

- `platform-engineering/dev-integration/profiles/governed-ai-gateway/profile.yaml`
- `platform-engineering/docs/components/governed-ai-gateway/README.md`
- `platform-engineering/security/governed-ai-access-plane.yaml`
- `platform-engineering/security/governed-ai-devint-egress-policy.yaml`
- `platform-engineering/security/governed-ai-runtime-assist-contract.yaml`
- `platform-engineering/docs/records/change-records/2026-05-06-governed-ai-gateway-devint-runtime.md`
- `workspace-governance/contracts/components.yaml`
- `workspace-governance/contracts/developer-integration-profiles.yaml`
