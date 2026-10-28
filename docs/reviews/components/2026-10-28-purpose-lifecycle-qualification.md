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
`467f8266b65bc272b796a9438fd484015c2b7a90`. The profile transaction changes these documents:

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

### Actual source fulfillment and final restored tree

Gary Platform [PR349](https://github.com/mfshaf7/platform-engineering/pull/349)
was reviewed at `4e3e9f2ee5fa0fd60bc5d160d207ce7ee1ffe4c7` and merged as
`f89269a153f1f548572de652185090cf918576a9`, with identical tree
`6b57c4d90e14f09ce3e2d5f0264dc898b7c14d73`. Full committed local validation
against fetched `origin/main` and exact locked OOS source passed. Hosted
[40614820030](https://github.com/mfshaf7/platform-engineering/actions/runs/40614820030)
and posture40614820022 passed. Actual clean merged-source readback published
immutable request history; the distinct Platform writer recorded applied at
revision6. The real Console then verified current reconciliation and next action
`complete`, with no profile activation. All six deliberately invalid owner
inputs were rejected without source or request mutation. The original failed
request remains truthfully visible through native history.

Full validation exposed a test-isolation miss: synthetic model-management
behavior cases read the changing real registry even though they exercise the
finite six-profile runtime boundary. The bounded repair uses the existing
`governed_ai_test_support.prepare_contracts` disposable fixtures, retaining the
actual policy and image contracts. Fifteen focused cases pass, including an
explicit refusal of an extra suspended profile. The production
`console_model_management.py` implementation and task/account grants are
unchanged. Source validation and complete runtime registry resolution continue
to inspect actual canonical source independently of these fixtures.

The actual corrected lifecycle receipt and rollback bundle produced restoration
candidate `d174217d6cbfe177862d34ce0c33feba9df1a921`, tree
`8bc54e24ba844ebaf90b5281a538b11bd3ac87d5`. Its three profile documents match
the original baseline byte for byte; actual registry resolution returns six
profiles and actual runtime management policy construction accepts that restored
source. Only `test_console_model_management.py` and its fixture README remain
different from the preceding accepted tree. This candidate is source acceptance
for landing; its merge and final native restoration readback are later facts.
The exact committed restoration candidate passed full local `make validate`
with the locked OOS source and a diff check against fetched `origin/main` at
`f89269a153f1f548572de652185090cf918576a9`. Its source receipt, byte-exact
restoration, real resolver and real management-policy readback are retained
under `1339-restored-source-*` and `1339-final-restoration-source-semantics.json`.

The paired finite YAML and prose advance only Platform to that exact candidate
and tree. All other execution owners, the original C786 manifest, expiry,
generation and WGCF worker digest remain unchanged. Preserve accepted primary
execution checkouts while staging. After both source landings are proven,
advance the paired sources together and commission through the existing normal
lifecycle. Do not edit private resolved policies or create another bundle to
hide source mismatch. The completed health exercise1341 remains independent;
final Purpose restoration and original durable recovery1346 remain operating
obligations before the Epic may close.

## Decision

`approved` for this bounded suspended configuration transaction and exact
baseline restoration under the existing source bridge. The review covers both
temporal source states without granting runtime activation, inference, a new
control plane, a weaker caller rule or an exception. Require full committed
validation, exact source review, truthful original and corrected histories,
merged readback, exact restoration and source resource cleanup before story1339
can close. Durable recovery story1346 remains independent and open.
