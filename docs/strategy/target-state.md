# Target State

## Architectural Goals

The target platform should:

- use SSO/OIDC for human access to Vault and Argo CD
- avoid shared local operator passwords
- use managed machine identity for Git and automation access
- keep recovery material under explicit dual-control governance
- maintain a current credential inventory with owners and rotation policy
- treat Vault as the source of truth for managed platform secrets

## Target Control Model

### Human Access

- Vault human login via OIDC
- Argo CD human login via OIDC
- local admin passwords disabled or reserved for break-glass only

### Machine Access

- External Secrets uses Vault Kubernetes auth
- Argo CD uses a dedicated GitHub App or equivalent machine identity
- CI/CD uses short-lived federation where supported

### Recovery

- Vault init material stored in approved secure storage
- encrypted backup copies tracked and periodically verified
- recovery requires documented operators and explicit procedure
- break-glass credentials are separate from daily operator credentials

### Governance

- every privileged credential has:
  - system owner
  - technical owner
  - storage location
  - rotation interval
  - revocation procedure

## Desired End-State Decisions

1. human access is federated
2. machine access is isolated and least-privileged
3. recovery material is governed and recoverable
4. no single reused secret can unlock multiple control planes
