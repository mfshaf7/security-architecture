# Platform Security Assessment: 2026-04

## Executive Summary

The platform is functional, but key security controls are immature. Identity, secrets, and recovery practices are partially implemented and too dependent on operator knowledge.

## Key Findings

1. Shared operator credentials had excessive blast radius across sudo, Vault, Argo CD, and recovery workflows.
2. Vault recovery material existed locally without a clearly governed storage and retrieval process.
3. Argo CD repository access was not under visible, declarative secret management until recovery work restored it.
4. Vault startup behavior was fragile because health probes were not aligned with manual-unseal operation.
5. Secret-delivery trust paths required recovery and re-bootstrap before returning to a healthy state.

## Architectural Risks

- over-centralization of trust in a single remembered secret
- insufficient separation of human, machine, and break-glass identities
- insufficient assurance around recovery-material custody
- operational drift in control-plane credentials

## Immediate Recommendations

1. rotate exposed operator credentials and tokens
2. move human access to OIDC
3. move Argo Git access to a managed machine identity model
4. formalize Vault recovery governance
5. establish recurring security review for platform control changes
