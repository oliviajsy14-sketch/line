# Weekly Tech News Research Agent: Combined Runbook

You are the executing agent. When you are asked to run the weekly pipeline for a date range, follow this runbook end to end: collect that week's real news and write the two output files in Section 1 (the HTML report and the JSON data file). This file is your instructions, not the report itself. Section 0 says exactly what a run does.

**Purpose.** In one run, for a fixed list of master queries grouped into six categories over a given week, collect news article links from primary sources, Google News, and secondary sources (trusted news sites); group links covering the same event into clusters; render each cluster as one row (Select, Headline, Tier, Sources, Date) in a static `Weekly Tech News Article List` HTML report, with n/a evidence preserved in validation/JSON after full search completion; and remove any story already covered last week.

The pipeline runs in seven phases (0 to 6): set up the run, collect and headline from primary sources, then secondary sources, then Google News, arrange each master query's stories by tier, mark empty queries n/a, and drop repeats. Headlines are written during collection, one per cluster. Collection uses the `web_search` and `web_fetch` tools. The deliverable is one self-contained `report_{since}_{until}.html`, rendered from a machine-readable `data_{since}_{until}.json` that also serves as next week's dedup memory; both are written by Python. See Section 0 for how to run it on Claude Code.

> This runbook merges two prior specs into one. The master query list comes from the canonical runbook; the per-query source maps in Section 4 are the union of both specs' links (deduped). The procedure has since been rearranged into the seven-phase flow in Section 4, and Section 3d defines the four-tier classification. There is one Query List, one HTML report, and one JSON data file. Weekly and Global are **not** split.

---

## ONE-SHOT EXECUTION INSTRUCTION

When this runbook is executed by Codex, Claude Code, or any coding agent, do not only summarize this document.

You must perform the full execution workflow:

1. Check whether crawler.py exists.
2. If crawler.py does not exist, create it from this runbook.
3. If crawler.py exists, inspect and update it so it fully follows this runbook.
4. Ensure the crawler can:
   - load all additional_source_url_pool entries
   - run Google News RSS queries for US/KR/JP/Global
   - discover RSS/feed endpoints
   - discover sitemap/news sitemap URLs
   - crawl direct newsroom/blog pages
   - use site: search fallback
   - use Playwright for JS-heavy sources when available
   - generate final HTML and JSON outputs

5. Do not sample additional_source_url_pool.
6. Iterate through every source URL.
7. Add diagnostic counters:
   - loaded source count
   - Google News query count
   - raw collected count
   - after date filter count
   - after AI filter count
   - after dedupe count
   - final visible row count

8. If the final visible row count is below 200, do not stop immediately.
   First expand:
   - Google News query variants
   - source-specific RSS discovery
   - sitemap discovery
   - site: query fallback
   - Playwright rendering for JS-heavy sources

9. Only mark the run incomplete after all collection routes have been attempted.

10. After updating or creating crawler.py, run:

python3 crawler.py --since {START_DATE} --until {END_DATE}

11. Generate:
   - report_{START_DATE}_{END_DATE}.html
   - data_{START_DATE}_{END_DATE}.json
   - diagnostics_{START_DATE}_{END_DATE}.json

12. Final output must include the HTML report path and diagnostics summary.

## 0. How to run on Claude Code

### What a run produces (read this first)
Running this runbook is an action, not a document conversion. When you are asked to run it for a date range, you collect that week's real news with `web_search` and `web_fetch`, follow Phases 0 to 6, and write two files:
- `./output/report_{since}_{until}.html`: the deliverable the desk reads. You build it by filling the ready-made template in Section 6 with this week's stories.
- `./output/data_{since}_{until}.json`: the machine-readable records, and next week's dedup memory.

Do not convert this runbook itself into HTML. This file is the instructions; the report is generated from collected news. If you find yourself turning these section titles (`0. How to run`, `1. Output`, `2. Headline format`, and so on) into a web page, stop, that is the wrong output.

### Invocation
1. Put this file and its helper folders in one project directory, then start Claude Code in that directory.
2. Run it one of two ways:
   - Slash command: `/weekly-news <since> <until>` (for example `/weekly-news 2026-06-17 2026-06-23`). The command file is at `.claude/commands/weekly-news.md`.
   - Or just tell Claude Code: "Execute this runbook for <since> to <until>."
3. If you pass no dates, use the `time_period` in Section 3a. Dates are inclusive.
4. Date input: ISO `YYYY-MM-DD` is canonical. A human may also type the range as `yyyy.m.d~yyyy.m.d` (no zero-padding, no slashes, for example `2026.6.17~2026.6.23`); normalize it to ISO before use. Inclusive both ends; do not extend past the end date.
5. Optional: rename this file to `CLAUDE.md` so Claude Code auto-loads it as context every session.

### Weekly run command
For a one-line weekly run, create `.claude/commands/weekly-news.md` with the text below, then each week run `/weekly-news 2026-06-17 2026-06-23` with your dates.

```text
Execute the runbook in this project (the Weekly Tech News Research Agent) for the dates: $ARGUMENTS.
Treat $ARGUMENTS as "<since> <until>" in ISO YYYY-MM-DD, inclusive of both ends.
Collect that week's news, follow Phases 0 to 6, and write ./output/report_<since>_<until>.html and ./output/data_<since>_<until>.json.
Do NOT convert this runbook to HTML. Generate the report from collected news by filling the Section 6 template.
```

### Tools you use
- **Collection (no live browser).** Use `web_search` and `web_fetch`. You cannot drive Google News in a real browser, so map the browser steps to:
  - Google News RSS per edition (date-filterable, returns clean article lists). Fetch each with `web_fetch`:
    - US / en: `https://news.google.com/rss/search?q={QUERY}+after:{since}+before:{until_plus_1}&hl=en-US&gl=US&ceid=US:en`
    - KR / ko: same URL with `hl=ko&gl=KR&ceid=KR:ko`
    - JP / ja: same URL with `hl=ja&gl=JP&ceid=JP:ja`
    - `before:` is exclusive, so pass `until + 1 day`. URL-encode the query (Korean and Japanese names included).
    - RSS items are Google redirect links. **Efficiency: do not resolve every redirect.** Cluster and dedup on the RSS titles/snippets first, then resolve to the real publisher URL only for the links you actually keep, so the URL cells hold real article links.
  - `web_fetch` on the Phase 1 source pages (newsrooms, blogs, GitHub releases, changelogs) listed in Section 4.
  - `web_search` as the fallback, and for the Phase 2 secondary sites, using `site:` filters plus the date window in the query.
  - This is best-effort. Note what each query actually returned.
- **Report and data I/O.** Write a Python script (run with bash) that builds the two output files in Section 1 from the same final records: the full machine-readable `data_{since}_{until}.json` and the clean user-facing `report_{since}_{until}.html`. No Excel, no `openpyxl`. The HTML is one file with inline CSS and JS, declares `<meta charset="utf-8">`, uses a CJK-capable font stack so Korean and Japanese render, contains static pre-rendered article rows in the DOM at build time, and includes working checkbox controls. Validation data belongs in JSON unless explicitly requested in HTML.
- **Filesystem.** Keep all working state in the project directory.

### Files and I/O contract
- Deliverable: `./output/report_{since}_{until}.html`, one self-contained HTML file (Section 1a): a clean article-selection list with expanded article coverage, no verbose validation/audit tables by default, static pre-rendered article HTML rows, and working checkbox controls.
- Data file: `./output/data_{since}_{until}.json`, the full machine-readable data (Section 1b): kept clusters, n/a audit records, validation logs, source-check evidence, crawl manifest, and dedup memory. The report and data file are built from the same final records.
- Archive: after the run, copy the data file to `./archive/data_{since}_{until}.json`.
- Previous week: Phase 6 reads `previous_week.data_path` (Section 3a), the prior week's archived data file. If it does not exist, skip the repetition drop and note it.
- Selections: the desk ticks rows in the report; ticks autosave in the browser, and an "Export selections" button downloads `selections_{since}_{until}.json` for a later step. No fixed schema yet (Section 1a).
- Create `./output/` and `./archive/` if missing.

### Execution loop
- Process one category at a time, fully through Phases 0 to 6, before the next. Order: AI Agent, AI/GPT, Global Big Tech, Asia Big Tech, Social, Theme.
- After each category, append its cluster records to `data_{since}_{until}.json`, so a crash is recoverable. Render the HTML report once at the end from the full data file.
- Do not fabricate URLs, dates, or headlines. A paywalled article is a lead only; prefer an accessible source for the same event.
- Apply the house-style rules in Section 2 to every headline.

---

## 1. Output

Two files: the HTML report (the deliverable) and the JSON data file (machine-readable record and dedup memory).

### 1a. HTML report (the deliverable)

One self-contained static HTML file, `./output/report_{since}_{until}.html`: inline CSS and JS, `<meta charset="utf-8">`, a CJK-capable font stack (for example `system-ui, "Apple SD Gothic Neo", "Noto Sans KR", "Noto Sans JP", sans-serif`), and no external requests. The final HTML must be readable when opened locally as a `file://` file. Keep the HTML title as `Weekly Tech News Article List` and keep the run date range from the source file/run arguments.

The HTML report is a high-coverage **article list/checklist**, not a validation dashboard. It must be regenerated from strengthened collection and validation logic, not just restyled from an earlier sparse HTML. Default visible content should be:
- Header with date range, generated date, and metadata pills for Range, Articles, AI Agent, AI/GPT, Global Big Tech, Asia Big Tech, Social, Theme, and Selected count.
- Category sections in strict order: AI Agent, AI/GPT, Global Big Tech, Asia Big Tech, Social, Theme.
- Master query groups in the exact order defined in Section 3b or the seed HTML; never reorder them ad hoc.
- All surviving article rows under each query; if multiple real articles exist for one query, show them all.
- Selection checkboxes, tier badges, up to three source links, and publish date.

Final row format:
- The visible article table uses exactly these columns: Select, Headline, Tier, Sources, Date.
- The Select cell must contain a real clickable `<input type="checkbox">`; never use a fake button, custom div, or non-clickable element.
- All checkboxes start unchecked.
- Headline shows the Korean title only; do not add an Original Title column.
- Source links use simple labels: `Source 1`, `Source 2`, `Source 3`.
- Date uses `YYYY-MM-DD`; the headline suffix uses `YYYY.M.D` with no zero padding.
- Every visible article row must have at least one real, reachable source URL.

`n/a` is assigned only at the end, after every required official source, source-first media sweep, Google US query, and applicable Asia/local-language query has completed. Do not create temporary n/a rows before collection is complete. Preserve n/a decisions and evidence in `na_audit` or validation JSON. The default HTML should remain article-row centered like the second/reference file; if n/a information is shown, put it only in a small collapsible audit section that does not interrupt the article list.

Do **not** show large validation tables, source-completion manifests, internal crawler logs, every-site crawl manifests, or raw Google query logs in the default HTML. Store validation, source-check evidence, crawl logs, n/a evidence, source manifest, Google search log, and dedup log in JSON or embedded metadata unless the user explicitly asks to display them. Validation data belongs in JSON/metadata unless explicitly requested in HTML.

Article rows must be rendered as static HTML first. JavaScript may enhance checkbox autosave/export, but if JavaScript fails, the article list must still be visible. Do not rely only on `JSON.parse()` rendering for the visible article list. The generated HTML must contain the rendered article rows in the DOM at build time.

Selection checkboxes:
- Ticks autosave in the browser (`localStorage`, keyed by the run dates plus Cluster ID) so a reload does not lose them.
- `Clear checks` clears all checked rows.
- `Export selections` downloads selected full records as JSON, including run dates and full selected records.

Rendering rules:
- One cluster = one row = one Korean headline = up to three source links.
- HTML-escape every dynamic value before injecting it: headlines contain `"` and `[ ]`, and source URLs contain `&`.
- Rows are grouped by category and master query using the strict display order in Section 3b-1.
- The `[Company]` tag in the headline is the owning company and may differ from the master query. Sub-brands roll up to their parent in the headline: `[Meta] Instagram`, `[Meta] WhatsApp`, `[Meta] Facebook`; `[Google] YouTube`, `[Google] Android`, `[Google] Gemini`; `[Kakao] Bank`, `[Kakao] Pay`, `[Kakao] Mobility`. Whole-market and multi-company stories carry `[Market]`.

### 1b. Data file (machine-readable record and dedup memory)

`./output/data_{since}_{until}.json`: the full record the report is rendered from, and the file next week's repetition check (Phase 6) reads. Not shown to readers. Saved every week to the archive path.

One record per cluster, with at least these fields:
- `cluster_id`: stable unique id for the cluster.
- `category`: one of the six categories.
- `master_query`: the owning master query.
- `company`: the owning company tag (the parent for sub-brands), or `Market`.
- `headline`: the Section 2 headline string.
- `tier`: 1, 2, or 3.
- `sources`: the up-to-three source URLs, ordered primary, then secondary, then Google News.
- `date`: the cluster date, `YYYY-MM-DD`.
- `source_headlines`, `source_dates`: per-source titles and publish dates.
- `article_texts`: the opened article text, used only for the Phase 6 same-event comparison.
- `dedup_status`: `keep` or `drop` (set in Phase 6).

---

## 2. Headline format

Pattern: `[Company] {one-line summary} (YYYY.M.D)`

- Bracket tag = owning company, in English (`[Meta]`, `[Apple]`, `[Netflix]`), or `[Market]` for market-level stories.
- Code-switched style: keep product names, feature names, company names, and technical or industry terms in English; use Korean for the grammatical glue and framing (as in `cohosting으로 공동 event planning과 party management 지원`).
- One dense line, comma-separated clauses, no terminal period.
- Capture the single most important and relevant point of the cluster, judged against LINE's strategic interests.
- Date in parentheses at the end, format `YYYY.M.D` (no zero-padding).
- House style: never use 에이전트 or 에이전틱, always English capitalized `Agent` / `Agentic`; replace the multiplier 배 with `x` (2.1배 -> 2.1x, 10배 -> 10x); KMBT for large numbers; YoY format; no em dashes.
- New feature/service names get double quotes when shipped (GA, public beta, or officially announced/upcoming). Do **not** quote internal/closed tests, rumors, updates or expansions of existing features, or button names.
- Target length: 120 Korean characters or fewer per headline.
- For the writing process (when to write, which source to base each headline on, clustering and dedup), follow the headline rule in Section 3f.

Examples (the one and only output format, used for all six categories):
- `[Anthropic] Claude Tag의 "Agent Identity" 공개, 팀 단위 AI Agent 접근 권한 모델 제시 (2026.6.24)`
- `[Meta] WhatsApp, Chats 탭 상단에 Status 캐러셀 통합 테스트하며 메시징 내 콘텐츠 소비 확장 추진 (2026.4.9)`
- `[Google] AI Edge Gallery, Apple App Store 생산성 앱 Top10 진입하며 On-device AI 수요 확대 신호 확인 (2026.4.6)`

---

## 3. Configuration and selection rules

### 3a. Run settings

```yaml
time_period:
  since: "2026-06-17"     # inclusive (ISO; accept yyyy.m.d~yyyy.m.d human input and normalize)
  until: "2026-06-23"     # inclusive
  cadence: weekly

ranking:                    # within each master query: arrange by tier (Section 3d)
  scope: per_master_query
  method: tiers             # Tier 1 highest, then Tier 2, then Tier 3
  drop: tier_4_only         # Tier 4 dropped; Tiers 1-3 written, ordered by tier

google_news:                       # Phase 3; see the trigger cluster size rule (Section 3f)
  editions: ["US / en", "KR / ko", "JP / ja"]   # search all three; Asian queries also search the local-language name
  sort: relevance
  max_results: 100                 # about 100 results per query
  trigger_cluster_size:
    threshold: 0.50                # if >50% of a query's Google hits only repeat Phase 1-2 coverage
    action: boolean_negate         # re-search with the dominant repeated term negated (e.g. Claude -Fable)
    max_results: 100

# Secondary sources: original-reporting outlets, across four languages so coverage
# matches the categories. See Phase 2 for which outlets to weight per category.
trusted_news_sites:
  # Global English: AI Agent, AI/GPT, Global Big Tech, Social, business
  - techcrunch.com
  - theverge.com
  - arstechnica.com
  - wired.com
  - engadget.com
  - axios.com
  - reuters.com
  - bloomberg.com
  - theinformation.com
  - venturebeat.com
  - siliconangle.com
  - the-decoder.com
  - marktechpost.com
  - socialmediatoday.com
  - 9to5mac.com
  - 9to5google.com
  # Asia-focused English: Asia Big Tech, super apps, Theme
  - restofworld.org
  - techinasia.com
  - kr-asia.com
  - scmp.com
  # Korean: Asia Big Tech (Kakao, Coupang, Toss), Korea AI
  - zdnet.co.kr
  - etnews.com
  - bloter.net
  - platum.kr
  - thebell.co.kr
  # Japanese: Asia Big Tech (Rakuten, DeNA, Mercari, Gree)
  - itmedia.co.jp
  - watch.impress.co.jp
  - ascii.jp
  - japan.cnet.com
  - asia.nikkei.com
  # Chinese: Asia Big Tech (Tencent, ByteDance, Alibaba)
  - technode.com
  - 36kr.com
  - caixinglobal.com

# Additional source URL pool supplied for broad coverage expansion.
# Duplicates already present elsewhere in this runbook were omitted by canonical host.
additional_source_url_pool:
  - https://247wallst.com/
  - https://abhs.in/
  - https://aboutamazon.eu/
  - https://aboutcoupang.com/
  - https://adweek.com/
  - https://aitimes.com/
  - https://ajunews.com/
  - https://aljazeera.com/
  - https://alphabiz.co.kr/
  - https://androidauthority.com/
  - https://appliedclinicaltrialsonline.com/
  - https://arise.tv/
  - https://asiabusinessoutlook.com/
  - https://asiae.co.kr/
  - https://asianews.network/
  - https://asiatoday.co.kr/
  - https://atptour.com/
  - https://auckland.ac.nz/
  - https://autos.yahoo.com/
  - https://azure.microsoft.com/
  - https://bain.com/
  - https://bbc.com/
  - https://bbntimes.com/
  - https://beckershospitalreview.com/
  - https://benzinga.com/
  - https://bereal.com/
  - https://betanews.com/
  - https://betanews.net/
  - https://beyondpost.co.kr/
  - https://bgr.com/
  - https://biz.chosun.com/
  - https://biz.heraldcorp.com/
  - https://biz.sbs.co.kr/
  - https://bizjournals.com/
  - https://blogs.cisco.com/
  - https://blogs.nvidia.com/
  - https://blogs.oracle.com/
  - https://bmmagazine.co.uk/
  - https://business.nikkei.com/
  - https://businesspost.co.kr/
  - https://businesstimes.com.sg/
  - https://businesswire.com/
  - https://ca.style.yahoo.com/
  - https://calcalistech.com/
  - https://carnewschina.com/
  - https://caspiannews.com/
  - https://cast.ai/
  - https://chinadaily.com.cn/
  - https://chosun.com/
  - https://civicnews.com/
  - https://cmu.edu/
  - https://cnbc.com/
  - https://code.claude.com/
  - https://contentgrip.com/
  - https://cryptobriefing.com/
  - https://customerthink.com/
  - https://dailian.co.kr/
  - https://daily.hankooki.com/
  - https://dataeconomy.co.kr/
  - https://davincicommerce.ai/
  - https://ddaily.co.kr/
  - https://decrypt.co/
  - https://defensescoop.com/
  - https://deloitte.com/
  - https://digitaltoday.co.kr/
  - https://digitaltrends.com/
  - https://digitimes.com/
  - https://docs.lovable.dev/
  - https://dronexl.co/
  - https://ebn.co.kr/
  - https://economictimes.indiatimes.com/
  - https://economist.co.kr/
  - https://econovill.com/
  - https://edaily.co.kr/
  - https://edition.cnn.com/
  - https://edtechinnovationhub.com/
  - https://edweek.org/
  - https://einnews.com/
  - https://en.sedaily.com/
  - https://en.tmtpost.com/
  - https://enewstoday.co.kr/
  - https://english.elpais.com/
  - https://etnews.com/
  - https://eu.36kr.com/
  - https://euronews.com/
  - https://expressnews.com/
  - https://facebook.com/
  - https://finance.biggo.com/
  - https://finance.yahoo.com/
  - https://finomy.com/
  - https://finovate.com/
  - https://fintech.ca/
  - https://firefox.com/
  - https://firstpost.com/
  - https://forbes.com/
  - https://fortune.com/
  - https://fox10phoenix.com/
  - https://ftoday.co.kr/
  - https://gamespew.com/
  - https://gmasia.ai/
  - https://googlecloudpresscorner.com/
  - https://governor.mo.gov/
  - https://greened.kr/
  - https://gurufocus.com/
  - https://hankyung.com/
  - https://hcamag.com/
  - https://help.twitch.tv/
  - https://hollywoodreporter.com/
  - https://hpcwire.com/
  - https://hsph.harvard.edu/
  - https://hypebot.com/
  - https://iconsumer.or.kr/
  - https://idnfinancials.com/
  - https://imnews.imbc.com/
  - https://inc.com/
  - https://inews24.com/
  - https://infoq.com/
  - https://infostockdaily.co.kr/
  - https://insidermonkey.com/
  - https://inspirepreneurmagazine.com/
  - https://japan.cnet.com/
  - https://jejumaeil.net/
  - https://jp.merpay.com/
  - https://kalinga.ai/
  - https://ket.kr/
  - https://kharon.com/
  - https://knpp.co.kr/
  - https://korea.kr/
  - https://koreapost.com/
  - https://kqed.org/
  - https://kz.kursiv.media/
  - https://ladbible.com/
  - https://latimes.com/
  - https://lawissue.co.kr/
  - https://lcnews.co.kr/
  - https://letsdatascience.com/
  - https://library.hbs.edu/
  - https://linuxfoundation.org/
  - https://linuxiac.com/
  - https://lkp.news/
  - https://m.joseilbo.com/
  - https://m.za.investing.com/
  - https://machinelearning.apple.com/
  - https://macrumors.com/
  - https://manilastandard.net/
  - https://marketbeat.com/
  - https://marketplacepulse.com/
  - https://mediaplaynews.com/
  - https://mentalfloss.com/
  - https://mezha.ua/
  - https://minimax.io/
  - https://mk.co.kr/
  - https://mlive.com/
  - https://mobile.newsis.com/
  - https://moneytalksnews.com/
  - https://moomoo.com/
  - https://morningbrew.com/
  - https://mp.weixin.qq.com/
  - https://mt.co.kr/
  - https://munhwa.com/
  - https://namdonews.com/
  - https://nbcnews.com/
  - https://nbnnews.co.kr/
  - https://neowin.net/
  - https://netflix.com/
  - https://news.bbsi.co.kr/
  - https://news.einfomax.co.kr/
  - https://news.mtn.co.kr/
  - https://news.nate.com/
  - https://news.tuoitre.vn/
  - https://news1.kr/
  - https://news18.com/
  - https://newscientist.com/
  - https://newsian.co.kr/
  - https://newspost.kr/
  - https://newsway.co.kr/
  - https://newswire.co.kr/
  - https://nokia.com/
  - https://nypost.com/
  - https://okta.com/
  - https://openads.co.kr/
  - https://orionbrowser.com/
  - https://panewslab.com/
  - https://payment.rakuten.co.jp/
  - https://pcworld.com/
  - https://pocketgamer.biz/
  - https://pointdaily.co.kr/
  - https://press.aboutamazon.com/
  - https://press9.kr/
  - https://prnewswire.com/
  - https://pulse2.com/
  - https://pymnts.com/
  - https://qwen.ai/
  - https://reuters.com/
  - https://roadtovr.com/
  - https://saastr.com/
  - https://sakana.ai/
  - https://salesforce.com/
  - https://scworld.com/
  - https://searchenginejournal.com/
  - https://security.apple.com/
  - https://sedaily.com/
  - https://sentv.co.kr/
  - https://seroundtable.com/
  - https://sg.finance.yahoo.com/
  - https://sisacast.kr/
  - https://sisaplusnews.com/
  - https://snyk.io/
  - https://spokesman.com/
  - https://statista.com/
  - https://stocktitan.net/
  - https://stocktwits.com/
  - https://straightnews.co.kr/
  - https://supermarketnews.com/
  - https://tech.yahoo.com/
  - https://techbuzz.ai/
  - https://techcommunity.microsoft.com/
  - https://techinformed.com/
  - https://techloy.com/
  - https://techpolicy.press/
  - https://techtimes.com/
  - https://techzine.eu/
  - https://thedefiant.io/
  - https://thedispatch.com/
  - https://theesa.com/
  - https://theguardian.com/
  - https://thelec.kr/
  - https://themoscowtimes.com/
  - https://thenextweb.com/
  - https://thestandard.com.hk/
  - https://tmo.report/
  - https://topics.smt.docomo.ne.jp/
  - https://tradingview.com/
  - https://trust3.ai/
  - https://uk.finance.yahoo.com/
  - https://ukstories.microsoft.com/
  - https://v.daum.net/
  - https://variety.com/
  - https://vaticannews.va/
  - https://verint.com/
  - https://viva100.com/
  - https://vogue.com/
  - https://voi.id/
  - https://voix.jp/
  - https://win.gg/
  - https://windowscentral.com/
  - https://womennews.co.kr/
  - https://wpr.org/
  - https://wreg.com/
  - https://x.ai/
  - https://xda-developers.com/
  - https://yahoo.com/
  - https://yna.co.kr/
  - https://yonhapnewstv.co.kr/
  - https://ytn.co.kr/
  - https://z.ai/
  - https://zuora.com/

# Dedup note: omitted 83 supplied URLs because their canonical host already appears elsewhere in this runbook.

# Excluded everywhere: press-release wires and pure aggregators with no original reporting.
site_denylist:
  - prnewswire.com
  - businesswire.com
  - globenewswire.com
  - newswire.com

# Geographic scope. A story outside the priority markets is Tier 2 unless it signals a
# cross-market trend, in which case Tier 1 (Section 3d). There is no hard geography drop.
priority_markets: [Japan, Taiwan, Thailand, Indonesia, Korea, United States, Europe, China]

output:
  report_path: "./output/report_{since}_{until}.html"          # self-contained HTML deliverable (Section 1a)
  data_path: "./output/data_{since}_{until}.json"              # machine-readable record + dedup memory (Section 1b)
  selections_path: "./output/selections_{since}_{until}.json"  # written by the report's Export button; no fixed schema yet
  archive_data_path: "./archive/data_{since}_{until}.json"     # copy of the data file kept each week

previous_week:
  # prior week's archived data file; Phase 6 reads it. Skip the dedup drop if it is missing.
  data_path: "./archive/data_prev_week.json"
```

### 3b. Categories and master queries

Master queries are grouped into six categories. The run processes them in this order, one full category before the next. Per-query Primary and Secondary sources are listed in the source maps in Section 4.

#### 1. AI Agent
All Other AI Agent News, OpenClaw (Moltbot, Clawdbot), Paperclip, BabyAGI, Microsoft AutoGen, AutoGPT, AgentGPT, Claude Cowork, A.(에이닷), KIRA, Wrtn Crack, Rinna, Cotomo, CrewAI, AutoGen, LangGraph, Chai, Nomi, Kindroid, Paradot, Replika, Poketomo, Hume AI, Mersoom, Bot Madang, NVIDIA

#### 2. AI/GPT
All Other AI/GPT News, Lovable, Generative AI, OpenAI, ChatGPT, Codex, Sora, Meta AI, Scale AI, Google AI, Gemini, Veo, NotebookLM, Google Chrome, Amazon AI, Nova AI, Trainium, Anthropic, Claude, Claude Code, Microsoft AI, Microsoft Edge, Bing, Copilot, Apple AI, Safari, Databricks, Thinking Machines Lab, Perplexity AI, Comet, Stability AI, Anysphere (Cursor), ElevenLabs, Speak AI, Writer AI, Ayar Labs, Physical Intelligence, Inflection AI, Moonshot AI, Canva AI, Le Chat, Leonardo AI, Cohere, Skywalker.ai, Kling AI, Seedance, Arc Browser, Dia Browser, Brave Browser, Opera One, Sigma Browser (SigmaOS), Zen Browser, Wavebox, Vivaldi Browser, Sidekick Browser, Shift Browser, Orion Browser, Maxthon Browser, Firefox, Samsung Internet, UC Browser, CryptoTab Browser, AI Startup, Stable Diffusion, DALL-E, Content Generator, Craiyon, Midjourney, MyHeritage, Voice Synthesis, Dream Fusion, AI Bot, AI Healthcare, Image AI, AI Assistant, AI Plugin, Sam Altman, LLM, Inflection AI (Pi), Chatbot, Adobe AI, Adobe Firefly, character.ai, Zeta, MDM, yandex, Kakao Brain, Kakao AI, Japan AI, Korea AI, China AI, US AI, AI Character, Copyright Shield

#### 3. Global Big Tech
Meta, Facebook, Instagram, WhatsApp, Amazon, Amazon Prime, Apple, iOS, Netflix, Google, YouTube, Android, Gmail, Microsoft, Grab

#### 4. Asia Big Tech
Rakuten (楽天市場), note（ノート), DeNA, Gree (グリー), Gunosy (グノシー), Time Tree (タイムツリ), Mercari(メルカリ), The Bridge, Ascii Startup, CNET, Diamond, Kakao, 카카오, 카카오톡, Coupang, 쿠팡, Toss, 토스, Tencent, WeChat (微信), ByteDance, Alibaba

#### 5. Social
TikTok, Douyin, Snapchat, Telegram, Pinterest, X, XChat, BlueSky, Twitch, BeReal, Discord

#### 6. Theme
Other Super Apps, Spotify, Linkedin, Figma, Paypal, Reddit, VSCO, locket, MZ Gen, Gen Z, 1020 trend, Social app, Tech Crunch Startup

Notes:
- The `All Other ...` entries (and `Other Super Apps`) are catch-all queries for category-relevant stories not matched by a more specific query in that category.
- Sub-brand rollups for tagging: Facebook, Instagram, and WhatsApp roll up to Meta; YouTube, Gmail, and Android roll up to Google; Amazon Prime rolls up to Amazon. A sub-brand story is filed once under its own master query but tagged with the parent company (see the routing rule).
- NVIDIA was tagged `AI Agent SR` in the source sheet; it is folded into the AI Agent category here.
- Some master queries carried alternate labels across the two source sheets (for example `Wrtn Crack`/`Crack (크랙)`, `Gemini`/`GeminI`). They are the same query; use the label above and treat the variant as an alias.

### 3b-1. Strict display order

The HTML report must follow the exact category and master query order listed in Section 3b. This order is mandatory and must not be changed by collection order, source order, article count, date, tier, or relevance score.

Category order:

1. AI Agent
2. AI/GPT
3. Global Big Tech
4. Asia Big Tech
5. Social
6. Theme

Within each category, master queries must appear exactly in the order listed in Section 3b.

Implementation requirement:
- Create explicit `CATEGORY_ORDER` and `MASTER_QUERY_ORDER` arrays in the report-building script.
- Sort rendered rows using those arrays.
- Do not sort categories alphabetically.
- Do not sort master queries alphabetically.
- Do not group by source domain.
- Do not move “All Other ...” catch-all rows away from their defined position.
- Within each master query, sort article clusters by:
  1. tier ascending: Tier 1 → Tier 2 → Tier 3
  2. date descending within the same tier
  3. stable cluster id as final tiebreaker

### 3c. Inclusion criteria

Collect a story if it matches at least one:
- New service launched, planned, or in testing.
- Feature added, planned, or in testing.
- Fintech feature or service, or a feature that affects fintech.
- Merger, acquisition, investment, or partnership.
- Quarterly user metrics or revenue results.
- Multi-company strategy comparison or industry-trend article.
- Market or economic article from a public or government institution (for example a `[Market]` item summarizing digital banking account growth alongside broader economic conditions).
- Any other story relevant to LINE's services or strategy.

Use this list to judge what counts as a relevant, collectible story, especially when scanning secondary feeds and Google results. Tiering in Phase 4 (Section 3d) then sets how each surviving story ranks.

### 3d. Tiers (classification and ranking)

Every story gets exactly one tier. **Tier 4 is dropped.** Tiers 1 to 3 are all kept and written; the tier sets the order within each master query (Tier 1 first) and how much summary each story earns downstream (Tier 1 the most). Phase 4 assigns the tier from the headline and the opened source.

To assign a tier, evaluate in this order and take the first that matches:
1. **Tier 4** (any condition in 3d.4): drop the story.
2. **Tier 3** (any condition in 3d.3): the story is Tier 3.
3. **Tier 2** (any condition in 3d.2): the story is Tier 2.
4. Otherwise: the story is **Tier 1**.

Inline exceptions can override this order: a cross-market trend lifts an out-of-market story to Tier 1, and a transportation story under an AI, AI Agent, or Global Big Tech query becomes Tier 3 instead of being dropped.

#### 3d.1 Tier 1 (default keep, highest rank)
Any primary- or secondary-source story that matches no Tier 2, 3, or 4 condition is Tier 1. These are the core competitor and market moves: a launch, a shipped or tested feature, a partnership, funding, a quarterly metric, or a market or generational trend on a surface LINE has or wants. Tier 1 stories earn the extended summary downstream.

#### 3d.2 Tier 2 (kept, mid rank)
A story is Tier 2 when any of these hold and no Tier 3 or Tier 4 condition applies:
1. **HR / personnel news** from a secondary source, or **AI-related** HR news (an AI hire, team, or org change).
2. **Outside LINE's service-map domains:** the story is not about Messaging, Social feed, Ads, Content, Fintech, Platform or mini-app, Commerce, Stickers or avatars, or AI.
3. **Outside LINE's priority markets:** the market is not one of Japan, Taiwan, Thailand, Indonesia, Korea, United States, Europe, or China. Exception: if it signals a cross-market trend, raise it to Tier 1.

#### 3d.3 Tier 3 (kept, lowest rank)
A story is Tier 3 when any of these hold and no Tier 4 condition applies:
1. **Hardware-focused** stories, except AI-related hardware (AI chips, memory, semiconductors), VR or AR products, and AI speakers, which skip this rule and are ranked by the Tier 1 and Tier 2 rules.
2. **Weak promotional PR** with little service, market, or strategic meaning.
3. **Security incidents** such as a hack or breach.
4. **Other HR news:** HR news that is neither from a secondary source nor AI-related, when the company is one of the master queries.
5. **Transportation under an AI, AI Agent, or Global Big Tech query:** the Tier 4 transportation drop is downgraded to Tier 3 here (see 3d.4 #10).

#### 3d.4 Tier 4 (hard exclusions, dropped)
Drop the story if any of these hold:
1. Any site in `site_denylist` (press-release wires, pure aggregators).
2. Gossip about celebrities, influencers, or personal social-media activity (for example what a celebrity posted on Instagram).
3. Review articles (for example the pros and cons of a phone).
4. How-to and what-is articles (for example "How to change your name on Snap", "What is Imagine AI", "How to use Imagine AI").
5. Overly speculative articles with weak evidence, including opinion and op-ed pieces by journalists.
6. Stories already covered last week. Enforced in Phase 6; cross-check the Weekly Trend email that goes out each week.
7. Business sectors unrelated to LINE: autonomous driving, space, cloud infrastructure. This list grows over time.
8. **Naver / LINE / LY Corporation single-company stories.** A story whose subject is Naver, LINE, or LY Corporation on its own is our own coverage and is dropped. Exception: when one of them is named as just one of several companies in a market-level story (a market shift, industry trend, or competitor comparison), keep it as a `[Market]` item only, never as a standalone Naver/LINE update. Kakao, Coupang, Toss, Rakuten, DeNA, Mercari, Tencent, ByteDance, and Alibaba are reviewed normally as competitors.
9. Simple stock-price-movement articles (for example "Square stock rose X%"), unless the move is tied to a strategic event.
10. **Transportation** stories, except when the master query is an AI, AI Agent, or Global Big Tech query, in which case the story is Tier 3 (see 3d.3 #5) rather than dropped.

### 3e. Multi-company routing rule (one destination per story)

A story is placed in exactly one master query and never duplicated. Destinations:
- Single primary actor: the master query whose company is the **primary actor** of the news (the one taking the action, launching the product, or most directly affected), tagged with that company.
- Whole-market, multi-company, or public-institution economic story: file under the `[Market]` destination and tag it `[Market]`.
- Same-parent multi-product story (for example one Meta change spanning Instagram and WhatsApp): file once under the parent's master query, not once per product.

Tie-break order when more than one company could be primary: highest LINE-strategic relevance, then the company the headline leads with.

AI-angle tie-break: a company can appear in an AI category (AI Agent or AI/GPT) and in a non-AI category (Global Big Tech, Asia Big Tech, or Social). When a story could fit both, file it by its substance. An AI-substance story (a model, an Agent, or an AI feature) goes to the AI category; a product, market, or business story goes to the big tech or social category. This keeps one story-event in one place while letting a company's AI news and product news land in their right categories.

### 3f. Operating rules

Three named rules are referenced by the phases in Section 4.

#### Headline rule
Write headlines during collection, one source at a time as you review it, not in a batch at the end. For each story:
- Base the headline on the best available source: a primary source first, then a trustworthy secondary source.
- Cluster articles that cover the same announcement, feature, product update, partnership, funding, or market event, and write only one headline per cluster (see the cluster rule).
- Skip a duplicate article unless it adds materially different information; if it does, either fold the new fact into the existing headline or, if it is really a distinct event, start a new cluster.
- Before finalizing a cluster's headline, confirm a primary source was used whenever one was available.
- Write the headline itself in the format and house style of Section 2.

#### Cluster rule
- A cluster holds up to 3 sources, no more.
- The first source is the basis for the headline and is normally a primary source. If the cluster has no primary source, base it on a secondary source; if it has neither, base it on a Google News source.
- Order a cluster's sources by source quality: official source first; closest original specialist outlet second; trusted outlets such as TechCrunch, 9to5Google, 9to5Mac, or Social Media Today; local specialist media; then general business or mainstream outlets. Once a cluster holds 3 sources, drop any further source unless it is an official source replacing a weaker Source 1.
- The cluster's date is the publish date of its primary source if it has one, otherwise the earliest publish date among its sources.
- Umbrella vs detail: a broad announcement and the deeper sub-stories under it are separate events, so cluster them separately (a model-suite launch is one cluster; each individually detailed model in the suite is its own cluster).

#### Trigger cluster size rule
This runs in Phase 3 (Google News), per master query. If more than 50% of a query's Google results only repeat coverage already captured in Phases 1 and 2 (for example a week where searching `Claude` returns almost only Fable-launch stories already sourced), run a boolean negated search to surface fresh results, for example `Claude -Fable`, and read up to 100 results from that negated search. Use the most frequent repeated term as the one to negate.

---

## 4. Procedure

The run is organized into the six categories from Section 3b. Process one category completely, through Phases 0 to 6, before starting the next, so each delivered block is internally consistent. Category order: AI Agent, AI/GPT, Global Big Tech, Asia Big Tech, Social, Theme.

All six categories use the same method and produce one combined deliverable: one HTML report, one headline format (Section 2), and one JSON data file that next week's repetition check compares against. There is no separate AI report and no second headline format. Headlines are written during collection (Phases 1 to 3) under the headline rule (Section 3f), one per cluster.

**Routing (one destination per cluster).** As you collect, assign each cluster to exactly one owning master query using the multi-company routing rule in Section 3e: the primary actor's query, `[Market]` for market-level stories, sub-brands filed under their own query but tagged to the parent, and the AI-angle tie-break for AI-versus-product stories. This is also the cross-query dedup step: when the same event is caught under more than one master query, merge it into one cluster filed once.

### Phase 0: Setup
Create `./output/` and `./archive/` if missing. Set `time_period` from the run dates, inclusive of both ends, normalizing any `yyyy.m.d~yyyy.m.d` input to ISO first (Section 0). Initialize an empty `data_{since}_{until}.json` (the per-cluster record store from Section 1b); the HTML report is rendered from it at the end of the run. Take the report and data paths from the `output` block in Section 3a. The report itself is produced at the end of the run by filling the Section 6 template (see Phase 6).

### Phase 1: Primary sources
For each master query in the current category, open its **Primary sources** from the source maps below and collect every article published inside `time_period`. Write a headline for every primary-source link under the headline rule (Section 3f). When two primary-source links cover the same event, cluster them into one row and write a single headline (cluster rule, Section 3f). Apply each query's handling note from the source map (filter a broad newsroom for the product, treat a notable GitHub or changelog release as the event, check more than one official page, treat in-app or Discord posts as the update channel, or verify the URL or path first). Primary sources set the cluster's date.

### Phase 2: Secondary sources
For each master query, scan its **Secondary sources** from the source maps below, plus the `trusted_news_sites` (Section 3a) weighted by the current category, for in-window articles relevant to the query. Drop anything that is Tier 4 (Section 3d.4) as you go. For every remaining secondary article, apply the cluster rule (Section 3f): if it covers an event already clustered in Phase 1, add it to that cluster as an extra source up to the 3-source cap, and once a cluster holds 3 sources discard any further secondary source for it; if it covers a new event not seen in Phase 1, start a new cluster and write its headline under the headline rule. Run the `All Other ... News` and `Other Super Apps` catch-alls last, and route keyword or theme feeds to the owning master query when one exists.

Secondary source sweep must be source-first before query routing. Do not run only a few query-specific `site:` searches. First sweep each major source's latest/archive/category/guide/topic pages for the target week, paginate until articles before the start date appear, then route each relevant article to the correct master query. Mandatory source-first sweeps include TechCrunch, 9to5Google, 9to5Mac, Social Media Today, The Verge, VentureBeat, SiliconANGLE, ZDNET, CNBC, The Decoder, MarkTechPost, and accessible alternatives for Reuters/Bloomberg/NYTimes/The Information leads.

Required source-specific coverage:
- TechCrunch: sweep latest, AI, startups, apps, and social/platform surfaces for OpenAI, Anthropic, Google, Meta, Apple, Microsoft, NVIDIA, AI infra, AI startup, agentic AI, creator tools, and social platform stories.
- 9to5Google: sweep Gemini, Google AI, Google Search, Android, Pixel, Google Photos, Google Home, YouTube, Workspace, and Google app guide/archive surfaces. Pair Google official sources as Source 1 with 9to5Google as Source 2 when both cover the event.
- 9to5Mac: sweep Apple, iOS, App Store, Apple Intelligence, Siri, Vision Pro, Mac, iPad, privacy, and developer policy surfaces. Pair Apple official sources as Source 1 with 9to5Mac as interpretive Source 2 when applicable.
- Social Media Today: sweep Meta, Instagram, Facebook, WhatsApp, Threads, TikTok, YouTube, LinkedIn, Snapchat, social ads, creator monetization, and social commerce updates, and route them across Social, Global Big Tech, AI/GPT, and Theme as appropriate.
- Asia/regional: sweep ITmedia, ASCII STARTUP, Impress Watch, CNET Japan, The Bridge, Nikkei Asia, Tech in Asia, KrASIA, Rest of World, SCMP, TechNode, 36Kr, ZDNet Korea, ETNews, Bloter, Platum, The Bell, Korea Herald, Korea JoongAng Daily, and Yonhap English where relevant.

Weight the secondary outlets by category: Global English outlets (techcrunch.com through 9to5google.com, plus the-decoder.com, marktechpost.com, siliconangle.com) are the main surface for AI Agent, AI/GPT, Global Big Tech, and Social; Asia-focused English (restofworld.org, techinasia.com, kr-asia.com, scmp.com) for Asia Big Tech, super apps, and Theme; Korean (zdnet.co.kr, etnews.com, bloter.net, platum.kr, thebell.co.kr) for the Korean Asia Big Tech queries and Korea AI; Japanese (itmedia.co.jp, watch.impress.co.jp, ascii.jp, japan.cnet.com, asia.nikkei.com) for the Japanese queries; Chinese (technode.com, 36kr.com, caixinglobal.com) for the Chinese queries. Several of these paywall (bloomberg.com, reuters.com, theinformation.com, asia.nikkei.com, caixinglobal.com, scmp.com); treat a paywalled article as a lead and prefer an accessible source for the same event.

### Phase 3: Google News
For each master query, search Google News across three editions: Google US (`US / en`), Google KR (`KR / ko`), and Google JP (`JP / ja`). On Claude Code you have no live browser, so use the Google News RSS endpoints and the `web_search` fallback from Section 0; apply the date window with `after:` / `before:` (`before:` is exclusive, pass `until + 1 day`), and do the date filtering and cross-edition dedup in code. For an Asian company, search both its English name in Google US and its local-language name in the local edition (for example Toss in Google US and `토스` in Google KR; Rakuten in Google US and `楽天` in Google JP). Pool the editions into one set and dedup the same event across them. Use the Phase 3 search-term overrides below for any query whose bare name is noisy.

Google US / English search is mandatory for every master query before n/a is assigned. Do not limit Google Query to major queries. For every master query, run the base query and these variants with `after:{since}` and `before:{until_plus_1}`: `{master query}`, `{master query} AI`, `{master query} update`, `{master query} launch`, `{master query} partnership`, `{master query} funding`, and `{master query} regulation`. Check at least the top 50 results and up to 100 where possible, using both Google News RSS and `web_search` fallback when available.

For Asia Big Tech, Google US search is mandatory; Google KR search is mandatory for Korean companies and Korean-language aliases; Google JP search is mandatory for Japanese companies and Japanese-language aliases; use local-language query variants listed in the search-term overrides; and do not mark any Asia Big Tech query as n/a unless local-language Google evidence exists. Examples: `Rakuten after:2026-06-17 before:2026-06-24`, `楽天 after:2026-06-17 before:2026-06-24`, `카카오 after:2026-06-17 before:2026-06-24`, and `토스 after:2026-06-17 before:2026-06-24`. If a Google result matches an event already found in Phase 1 or 2, add it as Source 2 or Source 3 only when it adds useful context; do not create a duplicate row.

Apply the **trigger cluster size rule** (Section 3f): if more than 50% of a query's Google results only repeat coverage already captured in Phases 1 and 2, re-run the search with the dominant repeated term negated (for example `Claude -Fable`) and read up to 100 results from that negated search. Apply the **cluster rule** the same way as Phase 2: add a Google source to an existing cluster up to the 3-source cap, or start a new cluster if the event is new, then write its headline under the headline rule. A Google News link is the basis for a cluster's headline only when the cluster has no primary or secondary source.

### Phase 3a: Asia Big Tech reinforcement

Before tiering or n/a assignment, separately reinforce Asia Big Tech. For each Asia Big Tech query, check in this order: official newsroom/blog/press/IR/developer pages; local-language official pages; Google US / English query; Google KR for Korean companies and aliases; Google JP for Japanese companies and aliases; and regional specialist media. Do not leave an Asia query as n/a without official page evidence, Google US evidence, applicable KR/JP/local-language evidence, and regional-source sweep evidence.

Required local query examples include: Kakao / 카카오, KakaoTalk / 카카오톡, Kakao Pay / 카카오페이, Kakao Bank / 카카오뱅크, Kakao Mobility / 카카오모빌리티, Toss / 토스, Coupang / 쿠팡, Woowa Brothers / 배달의민족, 당근 / Karrot, Rakuten / 楽天, Mercari / メルカリ, DeNA / ディー・エヌ・エー, Note / note, LINE Yahoo / LINEヤフー, PayPay, Tencent / 腾讯, WeChat / 微信, Alibaba / 阿里巴巴, Taobao / 淘宝, ByteDance / 字节跳动, Doubao / 豆包, TikTok, Grab, Shopee, and Gojek.

### Phase 4: Tier arrangement
With the headlines and clusters from Phases 1 to 3 in hand, go through every master query in the category and assign each cluster a tier using Section 3d. First apply the content exclusion rules (Tier 4, Section 3d.4) and drop those clusters outright. Then classify each surviving cluster as Tier 1, 2, or 3 by the Section 3d order, reading the cluster's opened source where the headline alone is not enough to judge. Arrange each master query's clusters by tier, Tier 1 first, then Tier 2, then Tier 3, and store the tier on each cluster record in the data file. Nothing else is cut: every cluster that is not Tier 4 and not a last-week repeat is written.

### Phase 5: N/a establishment

n/a is a final-state decision only. Do not mark n/a while any collection or routing work remains. Never assign n/a before checking official sources, TechCrunch/9to5Google/9to5Mac/Social Media Today sweeps where relevant, Google US for that master query, and applicable Google KR/JP/local-language aliases for Asia queries. Also do not assign n/a while a source sweep may still route an event from another query into this master query.

A master query gets n/a only when all applicable sources and Google Query variants were completed and no in-range, non-duplicate Tier 1-3 article survived. Store the evidence in `na_audit` or validation JSON, not as a large default HTML table. Each n/a audit entry must include:
- `primary_checked`
- `secondary_checked`
- `google_us_checked`
- `google_kr_checked`
- `google_jp_checked`
- `local_language_checked`
- `checked_queries`
- `checked_sources`
- `reason`

For Asia Big Tech, n/a is forbidden unless official newsroom/source page, Google US, applicable Google KR/JP, local-language aliases, and regional specialist media were all checked.

### Phase 6: Repetition check
Two passes. First, the across-week check: load last week's data file from `previous_week.data_path` and, for each cluster this week, decide whether it covers the **same news event** as any last-week cluster (compare on `article_texts`), even if the specific articles differ; set `dedup_status = drop` for genuine repeats (Tier 4 #6) and `keep` for real follow-on developments with new facts or escalation. Second, the within-week check: compare this week's clusters against each other and drop any duplicate, so the same event is not rendered twice across master queries. Save this week's data file to the archive path so next week's check can read it. Then build the deliverable: write both `data_{since}_{until}.json` and `report_{since}_{until}.html` from the same final records. The JSON contains full records, n/a audit records, validation logs, source-check evidence, and the crawl manifest. The HTML contains the clean user-facing article checklist with static pre-rendered rows, working checkboxes, and no verbose validation/audit tables by default.

### Per-category source maps (Phases 1 and 2)
Each query lists its source URLs and, in parentheses, the handling rule. (`GH` = read GitHub releases; `changelog` / `release notes` = treat a notable release as the event.) Primary sources are read in Phase 1; Secondary sources in Phase 2.

The **common Tech / AI / Social feeds** below back every category as secondary-source sweep surfaces; weight them by the current category:
- TechCrunch tag pages: `https://techcrunch.com/tag/ai/`, `/tag/openai/`, `/tag/anthropic/`, `/tag/google/`, `/tag/apple/`, `/tag/meta/`, `/tag/microsoft/`, `/tag/amazon/`, plus `/category/artificial-intelligence/` and `/category/startups/`
- 9to5Google guides: `https://9to5google.com/guides/gemini/`, `/guides/google-search/`, `/guides/android/`, `/guides/youtube/`, `/guides/chrome/`
- 9to5Mac guides: `https://9to5mac.com/guides/apple-intelligence/`, `/guides/ios/`, `/guides/siri/`, `/guides/app-store/`
- Social Media Today: `https://www.socialmediatoday.com/topic/social-media-updates/`
- AI trade press: `https://the-decoder.com/`, `https://www.marktechpost.com/`, `https://venturebeat.com/category/ai/`, `https://siliconangle.com/`, `https://aibusiness.com/`

#### AI Agent

**Primary sources** (the query's official channel; apply any per-query handling note shown in parentheses):
- **AutoGPT**: https://agpt.co/, https://github.com/Significant-Gravitas/AutoGPT/releases (homepage + GH), legacy https://autogpt.net/category/autogpt/
- **A.(에이닷)**: https://news.sktelecom.com/ (SKT newsroom, 에이닷 tag), https://www.sktelecom.com/
- **Wrtn Crack**: https://crack.wrtn.ai/announcement, https://wrtn.io/
- **Cotomo**: https://cotomo.ai/, https://cotomo.ai/posts, https://cotomo.ai/app-posts
- **Replika**: https://replika.com/, https://blog.replika.com/
- **Poketomo**: https://poketomo.com/, https://poketomo.com/news/
- **Hume AI**: https://www.hume.ai/blog, https://www.hume.ai/news, https://dev.hume.ai/docs
- **OpenClaw (Moltbot, Clawdbot)**: https://openclaw.ai/blog, https://github.com/openclaw/openclaw/releases (blog + GH; Moltbot/Clawdbot have no own source -> Google Query)
- **Paperclip**: https://github.com/paperclipai/paperclip/releases (GH)
- **BabyAGI**: https://github.com/yoheinakajima/babyagi/releases (GH)
- **Microsoft AutoGen**: https://github.com/microsoft/autogen/releases, https://microsoft.github.io/autogen/, https://devblogs.microsoft.com/ (GH + docs + devblog)
- **AgentGPT**: https://agentgpt.reworkd.ai/, https://github.com/reworkd/AgentGPT/releases (site + GH)
- **Claude Cowork**: https://claude.com/blog, https://www.anthropic.com/news, https://www.anthropic.com/engineering, https://docs.anthropic.com/ (filter for Claude Cowork)
- **KIRA**: https://kira.krafton-ai.com/, https://github.com/krafton-ai/KIRA/releases, https://www.krafton.ai/, https://www.krafton.com/news/press/ (site + GH + Krafton press)
- **Rinna**: https://rinna.co.jp/news/, https://rinna.co.jp/
- **CrewAI**: https://crewai.com/blog, https://docs.crewai.com/, https://github.com/crewAIInc/crewAI/releases (blog + docs + GH)
- **AutoGen**: https://github.com/microsoft/autogen/releases (GH; same project as Microsoft AutoGen)
- **LangGraph**: https://www.langchain.com/blog, https://docs.langchain.com/, https://github.com/langchain-ai/langgraph/releases, https://langchain-ai.github.io/langgraph/ (blog + docs + GH; blog covers many products, filter for LangGraph)
- **Chai**: https://www.chai-research.com/blog, https://www.chai-research.com/news (updates also ship via in-app Discord)
- **Nomi**: https://nomi.ai/updates/ (updates ship via app; community on Discord + r/NomiAI)
- **Kindroid**: https://kindroid.ai/blog/, https://kindroid.ai/docs/article/update-log/, https://discord.gg/kindroid (blog + update log; also r/KindroidAI)
- **Paradot**: https://www.paradot.ai/ (updates via app/Discord; Google Query backup)
- **Bot Madang**: https://github.com/hunkim/botmadang/releases (GH; if dry, Google Query)
- **NVIDIA**: https://developer.nvidia.com/blog/recent-posts/ (broad developer blog, filter for AI/Agent relevance; sheet labels this `AI Agent SR`)

**Secondary sources** (defined news outlets and catch-all/keyword feeds):
- **All Other AI Agent News** (catch-all): https://techcrunch.com/category/artificial-intelligence/, https://venturebeat.com/category/ai/, https://the-decoder.com/ (run last; sweep for agent stories not caught by a specific query; dedupe; add net-new)
- **Mersoom** (unresolved): no confirmed source; Google Query + flag for manual lookup

#### AI/GPT

**Primary sources** (the query's official channel; apply any per-query handling note shown in parentheses):
- **Lovable**: https://lovable.dev/blog
- **OpenAI**: https://openai.com/news/, https://openai.com/index/, https://openai.com/research/, https://platform.openai.com/docs/changelog, https://help.openai.com/en/articles/6825453-chatgpt-release-notes, https://developers.openai.com/codex/changelog (multiple official OpenAI surfaces)
- **Scale AI**: https://scale.com/blog, https://scale.com/press
- **NotebookLM**: https://blog.google/products/notebooklm/
- **Google Chrome**: https://blog.google/products/chrome/, https://developer.chrome.com/blog/, https://chromereleases.googleblog.com/ (blog + dev blog + release log)
- **Anthropic**: https://www.anthropic.com/news, https://www.anthropic.com/research, https://www.anthropic.com/engineering, https://docs.anthropic.com/
- **Claude**: https://claude.com/blog, https://www.anthropic.com/news
- **Microsoft Edge**: https://blogs.windows.com/msedgedev/, https://blogs.bing.com/search/
- **Bing**: https://blogs.bing.com/search/
- **Copilot**: https://www.microsoft.com/en-us/microsoft-copilot/blog/, https://devblogs.microsoft.com/microsoft365dev/
- **Databricks**: https://www.databricks.com/blog, https://www.databricks.com/company/newsroom, https://docs.databricks.com/release-notes/index.html
- **Thinking Machines Lab**: https://thinkingmachines.ai/news/
- **Perplexity AI**: https://www.perplexity.ai/hub/blog, https://www.perplexity.ai/hub/news
- **Stability AI**: https://stability.ai/news, https://stability.ai/blog, https://github.com/Stability-AI (news + blog + GH)
- **ElevenLabs**: https://elevenlabs.io/blog, https://elevenlabs.io/docs/changelog
- **Writer AI**: https://writer.com/blog/, https://writer.com/newsroom/, https://writer.com/product-updates/
- **Ayar Labs**: https://ayarlabs.com/newsroom/, https://ayarlabs.com/blog/
- **Physical Intelligence**: https://www.physicalintelligence.company/blog, https://www.physicalintelligence.company/news
- **Inflection AI**: https://inflection.ai/news, https://inflection.ai/blog
- **Moonshot AI**: https://www.moonshot.cn/, https://kimi.moonshot.cn/ (backup https://pandaily.com/)
- **Cohere**: https://cohere.com/blog, https://cohere.com/newsroom, https://docs.cohere.com/changelog
- **Brave Browser**: https://brave.com/blog/, https://github.com/brave/brave-browser/releases
- **Sigma Browser (SigmaOS)**: https://sigmaos.com/blog (Google Query backup)
- **Vivaldi Browser**: https://vivaldi.com/blog/, https://vivaldi.com/changelog/
- **Maxthon Browser**: https://www.maxthon.com/blog/ (Google Query backup)
- **MyHeritage**: https://blog.myheritage.com/, https://www.myheritage.com/ai
- **Inflection AI (Pi)**: https://pi.ai/, https://inflection.ai/news
- **character.ai**: https://blog.character.ai/
- **ChatGPT**: https://help.openai.com/en/articles/6825453-chatgpt-release-notes, https://openai.com/index/ (release notes + news; filter for ChatGPT)
- **Codex**: https://developers.openai.com/codex/changelog, https://openai.com/index/ (changelog; filter news for Codex)
- **Sora**: https://openai.com/sora/, https://openai.com/index/ (filter for Sora)
- **Meta AI**: https://ai.meta.com/blog/, https://about.fb.com/news/, https://engineering.fb.com/ (filter for AI)
- **Google AI**: https://blog.google/technology/ai/, https://blog.google/innovation-and-ai/, https://developers.googleblog.com/, https://research.google/blog/, https://deepmind.google/blog/ (filter for AI)
- **Gemini**: https://blog.google/products/gemini/, https://gemini.google/release-notes/, https://ai.google.dev/gemini-api/docs/changelog, https://deepmind.google/blog/ (product page + release notes + api changelog + DeepMind)
- **Veo**: https://deepmind.google/technologies/veo/, https://blog.google/technology/ai/ (filter for Veo)
- **Amazon AI**: https://aws.amazon.com/blogs/machine-learning/, https://aws.amazon.com/blogs/aws/, https://www.aboutamazon.com/news/aws, https://aws.amazon.com/about-aws/whats-new/machine-learning/ (filter for AI)
- **Nova AI**: https://aws.amazon.com/ai/generative-ai/nova/, https://www.aboutamazon.com/news/aws (filter for Amazon Nova)
- **Trainium**: https://aws.amazon.com/machine-learning/trainium/, https://www.aboutamazon.com/news/aws (filter for Trainium)
- **Claude Code**: https://claude.com/blog, https://docs.anthropic.com/en/docs/claude-code, https://www.anthropic.com/engineering (filter for Claude Code)
- **Microsoft AI**: https://blogs.microsoft.com/, https://news.microsoft.com/source/, https://www.microsoft.com/en-us/microsoft-365/blog/, https://devblogs.microsoft.com/, https://www.microsoft.com/en-us/research/blog/ (filter Microsoft surfaces for AI: Copilot, Azure AI, Microsoft AI)
- **Apple AI**: https://www.apple.com/newsroom/, https://developer.apple.com/news/, https://developer.apple.com/documentation/appleintelligence (filter for Apple Intelligence)
- **Safari**: https://developer.apple.com/documentation/safari-release-notes, https://developer.apple.com/news/, https://webkit.org/blog/ (filter for Safari releases)
- **Comet**: https://www.perplexity.ai/hub/blog, https://www.perplexity.ai/hub/news (verify; ambiguous name vs Comet ML)
- **Anysphere (Cursor)**: https://cursor.com/blog, https://cursor.com/changelog, https://docs.cursor.com/ (blog + changelog + docs)
- **Speak AI**: https://www.speak.com/, https://www.speak.com/blog (was unresolved; concrete blog now)
- **Canva AI**: https://www.canva.com/newsroom/news/ (filter for Canva AI / Magic Studio)
- **Le Chat**: https://mistral.ai/news/, https://docs.mistral.ai/, https://github.com/mistralai (filter for Le Chat)
- **Leonardo AI**: https://leonardo.ai/news, https://leonardo.ai/blog
- **Kling AI**: https://klingai.com/ (backup https://www.kuaishou.com/en)
- **Seedance**: https://seed.bytedance.com/en/, https://seed.bytedance.com/en/blog (filter for Seedance)
- **Arc Browser**: https://browsercompany.com/blog/, https://arc.net/ (release notes via resources.arc.net; Google Query backup)
- **Dia Browser**: https://www.diabrowser.com/release-notes/latest (read release notes)
- **Opera One**: https://blogs.opera.com/news/, https://blogs.opera.com/desktop/ (filter for Opera One)
- **Zen Browser**: https://zen-browser.app/, https://github.com/zen-browser/desktop/releases (site + GH release notes)
- **Wavebox**: https://wavebox.io/blog/, https://hub.wavebox.io/
- **Shift Browser**: https://shift.com/blog/ (Google Query backup)
- **Orion Browser**: https://browser.kagi.com/, https://browser.kagi.com/updates.html (read updates)
- **Firefox**: https://blog.mozilla.org/en/firefox/, https://www.mozilla.org/en-US/firefox/releases/, https://github.com/mozilla (news + release notes)
- **Samsung Internet**: https://news.samsung.com/global/, https://developer.samsung.com/internet (Google Query backup)
- **Stable Diffusion**: https://stability.ai/news, https://stability.ai/blog, https://github.com/Stability-AI (filter for Stable Diffusion)
- **DALL-E**: https://openai.com/index/, https://platform.openai.com/docs/changelog (filter for DALL-E)
- **Craiyon**: https://www.craiyon.com/ (Google Query backup)
- **Midjourney**: https://www.midjourney.com/updates, https://docs.midjourney.com/ (announcements also via official Discord)
- **Adobe AI**: https://news.adobe.com/, https://blog.adobe.com/, https://developer.adobe.com/ (filter for AI / Firefly / Sensei)
- **Adobe Firefly**: https://firefly.adobe.com/, https://blog.adobe.com/ (filter for Firefly)
- **yandex**: https://yandex.com/company/press_releases/, https://yandex.com/blog/, https://yandex.com/dev/
- **Kakao Brain / Kakao AI**: https://www.kakaocorp.com/page/, https://www.kakaocorp.com/page/press (filter for AI / Kanana; Kakao Brain merged into Kakao/Kanana)

**Secondary sources** (defined news outlets and catch-all/keyword feeds):
- **All Other AI/GPT News** (catch-all): https://techcrunch.com/category/artificial-intelligence/, https://www.theverge.com/ai-artificial-intelligence, https://the-decoder.com/ (run last; sweep)
- **Generative AI / AI Startup / Content Generator / Voice Synthesis / AI Bot / Image AI / AI Assistant / AI Plugin / LLM / Chatbot / AI Character** (keyword feeds): https://techcrunch.com/category/artificial-intelligence/, https://venturebeat.com/category/ai/, https://www.theverge.com/ai-artificial-intelligence, https://the-decoder.com/ (topical feeds; route to the owning company's master query when one applies)
- **AI Healthcare** (keyword): https://www.mobihealthnews.com/, https://techcrunch.com/category/artificial-intelligence/
- **Japan AI** (region keyword): https://www.itmedia.co.jp/aiplus/, https://asia.nikkei.com/Business/Technology
- **Korea AI** (region keyword): https://news.daum.net/ai-tech, https://zdnet.co.kr/ (filter for AI)
- **China AI** (region keyword): https://technode.com/, https://www.scmp.com/tech
- **US AI** (region keyword): https://techcrunch.com/category/artificial-intelligence/, https://www.theverge.com/ai-artificial-intelligence
- **Sam Altman** (person): https://techcrunch.com/tag/sam-altman/, https://www.businessinsider.com/
- **Copyright Shield** (program): https://openai.com/index/, https://www.theverge.com/ai-artificial-intelligence
- **Skywalker.ai / Dream Fusion / MDM** (unresolved): no confirmed source; Google Query + flag
- **Sidekick Browser**: https://www.meetsidekick.com/blog (homepage/blog only; Google Query + verify; may be inactive)
- **UC Browser**: https://www.ucweb.com/ (no English newsroom; App Store/Play listings + Google Query)
- **CryptoTab Browser**: https://cryptobrowser.site/en/news/ (news page + Google Query)
- **Zeta (제타)**: Google Query only, using the Phase 2 search overrides (제타 AI character, Zeta Scatter Lab); Scatter Lab's Korean character-chat app, not the fintech Zeta

#### Global Big Tech

**Primary sources** (the query's official channel; apply any per-query handling note shown in parentheses):
- **Meta**: https://about.fb.com/news/, https://ai.meta.com/blog/, https://engineering.fb.com/, https://investor.fb.com/investor-news/default.aspx
- **Instagram**: https://about.instagram.com/blog/announcements, https://about.fb.com/news/
- **Amazon**: https://www.aboutamazon.com/news, https://www.aboutamazon.com/news/aws, https://www.aboutamazon.com/news/devices, https://www.aboutamazon.com/news/retail
- **Apple**: https://www.apple.com/newsroom/, https://developer.apple.com/news/, https://developer.apple.com/news/releases/
- **Netflix**: https://about.netflix.com/en/newsroom
- **Google**: https://blog.google/, https://blog.google/products/, https://blog.google/technology/ai/, https://developers.googleblog.com/, https://cloud.google.com/blog/ (company-level query)
- **YouTube**: https://blog.youtube/, https://blog.youtube/news-and-events/
- **Android**: https://blog.google/products/android/, https://android-developers.googleblog.com/, https://developer.android.com/about/versions
- **Microsoft**: https://news.microsoft.com/source/, https://blogs.microsoft.com/, https://blogs.windows.com/
- **Facebook**: https://about.fb.com/news/, https://engineering.fb.com/ (filter for Facebook)
- **WhatsApp**: https://blog.whatsapp.com/, https://about.fb.com/news/ (WhatsApp blog + Meta newsroom filtered for WhatsApp)
- **Amazon Prime**: https://www.aboutamazon.com/news/prime, https://www.aboutamazon.com/news/entertainment, https://www.aboutamazon.com/news/retail (filter for Prime)
- **iOS**: https://www.apple.com/newsroom/, https://developer.apple.com/news/releases/, https://developer.apple.com/documentation/ios-ipados-release-notes (filter for iOS/software)
- **Gmail**: https://blog.google/products/gmail/, https://workspaceupdates.googleblog.com/ (Gmail blog + Workspace Updates filtered for Gmail)
- **Grab**: https://www.grab.com/sg/press/, https://www.grab.com/sg/blog/, https://www.grab.com/sg/newsroom/ (verify region path)

**Secondary sources** (defined news outlets and catch-all/keyword feeds): None (this category has no catch-all or keyword rows).

#### Asia Big Tech

**Primary sources** (the query's official channel; apply any per-query handling note shown in parentheses):
- **Rakuten (楽天市場)**: https://corp.rakuten.co.jp/news/press/, https://global.rakuten.com/corp/news/press/, https://global.rakuten.com/corp/innovation/
- **note（ノート)**: https://note.jp/ (Google Query backup)
- **DeNA**: https://dena.com/intl/news/, https://dena.com/jp/news/
- **Gree (グリー)**: https://corp.gree.net/jp/ja/news/, https://corp.gree.net/en/news/
- **Time Tree (タイムツリ)**: https://timetreeapp.com/intl/newsroom, https://timetreeapp.com/intl/blog
- **Mercari(メルカリ)**: https://about.mercari.com/press/news/, https://about.mercari.com/en/press/news/, https://jp-news.mercari.com/
- **Kakao / 카카오**: https://www.kakaocorp.com/page/, https://www.kakaocorp.com/page/press
- **Tencent**: https://www.tencent.com/en-us/articles.html, https://www.tencentcloud.com/blog, https://www.tencentcloud.com/press-release
- **Alibaba**: https://www.alibabagroup.com/en-US/news-and-resource, https://www.alibabacloud.com/en/press-room, https://www.alibabacloud.com/blog, https://www.alibabacloud.com/help/en/releasenotes/
- **Gunosy (グノシー)**: https://gunosy.co.jp/news/ (verify path; gunosy.co.jp/en for English; Google Query backup)
- **카카오톡**: https://www.kakaocorp.com/page/press (filter for KakaoTalk)
- **Coupang / 쿠팡**: https://news.coupang.com/, https://ir.aboutcoupang.com/news-events/news/default.aspx (newsroom + IR)
- **Toss / 토스**: https://toss.im/news, https://toss.tech/ (newsroom + tech blog)
- **WeChat (微信)**: https://www.tencent.com/en-us/articles.html (Tencent media; filter for WeChat)
- **ByteDance**: https://www.bytedance.com/en/news, https://newsroom.tiktok.com/, https://seed.bytedance.com/en/blog (news + TikTok newsroom + Seed blog)

**Secondary sources** (defined news outlets and catch-all/keyword feeds):
- **The Bridge** (media outlet): https://thebridge.jp/ (browse as a source, not a company)
- **Ascii Startup** (media outlet): https://ascii.jp/startup/ (browse as a source; verify path)
- **CNET** (media outlet): https://www.cnet.com/news/ (browse as a source)
- **Diamond** (media outlet): https://diamond.jp/ (browse as a source)

#### Social

**Primary sources** (the query's official channel; apply any per-query handling note shown in parentheses):
- **TikTok**: https://newsroom.tiktok.com/en-us/, https://www.tiktok.com/business/en/blog, https://developers.tiktok.com/doc/changelog (newsroom + business blog + changelog)
- **Snapchat**: https://newsroom.snap.com/, https://forbusiness.snapchat.com/blog, https://eng.snap.com/blog
- **Telegram**: https://telegram.org/blog, https://core.telegram.org/api#recent-changes (blog + api change log)
- **Pinterest**: https://newsroom.pinterest.com/en/, https://business.pinterest.com/en/blog/
- **BlueSky**: https://bsky.social/about/blog, https://github.com/bluesky-social/atproto (blog + GH)
- **Twitch**: https://blog.twitch.tv/en/, https://dev.twitch.tv/docs/change-log/
- **Discord**: https://discord.com/blog, https://discord.com/newsroom, https://discord.com/developers/docs/change-log (blog + newsroom + dev change log)
- **X**: https://blog.x.com/, https://business.x.com/en/blog, https://docs.x.com/x-api/changelog (blog + business + api changelog)
- **XChat**: https://blog.x.com/ (filter X blog for XChat; Google Query backup)

**Secondary sources** (defined news outlets and catch-all/keyword feeds):
- **Douyin** (secondary-source-only): https://www.techinasia.com/, https://technode.com/ (no English newsroom; scan secondary China-tech sources, filter for Douyin)
- **BeReal** (no usable official feed): Google Query

#### Theme

**Primary sources** (the query's official channel; apply any per-query handling note shown in parentheses):
- **Spotify**: https://newsroom.spotify.com/, https://engineering.atspotify.com/
- **Linkedin**: https://news.linkedin.com/, https://www.linkedin.com/business/marketing/blog (backup socialmediatoday.com)
- **Reddit**: https://redditinc.com/news, https://redditinc.com/blog
- **VSCO**: https://vsco.co/vsco/journal (Google Query backup)
- **Figma**: https://www.figma.com/blog/, https://www.figma.com/release-notes/ (blog + release notes)
- **Paypal**: https://newsroom.paypal-corp.com/, https://www.paypal.com/us/brc/article/ (verify)
- **locket**: https://apps.apple.com/us/app/locket-widget/id1600525061, https://locket.camera/ (read App Store "What's New"; no newsroom)

**Secondary sources** (defined news outlets and catch-all/keyword feeds):
- **Other Super Apps** (catch-all): https://www.techinasia.com/, https://www.businessofapps.com/news/ (run last; sweep super-app coverage)
- **MZ Gen** (keyword): https://www.emarketer.com/, https://www.businessofapps.com/news/
- **Gen Z** (keyword): https://www.emarketer.com/, https://www.socialmediatoday.com/
- **1020 trend** (keyword): https://www.careet.net/, https://news.daum.net/ai-tech (verify Careet)
- **Social app** (keyword): https://www.businessofapps.com/news/, https://www.socialmediatoday.com/
- **Tech Crunch Startup** (media outlet): https://techcrunch.com/category/startups/ (browse as a source)

### Phase 3 search-term overrides (disambiguation)

Many master queries are common words or names that return junk when searched bare. Use the search string(s) listed here instead. A query not listed uses its exact name; add the parent company or "AI" only if a quick check shows the bare name is noisy. For Korean and Japanese companies, pair these with the local-language name per the edition rule above.

AI Agent:
- OpenClaw: "OpenClaw AI agent", "Moltbot", "Clawdbot"
- Paperclip: "Paperclip AI agent"
- A.(에이닷): "에이닷", "SKT 에이닷", "A. SKT AI agent"
- KIRA: "KIRA Krafton", "KIRA AI agent"
- Wrtn Crack: "뤼튼 크랙", "Wrtn Crack"
- Rinna: "rinna AI", "rinna 株式会社"
- Cotomo: "Cotomo AI", "Cotomo アプリ"
- Chai: "Chai AI app", "Chai Research AI"
- Nomi: "Nomi AI companion"
- Paradot: "Paradot AI"
- Poketomo: "Poketomo AI"
- Bot Madang: "봇마당", "Bot Madang"
- NVIDIA: "NVIDIA AI agent" (this category only; the company itself is broad)

AI/GPT:
- Lovable: "Lovable AI", "Lovable vibe coding"
- Codex: "OpenAI Codex"
- Sora: "OpenAI Sora", "Sora AI video"
- Gemini: "Google Gemini"
- Veo: "Google Veo", "Veo AI video"
- Nova AI: "Amazon Nova AI"
- Claude: "Claude AI", "Anthropic Claude"
- Copilot: "Microsoft Copilot"
- Safari: "Apple Safari browser"
- Comet: "Perplexity Comet browser"
- Anysphere (Cursor): "Cursor AI code editor", "Anysphere Cursor"
- Le Chat: "Mistral Le Chat"
- Seedance: "ByteDance Seedance"
- Moonshot AI: "Moonshot AI Kimi"
- Physical Intelligence: "Physical Intelligence robotics", "Physical Intelligence robot company"
- Writer AI: "Writer.com AI", "Writer AI enterprise"
- Inflection AI (Pi): "Inflection Pi AI", "Pi AI assistant"
- Arc Browser: "Arc browser Browser Company"
- Dia Browser: "Dia browser"
- Zen Browser: "Zen browser"
- Sidekick Browser: "Sidekick browser"
- Shift Browser: "Shift browser app"
- Orion Browser: "Orion browser Kagi"
- yandex: "Yandex AI"
- Kakao Brain: "카카오브레인", "Kakao Brain"
- Kakao AI: "카카오 AI", "Kakao Kanana", "카카오 카나나"
- Zeta: "제타 AI character", "Zeta Scatter Lab" (Korean character-chat app, not the fintech Zeta)
- Speak AI: "Speak AI tutor", "Speak language app" (speak.com, not speakai.co)
- Stable Diffusion: "Stable Diffusion Stability AI"
- Kling AI: "Kling AI Kuaishou video"

Asia Big Tech:
- note（ノート): "note 株式会社", "note.com Japan" (not the generic word "note")
- DeNA: "DeNA ディー・エヌ・エー"
- Gree (グリー): "GREE グリー"
- Gunosy (グノシー): "Gunosy グノシー"
- Time Tree (タイムツリ): "TimeTree タイムツリー"
- Mercari (メルカリ): "Mercari メルカリ"
- Kakao / 카카오: "Kakao 카카오"
- Coupang / 쿠팡: "Coupang 쿠팡"
- Toss / 토스: "Toss 토스 핀테크", "Viva Republica Toss"
- WeChat (微信): "WeChat 微信"

Social:
- X: "X Twitter", "X app Musk"
- XChat: "X Chat messaging app"
- Douyin: "Douyin 抖音"
- Snapchat / Snap: "Snapchat Snap"
- BlueSky: "Bluesky social app"

Theme:
- locket: "Locket Widget app" (not jewelry)
- The keyword rows (Other Super Apps, MZ Gen, Gen Z, 1020 trend, Social app) follow their Phase 1 feed handling, not a single bare search.

---

## 5. What changed in this merge

- One Query List, one HTML report, one JSON data file. Weekly and Global are not split (carried from both specs).
- Master query list and the per-category source maps come from the canonical runbook; the procedure has since been rearranged (see the architecture bullets below).
- Section 4 source maps are now the **union of both specs' links**, deduped. Several queries that were "unresolved/verify/homepage-only" now have concrete official channels (for example Speak AI, Stability AI, KIRA, LangGraph, Pi), and many queries gained official docs / changelogs / release-notes and a shared common-feed block.
- Added the Naver / LINE / LY Corporation single-company drop (now Tier 4 #8, Section 3d.4), with a `[Market]`-only exception.
- The report row uses the required column order: Category, Master Query, Headline / Title, Checkbox, URL / Sources, Tier, Date (Section 1a). The checkbox is a real `<input>` the desk ticks; the agent never pre-ticks it. Source links render as clickable anchors, primary then secondary then Google News.
- Source taxonomy simplified to two defined types: Primary source (the query's official channel) and Secondary source (a defined news outlet or catch-all or keyword feed). Links found via Google search at run time are the third, undefined type. This replaces the earlier Group 1 / Group 2 / Group 3 split.
- Agent-efficiency notes: resolve Google News redirects only for kept links; add the US-edition pass for an Asian query only when the local-edition pass is thin; cap each cluster at 3 sources so collection stops early; all phases run inline, no spawned sub-agents.
- Procedure rearranged into Phases 0 to 6: Phase 0 setup; Phase 1 primary sources, one headline per link; Phase 2 secondary sources, clustered into Phase 1 with a 3-source cap; Phase 3 Google News across US, KR, and JP with the trigger cluster size rule; Phase 4 tier arrangement; Phase 5 n/a establishment; Phase 6 repetition check (across-week and within-week). Headlines are now written during collection, not in a separate pass.
- Replaced the hard/soft exclusion split and the old selection tiers with a single four-tier system (Section 3d): Tier 4 drops; Tiers 1 to 3 are kept and ranked. Geography is no longer a hard drop (out-of-market stories are Tier 2 unless they signal a cross-market trend); transportation is a Tier 4 drop (Tier 3 under AI or Global Big Tech queries); security incidents are Tier 3.
- Defined three named operating rules (Section 3f): the headline rule, the cluster rule (up to 3 sources, primary then secondary then Google News), and the trigger cluster size rule (Phase 3 boolean-negate when over 50% of Google hits repeat Phases 1 to 2).
- Output migrated from an Excel workbook to a self-contained HTML report (Section 1a) rendered from a JSON data file (Section 1b). No openpyxl, no .xlsx. The data file is also the Phase 6 dedup memory, replacing the archived Working sheet.
- The selection checkbox is now a real clickable `<input type="checkbox">`: ticks autosave in the browser and export to `selections_{since}_{until}.json` for a later agent step (no fixed schema yet). Phase 0 renamed to Setup; the column-letter and tab-name conventions are dropped.

---

### Final quality gate before writing files

Before finalizing, validate internally:
- Visible article count increased meaningfully versus the sparse seed/first HTML and approaches the reference/second HTML coverage level.
- Header pills show Range, Articles, AI Agent, AI/GPT, Global Big Tech, Asia Big Tech, Social, Theme, and Selected count.
- Asia Big Tech is not left at only a token article count; if it remains very low, rerun official, regional, Google US, KR/JP, and local-language searches.
- Social is not left at only a token article count; if it remains very low, rerun Social Media Today and social platform source sweeps.
- AI/GPT is not left at only a token article count; if it remains very low, rerun TechCrunch, 9to5Google, Google Blog, OpenAI, Anthropic, Microsoft, Amazon, Meta, and NVIDIA sources.
- TechCrunch, 9to5Google, 9to5Mac, and Social Media Today completion logs exist.
- Google US was checked for every master query.
- Google KR/JP/local-language searches were checked for applicable Asia/local-language queries.
- Asia Big Tech official newsroom/source pages were checked before n/a.
- Every visible article row has a real checkbox and at least one real source URL.
- No visible article row has a broken or missing source link.
- No event is duplicated across multiple rows or master queries.
- Category order exactly matches Section 3b.
- Master query order exactly matches Section 3b or the seed HTML/runbook order.
- Headline format is `[Company] ... (YYYY.M.D)` with no zero padding in the suffix date.
- Every article date is within the run range.
- Static HTML render test passes with JavaScript disabled.
- `Export selections`, `Clear checks`, and checkbox `localStorage` autosave work.
- `records`, `validation`, `source_manifest`, `google_search_log`, `crawl_log`, `na_audit`, and `dedup_log` are saved in JSON or embedded metadata.
- The phrase `best-effort targeted crawl` does not appear in the final HTML.

Do not finalize the report if any of these checks fail; rerun the missing collection step instead. Do not show the full quality gate table in the default HTML. Save gate results to validation JSON/metadata.

## 6. Report template (fill this and save as report.html)

The weekly report must be generated as static HTML with pre-rendered article rows. The JSON data may still be embedded for checkbox export and validation metadata, but the visible article list must not depend on runtime JSON parsing. Article rows must already exist in the DOM at build time so the report is readable with JavaScript disabled. Keep the document title and visible heading as `Weekly Tech News Article List`.

Generate the HTML from the same final records used for validation metadata. Save verbose validation, source manifests, Google query logs, crawl logs, n/a audit evidence, and dedup logs under `records`, `validation`, `source_manifest`, `google_search_log`, `crawl_log`, `na_audit`, and `dedup_log`; do not show those tables in the default HTML unless explicitly requested.

The visible HTML article table uses this column order only: Select, Headline, Tier, Sources, Date. Do not add Category, Master Query, or Original Title as table columns; show category and master query as section/group headings.

The generated HTML must include this row structure for each visible article cluster:

```html
<tr class="article-row" data-cluster-id="..." data-category="AI/GPT" data-master-query="Gemini">
  <td class="select-cell"><input type="checkbox" class="row-check" data-cluster-id="..." aria-label="Select article"></td>
  <td class="headline-cell"><div class="headline-text">[Google] Gemini in Sheets language support 확대, spreadsheet 생성·편집 AI workflow의 다국어 접근성 강화 (2026.6.18)</div></td>
  <td class="tier-cell"><span class="tier-badge tier-1">Tier 1</span></td>
  <td class="source-cell"><a class="source-link" href="..." target="_blank" rel="noopener noreferrer">Source 1</a></td>
  <td class="date-cell">2026-06-18</td>
</tr>
```

Checkbox requirements:
- Checkbox must be a real `<input type="checkbox">`.
- Do not wrap it in a fake button, custom div, or non-clickable element.
- Do not pre-check any row.
- Autosave selected cluster IDs in `localStorage`.
- `Clear checks` clears all selected rows.
- `Export selections` must download selected full records as JSON.

Source link requirements:
- Show up to 3 source links.
- Use simple labels: `Source 1`, `Source 2`, `Source 3`.
- Links must open in a new tab.
- Preserve real publisher URLs where available.

The HTML report is for human article selection. Keep it minimal. Allowed in default HTML: title, date range, generated date, header pills, category/query headings, full article table, checkbox controls, source links, export selections button, clear checks button, and optional collapsed audit details. Not allowed in default HTML unless explicitly requested: huge validation/source-completion tables, every-site crawl manifests, raw Google query logs, or long crawler notes.

```html
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Weekly Tech News Article List</title>
<style>
  body{margin:0;background:#f6f7f9;color:#15171c;font:14px/1.5 system-ui,"Apple SD Gothic Neo","Noto Sans KR","Noto Sans JP",sans-serif}
  .wrap{max-width:1180px;margin:0 auto;padding:24px}
  header,.summary,.controls{margin-bottom:14px}
  table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #e5e7eb}
  th,td{padding:8px 10px;border-bottom:1px solid #e5e7eb;text-align:left;vertical-align:top}
  th{font-size:12px;background:#f1f3f5;color:#4b5563}
  .category-cell{width:120px}.query-cell{width:160px}.select-cell{width:70px;text-align:center}.tier-cell{width:70px}.date-cell{width:105px}
  .source-cell a{margin-right:8px;color:#2447d8;text-decoration:none}.source-cell a:hover{text-decoration:underline}
  .category-break td{background:#eef1fe;font-weight:700}.query-break td{background:#fafafa;color:#4b5563;font-weight:600}
  .na-row{color:#6b7280;font-style:italic}.selected{background:#f0fff7}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>Weekly Tech News Article List</h1>
    <p>Date range: {since} to {until} · Generated: {generated_at}</p>
  </header>
  <section class="summary">
    <span class="pill">Range {since}–{until}</span> <span class="pill">Articles {visible_count}</span> <span class="pill">AI Agent {ai_agent_count}</span> <span class="pill">AI/GPT {ai_gpt_count}</span> <span class="pill">Global Big Tech {global_big_tech_count}</span> <span class="pill">Asia Big Tech {asia_big_tech_count}</span> <span class="pill">Social {social_count}</span> <span class="pill">Theme {theme_count}</span> <span class="pill" id="selected-pill">Selected 0</span>
  </section>
  <section class="controls">
    <button id="export" type="button">Export selections</button>
    <button id="clear" type="button">Clear all</button>
    <span id="selected-count">0 selected</span>
  </section>
  <table aria-label="Article selection list">
    <thead>
      <tr><th>Select</th><th>Headline</th><th>Tier</th><th>Sources</th><th>Date</th></tr>
    </thead>
    <tbody>
      <!-- Pre-render category and master-query heading rows in strict order, then all visible article rows for each query. -->
      <tr class="category-break"><td colspan="5">AI/GPT</td></tr>
      <tr class="query-break"><td colspan="5">Gemini</td></tr>
      <tr class="article-row" data-cluster-id="..." data-category="AI/GPT" data-master-query="Gemini">
        <td class="select-cell"><input type="checkbox" class="row-check" data-cluster-id="..." aria-label="Select article"></td>
        <td class="headline-cell"><div class="headline-text">[Google] Gemini in Sheets language support 확대, spreadsheet 생성·편집 AI workflow의 다국어 접근성 강화 (2026.6.18)</div></td>
        <td class="tier-cell"><span class="tier-badge tier-1">Tier 1</span></td>
        <td class="source-cell"><a class="source-link" href="..." target="_blank" rel="noopener noreferrer">Source 1</a></td>
        <td class="date-cell">2026-06-18</td>
      </tr>
    </tbody>
  </table>
</div>
<script type="application/json" id="report-data">{ "run": {"since":"{since}", "until":"{until}"}, "data": [] }</script>
<script>
const RUN={since:"{since}",until:"{until}"};
const STORE_KEY=`selections:${RUN.since}_${RUN.until}`;
function selectedIds(){return [...document.querySelectorAll('.row-check:checked')].map(cb=>cb.dataset.clusterId)}
function save(){const ids=selectedIds();localStorage.setItem(STORE_KEY,JSON.stringify(ids));document.getElementById('selected-count').textContent=`${ids.length} selected`; const pill=document.getElementById('selected-pill'); if(pill) pill.textContent=`Selected ${ids.length}`;}
function restore(){let ids=[];try{ids=JSON.parse(localStorage.getItem(STORE_KEY)||'[]')}catch{};const set=new Set(ids);document.querySelectorAll('.row-check').forEach(cb=>{cb.checked=set.has(cb.dataset.clusterId);cb.closest('tr').classList.toggle('selected',cb.checked);cb.addEventListener('change',()=>{cb.closest('tr').classList.toggle('selected',cb.checked);save();});});save();}
function fullRecords(){try{return JSON.parse(document.getElementById('report-data').textContent).data||[]}catch{return []}}
document.getElementById('export').addEventListener('click',()=>{const ids=new Set(selectedIds());const selected=fullRecords().filter(r=>ids.has(r.cluster_id));const blob=new Blob([JSON.stringify({since:RUN.since,until:RUN.until,count:selected.length,selections:selected},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=`selections_${RUN.since}_${RUN.until}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);});
document.getElementById('clear').addEventListener('click',()=>{document.querySelectorAll('.row-check').forEach(cb=>{cb.checked=false;cb.closest('tr').classList.remove('selected')});save();});
restore();
</script>
</body>
</html>
```


### Final response requirements

At the end of the run, the agent should report only:
- HTML path
- JSON path
- total visible article count
- n/a audit count
- whether strict query order passed
- whether checkbox test passed
- whether local static render test passed

Do not include long explanations, audit tables, or caveats unless a quality gate failed.
