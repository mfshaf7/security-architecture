# Governed Work Design AI Activation Boundary Review

## Summary

- date: 2026-08-25
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/994`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/21006ba15d8a8c725e1adf4c0e667db83ae998a8f224f4e4b00f7e333cd78bf3`
- reviewed source:
  - Work Design contract:
    `operator-orchestration-service@792fdf6b8742a4d34ee66199cad20a6eb154331a`
    via PR `#158`, merged as
    `7f5fb83661eec43f1e719567f42cd7841128fe44`
  - CGG Work Design projection:
    `context-governance-gateway@f9661709cbf39f33ca069744bcaa1375cae6514b`
    via PR `#17`, merged as
    `021eaf3f47dfa989f1b3d13f117f2a05c66225df`
  - governed AI gateway foundation:
    `platform-engineering@1f1e41f0c0cbb9309b854607f1cb24ed5ad25887`
    via PR `#219`, merged as
    `5ae564c3c9c46b69fb6085a2c21a5c0622a9ef35`
  - OOS Work Design runtime:
    `operator-orchestration-service@7fc95150d3274e79883884513deb96fd3b1355d3`
    via PR `#159`, merged as
    `a62419f191788c5bdb4c66d610d25e6d7db02013`
  - current approved Console baseline:
    `governance-operations-console@5cbc43dbc37c429e27e69778a4d0af92b03e9049`
- decision: `approved-with-findings`

The reviewed source establishes a coherent suggestion-only Work Design AI
path. OOS owns workflow semantics and canonical apply, CGG owns model-safe
context projection, Platform owns profile enforcement and provider custody,
Security owns activation acceptance, and the Console remains a same-origin
operator adapter.

This decision permits Platform work item `#995` to activate only the logical
`delivery-work-design-advisor-v1` profile in `dev-integration`, subject to the
findings below. It does not activate the profile, approve stage or production,
approve a paid provider, or approve Console live integration. Console wiring
remains separately gated by work item `#996`.

## Scope Delta

### Design Intent

- admit only receipt-bound Work Design context through CGG
- invoke only the reviewed logical profile through the platform gateway
- keep task instructions and typed result semantics under OOS ownership
- treat model output as untrusted advice, never mutation authority
- require an explicit operator-accepted draft before canonical apply
- preserve the approved Console workflow and replace only its local adapter
  seam in `#996`
- suspend the Work Design profile independently without disturbing
  `intake-classifier-v1`

### Implemented Control

The exact reviewed source provides:

- a versioned OOS Work Design contract with bounded task kinds, output schema,
  failure codes, acceptance identity, backend readback, and receipt shape
- a CGG projection route restricted to the OOS caller, with constant-time
  shared-secret comparison, exact request and source binding, redaction-safe
  projection, bounded age, byte and token budgets, replay recovery, and safe
  denial records
- a provider-neutral gateway registry that keeps the Work Design profile and
  local binding `selected-not-active`, isolates it from the active intake
  profile, enforces exact caller and task identity, validates allowed input and
  strict output schema, and denies before provider access when any activation
  or policy condition fails
- an OOS runtime that revalidates current OpenProject source revision, CGG
  packet and receipt bindings, gateway identity and audit fields, accepted tree
  digest, operator acceptance, idempotency identity, canonical apply result,
  backend readback, and final receipt
- a current Console baseline that still treats Work Design assistance as local
  prototype behavior and has no direct live CGG, gateway, provider, or
  OpenProject Work Design integration

No reviewed consumer holds provider credentials. No model response can call
the apply route. No profile activation or Console source change is included in
the reviewed Landing Units.

### Operating Evidence

The owner-repo Review Packets provide the current implementation evidence:

- Work Design contract:
  `wgcf://artifacts/delivery-art/sha256/cc8e23ab0301ae3a86db900f33e556a29c8d368315a2eac1ff7ed8296852f59a`
- CGG projection:
  `wgcf://artifacts/delivery-art/sha256/086e946a544726ea353a82b74a5050923af5012f5ddfaa345dd08bae53939e9a`
- gateway foundation:
  `wgcf://artifacts/delivery-art/sha256/1a2a3ec1d5aedae99c98aa53b1085668136c63f588cb1a84ad944abfe2de23c4`
- OOS runtime:
  `wgcf://artifacts/delivery-art/sha256/1d146be38f2194bf94ff35598f58cd9069c6a74e4a9d3834101846edf2067128`

Those packets prove source, contract, unit, negative, and bounded local runtime
behavior. They do not prove an active Work Design provider route. Exact
activation, audit persistence, bypass denial, provider health, and independent
suspension remain operating-evidence obligations for `#995`.

## Review Areas

### Identity And Authorization

The machine boundaries are separated correctly:

- the Console will authenticate only to OOS
- OOS is the only admitted Work Design caller to CGG
- `operator-orchestration-service/work-design-assist` is the only admitted
  Work Design gateway caller
- caller repo, workflow, requested profile, correlation identity, task kind,
  contract version, and output schema must all match before provider access

Operator identity is separately present in projection, invocation, acceptance,
apply, audit, and receipt data. The current Console baseline uses synthetic
operator identity, so this review permits that attribution only inside local
`dev-integration`. It does not claim authenticated human identity. Work item
`#996` must keep OOS credentials and configured operator attribution on the
server side; browser-supplied caller or operator authority is not approved.

### Secrets And Provider Custody

CGG and OOS use separate machine-caller credentials. OOS receives no provider
credential or direct provider endpoint. The gateway retains provider custody
and reports that provider material is not projected to consumers.

The selected local Ollama binding requires no API credential, but network
reachability is not authorization. `#995` must prove that only the gateway can
use the reviewed provider route and that unrelated consumers cannot bypass it.
Any future paid-provider credential or provider change requires separate
activation evidence and, where the binding changes, a fresh delta review.

### Context And Prompt Integrity

CGG binds source revision, caller, operator, task, request, correlation,
session, execution, digest, timestamp, and budget before returning model-safe
content. Raw projection remains denied. Unsafe, stale, oversized, malformed,
unauthorized, and replay-conflicting requests fail without echoing submitted
context.

OOS owns the versioned task instruction. Operator prompts and source content
remain untrusted. Prompt injection can influence a suggestion, but cannot widen
the admitted packet, select tools, change the output schema, activate a
profile, or invoke canonical apply. The local provider must continue to run
without tools or thinking output under the strict reviewed schema.

### Output And Action Safety

Gateway output is accepted only when profile, caller, task, contract, version,
schema, decision identity, invocation path, and audit reference match. OOS then
validates the Work Design result schema again.

Apply is a distinct route. It requires the accepted tree, its canonical digest,
operator acceptance, exact source revision, and an idempotency key. OOS applies
through its existing Delivery plan writer, reads canonical state back, and
emits a receipt. Model output alone has no path to apply.

The in-process replay cache is not treated as the sole durable control. Stable
application identity, canonical plan reconciliation, source revision checks,
and backend readback must remain effective across process restart. `#995` must
include restart or replay evidence sufficient to prove that activation does
not turn retry into duplicate mutation.

### Audit And Evidence

The path produces three distinct evidence layers:

- CGG packet, redaction, projection, denial, and replay evidence
- gateway caller/profile/provider/schema/outcome audit evidence
- OOS advice, acceptance, apply, backend readback, and receipt evidence

These layers preserve the distinction between model suggestion, operator
acceptance, and canonical mutation. `#995` must prove that gateway audit state
survives the declared runtime lifecycle and that failed or denied invocations
cannot project success. Raw prompts, raw context, credentials, and provider
secrets must remain absent from operator status surfaces and committed source.

### Console Compatibility

The reviewed Console head is an approved visual and product baseline, not a
live Work Design authority. `#996` must preserve the existing Work Design
workflow and use same-origin Console server routes that call OOS only. It must
not call CGG, the governed AI gateway, Ollama, another provider, or OpenProject
directly. Configured OOS failure must render a bounded non-success state and
must not fall back to fixture advice or local apply while presenting the result
as live.

Any Console source head other than the one reviewed here must be covered by
the `#996` Review Packet and shown to preserve these boundaries before the
Feature can become operating-ready.

### Activation And Rollback

The Work Design profile is currently inactive and independently selectable.
`#995` may change only that profile and its selected local binding to active in
`dev-integration`, update its security review reference to this artifact, and
produce the required operating evidence.

Rollback must suspend only `delivery-work-design-advisor-v1`, preserve denied
and failed audit evidence, retain canonical OOS apply receipts, and leave
`intake-classifier-v1` available. Broad gateway shutdown or repository rollback
is not an acceptable substitute for the profile-level suspension proof.

## Decision

`approved-with-findings`

The implemented boundary is suitable for bounded Work Design advice and
operator-approved plan application in `dev-integration`. Platform work item
`#995` may proceed with activation only when all of these conditions are met:

1. Bind activation to the exact CGG, Platform, OOS, and current Console source
   revisions listed in this review. Any changed security-relevant head requires
   delta evaluation before activation.
2. Activate only `delivery-work-design-advisor-v1` and only its reviewed local
   Ollama binding in `dev-integration`. Do not activate stage, production, a
   paid provider, tools, or model-direct mutation.
3. Prove exact caller, task, profile, schema, provider digest and runtime
   version enforcement, plus negative unknown-caller, mismatched-profile,
   malformed-output, timeout, unavailable-provider, and direct-bypass cases.
4. Prove CGG packet and receipt binding, gateway audit persistence, OOS replay
   and restart behavior, failed-state non-success projection, and independent
   Work Design profile suspension without intake regression.
5. Keep synthetic operator attribution explicitly limited to local
   `dev-integration`. `#996` must keep caller credentials and operator
   attribution server-side and preserve explicit human acceptance before apply.
6. Preserve the reviewed Console visual workflow. No direct Console access to
   CGG, gateway, provider, or OpenProject and no live-to-fixture success
   fallback is approved.

Failure to satisfy any activation condition blocks `#995`; it does not become
accepted risk implicitly.

## Related Artifacts

- `operator-orchestration-service/contracts/work-design/manifest.json`
- `operator-orchestration-service/docs/contracts/work-design-v1.md`
- `operator-orchestration-service/src/work-design/service.js`
- `context-governance-gateway/docs/operating-model/work-design-projection.md`
- `context-governance-gateway/contracts/schemas/work-design-context-projection-result.schema.json`
- `platform-engineering/security/governed-ai-model-profiles.yaml`
- `platform-engineering/dev-integration/profiles/governed-ai-gateway/runtime/gateway_policy.py`
- `governance-operations-console/docs/security-and-data-boundaries.md`
- `security-architecture/docs/standards/ai-security-and-governance.md`

