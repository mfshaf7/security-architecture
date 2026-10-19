# October 2026 Existing Security Baseline Reassessment

## Summary

Reviewed on 2026-10-19 UTC. Decision: `approved-with-findings` for continuation
of the existing architectural baseline only. Accountable reviewer: `mfshaf7`;
Codex prepares the evidence and security judgment for exact-head delegated
review. No independent third-party audit is claimed.

This review covers the 17 inventory subjects whose April18 baseline cadence
expired on October18: five repositories, two products and ten components. The
original 13 review narratives remain intact, with a dated reassessment at each
contracted path. Existing subsequent change reviews remain independently
applicable. This is not acceptance of the pending Console authoring/bootstrap
maintenance, a replacement security policy, or permission to activate anything.

Landing Unit: `maintenance-1275-security-baseline-renewal`;
`child_isolated_landing_unit` because its independent periodic-evidence change
must precede dependent governance CI, whereas new-composition acceptance must
later bind actual merged owner revisions. Work remains on the approved
Epic1275 maintenance/operating-qualification path; no new repair ART child.

## Scope And Source Evidence

Fetched canonical `origin/main` and primary HEAD matched for each source below;
all five primary working trees were unchanged. Pending maintenance worktrees
were excluded. These immutable revisions, not a floating repository name, are
the implementation-inspection boundary:

| Owner | Canonical source commit |
| --- | --- |
| Platform Engineering | `ac854a4e08a6d075bd1842127513c55de59f3997` |
| Operator Orchestration Service | `4c74d35b09864c12b4a63beb4fa8a23416381e70` |
| OpenClaw Runtime Distribution | `5f6cc48562e74fd0a3d17a60d436ff3300db87e1` |
| OpenClaw Host Bridge | `86cd8d1a8418ec984a5e915ecb935ae98d3180fd` |
| OpenClaw Telegram Enhanced | `53d77b79d16a0e27bfc06594f14d2d6d10cbb3b6` |

Security review inputs: the thirteen original April18 baselines; current
component/product security views; the identity, secrets, GitOps, host-control
and AI domain views; review checklist; current remediation inventory; and the
following subsequent decisions, without converting their historic proof into
fresh live evidence:

- [Telegram overlay delivery](../../reviews/products/2026-04-17-openclaw-telegram-overlay-governed-prod-lane.md)
- [OpenClaw release control](../../reviews/products/2026-04-23-openclaw-governed-release-control-state.md)
- [Singleton Vault and OpenProject sizing](../../reviews/components/2026-04-23-openproject-runtime-sizing-and-vault-single-node.md)
- [Observability layers and access](../../reviews/components/2026-04-24-observability-baseline-overlay-operator-access.md)
- [ART custody and provenance](../../reviews/components/2026-08-09-art-evidence-custody-and-source-provenance.md)
- [Accepted Console composition and explicit operating limits](../../reviews/components/2026-10-15-governance-console-platform-operation.md)

The August custody decision's implementation follow-ups are historical, not
proof that those capabilities are still absent. Conversely, the April OOS
phase1 capture admission is not a description or blanket approval of today's
whole broker. Later accepted owner/composition decisions govern later paths.

## Reassessment By Boundary

| Subjects | Documented and implemented control inspected | Operating qualification retained |
| --- | --- | --- |
| Platform repo; Argo CD | Platform remains the source/release owner; Argo Applications, reviewed environment contracts and Git-managed controller secret delivery remain present. Source-to-runtime attestation and rollback remain distinct from source review. | A valid source contract is not current stage/prod readiness. No sync, promotion or runtime override was performed for this reassessment. |
| Vault; External Secrets | The canonical Vault Application declares one replica despite the chart's `ha.enabled` setting. Namespace SecretStores declare Vault Kubernetes authentication, role and service-account references; Argo and OOS ExternalSecrets retain store-backed delivery. | This is a singleton on one host, not HA. No recovery drill, unseal-material access or secret-value inspection occurred. F-002/F-005 remain open. |
| Platform PostgreSQL; OpenProject | Shared database access/backup ownership remains Platform-owned. The current OpenProject contract explicitly suspends the platform-integrated application while retaining data and secrets; the active ART dev-integration instance is separate. | Do not start the suspended instance or claim its login works. Neither the dev-integration instance nor a schema test proves governed product readiness, backup restore or SSO. |
| Observability | The accepted model separates Platform baseline, shared component overlays and product overlays; its catalog explicitly remains read-only and secret-free. Product overlay ownership is not shared-control authority. | Existing access and telemetry limits remain. No new tenant, identity, alert destination, public endpoint or writable catalog operation is approved. |
| Runtime Distribution repo/component; Telegram repo/component; OpenClaw | Canonical owner source, published host interfaces and Platform release contracts retain separate packaging, channel and promotion ownership. Overlay approval remains exact-base/digest/stage-bound, not permission for arbitrary runtime patching. | No new base image, overlay, stage qualification or production smoke was executed. The retained promotion-readiness filename is not an alternate release model. |
| Host Bridge repo/component; host-control plugin | Bridge code retains bearer-authenticated operation dispatch, typed permission mapping, allowed-root policy and success/failure audit calls outside model/runtime policy. The plugin remains the typed request surface, not host enforcement authority. | Fresh live policy/identity/audit/environment attestation is not supplied by this document. F-006 remains open; source inspection does not close the high-trust host finding. |
| OOS repo/component | Canonical application/config code retains caller-secret handling, caller-specific isolation and allowlist checks. Its development bypass exists when no credentials are configured and must not be mistaken for an authenticated commissioned profile. Source identity and isolated execution remain purpose/owner/profile-bound, with human review separate from Gary publication. | Accepted runtime configuration must supply the commissioned authentication and exact composition. No new caller, proposed-owner token, model purpose, admission writer or app execution is enabled by this review. |

The review assessed the current architecture and implemented ownership/control
shape, not merely whether files exist. No source/native-test result is promoted
to a fresh operating-control result. Prior operating evidence remains limited
to its named revision, profile, identities and recorded decisions. The final
Console-only app witness and whole-system capability qualification are still
separate unfinished work.

Current bounded implementation checks also passed against the canonical owner
sources: Runtime Distribution's repository-doc validator and its three published
interface/workspace verification entrypoints; Telegram's seven router-contract
tests; the packaged plugin's three and Bridge's two interface tests; and four
Bridge policy tests. The aligned manifests expose 16 plugin tools, 15 stable
bridge operations and three explicitly forbidden scaffold operations. A separate
value-suppressed source check confirmed singleton Vault, namespace Kubernetes
SecretStore bindings, store-backed Argo/OOS ExternalSecrets and the observability
owner split. These checks read source and run isolated owner tests only: no
image build, live host action, credential inspection, secret read or deployment.

## Findings And Risk Disposition

No finding is closed, severity reduced, deadline extended or risk newly
accepted by this renewal. Retain the existing normalized remediation inventory:

- F-001/R-001, WS-001: federated human access and break-glass separation remain
  unimplemented; Security Architecture/Platform own the October30 checkpoint.
- F-002/R-002, WS-002: recovery-material custody, dual-control and drill evidence
  remain outstanding at the same checkpoint and owners.
- F-005/R-005, WS-005: Platform still owes end-to-end secret-delivery recovery
  evidence at the existing October30 checkpoint.
- F-006/R-006, WS-006: Security Architecture/Platform still owe active bridge
  policy, identity, audit and environment-boundary attestation at that checkpoint.
- F-003/R-003 and F-004/R-004 remain mitigated, not magically risk-free;
  machine-identity modernization remains an active workstream. F-007/R-007's
  mitigated governance position does not approve every model/action path.

No new remediation program or infrastructure work is introduced here. Existing
scope-specific delta findings and pending operating gates are retained rather
than duplicated into new defect stories.

## Decision And Review Cadence

Continue the existing narrow baseline decisions with the conditions above and
the unchanged findings/risks. Record this genuine reassessment on October19 and
the next six-month baseline review on 2027-04-19. The earlier October30 finding
and assessment checkpoints still apply; baseline freshness does not waive them.
Append the reassessment evidence at the existing contracted review paths rather
than changing repo-rule paths, schemas or validators to evade the expired gate.

The pending authoring/bootstrap purpose, template, context, provider installation,
model draft, source import and runtime changes require their own final exact
composed Security decision. This review cannot substitute for that decision,
public/private-client qualification, the Console to-do witness, or Epic closure.
