# Delivery ART Work-Session Evidence

`evidence-profile.json` declares the bounded commands OOS may run against an
exact Security Architecture source revision before a Review Packet becomes
merge-ready.

OOS reads the profile from the Landing Unit's recorded base commit. A branch
cannot add or modify its own evidence authority and use that changed profile
to validate itself. Cross-repository evidence references remain subject to the
full `validate-security-evidence` CI job before merge.

The repository structure contract test is the real-Git conformance binding.
The generated register-view check is the filesystem conformance binding, so a
Security review must keep its YAML source and generated Markdown/CSV views in
sync before publication. The exact source-diff command remains supporting
validation rather than a second conformance binding.
