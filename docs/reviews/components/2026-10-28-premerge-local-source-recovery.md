# Pre-merge Local Source Recovery Review

## Summary

- date: 2026-10-28
- decision: `approved`
- classification: owner maintenance, extending the existing source lifecycle
- implementation: [OOS PR390](https://github.com/mfshaf7/operator-orchestration-service/pull/390)
- existing composition: [exact Console capability review](2026-10-28-console-capabilities-exact-composition.md)

Approve the bounded delivery-lifecycle correction and its inclusion in the
existing local Console composition. Source acceptance and commissioning remain
distinct from the pending native Purpose, health and durable-run demonstrations.
This creates no new ART scope, workflow, identity or runtime capability.

## Scope Delta

Gary candidate `03c95c6ca3814232d0334642d7cfa2b698f8c5f8` merged as
`80323d653575cd19b77d51e2fe6be5aca995b490`, with unchanged tree
`f4d9dabf0008bf114017a3a2cc6a1d5f3eb14ab7`. The review compared the exact
five-file change against `5df11256a02298bce88707c89c9faa9bef6f454d`:
the existing lifecycle inspector/evaluator, faithful tests, primary operator
surface and existing security-tagged source record. The paired
[finite decision](2026-10-24-configurable-ai-routing.yaml) and
[prose source list](2026-10-24-configurable-ai-routing.md) select the merged OOS
revision together. Other accepted source bindings remain as previously reviewed.

The inspector now observes current local source while its merge-ready PR is
open or draft. Unpublished, dirty, wrong-branch or diverged source returns to
the existing source gate before human review or merge. The existing Gary
publisher and approved renewal then handle a clean correction under its
original scope. A published correction receives fresh exact-head evidence and
approval; the previous packet remains immutable. Merged/finalized history still
works after local source cleanup.

The exact candidate passed the committed base diff, all 1,671 unit tests with two
intentional skips, every workflow CI bundle/contract/documentation validator,
both Docker target builds, API health and unconfigured-worker fail-closed smoke.
The four regression cases fail on the accepted base and pass after correction;
they also exercise the actual work-session publish/renew action mapping and
preserve the prior packet. Hosted exact-head CI passed in
[40584247027](https://github.com/mfshaf7/operator-orchestration-service/actions/runs/40584247027).
Full local results are retained in the existing private
`local-evidence://governance-operations-console/.art/console-capability-completion-20261027/`
root under `premerge-local-source-ci-results.json` and its command logs.

## Review Areas

### Identity and delivery

No source credential is issued by inspection. Publication and renewal keep the
original approved owner, branch, base, intent, expiry and Gary identity. Dirty
or mismatched source is blocked rather than published. Existing Architecture,
Security and source-review gates remain; a prior approval never authorizes a
changed PR head. No raw push, engineering token for an ART session, registry
rewrite or new source endpoint is introduced.

### Secrets and runtime

The extra observation uses the existing bounded local Git adapter, without
credential reads, provider effects or raw source projection. Completed source
history does not depend on a removed worktree. The patch changes no Temporal
definition, durable authorization record, workflow/activity identity, queue,
worker image, network grant or model route. The accepted manifest digest remains
`sha256:c786d34579937ab09eb12340b5ac2e4831783416bf111a66bd7ca9898465cc73`;
its bytes, expiry and original generation remain unchanged. The previously
reviewed admission, same-generation restart and fenced retirement controls still
apply. This review does not create a successful native run receipt.

### AI and operator boundaries

Models gain no approval or source-effect authority. Existing model choices,
effort settings and account custody remain unchanged. The operator-facing next
action comes from the same OOS lifecycle; the Console remains its adapter.
The source bug required a bounded local coordination-cache recovery in the
existing session. That historical recovery preserves old WGCF custody and is
distinct from qualification of this repaired runtime.

## Decision

`approved` for the exact merged OOS source and existing bounded local composition.
Preserve currently accepted execution sources while staging. After paired
source acceptance, Platform must commission the complete exact source set,
verify current source/worker/manifest identity, restore ordinary refresh bindings
and retire temporary source resources. Reuse the accepted durable generation;
this delivery-only change supplies no reason to retire or replace it.

Native stories #1339, #1341 and #1346, their Feature outcomes, PI Objective and Epic closure remain
pending. Source review, CI and a ready worker do not satisfy those operating
obligations. Rollback reverts this OOS change and its paired source acceptance
together while preserving prior packets, source intents, Git and owner evidence.
