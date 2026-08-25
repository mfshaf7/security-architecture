# Refinement And Catalog Dev-Integration Boundary Review

## Summary

- date: 2026-08-26
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1012`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/4499a88bd84f6ce9c3294fd66935426107be2bafe78aba2c78caf30c33bf8505`
- reviewed source:
  - Workspace composition contract:
    `workspace-governance@d68a5810eda02efa647f38615db22e0f305d4ce0`
  - Operator Orchestration Service Refinement and Catalog runtimes:
    `operator-orchestration-service@e14d0affad3f5aeaad5de82592a2f439b5ac2bd5`
  - Context Governance Gateway Refinement projection:
    `context-governance-gateway@3483ba44f6366d5e28ec62f42c5e0f055a6cb789`
  - governed AI, composition-runner, and Temporal baseline:
    `platform-engineering@2571f0aebafeeabc5d14ffa18cc0e24f940a6f42`
  - repository-readiness evaluator and ledger:
    `workspace-governance-control-fabric@9106fb718a47484aa4b38118be2e9ed8d553349e`
  - current approved Console baseline:
    `governance-operations-console@490381ddffba57f6bb4d51f94856fd45fc3a3c3c`
- latest composition-contract Review Packet:
  `wgcf://artifacts/delivery-art/sha256/16f60bec3b50f2014f3be310af6ba8fbf1e95516d08e135613acde400b28cc33`
- latest Catalog-runtime Review Packet:
  `wgcf://artifacts/delivery-art/sha256/65f03d7a34a6e6f22af705bdc19a0a30ddb44e25ccea932d7f96f727b418273c`
- decision: `approved-with-findings`

The reviewed source establishes a coherent fail-closed boundary for Delivery
Refinement and Catalog, but it does not establish an active composition. OOS
owns typed workflow and canonical mutation, CGG owns model-safe Refinement
projection, Platform owns governed model and durable-execution runtime,
Workspace Governance owns the neutral composition contract, WGCF owns
repository-readiness decisions, and the Console remains a same-origin OOS
client.

This decision permits Platform work item `#1013` to implement and prove only
the activation delta defined below. It does not itself activate Refinement,
Catalog, Temporal, or the advisor profile. It does not approve stage,
production, a paid provider, direct browser access to an internal service,
repository lifecycle mutation through Catalog, or autonomous model action.

## Scope Delta

### Design Intent

- compose `accepted-idea-delivery` with CGG, the governed AI gateway, WGCF, and
  Temporal through the registered `refinement-catalog` composition
- keep the Console outside the composition and preserve its same-origin OOS
  boundary
- generate composition-lifetime CGG, WGCF, and Catalog-control credentials
  without committing or exposing their values
- keep Refinement advice suggestion-only and require authenticated operator
  acceptance of an immutable draft before durable apply
- require current digest-bound repository readiness before Catalog links an
  Owner Repo value
- preserve canonical OpenProject readback, idempotency, receipts, and history
  as completion truth
- suspend and clean up only the affected composition-owned runtime and
  bindings while preserving canonical records and evidence

### Implemented Control

The exact reviewed source provides:

- a proposed Workspace composition with exact profile identities, dependency
  edges, endpoint formats, caller identities, generated credential targets,
  non-secret profile bindings, startup order, teardown order, and cleanup owner
- a typed OOS Refinement contract and inactive runtime that bind source and
  packet revisions, CGG evidence, one logical advisor profile, immutable
  operator acceptance, durable run identity, canonical readback, and receipt
- a CGG Refinement route that admits only the configured OOS caller and shared
  secret, validates the canonical assist request, applies age and budget
  limits, denies raw projection, and keeps replay state in a Refinement-specific
  namespace
- a selected-not-active Platform advisor profile restricted to the exact OOS
  Refinement caller, task contract, output schema, local Ollama binding, and
  suggestion-only output
- a WGCF evaluator that reads exact Workspace repository authority, binds the
  repository, owner, Catalog value, policy scope, authority digest, rule
  digest, implementation revision, decision generation, and immutable receipt,
  and holds no repository or Catalog mutation authority
- an inactive OOS Catalog runtime that revalidates repository readiness,
  source revision, operator acceptance, mutation capability, idempotency,
  backend result, canonical readback, and durable receipt
- a current Console baseline with no live Refinement or Catalog adapter and no
  direct browser route to CGG, the gateway, WGCF, Temporal, or OpenProject

The current Platform composition runner supports the earlier Work Design
composition only. It does not yet interpret the new caller bindings, profile
bindings, or host-and-port projection, and the accepted-idea profile does not
yet consume the new Refinement and Catalog projections. Temporal remains
`build-admitted`, the Refinement advisor remains `selected-not-active`, and the
`refinement-catalog` composition remains `proposed`. These are activation work,
not operating evidence.

### Permitted Activation Delta

Work item `#1013` may change only the Platform-owned activation and integration
surfaces needed to:

- validate and project the registered caller bindings, profile bindings, and
  URL or host-and-port dependency endpoints
- project generated credentials only to their declared consumers, with
  private custody and profile-scoped cleanup
- make the admitted Temporal runtime and exact Refinement advisor binding
  available to this local composition
- make the accepted-idea profile consume only the registered Refinement,
  Catalog, WGCF, gateway, and Temporal bindings
- expose the bounded Catalog control adapter required by the existing OOS
  contract without granting general OpenProject administration
- activate only `refinement-catalog` in local `dev-integration`
- prove dependency readiness, negative authorization, replay, rollback,
  suspension, and cleanup behavior

The `#1013` Review Packet must bind its exact reviewed source head and prove
that every change is inside this envelope. A different dependency, credential
target, caller, provider, namespace, backend authority, browser path, or
mutation capability is outside this decision and requires a fresh Security
delta review before activation.

### Operating Evidence

The predecessor Review Packets prove merged source, contracts, unit and
negative behavior for the owner implementations. They do not prove a composed
runtime. In particular, no current evidence proves:

- active Refinement caller admission through the composed CGG route
- active provider invocation for `delivery-refinement-advisor-v1`
- active Temporal execution of `delivery.refinement.apply`
- active Catalog control or WGCF readiness calls from the accepted-idea profile
- composition-scoped credential projection and cleanup for this composition
- Console live Refinement or Catalog behavior

Those remain mandatory `#1013` and `#1014` evidence, and no fixture or source
test may be presented as proof that these runtime paths are active.

## Review Areas

### Identity And Authorization

The browser must authenticate only to same-origin Console routes. The Console
server may call OOS using server-held caller identity. OOS is the only admitted
Refinement caller to CGG and the governed AI gateway and the only admitted
Catalog caller to WGCF and the bounded Catalog control adapter.

Caller, workflow, profile, task, contract version, schema, request,
correlation, source revision, packet revision, repository identity, operator
acceptance, and idempotency identity must remain bound at their respective
boundaries. Synthetic operator attribution is accepted only in local
`dev-integration`; it is not authenticated human identity or production
authorization.

### Secrets And Provider Custody

Platform owns generated composition credentials and provider custody. OOS,
CGG, WGCF, and the Catalog control adapter may receive only their declared
projection. Credential values must not appear in Git, rendered status, logs,
browser payloads, OOS persisted environment files, or durable evidence.

The CGG, WGCF, and Catalog-control bindings are distinct authorities even when
generated by one composition runner. The general OpenProject API token must
not be reused as the Catalog-control credential. OOS must not receive provider
credentials or a direct provider route.

### Context, Advice, And Apply Safety

CGG remains the only model-safe Refinement context boundary. The gateway may
accept only the reviewed logical profile, caller, task contract, and strict
output schema. Tools, arbitrary provider selection, raw-context projection,
and model-direct mutation remain unavailable.

Advice is untrusted input. OOS must separately validate the exact accepted
draft, operator identity, packet and source revisions, apply plan, and
idempotency key before durable execution. Completion requires canonical
readback and a non-null digest-bound receipt. Accepted, running, or activity
completion alone is not success.

### Catalog And Repository Authority

Catalog may project and mutate canonical Delivery vocabulary only through the
bounded control adapter. It may link an already admitted repository only after
OOS revalidates a current WGCF readiness receipt. It may not create, admit,
rename, suspend, retire, or delete a repository.

WGCF decides readiness from current Workspace authority and issues evidence;
it does not write Catalog. The Catalog adapter writes the exact accepted value
and returns canonical readback; it must not expose general administrative
routes or infer success from the request.

### Durable Execution, Audit, And Recovery

Temporal may own durable execution state for the exact
`delivery.refinement.apply` definition only. OOS remains workflow and canonical
mutation authority. Retries must reuse the same run and idempotency identity,
conflicting replay must fail, and restart must not duplicate canonical effects.

CGG projection receipts, gateway audit records, WGCF readiness receipts,
Temporal run events, OOS apply or Catalog receipts, and canonical backend
readback remain distinct evidence layers. Failed and denied actions cannot
project success. Raw context and credentials remain excluded.

### Runtime Isolation And Rollback

The composition must fail closed on unknown profiles, missing or mismatched
bindings, dependency failure, caller denial, stale evidence, invalid output,
backend conflict, incomplete readback, or partial apply. Rollback may suspend
only the Refinement advisor, worker, durable definition, Catalog route, and
composition-owned bindings implicated by the failure.

Rollback must preserve accepted inputs, run history, partial-effect evidence,
canonical OpenProject state, OOS receipts, WGCF readiness history, and
unrelated active profiles. Broad namespace deletion or teardown of shared CGG,
WGCF, gateway, Temporal, OpenProject, or Console state is not approved.

### Console Compatibility

The Console source does not change in `#1012` or `#1013`. Work item `#1014`
may replace only the approved local data and action adapter seams for
Refinement and Catalog. It must preserve the current workflow and Catalog
visual behavior, call OOS through same-origin server routes only, keep
credentials and operator attribution server-side, and render configured
failure as a bounded non-success state without fixture fallback.

The `#1014` Review Packet must bind its exact Console head and prove the
same-origin route, semantic mapping, explicit acceptance, durable run polling,
Catalog readback, failure, and no-bypass cases. Any visual redesign or direct
internal-service access is outside this decision.

## Findings And Expansion Gates

1. The composition is not active. Platform `#1013` must implement and prove the
   permitted activation delta before any active claim.
2. Human attribution remains synthetic in local `dev-integration`.
   Authenticated identity is required before governed stage or production use.
3. This decision covers only the reviewed local Ollama binding and exact
   architecture. Paid-provider, changed model, stage, production, wider caller
   or credential projection, general OpenProject administration, or browser
   access to internal services requires fresh review.
4. Console live integration remains separately gated by `#1014` and must bind
   its exact source head and runtime evidence.

These findings are non-blocking for bounded `#1013` implementation. They do
not become accepted production risks and they do not authorize silent scope
expansion.

## Decision

`approved-with-findings`

The exact reviewed source and the explicitly bounded activation delta are
acceptable for local `dev-integration`. Security ART `#1012` may close and
Platform ART `#1013` may implement and rehearse the composition only when its
final Review Packet proves the exact head, change-envelope conformance, caller
and credential isolation, dependency readiness, positive and negative runtime
cases, replay, suspension, rollback, and cleanup.

Approval is revoked for this decision scope if any of the following occurs:

- a reviewed owner boundary changes outside the permitted activation delta
- the Console bypasses OOS or OOS bypasses CGG, the gateway, WGCF, Temporal
  ownership, or the bounded Catalog adapter
- model output can authorize or start apply without explicit operator
  acceptance
- Catalog can mutate repository lifecycle or use free-text repository identity
- a credential or raw model context reaches source, logs, evidence, or browser
  data
- failed, partial, stale, or unread-back work can project success
- rollback or cleanup affects unrelated profile or canonical state
- stage, production, paid-provider, or authenticated-identity claims are made
  from this local evidence

## Related Artifacts

- `workspace-governance/contracts/developer-integration-profiles.yaml`
- `workspace-governance/docs/developer-integration-runtime-composition.md`
- `operator-orchestration-service/contracts/refinement/manifest.json`
- `operator-orchestration-service/contracts/catalog/manifest.json`
- `operator-orchestration-service/docs/contracts/refinement-v1.md`
- `operator-orchestration-service/docs/contracts/catalog-v1.md`
- `context-governance-gateway/docs/operating-model/refinement-projection.md`
- `platform-engineering/security/governed-ai-model-profiles.yaml`
- `platform-engineering/scripts/dev_integration_compositions.py`
- `workspace-governance-control-fabric/contracts/repository-readiness/manifest.json`
- `governance-operations-console/docs/security-and-data-boundaries.md`
- `security-architecture/docs/reviews/components/2026-08-25-work-design-dev-integration-composition-boundary.md`
