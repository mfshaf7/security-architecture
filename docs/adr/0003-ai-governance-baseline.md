# ADR-0003: AI Systems Require Explicit Security And Governance Controls

## Status

Proposed

## Context

AI-assisted and agentic capabilities can cross trust boundaries, influence operator decisions, and potentially trigger privileged behaviors through indirect input channels.

## Decision

Treat AI systems as a first-class security architecture domain. All future AI and agentic integrations require explicit review for prompt risk, tool access, data exposure, action authorization, auditability, and human oversight.

## Consequences

- improves consistency of AI control design
- reduces hidden model-driven privilege escalation paths
- requires an AI system inventory and review process
