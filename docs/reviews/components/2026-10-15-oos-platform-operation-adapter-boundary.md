# OOS Platform Operation Adapter Security Delta

## Summary

- date: 2026-10-15
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1275`
- security acceptance item: `openproject://work_packages/1302`
- reviewed owner repo: `operator-orchestration-service`
- reviewed pull request:
  [operator-orchestration-service #336](https://github.com/mfshaf7/operator-orchestration-service/pull/336)
- reviewed exact revision:
  `operator-orchestration-service@de0c80ae7e8b0adb69fe53c06d87ee83ac13083b`
- reviewed tree: `16d788ce07a590a747d14d01cf3c249fdbe6ec21`
- architecture packet: `architecture-packet:delivery-1275-v1`
- architecture packet digest:
  `sha256:ea428f9ad9a14368aa9f789be278d3aac44def2cb2a4bc31caec7768f03335bb`
- decision: `approved`

Security approves only the exact reviewed OOS revision for merge as the bounded
Platform-operation adapter. This decision does not deploy the Platform owner
routes, activate the adapter, approve stage or production operation, authorize
an arbitrary Platform command, or replace the exact-head human review and
protected merge requirement.

The initial review found two pre-merge gaps: a downstream owner error body
could be persisted and returned to the Console, and denial, replay, and
readback-driven state transitions did not all reach the mutation audit
boundary. The reviewed revision maps downstream failures to bounded OOS-owned
messages and emits secret-free audit events for denial, accepted dispatch,
replay, reconciliation, blocked reconciliation, retry, and cancellation. No
open finding remains from this review.

## Scope Delta

### Design Intent

The Governance Operations Console will use OOS as its only workflow seam for
the Dev Integration and Governed Releases workspaces. OOS admits exact
operator-approved commands against current Platform capability truth, retains
durable coordination state, and publishes exact next actions. Platform remains
the authority for capability availability and every platform effect.

The boundary preserves these role separations:

- the Console presents intent and current readback but has no direct Platform
  credential or generic execution path;
- OOS owns caller/operator binding, command admission, durable idempotency,
  retry/cancel coordination, recovery, safe projection, and workflow audit;
- Platform owns the finite capability catalog, effect execution, owner state,
  and terminal receipts;
- Security accepts the exact source boundary but does not implement or operate
  the adapter;
- the human reviewer remains the only PR approver and merger.

### Implemented Control

The reviewed delta from OOS `main` at
`8aef131aafa9a8f3ddc43c89b6b3bd4a0fce5819` through `de0c80a` adds:

- a finite allowlist of dev-integration and governed-release actions rather
  than a generic proxy, shell, URL, method, or header surface;
- exact command, subject, capability, source-version, canonical intent digest,
  operator approval, and caller/operator binding;
- a disabled-by-default runtime admitted only in the `dev-integration` profile
  with an exact Security decision URI, digest, and reviewed OOS revision;
- current Platform catalog admission and denial of stale, missing,
  unavailable, mismatched, or non-approval-bearing capabilities;
- atomic mode-`0600` command and idempotency state with per-command writer
  exclusion and immutable intent conflict detection;
- persist-before-dispatch behavior for both commands and controls;
- restart reconciliation by immutable command identity without command
  resubmission;
- exact retry and cancel controls, including retained unknown outcomes and
  replay only under the original control idempotency binding;
- HTTPS-by-default owner access, an explicit loopback or cluster-local HTTP
  exception for dev-integration, server-held caller credentials, redirect
  denial, a 15-second timeout, and a 512-KiB response limit;
- exact allowlisted owner catalog and operation projections with identity,
  state-event, blocker, failure, and terminal-receipt validation;
- bounded OOS-owned error projection that does not copy downstream error
  bodies into durable state, audit, or Console responses;
- secret-free mutation audit for dispatch, denial, replay, reconciliation,
  blocked reconciliation, retry, cancellation, and receipt reference; and
- one operator surface and an OpenAPI projection matching all implemented OOS
  routes.

### Operating Evidence

This is a pre-merge source decision. Runtime operation is intentionally not
claimed. Against exact OOS head `de0c80a`:

- the full serial owner suite passed 1,325 tests with two intentional skips and
  zero failures;
- focused operation, configuration, and HTTP tests passed 114 tests with zero
  failures;
- tests covered success, denial, stale capability truth, caller
  impersonation, replay conflict, process-loss recovery, retry, cancel,
  unknown control outcome, safe provider error projection, and audit coverage;
- API validation matched all 176 documented and implemented routes;
- governance documentation, source-backed change-record, OpenProject mutation
  contract, and whitespace validations passed; and
- the GitHub `validate-governance-docs` check completed successfully on the
  exact reviewed head.

Platform owner implementation, runtime composition, Console controls, and the
fixture-free journey remain later separately owned acceptance steps. Their
absence is safe at this gate because the reviewed runtime cannot activate
without explicit dev-integration, provider, identity, secret, and exact
Security-decision configuration.

## Review Areas

### Identity And Approval

The OOS caller id is authenticated by the existing OOS boundary and maps to one
configured operator identity. Each command binds that same operator to the
canonical digest of the exact command intent. Retry and cancel carry the same
operator binding and their own immutable idempotency identities. Provider
credentials remain server-held and do not appear in commands, state, audit, or
responses.

The configured shared-secret transport remains acceptable only for the bounded
dev-integration composition in this decision. Platform commissioning must keep
the credential scoped to the OOS-to-Platform owner route and deliver it through
the existing secret authority; this review does not approve a browser-held,
source-stored, cross-service, stage, or production credential.

### Command And Effect Boundary

The action vocabulary is closed and versioned. Platform capability truth must
name the exact subject, source version, capability, and action before OOS
dispatches. Command input cannot supply a destination, HTTP method, header,
credential, executable, or generic operation name. Platform owns actual
effects and terminal receipts, so an OOS state transition alone cannot prove a
platform change.

### Denial And Disclosure

Unconfigured runtime, non-dev-integration profile, missing Security decision,
unbound caller, operator mismatch, malformed intent, stale source, missing or
unavailable capability, provider identity mismatch, invalid projection,
oversized response, redirect, external plain-HTTP destination, and conflicting
replay all fail closed. Provider error bodies are consumed only to enforce the
response-size and JSON boundary; OOS returns its own bounded error message.
Raw logs and command input are absent from audit and public projection.

### Recovery, Replay, And Rollback

OOS persists command and control intent before owner dispatch. A lost submit
response becomes blocked and reconciles by immutable command id. A lost control
response retains an unknown outcome and may be retried only with the same
control idempotency key, relying on the Platform owner contract to honor that
same key. Terminal owner receipts are retained and read without creating a new
effect.

Rollback is source and composition based: revert the OOS Landing Unit and keep
the feature disabled, or remove the later Platform composition binding. State
files must not be deleted to manufacture success; corrupt state remains a
fail-closed condition for investigation.

### Audit And Operating Visibility

OOS records bounded identifiers, state, outcome, error code, and receipt
reference for mutation and recovery transitions without downstream error
content or credentials. The Console receives explicit `next_action` authority
and reason. This is implemented source control, not operating proof; #1291,
#1292, and #1298 must still prove the deployed revision, owner availability,
restart behavior, and fixture-free Console journey.

### Residual Risk And Activation Boundary

The later Platform owner must implement idempotency for control replay and
serve projections that satisfy this exact contract. A compromised admitted OOS
caller credential could submit actions as its one configured operator, so
credential delivery, rotation, and namespace isolation remain part of the
Platform commissioning and Security operating-boundary review. These are
explicit downstream gates, not open findings against this disabled source.

## Decision

`approved`

OOS revision `de0c80ae7e8b0adb69fe53c06d87ee83ac13083b` may proceed to
exact-head human review and protected merge. Approval is invalid for any later
OOS head unless a fresh Security delta accepts it. Runtime activation remains
denied until Platform #1291 implements the owner protocol and Security #1303
accepts the exact composed operating boundary.
