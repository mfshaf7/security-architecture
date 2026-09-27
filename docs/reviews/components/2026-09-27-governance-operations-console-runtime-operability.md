# Governance Operations Console Runtime Operability Security Delta

## Summary

- date: 2026-09-27
- owner repo: `security-architecture`
- affected review subject: `repos.governance-operations-console`
- delivery initiative: `openproject://work_packages/898`
- parent feature: `openproject://work_packages/930`
- security evidence item: `openproject://work_packages/1188`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/58d8c0d3b71fa6bba96cc9c2be0a75f534541d521c2a5b16f3e6bc670cfe7d1c`
- decision: `approved-with-findings`

This review approves the exact merged configuration, correlation, bounded-error,
canonical-audit, and runtime-observation source boundary for controlled,
single-operator, loopback `dev-integration` use. It emits the architecture
packet's `gate:trusted-console-operating-ready` gate for that boundary. It does
not approve shared access, federated identity, stage, production, public
exposure, or a claim that workload readiness proves endpoint or workflow
success.

### Exact Source Binding

| Owner | Pull request | Merged source | Reviewed evidence |
| --- | --- | --- | --- |
| Platform Engineering | [platform-engineering#248](https://github.com/mfshaf7/platform-engineering/pull/248) | [`f4475dbd0129961302ff48aea10b751b6b85512a`](https://github.com/mfshaf7/platform-engineering/commit/f4475dbd0129961302ff48aea10b751b6b85512a) | Console runtime contract and private session-projection policy |
| Platform Engineering | [platform-engineering#249](https://github.com/mfshaf7/platform-engineering/pull/249) | [`604a91c4237ecc27e589defb31d16a3fe50a7a0a`](https://github.com/mfshaf7/platform-engineering/commit/604a91c4237ecc27e589defb31d16a3fe50a7a0a) | Session-projection operating evidence |
| Governance Operations Console | [governance-operations-console#37](https://github.com/mfshaf7/governance-operations-console/pull/37) | [`68706368de09f55fd2dba34c6b5b54535348ee19`](https://github.com/mfshaf7/governance-operations-console/commit/68706368de09f55fd2dba34c6b5b54535348ee19) | Central configuration, capability projection, request correlation, bounded errors, and canonical audit projection |
| Platform Engineering | [platform-engineering#250](https://github.com/mfshaf7/platform-engineering/pull/250) | [`0b41233e123f3ebf9ec14753bf01dd3292d22e11`](https://github.com/mfshaf7/platform-engineering/commit/0b41233e123f3ebf9ec14753bf01dd3292d22e11) | Runtime-observation policy, schemas, collector, tests, and operator runbook |
| Governance Operations Console | [governance-operations-console#38](https://github.com/mfshaf7/governance-operations-console/pull/38) | [`231858266bbf8d7152934f673081ff2e90a06573`](https://github.com/mfshaf7/governance-operations-console/commit/231858266bbf8d7152934f673081ff2e90a06573) | Private projection validation, browser-safe readback, Runtime Readiness consumption, and fail-closed tests |
| Operator Orchestration Service | [operator-orchestration-service#238](https://github.com/mfshaf7/operator-orchestration-service/pull/238) | [`23e87b88b2b32a1d4aba06f1718f7f6df11bebce`](https://github.com/mfshaf7/operator-orchestration-service/commit/23e87b88b2b32a1d4aba06f1718f7f6df11bebce) | Canonical Console source projection and receipt-binding readback |

The earlier [Console identity activation review](2026-09-27-governance-operations-console-identity-activation.md)
remains the identity authority for this runtime. This delta reviews the
operability controls added after that decision. A different source revision or
an expanded runtime boundary requires a new review.

## Scope Delta

### Design Intent

- Resolve governed Console integration settings through one server-only
  configuration boundary and expose only non-secret capability posture.
- Give every same-origin API request a fresh server-generated correlation
  identity without turning that identity into authorization or completion
  evidence.
- Keep canonical audit truth in validated owner receipts, events, and readback
  instead of creating a competing Console audit ledger.
- Project admitted Platform workload readiness into Runtime Readiness while
  keeping it separate from local host telemetry, workflow result, release
  readiness, and Security approval.
- Fail closed when configured authority is incomplete, stale, contradictory,
  replayed, unavailable, or malformed.

### Implemented Control

The Console central configuration module is the only product source permitted
to read governed endpoints, caller credentials, operator bindings, private
projection paths, and authority references. Partial live configuration selects
live mode and returns `invalid`; it does not silently fall back to fixtures.
The browser capability projection contains only state and stable reason codes,
not endpoints, paths, principals, credentials, or artifact values.

Middleware replaces caller-supplied correlation values with a new server UUID
for every same-origin API request. Authorized owner calls reuse that identity,
and success, denial, domain error, and unexpected owner failure return the same
bounded reference. Private owner diagnostics stay server-side. Correlation
does not grant authority and is not a receipt.

Canonical activity is projected from validated OOS and owner readback. Local
and synthetic activity stays explicitly labelled and cannot support a durable
mutation or completion claim. OOS remains workflow authority and durable
receipt owner.

Platform publishes `console-runtime-observations/v1` as an operator-owned
`0600` regular file with a bounded validity window. The policy admits six exact
workloads and their recovery owners. The Console server rejects symlinks,
non-regular files, wrong ownership or mode, oversized input, unknown fields,
wrong authority or lane, invalid timestamp ordering, stale evidence,
contradictory replica or capability posture, replay, and same-sequence
conflict. The browser receives only component identity, category, availability,
freshness, observation time, and an opaque observation reference. Kubernetes
references, recovery paths, private file paths, credentials, and collector
diagnostics are excluded.

Configured observation failure projects explicit unavailability. An
unconfigured runtime remains a clearly disconnected preview; fixture catalog
data cannot become live health. CPU, memory, disk, network, and uptime continue
through the independent host-telemetry adapter.

### Operating Evidence

The Console repository passed architecture guards, 443 semantic tests,
TypeScript checking, a production build, dependency installation with zero
reported vulnerabilities, and the full `npm run check` surface at the exact
merged source. Tests cover disconnected, invalid, and live capability states;
secret-safe projection; request correlation; bounded owner failure; unchanged
owner receipts; missing, malformed, stale, contradictory, non-private,
replayed, and conflicting runtime observations; and the Runtime Readiness
projection.

The Platform collector was run against the exact merged Platform source and
projected six admitted components as current and available with no secret
values. The exact merged Console reader consumed that projection as live,
current Platform authority with six available components and no private
details exposed. This is real local producer-to-consumer operating proof for
the bounded observation path.

The proof establishes collector-to-Console workload posture, not endpoint
reachability, business-operation success, deployment approval, or production
availability. Those remain with their owning controls.

## Review Areas

### Identity And Authorization

This delta introduces no new human or machine identity. It inherits the exact
Platform session and Console authorization boundary approved by the identity
activation review. The local operating-system account remains the trust root,
and the server-global projection is not bound to a federated browser session.
The runtime therefore remains controlled, single-operator, and loopback-only.

Runtime availability and correlation identities grant no mutation authority.
Canonical operations still require Console authorization, OOS workflow
authorization, expected-state controls, owner execution, and validated
readback.

### Secrets And Data Handling

The observation projection contains operational metadata, not credentials,
but it remains private server-side data. Its configured path and full contents
must not enter browser bundles, `NEXT_PUBLIC_*` values, logs, fixtures, ART
descriptions, or Review Packets. The Console's bounded projection removes
Kubernetes source references, recovery paths, filesystem paths, and private
diagnostics.

OOS caller credentials and the Platform session projection remain separate
server-only controls. Runtime-observation configuration neither contains nor
replaces them.

### Failure, Freshness, And Replay

Configured missing, unreadable, malformed, stale, contradictory, or replayed
observation truth fails closed and cannot fall back to a fixture success.
Expired observations must be recollected. Same-sequence content conflict is
rejected rather than treated as a newer state.

Platform workload posture can be `available`, `degraded`, or `unavailable`.
Those states describe replica readiness only. An available component may still
reject or fail a workflow, and that result must come from the canonical owner.

### Audit, Errors, And Visibility

The Console supplies a stable cross-layer correlation seam and bounded public
errors without becoming audit authority. A durable claim still requires the
validated owner receipt, event, or source readback. Raw owner errors and
projection internals remain private.

The UI may show Platform workload posture and local host telemetry together,
but their source categories remain explicit and neither may substitute for the
other. Security approval is also separate from both health sources.

### Delivery, Rollback, And Availability

The source order is complete: Platform session authority, Console operability,
Platform observations, Console consumption, and this Security decision landed
in owner order. Rollback remains separable:

1. stop refreshing or remove the private observation projection;
2. remove the Console observation-path configuration;
3. disable the bounded Console runtime; and
4. revert the Console or Platform Landing Unit in reverse owner order if a
   source rollback is required.

Observation rollback does not delete OOS state, owner records, or canonical
receipts. No ingress, shared endpoint, stage, production, or public route is
approved.

### AI

This delta adds no model call, model-selected action, prompt boundary, tool
invocation, or AI approval authority. Existing AI findings remain unchanged.

## Findings And Activation Ceiling

1. **The local operating-system account remains the trust root.** Federated
   identity, MFA, browser-session issuance, remote revocation, and shared
   runtime authorization require separate architecture and Security review.
2. **Browser request-origin binding remains bounded by the prior identity
   review.** The approved posture is single-operator and loopback-only; this
   decision does not widen it.
3. **Workload readiness is deliberately narrow.** Endpoint health,
   business-operation success, release posture, and product-specific recovery
   remain owner evidence and must not be inferred from this projection.
4. **Freshness is an operating requirement.** Platform must recollect before
   expiry for continued visibility. If publication stops, the Console must
   show stale or unavailable truth rather than preserve the last healthy state.

These findings are expansion limits, not blockers for the exact controlled
boundary reviewed here. They do not require another child under Feature #930.

## Decision

`approved-with-findings`

Approved:

- the exact source revisions bound above;
- centralized server-only configuration and bounded capability projection;
- server-issued correlation with bounded public errors;
- canonical owner-backed audit projection without a Console audit ledger;
- the private Platform runtime-observation collector and Console consumer;
- explicit separation of Platform workload readiness, host telemetry,
  workflow outcome, and Security approval;
- fail-closed missing, malformed, stale, conflicting, replayed, and unavailable
  observation behavior; and
- controlled, single-operator, loopback `dev-integration` operation.

Not approved:

- shared, remote, multi-user, stage, production, or public exposure;
- federated identity, MFA, or browser-session authority;
- exposing private configuration, credentials, projection internals, recovery
  paths, or raw owner diagnostics to the browser;
- treating correlation, capability posture, or workload readiness as
  authorization, workflow success, release readiness, or completion evidence;
- fixture fallback after live configuration is selected; or
- bypassing OOS or canonical owner readback.

## Related Artifacts

- [Console identity activation review](2026-09-27-governance-operations-console-identity-activation.md)
- [Console Proposal live-integration review](2026-08-16-governance-operations-console-proposal-live-integration.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Secrets and recovery architecture](../../architecture/domains/secrets-and-recovery.md)
- [GitOps and machine trust architecture](../../architecture/domains/gitops-and-machine-trust.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
