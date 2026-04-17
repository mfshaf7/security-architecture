#!/usr/bin/env python3
"""Render findings and risk register views from remediation inventory."""

from __future__ import annotations

import argparse
import csv
from io import StringIO
from pathlib import Path
import sys

import yaml


FINDINGS_HEADER = (
    "| Finding ID | Title | Severity | Likelihood | Affected Assets | Owner | Status | "
    "Target Date | Risk ID | Workstream |\n"
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
)
RISKS_HEADER = (
    "| Risk ID | Title | Severity | Likelihood | Status | Owner | Treatment | Residual Risk | "
    "Related Findings | Target Workstream |\n"
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
)
GENERATED_NOTICE = (
    "<!-- Generated from registers/remediation-inventory.yaml by "
    "scripts/render_register_views.py. Do not hand-edit. -->\n\n"
)


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def join_list(values: list[str]) -> str:
    return ", ".join(values)


def render_findings_markdown(findings: dict) -> str:
    lines = [GENERATED_NOTICE, "# Findings Register\n\n", FINDINGS_HEADER]
    for finding_id in sorted(findings):
        entry = findings[finding_id]
        lines.append(
            "| {id} | {title} | {severity} | {likelihood} | {assets} | {owner} | {status} | {target_date} | {risk_id} | {workstream} |\n".format(
                id=finding_id,
                title=entry["title"],
                severity=entry["severity"],
                likelihood=entry["likelihood"],
                assets=join_list(entry["affected_assets"]),
                owner=entry["owner"],
                status=str(entry["status"]).capitalize(),
                target_date=entry["target_date"],
                risk_id=entry["risk_id"],
                workstream=entry["workstream"],
            )
        )
    return "".join(lines)


def render_risks_markdown(risks: dict) -> str:
    lines = [GENERATED_NOTICE, "# Risk Register\n\n", RISKS_HEADER]
    for risk_id in sorted(risks):
        entry = risks[risk_id]
        lines.append(
            "| {id} | {title} | {severity} | {likelihood} | {status} | {owner} | {treatment} | {residual_risk} | {related_findings} | {workstream} |\n".format(
                id=risk_id,
                title=entry["title"],
                severity=entry["severity"],
                likelihood=entry["likelihood"],
                status=str(entry["status"]).capitalize(),
                owner=entry["owner"],
                treatment=entry["treatment"],
                residual_risk=entry["residual_risk"],
                related_findings=join_list(entry["related_findings"]),
                workstream=entry["workstream"],
            )
        )
    return "".join(lines)


def render_findings_csv(findings: dict) -> str:
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(
        [
            "Finding ID",
            "Title",
            "Severity",
            "Likelihood",
            "Affected Assets",
            "Owner",
            "Status",
            "Target Date",
            "Risk ID",
            "Workstream",
        ]
    )
    for finding_id in sorted(findings):
        entry = findings[finding_id]
        writer.writerow(
            [
                finding_id,
                entry["title"],
                entry["severity"],
                entry["likelihood"],
                "; ".join(entry["affected_assets"]),
                entry["owner"],
                str(entry["status"]).capitalize(),
                entry["target_date"],
                entry["risk_id"],
                entry["workstream"],
            ]
        )
    return output.getvalue()


def render_risks_csv(risks: dict) -> str:
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(
        [
            "Risk ID",
            "Title",
            "Severity",
            "Likelihood",
            "Status",
            "Owner",
            "Treatment",
            "Residual Risk",
            "Related Findings",
            "Target Workstream",
        ]
    )
    for risk_id in sorted(risks):
        entry = risks[risk_id]
        writer.writerow(
            [
                risk_id,
                entry["title"],
                entry["severity"],
                entry["likelihood"],
                str(entry["status"]).capitalize(),
                entry["owner"],
                entry["treatment"],
                entry["residual_risk"],
                "; ".join(entry["related_findings"]),
                entry["workstream"],
            ]
        )
    return output.getvalue()


def generated_views(repo_root: Path) -> dict[Path, str]:
    inventory = load_yaml(repo_root / "registers" / "remediation-inventory.yaml")
    findings = inventory.get("findings") or {}
    risks = inventory.get("risks") or {}
    return {
        repo_root / "registers" / "findings-register.md": render_findings_markdown(findings),
        repo_root / "registers" / "risk-register.md": render_risks_markdown(risks),
        repo_root / "registers" / "csv" / "findings-register.csv": render_findings_csv(findings),
        repo_root / "registers" / "csv" / "risk-register.csv": render_risks_csv(risks),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    outputs = generated_views(repo_root)

    if args.check:
        mismatches = []
        for path, expected in outputs.items():
            if not path.exists():
                mismatches.append(f"missing generated register view: {path}")
                continue
            actual = path.read_text()
            if actual != expected:
                mismatches.append(f"generated register view out of date: {path}")
        if mismatches:
            for mismatch in mismatches:
                print(f"ERROR: {mismatch}")
            return 1
        print("generated register views are current")
        return 0

    for path, content in outputs.items():
        path.write_text(content)
        print(f"rendered {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
