# Governance Operations Console Source-Owned Local Preview Security Baseline

## Scope

Review Governance Operations Console as an active source-owned product whose
highest real endpoint is owner-repository local preview.

The reviewed product boundary includes:

- durable source in `governance-operations-console`
- loopback-only local preview on `127.0.0.1:3317`
- fixture-backed or synthetic operational records
- read-only bounded local host telemetry
- synthetic unauthenticated identity
- manual, suggestion-only local Ollama use with synthetic context

It does not include a Platform product integration, live backend, shared
runtime, governed AI path, stage, production, release, public, or
client-visible endpoint.

## Authority

- `governance-operations-console` owns product source, product-local
  validation, and loopback-only local preview.
- `platform-engineering` is the declared platform authority but has no
  Governance Operations Console product integration or runtime surface in this
  baseline.
- `workspace-governance` owns product classification and the active product
  record.
- `security-architecture` owns this review decision and the unresolved
  expansion gates.
- Workspace Prototype Studio retains incubation history and the graduation
  record, not active product source.

## Decision

`approved-with-findings`

Approval is limited to the exact source-owned local-preview boundary described
above. It does not authorize runtime integration or a stronger lifecycle.

## Review Areas

### Identity

The current identity model is synthetic and unauthenticated. It cannot grant
operator authority. Trusted identity and server-side authorization are required
before live data or shared access.

### Secrets

The reviewed source contains no credential-delivery path. Future backend,
model, or platform integration requires reviewed secret custody and must not
move credentials into the browser or source repository.

### Delivery

The product is active because durable source custody and owner-repository
validation exist. It is not platform-integrated or fully governed. Any
Platform product surface, deployment, release, or promotion path requires a
separate reviewed landing.

### Runtime

Local preview remains loopback-only. The repository Dockerfile is build proof,
not runtime admission. Host telemetry remains local and read-only until access
control and response minimization are reviewed.

### AI

The local Ollama path remains manual, suggestion-only, and synthetic-context
only. It is not a governed AI path and has no tool or mutation authority.

## Findings And Expansion Gates

The inherited findings remain open:

1. `GOC-SEC-01`: local Ollama bypasses the governed AI access plane.
2. `GOC-SEC-02`: the Console has no trusted identity or server-side
   authorization.
3. `GOC-SEC-03`: local runtime readiness includes host metadata that requires
   access control and response minimization before sharing.
4. `GOC-SEC-04`: browser-memory agent evidence is not a durable audit trail.

These findings do not block durable source ownership or loopback-only local
preview. They block expansion into the affected shared or governed boundaries.

## Related Artifacts

- [Source-graduation security delta](../components/2026-07-31-governance-operations-console-source-graduation.md)
- [Owner-repository admission review](../components/2026-07-31-governance-operations-console-owner-repository-admission.md)
- [Prototype baseline security delta](../components/2026-07-30-governance-operations-console-baseline-security-delta.md)
- [Security review checklist](../security-review-checklist.md)
- [Owner-repository security boundary](https://github.com/mfshaf7/governance-operations-console/blob/9d8d2f0e550cd14ee915ecdb0aadd5cceddcc38d/docs/security-and-data-boundaries.md)
