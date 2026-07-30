# Platform Security Assessment: 2026-07

| Field | Value |
| --- | --- |
| Document ID | SAR-DET-2026-07 |
| Version | 1.0 |
| Status | Published |
| Owner | Security Architecture |
| Reviewers | mfshaf7 |
| Classification | Internal |
| Created | 2026-07-30 |
| Last Updated | 2026-07-30 |
| Related Executive Report | [`2026-07-executive.md`](2026-07-executive.md) |
| Supersedes | [`2026-04-detailed.md`](2026-04-detailed.md) |
| Related Findings Register | [`../../../registers/findings-register.md`](../../../registers/findings-register.md) |
| Related Risk Register | [`../../../registers/risk-register.md`](../../../registers/risk-register.md) |

## Summary

This assessment refreshes platform security posture from current source and
governance evidence. It distinguishes three evidence layers:

- design intent: standards, architecture, and proposed decisions
- implemented control: merged source, contracts, manifests, and validators
- operating evidence: current runtime, drill, identity, or audit proof

The source control model has advanced materially since April. The remaining
highest risks are concentrated in operating proof and trust concentration, not
in the absence of security vocabulary or review structure.

## Scope And Method

The reassessment covers:

- human identity and privileged access
- Vault recovery-material governance
- GitOps repository trust
- Vault and External Secrets recovery posture
- host-control trust boundaries
- AI and agentic governance

Evidence inspected on 2026-07-30 included:

- `security-architecture` standards, ADRs, architecture views, reviews, and
  inventories at `main` commit `5fd8325`
- `workspace-governance` aligned with remote `main` at `6a548e6`
- `platform-engineering` aligned with remote `main` at `3fa470f`
- `openclaw-host-bridge` aligned with remote `main` at `f433e3c`
- `openclaw-runtime-distribution` aligned with remote `main` at `5fa18f3`

The review did not inspect secret values, exercise production credentials,
mutate live runtime, perform penetration testing, or execute a recovery drill.
Where current operating evidence was absent, the corresponding finding remains
open.

## Current Architecture Judgment

### Identity And Privilege

Design intent is clear: Vault and Argo CD human access should use OIDC, while
local credentials should be break-glass only. The credential inventory still
describes human access as transitional and the federated-access ADR remains
proposed.

Implemented control therefore does not prove the shared privileged credential
blast radius has been removed.

### Secrets And Recovery

The platform has a normative secrets-and-recovery standard, Vault and External
Secrets architecture, declarative controller configuration, and recovery
runbooks. These are meaningful implemented controls.

Current evidence does not prove dual-control custody of recovery material,
periodic recovery verification, or a recent end-to-end secret-delivery recovery
drill. Documentation is not substituted for operating evidence.

### GitOps And Machine Trust

Argo CD repository access is represented through Vault-backed
`ExternalSecret` configuration and remains under the machine-identity target
model. The immediate unmanaged-visibility finding remains mitigated.

The longer-term GitHub App or equivalent machine-identity migration remains an
active workstream, but that target-state work does not reopen the already
mitigated repository-visibility defect.

### Host Control

Host control is intentionally separated from product runtimes through typed
tools, bridge policy, permission tiers, audit, allowed-root constraints, and
reviewed runtime packaging. This is the correct architecture.

The bridge still performs high-trust host actions and may be reached from
user-facing or model-adjacent paths. Without a fresh operating attestation for
the active bridge policy, audit path, and runtime identity, the finding remains
open.

### AI And Agentic Governance

AI governance is now formalized through:

- the AI security and governance standard
- the AI system inventory
- approved model-profile and access-plane contracts
- bounded runtime-assist activation rules
- context-admission requirements
- review triggers for AI-shaped action paths
- explicit separation between suggestion, operator acceptance, and mutation

This mitigates the original finding that no formal governance model existed.
It does not approve every model invocation. Direct providers, new data scopes,
tools, autonomous actions, identity boundaries, and shared runtime activation
still require concrete delta review and operating evidence.

## Finding Review

### F-001: Shared Privileged Credential Blast Radius

- status: open
- severity: High
- owner: Security Architecture / Platform
- next disposition checkpoint: 2026-10-30

Reason: the federated human-access decision remains proposed and the credential
inventory still records transitional local access. No current operating
evidence proves separation of routine and break-glass authority.

Required evidence:

- accepted federated-access decision
- implemented Vault and Argo CD identity integration
- role and revocation proof
- separate break-glass custody and audit

### F-002: Recovery-Material Governance Is Incomplete

- status: open
- severity: High
- owner: Security Architecture / Platform
- next disposition checkpoint: 2026-10-30

Reason: standards and runbooks exist, but current custody, dual-control, backup
verification, and recovery-drill evidence are not recorded.

Required evidence:

- named custody model
- approved secure storage and backup inventory
- dual-control or equivalent approval path
- dated recovery verification and post-drill review

### F-003: Argo CD Repository Trust Drifted Out Of Managed Visibility

- status: mitigated

Reason: the repository credential path is declarative and Vault-backed. The
target machine-identity modernization work remains active separately.

### F-004: Vault Manual-Unseal Deployment Was Operationally Fragile

- status: mitigated

Reason: the recovery path and operational handling remain documented, and no
source evidence was found that invalidates the earlier mitigation.

### F-005: Secret Delivery Was Correct In Design But Brittle In Recovery

- status: open
- severity: Medium
- owner: Platform
- next disposition checkpoint: 2026-10-30

Reason: declarative Vault and External Secrets configuration exists, but a
current end-to-end recovery drill and attestation are absent from the reviewed
evidence.

Required evidence:

- Vault-to-External-Secrets recovery drill
- namespace secret reconciliation proof
- rollback or failed-recovery evidence
- operator-attributed result

### F-006: Host-Control Crosses A High-Trust Boundary

- status: open
- severity: High
- owner: Security Architecture / Platform
- next disposition checkpoint: 2026-10-30

Reason: the architecture is correctly bounded, but the active policy, audit,
runtime identity, and environment alignment need fresh operating evidence
before the residual risk can be reduced.

Required evidence:

- active bridge source and policy attestation
- allowed-root and permission-tier verification
- audit-path verification
- stage/prod environment-boundary proof

### F-007: AI And Agentic Governance Is Not Yet Formalized

- status: mitigated
- residual risk: Medium

Reason: governance is now formalized in standards, inventories, access
contracts, context controls, and delta-review requirements. Concrete AI
activations remain gated and must not inherit this mitigation as runtime
approval.

## Decisions

1. retain F-001, F-002, F-005, and F-006 as open
2. set their next accountable disposition checkpoint to 2026-10-30
3. retain F-003 and F-004 as mitigated
4. mark F-007 and its broad governance-immaturity risk mitigated
5. complete the AI-governance formalization workstream while continuing
   concrete AI reviews through their owning delivery paths
6. require future published assessments to stay current while allowing
   superseded assessments to remain as immutable historical evidence

## Conclusion

Security governance is functioning as an active review and control system, but
the platform is not yet at mature operating-control posture. Current source
evidence supports continued governed development and bounded dev-integration
work. Identity, recovery, secret-delivery resilience, and host-control
operating proof remain explicit gates rather than implied completion.
