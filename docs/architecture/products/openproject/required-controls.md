# OpenProject Required Controls

## Identity

- admin access should be attributable and least-privileged
- break-glass or maintenance access should be distinct from routine use

## Secrets

- runtime secrets should come from governed platform secret paths
- any application-local credential should have explicit ownership and rotation

## Data And Recovery

- database access should be scoped
- backup and restore expectations should be documented and reviewable

## Visibility

- health, logs, and alerting should exist for the runtime and its data service
- observability access should follow least privilege
