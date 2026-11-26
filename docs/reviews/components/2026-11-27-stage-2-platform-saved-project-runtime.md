# Stage 2 Platform saved-project runtime

## Summary

Platform implements the saved-project runtime for Delivery #1388–#1391.
[Broker PR #433](https://github.com/mfshaf7/operator-orchestration-service/pull/433)
supplies the reviewed saved-source handoff. [Platform PR #392](https://github.com/mfshaf7/platform-engineering/pull/392)
contains the exact Platform source. The Platform
candidate at `f76068c51a9f6dc3828aefbd72688bfc573a77b5` has tree
`b19dd8c1d3c591d6557c136f1375244205794021` against protected Platform main
`74a46b229aaa5d1bc8b3efa209c1d63743262391`. The change contains 13 paths.
The 12 Console draft files and the existing larger Platform provider file
match the exercised candidate byte for byte. GitHub's test merge against
protected main produced the same tree. The candidate passed 44 focused
runtime and provider tests and the owner structure and document validators.

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

## Decision

`approved` for source landing of the exact Platform PR head and reviewed
tree above through the existing required checks and delegated review.
The [recorded plan work-start review](2026-11-26-recorded-plan-work-start-composed.md)
and [Broker publisher review](2026-11-26-protected-base-source-publication.md)
continue to govern the active composition and source publisher.
Live operating proof requires the reviewed Platform and Broker revision
set, a supported rollout and rollback, and the approved normal Console
readback.
