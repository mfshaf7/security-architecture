# Governed AI Gateway

## Role

`governed-ai-gateway` is the platform-owned access-plane component for bounded
governed AI consumers. It is responsible for caller identity checks, provider
credential custody, audit emission, and preventing consumers from bypassing the
gateway with direct provider access.

It is not a model provider, autonomous approval authority, workspace truth
writer, or replacement for operator acceptance.

## Trust Boundary

The gateway sits between governed consumers and any future provider route:

- consumers send caller identity, requested profile, output schema, and
  operator identity metadata to the gateway
- provider credentials are held only by the gateway runtime
- the gateway emits audit events before output can be used by downstream
  workflows
- consumer egress must be denied except for DNS and the gateway service

The current local dev-integration profile uses a provider sentinel to prove
direct-provider bypass denial before a real provider adapter is activated.
Two provider bindings are now selected but inactive:

- local Ollama `qwen3:8b` as the initial no-cost dev-integration route
- OpenAI Responses API plus `gpt-5.6-terra` as a future paid route

Consumers depend on the logical model profile, not either provider binding.
Each binding requires its own activation evidence and may be suspended without
rewriting consumers or activating the other route.

## Current Admitted Shape

- owner repo: `platform-engineering`
- workspace consumer contract owner: `workspace-governance`
- security owner: `security-architecture`
- current runtime lane: local-k3s `dev-integration`
- current profile: `governed-ai-gateway`
- stage/prod status: not admitted
- current activation posture: dev-integration runtime proof allowed; live
  governed workspace consumption still blocked

## Security Model

### Identity

The gateway must receive caller identity at the access-plane boundary and emit
that identity into audit records. Operator identity is separate and remains
required when human approval is required.

### Secrets

Provider credentials must stay in gateway custody. Consumer repos and consumer
namespaces must not receive provider secrets. Gateway inspection endpoints may
report custody metadata but must not reveal token values.

### Delivery

Dev-integration proof is local evidence only. Stage and production require
reviewed source changes, platform release authority, rollback controls, and
current security acceptance.

### Runtime

Consumer egress defaults to deny. The only allowed AI invocation path is the
gateway service. If the consumer can reach the provider sentinel directly, the
activation path is blocked.

A local provider route also crosses the Windows-host boundary. Host listener,
firewall, and forwarding rules must admit only the managed gateway path and
must deny direct consumer and unrelated local-network access. Local inference
does not make a broadly reachable provider endpoint acceptable.

### AI

Model output is suggestion-only. It must not directly mutate workspace,
platform, product, or component truth. Workspace intake remains operator
accepted or operator overridden.

## Principal Risks

- provider credentials leaking into consumer namespaces
- direct provider egress bypassing the gateway
- audit records missing caller or operator identity
- dev-integration evidence being mistaken for stage or prod readiness
- model output being treated as workspace decision authority
- a host-local provider being mistaken for an implicitly trusted endpoint
- provider or model drift occurring without route revalidation

## Required Companion Artifacts

- Gateway dev-integration review:
  [../../../reviews/platform/2026-05-06-governed-ai-gateway-devint-runtime.md](../../../reviews/platform/2026-05-06-governed-ai-gateway-devint-runtime.md)
- Local Ollama binding review:
  [../../../reviews/platform/2026-08-20-intake-classifier-v1-local-ollama-binding.md](../../../reviews/platform/2026-08-20-intake-classifier-v1-local-ollama-binding.md)
- Bounded runtime-assist activation review:
  [../../../reviews/platform/2026-04-29-bounded-governed-ai-runtime-assist-activation.md](../../../reviews/platform/2026-04-29-bounded-governed-ai-runtime-assist-activation.md)
- AI security and governance standard:
  [../../../standards/ai-security-and-governance.md](../../../standards/ai-security-and-governance.md)
- AI and agentic domain:
  [../../domains/ai-and-agentic.md](../../domains/ai-and-agentic.md)
- component inventory:
  [../../platform/component-inventory.md](../../platform/component-inventory.md)
- platform component docs:
  `platform-engineering/docs/components/governed-ai-gateway/README.md`
- dev-integration profile registry:
  `workspace-governance/contracts/developer-integration-profiles.yaml`
