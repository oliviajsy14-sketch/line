# Global IT Trend Report Archiving Agent

A small runnable Python agent that discovers public global IT trend reports, extracts report metadata, and archives the results as JSON and Markdown.

## Run

```bash
python -m trend_archive_agent --days 30 --out archive
```

Use `--offline` to generate an archive from built-in seed reports without network access:

```bash
python -m trend_archive_agent --offline --out archive
```

## Output

Each run creates:

- `archive/reports.json`: structured report metadata
- `archive/report_index.md`: human-readable report index with topics and link status

## Configuration

Create a JSON file and pass it with `--config` to add or replace seed sources:

```json
{
  "reports": [
    {
      "title": "Example IT Trend Report",
      "organization": "Example Research",
      "url": "https://example.com/report",
      "published": "2026-01-15",
      "topics": ["AI", "Cloud"],
      "summary": "Short report summary"
    }
  ]
}
```
