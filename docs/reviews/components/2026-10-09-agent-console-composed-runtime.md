# Agent Console Composed-Runtime Security Delta

## Summary

- date: 2026-10-09
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1203`
- parent feature: `openproject://work_packages/1215`
- security review item: `openproject://work_packages/1248`
- governing gate: `gate:agent-console-operating-acceptance`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/3a4b5edb6bc54ff47a45f610b41f75bc57dd9d1ab56e9475518100d75ff72ab0`
- reviewed source:
  - Context Governance Gateway implementation merge:
    `context-governance-gateway@7f9ca084cc1e41f360d3d27eb780ddebf11d2772`
  - Context Governance Gateway current runtime-hook revision:
    `context-governance-gateway@094c10a0df39bf0733ee02e3cb567f571cdf661f`
  - Operator Orchestration Service implementation merge:
    `operator-orchestration-service@015c74422901425892cf62cd46ab2f3a9f79c71a`
  - Operator Orchestration Service current reviewed revision:
    `operator-orchestration-service@e8b46ffbd9a11f5d0b4f037ca7ff1806991950a8`
  - Platform Engineering Agent Console admission merge:
    `platform-engineering@e780c33ecb64d7fc317121165aba8e8154518e3d`
  - Platform Engineering current reviewed revision:
    `platform-engineering@d9796f6db70d5c68012be0212ca3c4050f54794e`
  - Governance Operations Console integration merge:
    `governance-operations-console@585850a53ef6c348f4f297468f1ccdb487b5a6c9`
  - Workspace Governance composition-binding merge:
    `workspace-governance@20ffe1a2d3530b370c116ea0f54cef5c47b7afa4`
- source review:
  - [CGG context projection PR #23](https://github.com/mfshaf7/context-governance-gateway/pull/23)
  - [CGG runtime hook PR #24](https://github.com/mfshaf7/context-governance-gateway/pull/24)
  - [OOS orchestration PR #297](https://github.com/mfshaf7/operator-orchestration-service/pull/297)
  - [OOS runtime hook PR #298](https://github.com/mfshaf7/operator-orchestration-service/pull/298)
  - [OOS closeout regression repair PR #300](https://github.com/mfshaf7/operator-orchestration-service/pull/300)
  - [OOS failed-evidence retry repair PR #301](https://github.com/mfshaf7/operator-orchestration-service/pull/301)
  - [OOS invalid-evidence lifecycle retry completion PR #302](https://github.com/mfshaf7/operator-orchestration-service/pull/302)
  - [Platform admission PR #280](https://github.com/mfshaf7/platform-engineering/pull/280)
  - [Platform verifier cleanup PR #282](https://github.com/mfshaf7/platform-engineering/pull/282)
  - [Platform Ollama runtime reconciliation PR #283](https://github.com/mfshaf7/platform-engineering/pull/283)
  - [Console governed integration PR #61](https://github.com/mfshaf7/governance-operations-console/pull/61)
  - [Workspace composition correction PR #253](https://github.com/mfshaf7/workspace-governance/pull/253)
- decision: `approved`

The exact revisions are approved for the existing single-operator,
loopback-only `refinement-catalog` composition in local `dev-integration` and
for the bounded operating proof owned by Platform work item `#1246`. This
decision does not itself claim that operating proof has passed. Platform must
still run the exact positive and negative verifier, close its synthetic
session, retain the private receipt, and complete the Delivery ART evidence
sequence before the Feature is operating-ready.

## Scope Delta

### Design Intent

- replace the Console's direct local-provider path with one governed path
  through OOS, CGG, and the governed AI gateway;
- admit only Focus and Workspace context candidates, with manual operator
  prompts and no raw-context fallback;
- preserve exact operator, caller, agent, session, invocation, candidate,
  profile, audit, receipt, and source-revision bindings;
- keep model output suggestion-only and separate from Agent Action or owner
  mutation authority; and
- reuse `refinement-catalog` rather than create another runtime, composition,
  gateway, credential path, or control plane.

### Implemented Control

CGG authenticates the exact OOS caller, verifies the candidate digest and
scope, applies redaction and budget limits, retains raw candidate content only
inside CGG custody, and returns model-safe content plus packet, redaction,
projection, and artifact evidence. Its Agent Console hook accepts credentials
only from `refinement-catalog`; disabled, partial, standalone, and teardown
states remove the credential and fail closed.

OOS authenticates the Console machine caller and binds it to the exact local
operator. It durably reserves one invocation before upstream calls, verifies
the full CGG result, sends only the model-safe projection and manual prompt to
the exact governed profile, verifies the gateway response and audit binding,
and records a terminal digest-bound invocation receipt. Replay conflicts,
stale revisions, malformed evidence, caller or operator mismatch, upstream
failure, and concurrent invocation fail closed. The action route has no
admitted owner adapter in this composition and returns unavailable rather than
dispatching a mutation.

Platform admits only caller
`operator-orchestration-service/agent-console`, profile
`agent-console-assistant-v1`, task `assistant_response`, contract
`oos.agent-console.interaction.v1` version `1.0`, and the strict `{text}`
response schema. The selected binding is local Ollama `qwen3:8b` in
`dev-integration`; direct consumer-to-provider access remains prohibited. The
existing composition now projects one CGG endpoint, exact caller identity, one
runtime-generated composition-lifetime credential, and paired OOS and CGG
activation flags. No secret value is stored in Git or composition state.

The Console uses only its same-origin server route and server-only OOS
credential. It accepts a response only when operator, caller, session, agent,
mode, invocation, profile, CGG artifact, gateway audit, and OOS receipt
evidence match. Reset and mode change close the exact OOS session revision
before rotating the browser nonce. The direct Ollama adapter and fallback are
removed. Manual interaction neither constructs nor dispatches an Agent Action.

### Operating Evidence

The owner Landing Units passed their focused protocol suites, repository
validators, exact-head CI, human review, protected merge, and finalized source
evidence. CGG proves authenticated redaction-safe projection, digest and scope
denials, bounded replay, and receipt custody. OOS proves ordered completion,
caller/operator and session binding, CGG and model response verification,
terminal failure settlement, replay conflict, action unavailability, exact
close, and restart-safe durable state. Console proves same-origin session
authorization, server-only credentials, exact response evidence, fail-closed
partial configuration, and exact-session cleanup. Platform proves the closed
profile, caller, task, schema, revision-set, and Security-gate policy.

The active composition was observed without the Agent Console projections
before Workspace Governance PR #253, so both owner hooks remained correctly
disabled. The correction adds the complete existing-composition binding and
exact regression assertions; it does not add a new route or authority. Live
positive invocation, wrong-caller denial, gateway audit readback, exact session
close, and private receipt creation remain intentionally pending until this
decision lands. Source evidence must not be represented as that operating
proof.

## Review Areas

### Identity And Authorization

The browser session principal, Console machine caller, OOS-bound operator, OOS
Agent Console workflow caller, CGG caller, governed-gateway caller, Security
reviewer, and human source reviewer remain distinct bindings. The Console
cannot assert the OOS caller or operator, and OOS cannot select a different
gateway caller or profile. No machine identity can approve or merge its own
source change.

This remains acceptable only for the existing single-operator local lane.
Trusted human identity is still absent, so shared or multi-user exposure is
not approved.

### Secrets And Data

Console-to-OOS and OOS-to-CGG credentials are runtime-only and server-side.
The CGG credential is generated for one composition lifetime and projected to
only the two declared profiles. Provider credentials are not projected to the
Console, OOS, or CGG; the selected local Ollama binding requires none. Secret
values must not enter source, browser payloads, receipts, audit metadata, or
composition state.

Only the redacted, budgeted CGG projection and a manual operator prompt may
reach the model. Raw context fallback, real client data, secrets in prompts,
and uncontrolled workspace capture are not approved.

### Delivery, Replay, And Evidence Integrity

Every reviewed owner revision is exact. The Platform verifier requires all
five current revisions to appear in this review before it can run. Session and
invocation idempotency bind canonical request content; conflicting reuse is
denied. Success requires complete CGG receipts and artifact digest, the exact
model profile, a gateway audit reference, and the OOS terminal receipt. Source
review, Security approval, and live proof remain separate stages.

The later Platform auto-resume repair at
`platform-engineering@5e712eb75896db20a49b15a69452046833a798db`
changes composition recovery and retry bounding, not the Agent Console caller,
profile, data, credential, or action boundary. The later OOS documentation head
and Workspace Governance composition correction likewise narrow operating
truth without expanding the accepted path.

The OOS invalid-evidence lifecycle retry completion at
`operator-orchestration-service@e8b46ffbd9a11f5d0b4f037ca7ff1806991950a8`
routes a failed post-merge operating check back through the same exact-source,
exact-profile bounded acquisition after its reported cause is repaired. It
adds no caller, credential, command, source mutation, approval, merge,
readiness, closeout, model, context, or action authority; failed results remain
ineligible for durable replay and only a fully passing receipt may advance.

The Platform runtime reconciliation accepts host Ollama 0.40.1 only with the
unchanged full `qwen3:8b` digest after a synthetic Agent Console invocation
returned strict-schema-valid output. It does not change provider, model,
caller, data scope, credential custody, network exposure, or action authority.

### Runtime And Failure Integrity

OOS and CGG activation are default-off and valid only under the registered
composition. Missing, partial, foreign-composition, malformed, stale, or
torn-down bindings fail closed and remove their dedicated Secrets. The gateway
profile is fixed to local `dev-integration`; stage, production, paid-provider,
remote, and direct-provider routes are excluded.

The Platform verifier uses temporary loopback port-forwards, synthetic context,
the private Console caller credential, an explicitly unauthorized negative
caller, gateway audit readback, and exact session closure. Its receipt is
owner-private and contains source revisions and bounded outcomes, not secrets
or raw model context.

### AI And Action Authority

The model produces text under a strict response schema. It does not choose the
profile, provider, caller, context source, action, approval, or owner workflow.
The task instruction explicitly prohibits authorization or workspace mutation.
Agent Action remains a separate canonical request and policy path and is not
activated by this decision. Human review is the manually initiated prompt and
source-review boundary; model output is advisory only.

## Decision

`approved`

Security emits `gate:agent-console-operating-acceptance` for activation and
operating proof against exactly:

- `context-governance-gateway@094c10a0df39bf0733ee02e3cb567f571cdf661f`;
- `operator-orchestration-service@e8b46ffbd9a11f5d0b4f037ca7ff1806991950a8`;
- `platform-engineering@d9796f6db70d5c68012be0212ca3c4050f54794e`;
- `governance-operations-console@585850a53ef6c348f4f297468f1ccdb487b5a6c9`;
- `workspace-governance@20ffe1a2d3530b370c116ea0f54cef5c47b7afa4`;
- profile `agent-console-assistant-v1` on local Ollama 0.40.1 with the exact
  `qwen3:8b` digest;
- the existing `refinement-catalog` composition; and
- the loopback-only, single-operator `dev-integration` boundary described
  above.

Not approved:

- direct browser access to OOS, CGG, the gateway, or a provider;
- raw-context fallback, real client data, or secrets in model input;
- model-selected profiles, providers, actions, approvals, or mutations;
- an activated Agent Action owner adapter under this decision;
- stale, malformed, incomplete, conflicting, synthetic-substitute, or
  mismatched source and operating evidence;
- shared, multi-user, remote, public, stage, production, release, or
  paid-provider operation; or
- treating this decision as proof that Platform commissioning already passed.

Any change to identity, credential custody, data classification, context
projection, provider or model selection, response schema, action authority,
network exposure, runtime profile, composition membership, or source revision
requires another delta review.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
- [Governed AI access model](../../standards/governed-ai-access-model.md)
- [Governed AI Gateway component](../../architecture/components/governed-ai-gateway/README.md)
