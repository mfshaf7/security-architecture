# Work Design Dev-Integration Composition Boundary Review

## Summary

- date: 2026-08-25
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1003`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/de0491cabf2a6a7ab6a37fd082b2f709170430eb3f7fad2acc54fbe510974c07`
- reviewed source:
  - Workspace composition contract:
    `workspace-governance@c15ecc5bb57e151b419664cfacb1eadd8b887c64`
  - Platform composition runner and governed AI gateway:
    `platform-engineering@c27b8bf1f3accabe1d9fd6008cad65cd10eec327`
  - Context Governance Gateway:
    `context-governance-gateway@6508b5f363595f049b58944abfb09276b4c01e24`
  - Operator Orchestration Service:
    `operator-orchestration-service@efeefe0d389ad164a7c39b53fc4c407f047b1c60`
  - Governance Operations Console:
    `governance-operations-console@490381ddffba57f6bb4d51f94856fd45fc3a3c3c`
- composed runtime Review Packet:
  `wgcf://artifacts/delivery-art/sha256/9116e050b5fa34128c4276f1e557f5a6c98e0c68be9fd4a3a002eb3d04674b1b`
- decision: `approved-with-findings`

The reviewed source and operating evidence establish one bounded Work Design
advice path in local `dev-integration`. The Console calls its same-origin
server adapter, OOS owns workflow and apply authority, CGG admits model-safe
context, and the Platform gateway owns model selection, provider access, audit,
runtime composition, and credential custody.

This decision accepts the composed local path. It does not approve stage or
production activation, a paid provider, authenticated human identity, direct
browser access to internal services, raw-context projection, or model-direct
mutation.

## Scope Delta

### Design Intent

- compose only the registered `work-design-advice` profile set
- keep all service dependencies cluster-local and fail closed when any binding
  is missing or mismatched
- generate one composition-lifetime CGG caller credential and project it only
  to the declared OOS and CGG consumers
- preserve provider credentials and provider access inside Platform
- preserve explicit operator acceptance and canonical OOS apply
- preserve the approved Governance Console visual workflow and same-origin
  server boundary
- tear down only the composition-owned caller binding while retaining
  unrelated profile state and durable evidence

### Implemented Control

The exact reviewed source provides:

- a Workspace-owned composition registry containing profile identities,
  dependency edges, endpoint coordinates, credential ownership, and projection
  targets without credential values
- a Platform runner that resolves the dependency graph, generates the local
  caller binding, projects it only to OOS and CGG, and rejects incomplete,
  cyclic, unknown, or foreign composition input
- a dedicated ephemeral Kubernetes Secret in each consumer namespace rather
  than a credential copied into tracked source, rendered YAML, OOS
  `broker.env`, or persistent CGG local-secret state
- CGG caller admission that requires the OOS Work Design identity and the exact
  shared credential before model-safe projection
- OOS readiness that accepts Work Design only when both declared cluster-local
  endpoints and the dedicated caller-secret reference are present and match
  the registered composition
- a governed AI gateway that enforces the exact Work Design profile, caller,
  task contract, output schema, local provider binding, and audit record before
  returning advice
- OOS output validation, explicit operator acceptance, canonical apply,
  backend readback, idempotency, and durable receipt behavior
- a Console adapter that calls OOS only through same-origin server routes and
  does not fall back to fixture success when the configured live path fails
- profile-scoped down and failure cleanup that remove the caller binding
  without broad namespace, provider, CGG, OpenProject, or Console teardown

### Operating Evidence

The composed-runtime Review Packet for ART `#1002` proves the positive and
negative Feature path at `sandbox-runtime` fidelity, including real model-safe
context admission, governed local model advice, exact caller denial, explicit
apply separation, source readback, audit references, and receipt projection.
It also binds the merged OOS source and the positive and negative
`real-git` provenance cases.

Fresh review-time inspection additionally proved:

- all three registered profiles reconciled to `active` after the merged OOS
  source was loaded
- the OOS and CGG deployments reference separate dedicated Kubernetes Secret
  objects containing the same non-empty composition value
- the caller credential is absent from OOS `broker.env`, rendered local
  profile artifacts, OOS logs, and CGG API logs
- OOS receives only the declared CGG and governed AI gateway service
  coordinates; it receives no provider credential or direct provider route
- gateway and consumer namespaces retain the provider-egress and default-deny
  network policies proven by the activation work
- a stale local host-service command digest detected after the OOS merge was
  reconciled through the registered Platform composition runner; final
  composition state is `active`

The evidence does not claim stage, production, paid-provider, authenticated
human identity, or internet-facing operation.

## Review Areas

### Identity And Authorization

The machine identities remain separated. The Console authenticates only to
OOS. OOS is the sole admitted Work Design caller to CGG and the sole admitted
Work Design caller to the governed AI gateway. Caller, profile, task,
contract, schema, request, correlation, source revision, and acceptance
identity remain bound before advice or apply can succeed.

The local Console still uses configured synthetic operator attribution. That
is accepted only for local `dev-integration`; it is not evidence of human SSO,
OIDC, or production authorization.

### Secrets And Provider Custody

The composition caller credential is generated and retained by Platform for
the composition lifetime. OOS and CGG receive only their declared projections
through dedicated Secret references. Neither consumer receives provider
credentials. The active local Ollama binding has no API credential, but
network reachability is still constrained to the gateway-owned provider path.

Any paid-provider binding, wider caller projection, persistent copy, or
browser-visible credential requires a fresh review and is not covered here.

### Context, Model, And Action Safety

CGG remains the only model-safe context admission boundary. Raw context is not
projected to the gateway or Console. The gateway accepts only the reviewed
Work Design contract and strict output schema. Tools, arbitrary provider
routing, and model-direct mutation are unavailable.

Advice remains untrusted input. Only the operator-accepted draft can reach the
separate OOS apply path, which revalidates source and accepted-tree identity,
performs canonical mutation, reads the backend back, and writes the receipt.

### Runtime, Audit, And Failure Isolation

The composition has one declared root and two declared dependencies. Missing,
partial, foreign, or mismatched endpoint and credential projections fail
closed. Failed and denied requests cannot project success. CGG packet evidence,
gateway audit evidence, and OOS apply receipts remain distinct and redact raw
context and credentials.

Rollback suspends the composed Work Design path and removes only the dedicated
caller binding. Standalone CGG, the governed AI gateway, OpenProject history,
canonical OOS receipts, and unrelated profiles remain intact.

### Console Compatibility

The Console source did not change in this correction. Its approved Delivery
Work Design surface still calls same-origin routes that forward only to OOS.
The browser has no direct CGG, gateway, Ollama, provider, or OpenProject Work
Design path. Live failure remains a bounded non-success state and cannot be
presented as successful fixture behavior.

## Findings And Expansion Gates

1. Human attribution remains synthetic and configured for local
   `dev-integration`. Authenticated identity is required before any governed
   stage or production use.
2. This decision covers only the reviewed local Ollama binding and exact source
   revisions. Stage, production, paid-provider, changed model binding, wider
   credential projection, or changed trust-boundary source requires a fresh
   delta review.

These are non-blocking scope gates for the reviewed local composition. They are
not accepted as production controls and they do not authorize silent
expansion.

## Decision

`approved-with-findings`

The exact Work Design composition is acceptable for bounded local
`dev-integration`. Security ART `#1003` may close and the composed Feature path
may proceed to parent closeout because the declared dependency, credential,
caller, namespace, provider, audit, Console, rollback, and cleanup boundaries
are implemented and proven.

Approval is revoked for this decision scope if any of the following occurs:

- an exact reviewed source head changes without delta evaluation
- the caller credential is projected outside OOS and CGG or appears in source,
  rendered artifacts, status output, logs, or browser data
- the Console bypasses OOS or OOS bypasses CGG or the governed AI gateway
- model output can invoke apply without explicit operator acceptance
- cleanup becomes broad, ambiguous, or destructive to unrelated profile state
- stage, production, paid-provider, or authenticated-identity claims are made
  from this local evidence

## Related Artifacts

- `workspace-governance/contracts/developer-integration-profiles.yaml`
- `workspace-governance/docs/developer-integration-runtime-composition.md`
- `platform-engineering/scripts/dev_integration_compositions.py`
- `platform-engineering/security/governed-ai-model-profiles.yaml`
- `context-governance-gateway/docs/operating-model/work-design-projection.md`
- `operator-orchestration-service/docs/contracts/work-design-v1.md`
- `operator-orchestration-service/docs/records/change-records/2026-08-25-work-design-composed-oos-runtime.md`
- `governance-operations-console/docs/security-and-data-boundaries.md`
- `security-architecture/docs/reviews/components/2026-08-25-governed-work-design-ai-activation-boundary.md`
