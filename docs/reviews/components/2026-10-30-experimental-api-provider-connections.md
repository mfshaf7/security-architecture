# Experimental API-provider connections security delta

## Summary

Review Epic1363's extension of the existing authenticated Models & routing,
OOS, governed gateway and Vault boundaries for named Claude API, DeepSeek API
and GLM/Z.AI Standard API connections. This extends the
[composed routing review](2026-10-24-configurable-ai-routing.md) and
[provider evidence review](2026-10-30-provider-health-evidence.md). It introduces
no service, caller identity, installer, autonomous decision or arbitrary endpoint.
Source qualification and live commissioning remain separate from vendor account
eligibility. No eligible vendor accounts were available.

The corrected native plan retains `architecture-packet:delivery-1363-v1`,
`wgcf://artifacts/delivery-art/sha256/3ff4b91d20e935119a778c324bc8a2548bf1263da015e4a87aff09800efa3cf7`,
digest `sha256:3ff4b91d20e935119a778c324bc8a2548bf1263da015e4a87aff09800efa3cf7`.
Its immutable predecessor remains retained. Two Security case classifications
were corrected to existing real-Git evidence after the preliminary compatibility
probe omitted required test evidence. All source units then passed the actual
owner coverage validator with both mandatory categories. Completed owner work
was retained; no profile, runtime gate or new control was invented.

## Scope Delta

### Reviewed source

- Platform: `1862fd3ab614761852ef98969ec2bbafcc1525d8`, tree
  `df6aa9c1ed887f9a4262d5ae0afa29621a5d26da`, including
  [PR355](https://github.com/mfshaf7/platform-engineering/pull/355),
  [PR356](https://github.com/mfshaf7/platform-engineering/pull/356) and
  [PR357](https://github.com/mfshaf7/platform-engineering/pull/357).
- OOS: `1eceee2afaf34dbf2fbe4bb142bcff9fba7799e0`,
  [PR398](https://github.com/mfshaf7/operator-orchestration-service/pull/398).
- Console: `a5660e4e42216fc1e4d408c137de824f4b11c684`,
  [PR154](https://github.com/mfshaf7/governance-operations-console/pull/154).

Gary authored the changes and the delegated accountable human reviewed and
merged them. The Console candidate and merged tree match exactly. All owner
hosted checks passed. The paired composed decision selects these source revisions
and the Platform tree while retaining the existing activation identity and gate.
Unchanged owners retain their accepted exact bindings.

### Implemented controls

API keys use explicit bounded transient ingress, separate from OOS's generic
queued requests. The configured operator, canonical command and exact returned
receipt are bound and checked across Console/OOS/Platform. Safe durable intent
precedes Vault CAS writes. Stored connection state, operation history, audit,
recovery drafts and receipts exclude keys. Raw input clears on submission,
close, selection change and page exit; it is not advisor or saved-work context.

Platform owns a finite sixteen-connection register and the existing narrowly
scoped Vault custody prefix. Rotation changes an opaque credential generation
and invalidates earlier model proof. Original-operation reconciliation reads
existing owner effects; it does not resubmit a key. Disconnect clears stored
material and fences uncertain prior writes. It does not revoke a vendor account's
key. Removal checks current model references, retires the identity and withdraws
its backend. Settings restoration cannot revive credentials or a retired backend.
Existing per-connection locking serializes retirement with backend registration
and restoration through their atomic configuration writes.

Native adapters use three fixed HTTPS origins. Metadata reads and explicit
inference are separate. There is no caller-selected base URL, redirect, SDK retry,
tool execution or private-thinking projection. Connection, response size, pages,
parallelism, output and verification budgets are bounded. Known pre-effect busy
may use existing explicit fallback; post-submission uncertainty, policy,
integrity, output, refusal and truncation errors stop without unsafe fallback.
Provider error bodies and key material are not returned or logged.

Exact model identity, actual native effort, seven existing task contracts,
configuration revision, credential generation and strict canonical final output
remain invocation gates. Claude's native grammar projection keeps unsupported
length constraints in the full prompt and authoritative local validator. Cloud
runtime/digest unknowns remain null. GLM uses exact manual model IDs with documented
protocol capability rules and explicit provider-default behavior for unknown
families. Verification is an explicit potentially billable action, disclosed as
up to 4,096 output tokens and 60 seconds.

Console reuses Compact Control/Teras and the existing model/default/override,
ordered-fallback and history controls. Experimental — real-account testing
pending remains visible on every new provider independently of authentication,
health or a successful probe. Missing current owner data fails closed without a
fixture fallback. Core startup remains independent of external AI availability;
new API accounts are not silently probed, registered or selected at startup.

## Review Areas

Identity/secrets: reuse existing authenticated Console/OOS operator binding and
Platform-only Vault authority. The new user-entered provider key is not Console
or OOS authentication. Protected custody and generation checks remain owner
controls; the browser cannot choose identity, account authority or destinations.

Runtime/AI: all existing purpose, caller, task, data and output restrictions
remain. Native metadata does not prove entitlement or product readiness. Models
receive no approval, source merge, deployment or canonical mutation authority.

Delivery: retain exact source/tree acceptance, Gary authorship, accountable human
review, finalized source evidence, and bounded rollback. The existing
`gate:ai-routing-composed-security` still precedes live activation. No stage,
production, team identity or real-account qualification is granted by this review.

## Validation And Operating Boundary

Platform's focused native/custody tests, thirty-four routing tests and full owner
validation/hosted checks passed. Corrective retirement checks include concurrent
registration/restoration and removed-connection history. OOS passed 1,712 tests
with two existing skips, twenty-three focused tests, closed OpenAPI/bundles and
base-aware checks. Console passed 829 semantic tests, architecture, types,
production build, public-source validation and zero production vulnerabilities.
Its complete native owner evidence and hosted checks passed on the exact head.

The isolated browser exercise intercepted every API. It proved all three presets,
Experimental display, key clearing, known revision rejection, one key submission
across lost acknowledgement/reload/reconciliation, disconnect/reconnect and GLM
manual entry. Screens were inspected. These controlled fixtures were never live
provider, account or configuration evidence. Existing live configuration/history
remained exactly revision13 throughout source work.

Some local Node/Next processes exited with SIGSEGV; the locked native compiler
matched its integrity-verified archive. Root cause remains unproven. A temporary
process CPU limit allowed the complete unchanged owner checks to finish and was
restored afterward. No source or hardware repair is claimed by these results.

Live commissioning must separately prove the exact accepted running sources,
real owner-backed unconfigured presets and Experimental labels, preserved
Codex/Ollama controls and unchanged full configuration/history. New vendor-account
qualification remains pending and cannot be promoted from these controlled tests.

## Decision

**approved** for the exact source revisions/tree selected by the paired composed
decision, within the existing local dev-integration boundary and with persistent
Experimental qualification. Native account eligibility, real-account protocol
qualification and live operating proof are not established by this source review.
The accountable human reviews and merges this decision before commissioning.
No finding requires another control, permission, mechanism or ART item.
