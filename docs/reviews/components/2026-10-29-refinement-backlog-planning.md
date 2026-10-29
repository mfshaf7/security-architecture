# Refinement backlog planning security review

## Summary

- Date: 2026-10-29.
- Decision: `approved` for the exact reviewed source and existing local lane.
- Classification: operator-approved maintenance; no ART repair child.
- Primary owner: Operator Orchestration Service.
- Activation authority: [existing finite decision](2026-10-24-configurable-ai-routing.yaml).

Review the existing Refinement field-projection and accepted-planning correction.
It introduces no identity, credential, endpoint, database, model authority,
installer or runtime capability. The existing Console v1 parser and editor are
reused. Source acceptance remains distinct from native operating qualification.

## Scope Delta

Gary candidate `89633fb25cbfca0a9eb5908a6e05c17c1643e8d7` is reviewed in
[OOS PR393](https://github.com/mfshaf7/operator-orchestration-service/pull/393).
It merged as `9f19e978a688cacbd3e187dc5401adc3a4563226`; candidate/merge tree
equality is proven and the paired decision selects that exact merged source. Console and other source selections, the Platform tree,
durable activation manifest, generation and WGCF worker digest remain unchanged.

The packet uses existing native type/status planning rules. Required committed
and active planning fields remain separate from optional valid backlog planning
in existing v1 target groups. Separating the groups preserves the current
Console shared-selection editor's requiredness semantics. Packet revision binds
the field groups as well as their values and source state.

Accepted PI/Iteration pairs use the native validator when both reviewed mutable
properties exist. Populated read-only counterparts are not invented as blanks;
native authority still validates their effective state. Optional empty or
whitespace-only planning input retains its reviewed value. A concurrent change
to that retained value causes a conflict before planning writes; final readback
also verifies it before receipt issuance.

## Review Areas

### Identity, secrets and operation scope

Caller/operator binding, immutable acceptance, current source/packet binding,
server-only credentials and existing writable/form constraints are preserved.
No provider or raw OpenProject credential is exposed to Console or models.
The repair derives requiredness from the current canonical rules instead of
making PI universally optional. Active and structurally PI-required work,
iteration alignment, native hierarchy/leaf rules and genuine human acceptance
remain enforced.

### Delivery, runtime and evidence

Existing coordinated plan/apply receives only reviewed planning targets and
retains native parent/type/subject identity, current status and classification.
Other metadata requirements are unchanged. Unreviewed read-only and historical
state is preserved. Accepted planning pairs fail before starting a durable run
when invalid. Unavailable owners, stale scope, conflicting replay and incomplete
readback remain non-success outcomes; identical recovery retains its run and
receipt identity. There is no new release or deployment authority.

### Validation and qualification limits

Exact candidate source passed1,690tests with two existing skips. The53focused
Refinement tests include mixed backlog/committed projection, active and typed
requirements, accepted pair rejection, native form handling, retained-value
replay, whitespace and concurrent-change/readback rejection. Workflow bundles,
API/docs checks, fetched-base owner gates and exact API/worker image smoke passed.

Actual candidate projection was checked through the accepted Console parser and
individual/shared selection models, with unique draft keys and safe mixed
requiredness. That probe uses captured canonical shape and a synthetic handoff;
it is structural source evidence, not a live owner receipt. Hosted exact-head
checks and normal accepted-source commissioning precede final operating proof.
Native Console verification must confirm the served source and repaired planning
fields. Preserve the operator's deferred ART scope and report the actual limits
of any non-mutating proof; do not invent a completed apply receipt.

## Decision

`approved` for the exact reviewed source within existing local dev-integration.
The main security reviewer retains security closure; no delegated worker grants
trust acceptance. Normal paired acceptance and Platform commissioning remain
mandatory. Rollback restores the prior accepted source/decision through the
existing lifecycle while preserving business records, accepted inputs and history.
