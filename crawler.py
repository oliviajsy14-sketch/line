#!/usr/bin/env python3
"""Runbook-based weekly tech news crawler.

The script intentionally keeps dependencies to the Python standard library so it can
run in Codex and in local newsroom environments. It expands Google News RSS across
keyword x edition combinations, ingests every RSS item into candidates before strict
filtering, crawls every loaded source URL through concrete collection routes, and
writes the JSON, diagnostics, archive copy, and static HTML checklist outputs.
"""
import argparse
import datetime as dt
import email.utils
import hashlib
import html
import importlib.util
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

RUNBOOK = Path("weekly_news_research_agent_RUNBOOK2.md")
OUT = Path("output")
ARC = Path("archive")
UA = "Mozilla/5.0 weekly-news-crawler/3.0"
MAX_BYTES = 2_000_000

CATEGORY_ORDER = ["AI Agent", "AI/GPT", "Global Big Tech", "Asia Big Tech", "Social", "Theme"]
MASTER_QUERY_ORDER = {
    "AI Agent": "All Other AI Agent News, OpenClaw (Moltbot, Clawdbot), Paperclip, BabyAGI, Microsoft AutoGen, AutoGPT, AgentGPT, Claude Cowork, A.(에이닷), KIRA, Wrtn Crack, Rinna, Cotomo, CrewAI, AutoGen, LangGraph, Chai, Nomi, Kindroid, Paradot, Replika, Poketomo, Hume AI, Mersoom, Bot Madang, NVIDIA".split(", "),
    "AI/GPT": "All Other AI/GPT News, Lovable, Generative AI, OpenAI, ChatGPT, Codex, Sora, Meta AI, Scale AI, Google AI, Gemini, Veo, NotebookLM, Google Chrome, Amazon AI, Nova AI, Trainium, Anthropic, Claude, Claude Code, Microsoft AI, Microsoft Edge, Bing, Copilot, Apple AI, Safari, Databricks, Thinking Machines Lab, Perplexity AI, Comet, Stability AI, Anysphere (Cursor), ElevenLabs, Speak AI, Writer AI, Ayar Labs, Physical Intelligence, Inflection AI, Moonshot AI, Canva AI, Le Chat, Leonardo AI, Cohere, Skywalker.ai, Kling AI, Seedance, Arc Browser, Dia Browser, Brave Browser, Opera One, Sigma Browser (SigmaOS), Zen Browser, Wavebox, Vivaldi Browser, Sidekick Browser, Shift Browser, Orion Browser, Maxthon Browser, Firefox, Samsung Internet, UC Browser, CryptoTab Browser, AI Startup, Stable Diffusion, DALL-E, Content Generator, Craiyon, Midjourney, MyHeritage, Voice Synthesis, Dream Fusion, AI Bot, AI Healthcare, Image AI, AI Assistant, AI Plugin, Sam Altman, LLM, Inflection AI (Pi), Chatbot, Adobe AI, Adobe Firefly, character.ai, Zeta, MDM, yandex, Kakao Brain, Kakao AI, Japan AI, Korea AI, China AI, US AI, AI Character, Copyright Shield".split(", "),
    "Global Big Tech": "Meta, Facebook, Instagram, WhatsApp, Amazon, Amazon Prime, Apple, iOS, Netflix, Google, YouTube, Android, Gmail, Microsoft, Grab".split(", "),
    "Asia Big Tech": "Rakuten (楽天市場), note（ノート), DeNA, Gree (グリー), Gunosy (グノシー), Time Tree (タイムツリ), Mercari(メルカリ), The Bridge, Ascii Startup, CNET, Diamond, Kakao, 카카오, 카카오톡, Coupang, 쿠팡, Toss, 토스, Tencent, WeChat (微信), ByteDance, Alibaba".split(", "),
    "Social": "TikTok, Douyin, Snapchat, Telegram, Pinterest, X, XChat, BlueSky, Twitch, BeReal, Discord".split(", "),
    "Theme": "Other Super Apps, Spotify, Linkedin, Figma, Paypal, Reddit, VSCO, locket, MZ Gen, Gen Z, 1020 trend, Social app, Tech Crunch Startup".split(", "),
}
ALIASES = {"Facebook": "Meta", "Instagram": "Meta", "WhatsApp": "Meta", "YouTube": "Google", "Android": "Google", "Gmail": "Google", "Amazon Prime": "Amazon", "iOS": "Apple", "카카오톡": "Kakao", "카카오": "Kakao", "쿠팡": "Coupang", "토스": "Toss", "WeChat (微信)": "Tencent"}
GOOGLE_NEWS_KEYWORDS = [
    "OpenAI", "ChatGPT", "GPT", "Anthropic", "Claude", "Google Gemini", "AI Overview",
    "Microsoft Copilot", "Amazon Bedrock", "Meta AI", "Apple Intelligence", "NVIDIA AI",
    "AI agent", "AI model", "LLM", "generative AI", "AI search", "AI advertising",
    "AI shopping", "AI security", "AI regulation", "AI infrastructure", "enterprise AI",
    "ByteDance AI", "Alibaba Qwen", "Tencent AI", "Kakao AI", "LINE AI",
]
GOOGLE_EDITIONS = [
    {"name": "US", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"name": "KR", "hl": "ko", "gl": "KR", "ceid": "KR:ko"},
    {"name": "JP", "hl": "ja", "gl": "JP", "ceid": "JP:ja"},
    {"name": "Global", "hl": "en", "gl": "US", "ceid": "US:en"},
]
AI_TERMS = ["ai", "gpt", "llm", "agent", "agentic", "chatbot", "copilot", "gemini", "claude", "openai", "anthropic", "生成ai", "인공지능", "생성형", "챗gpt", "エーアイ", "人工知能"]


def now_z():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def fetch(url, timeout=6):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/rss+xml,application/xml;q=0.9,*/*;q=0.8"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return {"ok": True, "url": url, "final_url": r.geturl(), "content_type": r.headers.get_content_type(), "data": r.read(MAX_BYTES), "error": None}
    except Exception as exc:
        return {"ok": False, "url": url, "final_url": url, "content_type": None, "data": b"", "error": f"{type(exc).__name__}: {exc}"}


def clean(text):
    return re.sub(r"\s+", " ", re.sub("<.*?>", "", html.unescape(text or ""))).strip()


def parse_date(value):
    if not value:
        return None
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed:
            return parsed.date().isoformat()
    except Exception:
        pass
    match = re.search(r"(20\d\d)[-/\.](\d{1,2})[-/\.](\d{1,2})", value)
    if match:
        return f"{int(match.group(1)):04d}-{int(match.group(2)):02d}-{int(match.group(3)):02d}"
    return None


def in_range(date, since, until):
    return bool(date and since <= date <= until)


def canonical_url(url):
    if not url:
        return ""
    url = html.unescape(url.strip())
    parsed = urllib.parse.urlsplit(url)
    if not parsed.scheme:
        return ""
    query = [(k, v) for k, v in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True) if not k.lower().startswith("utm_") and k.lower() not in {"fbclid", "gclid"}]
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path or "/", urllib.parse.urlencode(query), ""))


def rss_items(xml_bytes, fallback_source=""):
    items = []
    try:
        root = ET.fromstring(xml_bytes)
    except Exception:
        return items
    for item in root.findall(".//item"):
        src = item.find("source")
        source_url = src.get("url") if src is not None else ""
        link = item.findtext("link") or source_url or ""
        items.append({
            "title": clean(item.findtext("title")),
            "url": clean(source_url or link),
            "google_url": clean(link) if "news.google." in link else "",
            "date": parse_date(item.findtext("pubDate") or item.findtext("date") or item.findtext("{http://purl.org/dc/elements/1.1/}date")),
            "source_name": clean(src.text if src is not None else fallback_source),
            "snippet": clean(item.findtext("description")),
        })
    for item in root.findall(".//{http://www.w3.org/2005/Atom}entry"):
        link = ""
        for node in item.findall("{http://www.w3.org/2005/Atom}link"):
            if node.get("href"):
                link = node.get("href")
                break
        items.append({
            "title": clean(item.findtext("{http://www.w3.org/2005/Atom}title")),
            "url": clean(link),
            "google_url": "",
            "date": parse_date(item.findtext("{http://www.w3.org/2005/Atom}updated") or item.findtext("{http://www.w3.org/2005/Atom}published")),
            "source_name": fallback_source,
            "snippet": clean(item.findtext("{http://www.w3.org/2005/Atom}summary")),
        })
    return items


def extract_sources():
    text = RUNBOOK.read_text(encoding="utf-8")
    sources = []
    in_pool = False
    for line in text.splitlines():
        if line.strip() == "additional_source_url_pool:":
            in_pool = True
            continue
        if in_pool:
            if line.startswith("  - "):
                sources.append(line.split("- ", 1)[1].strip())
            elif line and not line.startswith(" "):
                in_pool = False
    # Include official/source-map URLs too, not only the additional pool.
    for match in re.findall(r"https?://[^\s,)]+", text):
        sources.append(match.rstrip(".、。"))
    return list(dict.fromkeys(sources))


def google_news_url(query, since, until, edition):
    before = (dt.date.fromisoformat(until) + dt.timedelta(days=1)).isoformat()
    encoded = urllib.parse.quote_plus(f"{query} after:{since} before:{before}")
    return f"https://news.google.com/rss/search?q={encoded}&hl={edition['hl']}&gl={edition['gl']}&ceid={edition['ceid']}"


def add_candidate(candidates, item, route, query, category="AI/GPT", master_query="All Other AI/GPT News", diagnostics=None):
    title = clean(item.get("title"))
    url = canonical_url(item.get("url")) or canonical_url(item.get("google_url"))
    reason = None
    if not title:
        reason = "missing_title"
    elif not url:
        reason = "missing_or_invalid_url"
    if reason:
        if diagnostics is not None:
            diagnostics["skip_reasons"][reason] = diagnostics["skip_reasons"].get(reason, 0) + 1
            if route == "google_news":
                diagnostics["google_news_skip_reasons"][reason] = diagnostics["google_news_skip_reasons"].get(reason, 0) + 1
                diagnostics["google_news_skipped_count"] += 1
        return False
    candidates.append({
        "title": title,
        "url": url,
        "date": item.get("date"),
        "source_name": item.get("source_name") or urllib.parse.urlparse(url).netloc,
        "snippet": item.get("snippet") or "",
        "route": route,
        "query": query,
        "category": category,
        "master_query": master_query,
    })
    return True


def discover_feed_urls(source_url, timeout, log):
    base = source_url.rstrip("/")
    candidates = [base + suffix for suffix in ["/feed", "/rss", "/rss.xml", "/feed.xml", "/atom.xml"]]
    home = fetch(source_url, timeout)
    log["direct_fetch_ok"] = home["ok"]
    if not home["ok"]:
        log["direct_fetch_error"] = home["error"]
    else:
        text = home["data"].decode("utf-8", "ignore")
        for hrefs in re.findall(r"<link[^>]+(?:type=[\"']application/(?:rss|atom)\+xml[\"'][^>]+href=[\"']([^\"']+)|href=[\"']([^\"']+)[\"'][^>]+type=[\"']application/(?:rss|atom)\+xml)", text, re.I):
            href = hrefs[0] or hrefs[1]
            candidates.append(urllib.parse.urljoin(home["final_url"], href))
    return list(dict.fromkeys(candidates)), home


def crawl_rss_feeds(source_url, timeout, diagnostics):
    log = {"source": source_url, "method": "rss_feed_discovery", "attempted": True, "urls_attempted": [], "items_added": 0, "errors": []}
    feed_urls, home = discover_feed_urls(source_url, timeout, log)
    for feed_url in feed_urls:
        log["urls_attempted"].append(feed_url)
        res = fetch(feed_url, timeout)
        if not res["ok"]:
            
            if len(log["errors"]) < 3:
                log["errors"].append({"url": feed_url, "error": res["error"]})
            continue
        items = rss_items(res["data"], urllib.parse.urlparse(source_url).netloc)
        if items:
            log["items"] = len(items)
            log["items_added"] = len(items)
            diagnostics["rss_feed_discovery_successes"] += 1
            return items, log, home
    return [], log, home


def parse_sitemap(xml_bytes):
    out = []
    try:
        root = ET.fromstring(xml_bytes)
    except Exception:
        return out
    ns_strip = lambda tag: tag.rsplit("}", 1)[-1]
    for node in root.iter():
        if ns_strip(node.tag) != "url":
            continue
        loc = None
        lastmod = None
        title = None
        for child in node:
            name = ns_strip(child.tag)
            if name == "loc":
                loc = clean(child.text)
            elif name == "lastmod":
                lastmod = parse_date(child.text or "")
            elif name == "title":
                title = clean(child.text)
        if loc:
            out.append({"title": title or loc.rsplit("/", 1)[-1].replace("-", " "), "url": loc, "date": lastmod, "source_name": urllib.parse.urlparse(loc).netloc, "snippet": ""})
    return out


def crawl_sitemaps(source_url, timeout, diagnostics):
    base = source_url.rstrip("/")
    sitemap_urls = [base + "/sitemap.xml", base + "/news-sitemap.xml", urllib.parse.urljoin(base + "/", "/sitemap.xml")]
    log = {"source": source_url, "method": "sitemap_news_sitemap_discovery", "attempted": True, "urls_attempted": [], "items_added": 0, "errors": []}
    items = []
    for sm_url in list(dict.fromkeys(sitemap_urls)):
        log["urls_attempted"].append(sm_url)
        res = fetch(sm_url, timeout)
        if not res["ok"]:
            
            if len(log["errors"]) < 3:
                log["errors"].append({"url": sm_url, "error": res["error"]})
            continue
        found = parse_sitemap(res["data"])
        if found:
            items.extend(found[:200])
    log["items_added"] = len(items)
    if items:
        diagnostics["sitemap_news_sitemap_discovery_successes"] += 1
    return items, log


def crawl_direct_page(source_url, home_response, diagnostics):
    log = {"source": source_url, "method": "direct_newsroom_blog_crawling", "attempted": True, "items_added": 0, "errors": []}
    if not home_response or not home_response["ok"]:
        log["errors"].append({"url": source_url, "error": (home_response or {}).get("error", "home fetch unavailable")})
        return [], log
    text = home_response["data"].decode("utf-8", "ignore")
    items = []
    for href, label in re.findall(r"<a\b[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", text, re.I | re.S)[:300]:
        title = clean(label)
        if len(title) < 12:
            continue
        url = urllib.parse.urljoin(home_response["final_url"], href)
        date = parse_date(title) or parse_date(url)
        items.append({"title": title, "url": url, "date": date, "source_name": urllib.parse.urlparse(source_url).netloc, "snippet": ""})
    log["items_added"] = len(items)
    if items:
        diagnostics["direct_newsroom_blog_crawling_successes"] += 1
    return items, log


def crawl_site_search(source_url, since, until, timeout, diagnostics):
    host = urllib.parse.urlparse(source_url).netloc.replace("www.", "")
    query = f"site:{host} (AI OR GPT OR LLM)"
    url = google_news_url(query, since, until, GOOGLE_EDITIONS[0])
    log = {"source": source_url, "method": "site_search_fallback", "attempted": True, "provider": "Google News RSS site: query", "url": url, "items_added": 0, "errors": []}
    res = fetch(url, timeout)
    if not res["ok"]:
        log["errors"].append({"url": url, "error": res["error"]})
        return [], log
    items = rss_items(res["data"], host)
    log["items_added"] = len(items)
    if items:
        diagnostics["site_search_fallback_successes"] += 1
    return items, log


def crawl_playwright(source_url, diagnostics):
    log = {"source": source_url, "method": "playwright_browser_rendering", "attempted": True, "items_added": 0, "errors": []}
    if importlib.util.find_spec("playwright") is None:
        log["disabled_reason"] = "playwright package is not installed"
        diagnostics["playwright_disabled_count"] += 1
        return [], log
    # Avoid importing Playwright unless installed; this keeps normal runs dependency-free.
    from playwright.sync_api import sync_playwright
    items = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(user_agent=UA)
            page.goto(source_url, wait_until="networkidle", timeout=15000)
            for link in page.locator("a").evaluate_all("els => els.slice(0, 300).map(a => ({href:a.href, text:a.innerText}))"):
                title = clean(link.get("text"))
                if len(title) >= 12 and link.get("href"):
                    items.append({"title": title, "url": link["href"], "date": parse_date(title) or parse_date(link["href"]), "source_name": urllib.parse.urlparse(source_url).netloc, "snippet": ""})
            browser.close()
    except Exception as exc:
        log["errors"].append({"url": source_url, "error": f"{type(exc).__name__}: {exc}"})
    log["items_added"] = len(items)
    if items:
        diagnostics["playwright_rendering_successes"] += 1
    return items, log



def compact_source_log(source_log):
    compact = {"source": source_log["source"], "methods": []}
    for method in source_log.get("methods", []):
        errors = method.get("errors") or []
        reason = method.get("disabled_reason") or (errors[0].get("error") if errors else None)
        status = "success" if method.get("items_added", 0) else ("disabled" if method.get("disabled_reason") else "failed_or_empty")
        compact["methods"].append({
            "method": method.get("method"),
            "attempted": method.get("attempted", False),
            "status": status,
            "items_added": method.get("items_added", 0),
            "reason": reason,
            "provider": method.get("provider"),
        })
    return compact

def infer_route(candidate):
    text = f"{candidate.get('title','')} {candidate.get('snippet','')} {candidate.get('query','')}".lower()
    mapping = [
        ("OpenAI", "OpenAI"), ("ChatGPT", "ChatGPT"), ("Claude", "Claude"), ("Anthropic", "Anthropic"),
        ("Gemini", "Gemini"), ("Copilot", "Copilot"), ("Meta AI", "Meta AI"), ("Apple Intelligence", "Apple AI"),
        ("NVIDIA", "NVIDIA"), ("ByteDance", "ByteDance"), ("Alibaba", "Alibaba"), ("Tencent", "Tencent"),
        ("Kakao", "Kakao AI"), ("LINE", "All Other AI/GPT News"),
    ]
    for needle, master in mapping:
        if needle.lower() in text:
            cat = "Asia Big Tech" if master in {"ByteDance", "Alibaba", "Tencent"} else "AI/GPT"
            if master == "NVIDIA":
                cat = "AI Agent"
            return cat, master
    return candidate.get("category", "AI/GPT"), candidate.get("master_query", "All Other AI/GPT News")


def company_for(master_query):
    if master_query.startswith("All Other") or master_query in ["Other Super Apps", "MZ Gen", "Gen Z", "1020 trend", "Social app", "Tech Crunch Startup"]:
        return "Market"
    return ALIASES.get(master_query, re.sub(r"\s*\(.*?\)|（.*?）", "", master_query).split("/")[0].strip() or "Market")


def make_headline(company, title, date):
    parsed = dt.date.fromisoformat(date)
    trimmed = re.sub(r"\s[-|]\s.*$", "", clean(title))[:95]
    return f"[{company}] {trimmed} ({parsed.year}.{parsed.month}.{parsed.day})"


def tier(title):
    lower = title.lower()
    if any(word in lower for word in ["lawsuit", "probe", "antitrust", "layoff", "hiring", "ceo", "stock"]):
        return 2
    if any(word in lower for word in ["sports", "movie", "celebrity", "rumor"]):
        return 3
    return 1


def is_ai_relevant(candidate):
    text = f"{candidate.get('title','')} {candidate.get('snippet','')} {candidate.get('query','')} {candidate.get('master_query','')}".lower()
    return any(term.lower() in text for term in AI_TERMS)


def render(since, until, records):
    rows = []
    current = (None, None)
    for record in records:
        if (record["category"], record["master_query"]) != current:
            if record["category"] != current[0]:
                rows.append(f'<h2>{html.escape(record["category"])}</h2>')
            rows.append(f'<h3>{html.escape(record["master_query"])}</h3><table><thead><tr><th>Select</th><th>Headline</th><th>Tier</th><th>Sources</th><th>Date</th></tr></thead><tbody>')
            current = (record["category"], record["master_query"])
        links = " ".join(f'<a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener">Source {idx + 1}</a>' for idx, url in enumerate(record["sources"][:3]))
        rows.append(f'<tr data-id="{record["cluster_id"]}"><td><input type="checkbox" data-id="{record["cluster_id"]}"></td><td>{html.escape(record["headline"])}</td><td><span class="tier">Tier {record["tier"]}</span></td><td>{links}</td><td>{record["date"]}</td></tr>')
    body = "\n".join(rows).replace("</tbody><h", "</tbody></table><h")
    if body:
        body += "</tbody></table>"
    else:
        body = "<p>No visible article rows were collected. See diagnostics JSON for route counters.</p>"
    js = """<script>const K='weekly-news-%s-%s';const boxes=[...document.querySelectorAll('input[type=checkbox]')];function sync(){let s=JSON.parse(localStorage.getItem(K)||'[]');boxes.forEach(b=>b.checked=s.includes(b.dataset.id));document.getElementById('sel').textContent=boxes.filter(b=>b.checked).length}boxes.forEach(b=>b.onchange=()=>{localStorage.setItem(K,JSON.stringify(boxes.filter(x=>x.checked).map(x=>x.dataset.id)));sync()});function clearChecks(){localStorage.removeItem(K);sync()}function exportSelections(){let ids=boxes.filter(x=>x.checked).map(x=>x.dataset.id), recs=DATA.filter(r=>ids.includes(r.cluster_id));let a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify({since:'%s',until:'%s',records:recs},null,2)],{type:'application/json'}));a.download='selections_%s_%s.json';a.click()}const DATA=%s;sync()</script>""" % (since, until, since, until, since, until, json.dumps(records, ensure_ascii=False))
    html_text = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Weekly Tech News Article List</title><style>body{{font-family:system-ui,"Apple SD Gothic Neo","Noto Sans KR","Noto Sans JP",sans-serif;margin:24px;background:#f7f8fb;color:#111}}h1{{margin-bottom:4px}}.pill,.tier{{display:inline-block;background:#e8eefc;border-radius:999px;padding:4px 10px;margin:3px}}table{{width:100%;border-collapse:collapse;background:white;margin:8px 0 20px}}th,td{{border-bottom:1px solid #e5e7eb;padding:8px;text-align:left;vertical-align:top}}th{{background:#f1f5f9}}a{{color:#1d4ed8}}button{{margin:6px;padding:8px 12px}}</style></head><body><h1>Weekly Tech News Article List</h1><p>Range: {since} ~ {until} · Generated: {now_z()}</p><div><span class="pill">Range {since}~{until}</span><span class="pill">Articles {len(records)}</span>{''.join(f'<span class="pill">{html.escape(c)} {sum(1 for r in records if r["category"] == c)}</span>' for c in CATEGORY_ORDER)}<span class="pill">Selected <b id="sel">0</b></span></div><button onclick="clearChecks()">Clear checks</button><button onclick="exportSelections()">Export selections</button>{body}{js}</body></html>'''
    (OUT / f"report_{since}_{until}.html").write_text(html_text, encoding="utf-8")


def build_records(candidates, since, until, diagnostics):
    diagnostics["raw_collected_total"] = len(candidates)
    diagnostics["raw_collected_count"] = len(candidates)
    normalized = []
    invalid_urls = 0
    for candidate in candidates:
        candidate = dict(candidate)
        candidate["url"] = canonical_url(candidate.get("url"))
        if not candidate["url"]:
            invalid_urls += 1
            continue
        normalized.append(candidate)
    diagnostics["after_url_normalization_count"] = len(normalized)
    diagnostics["invalid_url_removed_count"] = invalid_urls
    dated = [candidate for candidate in normalized if in_range(candidate.get("date"), since, until)]
    diagnostics["after_date_filter_count"] = len(dated)
    ai_filtered = [candidate for candidate in dated if is_ai_relevant(candidate)]
    diagnostics["after_ai_filter_count"] = len(ai_filtered)
    seen = {}
    records = []
    for candidate in ai_filtered:
        category, master_query = infer_route(candidate)
        key_text = re.sub(r"[^a-z0-9가-힣一-龥ぁ-んァ-ン]+", " ", candidate["title"].lower()).strip()[:140]
        key = hashlib.sha1((key_text or candidate["url"]).encode()).hexdigest()[:16]
        if key in seen:
            record = seen[key]
            if candidate["url"] not in record["sources"] and len(record["sources"]) < 3:
                record["sources"].append(candidate["url"])
                record["source_headlines"].append(candidate["title"])
                record["source_dates"].append(candidate.get("date"))
            continue
        company = company_for(master_query)
        record = {
            "cluster_id": key,
            "category": category,
            "master_query": master_query,
            "company": company,
            "headline": make_headline(company, candidate["title"], candidate["date"]),
            "tier": tier(candidate["title"]),
            "sources": [candidate["url"]],
            "date": candidate["date"],
            "source_headlines": [candidate["title"]],
            "source_dates": [candidate.get("date")],
            "article_texts": [],
            "dedup_status": "keep",
        }
        seen[key] = record
        records.append(record)
    records = [record for record in records if record["tier"] in (1, 2, 3)]
    order = {category: idx for idx, category in enumerate(CATEGORY_ORDER)}
    query_order = {(category, query): idx for category, queries in MASTER_QUERY_ORDER.items() for idx, query in enumerate(queries)}
    records.sort(key=lambda record: (order.get(record["category"], 999), query_order.get((record["category"], record["master_query"]), 999), record["tier"], -int(record["date"].replace("-", "")), record["cluster_id"]))
    diagnostics["after_dedupe_count"] = len(records)
    diagnostics["final_visible_row_count"] = len(records)
    diagnostics["incomplete"] = len(records) < 200
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", required=True)
    parser.add_argument("--timeout", type=int, default=6)
    args = parser.parse_args()
    OUT.mkdir(exist_ok=True)
    ARC.mkdir(exist_ok=True)
    diagnostics = {
        "loaded_source_count": 0,
        "total_source_count": 0,
        "sources_attempted": 0,
        "google_news_query_count": 0,
        "google_news_raw_items": 0,
        "google_news_added_to_candidates": 0,
        "google_news_skipped_count": 0,
        "google_news_skip_reasons": {},
        "skip_reasons": {},
        "source_crawling_attempted": 0,
        "rss_feed_discovery_attempted": 0,
        "sitemap_news_sitemap_discovery_attempted": 0,
        "direct_newsroom_blog_crawling_attempted": 0,
        "site_search_fallback_attempted": 0,
        "playwright_rendering_attempted": 0,
        "playwright_disabled_count": 0,
        "collected_from_google_news": 0,
        "collected_from_rss_feeds": 0,
        "collected_from_sitemaps": 0,
        "collected_from_direct_pages": 0,
        "collected_from_site_search": 0,
        "collected_from_playwright": 0,
        "rss_feed_discovery_successes": 0,
        "sitemap_news_sitemap_discovery_successes": 0,
        "direct_newsroom_blog_crawling_successes": 0,
        "site_search_fallback_successes": 0,
        "playwright_rendering_successes": 0,
        "raw_collected_total": 0,
        "raw_collected_count": 0,
        "after_url_normalization_count": 0,
        "invalid_url_removed_count": 0,
        "after_date_filter_count": 0,
        "after_ai_filter_count": 0,
        "after_dedupe_count": 0,
        "final_visible_row_count": 0,
        "routes_attempted": [],
        "source_logs": [],
        "incomplete": False,
    }
    candidates = []

    # 1. Google News query expansion: keyword x US/KR/JP/Global.
    for keyword in GOOGLE_NEWS_KEYWORDS:
        for edition in GOOGLE_EDITIONS:
            diagnostics["google_news_query_count"] += 1
            url = google_news_url(keyword, args.since, args.until, edition)
            response = fetch(url, args.timeout)
            if not response["ok"]:
                diagnostics["google_news_skip_reasons"][response["error"]] = diagnostics["google_news_skip_reasons"].get(response["error"], 0) + 1
                continue
            items = rss_items(response["data"], "Google News")
            diagnostics["google_news_raw_items"] += len(items)
            for item in items:
                # Preserve Google redirect URLs when source URL is unavailable.
                before = len(candidates)
                added = add_candidate(candidates, item, "google_news", f"{keyword} [{edition['name']}]", diagnostics=diagnostics)
                if added:
                    diagnostics["google_news_added_to_candidates"] += 1
                    diagnostics["collected_from_google_news"] += len(candidates) - before
            time.sleep(0.02)
    print(f"Google News query count: {diagnostics['google_news_query_count']}")

    # 2. Source pool crawling: every loaded source, every concrete method.
    sources = extract_sources()
    diagnostics["loaded_source_count"] = len(sources)
    diagnostics["total_source_count"] = len(sources)
    for source in sources:
        diagnostics["sources_attempted"] += 1
        diagnostics["source_crawling_attempted"] += 1
        source_log = {"source": source, "methods": []}

        diagnostics["rss_feed_discovery_attempted"] += 1
        feed_items, feed_log, home_response = crawl_rss_feeds(source, args.timeout, diagnostics)
        source_log["methods"].append(feed_log)
        for item in feed_items:
            if add_candidate(candidates, item, "rss_feed", source, diagnostics=diagnostics):
                diagnostics["collected_from_rss_feeds"] += 1

        diagnostics["sitemap_news_sitemap_discovery_attempted"] += 1
        sitemap_items, sitemap_log = crawl_sitemaps(source, args.timeout, diagnostics)
        source_log["methods"].append(sitemap_log)
        for item in sitemap_items:
            if add_candidate(candidates, item, "sitemap", source, diagnostics=diagnostics):
                diagnostics["collected_from_sitemaps"] += 1

        diagnostics["direct_newsroom_blog_crawling_attempted"] += 1
        direct_items, direct_log = crawl_direct_page(source, home_response, diagnostics)
        source_log["methods"].append(direct_log)
        for item in direct_items:
            if add_candidate(candidates, item, "direct_page", source, diagnostics=diagnostics):
                diagnostics["collected_from_direct_pages"] += 1

        diagnostics["site_search_fallback_attempted"] += 1
        site_items, site_log = crawl_site_search(source, args.since, args.until, args.timeout, diagnostics)
        source_log["methods"].append(site_log)
        for item in site_items:
            if add_candidate(candidates, item, "site_search", source, diagnostics=diagnostics):
                diagnostics["collected_from_site_search"] += 1

        diagnostics["playwright_rendering_attempted"] += 1
        pw_items, pw_log = crawl_playwright(source, diagnostics)
        source_log["methods"].append(pw_log)
        for item in pw_items:
            if add_candidate(candidates, item, "playwright", source, diagnostics=diagnostics):
                diagnostics["collected_from_playwright"] += 1

        diagnostics["source_logs"].append(compact_source_log(source_log))

    diagnostics["routes_attempted"] = [
        "google_news_us_kr_jp_global",
        "rss_feed_discovery",
        "sitemap_news_sitemap_discovery",
        "direct_newsroom_blog_crawling",
        "site_search_fallback",
        "playwright_browser_rendering",
    ]
    records = build_records(candidates, args.since, args.until, diagnostics)
    data = {"run": {"since": args.since, "until": args.until, "generated_at": now_z()}, "records": records, "na_audit": [], "diagnostics": diagnostics, "source_pool": sources}
    data_path = OUT / f"data_{args.since}_{args.until}.json"
    diag_path = OUT / f"diagnostics_{args.since}_{args.until}.json"
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (ARC / f"data_{args.since}_{args.until}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    diag_path.write_text(json.dumps(diagnostics, ensure_ascii=False, indent=2), encoding="utf-8")
    render(args.since, args.until, records)
    print(json.dumps({k: diagnostics[k] for k in ["loaded_source_count", "google_news_query_count", "google_news_raw_items", "google_news_added_to_candidates", "sources_attempted", "raw_collected_total", "final_visible_row_count", "incomplete"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
