from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

import yaml

from .repo_checker import audit_all as audit_repos
from .report import write_reports
from .site_checker import audit_all as audit_sites


def _cmd_audit(args: argparse.Namespace) -> int:
    targets = yaml.safe_load(Path(args.targets).read_text()) or {}
    sites = targets.get("sites") or []
    repos = targets.get("repos") or []

    print(f"Auditing {len(sites)} site(s) and {len(repos)} repo(s)...", file=sys.stderr)
    site_results = asyncio.run(audit_sites(sites))
    repo_results = audit_repos(repos)
    path = write_reports(site_results, repo_results, Path(args.reports_dir))
    print(f"Wrote {path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="compliance")
    sub = parser.add_subparsers(dest="cmd", required=True)

    audit = sub.add_parser("audit", help="Run a full compliance audit")
    audit.add_argument("--targets", default="targets.yaml")
    audit.add_argument("--reports-dir", default="compliance-reports")
    audit.set_defaults(func=_cmd_audit)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
