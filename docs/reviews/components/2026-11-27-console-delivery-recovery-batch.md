# Console Delivery recovery and source editing

## Summary

The maintenance batch recovers the original result when a Delivery response
is interrupted, retains source drafts across Work Session replacement, and
reconciles a stored Technical Plan revision with the active OpenProject plan.
The Console also improves readable navigation, review dialogs and the source
editor. The existing Console composition and Delivery ownership apply.

## Scope Delta

The batch adds authenticated result reads, staged Work Session replacement,
a method-scoped registry lookup, same-operator session renewal and bounded
source section edits. It reuses the existing owners and the existing
protected source publication and plan approval paths.

## Review Areas

**Command and session authority.** Result reads bind the caller, operator,
work item and original command. Work Session replacement stages its successor
before changing the active alias and retains predecessor drafts for authorized
inspection. Platform renews the already admitted local operator session through
the existing host issuer. Revocation and session identity checks continue to
apply. Source publication and approved case verification retain their separate
approval and verification gates.

**Artifact custody.** The existing Broker credential can read the latest
verified lineage reference for one exact Technical Plan subject through its
own audited method scope. The read supplies the previous stored artifact
for a retry. The approval remains bound to the active OpenProject plan,
source facts and current Work Session impact. Registry append-only checks
and the optimistic OpenProject write remain in effect.

**Source editing.** A section edit is bound to an existing scoped work
session, clean source revision, file digest and permitted text range. It
uses a distinct operation that a whole-file-only source executor rejects
before writing. Private draft saving retains the original command receipt.
Explicit operator review still gates the action that applies a draft.

**Validation.** The exact Console source passed 1,208 checks, its production
build and dependency audit, and 70 browser cases. The Broker passed 2,104
tests with two existing skips. Workspace Governance cross-owner contract
checks and the WGCF API image smoke check passed. The disposable source
chain used the Console routes, Broker HTTP, private source executor, actual
local Git and Platform session issuer. It rejected expired access and stale
sections and recovered the same draft by original command. The previous
source executor refused a candidate section draft before a write. The
candidate reopened the saved draft after that refusal. Exact storage
compatibility kept the older active draft readable and retained predecessor
bytes through replacement.

## Rollout and recovery boundaries

Confirm the latest connected disposable owner readback and exact reviewed
source set before live activation. Reconcile pending Work Session replacements
before restoring older readers. Keep acknowledged private drafts and the
previous accepted source and artifact available. A pending bounded section
draft requires a compatible Broker and source executor to proceed.

## Decision

`approved` for the exact five source trees below under standing operator delegation. The connected rehearsal used the candidate Console routes, Broker, real isolated OpenProject, WGCF custody and local Git executor. It recovered the original PI receipt after dropping the response. An edited plan retry preserved the previously active plan through rejection, then recorded once and read back the exact new plan. A competing approval was rejected. Switching the Console, Broker and WGCF reader to the previous reviewed source and back retained the same plan and objective.

Platform's normal activation and the live owner readbacks remain the operating check.

| Owner | Reviewed PR | Merged revision | Reviewed and merged tree |
| --- | --- | --- | --- |
| workspace-governance | [PR #328](https://github.com/mfshaf7/workspace-governance/pull/328) | `421adb7d23c3a5a281bd3a315cb69992872327db` | `c6f66fe11469a46acd89a0d2723e7cd66c207829` |
| workspace-governance-control-fabric | [PR #128](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/128) | `6f3033bad9cfa41de200f640320a1536c052414f` | `8d7b4e3f5aee2877ecc79239c422d5a1b2bfa540` |
| operator-orchestration-service | [PR #437](https://github.com/mfshaf7/operator-orchestration-service/pull/437) | `5bb05fd3e0e0b70c3118436098977dd82ae821ab` | `181511b0cc084d3a952d341dd0d8debe50887230` |
| governance-operations-console | [PR #198](https://github.com/mfshaf7/governance-operations-console/pull/198) | `f626ff5af6ecdd4c4262fce81ed09532bfa92bd6` | `6c2c4c5c5dd3f925c9acc14ddfbf0708b476e016` |
| platform-engineering | [PR #393](https://github.com/mfshaf7/platform-engineering/pull/393) | `65707c132324ff372212068a6e00cdc9ef69692a` | `b9a1e57769645c06daf6f0632206e082d9796559` |
