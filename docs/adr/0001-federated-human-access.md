# ADR-0001: Federated Human Access For Vault And Argo CD

## Status

Proposed

## Context

Local operator credentials create excessive blast radius and weak attribution across privileged control planes.

## Decision

Adopt OIDC-based human authentication for Vault and Argo CD. Local password-based access remains break-glass only.

## Consequences

- stronger attribution and revocation
- lower dependence on shared memorized secrets
- requires IdP integration and role mapping
