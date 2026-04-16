# Trust Boundaries

This document defines the primary trust boundaries used by reviews and
assessments in this repository.

## Human Boundary

Humans interact with GitHub, Argo CD, Vault, Windows/WSL administration, and
user-facing channels. This boundary should move to federated identity and
explicit break-glass separation.

- main concern:
  - human privilege concentration and weak separation of routine versus
    break-glass access
- primary docs:
  - [`../domains/identity-and-access.md`](../domains/identity-and-access.md)
  - [`../../standards/identity-and-access.md`](../../standards/identity-and-access.md)

## GitOps Boundary

Argo CD bridges source repositories into cluster state. This boundary depends on
repository integrity, repository credentials, controller authorization, and
promotion governance.

- main concern:
  - compromise or drift between approved source and live runtime
- primary docs:
  - [`../domains/gitops-and-machine-trust.md`](../domains/gitops-and-machine-trust.md)
  - [`overview.md`](overview.md)

## Secrets Boundary

Vault and External Secrets define the secret-authority chain. This boundary must
preserve least privilege, explicit policy mapping, recovery governance, and
clear owner custody.

- main concern:
  - weak secret custody, unclear recovery material governance, or brittle
    bootstrap paths
- primary docs:
  - [`../domains/secrets-and-recovery.md`](../domains/secrets-and-recovery.md)
  - [`../../standards/secrets-and-recovery.md`](../../standards/secrets-and-recovery.md)

## Product Runtime Boundary

Product runtimes process user, system, and integration flows. This boundary
needs separation between user-facing behavior, product orchestration, and
privileged operations.

- main concern:
  - product logic becoming the trust anchor for secrets, approvals, or host
    actions
- primary docs:
  - [`../products/openclaw/README.md`](../products/openclaw/README.md)
  - [`../products/openproject/README.md`](../products/openproject/README.md)

## Host-Control Boundary

The host bridge and recovery services act on the WSL host with elevated
capability. This is the most sensitive local execution boundary in the current
platform.

- main concern:
  - user-facing or model-influenced inputs shaping privileged host operations
- primary docs:
  - [`../domains/host-control.md`](../domains/host-control.md)
  - [`../components/openclaw-host-bridge/README.md`](../components/openclaw-host-bridge/README.md)

## AI Boundary

Model-driven and agentic behaviors can influence actions, content handling, and
operator decisions. This boundary requires controls for prompt injection, tool
scoping, output validation, and human oversight.

- main concern:
  - untrusted input shaping prompts, tools, or privileged action paths
- primary docs:
  - [`../domains/ai-and-agentic.md`](../domains/ai-and-agentic.md)
  - [`../../standards/ai-security-and-governance.md`](../../standards/ai-security-and-governance.md)
