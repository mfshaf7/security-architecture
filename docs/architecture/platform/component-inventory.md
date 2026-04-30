# Component Inventory

This inventory highlights the components that matter most to security review and
points to their security views where they exist.

## Shared Platform Components

| Component | Role | Trust Relevance | Security View |
| --- | --- | --- | --- |
| Argo CD | GitOps control plane | deploys platform state and consumes repo credentials | [`../components/argo-cd/README.md`](../components/argo-cd/README.md) |
| Vault | secret authority | stores runtime secrets, operator credentials, and recovery-sensitive material | [`../components/vault/README.md`](../components/vault/README.md) |
| External Secrets Operator | secret delivery plane | materializes Vault secrets into namespaces | [`../components/external-secrets/README.md`](../components/external-secrets/README.md) |
| Kubernetes API | orchestration plane | underpins controller authority and service-account trust | reviewed through platform and domain views |
| Observability stack | visibility plane | holds operational telemetry, alerts, and sensitive runtime metadata | [`../components/observability/README.md`](../components/observability/README.md) |
| Platform PostgreSQL | shared data service | stores platform-managed state for platform products and services | [`../components/platform-postgresql/README.md`](../components/platform-postgresql/README.md) |
| workspace-governance-control-fabric | governance runtime control fabric | evaluates workspace readiness/admission inputs and will hold receipt, graph, and ledger runtime surfaces | [`../components/workspace-governance-control-fabric/README.md`](../components/workspace-governance-control-fabric/README.md) |
| operator-orchestration-service | shared operator workflow broker | holds backend credentials, authenticates machine callers, and emits durable workflow audit | [`../components/operator-orchestration-service/README.md`](../components/operator-orchestration-service/README.md) |

## Product And Runtime Components

| Component | Role | Trust Relevance | Security View |
| --- | --- | --- | --- |
| OpenClaw prod gateway | production runtime gateway | user and system interaction plane with privileged boundary crossings | [`../products/openclaw/README.md`](../products/openclaw/README.md) |
| OpenClaw stage gateway | pre-production validation gateway | mirrors high-trust runtime shape and should be governed accordingly | [`../products/openclaw/README.md`](../products/openclaw/README.md) |
| openclaw-runtime-distribution | governed runtime composition path | packages runtime inputs and preserves attestation between source and runtime | [`../components/openclaw-runtime-distribution/README.md`](../components/openclaw-runtime-distribution/README.md) |
| Telegram surface | user interaction surface | receives commands and returns content in a chat-driven threat model | [`../components/openclaw-telegram-channel/README.md`](../components/openclaw-telegram-channel/README.md) |
| host-control plugin | typed runtime tool surface | exposes which host-facing operations the runtime may request | [`../components/host-control-plugin/README.md`](../components/host-control-plugin/README.md) |
| OpenProject | product application surface | multi-user web application with persistent data and admin workflows | [`../products/openproject/README.md`](../products/openproject/README.md) |

## Privileged Host Components

| Component | Role | Trust Relevance | Security View |
| --- | --- | --- | --- |
| openclaw-host-bridge | host action executor | privileged local execution, staging, and audit boundary | [`../components/openclaw-host-bridge/README.md`](../components/openclaw-host-bridge/README.md) |
| openclaw-host-recovery | resilience service | recovery and supervision support for host-controlled runtime | reviewed through host-control domain and bridge component views |

## Cross-Cutting Risk Surfaces

| Surface | Why It Matters | Security View |
| --- | --- | --- |
| AI and agentic behavior | can influence privileged workflows, prompts, and tool routing | [`../domains/ai-and-agentic.md`](../domains/ai-and-agentic.md) |
| Identity and access | governs human, machine, and break-glass separation | [`../domains/identity-and-access.md`](../domains/identity-and-access.md) |
| Secrets and recovery | governs secret authority and recovery material | [`../domains/secrets-and-recovery.md`](../domains/secrets-and-recovery.md) |
| GitOps and machine trust | governs source-to-runtime control-plane trust | [`../domains/gitops-and-machine-trust.md`](../domains/gitops-and-machine-trust.md) |
| Host control | governs privileged boundary crossing from runtime to host | [`../domains/host-control.md`](../domains/host-control.md) |
