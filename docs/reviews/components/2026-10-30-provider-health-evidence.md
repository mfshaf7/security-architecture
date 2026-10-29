# Native connection checks and timestamped model success security delta

## Summary

Extend the existing post-core provider-health workflow. This supersedes only
[the preceding delta](2026-10-30-provider-lifecycle.md)'s account-presence-only
hosted health observation. Startup remains independent from AI availability.
No new service, provider permission, daemon, action executor or storage authority.
The paired composed decision remains the sole exact runtime activation gate.

Landing Unit Decision: feature_single_landing_unit,
maintenance-provider-health-security-architecture-20261030.

## Reviewed Source

- OOS: Gary candidate `77c7bbe8ce83a57621e20365486ca0cc1930504a`, merged `609f28b6948d86309439ea673c7df306f0fc8a2f` ([PR397](https://github.com/mfshaf7/operator-orchestration-service/pull/397)); equal source tree proven.
- Console: Gary candidate `a5c6112d6655757e92360c65edf4906b49cc4126`, merged `2d97ce5692969da1bf85da35e077766dc6bd8f0d` ([PR153](https://github.com/mfshaf7/governance-operations-console/pull/153)); equal source tree proven.
- Platform: Gary candidate `673149487cf35f0fbf36f4e53114202894fe1682` ([PR354](https://github.com/mfshaf7/platform-engineering/pull/354)); merged `d8bf4504366a0b20ed7b14bb99835fc32d3bf82f`, equal source tree `e9686202687940d0e5781bc20c6bb670edd95485` proven.

## Scope Delta

After same-boot, exact-decision core readiness, the existing timer may start one
isolated pinned native app-server for an authenticated `account/rateLimits/read`
and bounded model metadata. It uses the existing process semaphore, account lock,
fixed policy-selected executable, private account-only home and dedicated Vault
custody. The native account check sends no project data, creates no thread or
turn and performs no inference. Native token refresh persists through the existing
Vault compare-and-swap path. Fresh collector results are reused for 60 seconds
and expire after 120 seconds. Browser reads and core readiness never launch it.
Unsupported/failed/busy checks remain unknown or unavailable. Exhausted native
rate-limit windows cannot produce a green connection result. A catalogue is not
model entitlement. Protocol reference: [official app-server documentation](https://learn.chatgpt.com/docs/app-server).

The existing atomic model-configuration store retains bounded last-outcome and
last-success summaries outside configuration/history/revision/digest. Verification
success is recorded atomically with its existing configuration receipt. A real
request records success only after canonical output validation, using its frozen
selection reference. Replaying a receipt or invocation does not update its time
or dispatch again. No historical timestamp is inferred from filesystem metadata.
The private summary binds the complete registered model including verification
reference, admitted backend policy and dedicated account/login generation.
Native token refresh does not import Desktop/CLI accounts. No account identifier,
token, prompt, output or raw provider error is included in the health wire.

Failed verification and failed/uncertain dispatch retain the registration and
mark the model for verification. New outcomes invalidate cached health immediately;
collector publication compares the original outcome snapshot under the same store
lock, so it cannot overwrite a newer failure with an older success. Concurrent
registration edits reject an old request's observation. Metadata, account loss,
connection failure and drift take precedence over historical success. Last success
is still readable as historical evidence, and becomes stale after 15 minutes.
A reachable connection without recent model proof requires explicit verification;
this label grants no invocation authority and does not change routing admission.

OOS/Console validate optional finite last-success fields, timestamps, references,
identity and freshness. Old wire responses remain accepted. Malformed observations
become unknown health while configuration/recovery remain usable. Console extends
its existing metadata strip and actions, with no second interface. Verify remains
an explicit existing model.register command; routes and history are preserved.

Startup test isolation also includes the private STATE_ROOT. Previously, negative
startup tests could delete the live core-online signal while their commands and
receipts were mocked. The fix confines that invalidation to a temporary test
root. The normal core status/readiness procedure, never a fabricated marker,
restores post-start observations.

## Review Areas

Identity/secrets: exact dedicated account custody and login generation, no browser
credential path or ambient account import. Runtime/AI: fixed native metadata only,
no tool execution, context submission, inference retry or model adoption. Delivery:
Gary source identity, exact-head delegated review, CI-equivalent proof, equal
merged trees and exact composed acceptance remain required. Unknown completion,
policy, integrity and schema errors still prevent fallback.

## Validation

Producer tests: 34 routing/binding/timestamp/failure/replay checks passed. Core
unit tests: 77 passed with 4 native-only skips. The corrected unit suite retained
the real core-online signal unchanged through full Platform validation. OOS:
1706 tests passed/2 skipped, API/bundle/governance and fetched-origin/main
base-aware record/mutation validation passed. Console: 823 tests, architecture
guards, types, production build, repository validation and zero production audit
vulnerabilities. Both backends passed read-only isolated visual proof with
unchanged revision13 and reachable existing controls. The exact pinned Codex
0.163.0 executable's exported schema proves the new metadata request format;
this schema inspection used no account or inference. Full Platform make validate
passed on the final committed candidate after fetching origin/main. Exact-head
hosted checks passed and all three merged trees equal their Gary candidates. Actual native connection/request evidence is
operating qualification after exact composed activation; synthetic tests and an
isolated visual preview do not claim remote account access.

## Rollout And Rollback

Land the compatible OOS contract and Console, Platform producer, then exact
Security acceptance. Use the existing complete-runtime activation procedure,
preserving the original durable bundle, identities, routes, accounts and history.
The prior reviewed composition remains the rollback authority. New private
summaries are ignored by the older store reader and do not grant permissions.

## Decision

Approve the exact reviewed owner revisions/tree bound in the paired composed
decision after passing local and hosted validation. Operating evidence remains
a separate post-activation proof; no native account success is claimed here.
