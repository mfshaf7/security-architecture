# Intake Classifier OpenAI Terra Binding Review

## Summary

- date: 2026-08-20
- owner repo: `security-architecture`
- reviewed source: `platform-engineering@43528915fc45376c7145c1b0eedf95222c49d021`
- affected review subjects:
  - `repos.platform-engineering`
  - `components.governed-ai-gateway`
- delivery refs:
  - `openproject://work_packages/853`
  - `openproject://work_packages/854`
  - `openproject://work_packages/864`
- decision: `approved-with-findings`

The concrete `intake-classifier-v1` binding to `gpt-5.6-terra` through the
OpenAI Responses API is acceptable for the bounded intake-classification
purpose. This decision approves the selected binding, not live provider use.

The profile and the independent access-plane gate must remain inactive until a
Platform-owned activation slice implements and proves the real provider route,
data-handling posture, request restrictions, and rollback controls. Workspace
consumer activation follows that Platform proof; it must not absorb provider
implementation into `workspace-governance`.

## Scope Delta

### Design Intent

- use one platform-owned provider route instead of repo-local provider clients
- keep `workspace-governance/intake-assist` suggestion-only and subordinate to
  explicit operator acceptance
- send only declared, minimized, model-safe intake context
- return only the governed intake suggestion schema
- preserve independent profile, access-plane, security, and consumer gates

### Implemented Control

The reviewed Platform source:

- selects provider `openai`, route `openai-responses-api`, endpoint
  `/v1/responses`, and model `gpt-5.6-terra`
- keeps `intake-classifier-v1` suspended and
  `profile_activation_allowed: false`
- restricts the route to the selected profile and model
- keeps provider credentials in gateway custody and denies consumer projection
- requires caller identity, operator identity, structured audit fields, and
  operator acceptance before workspace truth can change
- independently enforces profile status and access-plane activation state at
  the dev-integration gateway
- denies direct provider reachability from the governed consumer namespace

### Operating Evidence

The exact reviewed source passed Platform CI and local dev-integration smoke.
That smoke proved gateway readiness, caller attribution, local audit emission,
gateway-only credential custody, provider-sentinel denial, exact binding
projection, and both activation gates remaining closed.

No OpenAI request was issued. The current runtime still uses a provider
sentinel, so this evidence cannot prove real-provider authentication, project
retention posture, request minimization, structured-output enforcement, provider
failure mapping, rate limiting, or provider-side rollback.

## Review Areas

### Identity

The caller and operator identities remain separate and attributable. The real
provider adapter must use a dedicated project-scoped machine credential held by
the gateway. A personal key, consumer-held key, or shared developer credential
is not acceptable.

### Secrets

The existing custody boundary is correct, but the current secret is only
sentinel proof. Real activation requires a project-scoped provider credential,
rotation and revocation ownership, and evidence that the credential is exposed
only to the gateway runtime.

### Data And Context

The declared input scope may contain private repository excerpts and operator
notes. Real provider use must accept only a model-safe packet with redaction and
receipt evidence. Raw workspace dumps, secrets, unrestricted files, and context
outside the declared profile scope remain denied.

OpenAI exposes organization- and project-level data-retention controls. The
exact project retention posture must be read and recorded before real workspace
context is sent. The provider request must also use stateless storage posture
where supported; provider defaults are not sufficient evidence.

### Runtime

The provider adapter must fail closed. It must bound timeout, retry, token and
cost limits; map provider errors without leaking request content or credentials;
and preserve the audit event before any suggestion reaches the operator.

The selected model supports hosted tools, but intake classification requires no
provider tool use. The request contract must send an empty tool set, deny tool
selection, use the approved JSON schema, and reject non-conforming output.

### AI

`gpt-5.6-terra` supports the Responses API and structured outputs and is a
reasonable intelligence/cost choice for bounded classification. Model output
remains untrusted suggestion data. It cannot mutate workspace truth, choose its
own tools, widen input scope, or bypass operator acceptance.

The gateway must record the requested model, provider-returned model identity,
prompt or policy version, response identifier, and schema-validation outcome.
If a stable model snapshot becomes available for this route, Platform should
prefer it or explicitly accept alias drift with revalidation.

### Delivery And Rollback

Security judgment and Platform implementation remain separate Landing Units.
Activation order is:

1. this review lands and records the exact binding decision
2. Platform work item `#864` implements and proves the real provider route and
   closes the findings below
3. Security confirms the evidence still matches this decision
4. `workspace-governance` enables the consumer and runs the governed suggestion
   smoke

Rollback must independently support suspending the profile, closing the
access-plane gate, disabling the consumer, and revoking the provider credential.

## Decision

`approved-with-findings`

The OpenAI Responses API and `gpt-5.6-terra` binding is approved for the
declared bounded intake-classification purpose. Live activation is not approved
by this artifact.

Blocking activation findings:

1. Complete Platform work item `#864` before workspace consumer work. It must
   implement the real Responses API adapter and keep both activation gates
   closed until its evidence passes.
2. Record and approve the OpenAI project data-retention posture and use a
   project-scoped gateway credential with rotation and revocation evidence.
3. Require model-safe packet input with redaction receipt, `store: false`, no
   tools, strict JSON-schema output, bounded retries and cost, and fail-closed
   provider error mapping.
4. Audit requested and returned model identity, prompt or policy version,
   provider response id, schema-validation result, and operator acceptance.
5. Keep `openproject://work_packages/415` dependent on
   `openproject://work_packages/864` until the Platform activation slice and
   this review's evidence conditions are complete.

These findings must be routed to active ART rather than left as review prose.

## Related Artifacts

- [Platform PR 213](https://github.com/mfshaf7/platform-engineering/pull/213)
- [GPT-5.6 Terra model documentation](https://developers.openai.com/api/docs/models/gpt-5.6-terra)
- [OpenAI organization data-retention API](https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)
- [OpenAI project data-retention API](https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)
- `platform-engineering/security/governed-ai-model-profiles.yaml`
- `platform-engineering/security/governed-ai-access-plane.yaml`
- `platform-engineering/security/governed-ai-runtime-assist-contract.yaml`
- `workspace-governance/contracts/governed-intake-assist.yaml`
- `workspace-governance/contracts/context-behavior.yaml`
- `security-architecture/docs/reviews/platform/2026-04-29-bounded-governed-ai-runtime-assist-activation.md`
- `security-architecture/docs/reviews/platform/2026-05-06-governed-ai-gateway-devint-runtime.md`
