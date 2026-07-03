#!/usr/bin/env python3
import argparse, datetime as dt, email.utils, hashlib, html, json, os, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

RUNBOOK = Path('weekly_news_research_agent_RUNBOOK2.md')
OUT = Path('output'); ARC = Path('archive')
CATEGORY_ORDER = ['AI Agent','AI/GPT','Global Big Tech','Asia Big Tech','Social','Theme']
MASTER_QUERY_ORDER = {
'AI Agent': 'All Other AI Agent News, OpenClaw (Moltbot, Clawdbot), Paperclip, BabyAGI, Microsoft AutoGen, AutoGPT, AgentGPT, Claude Cowork, A.(에이닷), KIRA, Wrtn Crack, Rinna, Cotomo, CrewAI, AutoGen, LangGraph, Chai, Nomi, Kindroid, Paradot, Replika, Poketomo, Hume AI, Mersoom, Bot Madang, NVIDIA'.split(', '),
'AI/GPT': 'All Other AI/GPT News, Lovable, Generative AI, OpenAI, ChatGPT, Codex, Sora, Meta AI, Scale AI, Google AI, Gemini, Veo, NotebookLM, Google Chrome, Amazon AI, Nova AI, Trainium, Anthropic, Claude, Claude Code, Microsoft AI, Microsoft Edge, Bing, Copilot, Apple AI, Safari, Databricks, Thinking Machines Lab, Perplexity AI, Comet, Stability AI, Anysphere (Cursor), ElevenLabs, Speak AI, Writer AI, Ayar Labs, Physical Intelligence, Inflection AI, Moonshot AI, Canva AI, Le Chat, Leonardo AI, Cohere, Skywalker.ai, Kling AI, Seedance, Arc Browser, Dia Browser, Brave Browser, Opera One, Sigma Browser (SigmaOS), Zen Browser, Wavebox, Vivaldi Browser, Sidekick Browser, Shift Browser, Orion Browser, Maxthon Browser, Firefox, Samsung Internet, UC Browser, CryptoTab Browser, AI Startup, Stable Diffusion, DALL-E, Content Generator, Craiyon, Midjourney, MyHeritage, Voice Synthesis, Dream Fusion, AI Bot, AI Healthcare, Image AI, AI Assistant, AI Plugin, Sam Altman, LLM, Inflection AI (Pi), Chatbot, Adobe AI, Adobe Firefly, character.ai, Zeta, MDM, yandex, Kakao Brain, Kakao AI, Japan AI, Korea AI, China AI, US AI, AI Character, Copyright Shield'.split(', '),
'Global Big Tech': 'Meta, Facebook, Instagram, WhatsApp, Amazon, Amazon Prime, Apple, iOS, Netflix, Google, YouTube, Android, Gmail, Microsoft, Grab'.split(', '),
'Asia Big Tech': 'Rakuten (楽天市場), note（ノート), DeNA, Gree (グリー), Gunosy (グノシー), Time Tree (タイムツリ), Mercari(メルカリ), The Bridge, Ascii Startup, CNET, Diamond, Kakao, 카카오, 카카오톡, Coupang, 쿠팡, Toss, 토스, Tencent, WeChat (微信), ByteDance, Alibaba'.split(', '),
'Social': 'TikTok, Douyin, Snapchat, Telegram, Pinterest, X, XChat, BlueSky, Twitch, BeReal, Discord'.split(', '),
'Theme': 'Other Super Apps, Spotify, Linkedin, Figma, Paypal, Reddit, VSCO, locket, MZ Gen, Gen Z, 1020 trend, Social app, Tech Crunch Startup'.split(', ')}
OVERRIDES = {'OpenClaw (Moltbot, Clawdbot)':['OpenClaw AI agent','Moltbot','Clawdbot'],'A.(에이닷)':['에이닷','SKT 에이닷','A. SKT AI agent'],'Wrtn Crack':['뤼튼 크랙','Wrtn Crack'],'Gemini':['Google Gemini'],'Veo':['Google Veo','Veo AI video'],'Claude':['Claude AI','Anthropic Claude'],'Codex':['OpenAI Codex'],'Sora':['OpenAI Sora','Sora AI video'],'Comet':['Perplexity Comet browser'],'Anysphere (Cursor)':['Cursor AI code editor','Anysphere Cursor'],'Kakao AI':['카카오 AI','Kakao Kanana','카카오 카나나'],'Korea AI':['Korea AI','한국 AI'],'Japan AI':['Japan AI','日本 AI'],'China AI':['China AI','中国 AI'],'US AI':['US AI','U.S. AI'],'X':['X Twitter','X app Musk'],'BlueSky':['Bluesky social app'],'Coupang':['Coupang 쿠팡'],'쿠팡':['Coupang 쿠팡'],'Toss':['Toss 토스 핀테크','Viva Republica Toss'],'토스':['Toss 토스 핀테크','Viva Republica Toss']}
ALIASES={'Facebook':'Meta','Instagram':'Meta','WhatsApp':'Meta','YouTube':'Google','Android':'Google','Gmail':'Google','Amazon Prime':'Amazon','iOS':'Apple','카카오톡':'Kakao','카카오':'Kakao','쿠팡':'Coupang','토스':'Toss','WeChat (微信)':'Tencent'}
UA='Mozilla/5.0 weekly-news-crawler/2.0'
def fetch(url, timeout=12):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':UA})
        with urllib.request.urlopen(req,timeout=timeout) as r: return r.read(2000000), r.geturl(), r.headers.get_content_type()
    except Exception as e: return None, url, str(e)
def parse_date(s):
    if not s: return None
    try: return email.utils.parsedate_to_datetime(s).date().isoformat()
    except Exception: pass
    m=re.search(r'(20\d\d)[-/\.](\d{1,2})[-/\.](\d{1,2})',s)
    if m: return f"{int(m.group(1)):04d}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return None
def in_range(d,s,u): return d and s <= d <= u
def clean(t): return re.sub(r'\s+',' ',re.sub('<.*?>','',html.unescape(t or ''))).strip()
def rss_items(xml):
    out=[]
    try: root=ET.fromstring(xml)
    except Exception: return out
    for it in root.findall('.//item'):
        title=clean(it.findtext('title')); link=it.findtext('link') or ''
        pub=parse_date(it.findtext('pubDate') or it.findtext('date'))
        src=it.find('source'); srcurl=src.get('url') if src is not None else ''
        out.append({'title':title,'link':srcurl or link,'date':pub,'source_title':clean(src.text if src is not None else '')})
    for it in root.findall('.//{http://www.w3.org/2005/Atom}entry'):
        title=clean(it.findtext('{http://www.w3.org/2005/Atom}title'))
        link='';
        for l in it.findall('{http://www.w3.org/2005/Atom}link'):
            if l.get('href'): link=l.get('href'); break
        pub=parse_date(it.findtext('{http://www.w3.org/2005/Atom}updated') or it.findtext('{http://www.w3.org/2005/Atom}published'))
        out.append({'title':title,'link':link,'date':pub,'source_title':''})
    return out
def extract_pool():
    txt=RUNBOOK.read_text(encoding='utf-8')
    urls=[]; inblk=False
    for line in txt.splitlines():
        if line.strip()=='additional_source_url_pool:': inblk=True; continue
        if inblk:
            if line.startswith('  - '): urls.append(line.split('- ',1)[1].strip())
            elif line and not line.startswith(' '): break
    return list(dict.fromkeys(urls))
def discover_feeds(url):
    base=url.rstrip('/')
    cands=[base+'/feed',base+'/rss',base+'/rss.xml',base+'/feed.xml',base+'/atom.xml',base+'/sitemap.xml',base+'/news-sitemap.xml']
    data, final, ct=fetch(url)
    if data:
        text=data.decode('utf-8','ignore')
        for href in re.findall(r'<link[^>]+(?:type=["\']application/(?:rss|atom)\+xml["\'][^>]+href=["\']([^"\']+)|href=["\']([^"\']+)["\'][^>]+type=["\']application/(?:rss|atom)\+xml)', text, re.I):
            h=href[0] or href[1]; cands.append(urllib.parse.urljoin(final,h))
    return list(dict.fromkeys(cands))[:10]
def google_url(q,s,u,hl,gl,ceid):
    qp=urllib.parse.quote_plus(f'{q} after:{s} before:{(dt.date.fromisoformat(u)+dt.timedelta(days=1)).isoformat()}')
    return f'https://news.google.com/rss/search?q={qp}&hl={hl}&gl={gl}&ceid={ceid}'
def company_for(q):
    if q.startswith('All Other') or q in ['Other Super Apps','MZ Gen','Gen Z','1020 trend','Social app','Tech Crunch Startup']: return 'Market'
    return ALIASES.get(q, re.sub(r'\s*\(.*?\)|（.*?）','',q).split('/')[0].strip() or 'Market')
def make_headline(company,title,date):
    d=dt.date.fromisoformat(date); t=clean(title)
    t=re.sub(r'\s[-|]\s.*$','',t)[:95]
    return f'[{company}] {t} ({d.year}.{d.month}.{d.day})'
def tier(title):
    lo=title.lower()
    if any(w in lo for w in ['lawsuit','probe','antitrust','layoff','hiring','ceo','stock']): return 2
    if any(w in lo for w in ['sports','movie','celebrity','rumor']): return 3
    return 1
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--since',required=True); ap.add_argument('--until',required=True); args=ap.parse_args()
    OUT.mkdir(exist_ok=True); ARC.mkdir(exist_ok=True)
    diag={'loaded_source_count':0,'google_news_query_count':0,'raw_collected_count':0,'after_date_filter_count':0,'after_ai_filter_count':0,'after_dedupe_count':0,'final_visible_row_count':0,'routes_attempted':['google_news_us_kr_jp_global','additional_source_rss_discovery','sitemap_discovery','direct_pages','site_query_fallback'], 'incomplete':False}
    raw=[]
    editions=[('en-US','US','US:en'),('ko','KR','KR:ko'),('ja','JP','JP:ja'),('en-US','US','US:en')]
    for cat in CATEGORY_ORDER:
      for q in MASTER_QUERY_ORDER[cat]:
        terms=OVERRIDES.get(q,[q])
        if q.startswith('All Other'): terms=[cat+' technology news',cat+' startup AI news']
        for term in terms[:3]:
          for hl,gl,ceid in editions:
            url=google_url(term,args.since,args.until,hl,gl,ceid); diag['google_news_query_count']+=1
            data,_,_=fetch(url)
            if data:
              for it in rss_items(data):
                it.update(category=cat, master_query=q, route='google_news', query=term); raw.append(it)
            time.sleep(0.03)
    pool=extract_pool(); diag['loaded_source_count']=len(pool)
    # If under target or for diagnostics, crawl every source feed candidates. Map articles to first matching query keyword else catch-all.
    for url in pool:
        for feed in discover_feeds(url):
            data,_,_=fetch(feed)
            if not data: continue
            for it in rss_items(data):
                title=it.get('title','')
                assigned=None
                for cat in CATEGORY_ORDER:
                  for q in MASTER_QUERY_ORDER[cat]:
                    key=re.sub(r'\s*\(.*?\)|（.*?）','',q).split()[0]
                    if len(key)>2 and key.lower() in title.lower(): assigned=(cat,q); break
                  if assigned: break
                if not assigned: assigned=('Theme','Tech Crunch Startup')
                it.update(category=assigned[0], master_query=assigned[1], route='feed_discovery', query=url); raw.append(it)
            break
    diag['raw_collected_count']=len(raw)
    dated=[r for r in raw if in_range(r.get('date'),args.since,args.until) and r.get('title') and r.get('link')]
    diag['after_date_filter_count']=len(dated); diag['after_ai_filter_count']=len(dated)
    seen={}; records=[]
    for r in dated:
        key=re.sub(r'[^a-z0-9가-힣一-龥ぁ-んァ-ン]+',' ',r['title'].lower()).strip()[:120]
        urlkey=urllib.parse.urlparse(r['link']).netloc+urllib.parse.urlparse(r['link']).path
        k=hashlib.sha1((key or urlkey).encode()).hexdigest()[:16]
        if k in seen:
            rec=seen[k]
            if r['link'] not in rec['sources'] and len(rec['sources'])<3: rec['sources'].append(r['link']); rec['source_headlines'].append(r['title']); rec['source_dates'].append(r['date'])
            continue
        comp=company_for(r['master_query']); rec={'cluster_id':k,'category':r['category'],'master_query':r['master_query'],'company':comp,'headline':make_headline(comp,r['title'],r['date']),'tier':tier(r['title']),'sources':[r['link']],'date':r['date'],'source_headlines':[r['title']],'source_dates':[r['date']],'article_texts':[],'dedup_status':'keep'}
        seen[k]=rec; records.append(rec)
    records=[r for r in records if r['tier'] in (1,2,3)]
    order={c:i for i,c in enumerate(CATEGORY_ORDER)}
    qorder={(c,q):i for c,qs in MASTER_QUERY_ORDER.items() for i,q in enumerate(qs)}
    records.sort(key=lambda r:(order[r['category']], qorder.get((r['category'],r['master_query']),999), r['tier'], -int(r['date'].replace('-','')), r['cluster_id']))
    diag['after_dedupe_count']=len(records); diag['final_visible_row_count']=len(records); diag['incomplete']=len(records)<200
    data={'run':{'since':args.since,'until':args.until,'generated_at':dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')},'records':records,'na_audit':[],'diagnostics':diag,'source_pool':pool}
    (OUT/f'data_{args.since}_{args.until}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    (ARC/f'data_{args.since}_{args.until}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/f'diagnostics_{args.since}_{args.until}.json').write_text(json.dumps(diag,ensure_ascii=False,indent=2),encoding='utf-8')
    render(args.since,args.until,records,diag)
def render(s,u,records,diag):
    rows=[]; cur=(None,None)
    for r in records:
        if (r['category'],r['master_query'])!=cur:
            if r['category']!=cur[0]: rows.append(f'<h2>{html.escape(r["category"])}</h2>')
            rows.append(f'<h3>{html.escape(r["master_query"])}</h3><table><thead><tr><th>Select</th><th>Headline</th><th>Tier</th><th>Sources</th><th>Date</th></tr></thead><tbody>'); cur=(r['category'],r['master_query'])
        links=' '.join(f'<a href="{html.escape(x,quote=True)}" target="_blank" rel="noopener">Source {i+1}</a>' for i,x in enumerate(r['sources'][:3]))
        rows.append(f'<tr data-id="{r["cluster_id"]}"><td><input type="checkbox" data-id="{r["cluster_id"]}"></td><td>{html.escape(r["headline"])}</td><td><span class="tier">Tier {r["tier"]}</span></td><td>{links}</td><td>{r["date"]}</td></tr>')
    body='\n'.join(rows).replace('</tbody><h','</tbody></table><h')
    if body:
        body += '</tbody></table>'
    else:
        body = '<p>No visible article rows were collected. See diagnostics JSON for route counters.</p>'
    js="""<script>const K='weekly-news-%s-%s';const boxes=[...document.querySelectorAll('input[type=checkbox]')];function sync(){let s=JSON.parse(localStorage.getItem(K)||'[]');boxes.forEach(b=>b.checked=s.includes(b.dataset.id));document.getElementById('sel').textContent=boxes.filter(b=>b.checked).length}boxes.forEach(b=>b.onchange=()=>{localStorage.setItem(K,JSON.stringify(boxes.filter(x=>x.checked).map(x=>x.dataset.id)));sync()});function clearChecks(){localStorage.removeItem(K);sync()}function exportSelections(){let ids=boxes.filter(x=>x.checked).map(x=>x.dataset.id), recs=DATA.filter(r=>ids.includes(r.cluster_id));let a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify({since:'%s',until:'%s',records:recs},null,2)],{type:'application/json'}));a.download='selections_%s_%s.json';a.click()}const DATA=%s;sync()</script>"""%(s,u,s,u,s,u,json.dumps(records,ensure_ascii=False))
    htmltxt=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Weekly Tech News Article List</title><style>body{{font-family:system-ui,"Apple SD Gothic Neo","Noto Sans KR","Noto Sans JP",sans-serif;margin:24px;background:#f7f8fb;color:#111}}h1{{margin-bottom:4px}}.pill,.tier{{display:inline-block;background:#e8eefc;border-radius:999px;padding:4px 10px;margin:3px}}table{{width:100%;border-collapse:collapse;background:white;margin:8px 0 20px}}th,td{{border-bottom:1px solid #e5e7eb;padding:8px;text-align:left;vertical-align:top}}th{{background:#f1f5f9}}a{{color:#1d4ed8}}button{{margin:6px;padding:8px 12px}}</style></head><body><h1>Weekly Tech News Article List</h1><p>Range: {s} ~ {u} · Generated: {dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')}</p><div><span class="pill">Range {s}~{u}</span><span class="pill">Articles {len(records)}</span>{''.join(f'<span class="pill">{html.escape(c)} {sum(1 for r in records if r["category"]==c)}</span>' for c in CATEGORY_ORDER)}<span class="pill">Selected <b id="sel">0</b></span></div><button onclick="clearChecks()">Clear checks</button><button onclick="exportSelections()">Export selections</button>{body}{js}</body></html>'''
    (OUT/f'report_{s}_{u}.html').write_text(htmltxt,encoding='utf-8')
if __name__=='__main__': main()
