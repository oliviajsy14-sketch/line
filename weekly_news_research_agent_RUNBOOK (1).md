# Weekly Tech News Research Agent: Combined Runbook

You are the executing agent. When you are asked to run the weekly pipeline for a date range, follow this runbook end to end: collect that week's real news and write the two output files in Section 1 (the HTML report and the JSON data file). This file is your instructions, not the report itself. Section 0 says exactly what a run does.

**Purpose.** In one run, for a fixed list of master queries grouped into six categories over a given week, collect news article links from primary sources, Google News, and secondary sources (trusted news sites); group links covering the same event into clusters; render each cluster as one row (category, master query, a formatted headline, a clickable selection checkbox, and up to three source links) in a self-contained HTML report; and remove any story already covered last week.

The pipeline runs in seven phases (0 to 6): set up the run, collect and headline from primary sources, then secondary sources, then Google News, arrange each master query's stories by tier, mark empty queries n/a, and drop repeats. Headlines are written during collection, one per cluster. Collection uses the `web_search` and `web_fetch` tools. The deliverable is one self-contained `report_{since}_{until}.html`, rendered from a machine-readable `data_{since}_{until}.json` that also serves as next week's dedup memory; both are written by Python. See Section 0 for how to run it on Claude Code.

> This runbook merges two prior specs into one. The master query list comes from the canonical runbook; the per-query source maps in Section 4 are the union of both specs' links (deduped). The procedure has since been rearranged into the seven-phase flow in Section 4, and Section 3d defines the four-tier classification. There is one Query List, one HTML report, and one JSON data file. Weekly and Global are **not** split.

---

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
- **Report and data I/O.** Write a Python script (run with bash) that builds the two output files in Section 1: the machine-readable `data_{since}_{until}.json` (one record per cluster) and the self-contained `report_{since}_{until}.html` rendered from it. No Excel, no `openpyxl`. The HTML is one file with inline CSS and JS, declares `<meta charset="utf-8">`, and uses a CJK-capable font stack so Korean and Japanese render. Build `report.html` from the Section 6 template by replacing only its `#report-data` JSON block; do not hand-write the page. The template inserts every value with `textContent`/`href` and reads data as JSON, so quotes, brackets, and `&` are handled for you.
- **Filesystem.** Keep all working state in the project directory.

### Files and I/O contract
- Deliverable: `./output/report_{since}_{until}.html`, one self-contained HTML file (Section 1a).
- Data file: `./output/data_{since}_{until}.json`, one record per cluster (Section 1b). The report is rendered from this, and it is also the dedup memory.
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

One self-contained file, `./output/report_{since}_{until}.html`: inline CSS and JS, `<meta charset="utf-8">`, a CJK-capable font stack (for example `system-ui, "Apple SD Gothic Neo", "Noto Sans KR", "Noto Sans JP", sans-serif`), and no external requests. It is built from the ready-made template in Section 6: copy that template and replace only its `#report-data` JSON block with this run's records. Do not write the HTML from scratch each week.

Structure:
- A header showing the week range (`since` to `until`) and the generated date.
- The body is grouped by the six categories in run order (Section 4). Within a category, group by master query and show the label once. Within a master query, order rows by tier, Tier 1 first.
- One row per cluster, showing: a clickable selection checkbox; the headline (Section 2 format, rendered as normal text, never as code); a tier badge (Tier 1, 2, or 3); up to three source links as real clickable `<a href>` that open in a new tab; and the date.
- A master query with no surviving cluster shows a single `n/a` line (Phase 5), with no active checkbox.

Selection checkboxes:
- Each row has a real `<input type="checkbox">` the desk ticks for final selection. The agent never pre-ticks it.
- Each row carries its Cluster ID (for example a `data-cluster-id` attribute) so a tick maps back to one record.
- Ticks autosave in the browser (localStorage, keyed by the run dates plus Cluster ID) so a reload does not lose them.
- An "Export selections" button downloads `selections_{since}_{until}.json`: the ticked rows as full records (id, category, master query, company, headline, tier, sources, date) plus the run dates. There is no fixed downstream schema yet; this is a placeholder a later agent step can read or be adapted to.

Rendering rules:
- One cluster = one row = one headline = up to three source links.
- HTML-escape every dynamic value before injecting it: headlines contain `"` and `[ ]`, and source URLs contain `&`.
- Rows read grouped by category, with category and master query shown as headings.
- The `[Company]` tag in the headline is the owning company and may differ from the master query (master query `iOS` carries `[Apple]`; `WhatsApp` carries `[Meta]`). Sub-brands roll up to their parent: Facebook, Instagram, and WhatsApp carry `[Meta]`; YouTube, Gmail, and Android carry `[Google]`; Amazon Prime carries `[Amazon]`. Whole-market and multi-company stories carry `[Market]`.

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

- All Other AI Agent News
- OpenClaw (Moltbot, Clawdbot)
- Paperclip
- BabyAGI
- Microsoft AutoGen
- AutoGPT
- AgentGPT
- Claude Cowork
- A.(에이닷)
- KIRA
- Wrtn Crack
- Rinna
- Cotomo
- CrewAI
- AutoGen
- LangGraph
- Chai
- Nomi
- Kindroid
- Paradot
- Replika
- Poketomo
- Hume AI
- Mersoom
- Bot Madang
- NVIDIA

#### 2. AI/GPT

- All Other AI/GPT News
- Lovable
- Generative AI
- OpenAI
- ChatGPT
- Codex
- Sora
- Meta AI
- Scale AI
- Google AI
- Gemini
- Veo
- NotebookLM
- Google Chrome
- Amazon AI
- Nova AI
- Trainium
- Anthropic
- Claude
- Claude Code
- Microsoft AI
- Microsoft Edge
- Bing
- Copilot
- Apple AI
- Safari
- Databricks
- Thinking Machines Lab
- Perplexity AI
- Comet
- Stability AI
- Anysphere (Cursor)
- ElevenLabs
- Speak AI
- Writer AI
- Ayar Labs
- Physical Intelligence
- Inflection AI
- Moonshot AI
- Canva AI
- Le Chat
- Leonardo AI
- Cohere
- Skywalker.ai
- Kling AI
- Seedance
- Arc Browser
- Dia Browser
- Brave Browser
- Opera One
- Sigma Browser (SigmaOS)
- Zen Browser
- Wavebox
- Vivaldi Browser
- Sidekick Browser
- Shift Browser
- Orion Browser
- Maxthon Browser
- Firefox
- Samsung Internet
- UC Browser
- CryptoTab Browser
- AI Startup
- Stable Diffusion
- DALL-E
- Content Generator
- Craiyon
- Midjourney
- MyHeritage
- Voice Synthesis
- Dream Fusion
- AI Bot
- AI Healthcare
- Image AI
- AI Assistant
- AI Plugin
- Sam Altman
- LLM
- Inflection AI (Pi)
- Chatbot
- Adobe AI
- Adobe Firefly
- character.ai
- Zeta
- MDM
- yandex
- Kakao Brain
- Kakao AI
- Japan AI
- Korea AI
- China AI
- US AI
- AI Character
- Copyright Shield

#### 3. Global Big Tech

- Meta
- Facebook
- Instagram
- WhatsApp
- Amazon
- Amazon Prime
- Apple
- iOS
- Netflix
- Google
- YouTube
- Android
- Gmail
- Microsoft
- Grab

#### 4. Asia Big Tech

- Rakuten (楽天市場)
- note（ノート)
- DeNA
- Gree (グリー)
- Gunosy (グノシー)
- Time Tree (タイムツリ)
- Mercari(メルカリ)
- The Bridge
- Ascii Startup
- CNET
- Diamond
- Kakao
- 카카오
- 카카오톡
- Coupang
- 쿠팡
- Toss
- 토스
- Tencent
- WeChat (微信)
- ByteDance
- Alibaba

#### 5. Social

- TikTok
- Douyin
- Snapchat
- Telegram
- Pinterest
- X
- XChat
- BlueSky
- Twitch
- BeReal
- Discord

#### 6. Theme

- Other Super Apps
- Spotify
- Linkedin
- Figma
- Paypal
- Reddit
- VSCO
- locket
- MZ Gen
- Gen Z
- 1020 trend
- Social app
- Tech Crunch Startup

Notes:
- The `All Other ...` entries (and `Other Super Apps`) are catch-all queries for category-relevant stories not matched by a more specific query in that category.
- Sub-brand rollups for tagging: Facebook, Instagram, and WhatsApp roll up to Meta; YouTube, Gmail, and Android roll up to Google; Amazon Prime rolls up to Amazon. A sub-brand story is filed once under its own master query but tagged with the parent company (see the routing rule).
- NVIDIA was tagged `AI Agent SR` in the source sheet; it is folded into the AI Agent category here.
- Some master queries carried alternate labels across the two source sheets (for example `Wrtn Crack`/`Crack (크랙)`, `Gemini`/`GeminI`). They are the same query; use the label above and treat the variant as an alias.

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
- Order a cluster's sources primary, then secondary, then Google News. Once a cluster holds 3 sources, drop any further source for that story.
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

Weight the secondary outlets by category: Global English outlets (techcrunch.com through 9to5google.com, plus the-decoder.com, marktechpost.com, siliconangle.com) are the main surface for AI Agent, AI/GPT, Global Big Tech, and Social; Asia-focused English (restofworld.org, techinasia.com, kr-asia.com, scmp.com) for Asia Big Tech, super apps, and Theme; Korean (zdnet.co.kr, etnews.com, bloter.net, platum.kr, thebell.co.kr) for the Korean Asia Big Tech queries and Korea AI; Japanese (itmedia.co.jp, watch.impress.co.jp, ascii.jp, japan.cnet.com, asia.nikkei.com) for the Japanese queries; Chinese (technode.com, 36kr.com, caixinglobal.com) for the Chinese queries. Several of these paywall (bloomberg.com, reuters.com, theinformation.com, asia.nikkei.com, caixinglobal.com, scmp.com); treat a paywalled article as a lead and prefer an accessible source for the same event.

### Phase 3: Google News
For each master query, search Google News across three editions: Google US (`US / en`), Google KR (`KR / ko`), and Google JP (`JP / ja`). On Claude Code you have no live browser, so use the Google News RSS endpoints and the `web_search` fallback from Section 0; apply the date window with `after:` / `before:` (`before:` is exclusive, pass `until + 1 day`), and do the date filtering and cross-edition dedup in code. For an Asian company, search both its English name in Google US and its local-language name in the local edition (for example Toss in Google US and `토스` in Google KR; Rakuten in Google US and `楽天` in Google JP). Pool the editions into one set and dedup the same event across them. Use the Phase 3 search-term overrides below for any query whose bare name is noisy.

Apply the **trigger cluster size rule** (Section 3f): if more than 50% of a query's Google results only repeat coverage already captured in Phases 1 and 2, re-run the search with the dominant repeated term negated (for example `Claude -Fable`) and read up to 100 results from that negated search. Apply the **cluster rule** the same way as Phase 2: add a Google source to an existing cluster up to the 3-source cap, or start a new cluster if the event is new, then write its headline under the headline rule. A Google News link is the basis for a cluster's headline only when the cluster has no primary or secondary source.

### Phase 4: Tier arrangement
With the headlines and clusters from Phases 1 to 3 in hand, go through every master query in the category and assign each cluster a tier using Section 3d. First apply the content exclusion rules (Tier 4, Section 3d.4) and drop those clusters outright. Then classify each surviving cluster as Tier 1, 2, or 3 by the Section 3d order, reading the cluster's opened source where the headline alone is not enough to judge. Arrange each master query's clusters by tier, Tier 1 first, then Tier 2, then Tier 3, and store the tier on each cluster record in the data file. Nothing else is cut: every cluster that is not Tier 4 and not a last-week repeat is written.

### Phase 5: N/a establishment
After Phases 1 to 3, any master query with no surviving cluster gets a single n/a entry, so the report shows coverage rather than a silent gap: Category and Master Query filled, Headline `n/a`, no active checkbox, no sources. A genuine "checked, nothing to report" is `n/a`; a fetch or access failure is not `n/a`, it goes to the run log.

### Phase 6: Repetition check
Two passes. First, the across-week check: load last week's data file from `previous_week.data_path` and, for each cluster this week, decide whether it covers the **same news event** as any last-week cluster (compare on `article_texts`), even if the specific articles differ; set `dedup_status = drop` for genuine repeats (Tier 4 #6) and `keep` for real follow-on developments with new facts or escalation. Second, the within-week check: compare this week's clusters against each other and drop any duplicate, so the same event is not rendered twice across master queries. Save this week's data file to the archive path so next week's check can read it. Then build the deliverable: copy the template in Section 6 and put the kept records into its `#report-data` JSON block (`run` = the dates; `data` = each kept cluster's display fields). Save the filled file as `report_{since}_{until}.html`.

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
- The report row carries five fields: Category, Master Query, Headline, a clickable selection checkbox, and up to three source links (Section 1a). The checkbox is a real `<input>` the desk ticks; the agent never pre-ticks it. Source links render as clickable anchors, primary then secondary then Google News.
- Source taxonomy simplified to two defined types: Primary source (the query's official channel) and Secondary source (a defined news outlet or catch-all or keyword feed). Links found via Google search at run time are the third, undefined type. This replaces the earlier Group 1 / Group 2 / Group 3 split.
- Agent-efficiency notes: resolve Google News redirects only for kept links; add the US-edition pass for an Asian query only when the local-edition pass is thin; cap each cluster at 3 sources so collection stops early; all phases run inline, no spawned sub-agents.
- Procedure rearranged into Phases 0 to 6: Phase 0 setup; Phase 1 primary sources, one headline per link; Phase 2 secondary sources, clustered into Phase 1 with a 3-source cap; Phase 3 Google News across US, KR, and JP with the trigger cluster size rule; Phase 4 tier arrangement; Phase 5 n/a establishment; Phase 6 repetition check (across-week and within-week). Headlines are now written during collection, not in a separate pass.
- Replaced the hard/soft exclusion split and the old selection tiers with a single four-tier system (Section 3d): Tier 4 drops; Tiers 1 to 3 are kept and ranked. Geography is no longer a hard drop (out-of-market stories are Tier 2 unless they signal a cross-market trend); transportation is a Tier 4 drop (Tier 3 under AI or Global Big Tech queries); security incidents are Tier 3.
- Defined three named operating rules (Section 3f): the headline rule, the cluster rule (up to 3 sources, primary then secondary then Google News), and the trigger cluster size rule (Phase 3 boolean-negate when over 50% of Google hits repeat Phases 1 to 2).
- Output migrated from an Excel workbook to a self-contained HTML report (Section 1a) rendered from a JSON data file (Section 1b). No openpyxl, no .xlsx. The data file is also the Phase 6 dedup memory, replacing the archived Working sheet.
- The selection checkbox is now a real clickable `<input type="checkbox">`: ticks autosave in the browser and export to `selections_{since}_{until}.json` for a later agent step (no fixed schema yet). Phase 0 renamed to Setup; the column-letter and tab-name conventions are dropped.

---

## 6. Report template (fill this and save as report.html)

This is the deliverable's exact HTML. It is self-contained (inline CSS and JS, no external requests, `<meta charset="utf-8">`, a CJK font stack) and already implements Section 1a: rows grouped by category then master query with Tier 1 first, a tier badge, up to three clickable source links, real clickable checkboxes that autosave in the browser, and an Export button that downloads `selections_{since}_{until}.json`. Every value is inserted with `textContent`/`href`, so it is HTML-escaped automatically.

To produce a week's report, copy the file below verbatim and replace only the JSON inside the `<script type="application/json" id="report-data">` block, then save it as `report_{since}_{until}.html`. Change nothing outside that JSON. Because the data is JSON, all quotes and ampersands are handled for you; just keep the JSON valid. (If any value could literally contain the text `</script>`, escape the `<` as `\u003c`.) The JSON shape:

```json
{
  "run": { "since": "2026-06-17", "until": "2026-06-23" },
  "data": [
    { "cluster_id": "c001", "category": "AI/GPT", "master_query": "ChatGPT", "company": "OpenAI",
      "tier": 1, "date": "2026-06-17",
      "headline": "[OpenAI] ChatGPT Projects 공유 기능 \"GA\" 공개 (2026.6.17)",
      "sources": ["https://openai.com/index/projects", "https://techcrunch.com/2026/06/17/openai"] },
    { "cluster_id": "c099", "category": "AI/GPT", "master_query": "Codex", "is_na": true, "headline": "n/a", "sources": [] }
  ]
}
```

`data` is the display subset of the records you wrote to `data.json`: one object per kept cluster (order does not matter; the page groups and sorts). Use `"is_na": true` for a master query with no story this week (it renders with no checkbox). The embedded HTML:

```html
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Weekly Tech Research · 2026.6.17–2026.6.23</title>
<style>
  :root{
    --ink:#15171c; --paper:#ffffff; --soft:#f5f6f8; --line:#e6e8ec; --muted:#6a7280;
    --accent:#2f4cdd; --accent-soft:#eef1fe;
    --t1:#3b3f8f; --t1-bg:#ecedfb; --t2:#9a5b00; --t2-bg:#fdf3e3; --t3:#566174; --t3-bg:#eef1f4;
    --sel:#f0fff7; --sel-line:#9fe3c2;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{
    margin:0; background:var(--soft); color:var(--ink);
    font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans KR","Apple SD Gothic Neo","Noto Sans JP",Arial,sans-serif;
    -webkit-font-smoothing:antialiased;
  }
  .wrap{max-width:980px;margin:0 auto;padding:0 20px 96px}

  /* sticky toolbar */
  .bar{
    position:sticky; top:0; z-index:20; background:rgba(255,255,255,.9); backdrop-filter:blur(8px);
    border-bottom:1px solid var(--line); margin:0 -20px 0; padding:14px 20px;
    display:flex; align-items:center; gap:16px; flex-wrap:wrap;
  }
  .bar .lead{display:flex;flex-direction:column;line-height:1.2;margin-right:auto}
  .bar .lead b{font-size:15px;letter-spacing:-.01em}
  .bar .lead span{font-size:12.5px;color:var(--muted)}
  .count{font-variant-numeric:tabular-nums;font-weight:700;color:var(--accent)}
  .btn{
    appearance:none;border:1px solid var(--line);background:#fff;color:var(--ink);
    font:600 14px/1 inherit;padding:10px 14px;border-radius:9px;cursor:pointer;white-space:nowrap;
  }
  .btn:hover{border-color:#c9cdd4}
  .btn.primary{background:var(--accent);border-color:var(--accent);color:#fff}
  .btn.primary:hover{background:#2740c4}
  .btn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

  header.page{padding:40px 0 8px}
  .eyebrow{margin:0;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
  h1{margin:.25em 0 .15em;font-size:clamp(1.7rem,3.4vw,2.4rem);letter-spacing:-.02em}
  .sub{margin:.2em 0 0;color:var(--muted);font-size:14.5px}
  .sample{display:inline-block;margin-top:10px;font-size:12px;color:#9a5b00;background:var(--t2-bg);border:1px solid #f0dcb6;border-radius:999px;padding:3px 10px}

  .cat{margin-top:40px}
  .cat > h2{
    display:flex;align-items:baseline;gap:10px;margin:0 0 4px;font-size:1.15rem;letter-spacing:-.01em;
    padding-bottom:8px;border-bottom:2px solid var(--ink);
  }
  .cat > h2 .n{font-size:.8rem;color:var(--muted);font-weight:600;font-variant-numeric:tabular-nums}
  .mq{margin:18px 0 0}
  .mq > h3{margin:0 0 2px;font-size:.82rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}

  .row{
    display:grid;grid-template-columns:26px 1fr;gap:14px;align-items:start;
    padding:14px 12px;border:1px solid var(--line);border-radius:11px;background:var(--paper);margin-top:8px;
  }
  .row.sel{background:var(--sel);border-color:var(--sel-line)}
  .row.na{background:var(--soft);border-style:dashed}
  .cbx{margin-top:3px}
  .cbx input{width:18px;height:18px;accent-color:var(--accent);cursor:pointer}
  .head{font-size:15.5px;line-height:1.5;letter-spacing:-.005em}
  .row.na .head{color:var(--muted);font-style:italic}
  .meta{margin-top:7px;display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:13px;color:var(--muted)}
  .tier{font-weight:700;font-size:11.5px;letter-spacing:.02em;padding:2px 8px;border-radius:999px;border:1px solid transparent}
  .t1{color:var(--t1);background:var(--t1-bg);border-color:#d6d8f4}
  .t2{color:var(--t2);background:var(--t2-bg);border-color:#f0dcb6}
  .t3{color:var(--t3);background:var(--t3-bg);border-color:#dde2e8}
  .date{font-variant-numeric:tabular-nums}
  .srcs{display:flex;gap:8px;flex-wrap:wrap}
  .srcs a{
    color:var(--accent);text-decoration:none;font-size:12.5px;border:1px solid var(--accent-soft);
    background:var(--accent-soft);padding:2px 8px;border-radius:7px;max-width:280px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  }
  .srcs a:hover{text-decoration:underline}
  .dot{color:#cdd2da}

  .toast{
    position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);
    background:var(--ink);color:#fff;padding:11px 16px;border-radius:10px;font-size:13.5px;
    opacity:0;pointer-events:none;transition:.25s;z-index:40;max-width:90vw;
  }
  .toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
  @media (max-width:560px){ .row{grid-template-columns:24px 1fr} .bar .lead{margin-right:0;width:100%} }
  @media (prefers-reduced-motion:reduce){ *{transition:none!important;scroll-behavior:auto} }
</style>
</head>
<body>
<div class="wrap">

  <div class="bar">
    <div class="lead">
      <b>주간 리서치 · 최종 선별</b>
      <span id="range"></span>
    </div>
    <div><span class="count" id="count">0</span> selected</div>
    <button class="btn" id="clear" type="button">Clear all</button>
    <button class="btn primary" id="export" type="button">Export selections</button>
  </div>

  <header class="page">
    <p class="eyebrow">Weekly Tech News Research</p>
    <h1>Global IT · AI 주간 리서치</h1>
    <p class="sub" id="subline"></p>
  </header>

  <main id="report" aria-live="polite"></main>
</div>

<div class="toast" id="toast"></div>

<!-- ====== AGENT-INJECTED DATA: replace the JSON below on every run ====== -->
<script type="application/json" id="report-data">
{ "run": { "since": "YYYY-MM-DD", "until": "YYYY-MM-DD" }, "data": [] }
</script>

<script>
/* CATEGORY_ORDER is fixed. RUN and DATA are read from the JSON in the
   #report-data block below, which is the ONLY thing the agent replaces. */
const CATEGORY_ORDER = ["AI Agent","AI/GPT","Global Big Tech","Asia Big Tech","Social","Theme"];
let RUN = { since:"", until:"" }, DATA = [];
try {
  const _p = JSON.parse(document.getElementById("report-data").textContent);
  RUN = _p.run || RUN;
  DATA = Array.isArray(_p.data) ? _p.data : [];
} catch (e) { console.error("report-data JSON failed to parse:", e); }

/* ----- helpers ----- */
const $ = (s,r=document)=>r.querySelector(s);
const fmtDot = d => d.replaceAll("-",".").replace(/\.0?(\d)/g,(m,x,o)=> o===4? "."+x : m); // 2026-06-17 -> 2026.6.17
function pretty(d){ const [y,m,da]=d.split("-"); return `${y}.${+m}.${+da}`; }
const STORE_KEY = `selections:${RUN.since}_${RUN.until}`;

function loadChecked(){
  try { return new Set(JSON.parse(localStorage.getItem(STORE_KEY) || "[]")); }
  catch { return new Set(); }
}
function saveChecked(){
  const ids = [...document.querySelectorAll('input[data-cluster-id]:checked')].map(i=>i.dataset.clusterId);
  try { localStorage.setItem(STORE_KEY, JSON.stringify(ids)); } catch {}
  $("#count").textContent = ids.length;
}

/* ----- render (textContent + href => auto-escaped) ----- */
function render(){
  const root = $("#report");
  root.textContent = "";
  const checked = loadChecked();
  const byCat = {};
  for(const r of DATA){ (byCat[r.category] ||= []).push(r); }

  for(const cat of CATEGORY_ORDER){
    const rows = byCat[cat]; if(!rows) continue;
    const realCount = rows.filter(r=>!r.is_na).length;
    const sec = document.createElement("section"); sec.className="cat";
    const h2 = document.createElement("h2");
    h2.append(cat);
    const n = document.createElement("span"); n.className="n"; n.textContent = `${realCount} stor${realCount===1?"y":"ies"}`;
    h2.append(n); sec.append(h2);

    // group by master query, preserve first-seen order
    const mqOrder = [...new Set(rows.map(r=>r.master_query))];
    for(const mq of mqOrder){
      const grp = document.createElement("div"); grp.className="mq";
      const h3 = document.createElement("h3"); h3.textContent = mq; grp.append(h3);

      rows.filter(r=>r.master_query===mq)
          .sort((a,b)=>(a.tier??99)-(b.tier??99))
          .forEach(r=>{
        const row = document.createElement("div");
        row.className = "row" + (r.is_na?" na":"");
        // checkbox cell
        const cbWrap = document.createElement("div"); cbWrap.className="cbx";
        if(!r.is_na){
          const cb = document.createElement("input");
          cb.type="checkbox"; cb.dataset.clusterId=r.cluster_id;
          cb.setAttribute("aria-label","select: "+r.headline);
          cb.checked = checked.has(r.cluster_id);
          cb.addEventListener("change",()=>{ row.classList.toggle("sel",cb.checked); saveChecked(); });
          if(cb.checked) row.classList.add("sel");
          cbWrap.append(cb);
        }
        row.append(cbWrap);
        // content cell
        const body = document.createElement("div");
        const head = document.createElement("div"); head.className="head"; head.textContent=r.headline;
        body.append(head);
        if(!r.is_na){
          const meta = document.createElement("div"); meta.className="meta";
          const tier = document.createElement("span"); tier.className="tier t"+r.tier; tier.textContent="Tier "+r.tier;
          const date = document.createElement("span"); date.className="date"; date.textContent=pretty(r.date);
          meta.append(tier, date);
          if(r.sources?.length){
            const dot=document.createElement("span"); dot.className="dot"; dot.textContent="·"; meta.append(dot);
            const srcs=document.createElement("span"); srcs.className="srcs";
            r.sources.slice(0,3).forEach(u=>{
              const a=document.createElement("a"); a.href=u; a.target="_blank"; a.rel="noopener noreferrer";
              try{ a.textContent=new URL(u).hostname.replace(/^www\./,""); }catch{ a.textContent=u; }
              srcs.append(a);
            });
            meta.append(srcs);
          }
          body.append(meta);
        }
        row.append(body);
        grp.append(row);
      });
      sec.append(grp);
    }
    root.append(sec);
  }
  saveChecked(); // sync count
}

/* ----- export ----- */
function buildSelectionsJSON(){
  const ids = [...document.querySelectorAll('input[data-cluster-id]:checked')].map(i=>i.dataset.clusterId);
  const set = new Set(ids);
  const selected = DATA.filter(r=>set.has(r.cluster_id)).map(r=>({
    cluster_id:r.cluster_id, category:r.category, master_query:r.master_query,
    company:r.company, headline:r.headline, tier:r.tier, sources:r.sources, date:r.date
  }));
  return JSON.stringify({ since:RUN.since, until:RUN.until, generated:new Date().toISOString(),
                          count:selected.length, selections:selected }, null, 2);
}
function download(json){
  const blob = new Blob([json], {type:"application/json"});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href=url; a.download=`selections_${RUN.since}_${RUN.until}.json`;
  document.body.append(a); a.click(); a.remove();
  setTimeout(()=>URL.revokeObjectURL(url), 1000);
}
function toast(msg){ const t=$("#toast"); t.textContent=msg; t.classList.add("show"); setTimeout(()=>t.classList.remove("show"),2200); }

/* ----- wire up ----- */
function init(){
  $("#range").textContent = `${pretty(RUN.since)} – ${pretty(RUN.until)}`;
  $("#subline").textContent = `${pretty(RUN.since)} – ${pretty(RUN.until)} · 6개 카테고리 · Tier 1 우선 정렬`;
  render();
  $("#export").addEventListener("click",()=>{
    const json = buildSelectionsJSON();
    const n = JSON.parse(json).count;
    if(n===0){ toast("No rows selected yet. Tick the stories to keep, then export."); return; }
    download(json); toast(`Exported ${n} selected row${n===1?"":"s"} to selections_${RUN.since}_${RUN.until}.json`);
  });
  $("#clear").addEventListener("click",()=>{
    document.querySelectorAll('input[data-cluster-id]:checked').forEach(cb=>{ cb.checked=false; cb.closest(".row").classList.remove("sel"); });
    saveChecked(); toast("Cleared all selections.");
  });
}
if(typeof document!=="undefined" && document.readyState!=="loading") init();
else if(typeof document!=="undefined") document.addEventListener("DOMContentLoaded", init);

/* test hook (no effect in browser) */
if(typeof window!=="undefined"){ window.__test = { buildSelectionsJSON, saveChecked, STORE_KEY, DATA, RUN }; }
</script>
</body>
</html>
```
