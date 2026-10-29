# Saved operator work and original browser recovery

## Decision and scope

- Date:2026-10-29.
- Decision:`approved` for the exact reviewed source in the existing local lane.
- Classification: operator-approved maintenance across the existing OOS and
  Console owners; no new ART item, database, daemon or installer.
- Activation authority: the existing
  [finite composed decision](2026-10-24-configurable-ai-routing.yaml).

Review the Work Design, Refinement and Orchestration saved-input extension.
Gary authors both owner PRs. The main reviewer retains Security closure and the
delegated accountable human reviews/merges exact source. Source acceptance is
separate from actual original-content recovery and operating qualification.

## Reviewed implementation

[OOS PR394](https://github.com/mfshaf7/operator-orchestration-service/pull/394)
candidate `bb658761aeda4635225335153ffbbf0571ebcb23` owns private saved input,
strict commands and the authenticated source-projection read. The companion
[Console PR146](https://github.com/mfshaf7/governance-operations-console/pull/146)
candidate `60b4adf59e6a5ad361757493926047e9e655c146` owns its same-origin adapter,
existing-editor integration and browser recovery. OOS merged as
`670dc727194facae776633656b71417c993b824d`; Console merged as
`753162abc3b85b67240e5b64037c4da88b2eb1f0`. The bounded historical-state
correction in [Console PR147](https://github.com/mfshaf7/governance-operations-console/pull/147)
candidate `479fc73f4cf57a86bc2445496bd8ca3cd8924f8c` merged as
`9bb812189bb25f073a96f27d90f73b7c11690f79`, the final accepted Console revision.
It explicitly labels unuploaded historical copies as browser-only without
starting owner writes. Exact candidate/merge trees match.
The finite decision selects the final merged owner revisions only after exact
candidate/merge tree equality is proven. Other owner pins, Platform tree,
durable activation manifest/generation and worker digest remain unchanged.

### Identity and private data

OOS requires caller-specific credentials and the existing configured caller to
operator binding for reads and writes. Private subjects include caller,
operator, kind and subject identity. Console derives operator identity from its
verified Platform session and uses server-only credentials; browser-supplied
identity and configuration are not accepted. Canonical source-envelope binding
and payload digest validation protect reads. Same-origin writes reject foreign
origins; requests and content have finite byte limits.

Existing private OOS transactions supply kernel locks, fsync and atomic commit
on the current persistent state volume. Source/runtime proof confirms the root
is actually configured; a missing explicit root leaves this service unavailable.
No root credential, provider token or raw model context is exposed by this API.
Saved notes/source may be private operator input, so they stay in the owner
volume and never enter public source or automatic model invocation.

### Save semantics and history

Revision comparison prevents silent concurrent replacement. Exact latest-command
replay handles a lost save response; conflicting/stale inputs return failure.
Acknowledgement follows durable commit and binds exact content. Record digests
detect altered bytes; unavailable/corrupt state is not projected as success.
One bounded subject is loaded at a time; no all-project payload/history scan.

Finalized brief versions cannot be altered or removed by draft saves. Recovery
keeps newer finalized versions and still uses the same backend guard. Current
and older browser bytes are preserved separately before normalization or
autosave; malformed/unsupported originals remain downloadable. Choosing a server
copy also preserves newer conflicted browser edits. Different-operator
acknowledged caches are not automatically imported into another actor's state.

Payload JSON text preserves fractional canvas geometry without changing WGCF's
formal integer-only artifact contract. The WGCF registry stays bounded to its
admitted formal classes; it does not become a general draft store. Backend save
time and import origin do not attest legacy authorship or approval.

### Workflow and Console boundary

The current editors and typed session formats are reused. Hydration gates their
autosave controllers so an empty startup cannot overwrite saved input. Pending,
saving, acknowledged, unavailable and conflicting states remain distinct.
Explicit disconnected preview stays local; configured owner failure cannot
select it. Read-only history uses the original Work Design screen and does not
write owner state. Restore controls are locked there.

Saving/restoring inert drafts cannot apply ART, approve a brief, record a
qualification, request implementation, execute definitions or invoke a model.
Native workflow/source/packet revision and human acceptance controls remain in
force. Apply receipts and saved artifact acknowledgements stay distinct; the
handoff view links the saved-work screen without claiming that its canonical
receipt restored missing historical browser originals.

## Evidence and operating limits

OOS passed 1,702 tests with two existing skips, deterministic bundles, API/docs,
fetched-base owner gates and actual API/worker image smoke. The configured API
image saved/read exact content across container replacement; an unconfigured
worker remained denied. Console's full architecture, behavior, type, build and
dependency checks passed; the final conflict-preservation amendment includes
its own regression; the final historical-state source passed the full 816-test
check. Hosted exact-head owner CI passed.

Five actual records were recovered from Console-only managed profiles, including
five named sessions and four finalized brief versions. Controlled candidate
client/store proof recovered exact raw originals and diagram snapshots from fresh
storage after owner reconstruction. This is source proof, not live Console
commissioning or evidence about the operator's separate desktop browser.
The three retained 1332 versions contain snapshots but no complete finalized-brief
object; 1349 retains its complete object. Missing historical fields remain marked
unavailable. Recovering exact retained bytes does not invent missing approval,
authorship or finalization checks from a diagram or canonical apply receipt.

Before completion require normal exact-source activation, actual original-data
migration through the Console, fresh-browser retrieval, readonly final-history
inspection and service recovery. Do not claim inaccessible/cleared desktop data
was recovered. No browser-only backup protects against loss of the underlying
disk; whole-product off-machine disaster recovery remains separate qualification.

## Rollout and rollback

Merge the OOS owner record/source, Console owner source, and then the paired
Security index/decision. Preserve accepted main consumers until this chain is
ready. Normal Platform activation supplies the existing mounts and credentials.
Rollback uses the prior accepted source decision while preserving new private
saved-work state and raw browser originals. No destructive migration or cleanup
of uncertain original data is authorized.
