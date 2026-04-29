# Bounded Governed AI Runtime Assist Activation Review

## Summary

- date: 2026-04-29
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.platform-engineering`
  - `repos.workspace-governance`
- decision: `approved-with-findings`

This review evaluates the first concrete activation contract for bounded
governed AI runtime assists under delivery `#251`. It approves the platform
contract shape and sequencing discipline. It does not approve live runtime
activation or direct provider use.

## Scope Delta

### Design Intent

- bounded AI runtime assists must use platform-owned governed profile and access
  truth instead of repo-local AI policy
- consumer repos should not activate AI-assist behavior until profile,
  invocation, identity, audit, approval, egress, and rollback gates are proven
- operator approval must remain the authority for governance decisions even when
  model output is structurally valid

### Implemented Control

- `platform-engineering` now defines
  `security/governed-ai-runtime-assist-contract.yaml`
- the contract binds runtime-assist activation to:
  - approved model-profile selection
  - governed invocation path
  - caller and operator identity separation
  - minimum audit fields
  - direct-provider egress denial
  - environment activation gates
  - suspension and rollback gates
- `platform-engineering` validates the runtime-assist contract from
  `scripts/validate_ai_model_profiles.py`
- `platform-engineering` documents that the profile registry alone is not live
  activation authority

### Operating Evidence

- the current profile remains `suspended`
- the runtime-assist contract status is `blocked`
- the contract references this delta review as current security evidence
- there is no approved live access plane, model invocation, provider secret
  placement, or runtime deployment in this slice

## Review Areas

### Identity

- the contract correctly separates caller identity from operator acceptance
  identity
- live activation remains blocked until the access plane proves both identities
  in emitted audit records

### Secrets

- direct provider credentials remain disallowed in consumers
- this review does not approve provider-secret placement outside the governed
  access plane

### Delivery

- `platform-engineering` is the correct owner for the activation contract and
  profile registry
- `workspace-governance` must remain a consumer of the platform contract rather
  than cloning governed-model policy in repo-local validators
- downstream delivery items such as `#356` and `#359` must stay dependency
  blocked until the platform contract, security review, and access-plane
  prerequisite are complete

### Runtime

- no live runtime change is approved by this review
- environment activation must start in dev-integration only after the contract's
  activation gates are proven for the profile and caller
- stage and production use require governed promotion evidence and release
  authority approval

### AI

- the bounded assist remains suggestion-only and must use structured output
  contracts
- model output must not directly mutate active platform, workspace, product, or
  component contracts
- human approval remains required for governance decisions

## Decision

`approved-with-findings`

Approved because the platform contract creates an explicit control surface for
runtime-assist activation and prevents premature governed-AI claims.

Findings and residual risk:

1. Live activation remains blocked until the governed access plane, caller
   identity, audit retention, provider-egress block, and rollback path are
   implemented and proven.
2. `workspace-governance` must consume this platform contract and profile
   registry; it must not create independent repo-local governed-AI policy.
3. Delivery `#356` and milestone `#359` must remain dependency-blocked until
   platform, security, and access-plane evidence is complete.

## Related Artifacts

- `platform-engineering/security/governed-ai-runtime-assist-contract.yaml`
- `platform-engineering/security/governed-ai-model-profiles.yaml`
- `platform-engineering/docs/standards/governed-ai-access-model.md`
- `platform-engineering/docs/records/change-records/2026-04-29-governed-ai-runtime-assist-contract.md`
- `security-architecture/docs/standards/ai-security-and-governance.md`
- `security-architecture/docs/reviews/platform/2026-04-18-governed-ai-intake-assist-and-model-profiles.md`
- `security-architecture/docs/reviews/platform/2026-04-24-governed-ai-model-access-and-audit-contract.md`
