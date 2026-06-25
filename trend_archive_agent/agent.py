"""Core archive workflow for global IT trend reports."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Iterable
from urllib.error import URLError
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class TrendReport:
    title: str
    organization: str
    url: str
    published: str
    topics: list[str]
    summary: str
    reachable: bool | None = None

    @property
    def published_date(self) -> date:
        return date.fromisoformat(self.published)


@dataclass(frozen=True)
class ArchiveResult:
    output_dir: Path
    json_path: Path
    markdown_path: Path
    reports: list[TrendReport]


DEFAULT_REPORTS = [
    TrendReport(
        title="Tech Trends 2026",
        organization="Info-Tech Research Group",
        url="https://www.infotech.com/research/ss/tech-trends-2026",
        published="2025-10-01",
        topics=["AI", "IT strategy", "Governance"],
        summary="Annual technology trends report covering enterprise adoption priorities and risks.",
    ),
    TrendReport(
        title="2026 Work Trend Index Annual Report",
        organization="Microsoft",
        url="https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization",
        published="2026-05-06",
        topics=["AI agents", "Future of work", "Productivity"],
        summary="Research on AI agents, organizational readiness, and human agency at work.",
    ),
    TrendReport(
        title="Global Tech Report",
        organization="KPMG",
        url="https://kpmg.com/xx/en/our-insights/ai-and-technology/global-tech-report.html",
        published="2026-01-01",
        topics=["AI", "Digital transformation", "Technology leadership"],
        summary="Global technology leadership perspectives on emerging technology adoption.",
    ),
]


class ArchiveAgent:
    """Collects, validates, filters, and writes trend-report archive files."""

    def __init__(self, reports: Iterable[TrendReport]) -> None:
        self.reports = list(reports)

    @classmethod
    def from_config(cls, config_path: str | None = None) -> "ArchiveAgent":
        if not config_path:
            return cls(DEFAULT_REPORTS)

        raw = json.loads(Path(config_path).read_text(encoding="utf-8"))
        reports = [TrendReport(**item) for item in raw.get("reports", [])]
        return cls(reports)

    def run(self, output_dir: Path, days: int, offline: bool = False) -> ArchiveResult:
        output_dir.mkdir(parents=True, exist_ok=True)
        cutoff = datetime.now(UTC).date() - timedelta(days=days)
        filtered = [report for report in self.reports if report.published_date >= cutoff]
        checked = [self._with_reachability(report, offline=offline) for report in filtered]
        checked.sort(key=lambda report: (report.published, report.organization, report.title), reverse=True)

        json_path = output_dir / "reports.json"
        markdown_path = output_dir / "report_index.md"
        json_path.write_text(self._to_json(checked), encoding="utf-8")
        markdown_path.write_text(self._to_markdown(checked), encoding="utf-8")
        return ArchiveResult(output_dir=output_dir, json_path=json_path, markdown_path=markdown_path, reports=checked)

    def _with_reachability(self, report: TrendReport, offline: bool) -> TrendReport:
        if offline:
            return TrendReport(**{**asdict(report), "reachable": None})

        request = Request(report.url, method="HEAD", headers={"User-Agent": "trend-archive-agent/0.1"})
        try:
            with urlopen(request, timeout=8) as response:
                reachable = 200 <= response.status < 400
        except (OSError, URLError, ValueError):
            reachable = False
        return TrendReport(**{**asdict(report), "reachable": reachable})

    def _to_json(self, reports: list[TrendReport]) -> str:
        return json.dumps([asdict(report) for report in reports], ensure_ascii=False, indent=2) + "\n"

    def _to_markdown(self, reports: list[TrendReport]) -> str:
        lines = ["# Global IT Trend Report Archive", ""]
        if not reports:
            lines.extend(["No reports matched the selected date window.", ""])
            return "\n".join(lines)

        for report in reports:
            status = "not checked" if report.reachable is None else "reachable" if report.reachable else "unreachable"
            topics = ", ".join(report.topics)
            lines.extend(
                [
                    f"## {report.title}",
                    "",
                    f"- Organization: {report.organization}",
                    f"- Published: {report.published}",
                    f"- Topics: {topics}",
                    f"- URL: {report.url}",
                    f"- Link status: {status}",
                    "",
                    report.summary,
                    "",
                ]
            )
        return "\n".join(lines)
