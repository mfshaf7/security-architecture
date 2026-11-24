# Temporal startup addresses review

## Summary

The pinned Temporal chart used short service addresses for its namespace Job,
admin tools, and diagnostic UI. A live namespace Job timed out at the short
address, while the fully qualified address returned the existing registered
namespace. The Console integrity check then encountered a container that had
yet to start and had no image identity.

## Scope Delta

The Platform renderer qualifies the four chart-provided frontend address
values within the actual release namespace. Helm waits for the namespace
Job as part of the existing atomic launch. The same renderer is applied in
ordinary startup and in the controlled-proof launch.

## Review Areas

**Runtime.** The destination is the existing Temporal frontend ClusterIP
Service. The pinned chart render test showed that the renderer changes exactly
the four frontend address values. The resulting manifest passed the digest and
ClusterIP-only checks. The existing workflow namespace returned its registered
state and seven-day retention over the corrected address.

## Decision

`approved` for the existing local Console composition.

The [Platform PR](https://github.com/mfshaf7/platform-engineering/pull/389)
passed required GitHub checks and delegated review. The reviewed tree and
merged tree match.

- `platform-engineering@3459da0acb843ef670f106009059ca51d1fe40a4`
- `platform-engineering-tree@6ba2fbbfa092476a83293eb860fcead2893cfbed`

The [composed runtime decision](../components/2026-10-24-configurable-ai-routing.md)
binds this Platform revision with the previously reviewed owner sources.
Operating proof requires the normal startup to finish its generated namespace
Job and record native Console readiness.
