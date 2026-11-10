# Windowless Windows health monitor launcher

> Withdrawn; not commissioned. Live deployment was terminated by endpoint
> protection. The conditional approval below is superseded by the
> [withdrawal review](2026-11-11-withdraw-windowless-health.md), which authorizes
> rollback and containment only. It does not authorize restoring blocked items.

## Summary

- Date: 2026-11-11.
- Classification: operator-approved host-bridge maintenance outside ART.
- Landing Unit Decision: `child_isolated_landing_unit`,
  `windows-health-acceptance-20261111`; separate Security review/index follows the
  owner source landing.
- Decision: approved within the local existing-user boundary below.

Extends the [host-bridge baseline](2026-04-18-openclaw-host-bridge-security-baseline.md).
This is a Windows utility launcher repair, not a governed bridge-runtime release.

## Scope Delta

Bridge PR18 merges Gary candidate `cc2ed52064396441c2663ce5b1543acfaf7e27f2` as
`0a74974e2a23b4e1732b94e4f16b5ad607e74f2a`, identical reviewed tree
`b8539b068c695316896b277b9673b00f41e8c22f`. The existing GUI Windows Script Host
starts the existing fixed health script with a hidden console at creation time.
The compatibility CMD returns immediately. A GUI Startup shortcut replaces the
visible waiting parent. Stdout/stderr append to the existing private runtime
directory; launcher errors have a separate diagnostic log.

The local native console-host experiment stalled on the installed Windows build
and was rejected before publication. No experimental console-host dependency
is part of the accepted source. The accepted JScript is explicitly hosted by
Windows Script Host; it is not Node.js or VBScript. Script-host policy must be
qualified on each supported installation and is never enabled or weakened here.

## Review Areas

Runtime: fixed installation-local script, same interactive Windows user, same
monitor interval and private runtime directory. No elevation, scheduled task,
service, network permission or new host operation is added. Inherited CMD
redirection preserves native stderr without altering the monitor's PowerShell
error handling. Monitor output remains local with the existing runtime custody.
Only trusted installation paths and the pre-existing private runtime environment
override are used; there is no browser/model-supplied command interface.

The installed monitor contains local recovery extensions. Installation must
preserve its exact bytes and existing recovery behavior, replacing only the
accepted launcher files and Startup entry. Interactive terminal settings and
global execution policy are unchanged. Existing identity, secrets, AI and host
enforcement authority remain inherited; no baseline finding is closed here.

## Validation And Operating Evidence

All26 bridge tests, committed governance and change-record checks against fetched
origin/main, and the required hosted check pass. Delegated mfshaf7 approval covers
the exact Gary head. Native Windows qualification with spaces in paths returned
the caller in218ms, advanced the worker heartbeat after caller exit, captured
stdout plus native stderr, and used EnumWindows to prove no visible worker
window. The finite worker exited; real monitor data was untouched by that test.

Live installation must preserve rollback bytes, stop only the positively
identified previous monitor, launch the native GUI Startup shortcut once, and
prove exactly one monitor and two fresh real snapshots with no visible monitor
window. A detached return alone is not health evidence. The native shortcut
exercise is not a claim of an actual reboot rehearsal.

## Decision

Approved for this existing local-user installation boundary after reviewed-source
installation and native operating readback. Rollback restores the preserved
launcher/Startup entry without replacing the monitor script or deleting runtime
data. Main agent retains Security closure and final landing judgment under
standing operator delegation; this is not independent external attestation.
No Platform/Console composed source pin changes or new ART item are required.
