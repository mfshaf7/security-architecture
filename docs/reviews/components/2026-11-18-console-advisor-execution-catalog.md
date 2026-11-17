# Console advisor, Context Brief, Execution and Catalog maintenance

## Summary

Fresh delta review of the complete operator-approved maintenance batch, now
merged in its four implementation owners. Main-agent Security judgment and
final landing judgment use the existing delegated operator authority; this is
not independent assurance. Landing Unit Decision: `feature_single_landing_unit`,
`maintenance-project-membership-review-20261117`, retains Security's separate
review and rollback boundary. No ART item or new acceptance mechanism is added.

## Scope Delta

- Context Brief retains multiple named architecture/sequence views, explicit
  selection and finalized snapshots. Diagrams describe the system under design;
  ART task ordering does not substitute for architecture. Existing private
  saved-work transactions retain the document; no browser-only canonical store.
- Trusted OOS role guides describe each advisor's actual workflow. Supplied
  selected and recorded upstream facts, references, coverage and revisions are
  distinct from untrusted user text. Closed owner reads supply selected project
  details; reference strings do not imply loaded contents. CGG enforces complete
  selected drafting context before provider dispatch. Supporting source files
  and inactive diagrams remain read-only, within existing project/path scope.
- Saved bounded working conversation uses existing private saved-input custody
  with caller/operator/project binding. It is working data, never attested proof.
  Missing history, omissions, conflicts and interrupted outcomes are visible;
  restoration does not infer, apply or silently retry. No cross-agent global
  transcript store, automatic repository scan or provider tool is introduced.
- Native provider `draft_reply` grammar and OOS validation constrain advisory
  text/board/tree edits. Answer-only intent cannot mutate. Unknown, duplicate,
  read-only or unauthorized fields fail atomically. Console retains local review
  and explicit acceptance; final decisions and source/release actions stay
  outside model authority. Both actual provider profiles use this contract.
- Execution repairs work selection, current/history boundaries, technical-plan
  explanation and advisor, session recovery and review presentation. Existing
  canonical planning and source gates retain their authority and prerequisites.
- Catalog preserves reviewed revisions, exact accepted request bodies, native
  receipts and successful outcomes across later list failures. Stale unseen
  changes remain denied; historical receipt recovery never reapplies a newer
  decision. Loading, error, read-only/system-managed, eligibility, dates,
  repository linkage and bounded register navigation reflect owner truth.
- [Project membership](2026-11-17-console-project-membership.md) remains a closed
  extension for existing native users/groups and project roles, under the
  Delivery-only non-admin broker grant. It is not an account administration API.

## Review Areas

Identity and delivery: Console verifies the existing session and server-bound
operator. OOS authenticates caller-specific credentials, validates Delivery
permission and rejects browser authority injection. Native OpenProject enforces
project role grantability, protected service/admin access and group propagation.
No Proposal, global directory, user creation or platform-production grant is
added. Assignee choices follow native assignment eligibility, not all members.
Membership effects and original request-bound readback receipts share a native
transaction; stale reviews and conflicting request reuse fail closed.

AI and context: trusted guides are maintained by the workflow owner; user and
upstream content cannot replace instructions or supply approval. Current recorded
facts take precedence over old conversation. Incomplete selected edits are
refused before inference. Ordinary bounded overview remains available. The
existing approved models, effort, caller binding, CGG receipts and explicit
human acceptance apply; no implicit model fallback or automatic inference retry.

Secrets and storage: credentials stay server-side. Conversations, memberships,
receipts and project details remain in installation-private operational storage
and bounded responses. No new public Git data export, arbitrary URL fetch,
generic privileged runner or live backend credential is added to the browser.
The three private developer review routes were removed before public validation.

Runtime: implementation sources are now merged and source-identical to their
reviewed Gary candidates. Fresh exact-source acceptance authorizes the existing
local complete-runtime activation path. It does not authorize Stage/Prod,
Delivery runtime execution or the separately pending governed-release feature.
Original incidents/history and owner data remain intact. Rollback selects prior
accepted sources and removes only the added broker role if needed, preserving
memberships, private drafts and immutable receipts.

## Evidence

- CGG: all 104 tests, compilation and JSON contract checks; exact-head CI passed.
- Console: 1,129 semantic tests, architecture guards, types, optimized build,
  public-source validation and production dependency audit; exact-head CI passed.
  Isolated browser checks cover filled forms, multi-view selection, read-only
  supporting context, conversation recovery, request origin, applied-receipt
  preservation and compact/large viewport containment. These are isolated
  conformance checks, not live-model or live mutation evidence.
- OOS: 2,007 tests passed with two existing skips; generated API contracts,
  synthetic examples, owner/base-aware mutation checks and API/worker image
  builds/smoke passed. Exact-head CI passed.
- Platform: 122 admitted dev-integration cases, 11 gateway cases, 10 Ollama
  adapter cases and native reply schema checks passed. Both older provider test
  fixtures were aligned to the stricter reply grammar; runtime validation was
  not weakened. Exact-head CI passed.
- Native membership: 18 rollback-only cases exercised authenticated native
  dispatch, add/change/remove, assignment visibility, exact historical replay,
  conflict/stale/protected/global-role denial, group propagation/cleanup and
  bounded paging/search. All temporary fixtures and receipt effects rolled back.
  An initial native 403 was resolved with the explicit project-only broker role;
  no global administrator grant or fabricated member result was used.

Source PRs, all Gary-authored, exact-head approved with passing checks:
[CGG 32](https://github.com/mfshaf7/context-governance-gateway/pull/32),
[Platform 381](https://github.com/mfshaf7/platform-engineering/pull/381),
[OOS 414](https://github.com/mfshaf7/operator-orchestration-service/pull/414),
[Console 179](https://github.com/mfshaf7/governance-operations-console/pull/179).
Merge order was CGG, Platform, OOS, Console, followed by this generated Security
index and exact-source acceptance. The source set is:

- `context-governance-gateway@b83b3978f04ce951226367a60117000290e1c86a`
- `governance-operations-console@560946028f30d8706ee460be539a501a8f821355`
- `operator-orchestration-service@492a2c6bb034cb649277658537e74bce66a0f69e`
- `platform-engineering@7cb8c908909878d2b63aa3da5e4eeb043dfd21ca`
- `workspace-governance@dd0a0c094e880e40297dcea484ebd8ad3c75ef7b`
- `workspace-governance-control-fabric@d3b8ba934275324abcb794c0276fd3dea0a9ceb9`
- `workspace-prototype-studio@07776dbcb13acaf8ad2d39d02c28929dd14f5fe3`
- `platform-engineering-tree@5db0593967d13b43a09dfedd84c08528c2b93ae7`

The unchanged accepted architecture is
`wgcf://artifacts/delivery-art/sha256/7715729bdb3420a790ff816d204c4c9c96a94745265444c517b2d02cb3e316b6`, digest
`sha256:7715729bdb3420a790ff816d204c4c9c96a94745265444c517b2d02cb3e316b6`.
The existing durable orchestration manifest and worker digest remain unchanged.

## Decision

`approved` for this exact coordinated local source set and subsequent normal
accepted-source activation. No new exception or Security risk acceptance.
Existing reviews continue to govern their unchanged boundaries. Fresh live
source/artifact/credential and owner projection readback is required before
claiming commissioned availability. Native model semantic quality and broader
future-work completeness are not established by deterministic conformance or
this source decision. Preserve prior accepted runtime and original data for
rollback; recurring known hardware instability is not repaired by this batch.


## Native gateway configuration deployment amendment

The first accepted-source rollout was rejected by native Kubernetes because
client-side apply duplicated the rendered gateway runtime into a 356,140-byte
annotation; the annotation limit is 262,144 bytes. The actual runtime data is
337,473 bytes and is within the ConfigMap data limit. This is a native deployment
admission failure, not damaged application data or a reason to relax AI schemas.

Approve the existing profile's namespace/name-bound runtime ConfigMap deployment
through server-side apply under `platform-governed-ai-gateway`. Only that finite
Platform-owned runtime object may transfer conflicting fields. Other resources
retain ordinary apply, and no caller-supplied object or arbitrary forced resource
path is introduced. Existing dynamic model-selection replacement semantics are
retained. No model, caller, credential, namespace, source, canonical mutation or
production authority expands.

Native Kubernetes server dry-run accepts all 16 exact rendered resources through
the amended split path. Structural equality proves every original resource and
all runtime data are preserved. The dry-run performs zero mutations; it does not
claim live commissioning. Source validators, admitted profile/runtime tests and
exact-head CI remain required. Merge the Platform repair first, regenerate the
owner change-record index, then bind its exact merged revision/tree in the
existing composed decision before normal activation. Preserve the original
failed rollout and prior accepted sources; do not delete objects, trim runtime
content or introduce a new acceptance mechanism.


### Exact source after native deployment amendment

Platform [PR382](https://github.com/mfshaf7/platform-engineering/pull/382)
passed exact-head CI and delegated review. The merged source tree equals Gary
candidate `2db9f7de3d8b6e83777adc213cbceb22fb2278f1`. The following source set
supersedes the earlier Platform pin for this bounded deployment amendment:

- `context-governance-gateway@b83b3978f04ce951226367a60117000290e1c86a`
- `governance-operations-console@560946028f30d8706ee460be539a501a8f821355`
- `operator-orchestration-service@492a2c6bb034cb649277658537e74bce66a0f69e`
- `platform-engineering@6f52edf1b8d2a3b747a72c64c777ba64b5ffd2bd`
- `workspace-governance@dd0a0c094e880e40297dcea484ebd8ad3c75ef7b`
- `workspace-governance-control-fabric@d3b8ba934275324abcb794c0276fd3dea0a9ceb9`
- `workspace-prototype-studio@07776dbcb13acaf8ad2d39d02c28929dd14f5fe3`
- `platform-engineering-tree@938ebaebd9d1c77b9f1a41d714d564346b8920b0`

All other accepted boundaries, architecture, durable manifest and native
commissioning obligations remain unchanged.
