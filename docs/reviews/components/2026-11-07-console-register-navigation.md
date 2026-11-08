# Console register navigation and bounded reads

## Summary

- Date: 2026-11-07
- Classification: operator-approved maintenance, outside active ART scope.
- Landing Unit Decision: feature_single_landing_unit,
  maintenance-console-register-acceptance-20261107.
- Review subjects: Console, OOS, WGCF and Workspace Governance; OpenProject
  remains the existing canonical Delivery backend.
- Decision: approved for commissioning after exact merged-source binding and
  passing required checks. Native operating proof remains pending.

## Scope Delta

### Design intent

Growing registers need consistent navigation without treating a bounded overview
as complete authority. Use existing owner read interfaces and the existing
Console/Platform/Security composition rather than a new service or control.

### Implemented controls

Console preserves existing register columns, global summary/board scope and
selected originals. It offers shared 25/50/100 display sizes, default 25,
continuous ranges, search/filter reset, loading/error/retry and bounded
continuation. Configuration snapshots page locally. Only the chosen page size is
stored in localStorage; project records and original evidence are not cached
there by this change. Edited drafts and independently selected originals survive
list changes without being inserted into page counts.

Native read windows compose at most six source pages and at most 100 displayed
records. They retain owner cursors unchanged and reject denial, source drift,
duplicate identities, loops and incompatible totals. Native signed private
Registry pages request 25/50/100 directly; the Console validates the actual
signed page and never reuses its digest for combined records. Short mixed
legacy/private windows remain explicit rather than fabricating completeness.

OOS extends existing authenticated GETs with opt-in register views. It scopes
history before bounding it, preserves independent pending requests and immutable
owner originals, and retains legacy response shapes. Prototype metadata and
transitive evidence are selected from one owner revision. Closure retains all
qualifying historical outcomes. Temporal/Delivery pages and selected workflow
progress do not become decisions or global board evidence.

WGCF's explicit products-page contract binds source revision and selection;
selected readiness is hydrated with the existing actor/freshness checks. Complete
continuity remains global. Invalid metadata cannot be hidden by a page filter.
The latest-readiness database query is batched without schema changes.

### Source and operating evidence

The owner source PRs bind the exact implementation heads and fetched-base
validation. Governance's structure/contracts, 12 lifecycle-proof scenarios and
315 tests pass. WGCF's full 597-test suite passes. Console's architecture,
1,026 semantic tests, typecheck, dependency audit and isolated production build
pass, along with the retained multi-register browser walkthroughs at 1280/1700.
OOS's full suite passes 1,938 tests (1,936 pass, two intentional skips), and
all 94 focused HTTP cases pass, including native register caller/query boundaries.
Both owners' API/worker images build and their health, source/default-denial
smoke checks pass. WGCF source custody and UID10001 checks also pass.

The initial OOS full-suite failure was an old expectation that the newly admitted
register route was invalid; the test now rejects an actually unknown view and
separately proves the admitted route. WGCF's first API check used worktree alias
names instead of the expected workspace owner layout; with canonical owner names
mapped in the isolated validation lane, the complete 597-case suite passes.
Neither failure is evidence of hardware or source corruption.

Source and isolated browser checks do not establish native runtime qualification.
After exact-source acceptance, Platform must activate the existing composition
and native Console reads must prove supported views, real original access and
size choices. No fabricated business records or final workflow decisions are
needed for read-only qualification. Existing unrelated experimental provider
account limitations remain as previously disclosed.

## Review Areas

Identity/secrets: existing caller-bound server credentials and operator scope
remain enforced. There are no new accounts, secrets or browser credentials.
Private source remains subject to existing read authorization and AI context
admission; paging does not grant model access.

Runtime/delivery: bounded authenticated read projections extend existing
endpoints. Existing canonical mutation/form validation, human review/approval,
Gary source identity, exact-source Security decision and Platform activation
remain authoritative. No database migration, new service, worker activation or
privileged host capability is introduced. Existing complete-runtime rollback
restores the previous accepted source/decision pair without a data migration.

AI: model/profile configuration presentation is paged over the same complete
configuration. Routing, provider authority, effort, approval and model-mediated
canonical changes are not expanded.

## Decision

Approved for the existing local dev-integration commissioning boundary after
passing owner/CI checks and exact merged-source binding. The composed finite
YAML and its companion review must identify those exact merged revisions before
activation; this document alone cannot change a runtime source pin.

The main agent retains Security closure and final landing judgment under the
operator's standing delegation. Gary authors source; mfshaf7 remains accountable
reviewer/merger. This is not an independent external security attestation. No new
finding, waiver, accepted risk or ART item is required by this bounded read/UI
delta. Final operational completion remains conditional on native readback,
source lease revocation and branch/worktree cleanup.

## Review coverage dependency

The first Governance CI run rejected four expired baseline-review dates
(2026-11-05/06), independently of this contract's source checks. CGG repository
and component share one baseline; Studio and the AI gateway use their existing
baselines. Those three baseline artifacts now record current source/control
inspection, focused validation, preserved findings and a six-month review date.
No runtime authority or accepted source pin changes in this prerequisite review.
The final exact-source composition/index acceptance follows the owner merges.


## Final qualification repair delta — 2026-11-07

The same maintenance boundary includes Console PR170 and Platform PR375. Native
qualification exposed a compact Model register with a 39px body under a 52px
header, and kubectl stream-creation timeouts while health probes still succeeded.
These observations do not establish source corruption or a new business defect.

Console restores the compact register body minimum, bounds row-driven layout
height and allows the existing outer work area to scroll on short screens.
The shared portal selector measures before paint and opens above the trigger
when the options cannot fit below. Existing columns, summaries, selection,
keyboard controls and mutation gates remain. Fourteen affected browser cases
pass at 1280/1700; two further Prototype cases verify full menu viewport bounds.
Architecture guards, 1,026 semantic tests, typecheck, public-source validation,
locked dependency audit and isolated exact-source production build pass.

Platform drains the existing tunnel child's stderr in bounded chunks, retains
its diagnostics and recognizes the reproduced kubectl stream-creation timeout.
That signal causes only the existing child process group to be reaped and its
supervisor to exit for the existing delayed service restart. Health success
cannot clear that transport fault. Unrelated diagnostics and HTTP error
responses do not cause recycling. No request body is inspected or replayed, no
owner workload is restarted and no credential or privilege is added. Seven
real-child tests and the complete-runtime suite (94 tests, four intentional
skips) pass; full owner validation passes. The existing connection runbook and
source record carry the procedure and rollback boundary.

Decision: approved within the existing local commissioning boundary, subject to
exact merged Console and Platform revision/tree binding in the composed decision.
The already accepted native model-profile policy descendant is included in the
new full Platform tree; its prior review remains applicable. Prior identity,
secrets, AI and canonical mutation controls are inherited without expansion.
Native reads passed after connection-only refresh during initial qualification;
final operating status and browser proof must follow activation of these exact
repairs. This decision grants no new runtime action or release maturity.


## Registry, refresh and attention projection maintenance — 2026-11-08

Operator-approved owner maintenance is tracked as Landing Unit
`maintenance-registry-usability-20261107`; the corresponding exact-source
acceptance is `maintenance-console-registry-acceptance-20261108`, with decision
`feature_single_landing_unit`. This extends the existing review; it introduces
no new service, provider permission, data store or canonical mutation authority.

The intended operator outcome is to preserve source truth while making existing
workspaces readable and usable. Registry classification, inventory activation,
private-record scope and pending versus completed outcomes remain distinct.
Preparation, uncertain submission and history recovery keep their original
request identity. Dependent repository reads cannot remain falsely loading after
an owner failure. Quiet background reads retain selections and edited drafts;
explicit navigation and failed reads retain visible loading/retry and write gates.

The implemented shared register changes provide readable column minima,
remembered numeric column widths and internal resize boundaries with an anchored
outer edge. Optional browser preferences contain layout only, not project records
or authority. Existing workspace structures, paging, original record access,
mutation controls and outer scrolling remain. Reviewed panel spacing, loading
feedback, single-line status pills and constrained modal content use existing
components. There is no broad replacement of the interface baseline.

Primary attention now distinguishes retained diagnostic failures from outstanding
workflow work. Source authorization attempts resolve only with a validated,
successful revocation receipt bound to the complete original intent and command;
a newer unrelated success, shared profile, timestamp or expiry is insufficient.
Original failed operation records remain inspectable. Readiness checks all known
unresolved operations, preserving real recovery and pending work. Shared owner
composition preserves record freshness rather than promoting stale records to
current because the transport succeeded. Stale records cannot supply executable
routes. Partial Prototype collections and bounded Platform/Orchestration windows
are explicitly qualified in counts and existing Agent context metadata. Incomplete
history is informational and does not disable otherwise valid current actions.
Owner authorization, context admission, model routing, credentials and final
approval remain unchanged.

Source evidence: architecture guards, 1,042 semantic tests, typecheck,
public-source repository validation and production dependency audit pass. The
retained preview walkthrough covers the repaired workspaces, table resize and
persistence, loading and freshness paths at 1280/1700. Ten focused attention,
colour and Pulse browser scenarios pass; the four attention/history scenarios
also pass after the final completeness refinement. Connected preview reads show
nine current source feeds, two actions, one decision and zero blockers, with no
page errors or business writes. All 84 operation records, including the two
historical failures, remain retained. These are scoped source/preview results,
not a universal readiness or independent external security attestation.

Decision: approved for the existing local dev-integration boundary after exact
merged Console source, production build and CI verification are bound in the
finite composed decision and its companion review. Platform, OOS, WGCF, CGG,
Governance and Studio selections, durable manifest and worker digest remain
unchanged. Native proof must follow normal accepted-source activation. The main
agent retains Security closure and final landing judgment under the operator's
standing delegation; Gary authors and the delegated human reviews and merges.
Rollback uses the prior accepted source/decision pair; there is no data migration.


Exact source acceptance: Console PR171 merged as
`24b1027321e7d0b72aa143d9329c61cc2f4e5b3f`, from Gary candidate
`9a7773095f52de7b27c1ed52047bb32d6d9e3da1`, tree
`0b3a95e598ab76b84ff20edd02571f94912e982b` for both. Exact-head CI and the
local production build pass. The finite decision and companion review select
this merged revision; other composition bindings remain unchanged.
