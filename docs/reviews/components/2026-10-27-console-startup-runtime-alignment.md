# Console startup provider-version security delta

## Summary

Approve the existing local dev-integration binding alignment for the exact Gary Platform candidate `a3412fbd89ee953a7e9450e412068a13854e2236`, tree `b5a4c020860aa4570b489826bd3173fc8b5f9cc5`. Merged Platform revision `e43abde20b01dfea997c55d3149f1ecb02e0665e` has that identical reviewed tree; the paired finite decision selects this merged revision before live commissioning. This retains the same architecture, gate, provider/model and caller authority.

## Scope Delta

All six active local Ollama bindings require0.40.8, while a bounded query from the actual gateway observes0.40.11. The full selected qwen3:8b digest matches. Source-realization readiness is active/eligible but explicitly refused with provider-integrity-failed. Updating the six version fields together resolves this known metadata mismatch without widening accepted versions or disabling integrity checks. Every other registry field remains identical, including model digest, route, callers, purpose/tasks, data scope, limits, fallback and selected model-management configuration.

The same source corrects operator documentation about the unchanged systemd start-rate policy. Three starts per ten-minute window is not a lifetime attempt cap; slow faults can retry across windows. Let an in-flight owner upgrade/rollback finish before stopping a subsequent retry. No executable, retry policy, new scheduler, service or privileged host path is introduced.

## Review Areas

AI/runtime: metadata alignment accepts this exact existing daemon version, not arbitrary future automatic updates or new model bytes. Model inference is not used to establish metadata integrity. Provider unavailability or later version/digest drift remains a visible refusal. Existing dedicated accounts, purpose activation, explicit configured routing/fallbacks, provider credential custody, closed APIs, egress and caller/data boundaries are retained. Other execution-owner pins and existing Security gates remain unchanged.

Delivery: the owner change record and primary operator procedure describe the demonstrated drift, exact source/Security sequence and rollback. All six shared bindings are reconciled together. The earlier startup-registration source correction and all inherited editor, source, publication, performance and truthfulness boundaries remain accepted through their prior deltas. The generated owner-record index must include this new record before closure.

Source proof: full local Platform make validate passed, including existing profile/adapter, complete-runtime, lifecycle, controlled-proof and infrastructure checks. Committed base-aware whitespace and governance-document checks pass against fetched origin/main at2a04eda. A semantic comparison proves only the six expected version fields differ in the registry. Exact-head hosted CI40358892117 and repo-posture40358892099 passed. Delegated mfshaf7 approval covered Gary head a3412fb before PR344 merged with identical tree.

Operating limits: a delayed normal startup completed all five profiles, yet final readiness still refused the older selected provider version. The sample retained at least12264MiB available, zero swap and zero memory-pressure stalls. One additional Python segmentation fault occurred during the delayed run. The version mismatch does not explain cross-runtime native faults or prove a timing-only cause. Direct blob comparisons for202 relevant files matched Git. Bounded database logs showed no corruption/panic signal; no full database integrity claim is made.

An earlier controller stop interrupted Temporal's owner rollback. The existing native Helm rollback restored the exact last deployed revision320 as revision323, leaving no pending operation and preserving owner PVC/history. This is interrupted-action recovery, not a new source defect or permission to edit Helm records. The procedural correction belongs in the same existing memory learning PR314.

## Decision

**approved** for the exact reviewed Platform source/tree and the six existing local version bindings. Land Platform first, update the paired finite decision and generated owner-record index, then land this Security acceptance before advancing the watched runtime checkout. Preserve all seven-owner source bindings, decision delivery-1313-ai-routing, gate gate:ai-routing-composed-security and architecture-packet delivery-1313-v1 except the exact reviewed Platform revision/tree selection.

Commission through the existing complete-runtime operation and require current all-six profile metadata readiness, consumed credentials/renewal, authenticated Console, model registry and retained owner/current/history projections. Neither source checks nor a healthy frontend establishes restored operation or crash-free PC startup. The native fault cause remains unverified and outside this version-alignment judgment. Final operating evidence and cleanup stay in the existing memory learning PR314; no new ART item or architecture version is created. The main agent retains Security closure and final landing judgment.
