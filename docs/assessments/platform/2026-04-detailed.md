# Platform Security Assessment: 2026-04

| Field | Value |
| --- | --- |
| Document ID | SAR-DET-2026-04 |
| Version | 1.1 |
| Status | Published |
| Owner | Security Architecture |
| Reviewers | mfshaf7 |
| Classification | Internal |
| Created | 2026-04-02 |
| Last Updated | 2026-04-18 |
| Related Executive Report | [`2026-04-executive.md`](2026-04-executive.md) |
| Related Findings Register | [`../../../registers/findings-register.md`](../../../registers/findings-register.md) |
| Related Risk Register | [`../../../registers/risk-register.md`](../../../registers/risk-register.md) |

## Executive Summary

The platform is operational and recoverable, but several security controls are still immature. The most important weaknesses are concentrated in identity, secret governance, recovery handling, and control-plane trust. The platform currently works because those paths were repaired, not because they were already resilient by design.

The highest-risk pattern is over-concentration of trust. A single reused operator secret crossed local administration, Vault, Argo CD, and recovery handling. That is not a sustainable control model. The second major theme is governance drift: critical trust paths existed, but some were not declarative, not clearly owned, or not robust under failure.

This assessment recommends treating the platform as ready for security architecture hardening, not as a finished secure operating model.

## Assessment Scope

This assessment covers:

- shared control plane: Vault, Argo CD, External Secrets, Kubernetes
- platform delivery and repository trust
- OpenClaw gateway trust boundaries
- host-control and host-bridge interaction paths
- credential, recovery, and secret handling posture
- immediate AI and agentic governance implications

## Assessment Basis

This assessment is based on observed platform behavior and live remediation work performed on April 2, 2026, including:

- Vault outage and recovery
- Argo CD repository credential restoration
- External Secrets trust-path restoration
- host-stack runtime verification
- review of platform runbooks and source-controlled manifests

## Current-State Architecture Summary

The platform currently depends on:

- GitHub as the source repository boundary
- Argo CD as the deployment control plane
- Vault as the secret source of truth
- External Secrets Operator as the delivery mechanism into namespaces
- Kubernetes service-account based machine trust for secret delivery
- a WSL/systemd host-control runtime for local privileged operations
- user-facing Telegram and model-assisted interaction paths that can reach privileged boundaries indirectly

This architecture is workable, but not yet governed at the level expected for long-term security maturity.

## Findings

### F-001: Shared Privileged Credential Blast Radius

Severity: High
Likelihood: High

Affected Assets: Vault, Argo CD, local administration boundary, recovery handling

#### Observation

A single remembered secret was used across multiple privileged workflows, including local sudo access, Vault operator access, Argo CD local operator access, and recovery-related handling.

#### Why It Matters

This creates excessive blast radius. Exposure or reuse of one secret can affect several control planes at once. It also weakens attribution because multiple actions may collapse to effectively the same credential boundary.

#### Evidence

- Vault and Argo CD operator access were standardized on a shared local password model.
- the same secret was also used operationally during recovery handling
- recovery bundle encryption temporarily depended on the same password class

#### Risk

- privilege escalation by credential reuse
- weak separation between routine access and break-glass access
- poor revocation posture after exposure

#### Recommendation

Move human privileged access to OIDC and reserve local passwords for controlled break-glass only. Separate local admin, control-plane operator, and recovery encryption secrets.

### F-002: Recovery-Material Governance Is Incomplete

Severity: High
Likelihood: Medium

Affected Assets: Vault recovery authority, break-glass process

#### Observation

Vault init and unseal material existed and was recoverable, but its storage model was not governed tightly enough. Recovery depended partly on locating material outside normal documented operator memory, and local copies existed on disk.

#### Why It Matters

Recovery material is the highest-sensitivity break-glass asset in the platform. If it is lost, recovery becomes uncertain. If it is exposed, the secret authority boundary is compromised.

#### Evidence

- recovery material was found locally under the platform-core path
- the repo runbooks correctly stated it should be outside the repo, but custody and retrieval workflow were not formalized enough
- a Desktop recovery copy had to be created after the fact for resilience

#### Risk

- weak custody of root recovery authority
- unclear ownership and rotation process
- recovery dependent on operator discovery rather than governed procedure

#### Recommendation

Define a formal recovery-material policy covering storage location, encrypted backup rules, restore procedure, access approval, review cadence, and post-use review.

### F-003: Argo CD Repository Trust Drifted Out Of Managed Visibility

Severity: High
Likelihood: Medium

Affected Assets: Argo CD, platform-engineering source trust, GitOps reconciliation

#### Observation

Argo CD lost effective repository access for the `platform-engineering` source path. There were no repository credential secrets present in the `argocd` namespace at the time of failure, and GitOps reconciliation became partially blind.

#### Why It Matters

If GitOps loses repository trust, the control plane cannot reliably determine desired state. That affects deployment, rollback, compliance, and operator confidence.

#### Evidence

- `platform-root-shared` failed with Git authentication errors
- `argocd` had no repository secrets at the time of inspection
- repo access had to be restored through a new Vault-backed ExternalSecret path

#### Risk

- inability to reconcile platform state
- hidden drift between source and live cluster
- insecure ad hoc recovery if operators bypass managed secret paths

#### Recommendation

Treat machine Git access as a first-class architecture domain. The current Vault-backed repository secret is a valid intermediate state, but the target should be a GitHub App based machine identity with explicit ownership and rotation.

### F-004: Vault Manual-Unseal Deployment Was Operationally Fragile

Severity: Medium
Likelihood: Medium

Affected Assets: Vault control plane

#### Observation

Vault health probes were not compatible with sealed/manual-unseal operation. As a result, Kubernetes restarted Vault pods before operators could complete recovery.

#### Why It Matters

This is a resilience and recoverability defect. Even if recovery material exists, the control plane can still fail to stabilize if orchestration behavior is misaligned with recovery reality.

#### Evidence

- Vault pods were in `CrashLoopBackOff`
- readiness and liveness behavior had to be corrected in `platform-engineering`
- the live StatefulSet also required correction before recovery could complete cleanly

#### Risk

- prolonged control-plane outage
- increased operator error during incident response
- greater temptation to use unsafe recovery shortcuts

#### Recommendation

Treat recoverability as an architecture requirement. Probe behavior, startup assumptions, and break-glass procedures must be designed together, not separately.

### F-005: Secret Delivery Was Correct In Design But Brittle In Recovery

Severity: Medium
Likelihood: Medium

Affected Assets: Vault, External Secrets Operator, runtime secret delivery

#### Observation

Vault plus External Secrets is the correct target design for runtime secret delivery, but the recovery path required reapplying Kubernetes auth and role configuration before namespace SecretStores became healthy again.

#### Why It Matters

This is not a design failure, but it shows that bootstrap and re-bootstrap procedures were not yet sufficiently hardened as repeatable operations.

#### Evidence

- namespace SecretStores returned `InvalidProviderConfig`
- External Secrets recovered only after Vault Kubernetes auth and role setup was re-applied
- controller-side trust was healthy again after forced reconciliation

#### Risk

- degraded confidence in secret delivery during incidents
- hidden dependency on operator-specific recovery knowledge

#### Recommendation

Document and test the full Vault bootstrap and re-bootstrap path, including expected controller outcomes and validation checks.

### F-006: Host-Control Crosses A High-Trust Boundary

Severity: High
Likelihood: Medium

Affected Assets: OpenClaw gateway, host bridge, WSL host boundary

#### Observation

The platform includes a user-facing interaction plane that can eventually drive host-side actions through the host bridge and recovery services on the WSL host.

#### Why It Matters

This is the most sensitive runtime trust boundary in the platform. Any weakness in prompt handling, authorization, policy enforcement, or tool routing can have disproportionate impact.

#### Evidence

- Telegram and gateway flows reach host-control logic
- the host bridge runs under platform-managed systemd services
- host audit logs and media staging are part of the runtime path

#### Risk

- user-facing or model-influenced inputs affecting privileged host operations
- insufficiently constrained tool or action scope
- unclear separation between informational and privileged requests

#### Recommendation

Create a dedicated host-control threat model and architecture review. This should cover authorization gates, deterministic policy enforcement, audit trails, safe staging, and rollback expectations.

### F-007: AI And Agentic Governance Is Not Yet Formalized

Severity: Medium
Likelihood: Medium

Affected Assets: AI-enabled workflows, future agentic systems, model-assisted trust paths

#### Observation

The platform already has model-assisted and chat-driven behavior, and future agentic capabilities are expected, but there was no explicit AI security standard or AI system inventory before this repository was created.

#### Why It Matters

AI-enabled systems change the threat model. Prompt injection, unsafe tool use, hidden context exposure, and weak output validation become architecture concerns, not just product concerns.

#### Evidence

- model-assisted operational flows exist or are expected
- chat-facing interaction is already part of a privileged ecosystem
- AI governance content had to be added as a new architecture workstream

#### Risk

- indirect privilege escalation through model behavior
- data exposure through prompts or retrieved context
- insufficient review before agentic features expand

#### Recommendation

Maintain AI as an explicit security architecture domain. New AI or agentic capabilities should require inventory, trust-boundary review, tool-scope review, and action-safety controls.

## Risk Themes

### Theme 1: Identity Over-Concentration

Too much trust is concentrated in too few human secrets.

### Theme 2: Recovery Depends On Operator Knowledge More Than Desired

Recovery is possible, but still too dependent on ad hoc operator memory and intervention.

### Theme 3: Control-Plane Trust Must Be More Declarative

Repository trust, secret delivery, and recovery should all be clearly visible and governed through source-controlled architecture and managed secret paths.

### Theme 4: Runtime Boundaries Need Stronger Deliberate Design

Host-control and AI-adjacent behavior require dedicated review because they connect lower-trust inputs to higher-trust actions.

## Recommended Workstreams

### Workstream A: Human Identity Modernization

- move Vault human access to OIDC
- move Argo CD human access to OIDC
- define local accounts as break-glass only

### Workstream B: Machine Identity Modernization

- replace PAT-based Argo repo access with GitHub App credentials
- inventory all machine credentials and ownership
- define rotation and revocation procedure for each machine trust path

### Workstream C: Recovery Governance

- formalize recovery-material handling
- define encrypted backup rules
- define post-use review and periodic recovery drills

### Workstream D: Host-Control Security Review

- create a host-control threat model
- map user-facing inputs to privileged actions
- define deterministic authorization and tool-scope controls

### Workstream E: AI Security And Governance

- maintain an AI system inventory
- define review criteria for agentic features
- require prompt, tool, data, and action safety analysis for future AI changes

## Prioritized Actions

### Immediate

1. rotate exposed shared operator credentials and tokens
2. classify break-glass vs routine access paths
3. maintain Vault-backed management for controller credentials

### Near-Term

1. design OIDC for Vault and Argo CD
2. design GitHub App access for Argo CD
3. formalize recovery-material storage and restore procedure
4. assess host-control architecture as a dedicated review

### Longer-Term

1. retire routine local operator passwords
2. reduce or eliminate long-lived static user tokens
3. build recurring architecture review for platform and AI changes

## Overall Assessment

The platform is now recoverable and presently healthy, but it is still in a security transition state. The right next move is not more ad hoc hardening. The right next move is disciplined architecture work that separates human identity, machine identity, and recovery authority, while explicitly governing host-control and future AI-enabled behavior.
