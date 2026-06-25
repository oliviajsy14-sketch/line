from datetime import UTC, datetime

from trend_archive_agent.agent import ArchiveAgent, TrendReport


def test_offline_archive_writes_json_and_markdown(tmp_path):
    report = TrendReport(
        title="Sample",
        organization="Org",
        url="https://example.com",
        published=str(datetime.now(UTC).date()),
        topics=["AI"],
        summary="Summary",
    )
    result = ArchiveAgent([report]).run(tmp_path, days=1, offline=True)

    assert result.json_path.exists()
    assert result.markdown_path.exists()
    assert "Sample" in result.markdown_path.read_text(encoding="utf-8")
    assert result.reports[0].reachable is None
