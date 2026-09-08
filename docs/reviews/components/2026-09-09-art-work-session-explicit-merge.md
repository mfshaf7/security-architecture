# ART Work-Session Explicit Merge Security Delta

## Summary

- date: 2026-09-09
- owner repo: `security-architecture`
- affected review subject: `repos.operator-orchestration-service`
- delivery initiative: `openproject://work_packages/892`
- implementation item: `openproject://work_packages/1117`
- reviewed implementation:
  [OOS PR #199](https://github.com/mfshaf7/operator-orchestration-service/pull/199)
- exact reviewed head:
  [`75cb8b5f1739265ce31be52b6ef977a0b820ab80`](https://github.com/mfshaf7/operator-orchestration-service/commit/75cb8b5f1739265ce31be52b6ef977a0b820ab80)
- review trigger: `broker-runtime-and-caller-surface`
- decision: `approved`

This review approves the exact OOS head above for source merge. The delta adds
one explicit Delivery work-session merge command to the already admitted
caller-bound source executor. It does not add automatic merge, a new identity,
a new credential path, OpenProject mutation behavior, or broader host command
execution.

This approval is exact-head and source-only. The landing unit must still
dogfood the command against PR #199, finalize its Review Packet, and close ART
#1117 through the normal ordered workflow.

## Scope Delta

### Design Intent

- Keep source merge as an explicit operator approval, distinct from
  deterministic `work continue` reconciliation.
- Let OOS expose the same bounded merge semantic to the CLI and future Console
  adapter without placing GitHub or lifecycle policy in the browser.
- Bind merge to the current work-session revision, durable merge-ready Review
  Packet, Security status, and exact live pull-request identity.
- Reject stale or ambiguous state before source authority is invoked.
- Validate generated completion payloads while the Review Packet remains
  repairable instead of discovering deterministic formatting failures after
  finalization.

### Implemented Control

The exact reviewed OOS head implements these controls:

- The API uses the existing caller authentication and separately attributed
  operator identity. Merge requests require a unique command id and the exact
  current session revision.
- The replay-safe command store binds action, caller, operator, work item, and
  request content. A repeated command returns its retained result; conflicting
  reuse fails closed.
- The controller offers merge only when authoritative session projection
  reports `source-merge-approval-required`. Open Security acceptance items
  override that projection and block merge.
- The source adapter re-reads GitHub immediately before merge and requires the
  live PR URL, base branch, and head commit to match the already observed
  merge-ready state.
- GitHub receives an exact-head squash merge using
  `--match-head-commit`. The adapter then requires merged readback for the
  same PR and head plus a concrete merge commit.
- Changed heads, closed or draft PRs, wrong bases, missing merge evidence,
  stale revisions, unavailable executor state, and uncertain outcomes fail
  without claiming successful completion.
- Merge does not delete the branch or worktree. Existing terminal closeout
  remains responsible for manifest-bound resource retirement.
- Review Packet finalization now runs the same completion-evidence rules used
  by landing-unit submission for each directly covered work item.
- The OpenProject mutation validator explicitly distinguishes the GitHub-only
  merge route from canonical backend write routes.

### Operating Evidence

The exact OOS head passed:

- the complete OOS suite: 974 tests with zero failures;
- focused merge, replay, executor-authentication, HTTP, and completion-preflight
  cases;
- API documentation parity: 122 documented and implemented routes;
- orchestration and Refinement workflow bundle validation;
- governance-document validation;
- base-aware change-record validation;
- base-aware OpenProject mutation classification; and
- the GitHub `validate-governance-docs` check on PR #199.

This is implementation evidence. The first operating proof is the same landing
unit using `work merge 1117` against exact PR #199 after this review lands.

## Review Areas

### Identity

No new human or machine identity is introduced. The existing authenticated OOS
caller, accountable operator, work-session identity, and host executor remain
distinct. The executor invokes GitHub with the already admitted operator-owned
host identity; OOS receives no GitHub credential.

This delta expands the finite actions that the executor may perform, but not
who may request them. Caller binding, operator attribution, exact session
revision, and explicit merge invocation remain mandatory.

### Secrets

No secret is added, copied, logged, or delivered to OOS. Existing executor
socket authentication remains unchanged. GitHub authentication stays in the
host operator environment and is not included in the command request, command
receipt, work-session state, or Review Packet.

### Delivery

The merge action preserves pull-request review as a human gate. It cannot be
reached through `work continue`, and it cannot select a different PR, base, or
head from the merge-ready evidence. Direct GitHub merge remains a recovery path
whose result is reconciled from authoritative GitHub state; it is not the
normal receipt-backed workflow.

Rollback is the source revert described by the OOS change record. Existing ART,
GitHub, WGCF, and Review Packet evidence remains preserved.

### Runtime

The host executor gains one named action rather than general shell access. Its
input is the validated work session plus expected PR observation. All command
construction remains internal to the adapter; callers cannot provide shell
arguments or an arbitrary repository path.

The action emits the existing executor audit event and work-session command
receipt. A process or network interruption after GitHub accepts the merge may
produce an uncertain command result; subsequent status reconciles the actual
GitHub state before another action is offered.

### AI

No model call, prompt, AI-derived decision, or autonomous tool authority is
added.

## Decision

`approved`

Approval is limited to:

- OOS PR #199 at head
  `75cb8b5f1739265ce31be52b6ef977a0b820ab80`;
- the explicit caller-bound `work merge` command;
- exact URL, base, and head verification against durable merge-ready evidence;
- the existing host executor and operator-owned GitHub identity;
- pre-finalization validation of generated direct-completion payloads; and
- source-only landing followed by Review Packet and ART closeout.

Approval excludes:

- automatic merge from `work continue`;
- arbitrary GitHub, Git, shell, repository, or pull-request input;
- a new GitHub credential or credential delivery path;
- browser-side lifecycle or merge authority;
- bypass of open Security acceptance, PR review, or ART closeout;
- OpenProject mutation changes;
- stage or production activation claims; and
- any OOS source revision other than the exact reviewed head.

## Related Artifacts

- [OOS owner change record](https://github.com/mfshaf7/operator-orchestration-service/blob/75cb8b5f1739265ce31be52b6ef977a0b820ab80/docs/records/change-records/2026-09-08-art-work-session-lifecycle-order.md)
- [Existing Console/OOS work-session boundary review](2026-08-27-console-oos-delivery-work-session-boundary.md)
- [Existing work-session lifecycle review](2026-08-23-delivery-art-work-session-lifecycle.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
