# Source publication after verified protected base advancement

## Summary

The existing Gary publisher can authorize a clean branch that includes newer,
already accepted protected main history. The repair is in [Broker PR #434](https://github.com/mfshaf7/operator-orchestration-service/pull/434),
on Gary's exact source head `73f6e91f7d76f0fbf78fc6ed45b6b1365acf5cc2`.
This is owner maintenance for the strict freshness rule that blocked
[Broker PR #433](https://github.com/mfshaf7/operator-orchestration-service/pull/433)
in Delivery #1384.

## Scope Delta

Keep the original approved session and repository-scoped source grant.
When the original author check includes inherited human or GitHub history,
read the exact canonical branch under the existing provider identity. The
protected head must descend from the session's stored base and already be
an ancestor of the source head. Check Gary's author and committer on every
commit introduced outside that protected history. The approved source branch,
clean worktree condition, non-force publication and exact-head approval still
apply. Bootstrap and special-purpose credential paths retain their existing
verification.

## Review Areas

- **Identity.** The same scoped installation must identify exactly the
  admitted repository before its authenticated branch read can authorize the
  narrower commit comparison. Local remote-tracking refs and unprotected
  provider branches cannot supply that proof.
- **Secrets.** The existing source lease supplies only the current
  repository-scoped provider access. The review introduces no credentials or
  new provider permissions.
- **Delivery.** The proposed head remains immutable during publication.
  Git ancestry is verified without replacement objects. GitHub's strict
  check and delegated human review apply to every new PR head.
- **Runtime.** The executor interface and authorization envelopes are
  unchanged. Existing worker admission and deployment boundaries apply.

The real Git rehearsal started with an already published branch in a
disposable repository. A forward-only update carrying an authenticated and
protected main history succeeded and reused the review. Unprotected main,
newer main absent from the branch, and an unauthorized PR-only commit all
failed before a push. The existing human-authored source denial still passes.
The Broker suite passed 2,087 tests with two skips and zero failures.
Both images built, API health passed and the worker denied execution
without admission.

## Decision

`approved` for the exact merged repair and the existing dev-integration
source publisher. The accepted source revision and tree are recorded in the
composition decision. Use the native owner path for activation and verify
the live continuation of the original work session. The earlier
[Stage 2 Broker source review](2026-11-26-stage-2-broker-saved-project-source.md)
and Platform-specific operating evidence remain valid for their stated scope.
Review the updated #433 head again after synchronizing its protected base.

The merged Broker revision is `9fb97de3da23b6ec09cba88a90dd4336bd85aa10` and its exact tree is `a3ae47fb532c81c82892453fca6543d860d7a275`.
