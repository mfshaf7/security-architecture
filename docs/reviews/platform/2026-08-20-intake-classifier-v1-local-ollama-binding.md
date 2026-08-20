# Intake Classifier Local Ollama Binding Review

## Summary

- date: 2026-08-20
- owner repo: `security-architecture`
- reviewed platform source: `platform-engineering@43528915fc45376c7145c1b0eedf95222c49d021`
- affected review subjects:
  - `repos.platform-engineering`
  - `components.governed-ai-gateway`
- delivery refs:
  - `openproject://work_packages/251`
  - `openproject://work_packages/411`
  - `openproject://work_packages/865`
  - `openproject://work_packages/866`
  - `openproject://work_packages/415`
- decision: `approved-with-findings`

The `intake-classifier-v1` binding to local Ollama model `qwen3:8b` is
acceptable for bounded, suggestion-only intake classification in
`dev-integration`. The model must remain behind the platform-owned governed AI
gateway. Consumers must not call Ollama directly.

This decision approves the provider and model binding, not live activation.
Platform work item `#866` must implement and prove the gateway-to-host route,
including removal of the currently broad host exposure, before Workspace
Governance work item `#415` may consume it.

The separately reviewed OpenAI Responses API and `gpt-5.6-terra` binding remains
an inactive future route under work item `#864`. Local activation must not
replace that route in consumer code or collapse the logical model profile into
an Ollama-specific contract.

## Scope Delta

### Design Intent

- keep `intake-classifier-v1` as the provider-neutral capability contract
- use local Ollama for no-cost `dev-integration` evaluation
- bind the initial local route to `qwen3:8b`
- keep caller authorization, model-safe context, schema validation, audit, and
  operator acceptance at the governed gateway boundary
- preserve OpenAI as a separately activatable future binding

### Implemented Control

The reviewed Platform source currently provides:

- a local-k3s governed AI gateway and provider sentinel
- independent profile and access-plane activation gates
- caller and operator identity capture
- gateway-owned audit emission
- default-deny consumer egress with an explicit gateway path
- a suspended `intake-classifier-v1` profile currently describing only the
  inactive OpenAI binding

The local Ollama adapter, route-specific binding model, and real local-provider
proof are not implemented yet. Those controls belong to Platform work item
`#866`, not this security repository.

### Operating Evidence

Point-in-time host inspection on 2026-08-20 proved:

- Ollama version `0.32.14` is running on the Windows host
- model `qwen3:8b` is installed with digest
  `500a1f067a9f782620b40bee6f7b0c89e17ae61f686b92c24933e4ca4b2b8b41`
- the model is Qwen3 architecture, 8.2B parameters, GGUF Q4_K_M
- the model advertises completion, thinking, and tool capabilities
- the active local OpenClaw configuration also selects `ollama/qwen3:8b`,
  providing operational familiarity but not governed-gateway proof
- port `11434` is listening on host and WSL-facing addresses
- Windows Firewall rule `PlatformCore Ollama 11434` currently allows remote
  address `Any`

The broad listener and firewall posture is not acceptable evidence for gateway
activation. It is a blocking implementation finding for `#866`.

## Review Areas

### Identity

The local provider introduces no external provider identity or API credential.
That does not remove the gateway identity boundary. Every invocation must still
carry an allowed caller identity, requested profile, correlation identity, and
operator identity when acceptance is required.

Ollama must not become a shared anonymous workspace endpoint. Network
reachability is transport, not authorization.

### Secrets

The local Ollama route does not require a provider API secret. Consumer
namespaces must still receive neither provider configuration authority nor a
direct Ollama endpoint. Future OpenAI credentials remain gateway-custodied and
outside this local route.

Prompts, model-safe packets, and model output remain sensitive runtime data.
They must not be written into unbounded provider logs, command lines, or status
surfaces.

### Data And Context

Only the declared `intake-classifier-v1` model-safe packet may cross to Ollama.
Raw workspace dumps, secrets, unrestricted files, and context outside the
profile remain denied even though inference stays on the local host.

Context admission and redaction receipts must be preserved when private
repository excerpts or operator notes are included. Local processing lowers
external disclosure risk; it does not remove data-minimization requirements.

### Runtime And Host Boundary

The route crosses from local k3s into a Windows-host model runtime. Platform
must treat this as an explicit host boundary:

- only the gateway runtime may reach the selected Ollama endpoint
- consumer namespaces must remain unable to reach Ollama directly
- Windows Firewall and forwarding rules must scope port `11434` to the exact
  managed source boundary required by the gateway
- listener and firewall state must be restart-survivable and validated rather
  than repaired ad hoc
- the gateway must bound request size, output tokens, concurrency, timeout,
  retry, and model residency behavior
- provider unavailability, timeout, malformed output, and resource exhaustion
  must fail closed without emitting a suggestion
- the gateway must not pull, delete, replace, or reconfigure models

The current `RemoteAddress: Any` firewall rule blocks activation until it is
narrowed and bypass denial is proven from both governed consumer and unrelated
local-network perspectives.

### AI

`qwen3:8b` is an acceptable speed and stability choice for bounded local
classification. Its advertised capabilities are broader than this use case.
The provider request must therefore:

- disable thinking output
- provide no tools and deny tool selection
- use the approved strict JSON schema
- use bounded, low-variance generation settings
- reject prose, thinking tags, extra fields, and schema-invalid output

Model output remains untrusted suggestion data. It cannot mutate workspace
truth, widen its own input, select tools, or bypass operator acceptance.

The gateway audit must record the logical profile, configured model name,
installed model digest, Ollama version, prompt or policy version, schema result,
latency, bounded usage data, caller identity, and final policy outcome. A model
digest or runtime-version change requires revalidation before continued use.

### Delivery And Rollback

The security review and Platform implementation are separate Landing Units.
The activation sequence is:

1. land and close security review work item `#865`
2. implement and prove the provider-neutral local route in Platform work item
   `#866`
3. confirm that operating evidence satisfies this review
4. allow Workspace Governance work item `#415` to run the governed suggestion
   smoke

Rollback must support independently closing the access-plane gate, suspending
the profile or local binding, restoring the provider sentinel, and disabling
the workspace consumer. Rollback must not require removing the future OpenAI
binding.

## Decision

`approved-with-findings`

The local Ollama and `qwen3:8b` binding is approved for the declared bounded
`dev-integration` purpose. Live activation is not approved by this artifact.

Blocking activation findings routed to Platform work item `#866`:

1. Implement a provider-neutral binding and adapter boundary. Do not encode
   Ollama details in Workspace Governance or Console consumer code.
2. Replace the current broad port `11434` exposure with a managed,
   restart-survivable gateway-only host route and prove direct bypass denial.
3. Pin and audit the selected model digest and Ollama version. Fail closed on
   unreviewed model or runtime drift.
4. Disable thinking and tools, enforce strict schema output, bound request and
   response resources, and reject malformed provider output.
5. Preserve model-safe packet and redaction receipts, gateway audit evidence,
   caller attribution, and operator acceptance.
6. Prove positive invocation plus negative caller, bypass, malformed-output,
   unavailable-provider, timeout, and rollback cases before consumer use.
7. Keep work item `#415` dependent on `#866`. Keep paid OpenAI activation
   isolated under blocked work item `#864`.

## Related Artifacts

- `platform-engineering/docs/components/governed-ai-gateway/README.md`
- `platform-engineering/security/governed-ai-model-profiles.yaml`
- `platform-engineering/security/governed-ai-access-plane.yaml`
- `platform-engineering/security/governed-ai-runtime-assist-contract.yaml`
- `workspace-governance/contracts/governed-intake-assist.yaml`
- `workspace-governance/contracts/context-behavior.yaml`
- `security-architecture/docs/reviews/platform/2026-08-20-intake-classifier-v1-openai-terra-binding.md`
- `security-architecture/docs/reviews/platform/2026-05-06-governed-ai-gateway-devint-runtime.md`
- `security-architecture/docs/architecture/components/governed-ai-gateway/README.md`
- `security-architecture/docs/standards/ai-security-and-governance.md`
