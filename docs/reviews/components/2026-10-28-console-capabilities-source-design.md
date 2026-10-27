# Console Capabilities: Bounded Source-Design Review

## Summary

- date: 2026-10-28
- decision: `approved`
- initiative: `openproject://work_packages/1332`
- source-design story: `openproject://work_packages/1342`
- final exact-composition review: `openproject://work_packages/1345`
- affected owners: Governance Operations Console, Operator Orchestration Service
  (OOS), Platform Engineering, and Security Architecture
- architecture: `architecture-packet:delivery-1332-v1`, schema 6,
  `sha256:afa065834ed8bfff220c465def360522e45379cec1c42a051e372cac76594649`

This decision approves the bounded source changes and commissioning design below.
It does not activate Temporal, authorize a durable run, change a model profile,
or assert that any of the three capabilities is operational. Existing accepted
runtime authority remains separate and unchanged.

## Scope Delta

### Reviewed source and existing controls

The review inspected these owner baselines:

| Owner | Revision | Relevant authority |
| --- | --- | --- |
| OOS | `198c54405b7a1c3f0741b8521469540884b0ea8e` | Existing profile-request lifecycle, durable-run admission, and launcher |
| Platform | `25ab9f3862b3c7b3b455188f90b6223f0d4ea9a9` | Existing runtime composition, atomic observation collector, model registry, and activation evidence |
| Console | `7aa73d070bb0dc369f4f7e772c8f232a6585c133` | Current registry and request-specific history adapters, explicit review surface, and original source-command recovery |
| Security | `642ead187a33b07434baa8b05bada51eb5953f0f` | Existing finite runtime acceptance, durable source admission, and trust boundaries |

OOS currently hardcodes the accepted-idea-delivery runtime and execution switches
off, leaves activation evidence empty, and declares zero orchestration-worker
replicas. Its launcher does not forward the existing model-profile request
configuration. Source extension in OOS is therefore necessary; a downstream
Platform override cannot replace that owner change.

The existing OOS services, Platform collector, Temporal workflow, and WGCF
read-only activity are reused. This review introduces no new controller,
permission model, source-authoring service, or execution definition. Source tests
and historical commissioning records are not current operating evidence.

### Approved implementation intent

1. OOS story 1343 may extend its launcher to forward the existing bounded
   model-profile bindings and conditionally configure the existing durable API
   and worker from exact accepted activation evidence. Missing, invalid, expired,
   or mismatched admission must preserve the existing execution denial. Merely
   setting an environment switch must not authorize execution.
2. Platform stories 1338, 1340, and 1344 share one composition and rollback unit.
   They may wire the existing profile-request roles, publish current registry and
   request-specific evidence, refresh bounded health observations independently
   of credential renewal, and compose the admitted durable runtime and WGCF
   activity using the existing exact-bundle controls.
3. Final review 1345 must inspect merged Console/OOS revisions and the exact
   validated, unmerged Platform candidate tree with CI evidence. Platform merge
   and activation must preserve that accepted tree. Authoring a candidate is
   allowed before final review; merging or activating it is not.
4. Native operating stories 1339, 1341, and 1346 must prove the actual lifecycle,
   health expiry/recovery, and original-run durable continuity. They remain
   separate from source completion and from this decision.

### Identity and decision boundaries

- The authenticated Console caller retains its configured accountable operator.
  The same bound operator may submit and explicitly review a caller-owned model
  profile request. The existing service contract does not require a second human
  reviewer account. A model never supplies the final review decision.
- Platform fulfillment uses a separately admitted caller, without operator
  impersonation. It consumes the approved request revision and supplies exact
  source and owner receipt evidence; OOS coordination does not itself change the
  authoritative registry.
- Durable business runs admit only the existing authenticated Console caller.
  Temporal receives no Console, OpenProject, Security, or general backend
  credential. API and workflow-worker process identities remain distinct; WGCF
  retains its separate activity-owner identity and read-only validation scope.
- The initial definition remains `validation-readiness-run` version 1. This is
  not admission for arbitrary commands, source mutation, host control, or other
  definitions. Agent Gary's existing bounded source-authoring path and delegated
  human review remain separate from model and workflow authority.
- Existing model choices, effort settings, six-purpose baseline, and account
  custody remain unchanged. No Desktop or CLI account credential is imported.

### Evidence and recovery boundaries

Current model registry readiness must not require an unrelated completed request.
Historical completion must bind that original request, explicit review,
distinct Platform fulfillment, exact merged source, and matching owner receipts.
A later registry change must not rewrite or invalidate a legitimately completed
earlier request. Private request-history files remain owner-selected, bounded,
same-UID, nonsymlink artifacts; browser input cannot select a filesystem path.
Missing, corrupt, cross-request, or forged evidence cannot become success.

Health publication reuses the existing collector and atomic artifact boundary.
It must prevent overlapping collection, publish the six admitted components
honestly, expire at the actual 120-second deadline, and identify other components
as unobserved. Collector failure or unavailable publication cannot extend old
healthy observations indefinitely. No private endpoint or credential enters the
browser-safe projection.

Normal restart under a still-valid activation preserves the original bundle,
generation queue, run identity, and history. Reactivation, suspension, or changed
authority uses the existing generation-fencing and retirement procedure. Lost
acknowledgement requires reading and reconciling the original command or run;
it does not authorize a duplicate effect. Bounded retry and cancellation retain
their existing immutable bindings and complete owner receipts.

Workflow payloads and durable history remain reference-oriented and bounded.
Secret values, raw operational context, unbounded logs, source text, and model
credentials do not become workflow history. Existing private persistence,
retention, backup/restore custody, and network boundaries still apply.

## Review Areas

| Area | Judgment |
| --- | --- |
| Identity | Reuse caller/operator binding, distinct fulfillment, and separate API/workflow/activity identities. No additional human identity requirement. |
| Secrets | Preserve server-only custody, private evidence roots and least-privilege worker credentials. No new credential-import boundary. |
| Delivery | Source design is approved; final exact-candidate acceptance remains a pre-merge gate. Preserve independent owner rollback and source evidence. |
| Runtime | Source activation remains conditional on the existing exact digest-bound evidence and lifecycle authority. Source review is not operating permission. |
| AI | Assistance may draft requested content; models do not approve requests, activate execution, or replace owner acceptance. |

## Decision

`approved` for the bounded source-design scope only.

This review satisfies `gate:1332-bounded-source-design` before OOS implementation
and supplies the design-intent part of `gate:1332-source-activation-chain`.
The latter remains incomplete until the OOS source change and final exact
composition review are complete. It cannot be replayed as runtime permission.

The main Security authority retains final judgment under story 1345. Positive
source conformance must show the role split, exact evidence chain, bounded
read-only activity, recovery, and rollback described here. Negative conformance
must reject absent or mismatched authority, changed source or worker bytes,
wrong caller or request, and automatic decisions without explicit operator
review. A retired controlled-proof permit grants no authority to this work.

Operating stories must retain real owner and aggregate receipts and restore the
agreed model baseline after their controlled exercise. Deliberate hardware
corruption, stage/production qualification, and arbitrary project execution are
outside this decision. Existing accepted source must remain available to runtime
refresh while newer source is staged; remove temporary source bindings after
normal exact-composition commissioning and prove the ordinary refresh path.

## Related Artifacts

- [OOS durable source admission](2026-08-01-operator-orchestration-service-durable-orchestration-source-admission.md)
- [Temporal build admission](2026-07-31-temporal-durable-orchestration-build-admission.md)
- [Existing finite composed acceptance](2026-10-24-configurable-ai-routing.md)
- [Security delta review process](../security-delta-review-process.md)
- [OOS profile-request procedure](https://github.com/mfshaf7/operator-orchestration-service/blob/198c54405b7a1c3f0741b8521469540884b0ea8e/docs/operations/model-profile-request-operator-surface.md)
- [OOS durable contract](https://github.com/mfshaf7/operator-orchestration-service/blob/198c54405b7a1c3f0741b8521469540884b0ea8e/docs/contracts/durable-orchestration-v1.md)
- [OOS launcher](https://github.com/mfshaf7/operator-orchestration-service/blob/198c54405b7a1c3f0741b8521469540884b0ea8e/dev-integration/profiles/accepted-idea-delivery/scripts/up.sh)
