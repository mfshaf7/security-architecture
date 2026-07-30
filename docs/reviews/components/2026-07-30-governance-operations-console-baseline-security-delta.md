# Governance Operations Console Baseline Security Delta

## Summary

- date: 2026-07-30
- owner repo: `security-architecture`
- affected review subject:
  - `repos.workspace-prototype-studio`
- ART item: `openproject://work_packages/769`
- source landing unit: `openproject://work_packages/768`
- source commit:
  [`aa12fdb`](https://github.com/mfshaf7/workspace-prototype-studio/commit/aa12fdbb9b4f7b16c8ac2d2229c4dd4f6c95ec98)
- source review:
  [workspace-prototype-studio#2](https://github.com/mfshaf7/workspace-prototype-studio/pull/2)
- decision: `approved-with-findings`

This delta approves the Governance Operations Console as a local, loopback-only
prototype baseline. It permits bounded read-only host telemetry, synthetic
operator identity display, and manual operator interaction with a local Ollama
runtime under the implemented prototype controls.

It does not approve shared or external exposure, authenticated identity
authority, secrets, real client data, mutable backend integration, tools or
autonomous action, governed AI status, production deployment, or stage/prod
release.

## Scope Delta

### Design Intent

- Establish a reviewable source and interface baseline for the Governance
  Operations Console before live integration begins.
- Keep operator workflows and operational projections synthetic or local while
  preserving explicit authority boundaries for future backend wiring.
- Allow a local assistant for manual, suggestion-only interaction without
  claiming governed model access or operational action authority.
- Display local runtime readiness without granting host mutation capability.

### Implemented Control

The reviewed candidate provides:

- a Next.js development command bound to `127.0.0.1:3317`
- a read-only runtime-readiness route sourced from `/proc`, filesystem
  statistics, and Node OS telemetry
- no host-control, shell execution, write, or privileged action path
- an agent request policy with a 2,000-character prompt limit, a bounded
  16-message and 6,000-character history, structured context validation, and
  rejection of common secret-like material
- synthetic-context-only model projection; live and source-projected context is
  denied pending Context Governance Gateway admission
- local Ollama discovery with a 260-token response limit and no tool schema,
  action adapter, or mutation capability
- browser-memory-only transcript and conversation state
- a typed identity projection whose active fixture is synthetic,
  `not-authenticated`, and `unverified`, and which cannot establish trusted
  operator authority
- architecture guards and semantic tests that preserve the local/source
  projection boundaries

### Operating Evidence

The reviewed evidence is source and local validation only:

- source candidate commit `aa12fdb`
- draft source PR `workspace-prototype-studio#2`
- `make validate` passes
- 330 semantic tests pass
- TypeScript validation passes
- the Next.js 15.5.22 production build passes
- `npm audit --omit=dev` reports zero known vulnerabilities
- no shared, stage, prod, or externally reachable deployment evidence exists

## Review Areas

### Identity

The Console does not implement authentication or authorization. Its current
operator identity is a synthetic attribution fixture and is correctly
projected as prototype-local rather than trusted. It must not authorize
commands, backend mutations, data access, or approvals.

Any shared or live integration requires a real identity source, authenticated
session handling, server-side authorization, role and authority mapping,
expiry handling, and auditable operator attribution.

### Secrets

No application secret is required for the reviewed local Ollama path. The
request policy rejects several common private-key, token, password, and bearer
patterns from prompts, history, and context candidates. This is a containment
control, not a secret-scanning or data-loss-prevention guarantee.

Operators must not enter secrets or sensitive operational exports. Any future
provider credentials require approved custody, delivery, rotation, and egress
controls outside Prototype Studio.

### Delivery

This decision covers source-baseline approval only. Prototype Studio remains an
incubation owner and is not a deployment or release authority. The source PR
must bind this review before merge, and later live integration must be
decomposed into governed delivery work with its own review evidence.

### Runtime

The runtime-readiness endpoint reads local CPU, memory, disk, uptime, hostname,
and interface counters. It is acceptable only on the loopback development
surface. Hostname and interface names are operational metadata and must not be
exposed through a shared route without authentication, authorization, response
minimization, and audit.

The local model adapter may connect to the configured Ollama URL, the WSL
gateway, `host.docker.internal`, or loopback. This approval does not permit
arbitrary provider egress, externally supplied endpoints in a shared runtime,
or privileged host access.

### Visibility

The Console reports model provider state, selected model, context policy
decision, and local runtime readiness. Those displays are prototype
observations, not deployment attestations. The current browser-memory
transcript is not a durable audit trail.

Any governed runtime requires version and deployment identity, durable
operator-attributed audit evidence, bounded log access, and health data from
the authoritative runtime surface.

### AI

The assistant is a prototype-local, suggestion-only system. It has no tools,
mutation adapter, approval authority, or autonomous trigger. Only manual
operator prompts and explicitly synthetic context may reach the local model.

This is not a governed AI profile or governed model-access path. Live or
source-projected context must remain denied until Context Governance Gateway
admission is wired. Shared activation also requires an approved model profile,
identity and access controls, provider egress controls, durable audit, and
review of output-to-action boundaries.

## Findings

1. `GOC-SEC-01`: Local Ollama invocation bypasses the governed AI access plane.
   This is accepted only for loopback prototype use with synthetic context and
   no tools. It must be replaced before shared or governed runtime activation.
2. `GOC-SEC-02`: The Console has no trusted identity or server-side
   authorization. The synthetic identity display must remain non-authoritative
   until a reviewed identity integration lands.
3. `GOC-SEC-03`: Runtime readiness exposes local hostname and interface names.
   Loopback use is acceptable; shared exposure requires authenticated access
   and response minimization.
4. `GOC-SEC-04`: Agent interaction evidence is browser-memory-only. A governed
   runtime requires durable, bounded, operator-attributed audit evidence.

The findings are expansion gates, not blockers to the reviewed source
baseline. They must be routed into the later Live Integration and Deployment
work before those boundaries are activated.

## Decision

`approved-with-findings`

The baseline is approved because its implemented controls keep the
security-significant behavior local, bounded, non-mutating, visibly synthetic,
and separate from governed runtime authority.

Approval is limited to:

- local loopback development
- private prototype evaluation
- read-only local host telemetry
- synthetic and mock operational data
- synthetic, unauthenticated identity display
- manual suggestion-only local Ollama interaction
- explicitly synthetic, budgeted context

Approval excludes:

- shared, client-visible, stage, or production exposure
- real identity or authorization claims
- secrets or real client data
- mutable canonical-backend integration
- tools, autonomous action, or approval authority
- live or source-projected model context
- governed AI or governed deployment status

## Related Artifacts

- [Workspace Prototype Studio product-incubation baseline](2026-05-06-workspace-prototype-studio-product-incubation-baseline.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
- [Governance Operations Console source candidate at `aa12fdb`](https://github.com/mfshaf7/workspace-prototype-studio/tree/aa12fdbb9b4f7b16c8ac2d2229c4dd4f6c95ec98/apps/governance-operations-console)
- [Baseline candidate review at `aa12fdb`](https://github.com/mfshaf7/workspace-prototype-studio/blob/aa12fdbb9b4f7b16c8ac2d2229c4dd4f6c95ec98/docs/prototypes/governance-operations-console/baseline-candidate-review.md)
