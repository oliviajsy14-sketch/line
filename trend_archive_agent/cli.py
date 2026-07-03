"""Command line interface for the trend report archiving agent."""

from __future__ import annotations

import argparse
from pathlib import Path

from .agent import ArchiveAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Archive global IT trend report metadata as JSON and Markdown."
    )
    parser.add_argument("--out", default="archive", help="Output directory for archive files.")
    parser.add_argument("--config", help="Optional JSON config containing report seed data.")
    parser.add_argument("--days", type=int, default=365, help="Only include reports newer than this many days.")
    parser.add_argument("--offline", action="store_true", help="Do not validate report URLs over the network.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    agent = ArchiveAgent.from_config(args.config)
    result = agent.run(output_dir=Path(args.out), days=args.days, offline=args.offline)
    print(f"Archived {len(result.reports)} reports to {result.output_dir}")
    print(f"JSON: {result.json_path}")
    print(f"Markdown: {result.markdown_path}")
    return 0
