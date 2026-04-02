# Identity And Access Standard

## Principles

- no shared human administrator credentials for normal operations
- human privileged access should use federated identity
- machine identities must be isolated from human identities
- break-glass access must be explicitly separate and tightly governed

## Required Outcomes

- Vault human access via OIDC
- Argo CD human access via OIDC
- role mapping based on groups, not individual secret sharing
- documented approval path for privileged access changes
