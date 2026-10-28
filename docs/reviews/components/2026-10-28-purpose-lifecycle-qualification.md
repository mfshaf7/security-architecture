# Purpose lifecycle qualification source delta

## Summary

- date: 2026-10-28
- decision: `approved`
- subject: `repos/platform-engineering`
- trigger: `shared-platform-control-plane-and-secrets`
- classification: existing source configuration bridge for Epic1332 story1339
- authority: main-agent Security judgment and existing delegated exact-head human review; Gary authors and publishes

Approve one suspended qualification profile and its subsequent exact baseline
restoration through the existing Platform model-profile lifecycle. The preceding
[composition recovery review](2026-10-28-console-capability-recovery.md) remains
the runtime acceptance. This source exercise changes no finite runtime decision,
activation bundle, worker, provider route, model selection or credential custody.

## Scope Delta

The accepted source baseline is Platform
`467f8266b65bc272b796a9438fd484015c2b7a90`. Only these source documents change:

- `security/governed-ai-model-profiles.yaml`
- `security/governed-ai-access-plane.yaml`
- `security/governed-ai-runtime-assist-contract.yaml`

The new `console-purpose-qualification-1339-v1` profile is suspended. Its sole
logical caller is `workspace-governance/intake-assist-qualification-1339`, using
the existing intake purpose, output schema, task contract and provider bindings.
Platform records activation as disallowed. No caller credential or active
consumer binding is created. All six existing profile objects and active
consumer memberships are preserved. The existing YAML serializer may normalize
formatting and list order; semantic source preservation is separately checked.

The original native request
`model-profile-request:console-5f34e213-0600-49e1-ae39-53c407e7a216`
incorrectly reused the already-bound intake caller. Full committed validation
rejected that candidate before publication or activation. OOS now preserves its
actual failed fulfillment at revision6. This was a qualification setup mistake;
the caller uniqueness control is retained. Corrected native request
`model-profile-request:console-c512f813-9e47-459e-873a-aa166e04760f`
explicitly links the failed attempt, was separately reviewed through the
Console, and is implementing under the distinct Platform caller.

## Review Areas

### Identity, secrets and AI

A source registration is not an authenticated runtime identity. The distinct
qualification caller has no issued secret, active consumer membership or
profile activation. No inference is part of this exercise. Existing gateway
caller uniqueness, purpose/task/schema checks, bounded invocation controls,
human approval and direct-provider prohibition continue to apply. This review
does not authorize an activation or exception decision.

### Delivery and recovery

OOS owns reviewed intent and the request history; Platform owns source and
fulfillment. Both approved requests and the rejected local candidate remain
auditable. The corrected intent cannot silently replace the original approval.
The normal Gary source bridge, exact-head delegated human review and required
checks remain necessary before landing. Merged source readback and Platform
fulfillment must reference actual landed evidence, never a future merge.

After applied fulfillment and historical readback, the existing exact receipt
and rollback bundle restore the three original source documents byte for byte
through a separately reviewed Platform restoration. The canonical current
registry returns to six profiles while immutable request history remains.
Live accepted execution checkouts and finite source selections remain unchanged
through staging; publication of owner source metadata is not runtime activation.

### Evidence and limits

Before corrected request creation, actual source validation and the complete
runtime registry resolver passed temporary candidate copies, resolving seven
profiles with the qualification suspended and the six existing profiles intact.
Actual Console create, start-review and explicit approval succeeded. Actual
OOS wrong-actor fulfillment returned403 without advancing the request; the
admitted distinct Platform actor then recorded implementing. These operating
facts do not replace committed CI, reviewed merge, applied readback, source
restoration or final native operating acceptance, which remain to be collected.

Evidence is retained under
`local-evidence://governance-operations-console/.art/console-capability-completion-20261027/`
in `1339-corrected-*` and the preserved original `1339-*` records. No credential
values appear in source or review evidence.

## Decision

`approved` for this bounded suspended configuration transaction and exact
baseline restoration under the existing source bridge. The review covers both
temporal source states without granting runtime activation, inference, a new
control plane, a weaker caller rule or an exception. Require full committed
validation, exact source review, truthful original and corrected histories,
merged readback, exact restoration and source resource cleanup before story1339
can close. Durable recovery story1346 remains independent and open.
