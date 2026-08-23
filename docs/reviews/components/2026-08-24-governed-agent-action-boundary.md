# Governed Agent Action Boundary

## Summary

- date: 2026-08-24
- owner repos:
  - `workspace-governance`
  - `workspace-governance-control-fabric`
  - `operator-orchestration-service`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
  - `repos.operator-orchestration-service`
  - `components.workspace-governance-control-fabric`
  - `components.operator-orchestration-service`
- review trigger: `governed-agent-action-authority-boundary`
- ART initiative: `openproject://work_packages/882`
- source feature: `openproject://work_packages/906`
- security review: `openproject://work_packages/955`
- decision: `approved-with-findings`

This review accepts the inactive source foundation for governed agent actions.
It does not activate Console mutation, shared runtime access, canonical backend
mutation, direct model-provider access, stage execution, or production
execution.

The accepted boundary keeps authority with an accountable operator and the
domain owner. A logical agent identity supplies attribution only. WGCF evaluates
current policy, OOS enforces the resulting decision immediately before owner
dispatch, and the domain owner remains the only component allowed to mutate its
canonical backend.

## Scope Delta

### Design Intent

The source foundation introduces four action classes with different authority:

| Action | Canonical mutation | Model use | Operator approval | Required terminal evidence |
| --- | --- | --- | --- | --- |
| `read` | denied | optional | not required | OOS action receipt |
| `advise` | denied | required | not required | context packet and OOS action receipt |
| `draft` | denied | required | accepted output only | context packet and OOS action receipt |
| `mutate` | owner-controlled only | optional | exact approval required | owner receipt and OOS action receipt |

Authority is derived from the authenticated caller, operator delegation,
admitted workflow, action class, exact target, source version, current policy
decision, and exact approval for mutation. It is never derived from agent
identity, model output, a stale decision, or possession of a request envelope.

### Implemented Control

The reviewed source provides:

- a Workspace Governance authority contract and schemas for requests, policy
  decisions, action receipts, and owner receipts;
- a WGCF evaluator that validates current bindings and emits bounded
  `allow` or `deny` decisions;
- an OOS enforcement boundary that refreshes current authority immediately
  before dispatch and rejects caller, target, source, approval, expiry, replay,
  and obligation mismatches;
- digest-bound references instead of raw context, raw model output, or secret
  material in authority envelopes;
- exact owner receipts when a mutation owner is invoked and terminal OOS
  receipts for admitted outcomes;
- source-level negative cases proving fail-closed behavior for mismatched or
  replayed authority; and
- an explicit `runtime_activation.enabled: false` contract state.

The implementation does not expose a generic client-selected dispatch target,
grant an agent backend credentials, or permit direct model-to-owner mutation.

### Source And Evidence Binding

The review is bound to these exact source revisions:

| Repository | Revision |
| --- | --- |
| `workspace-governance` | `c698bec7dcd4d4c38f957c4ee2a66b742dabc634` |
| `workspace-governance-control-fabric` | `8b83ba7a2fc0dbbe52ed2892e1b190d2ce0e5de9` |
| `operator-orchestration-service` | `61c037fdd5368863681f6582970bc7f976d40b22` |
| `security-architecture` review base | `e07c2c4c2137b8029d4476746b83e17b111dcfbd` |

Accepted evidence:

- Workspace authority contract digest:
  `sha256:8ed8aee6b03e42d02d5621e650d4488ee3a043e55b38cbd9e4018e4b9bf8d0c3`
- conformance contract digest:
  `sha256:a7f5734c1036865dec69c18153fa3f56562aea140a989ed962dc813bea0a557c`
- generated conformance JSON digest:
  `sha256:f4d297875705a4889c9067ccfd0971430c9737552994fc3c7437efefc1f53a47`
- generated conformance report digest:
  `sha256:3172d1dac51a8454d8c20bbf52c1b7f6598ef11c516cd00b8e8293c64015a099`
- integrated result: `11/11` scenarios passed, comprising four positive and
  seven negative scenarios;
- Security Architecture PR #129 is the review and merge path; its exact-head
  `validate-security-evidence` result is required by Review Packet readiness;
- the mutation adapter used by conformance is synthetic; no canonical backend
  was mutated.

### Operating Evidence

Operating evidence is absent by design. No shared agent runtime, authenticated
Console caller, live owner adapter, canonical backend mutation, secret delivery,
stage execution, or production execution is claimed by this review.

The conformance result proves source compatibility and fail-closed control
behavior. It is not live owner-backend or runtime-operability evidence.

## Threat Model

The reviewed boundary addresses these primary threats:

- logical agent identity being mistaken for authorization;
- model output being treated as operator approval;
- stale or replayed policy decisions authorizing a later action;
- caller, target, source-version, or context substitution between evaluation
  and dispatch;
- an OOS workflow bypassing the canonical WGCF decision boundary;
- mutation outside the domain owner's executor;
- success being returned without required owner and terminal receipts; and
- raw context, model output, or secret material leaking into durable authority
  evidence.

The source controls materially reduce these risks while activation remains
disabled.

## Review Areas

### Identity

The identity split is acceptable at source level: the operator is accountable,
the caller is authenticated, the agent is attributed, the model invocation is
attributed, and the backend executor remains owner-controlled. Activation must
prove real caller, operator, OOS, WGCF, and owner-executor identities without
collapsing them into a shared credential.

### Secrets

The contracts prohibit secret material in references and authority receipts.
No runtime secret path is introduced or approved. Any activated workflow must
receive credentials through the existing owner and platform secret-delivery
boundaries and must prove redaction in logs and receipts.

### Delivery

The reviewed revisions are source evidence only. Merge, conformance, or this
review cannot independently activate an agent workflow. Any future activation
must bind exact deployed revisions, admitted workflow ids, owner adapters,
policy profiles, identities, and rollback evidence.

### Runtime

Runtime activation is explicitly disabled. No shared listener, worker,
canonical owner adapter, stage path, or production path is accepted here. A
fresh runtime delta review is required before enabling any of them.

### AI

Model output remains advisory or draft content and cannot become authority.
`mutate` requires exact operator approval even when a model participated.
Direct provider access and direct model-to-owner mutation remain denied.

## Findings

### Post-mutation receipt failure leaves an ambiguous reconciliation state

The negative conformance cases correctly avoid returning success after owner
mutation when audit or receipt storage fails. However, the
`mutate-receipt-store-failure` case proves that an owner mutation may already
have occurred while the caller receives neither a terminal OOS receipt nor a
returned owner receipt. The current source therefore cannot prove a durable,
operator-visible reconciliation path for that post-owner failure.

This is an activation-blocking finding, not an accepted live defect: the
reviewed runtime is inactive and the conformance owner is synthetic.

Before any canonical owner mutation is activated, OOS and the owner adapter
must prove one durable reconciliation design that:

1. preserves or reconstructs the owner result after owner invocation;
2. emits an immutable terminal action outcome without falsely returning
   success;
3. supports idempotent operator retry or explicit manual reconciliation; and
4. demonstrates the behavior against the exact live owner adapter in the fresh
   activation review.

Owner: `operator-orchestration-service` with the activating domain owner.
Closure condition: this proof is required before any workflow containing the
`mutate` action class can become active.

## Decision

`approved-with-findings`

Approved:

- the Workspace Governance action authority contract and schemas;
- the WGCF source-level policy evaluator;
- the OOS source-level enforcement boundary;
- the inactive synthetic conformance suite and its `11/11` result;
- continued local development and review while runtime activation remains
  disabled.

Not approved:

- Console-originated mutation;
- shared agent-action runtime exposure;
- canonical backend mutation;
- activation of a workflow containing `mutate` before durable reconciliation
  is proven;
- direct model-provider or owner-backend access;
- stage or production execution; or
- reuse of this source review as future runtime acceptance.

Any activation proposal requires a fresh Security delta review bound to exact
deployed source, real identities, admitted workflows, owner adapters, secret
paths, runtime controls, and operating evidence. The finding above must be
closed for mutation-capable workflows or those workflows must remain excluded.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [AI security and governance standard](../../standards/ai-security-and-governance.md)
- [OOS agent-action decision enforcement](https://github.com/mfshaf7/operator-orchestration-service/blob/main/docs/records/change-records/2026-08-23-agent-action-decision-enforcement.md)
- [Workspace Governance action authority](https://github.com/mfshaf7/workspace-governance/blob/main/docs/agent-action-authority.md)
