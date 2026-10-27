# Console Capabilities: Exact Composition Acceptance

## Summary

- date: 2026-10-28
- decision: `approved`
- initiative: `openproject://work_packages/1332`
- final review: `openproject://work_packages/1345`
- accepted design: [bounded source-design review](2026-10-28-console-capabilities-source-design.md)
- architecture: `architecture-packet:delivery-1332-v1`, schema6,
  `sha256:afa065834ed8bfff220c465def360522e45379cec1c42a051e372cac76594649`

Approve the exact source composition and bounded local commissioning below.
This satisfies `gate:1332-exact-composition-merge` and completes the source
acceptance part of `gate:1332-source-activation-chain`. It does not close the
three native operating stories, assert their outcomes, admit another definition,
or authorize stage/production operation.

## Scope Delta

| Owner | Accepted source |
| --- | --- |
| Console | `d0df22a5b9b88157409f6c877f53aa4b6e4714a7` |
| OOS | `5df11256a02298bce88707c89c9faa9bef6f454d` |
| Platform candidate | `a2fd8102881779cdaec7adf1368f8869372f8c51` |
| Platform candidate tree | `af13ceec2792db3e87c000e4d92734c874182b21` |
| WGCF | `1fc25783c59d1a6b0eb9935f42b0ee1fd81cf144` |
| CGG | `e29c59a4ed56048f6aa47bb924899566a5e68bae` |
| Workspace contract baseline | `912fbd2131101fce75acc5efc34a94b5f6366835` |
| Studio execution baseline | `84b7e7a596ce3d6f1c5853bbf1c348611ed9cdb6` |

Existing permitted record-only Workspace Governance and Studio advancements
remain record-only; this review does not repin their execution or weaken those
checks. The Platform candidate is intentionally unmerged. Its actual merge must
preserve the reviewed tree. The existing paired
[finite decision](2026-10-24-configurable-ai-routing.yaml) and
[source list](2026-10-24-configurable-ai-routing.md) bind that exact tree and
the unchanged inherited composition authority.

The review inspected the new private profile-request composition, independent
observation refresh and durable composition adapters, the existing lifecycle
publisher, their actual emitted configuration, the primary complete-runtime
coordinator, operator instructions, artifact-integrity policy and negative
cases. New helpers remain Platform implementation; this repository records
judgment and reviewed data.

### Validation boundary

Exact candidate `a2fd8102881779cdaec7adf1368f8869372f8c51` passed committed
`git diff --check origin/main...HEAD` against fetched base
`25ab9f3862b3c7b3b455188f90b6223f0d4ea9a9` and the complete local
`make validate` using CI's existing locked OOS contract source. Its result index
digest is `sha256:28694955bcdc109accce63a2e69b1c105bce6969e08be06cd0f4a2d370658889`.
The bounded private evidence is retained under the existing
`local-evidence://governance-operations-console/.art/console-capability-completion-20261027/`
root with the `effective-target` validation binding/results/logs.

Focused source proof includes50composition/filesystem cases,74runtime checks
with four documented native-only skips,78controlled recovery cases and14real
Git profile-lifecycle cases. It includes the effective environment after the
shared composition's endpoint override, checked through the real OOS role
validator. Source-only fixtures are not native operating evidence.

The [existing Platform PR347](https://github.com/mfshaf7/platform-engineering/pull/347)
is the publication target. This review accepts the exact locally validated
candidate, as allowed by the architecture. Publication/readiness must reconcile
that same head after this gate clears. GitHub CI must pass at the identical
candidate before Platform merge. An earlier failed or different PR head is
not accepted evidence, and this review does not waive CI.

OOS source validation at the selected merged revision passed in
[40550401315](https://github.com/mfshaf7/operator-orchestration-service/actions/runs/40550401315).
WGCF source validation and the published image at the selected revision passed
[39944188220](https://github.com/mfshaf7/workspace-governance-control-fabric/actions/runs/39944188220)
and [39944188198](https://github.com/mfshaf7/workspace-governance-control-fabric/actions/runs/39944188198).
Read-only Platform observation at2026-10-27T20:33:22Z saw all six admitted
components available. That timestamped component snapshot is not qualification
of the new request or durable-run paths; ordinary activation must recheck live
dependencies and publish fresh observations.

## Review Areas

### Identity and explicit decisions

Console retains its authenticated caller and bound accountable operator. The
same human may submit and explicitly review a caller-owned Purpose request.
The separate `platform-engineering/model-profile-lifecycle` fulfiller has a
distinct credential and no operator binding. Unrelated existing caller grants
and aliases are preserved. No model approves requests, merges source, or
supplies a final governance decision.

The API identity remains `operator-orchestration-service-api`, workflow identity
`oos-workflow-worker`, and activity identity `wgcf-activity-worker`. The workflow
worker receives selected runtime fields rather than the API credential set.
WGCF performs its existing bounded read-only activity and owns its local
evidence; OOS owns aggregate state, retry, cancellation and receipts.

### Private source evidence and secrets

Current registry publication does not depend on a previous transaction. Original
request history uses private same-UID files with hashed names, bounded size,
canonical digests and exact original request/revision/fulfillment binding.
Publication does not make a request completed without canonical OOS applied
evidence. Historical source remains available after a later registry change or
baseline restore. Missing, altered, symlinked or cross-request evidence denies
success. Credentials remain server-only; existing account custody, model/effort
choices and the six-purpose baseline remain unchanged.

### Honest observations

The independent oneshot/timer reuses the admitted six-component collector and
120-second validity window. It has its own nonblocking lock, bounded command
and service times and256MiB service limit. It does not wait on credential renewal.
Collection completes before atomic private publication. Failed collection
leaves prior bytes to expire, and incoherent health/receipt reads fail closed.
Unobserved products remain explicitly unknown; replicas do not prove endpoint,
workflow or business success.

### Exact durable admission and recovery

The reviewed proposed Platform bundle is retained in
[`console-capabilities-1332/manifest.json`](console-capabilities-1332/manifest.json).
Its exact digest is
`sha256:c786d34579937ab09eb12340b5ac2e4831783416bf111a66bd7ca9898465cc73`.
Security approves these proposed bytes; Platform issues them unchanged through
its accepted owner lifecycle into the fixed private read-only mount. Security
does not perform runtime effects. The existing ten authority records identify
contract/source qualification, active component admission and this decision;
their accepted outcomes are admission judgments, not fabricated native-run
receipts. Operating qualification remains separately required below.

Only `validation-readiness-run` version1 in the existing local Temporal profile,
operator namespace and authenticated Console caller is admitted. The shared
Platform endpoint producer supplies the exact same full target to the bundle,
OOS and WGCF. Both OOS roles revalidate the original manifest/record bytes and
current lifetime before use. The proposed authorization expires
`2027-01-25T20:38:00.181250Z`; expiry is enforced, not silently extended.

The activity image is exactly
`ghcr.io/mfshaf7/workspace-governance-control-fabric-worker@sha256:b6f76760c67c64264bdd652d6da9365e8cd34fba73f583a18b6180a563419c97`.
Published OCI metadata binds WGCF source
`1fc25783c59d1a6b0eb9935f42b0ee1fd81cf144`; runtime also checks the baked
source revision. Tags, other worker bytes and other definitions are not admitted.
The existing finite integrity policy covers that worker repository. Deliberate
installation of the reviewed policy precedes commissioning; no browser or model
supplies root paths, image references or commands.

An ordinary restart under valid authority preserves original bundle bytes,
generation queue, run IDs and history. Suspension drains API start ingress and
ordinary workflow pollers, then invokes the existing fenced OOS retirement
operation in a bounded job. Platform verifies the original-generation signed
receipt before withdrawal. The job retains the owner/network identity, selected
worker configuration and scoped keys; it receives no general API credential set.
Uncertain acknowledgement reconciles the same job. Failed/expired retirement
preserves evidence and blocks completion. A retired digest cannot be reactivated
without fresh accepted authority and verified retirement.

## Decision

`approved` for the exact source tree, inherited boundaries and bounded local
commissioning above. Platform merge requires green exact-head CI and must retain
the accepted tree. Preserve the accepted execution sources for credential and
record refresh while the new composition is staged; coordinate activation,
retire temporary bindings and prove normal refresh afterward.

Native1339 must prove request/review/fulfillment, immutable history and baseline
restoration. Native1341 must prove actual expiry and recovery. Native1346 must
prove the original run across worker loss/replay plus owner/aggregate receipts
and control denials. Those stories and their parents remain open until their
real evidence is finalized. This approval is not their completion evidence.

Rollback uses the existing Platform procedure and fenced lifecycle, preserving
canonical requests, Git history, retired generations, private owner evidence
and account custody. No hardware-corruption injection, new controlled-proof
permit, arbitrary command execution, stage or production authority is included.
