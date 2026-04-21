#!/usr/bin/env python3
"""Render human-facing register views from security evidence inventories."""

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
REVIEWS_HEADER = (
    "| Entry Type | Entry | Owner Repo | Scope | Baseline Review | Baseline Due | "
    "Baseline Decision | Latest Change Review | Latest Status | Latest Decision | Review Areas | Review Trigger IDs |\n"
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
)
ASSESSMENTS_HEADER = (
    "| Assessment | Scope | Status | Reviewed On | Review Due | Reviewers | Path |\n"
    "| --- | --- | --- | --- | --- | --- | --- |\n"
)


def generated_notice(source_path: str) -> str:
    return (
        f"<!-- Generated from {source_path} by "
        "scripts/render_register_views.py. Do not hand-edit. -->\n\n"
    )


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def join_list(values: list[str]) -> str:
    return ", ".join(values)


def render_findings_markdown(findings: dict) -> str:
    lines = [
        generated_notice("registers/remediation-inventory.yaml"),
        "# Findings Register\n\n",
        FINDINGS_HEADER,
    ]
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
    lines = [
        generated_notice("registers/remediation-inventory.yaml"),
        "# Risk Register\n\n",
        RISKS_HEADER,
    ]
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


def review_rows(review_inventory: dict) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    inventory = review_inventory.get("review_inventory") or {}
    for entry_type in ("repos", "products", "components"):
        for entry_name, entry in sorted((inventory.get(entry_type) or {}).items()):
            baseline = entry.get("baseline_review") or {}
            latest = entry.get("latest_change_review") or {}
            rows.append(
                {
                    "entry_type": entry_type[:-1],
                    "entry_name": entry_name,
                    "owner_repo": entry.get("owner_repo", ""),
                    "scope": entry.get("scope", ""),
                    "baseline_path": baseline.get("path", ""),
                    "baseline_reviewed_on": str(baseline.get("reviewed_on", "")),
                    "baseline_review_due_on": str(baseline.get("review_due_on", "")),
                    "baseline_status": str(baseline.get("status", "")),
                    "baseline_decision": str(baseline.get("decision", "")),
                    "latest_path": latest.get("path", ""),
                    "latest_reviewed_on": str(latest.get("reviewed_on", "")),
                    "latest_status": str(latest.get("status", "")),
                    "latest_decision": str(latest.get("decision", "")),
                    "review_areas": join_list(latest.get("review_areas") or []),
                    "review_trigger_ids": join_list(latest.get("review_trigger_ids") or []),
                    "owner_artifacts": join_list(
                        [
                            f"{artifact.get('repo')}/{artifact.get('path')}"
                            for artifact in (latest.get("owner_artifacts") or [])
                        ]
                    ),
                }
            )
    return rows


def render_review_inventory_markdown(review_inventory: dict) -> str:
    lines = [
        generated_notice("registers/review-inventory.yaml"),
        "# Review Inventory\n\n",
        REVIEWS_HEADER,
    ]
    for row in review_rows(review_inventory):
        lines.append(
            "| {entry_type} | {entry_name} | {owner_repo} | {scope} | {baseline_path} | {baseline_review_due_on} | {baseline_decision} | {latest_path} | {latest_status} | {latest_decision} | {review_areas} | {review_trigger_ids} |\n".format(
                **row
            )
        )
    return "".join(lines)


def render_review_inventory_csv(review_inventory: dict) -> str:
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(
        [
            "Entry Type",
            "Entry",
            "Owner Repo",
            "Scope",
            "Baseline Review Path",
            "Baseline Reviewed On",
            "Baseline Review Due On",
            "Baseline Status",
            "Baseline Decision",
            "Latest Change Review Path",
            "Latest Change Reviewed On",
            "Latest Change Status",
            "Latest Change Decision",
            "Review Areas",
            "Review Trigger IDs",
            "Owner Artifacts",
        ]
    )
    for row in review_rows(review_inventory):
        writer.writerow(
            [
                row["entry_type"],
                row["entry_name"],
                row["owner_repo"],
                row["scope"],
                row["baseline_path"],
                row["baseline_reviewed_on"],
                row["baseline_review_due_on"],
                row["baseline_status"],
                row["baseline_decision"],
                row["latest_path"],
                row["latest_reviewed_on"],
                row["latest_status"],
                row["latest_decision"],
                row["review_areas"],
                row["review_trigger_ids"],
                row["owner_artifacts"],
            ]
        )
    return output.getvalue()


def assessment_rows(assessment_inventory: dict) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for assessment_name, entry in sorted(
        (assessment_inventory.get("assessment_inventory") or {}).items()
    ):
        rows.append(
            {
                "assessment_name": assessment_name,
                "scope": entry.get("scope", ""),
                "status": str(entry.get("status", "")),
                "reviewed_on": str(entry.get("reviewed_on", "")),
                "review_due_on": str(entry.get("review_due_on", "")),
                "reviewers": join_list(entry.get("reviewers") or []),
                "path": entry.get("path", ""),
            }
        )
    return rows


def render_assessment_inventory_markdown(assessment_inventory: dict) -> str:
    lines = [
        generated_notice("registers/assessment-inventory.yaml"),
        "# Assessment Inventory\n\n",
        ASSESSMENTS_HEADER,
    ]
    for row in assessment_rows(assessment_inventory):
        lines.append(
            "| {assessment_name} | {scope} | {status} | {reviewed_on} | {review_due_on} | {reviewers} | {path} |\n".format(
                **row
            )
        )
    return "".join(lines)


def render_assessment_inventory_csv(assessment_inventory: dict) -> str:
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(
        [
            "Assessment",
            "Scope",
            "Status",
            "Reviewed On",
            "Review Due On",
            "Reviewers",
            "Path",
        ]
    )
    for row in assessment_rows(assessment_inventory):
        writer.writerow(
            [
                row["assessment_name"],
                row["scope"],
                row["status"],
                row["reviewed_on"],
                row["review_due_on"],
                row["reviewers"],
                row["path"],
            ]
        )
    return output.getvalue()


def generated_views(repo_root: Path) -> dict[Path, str]:
    inventory = load_yaml(repo_root / "registers" / "remediation-inventory.yaml")
    review_inventory = load_yaml(repo_root / "registers" / "review-inventory.yaml")
    assessment_inventory = load_yaml(repo_root / "registers" / "assessment-inventory.yaml")
    findings = inventory.get("findings") or {}
    risks = inventory.get("risks") or {}
    return {
        repo_root / "registers" / "findings-register.md": render_findings_markdown(findings),
        repo_root / "registers" / "risk-register.md": render_risks_markdown(risks),
        repo_root / "registers" / "review-inventory.md": render_review_inventory_markdown(review_inventory),
        repo_root / "registers" / "assessment-inventory.md": render_assessment_inventory_markdown(assessment_inventory),
        repo_root / "registers" / "csv" / "findings-register.csv": render_findings_csv(findings),
        repo_root / "registers" / "csv" / "risk-register.csv": render_risks_csv(risks),
        repo_root / "registers" / "csv" / "review-inventory.csv": render_review_inventory_csv(review_inventory),
        repo_root / "registers" / "csv" / "assessment-inventory.csv": render_assessment_inventory_csv(assessment_inventory),
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
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        print(f"rendered {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
