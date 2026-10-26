# Console standalone runtime and workstation memory

## Summary

Approve the existing local dev-integration frontend's transition from a watched
development server to private source-bound standalone output. Reviewed Platform
candidate `7c378f2909031738532f55888751b22016bc532b`, tree
`33ffd32dad2a59fe3fb51dcbffaa74a379f83059`; the paired decision records the
landed revision `3a686e9ee4eafb2e3a617b0248731cbfc5564af5`, whose tree matches exactly. Console application
source remains `f208f67c03e2cce1d036d108636328b11d6164aa`. This is a runtime
maintenance extension under the existing owner, architecture and gate.

## Scope Delta

The existing Platform launcher exports only the clean selected Console commit,
installs locked dependencies and builds in separate private state. The build
inherits a small explicit environment allowlist; live caller, provider, session,
public-prefixed secret and debug configuration are not forwarded. Complete
standalone code and static assets are staged before publication. A local
manifest binds source, Node version, dependency lock and code-file inventory.
This manifest is integrity evidence inside the existing trusted OS-user boundary;
it does not replace the exact Security-selected source or grant source authority.

Start/status rejects missing, modified, foreign, unsafe or incomplete artifacts.
The actual managed process must match the selected executable, working directory,
production/loopback configuration, heap setting and resource limits; process-start
identity and the current manager PID must remain stable during readback. Next's
process-title rewriting is not treated as changed source. Normal image/response
cache data remain mutable in their specific framework locations; executable
route-cache files, foreign code and symlinks are rejected. Running code and
normal development/build output are separate.

Build failure or timeout kills its compiler process group before service effects.
The build has a4096MiB heap bound. The normal frontend uses a2048MiB heap bound,
MemoryHigh3GiB, MemoryMax4GiB and MemorySwapMax1GiB with bounded rapid restarts.
These limits contain failure and do not attest sufficient capacity by themselves.
Existing source review, credentials, session expiration, OOS command authority,
private accounts, model/provider permissions and backend state remain unchanged.

A staged Windows-user configuration uses a measured20GiB WSL ceiling and6GiB
swap, preserving unrelated settings. DropCache is already the documented default;
recording it explicitly is not evidence of returned host RAM. The installed
WSL3.0.3 source uses a two-minute CPU-idle eligibility condition. Active-workload
and idle/reclaim observations must be separated. Windows working set, Linux
active/cache/available memory and pressure are different measurements. No periodic
cache-flush service, custom reclaim controller or backend shutdown is introduced.
Host configuration activation requires a controlled VM restart and actual readback.

During source staging, unignored diagnostics temporarily dirtied the live Platform
checkout, correctly blocking credential renewal. Evidence was preserved and moved
to verified ignored custody; normal renewal recovered. The owner-local `.art/`
ignore extends the prior review-packet-only rule; no tracked source is hidden.
The separate expired operator session is handled by the existing owning-session
activation path, never by editing issued identity timestamps or widening TTL.

## Review Areas

Runtime and delivery: private exact-source artifacts replace live compilation.
Build publication cannot overwrite the running artifact, and failed preparation
leaves running services untouched. Restoring previous execution follows the
existing accepted-source decision and activation workflow. Artifact/code checks,
readiness and original owner receipts remain distinct. Backend, UI and command
capabilities must retain their prior scope through commissioning.

Identity and secrets: caller credentials remain server-side in the existing
private environment file, with unchanged session/operator verification. The
new launcher does not import interactive credentials, open a debugger, select a
caller/provider, grant browser filesystem access or issue human identity. Build
logs are private, and build inputs exclude live configuration.

Host control: the existing local OS user and reviewed Platform commands remain
the execution boundary. Memory settings do not grant extra host authority.
Capacity must be measured; required services remain available. VM restart
readiness, recovery and configuration rollback are explicit operator procedures.

Source proof: full local Platform validation passed, including the existing
complete-runtime tests. Seven added artifact/process tests cover source/toolchain
mismatch, modified/extra code, missing assets, symlinks/environment files, legitimate
framework cache data, build credential exclusion, process-group timeout cleanup,
isolated committed export, owner-output preservation and real Node process-title
readback. Thirty-one cross-domain cases pass, including build-failure preservation
of existing services. A fresh build took75.12s, conservative summed process RSS
peaked2.54GiB and guest available memory remained above10GiB. Credential-free
standalone preview served the page and12static assets and used about140MiB.
These are source/packaging measurements, not authenticated operating acceptance.

## Decision

**approved** for the exact sources/tree in the paired composed decision. Preserve
all unchanged execution pins and architecture/gate identifiers. Merge the owner
record first, then the regenerated Security change-record index and exact-source
acceptance. Commission only through the existing complete-runtime path. Require
native source/process/budget proof, all existing destinations and owner history,
normal frontend recovery/credential operation, warmed memory comparison and actual
WSL configuration activation. A restart or lower guest allocation alone is not
proof of long-term memory stability or automatic idle reclamation.

Final operating evidence and cleanup are recorded in the linked Workspace
Governance learning closeout rather than creating a post-review owner-source pin
loop. Main-agent judgment retains Security decision and final landing authority.
