# Console source editor assistance and embedded Prototype preview

## Summary

Date: 2026-11-10. Operator-approved maintenance release, outside active ART.
Security Landing Unit: `source-editor-composed-security-20261110`,
`child_isolated_landing_unit`. Agent Gary authors source; mfshaf7 is the
accountable reviewer and merger under standing delegation. The main agent
retains Security decision closure and final landing judgment; no independent
external audit is implied.

Extend existing Console, OOS, Studio and governed-model controls. No service,
provider account, storage subsystem or general source executor is introduced.
The existing composed decision remains the activation authority, with its
original architecture and durable orchestration bindings preserved. Exact
source bindings are refreshed only for the reviewed release.

## Exact reviewed sources

- `context-governance-gateway@e29c59a4ed56048f6aa47bb924899566a5e68bae`
- `governance-operations-console@bd6b63bb7d277de46824ac1369473e673c06431d`
- `operator-orchestration-service@9e68d7bb1aee1f94e766fa10784fbddc7726d953`
- `platform-engineering@a815752137438784252f8a19498285f977a36c6a`
- `workspace-governance@02891e37b8abb1cc0eccfbf56fb1812c8f9f2e80`
- `workspace-governance-control-fabric@d3b8ba934275324abcb794c0276fd3dea0a9ceb9`
- `workspace-prototype-studio@07776dbcb13acaf8ad2d39d02c28929dd14f5fe3`
- `platform-engineering-tree@39078e5160e1bf5f64b38a422611c599ea7c37fd`

Studio PR44, OOS PR412, Platform PR379 and Console PR172 are merged.
Console PR173 adds the HTTP-parser correction and standard dialog scrollbar
reviewed below; its exact merged source is the current Console pin.
Exact-head delegated review and required provider checks passed.
No native availability result is inferred from these source merges.

## Scope Delta

### Design intent

Make scoped manual source work usable in Prototype and Delivery, and allow
explicit questions or reviewable AI edit proposals over selected current
buffers. Preserve private saving, exact acceptance, Gary source delivery,
accountable review and owner workflow authority as separate steps. Prototype
may display its already running static app inside the same editor. Delivery
has no runtime binding and gains no invented preview or deployment capability.

### Implemented controls

OOS authenticates the actual source session/caller/operator before reading an
original assistance artifact. The immutable request binds realization revision,
selected baseline digests and a local snapshot. Owner capture verifies clean
source and proven absence for new paths. Scope, unsafe paths, duplicate paths,
text size, file count, total context and conversation bounds are enforced.
Selected unsaved text is explicitly labelled operator input and enters CGG;
missing/truncated context fails closed, without raw model fallback.

The gateway retains existing profile/caller boundaries. The new finite
`source_editor_assistance` task inherits the configured source-generation
route unless explicitly overridden. Registered model, effort and permission
validation remain active. Replies require current profile/task, caller, audit,
selection and timestamp binding. Questions cannot carry edits. Proposals can
change only selected files or owner-proven absent files in the real scope.
The owner rechecks source state after inference. Replies are private artifacts;
they cannot save, accept, commit, execute, approve, publish or activate source.
Original replay checks exact input and caller custody. Browser cancellation
stops waiting without falsely claiming provider cancellation.

The Console reviews diffs before local application and protects later operator
edits against stale proposals and undo. Import/save and new file/folder controls
remain bounded inert source operations. Empty folders use a visible `.gitkeep`.
Tree expansion, search, AI hide/show, grouped panels and view switching do not
grant workflow authority. Internal source metadata stays in existing private
custody and is not automatic model context. Credential-path exclusions do not
claim to be a general secret-content scanner.

The optional Studio `embedding.allowed_origins` defaults to framing denied.
Its maximum eight unique exact HTTP loopback origins require unprivileged
ports and exclude paths, credentials, wildcards, query and fragment. The same
reviewed source-preparation intent carries `embedding_origins`; native plan and
request digests bind it. Profile changes still require reviewed source custody
and normal runtime reconciliation. CSP uses only those exact ancestors; an
opt-in omits conflicting X-Frame-Options. Existing network, form, worker,
object, read-only HTTP, path and source/process identity restrictions remain.

The Console embeds only a confirmed running owner endpoint on a separate
loopback origin with an exact current Console ancestor permission. The iframe
is sandboxed without forms, popups or top navigation, uses no-referrer and
denies camera, microphone, geolocation and clipboard permissions. It does not
proxy app HTML into the Console origin. Preview source revision/digest stays
separate from unapplied private draft identity. Refresh/polling never apply
source or start/restart a process. Stopped, stale, invalid and unavailable
owner state remove the frame while retaining local buffers. Browser frame
load is not an application acceptance claim.

The compact Prototype overview validates a bounded canonical index and
caller-owned current metadata without reading all retained documents. Complete
counts and lifecycle semantics remain independent of register paging. Only a
typed old-owner unsupported-view response permits the explicit legacy read;
authority/read failures never become fixture or partial-success counts.

### Evidence and operating boundary

Studio full `make validate`: 99 tests and owner/registry/runtime/architecture
validators pass. Native HTTP tests prove default framing denial, exact opt-in
headers, source identity, invalid-origin denial and process cleanup.
OOS: 1,958 tests pass with two existing optional Studio-source tests skipped;
API/bundle/governance and fetched-base validators pass. Native API and worker
images build; live API health and fail-closed worker smoke pass without
business writes. Console: 1,061 tests, architecture guards, types, production
build, repository validation and production audit (zero vulnerabilities) pass.
Platform full serial `make validate`, routing inheritance and model-policy
checks pass. Provider checks remain separately bound to the exact PR heads.

Browser review proves both shared editor layouts, compact widths, text/cursor/
undo retention, dirty notice after private save, loading/stale/error/denied/
wrong-project states and unchanged-frame status polling. The explicit isolated
UI sample uses the actual native Studio runtime with simulated source/model
actions; it is not a native Delivery runtime or live model/source proof.
Windows HTTP access was verified for both editor and isolated sample app;
the sample port was selected outside Windows excluded ranges without changing
host forwarding or firewall policy. Review routes are parked outside release
source and are excluded from production.

Normal exact-source Platform activation and native owner/model/preview
readback remain required. This source decision does not predeclare those
results. Earlier accepted source, private drafts, original journals, model
configuration and account custody remain the rollback/recovery boundary.

## Review Areas

### Native qualification correction: assistant HTTP parsing

The first native editor-assistance call exposed an availability defect before
owner/model dispatch: both Console domain routes passed assistance JSON to the
saved-draft validator. Earlier adapter tests bypassed that HTTP-body boundary.
No model invocation, private save or source change occurred from the rejected
request; the temporary authorization was revoked and its unchanged verification
checkout retired.

The reviewed Console repair retains the existing bounded UTF-8 reader and uses
separate closed validators for assistant requests and saved-draft commands.
Both Prototype and Delivery select the assistant parser on assistance routes.
No task contract, profile, provider, caller, authorization, source effect or
data boundary changes. The same owner correction includes the operator-requested
standard Teras scrollbar on scrollable dialog bodies. It changes two CSS
properties without changing dialog size, scroll ownership, content or actions.
The populated four-fallback routing browser check reproduced the default
scrollbar before the fix and passed afterward, retaining the draft guard. Actual domain HTTP-handler regressions cover question
and edit dispatch, separate explicit saving, wrong-command rejection, malformed
UTF-8 and oversized input without unintended owner dispatch. All 1,064 Console
semantic tests, guards, types, build, repository validation and production
dependency audit pass. Native model qualification follows accepted activation;
source and isolated owner tests do not attest provider availability.

Security accepts this corrective delta under the same composed gate and
unchanged architecture, six other source pins, Platform tree and durable
orchestration binding. The exact current Console revision above and in the
paired composed decision is the corrected source; the prior merged PR172
remains release history. This does not grant source actions to the assistant
or introduce a new implementation work item or runtime control.

- identity: existing caller/operator/session and Gary/human roles retained;
- secrets: no new credentials, browser/model credential exposure or account import;
- delivery: exact draft acceptance and reviewed source publication remain separate;
- runtime: bounded explicit ancestor opt-in, source/process proof and unchanged controls;
- AI: governed selected-file context, finite output and no action authority.

Existing review context:
[Source editor/import](2026-10-25-console-source-editor-import.md),
[Prototype runtime execution boundary](2026-10-09-prototype-preview-runtime-execution-boundary.md),
[Composed runtime decision](2026-10-24-configurable-ai-routing.md).

## Decision

Approved for this reviewed public/synthetic, single-operator loopback
maintenance source and its exact composed local activation. Fresh native
readback is required before reporting operating availability. No private
client or hostile-source qualification, general draft execution, Delivery app
hosting, arbitrary toolchain, public ingress, stage/prod release, automatic
source acceptance or autonomous governance is granted.

The next Delivery development-runtime design remains a separate discussion;
this release provides applied-source Prototype viewing only. No unresolved
implementation finding requires another control plane or ART repair item.
