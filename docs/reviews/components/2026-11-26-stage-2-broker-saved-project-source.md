# Stage 2 Broker saved project source and Run coordination

## Summary

The Broker source for Delivery #1386, #1387 and #1392 captures the pinned
project source and retains the original Run request before dispatch to Platform.
This review covers the Broker source landing in [PR #433](https://github.com/mfshaf7/operator-orchestration-service/pull/433).

The Gary-authored head is `d43ef23f8d3cc78eca8049972d0c05ea069f2080`.
Its tested merge against Broker
`fc211b2101aca91133d230e9244bc69c3daf1e34` has tree
`51051a85d72d5f839d337bea04014c13f44fb5bb`. GitHub's test merge and the
local merge independently produced that tree. The PR changes exactly the 20
reviewed paths. The existing source-start scope and #1393 prerequisite remain
part of the approved #1384 Technical Plan.

## Scope Delta

The Broker adds bounded saved-source capture to its existing authenticated
source executor. Capture reads an admitted Git commit and the acknowledged
saved draft, writes content-addressed blobs and a manifest to a private
snapshot volume, and returns an opaque reference. The image includes the
contract needed to validate the snapshot. The original Run identity, source
digest, setup and observation are bound by the Broker before dispatch.
Platform remains responsible for materializing and running the project.

This review does not update the current Console or Platform activation
bindings. The existing
[resource-record identity review](2026-11-26-delivery-resource-record-identity-composed.md)
continues to describe that live composition. The owner revision and reviewed
tree must be checked again if the source or merge base changes.

## Review Areas

- **Identity and access.** Delivery binds the caller and operator, the
  covered work item, source session, approved base and repository admission to
  the existing source lease. Prototype uses its own admitted source owner
  and custody, and the caller cannot pick a filesystem root or arbitrary
  repository. The executor rejects absent or mismatched command context.
- **Secrets and source custody.** Capture reads admitted Git paths and the
  exact stored overlay. It rejects unsupported entries such as links and
  submodules, out-of-scope paths, baseline mismatches and altered retained
  blobs. Snapshot bytes remain in the private volume. New files are verified
  by size and content digest before being referenced.
- **Delivery and recovery.** A current source lease and setup scope govern
  the first dispatch. The Broker records the exact Run request before the
  Platform effect and reconciles the original operation on interruption.
  The cross-owner shape is checked against the source, setup and manifest
  digests. The retained snapshot and the authorized Git branch are separate
  records. Gary authors source, and the delegated human approval is bound to
  the exact PR head.
- **Runtime responsibilities.** The reviewed Broker image packages the
  schema and handoff code. The API health smoke passed, and the worker
  denied execution without admission. A separately reviewed Platform
  composition must qualify the snapshot mount, execution isolation,
  connection policy and rollback before live activation.

The exact Broker branch passed 2,087 tests, with two skips and no failures.
Required GitHub validation passed. The source tests exercised real Git bytes,
saved overlay and baseline mismatches, rejected links and altered retained
blobs, and recovery of the original Platform observation after a lost reply.
An isolated candidate rehearsal exercised the private source handoff to the
paired Platform implementation. That rehearsal does not certify a merged or
activated composition.

## Decision

`approved` for source landing of the exact Broker PR head and reviewed merge
tree above. The Platform implementation review, controlled activation and
operating proof remain governed by the existing Stage 2 plan. Verify the
landed tree and include the Broker change record in the generated Security
index before closure.
