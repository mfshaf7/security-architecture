---
native_release_activation:
  status: pending
  gate_id: gate:ai-routing-composed-security
  reviewed_revisions: {}
  reviewed_platform_tree: null
---

# Console native governed-release submission

## Summary

Review the operator-approved extension of the existing Console → OOS → Platform
operation path. It reuses protected owner GitHub workflows; it does not introduce
a service, stage/prod executor, database, approval authority or generic script
runner. Gary authors source and the accountable delegated human reviews/merges.
The main agent retains Security judgment; this is not an independent assessment.

This review covers source design and local conformance. The exact composed
Platform activation decision, real dedicated-App commissioning and controlled
operating evidence are separate. Current live capability remains disabled.
The existing Platform resolver derives native authority only from accepted
activation metadata matching its exact current composed decision. It never asks
an operator to hand-pin a future decision digest into tracked Platform source.
Commissioning then explicitly connects the dedicated App; its missing lease
keeps native actions unavailable and does not block core startup.

## Scope Delta

The OpenClaw adapter supports its existing stage readiness, approved promotion
and production runtime-state workflows. Product support/maturity remains owned by
Workspace Governance. Other products retain inspection and their actual endpoint;
they do not inherit OpenClaw's release capabilities. Recorded source evidence,
executable action, observed health and readiness acceptance remain distinct.

Console reuses the release Details/Review pattern with owner-defined finite
fields. Actual verification results start blank. Explicit review binds immutable
source and input. OOS retains the approved command in its existing private
journal. Platform validates actor, intent/approval digest, product, capability,
source and fields, then retains its write-ahead record before dispatch. A valid
pre-dispatch rejection gets a no-effect terminal receipt instead of disappearing
from original-request recovery.

The dedicated GitHub App has Actions write plus Metadata, Contents and Pull
requests read, for the selected Platform repository only. The App, account,
installation, exact permissions, numeric repository and bot identities, token
expiry and contract/security bindings are verified. A temporary Metadata-read
installation inventory token proves that broader selected repositories are not
hidden by the restricted runtime token; that inspection token is revoked before
the final scoped lease is issued. Its separate Vault key never
enters OOS, browser state, source or receipts. A private atomic bundle and shared
lease/exclusive rotation reuse Platform custody. Old tokens retire before
replacement; uncertain revocation cannot mint an overlapping replacement.
Optional renewal reuses existing maintenance and does not gate core startup.

Dispatch selects only three fixed workflows on main. Before dispatch, Platform
checks exact main and existing human environment reviewers/protected-branch
policy. Before effects, each existing protected job binds native App actor,
repository, workflow, original attempt, reviewed SHA and input digest. Free text
enters shell through quoted environment values. The existing workflow token
pushes an original branch without force and opens its source review. The native
App cannot write source, approve the environment or merge the PR. Existing manual
workflow entry remains available, with its normal protected environment.

Unknown dispatch acknowledgement only discovers the original correlated run; no
automatic retry/rerun is allowed after its marker. Normal approval/review waits
are not failed releases. Completed workflows remain nonterminal until the source
review is merged, its merge commit is on main and exact desired state is read
back. Squash merges are supported. Failed-after-push branches remain recoverable.
Cancellation targets only the original in-flight run and claims no rollback.
Terminal receipts are immutable. Polling unchanged phases does not grow events.

The browser retains only an opaque recovery pointer before submission; canonical
commands/evidence remain in OOS and Platform. Exact-original reads do not require
a current executable catalog. Closed optional native DTOs reject foreign routes,
private fields, mismatched products/workflows and unsupported evidence. Existing
legacy operations retain their receipt meaning. Read-only GitHub navigation stays
available when source/capability is unavailable. History retains existing bounded
workspace pagination and its documented cold file-discovery scaling limit.

## Owner-data advancement within accepted code

Routine release merges must not require changing the running Console code or
repinning its source group. The Platform-owned read adapter uses the dedicated
App's existing Contents read scope to verify current owner main against the
accepted executing checkout. Complete Git-tree leaf equivalence is required for
all paths except the explicit existing OpenClaw release/verification/lifecycle
records and associated GitOps desired-state YAML declared in
`console_release_source.py`. Main must retain accepted ancestry. Mutable records
must remain regular files; each read blob must match its verified tree identity.
Fetched code is never executed or installed in the provider.

A non-record source change, incomplete tree, foreign lineage, wrong repository
or mismatched blob withholds new native authority. Source availability is distinct
from credential commissioning. Current owner main, reviewed local snapshot and
retained owner snapshot are explicit closed DTO postures. Only current owner main
can enable a new request. Read-only links and original command/receipt recovery
remain separate from new-action admission.

One bounded private derived snapshot survives restart, with an integrity digest
and code-revision binding. It is never canonical work-state authority. In-memory
proof/document caches retain at most four revisions and reuse unchanged immutable
blobs. The existing provider response limit bounds tree reads; incomplete/slow
refreshes return labelled retained source rather than fabricate freshness. The
adapter never advances a checkout or fetches a repository clone. This follows the
existing code/data authority distinction without creating another control plane.

Repeat-use qualification exercises two consecutive native transitions, each with
a protected-run/PR/merge/readback sequence, different owner-data revisions and the
same accepted runtime-code revision. It also covers cold offline snapshot reads,
corrupt cache rejection, non-record source rejection, missing readiness inputs
without loss of runtime capability, complete-tree/blob/lineage denial and bounded
warm reads. GitHub remains synthetic in this qualification; real account and
protected workflow operating acceptance remain unproven until commissioning.

## Review Areas

- Identity/secrets: purpose-separated installation token, fixed selected scope,
  explicit commissioning, bounded lease/rotation and retryable revocation custody.
- Delivery/runtime: protected environment and human PR merge remain external
  authority; exact run/source/effect binding, no unsafe redispatch or rollback claim.
- AI: the model may assist/author source within its existing lane; it receives
  neither runtime token nor environment approval/source-merge authority.

## Evidence Boundary

Local qualification uses current pending owner source and a synthetic GitHub
transport, not a real App or protected stage/prod run. Platform tests cover
dispatch ambiguity, replay/cold recovery, credential outage, stale-source
no-effect receipts, rejected targets/permissions, run/intent tampering, approval
and review waits, squash merge/readback, retained branches, cancellation and
credential rotation/revocation. The authenticated composed browser proof covers
Console → OOS → Platform, lost acknowledgement with one dispatch, explicit
approval/review waits, final desired-source readback and cold OOS recovery.
No live release, environment, approval, source push or merge was performed.

Source review/landing must retain final owner CI-equivalent checks and exact-head
review. Local working-tree proof does not replace that later evidence. Live
activation must bind the final reviewed composition/decision digest, verify the
real App account/install/scope and existing protected environment, and retain real
run, approval, PR/merge and desired-state readback. Runtime health/UAT needs its
own owner evidence. If the real provider cannot satisfy those facts, withhold
native availability; core inspection and startup remain independent.

## Decision

`approved` for this bounded source extension and its default-disabled posture.
This does not activate native release authority, waive final source checks, or
approve a stage/prod action. The fresh exact-composition operating gate remains
required. Rollback withdraws the connection/capabilities, revokes its token and
retains original commands, receipts and source branches for accountable review.

## November 2 reviewed Console batch three composition

The operator approved the reviewed batch for publication after live-preview
inspection. This extends the existing composed local installation; it creates no
new service, authority, autonomous workflow or installer. Gary authors owner
source; the delegated accountable human reviews and merges. This is the main
agent Security judgment, not an independent assessment.

The delta includes truthful Lifecycle/Registry/profile/product readback and native
profile request recording, guarded original-operation recovery, scoped history,
consistent waiting feedback, stable Model/Prototype geometry and the approved
primary Console activity/Focus layout. Loading is tied to actual pending requests;
known data, errors, reduced motion and command guards remain. Cosmetic primary
Console styling does not change Workbench primitives or canonical work-state truth.

Owner-native release dispatch remains separately default-off. The optional new
review activation metadata remains pending, with no commissioned dedicated App.
The source update cannot widen Gary credentials, enable native release authority,
automatically approve an environment or merge a runtime-source PR. Existing manual
owner workflows, read-only navigation and original-operation recovery remain.

Qualification includes Console884 semantic tests, full architecture/types/build,
zero production dependency vulnerabilities and desktop browser proofs; OOS1754
cases with1752passing and2existing skips, deterministic bundles, schema/API and
base-aware owner checks; Workspace Governance300unit cases and full hosted checks;
and complete Platform make validate on the exact committed source in isolated CI
context. The full Platform check caught and corrected helper imports preceding
module-path initialization; its existing38-case source-intent regression passes.
Synthetic GitHub transport and preview data are presentation/source qualification,
not operating acceptance or proof of complete live audit coverage.

The original durable activation generation and reviewed WGCF worker digest remain.
No owner request journal, model selection, account custody or business record is
reset. Final normal managed activation and read-only operating checks must pass
before declaring this batch live. Source rollback selects the preceding accepted
composition while preserving mutable owner records and receipts.

The exact merged sources selected by the existing composed YAML are:

| Owner | Merged source |
| --- | --- |
| context-governance-gateway | `context-governance-gateway@e29c59a4ed56048f6aa47bb924899566a5e68bae` |
| governance-operations-console | `governance-operations-console@e1c2477c3d0a5756ec832095db3233d946c396c4` |
| operator-orchestration-service | `operator-orchestration-service@11d3a959b7d463a3b33152839fd31cefdbbdff2e` |
| platform-engineering | `platform-engineering@b40bb3421f19d7a2727c1ddef62536c6939703e1` |
| workspace-governance | `workspace-governance@c442245b3bcc9671bf2ddf14adb473e09229d3f6` |
| workspace-governance-control-fabric | `workspace-governance-control-fabric@d3516e570aec812a3cd66933387d89b6f1fc94e4` |
| workspace-prototype-studio | `workspace-prototype-studio@84b7e7a596ce3d6f1c5853bbf1c348611ed9cdb6` |

Platform tree: `platform-engineering-tree@aaa827463809d2ef0e8d3d18572b367fd8b6d451`. Source PRs: [Platform359](https://github.com/mfshaf7/platform-engineering/pull/359), [OOS402](https://github.com/mfshaf7/operator-orchestration-service/pull/402), [Console160](https://github.com/mfshaf7/governance-operations-console/pull/160), [Governance318](https://github.com/mfshaf7/workspace-governance/pull/318). Each merged tree equals its tested Gary candidate. The generated index now includes the merged owner records.

## November 2 managed integration activation correction

Live read-only publication proof returned dev_integration_not_configured because
the staged profile/product flags were absent from the normal managed binding.
Use the existing canonical-record binding shared by activate and restart to set
both flags; consumed-state readiness rejects either disabled flag, and existing
rollback disables/removes them. This is the already-reviewed bounded readback and
profile-request recording, not native owner-workflow dispatch. The separate native
release App remains pending/uncommissioned. No account, journal, image, identity,
privilege, workflow engine or activation generation is added or reset.

The existing77 lifecycle cases pass with four native-only skips, including both
disabled consumed-flag cases and rollback; profile/product suites and hosted owner
checks pass. Platform PR360 merged with exact candidate/merge tree equality.
Decision: approved for normal managed restart and subsequent native read-only
profile/product qualification. Readiness is not inferred from source alone.

Current source: `platform-engineering@a5e751df89b476f6515c02184df1f5c02de88e45`.
Current tree: `platform-engineering-tree@244baa26da3d47d24dee294a2867fb672051e1f5`.
