# Console core and configured-provider lifecycle security delta

## Summary

Review corrective maintenance of ADR-030's separate management and provider
availability. This extends existing Model Operations, the gateway and observation
timer. It creates no provider registry, daemon, account authority or browser
credential path. The previous [recovery timing review](2026-10-30-console-recovery-timing.md)
and [composed AI routing review](2026-10-24-configurable-ai-routing.md) retain all
unchanged controls. Runtime activation requires the exact merged sources/tree
in the paired composed decision; this draft is not operating evidence.

## Reviewed Source

- operator-orchestration-service: Gary candidate `e3a19757102b7a0ef769376f80d3a461f1c92b9c`, merged `a58a4dabadb498fee219da0c967dbebd32b5f30c`, equal tree `f83a22f1b7d656db2e44c13e3062517afb0fac6a` ([PR396](https://github.com/mfshaf7/operator-orchestration-service/pull/396)).
- platform-engineering: Gary candidate `ae636eda67ac00f4abf425417128a0b5de728ce8`, merged `1a1c2b3eb8a712845d02191ce3d6954272737145`, equal tree `fd4cd6b8f539540d211cae791cdb895b4114719e` ([PR353](https://github.com/mfshaf7/platform-engineering/pull/353)).
- governance-operations-console: Gary candidate `445f362bc00bcbe3584532ae405953916668b2f1`, merged `9776edb757e33317661feb32caa99130376a760c`, equal tree `b65ea0e1170b588d95eea7875b71f4653f835cec` ([PR151](https://github.com/mfshaf7/governance-operations-console/pull/151)).

## Scope Delta

The managed gateway's Kubernetes readiness uses its existing core `/healthz`
endpoint. Its configuration, owned artifacts, identities, storage and management
remain required; external provider capability is checked separately. The
complete-runtime status no longer requires an unused legacy Ollama binding when
managed routing is enabled. Purpose/caller/data/output policy and strict selected
model integrity remain invocation gates, including explicit legacy selections.
Standalone legacy gateway readiness retains its original `/readyz` behavior.

After successful core checks and a durable receipt, Platform writes a private
same-boot, exact-decision core signal. Accepted activation/restart invalidates
that signal before effects; cleanup removes it. The existing observation timer
refreshes provider metadata only after that signal, never during core startup.
No provider probe can hold startup open or restart the core. The six admitted
runtime components and their independent freshness contracts remain unchanged.

Platform checks only registered backends with fixed policy-selected endpoints.
Local checks read version, model catalogue and native effort metadata, bounded
responses/values and a finite collection budget. They do not perform inference,
load a model, send project context or change configuration. Dedicated-account
inspection remains within scoped Vault/projected-home custody and is serialized
with account users. It does not launch Codex or claim connectivity/entitlement
from an account file. Busy, unavailable, unprobed and changed metadata remain
explicit, without raw provider error messages, secrets or browser endpoints.

Health is private disposable evidence, not configuration or authorization. Its
revision/digest binding and 120-second validity prevent stale observations from
representing a newer registration. Owner and Console validation reject/drop
unknown fields, invalid identity, duplicates and invalid freshness. Bad evidence
becomes unknown health while authenticated configuration/recovery stays usable.
Existing backend availability metadata remains explicitly not-probed; the new
optional health projection is independent and backward compatible. OOS includes
health only when the upgraded consumer requests `include_health=true`; previous
strict consumers retain their exact response during staged replacement.

Console reuses Compact Control/Teras patterns. It displays the configured
primary's health and the selected model's accepted/observed runtime and digest.
Only explicit Verify & update registration uses existing model.register and its
bounded synthetic verification/receipt. Success preserves the stable model ID,
routes and historical evidence; failure or uncertain completion adopts nothing.
Reconcile still recovers the original command. In-flight selections remain frozen;
unknown completion, integrity, output and policy errors never permit fallback.

## Review Areas

Runtime/AI: removing an external capability from core readiness does not accept
inference or provider drift. Every invocation still validates the profile,
backend permissions, registered runtime/model/effort, audit and output. No new
automatic retry, default choice, fallback route or dynamic backend endpoint.

Identity/secrets: existing OOS management auth, operator binding, dedicated
account and Platform-only finite timer request remain. Browser inputs cannot
supply destinations, shell, account material or authority. Refresh accepts only
an empty object and returns finite non-secret observations; actual credential
bytes stay within existing private projections. No root or network-policy grant.

Delivery: owner maintenance remains Gary-authored with exact human review and
merge. Exact composed acceptance precedes normal activation. Retain original
owner data, sessions, requests, activation generation and durable manifest.

## Validation And Operating Boundary

Source validation passed: OOS1705 tests with two existing skips, bounded API227
contracts/bundles, governance and fetched-base checks; Console822 tests, all
architecture guards, typecheck, production build, source safety and zero
production dependency vulnerabilities; Platform full `make validate`, including
77 complete-runtime tests (four existing skips), 28 routing and 15 management
checks. Exact-head hosted checks and delegated human reviews passed for all
three owner PRs; merged trees equal the reviewed candidates.

Focused checks cover offline/drifted local metadata, no routine inference or
Codex launch, account-presence limits, same-boot post-core ordering, optional and
invalid/stale health, unchanged configuration and existing uncertain-command
recovery. Native core recovery and source-bound Console
health/re-verification readback remain required before operational completion.
Known hardware faults are not repaired or hidden by this delta.

## Decision

**approved** for the exact owner revisions/tree selected by the paired composed
decision in the existing local dev-integration boundary. Owner validation, hosted
checks and exact review have passed; runtime proof remains separate. No stage/prod, remote/team identity, new provider protocol, source
version trust bypass or automatic configuration adoption is authorized.
