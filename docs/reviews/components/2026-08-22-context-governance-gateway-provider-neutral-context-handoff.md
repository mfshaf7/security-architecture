# Context Governance Gateway Provider-Neutral Context Handoff Security Delta

## Summary

- date: 2026-08-22
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.context-governance-gateway`
  - `components.context-governance-gateway`
- ART items:
  - `openproject://work_packages/945`
  - `openproject://work_packages/946`
- reviewed implementation:
  - `context-governance-gateway` PR #16
  - merge commit `c06452ddcf2dedd71299db623c39578142deb89c`
- architecture evidence:
  - `wgcf://artifacts/delivery-art/sha256/3a527075c2e8de2c4fb4eea3237f80bc539b832e4477f3e9021b85b4ddc1e131`
- decision: `approved`

This review approves the merged provider-neutral CGG context handoff as a
dormant source contract. It does not approve a network integration, model or
provider selection, provider credential custody, model invocation, raw context
projection, canonical-state mutation, or runtime activation.

## Scope Delta

### Design Intent

CGG should admit and project safe context without learning which model provider
or AI harness ultimately consumes it. The platform governed AI gateway retains
model-profile resolution, provider routing, credential custody, invocation,
and invocation audit authority.

The approved handoff contains exactly:

- `packet_ref`
- `redaction_receipt_ref`
- `content`

The packet and receipt must describe the same admitted artifact before CGG can
produce that handoff.

### Implemented Control

The exact merged source at `c06452ddcf2dedd71299db623c39578142deb89c`:

- removes the LiteLLM, OpenClaw, Ollama, and Codex-style provider adapters
- adds one `GovernedAiGatewayContextAdapter`
- keeps the human operator projection separate from the gateway projection
- rejects non-model-safe packets and raw projection
- requires valid packet and receipt digests and matching artifact digests
- requires matching policy profile and raw-projection decisions
- removes source metadata from downstream packet references
- closes the gateway handoff and packet-reference schemas against additional
  fields
- performs no network call, model selection, credential access, or invocation

### Operating Evidence

Evidence for this delta is immutable source and validation evidence only:

- CGG PR #16 merged at the exact reviewed commit
- all 30 CGG unit tests passed on PR head
  `487e6d8b9885e59f30d0c46f42266a1881c956b2`
- GitHub validation passed for PR #16
- the finalized Review Packet for work item #945 binds the source head and
  merge commit

No deployed consumer, gateway call, model call, or live handoff is claimed.

## Review Areas

### Identity

No human or machine identity is added. A future runtime consumer must identify
itself to CGG and the governed AI gateway under separately reviewed caller and
operator attribution controls.

### Secrets

The handoff contains a model-safe excerpt and reference paths only. Provider
credentials and raw artifact locations are absent. Existing CGG findings about
deterministic redaction and local raw-artifact custody remain unchanged; this
source contract does not broaden either boundary.

### Delivery

The security decision binds the immutable CGG merge commit rather than a
mutable branch. CGG remains context-projection authority only and cannot use
this handoff to mutate ART, product state, workspace contracts, platform
release state, or security decisions.

### Runtime

The reviewed adapter is dormant. It does not call the governed AI gateway and
does not activate a stage, production, or shared-service path. Any later
consumer wiring must receive a fresh review against the actual caller identity,
network path, release artifact, rollback control, and operating evidence.

### AI

Provider-specific selection has been removed from CGG. The platform gateway
must still resolve an approved logical model profile and enforce its own
authorization, credential, egress, structured-output, audit, and human-approval
contracts. CGG safe context remains untrusted model input and is not approval
or action authority.

## Decision

`approved`

Approved for dormant source use because the exact merged implementation narrows
the handoff to a provider-neutral three-field contract, validates packet and
receipt integrity before projection, removes raw source metadata, and contains
no invocation or mutation behavior.

This decision does not supersede the findings or stage/prod denials in the
active dev-integration review. Runtime activation requires a new delta that
proves:

1. admitted caller identity and operator attribution
2. approved logical model-profile resolution in the platform gateway
3. authorized packet and receipt dereferencing
4. gateway-owned provider credentials and provider egress
5. invocation audit and structured output validation
6. no direct-provider or raw-context bypass

## Related Artifacts

- [`2026-05-05-context-governance-gateway-active-devint-runtime.md`](2026-05-05-context-governance-gateway-active-devint-runtime.md)
- [`../../architecture/components/context-governance-gateway/README.md`](../../architecture/components/context-governance-gateway/README.md)
- [`../../architecture/components/context-governance-gateway/service-mode-security-requirements.md`](../../architecture/components/context-governance-gateway/service-mode-security-requirements.md)
- [`../../standards/ai-security-and-governance.md`](../../standards/ai-security-and-governance.md)
- `context-governance-gateway/contracts/schemas/governed-ai-context-handoff.schema.json`
- `context-governance-gateway/packages/context_adapters/src/context_adapters/gateway.py`
- `context-governance-gateway/packages/context_adapters/src/context_adapters/authority.py`
- `context-governance-gateway/tests/test_adapter_foundation.py`
