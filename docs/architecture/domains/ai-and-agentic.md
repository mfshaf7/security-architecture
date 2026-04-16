# AI And Agentic Domain

## Purpose

This document defines the security architecture view for model-assisted and
agentic behavior on the platform.

## Scope

This domain covers:

- LLM-integrated application behavior
- chat-driven product workflows
- tool calling and agentic action paths
- prompt, context, and output handling
- auditability for AI-shaped decisions and actions

## Boundaries And Interfaces

- untrusted input reaches products through chat, web, or retrieved context
- model behavior may influence routing, tool selection, or operator decisions
- privileged actions must still be gated by deterministic controls outside the
  model

## Key Risks

- prompt injection influencing tools or policy decisions
- hidden context exposure to models or agent loops
- model output treated as trusted action authority
- weak attribution for AI-triggered actions

## Control Objectives

- keep authorization and policy checks outside the model
- minimize sensitive context and justify its use
- require deterministic checks for privileged or destructive actions
- log prompts, tool calls, and policy decisions at an appropriate level
- require architectural review for materially new agentic capabilities

## Review Triggers

- new model provider or major model behavior change
- new tool-calling or agentic execution path
- new use of confidential context in prompts or retrieval
- any AI path that crosses host-control, secrets, or delivery boundaries

## Related Standards And Evidence

- [`../../standards/ai-security-and-governance.md`](../../standards/ai-security-and-governance.md)
- [`../products/openclaw/threat-model.md`](../products/openclaw/threat-model.md)
- [`../../../registers/ai-system-inventory.md`](../../../registers/ai-system-inventory.md)
