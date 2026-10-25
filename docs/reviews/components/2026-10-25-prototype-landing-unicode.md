# Prototype Landing Unicode integrity correction

## Summary

Approve the Landing-local canonical-byte correction for the existing local
dev-integration composition. The actual Studio source is
`workspace-prototype-studio@84b7e7a596ce3d6f1c5853bbf1c348611ed9cdb6`,
merged through Gary PR42 from reviewed candidate
`55d1909ce788e64979aa7e7f9853cde37262d0db`.
The [existing exact composed decision](2026-10-24-configurable-ai-routing.yaml)
and [source review](2026-10-24-configurable-ai-routing.md) remain the activation
authority. No new identity, source permission, service, flag, decision version,
model entitlement or release authority is introduced.

## Scope Delta

The real Epic1323/1328 Prototype exercise received a native ready-state
rejection before source preparation: Studio reported registry digest5cf9ee17
while WGCF observed9e01a343 at the same e04dfd2 source revision. Recomputing the
actual committed registry proved the difference was ASCII-escaped versus
unescaped UTF-8 JSON. Landing had reused the separate Delivery packet codec,
while native Console/OOS/WGCF Landing already used compact sorted UTF-8.
Fixing only the observed registry hash would still reject legitimate Unicode
Entry/Request artifacts and emitted readbacks.

The correction therefore uses one Landing-local codec for all Landing artifact,
registry, record and readback integrity. Imported-file manifests and unrelated
Delivery/Closure protocols retain their established bytes. Existing committed
Landing artifacts were inspected and contain only ASCII; their digests remain
identical and full historical-record validation passes. No retained artifact,
readiness decision, failed request or business lifecycle state was rewritten.
The original stopped exercise request has no apply, preparation, PR or source
mutation and remains retained. A fresh explicit corrected request must bind the
new accepted source and its actual state.

## Review Areas

Identity and source authority are unchanged: the Console's admitted operator,
OOS ownership/caller checks, source-owner review branch, WGCF readiness and exact
apply/merge/readback remain separate controls. Valid Unicode text is accepted
under the already established native Landing format; changed content, wrong
expected source/state or a broken artifact chain still fails closed. Invalid
canonical JSON is rejected before source mutation. The repair grants no
filesystem, network, provider, approval or model capability.

Evidence integrity is improved across the entire affected chain. The two
original failures reproduce before correction: unchanged Unicode registry state
is wrongly stale, and a genuine native Unicode Entry is rejected. All95 Studio
tests and full `make validate` pass at the exact committed candidate, including
Unicode apply/replay/readback, changed-content denial before mutation and
unchanged packet-format golden evidence. Four Preview tests require a clean
reviewed source checkout; the full suite passed after committing the validated
candidate rather than weakening that existing prerequisite.

Six additional isolated checks execute the actual Console command builder, OOS
normalizer/apply builder and output validator, WGCF service with private SQLite
and its real committed-Git authority reader, and the Studio CLI. They prove
agreement on the actual Unicode registry, native Unicode request/readiness,
owner apply and OOS consumption of both emitted artifacts, exact replay and
receipts, plus owner/readiness tamper denial. These use synthetic subjects in a
disposable Git/ledger sandbox and do not claim live provider or runtime proof.
The exact-head Studio CI40158278806 passed and accountable human review approved
that Gary head before its maintenance merge.

## Decision

- decision: `approved`
- scope: the exact Landing-local implementation correction and unchanged
  seven-owner local dev-integration composition with the selected Studio source.
- operating requirement: normal exact-source activation/status and fresh native
  Prototype Landing, editor/import/amendment/reload/cancellation proof in1328,
  followed by the existing real LittleList source delivery in1329.

The source correction does not complete that operating requirement. Preserve
all failed-request history, account/configuration custody, exact source/gate
bindings and review/cleanup controls. The delegated accountable reviewer retains
security and final landing judgment. No sub-agent was used. Stage/prod and
private-client qualification remain separate.
