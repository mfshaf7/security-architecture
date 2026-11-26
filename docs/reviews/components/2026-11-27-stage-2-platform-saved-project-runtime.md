# Stage 2 Platform saved-project runtime

## Summary

Platform implements the saved-project runtime for Delivery #1388–#1391.
[Broker PR #433](https://github.com/mfshaf7/operator-orchestration-service/pull/433)
supplies the reviewed saved-source handoff. [Platform PR #392](https://github.com/mfshaf7/platform-engineering/pull/392)
contains the exact Platform source. The Platform
candidate at `552f5e5c03cbc33b428855c1055c09c549d5fdf2` has tree
`4701551960cb9a743643e3012c4bab328399641e` against protected Platform main
`74a46b229aaa5d1bc8b3efa209c1d63743262391`. The runtime implementation
from the original review remains covered. The revised head binds operating
evidence to the named rehearsals and includes their source and regression
tests. GitHub's test merge against protected main produced the same tree.
The candidate passed Platform validation, including 50 focused runtime
and evidence tests.

## Scope Delta

The existing authenticated Platform provider gains an optional project
runtime owner. The owner requires its exact Security decision and a current
private admission for the internal local Dev Integration scope. The
Broker retains the saved-source binding and the original operation.
Platform stages the admitted snapshot, qualifies the build, and reads the
result back. This source review does not change the active composition
decision or authorize a runtime rollout.

## Review Areas

- **Identity and custody.** Requests enter through the existing protected
  provider. Project, subject and admitted scope are checked before dispatch.
  The snapshot is bounded and content-verified. Dependencies use an
  approved offline cache bound to recipe, image and lockfile.
- **Runtime isolation.** Each project uses a dedicated namespace and
  quotas. Workloads run as non-root without a Kubernetes service token
  and with a read-only root filesystem. The paired frontend and API
  share the qualified source and artifact. Their network rule is bound
  to the same project and Run generation.
- **Lifecycle and retained data.** Stop releases both workloads.
  Resume reuses the original setup, artifact and retained volume. A
  failed update preserves the previous pair and its data. Reset is
  refused in this scope. The current Technical Plan puts the visible
  Cancel interaction in a later owner stage.
- **Operating evidence.** The isolated K3s rehearsal used the Broker
  command and authenticated Platform HTTP provider. It served the paired
  frontend/API, denied access to the other project, rejected an
  over-quota Run without interrupting the active pair, and preserved
  the retained-data witness across Stop and Resume. A failed update
  left the previous pair serving. Reset returned 409 and left data
  untouched. The disposable namespaces were removed.

### Operating case evidence

The rehearsal starts only from clean exact Platform and reviewed Broker
checkouts and uses an isolated temporary project and local provider. The
runtime cases include active-pair update failure, interrupted Stop recovery,
retained volume and declared scratch, and native capacity refusal. Both
application processes confirmed network denial against the configured Broker
and Kubernetes services. Disposable resources were removed after the test.

Platform retains the exact result privately with both source revisions and
a content digest. The read-only commands name one approved case each and
check its required observations. The actual Broker evidence adapter
rejected missing case evidence even when the general tests passed, then
accepted the four cases after owner receipt verification. The file permissions
preserve the established Platform owner trust boundary.

## Decision

`approved` for source landing of the exact Platform PR head and reviewed
tree above through the existing required checks and delegated review.
The [recorded plan work-start review](2026-11-26-recorded-plan-work-start-composed.md)
and [Broker publisher review](2026-11-26-protected-base-source-publication.md)
continue to govern the active composition and source publisher.
Live operating proof requires the reviewed Platform and Broker revision
set, a supported rollout and rollback, and the approved normal Console
readback.
