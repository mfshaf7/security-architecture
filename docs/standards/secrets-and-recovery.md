# Secrets And Recovery Standard

## Secrets

- secrets must have a system owner and rotation policy
- static credentials should be minimized
- runtime secrets should be sourced from Vault where supported
- controller credentials must be declarative and reviewable

## Recovery Material

- recovery material must not rely on operator memory
- recovery material must be stored in approved secure storage
- encrypted backup copies may exist, but must be tracked
- break-glass usage must be logged and followed by review

## Prohibited Patterns

- reusing one password across multiple control planes
- storing plaintext recovery material on desktops
- unmanaged controller secrets without an owner
