# Console capability commissioning recovery

## Summary

- date: 2026-10-28
- decision: `approved`
- classification: existing owner maintenance for Epic1332 operating obligations
- owners: Platform Engineering and Governance Operations Console
- authority: existing delegated human review; Security closure remains with the main agent

Approve the exact bounded changes below for source landing and normal local
dev-integration commissioning. They repair two observed gaps in the existing
capability composition; they do not introduce a new architecture, runtime
identity, model route or canonical decision authority. The preceding
[exact composition](2026-10-28-console-capabilities-exact-composition.md) and
[local-source recovery](2026-10-28-premerge-local-source-recovery.md) remain
the inherited controls. Native stories1339/1341/1346 remain open.

## Scope Delta

Console [PR141](https://github.com/mfshaf7/governance-operations-console/pull/141)
was authored by Gary at `88d223cd158eb1eef17a8c5ac67fa126add99cb1`, reviewed
by delegated `mfshaf7`, and merged as
`0f58ce9b9226b42b30cbb617155404c6e5336d90`. The merged tree is exactly
`4448fbda396d537bd33eecce7ea96ede9a03c7b4`, identical to the reviewed candidate.
The base was `d0df22a5b9b88157409f6c877f53aa4b6e4714a7`.

The live owner admitted starts, but the Console had no Start Run action. The
repair exposes the existing read-only validation-readiness definition with a
selected initiative, current-source review, explicit approval and an original
run recovery read. OOS still owns admission, execution and receipts. No new
OOS endpoint or orchestration definition is introduced.

Platform [PR348](https://github.com/mfshaf7/platform-engineering/pull/348)
is reviewed at Gary candidate `1f9e65b3f58c7af2bb560447a17f2389d63a71c0`,
tree `0547b1607e2a069421f99d533a887d02c493f88d`, against merged base
`bc0332b566cc78e2dbd577f15d437d619e7606b3`. Source acceptance precedes its
merge; the merged tree must be identical. The existing profile binder reads
the actual patched Secret resourceVersion into its existing rollout annotation.
This corrects an observed Secret/process mismatch after base composition
restored credentials while retaining the old annotation. Unchanged publication
keeps an already consuming process. Missing publication evidence fails closed.
Two rollback unit fixtures also explicitly bind their temporary workspace root,
preventing the test from reading the real activation bundle.

The paired [finite decision](2026-10-24-configurable-ai-routing.yaml) and
[prose source list](2026-10-24-configurable-ai-routing.md) advance only these
two owners. OOS remains `80323d653575cd19b77d51e2fe6be5aca995b490`. The existing
manifest remains
`sha256:c786d34579937ab09eb12340b5ac2e4831783416bf111a66bd7ca9898465cc73`,
and the WGCF worker digest remains
`sha256:b6f76760c67c64264bdd652d6da9365e8cd34fba73f583a18b6180a563419c97`.
All durable bundle bytes, expiry and original generation remain unchanged.

## Review Areas

### Identity, secrets and delivery

Console POST uses existing same-origin mutation authorization. Its server owns
the authenticated OOS caller and configured accountable operator; browser
actor injection is rejected. The Platform fulfiller remains distinct, with no
human-operator binding. This patch adds no caller, secret class or permission.
Secret contents remain in the existing protected owner path, never browser
responses, source or proof logs. Only the publication version enters the
existing annotation digest. The normal Gary publication and exact-head human
review boundary remains in force.

### Current source, explicit decisions and recovery

Start rereads the admitted definition and selected initiative's existing
canonical source envelope. Authority, owner, record, Epic identity and version
must match. A stale reviewed version is refused before owner mutation. The
explicit approval binds source and purpose for fifteen minutes; the server
constructs the exact OOS wire digest and request. The browser supplies no opaque
source, actor or approval references.

An uncertain response retains the same frozen request, idempotency key and run
identity. A later local refusal cannot erase an earlier unknown effect. Owner
acknowledgement may have a null projection and is displayed as admission, never
completion. Exact original-run GET and refresh work independently of the run
register. No automatic replacement run is created. Receipt and source bindings
are checked on returned owner data. Existing retry/cancel controls remain.

### Runtime and AI boundaries

The selected definition remains bounded WGCF validation/readiness; no model
invocation, source-authoring privilege, deployment or Delivery completion is
granted by Start. API, workflow and activity identities remain separate. The
Secret publication correction uses the existing Platform rollout rather than
another supervisor, source pin, recovery mechanism or credential authority.
Keep accepted primary checkouts while staging; coordinate both source changes
with this acceptance before normal commissioning.

### Evidence and its limits

Console committed full CI-equivalent validation passed against fetched
`origin/main` at its base: repository and compile validators, 800 semantic
cases, architecture checks, TypeScript, production build and production
dependency audit. Three browser interaction cases passed using explicitly
synthetic owner effects: human review/null-projection admission, lost-response
same-request retry, and original recovery after reload with an empty register.
The actual OOS normalizer accepted the wire vector and rejected tampered
source. A live read-only preflight made four owner GETs, zero business writes
and zero model calls, confirming admitted current initiative source. Hosted
[40600679490](https://github.com/mfshaf7/governance-operations-console/actions/runs/40600679490)
passed at the exact candidate. These are source/protocol proofs, not native
run-start operating acceptance.

Platform's nine focused cases distinguish stored Secret and consumed process
environment, including resumed base composition, unchanged no-extra-rollout
and unconfirmed-publication denial. The new stale-consumer case fails on the
preceding implementation. Full committed `make validate` and fetched-base diff
passed. Hosted validation
[40594829430](https://github.com/mfshaf7/platform-engineering/actions/runs/40594829430)
and posture40594829341 passed at the exact candidate. Live process consumption
was repaired by normal restart as containment; full commissioning and native
fulfillment proof remain pending.

Detailed commands, source bindings, browser evidence and read-only receipts are
retained in the existing private
`local-evidence://governance-operations-console/.art/console-capability-completion-20261027/`
under `orchestration-run-start-*` and `purpose-profile-consumption-*`.

## Decision

`approved` for the exact source/tree set and existing local dev-integration
composition. No new standards, exceptions or runtime authority are required.
Commission through the normal Platform lifecycle after the accepted Platform
tree lands. Confirm actual process credentials, current source selection,
independent health observations and original worker/manifest identity. The
deliberately paused coordinator and its attached host services must return
through that normal lifecycle, without detached replacements.

Close native1339/1341/1346 only after their actual Purpose lifecycle,
wall-clock health expiry/recovery and original-run worker-loss/replay/control
exercises pass. Review and CI do not satisfy those obligations. Rollback pairs
the two implementation reverts with their previous finite source acceptance,
preserving original requests, packets, registry history and durable evidence.
