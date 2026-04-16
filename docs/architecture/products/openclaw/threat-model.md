# OpenClaw Threat Model

## Principal Threats

| Threat | Why It Matters | Main Control Surface |
| --- | --- | --- |
| Prompt injection through chat or retrieved context | can influence tool routing, approvals, or sensitive context | AI domain and product control review |
| Privileged host actions triggered from user-facing workflows | crosses the highest-trust local execution boundary | host-control domain and bridge policy |
| Environment drift between stage and prod | can break delivery, file staging, or admin gating unexpectedly | platform governance and bridge attestation |
| Delivery-path failures for files and screenshots | expose weak seams between runtime, bridge, and chat surface | product runtime plus host-control review |
| Over-broad admin capability exposure | increases blast radius for model or user mistakes | typed tool exposure and explicit admin gating |

## Review Questions

- can untrusted input influence prompts, tools, or approvals
- is host-facing behavior deterministically constrained outside the model
- are file and screenshot paths environment-aligned and auditable
- is stage treated as a true pre-production trust boundary
- can the live deployment be attested from source through digest to runtime
