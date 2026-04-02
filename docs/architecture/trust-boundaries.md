# Trust Boundaries

## Human Boundary

Humans interact with GitHub, Argo CD, Vault, Windows/WSL administration, and user-facing channels. This boundary should move to federated identity and explicit break-glass separation.

## GitOps Boundary

Argo CD bridges source repositories into cluster state. This boundary depends on repository credentials, repository integrity, and controller authorization.

## Secrets Boundary

Vault and External Secrets define the secret-authority chain. This boundary must preserve least privilege, explicit policy mapping, and recovery governance.

## Runtime Boundary

OpenClaw gateways process user, system, and integration flows. This boundary needs separation between chat-facing logic and privileged operations.

## Host-Control Boundary

The host bridge and recovery services act on the WSL host with elevated capability. This is the most sensitive local execution boundary.

## AI Boundary

Model-driven and agentic behaviors can influence actions, content handling, and operator decisions. This boundary requires controls for prompt injection, tool scoping, output validation, and human oversight.
