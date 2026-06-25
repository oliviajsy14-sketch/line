# Weekly Archiving Process

## 목차

- [업무 목적](#업무-목적)
- [기본 작업 단위](#기본-작업-단위)
- [카테고리 구분](#카테고리-구분)
- [카테고리별 기준](#카테고리별-기준)
- [Global IT Trend Report 기사 범위](#global-it-trend-report-기사-범위)
- [Naver / LINE 아카이빙 제외 기준](#naver--line-아카이빙-제외-기준)
- [작업 전 준비사항](#작업-전-준비사항)
- [날짜 입력 방식](#날짜-입력-방식)
- [전체 작업 순서](#전체-작업-순서)
- [Google Query 전 우선 확인 소스](#google-query-전-우선-확인-소스)
- [Google Query 전 우선 확인 링크](#google-query-전-우선-확인-링크)
- [Query List 적용 방식](#query-list-적용-방식)
- [Official Source 확인 방식](#official-source-확인-방식)
- [Google Query 및 외부 기사 검색 방식](#google-query-및-외부-기사-검색-방식)
- [Google Query 기사 중복 확인 방식](#google-query-기사-중복-확인-방식)
- [기사 선별 기준](#기사-선별-기준)
- [기사 제외 기준](#기사-제외-기준)
- [국가 중요도 우선순위](#국가-중요도-우선순위)
- [국가 우선순위 적용 방식](#국가-우선순위-적용-방식)
- [Cluster 처리 방식](#cluster-처리-방식)
- [Paywall 기사 처리 방식](#paywall-기사-처리-방식)
- [URL 언어 기준](#url-언어-기준)
- [Sheet 정리 방식](#sheet-정리-방식)
- [중복 기사 처리 방식](#중복-기사-처리-방식)
- [최종 Title 작성 방식](#최종-title-작성-방식)
- [Query 전체 리스트](#query-전체-리스트)
- [Query별 검색 결과 정리 방식](#query별-검색-결과-정리-방식)
- [최종 검수 체크리스트](#최종-검수-체크리스트)
- [최종 산출물](#최종-산출물)
- [산출물 활용 방식](#산출물-활용-방식)

## 업무 목적

- 주간 단위로 주요 IT 및 AI 관련 뉴스 수집
- 수집 기사를 기사 리스트업 Sheet에 카테고리별 정리
- Weekly AI Trend Report 및 Global IT Trend Report 작성에 활용
- 중복 기사, 비대상 기사, 단순 PR성 기사 제외
- 리포트에 활용 가능한 유의미한 기사만 최종 선별

## 기본 작업 단위

- 작업 주기: 주 1회
- 검색 기간: 작업자가 `YYYY/MM/DD~YYYY/MM/DD` 형식으로 직접 입력
- 작업 위치: 기사 리스트업 Sheet
- 탭 생성 방식: 주차별 새 탭 생성
- 탭명 예시: `4월 3주`, `4월 4주`, `6월 4주`
- 템플릿 관리: 기존 서식 유지 후 새 탭에 복사
- 저장 인코딩: UTF-8

## 카테고리 구분

- AI/GPT
- Global Big Tech
- Asia Big Tech
- Social
- Theme

## 카테고리별 기준

### AI/GPT

- Weekly AI Trend Report 별도 시트에 따로 아카이빙
- AI 중심 기사만 선별
- 포함 범위:
  - AI Agent
  - Agentic Platform
  - LLM
  - 생성형 AI
  - AI 모델
  - AI 인프라
  - AI Search
  - AI 광고
  - AI 보안
  - AI 규제
  - AI 투자
- 기사 제목은 영어 원문 제목 기준으로 입력
- 관련 지역을 별도 확인
- 이후 국문 요약 및 정리는 Global IT Trend Report 양식 기준 적용

### Global Big Tech

- 대상 기업:
  - Meta
  - Amazon
  - Apple
  - Netflix
  - Google
  - Microsoft
  - Grab
- 포함 관계:
  - Facebook, Instagram, WhatsApp은 Meta에 포함
  - YouTube, Gmail, Android는 Google에 포함
- 포함 가능 기사:
  - AI
  - 플랫폼 전략
  - 광고
  - 커머스
  - 콘텐츠
  - OS
  - 검색
  - 구독
  - 크리에이터 생태계

### Asia Big Tech

- 대상 기업 및 서비스:
  - Rakuten
  - Note
  - DeNA
  - Gree
  - Gunosy
  - Time Tree
  - Mercari
  - Kakao
  - Coupang
  - Toss
  - Tencent
  - ByteDance
  - Alibaba
- 포함 가능 기사:
  - AI
  - 플랫폼
  - 콘텐츠
  - 커머스
  - 메신저
  - 앱 서비스
  - 게임
  - 광고
  - 유저 성장
- 제외 대상:
  - Naver 단독 기사
  - LINE 단독 기사
  - LY Corporation 단독 기사

### Social

- 대상 서비스:
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
- 포함 가능 기사:
  - 신규 기능
  - 유저 성장
  - 커뮤니티 기능
  - 크리에이터 기능
  - 광고
  - 수익화
  - 안전 기능
  - 메시징 기능

### Theme

- 특정 기업보다 시장 흐름 중심으로 정리
- 포함 가능 기사:
  - 시장 트렌드
  - 유저 행동 변화
  - 규제
  - 산업 변화
  - 신기술 흐름
  - 여러 기업 비교
  - 국가 단위 정책
  - 국가 단위 유저 트렌드
  - 산업 구조 변화
  - 소비 트렌드
  - 플랫폼 사용 방식 변화
  - Gen Z/MZ 트렌드

## Global IT Trend Report 기사 범위

- AI 관련 기사만 포함하지 않아도 됨
- 포함 가능 범위:
  - 주요 IT
  - 플랫폼
  - social media
  - 커머스
  - 광고
  - 콘텐츠
  - 규제
  - 유저 행동 변화
  - 시장 트렌드
- AI 관련성이 약해도 아래 관점에서 의미 있는 변화면 선별 가능:
  - Big Tech
  - Asia Big Tech
  - Social
  - Theme
- 단순 기능 업데이트도 아래 변화와 연결되면 포함 가능:
  - 플랫폼 전략
  - 수익화
  - 유저 경험
  - 커뮤니티
  - 광고
  - 크리에이터 생태계
- 제외:
  - 단순 PR성 기사
  - 이벤트성 기사
  - 영향도 낮은 단순 업데이트

## Naver / LINE 아카이빙 제외 기준

- 아카이빙 제외:
  - Naver 단독 기사
  - LINE 단독 기사
  - LY Corporation 단독 기사
- 제외 이유:
  - Naver, LINE은 당사 관련 기사로 Weekly Archiving 대상에서 제외
  - LY Corporation도 LINE/Naver와 직접 연결된 단독 기사면 제외
- 예외 검토:
  - 외부 시장 기사에서 Naver, LINE, LY Corporation이 여러 기업 중 하나로 언급되는 경우
  - 기사 전체 주제가 시장 변화, 산업 트렌드, 경쟁사 비교인 경우
  - 이 경우 `[Market]` 기사로만 검토
- 예외 적용 시 주의:
  - Naver/LINE 단독 업데이트로 정리 금지
  - 시장 전체 흐름 중심으로 판단
- 기존 기준대로 검토할 기업:
  - Kakao
  - Coupang
  - Toss
  - Rakuten
  - DeNA
  - Mercari
  - Tencent
  - ByteDance
  - Alibaba

## 작업 전 준비사항

- [ ] 작업자가 입력한 검색 기간 확인
- [ ] 검색 기간이 `YYYY/MM/DD~YYYY/MM/DD` 형식인지 확인
- [ ] 기사 리스트업 Sheet의 기존 템플릿 확인
- [ ] 새 주차 탭 생성
- [ ] 기존 서식 유지
- [ ] 카테고리별 입력 영역 확인
- [ ] 이전 주차 기사와 중복 확인이 가능하도록 기존 Sheet 접근 상태 확인

## 날짜 입력 방식

- 입력 형식: `YYYY/MM/DD~YYYY/MM/DD`
- 입력 예시: `2026/06/18~2026/06/24`
- 적용 범위:
  - Official Source 확인
  - Google News 검색
  - Google Search 검색
  - 기사 발행일 검수
- 주의사항:
  - Sheet 최종 Title 날짜는 0 padding 없이 작성
  - 최종 Title 날짜 예시: `2026/6/24`

## 전체 작업 순서

1. 작업자가 입력한 날짜 범위 확인
2. 날짜 범위 기준으로 모든 검색 및 기사 확인 진행
3. 1차: `Google Query 전 우선 확인 링크`의 공식 사이트, Blog, Newsroom, GitHub, release notes, changelog 검토
4. 2차: 공식 링크가 없거나 누락 가능성이 있는 항목만 Google Query 실행
5. 3차: 공통 Tech / AI / Social Source 확인으로 외부 기사와 시장 반응 보완
6. 4차: 중복 제거, 제외 대상 필터링, AI 관련성 판단
7. 5차: 기사 리스트업 Sheet 입력
8. Query List에서 `(Google Query)` 표시 항목은 Google Search 또는 Google News에서만 검색
9. 우선 확인 링크와 우선 확인 소스의 주요 업데이트 먼저 기록
10. Google News 및 Google Search로 추가 기사 검색
11. Google Query 기사 Sheet 입력 전 과거 중복 여부 확인
12. 중복 확인 시 날짜 필터 해제 후 기사 타이틀 또는 핵심 키워드로 재검색
13. 동일 기사 또는 동일 이슈의 과거 주차 사용 여부 확인
14. 동일 이벤트 기사는 하나의 Cluster로 묶기
15. Cluster별 가장 적합한 Source 1개만 최종 유지
16. Bloomberg, Reuters, NYTimes 등 Paywall 기사는 접근 가능한 기사로 대체
17. Naver, LINE, LY Corporation 단독 기사 제외
18. 기사 제목, 출처, 날짜, URL, 카테고리, 주요 내용, 포함 여부 Sheet 정리
19. 최종 선별 기사별 Korean Title 작성
20. Weekly AI Trend Report와 Global IT Trend Report에 활용 가능한 기사만 최종 유지

## Google Query 전 우선 확인 소스

- Google Query 전 Official Source가 존재하는 기업·서비스·제품은 우선 확인
- `(Google Query)` 표시 항목은 예외로 Google Search 또는 Google News에서만 검색

### 우선 확인 대상

- Official Sources
- GitHub
- Changelog
- Release Notes
- Docs
- Blogs
- 9to5Mac
- 9to5Google
- TechCrunch
- Social Media Today

### 적용 기준

- 기업명, 서비스명, 제품명 Query는 우선 확인 소스 먼저 확인
- 일반 키워드성 Query는 Google Query 중심으로 검색
- `(Google Query)` 표시 항목은 공식 사이트 확인 없이 Google Query만 진행
- Official Source 주요 업데이트 우선 기록
- 이후 Google Search 또는 Google News로 외부 기사, 시장 반응, 보완 정보 확인

### Official Sources 세부 기준

- 기업 공식 홈페이지
- 공식 Newsroom
- 공식 Blog
- 공식 Developer Blog
- 공식 Product Update Page
- 공식 Research Blog
- 공식 Engineering Blog

### GitHub 세부 기준

- Release
- Commit
- Issue
- Pull Request
- README 업데이트
- Version tag
- Repository announcement

### Changelog 세부 기준

- 제품 업데이트 내역
- 버전별 변경 사항
- 기능 추가 및 개선 사항
- 버그 수정
- API 변경 사항

### Release Notes 세부 기준

- 앱 업데이트
- API 업데이트
- 모델 업데이트
- 플랫폼 업데이트
- SDK 업데이트
- 개발자 도구 업데이트

### Docs 세부 기준

- Developer Docs
- API Docs
- Help Center
- Product Guide
- Integration Guide
- Migration Guide

## Google Query 전 우선 확인 링크

Google Query를 실행하기 전에 아래 공식 링크, 블로그, 뉴스룸, GitHub, release notes, changelog를 우선 확인한다. 공식 링크에서 관련 기사를 먼저 수집한 뒤, 공식 링크가 없거나 추가 확인이 필요한 항목만 Google Query를 사용한다.

### 적용 순서

1. 1차: 아래 우선 확인 링크 검토
2. 2차: 공식 링크가 없거나 누락 가능성이 있는 항목 Google Query 실행
3. 3차: 공통 Tech / AI / Social Source 확인
4. 4차: 중복 제거, 제외 대상 필터링, AI 관련성 판단
5. 5차: 기사 리스트업 Sheet 입력

### 공통 Tech / AI / Social Source

[TechCrunch]

https://techcrunch.com/category/artificial-intelligence/

https://techcrunch.com/category/startups/

https://techcrunch.com/tag/ai/

https://techcrunch.com/tag/openai/

https://techcrunch.com/tag/anthropic/

https://techcrunch.com/tag/google/

https://techcrunch.com/tag/apple/

https://techcrunch.com/tag/meta/

https://techcrunch.com/tag/microsoft/

https://techcrunch.com/tag/amazon/

[9to5Google]

https://9to5google.com/

https://9to5google.com/guides/gemini/

https://9to5google.com/guides/google-search/

https://9to5google.com/guides/android/

https://9to5google.com/guides/youtube/

https://9to5google.com/guides/chrome/

[9to5Mac]

https://9to5mac.com/

https://9to5mac.com/guides/apple-intelligence/

https://9to5mac.com/guides/ios/

https://9to5mac.com/guides/siri/

https://9to5mac.com/guides/app-store/

[Social Media Today]

https://www.socialmediatoday.com/

https://www.socialmediatoday.com/topic/social-media-updates/

https://www.socialmediatoday.com/topic/digital-marketing/

[Reuters / CNBC / Yahoo Finance / BusinessWire / PRNewswire]

https://www.reuters.com/technology/

https://www.cnbc.com/technology/

https://finance.yahoo.com/topic/ai/

https://www.businesswire.com/newsroom

https://www.prnewswire.com/news-releases/

[AI Business / VentureBeat / SiliconANGLE / Techzine / MarkTechPost / The Decoder]

https://aibusiness.com/

https://venturebeat.com/category/ai/

https://siliconangle.com/

https://www.techzine.eu/

https://www.marktechpost.com/

https://the-decoder.com/

https://www.artificialintelligence-news.com/

https://letsdatascience.com/news

---

### AI Agent

[OpenClaw]

https://openclaw.ai/blog

https://github.com/openclaw/openclaw

https://github.com/openclaw/openclaw/releases

[Moltbot]

(Google Query)

[Clawdbot]

(Google Query)

[Paperclip]

https://github.com/paperclipai/paperclip

https://github.com/paperclipai/paperclip/releases

[BabyAGI]

https://github.com/yoheinakajima/babyagi

https://github.com/yoheinakajima/babyagi/releases

[Microsoft AutoGen / AutoGen]

https://microsoft.github.io/autogen/

https://github.com/microsoft/autogen

https://github.com/microsoft/autogen/releases

https://devblogs.microsoft.com/

[AutoGPT]

https://agpt.co/

https://github.com/Significant-Gravitas/AutoGPT

https://github.com/Significant-Gravitas/AutoGPT/releases

[AgentGPT]

https://agentgpt.reworkd.ai/

https://github.com/reworkd/AgentGPT

https://github.com/reworkd/AgentGPT/releases

[Claude Cowork]

https://claude.com/blog

https://www.anthropic.com/news

https://www.anthropic.com/engineering

https://docs.anthropic.com/

[A.(에이닷)]

https://news.sktelecom.com/

https://www.sktelecom.com/

[KIRA]

https://kira.krafton-ai.com/

https://github.com/krafton-ai/KIRA

https://github.com/krafton-ai/KIRA/releases

https://www.krafton.ai/

https://www.krafton.com/news/press/

[Wrtn Crack]

https://crack.wrtn.ai/announcement

https://wrtn.io/

[Rinna]

https://rinna.co.jp/news/

https://rinna.co.jp/

[Cotomo]

https://cotomo.ai/

https://cotomo.ai/posts

https://cotomo.ai/app-posts

[CrewAI]

https://crewai.com/blog

https://docs.crewai.com/

https://github.com/crewAIInc/crewAI

https://github.com/crewAIInc/crewAI/releases

[LangGraph / LangChain]

https://www.langchain.com/blog

https://docs.langchain.com/

https://langchain-ai.github.io/langgraph/

https://github.com/langchain-ai/langgraph

https://github.com/langchain-ai/langgraph/releases

https://github.com/langchain-ai/langchain

https://github.com/langchain-ai/langchain/releases

[Chai]

https://www.chai-research.com/

https://www.chai-research.com/blog

https://www.chai-research.com/news

[Nomi]

https://nomi.ai/

https://nomi.ai/updates/

[Kindroid]

https://kindroid.ai/

https://kindroid.ai/blog/

https://kindroid.ai/docs/

https://kindroid.ai/docs/article/update-log/

[Paradot]

https://www.paradot.ai/

보조: Google Query

[Replika]

https://replika.com/

https://blog.replika.com/

[Poketomo]

https://poketomo.com/

https://poketomo.com/news/

[Hume AI]

https://www.hume.ai/

https://www.hume.ai/blog

https://www.hume.ai/news

https://dev.hume.ai/docs

[Mersoom]

(Google Query)

[Bot Madang]

(Google Query)

---

### AI / GPT

[OpenAI]

https://openai.com/news/

https://openai.com/index/

https://openai.com/research/

https://platform.openai.com/docs/changelog

https://help.openai.com/en/articles/6825453-chatgpt-release-notes

https://developers.openai.com/codex/changelog

[ChatGPT]

https://openai.com/index/

https://help.openai.com/en/articles/6825453-chatgpt-release-notes

[Codex]

https://developers.openai.com/codex/changelog

https://openai.com/index/

[Sora]

https://openai.com/sora/

https://openai.com/index/

[Meta AI]

https://ai.meta.com/blog/

https://about.fb.com/news/

https://engineering.fb.com/

https://www.facebook.com/business/news

[Scale AI]

https://scale.com/blog

https://scale.com/press

[Google AI]

https://blog.google/innovation-and-ai/

https://blog.google/technology/ai/

https://blog.google/technology/developers-tools/

https://developers.googleblog.com/

https://research.google/blog/

https://deepmind.google/blog/

[Gemini]

https://blog.google/products/gemini/

https://gemini.google/release-notes/

https://deepmind.google/technologies/gemini/

https://ai.google.dev/gemini-api/docs/changelog

[Veo]

https://deepmind.google/technologies/veo/

https://blog.google/technology/ai/

https://blog.google/innovation-and-ai/

[NotebookLM]

https://blog.google/products/notebooklm/

https://blog.google/technology/ai/

[Google Chrome]

https://blog.google/products/chrome/

https://developer.chrome.com/blog/

https://chromereleases.googleblog.com/

[Amazon AI / AWS AI]

https://www.aboutamazon.com/news/aws

https://aws.amazon.com/blogs/aws/

https://aws.amazon.com/blogs/machine-learning/

https://aws.amazon.com/about-aws/whats-new/machine-learning/

[Nova AI]

https://aws.amazon.com/ai/generative-ai/nova/

https://aws.amazon.com/blogs/machine-learning/

https://www.aboutamazon.com/news/aws

[Trainium]

https://aws.amazon.com/machine-learning/trainium/

https://aws.amazon.com/blogs/machine-learning/

https://www.aboutamazon.com/news/aws

[Anthropic]

https://www.anthropic.com/news

https://www.anthropic.com/research

https://www.anthropic.com/engineering

https://docs.anthropic.com/

[Claude]

https://claude.com/blog

https://www.anthropic.com/news

https://www.anthropic.com/research

https://docs.anthropic.com/

[Claude Code]

https://claude.com/blog

https://docs.anthropic.com/en/docs/claude-code

https://www.anthropic.com/engineering

[Microsoft]

https://blogs.microsoft.com/

https://news.microsoft.com/source/

https://www.microsoft.com/en-us/microsoft-365/blog/

https://devblogs.microsoft.com/

https://www.microsoft.com/en-us/research/blog/

[Microsoft Edge]

https://blogs.windows.com/msedgedev/

https://blogs.bing.com/search/

[Bing]

https://blogs.bing.com/search/

[Copilot]

https://www.microsoft.com/en-us/microsoft-copilot/blog/

https://www.microsoft.com/en-us/microsoft-365/blog/

https://devblogs.microsoft.com/microsoft365dev/

[Apple AI / Apple Intelligence]

https://www.apple.com/newsroom/

https://developer.apple.com/news/

https://developer.apple.com/documentation/updates/

https://developer.apple.com/documentation/appleintelligence

[Safari]

https://www.apple.com/newsroom/

https://developer.apple.com/news/

https://developer.apple.com/documentation/safari-release-notes

[Databricks]

https://www.databricks.com/blog

https://www.databricks.com/company/newsroom

https://docs.databricks.com/release-notes/index.html

[Thinking Machines Lab]

https://thinkingmachines.ai/

https://thinkingmachines.ai/news/

[Perplexity AI]

https://www.perplexity.ai/hub/blog

https://www.perplexity.ai/hub/news

[Comet]

https://www.perplexity.ai/hub/blog

https://www.perplexity.ai/hub/news

[Stability.ai]

https://stability.ai/news

https://stability.ai/blog

https://github.com/Stability-AI

[Anysphere / Cursor]

https://cursor.com/blog

https://cursor.com/changelog

https://docs.cursor.com/

[ElevenLabs]

https://elevenlabs.io/blog

https://elevenlabs.io/docs

https://elevenlabs.io/docs/changelog

[Speak AI]

https://www.speak.com/

https://www.speak.com/blog

[Writer AI]

https://writer.com/blog/

https://writer.com/newsroom/

https://writer.com/docs/

https://writer.com/product-updates/

[Ayar Labs]

https://ayarlabs.com/newsroom/

https://ayarlabs.com/blog/

[Physical Intelligence]

https://www.physicalintelligence.company/

https://www.physicalintelligence.company/blog

https://www.physicalintelligence.company/news

[Inflection AI]

https://inflection.ai/news

https://inflection.ai/blog

[Inflection AI Pi]

https://pi.ai/

https://inflection.ai/news

https://inflection.ai/blog

[Moonshot AI / Kimi]

https://www.moonshot.cn/

https://kimi.moonshot.cn/

보조: https://pandaily.com/

[Canva AI]

https://www.canva.com/newsroom/news/

https://www.canva.com/newsroom/

[Le Chat / Mistral AI]

https://mistral.ai/news/

https://docs.mistral.ai/

https://github.com/mistralai

[Leonardo AI]

https://leonardo.ai/

https://leonardo.ai/news

https://leonardo.ai/blog

[Cohere]

https://cohere.com/blog

https://cohere.com/newsroom

https://docs.cohere.com/changelog

[Skywalker.ai]

(Google Query)

[Kling AI]

https://klingai.com/

보조: https://www.kuaishou.com/en

[Seedance]

https://seed.bytedance.com/en/

https://seed.bytedance.com/en/blog

[Stable Diffusion]

https://stability.ai/news

https://stability.ai/blog

https://github.com/Stability-AI

[DALL-E]

https://openai.com/index/

https://help.openai.com/

https://platform.openai.com/docs/changelog

[Content Generator]

(Google Query)

[Craiyon]

https://www.craiyon.com/

보조: Google Query

[Midjourney]

https://www.midjourney.com/

https://docs.midjourney.com/

보조: Google Query

[MyHeritage]

https://blog.myheritage.com/

https://www.myheritage.com/ai

[Voice Synthesis]

(Google Query)

[Dream Fusion]

(Google Query)

[AI Bot]

(Google Query)

[AI Healthcare]

(Google Query)

[Image AI]

(Google Query)

[AI Assistant]

(Google Query)

[AI Plugin]

(Google Query)

[Sam Altman]

(Google Query)

[LLM]

(Google Query)

[Chatbot]

(Google Query)

[Adobe AI]

https://news.adobe.com/

https://blog.adobe.com/

https://developer.adobe.com/

[Adobe Firefly]

https://firefly.adobe.com/

https://blog.adobe.com/

https://news.adobe.com/

[character.ai]

https://blog.character.ai/

https://character.ai/

[MDM]

(Google Query)

[yandex]

https://yandex.com/company/press_releases/

https://yandex.com/blog/

https://yandex.com/dev/

[Kakao Brain / Kakao AI]

https://www.kakaocorp.com/page/

https://www.kakaocorp.com/page/detail/

https://www.kakaocorp.com/page/press

[Japan AI]

(Google Query)

[Korea AI]

(Google Query)

[China AI]

(Google Query)

[US AI]

(Google Query)

[AI Character]

(Google Query)

[Copyright Shield]

(Google Query)

[Microsoft Industry Blogs]

https://blogs.microsoft.com/

https://news.microsoft.com/source/

https://www.microsoft.com/en-us/industry/blog/

[blog.google]

https://blog.google/

---

### AI Browser / Browser

[Arc Browser]

https://browsercompany.com/

https://browsercompany.com/blog/

보조: Google Query

[Dia Browser]

https://www.diabrowser.com/

https://www.diabrowser.com/release-notes/latest

[Brave Browser]

https://brave.com/

https://brave.com/blog/

https://brave.com/latest/

https://github.com/brave/brave-browser

https://github.com/brave/brave-browser/releases

[Opera One]

https://blogs.opera.com/news/

https://blogs.opera.com/desktop/

[Sigma Browser / SigmaOS]

https://sigmaos.com/

https://sigmaos.com/blog

보조: Google Query

[Zen Browser]

https://zen-browser.app/

https://github.com/zen-browser/desktop

https://github.com/zen-browser/desktop/releases

[Wavebox]

https://wavebox.io/

https://wavebox.io/blog/

https://hub.wavebox.io/

[Vivaldi Browser]

https://vivaldi.com/

https://vivaldi.com/blog/

https://vivaldi.com/changelog/

[Sidekick Browser]

https://www.meetsidekick.com/

https://www.meetsidekick.com/blog

보조: Google Query

[Shift Browser]

https://shift.com/

https://shift.com/blog/

보조: Google Query

[Orion Browser]

https://browser.kagi.com/

https://browser.kagi.com/updates.html

[Maxthon Browser]

https://www.maxthon.com/

https://www.maxthon.com/blog/

보조: Google Query

[Firefox / Mozilla]

https://blog.mozilla.org/en/

https://blog.mozilla.org/en/firefox/

https://blog.mozilla.org/en/privacy-security/

https://www.mozilla.org/en-US/firefox/releases/

https://github.com/mozilla

[Samsung Internet]

https://news.samsung.com/global/

https://developer.samsung.com/internet

보조: Google Query

[UC Browser]

https://www.ucweb.com/

https://play.google.com/store/apps/details?id=com.UCMobile.intl

https://apps.apple.com/us/app/uc-browser/id1048518592

[CryptoTab Browser]

https://cryptobrowser.site/

https://cryptobrowser.site/en/news/

https://play.google.com/store/apps/details?id=max.cryptotab.android

---

### Global Big Tech

[Meta]

https://about.fb.com/news/

https://ai.meta.com/blog/

https://engineering.fb.com/

https://www.facebook.com/business/news

https://investor.fb.com/investor-news/default.aspx

[Facebook]

https://about.fb.com/news/

https://www.facebook.com/business/news

https://engineering.fb.com/

[Instagram]

https://about.instagram.com/blog/announcements

https://about.fb.com/news/

https://www.facebook.com/business/news

[WhatsApp]

https://blog.whatsapp.com/

https://about.fb.com/news/

https://www.facebook.com/business/news

[Amazon]

https://www.aboutamazon.com/news

https://www.aboutamazon.com/news/aws

https://www.aboutamazon.com/news/devices

https://www.aboutamazon.com/news/retail

[Amazon Prime]

https://www.aboutamazon.com/news/prime

https://www.aboutamazon.com/news/entertainment

https://www.aboutamazon.com/news/retail

[Apple]

https://www.apple.com/newsroom/

https://developer.apple.com/news/

https://developer.apple.com/documentation/updates/

https://developer.apple.com/news/releases/

[iOS]

https://www.apple.com/newsroom/

https://developer.apple.com/news/releases/

https://developer.apple.com/documentation/ios-ipados-release-notes

[Netflix]

https://about.netflix.com/en/newsroom

https://about.netflix.com/en/newsroom/company-assets

[Google]

https://blog.google/

https://blog.google/products/

https://blog.google/technology/ai/

https://blog.google/products/search/

https://blog.google/products/ads-commerce/

https://developers.googleblog.com/

https://cloud.google.com/blog/

https://www.googlecloudpresscorner.com/

[YouTube]

https://blog.youtube/

https://blog.youtube/news-and-events/

https://blog.google/products/ads-commerce/

[Android]

https://blog.google/products/android/

https://android-developers.googleblog.com/

https://developer.android.com/about/versions

[Gmail]

https://blog.google/products/gmail/

https://workspaceupdates.googleblog.com/

[Microsoft]

https://blogs.microsoft.com/

https://news.microsoft.com/source/

https://www.microsoft.com/en-us/microsoft-365/blog/

https://devblogs.microsoft.com/

https://blogs.windows.com/

https://blogs.bing.com/search/

[Grab]

https://www.grab.com/sg/press/

https://www.grab.com/sg/blog/

https://www.grab.com/sg/newsroom/

---

### Asia Big Tech

[Rakuten]

https://corp.rakuten.co.jp/news/press/

https://global.rakuten.com/corp/news/press/

https://global.rakuten.com/corp/innovation/

[Note]

https://note.jp/

https://note.jp/n/

보조: Google Query

[DeNA]

https://dena.com/intl/news/

https://dena.com/jp/news/

[Gree]

https://corp.gree.net/jp/ja/news/

https://corp.gree.net/en/news/

[Gunosy]

https://gunosy.co.jp/news/

보조: Google Query

[TimeTree]

https://timetreeapp.com/intl/newsroom

https://timetreeapp.com/intl/blog

[Mercari]

https://about.mercari.com/press/news/

https://about.mercari.com/en/press/news/

https://jp-news.mercari.com/

[Kakao]

https://www.kakaocorp.com/page/

https://www.kakaocorp.com/page/detail/

https://www.kakaocorp.com/page/press

[Coupang]

https://news.coupang.com/

https://ir.aboutcoupang.com/news-events/news/default.aspx

[Toss]

https://toss.im/news

https://toss.tech/

[Tencent]

https://www.tencent.com/en-us/articles.html

https://www.tencentcloud.com/blog

https://www.tencentcloud.com/press-release

[ByteDance]

https://www.bytedance.com/en/news

https://seed.bytedance.com/en/blog

https://newsroom.tiktok.com/

[Alibaba]

https://www.alibabagroup.com/en-US/news-and-resource

https://www.alibabacloud.com/en/press-room

https://www.alibabacloud.com/blog

https://www.alibabacloud.com/help/en/releasenotes/

[Alibaba Cloud]

https://www.alibabacloud.com/blog

https://www.alibabacloud.com/en/press-room

https://www.alibabacloud.com/help/en/releasenotes/

[Baidu / ERNIE]

https://ir.baidu.com/news-releases

https://research.baidu.com/Blog

https://yiyan.baidu.com/

보조: Google Query

[Huawei]

https://www.huawei.com/en/news

https://developer.huawei.com/consumer/en/doc/

https://www.huaweicloud.com/intl/en-us/news/

보조: Google Query

[Samsung]

https://news.samsung.com/global/

https://news.samsung.com/kr/

https://developer.samsung.com/

[SK Telecom]

https://news.sktelecom.com/

[Naver]

아카이빙 제외

단, 시장 비교/산업 트렌드 기사에서 여러 기업 중 하나로 언급될 때만 [Market] 검토

[LINE / LY Corporation]

아카이빙 제외

단, 시장 비교/산업 트렌드 기사에서 여러 기업 중 하나로 언급될 때만 [Market] 검토

---

### Social

[TikTok]

https://newsroom.tiktok.com/

https://newsroom.tiktok.com/en-us/

https://www.tiktok.com/business/en/blog

https://developers.tiktok.com/doc/changelog

[Douyin]

(Google Query)

[Snapchat / Snap]

https://newsroom.snap.com/

https://forbusiness.snapchat.com/blog

https://eng.snap.com/blog

[Telegram]

https://telegram.org/blog

https://telegram.org/apps

https://core.telegram.org/api#recent-changes

[Pinterest]

https://newsroom.pinterest.com/en/

https://business.pinterest.com/en/blog/

https://pinterestcannes.com/

[X / Twitter]

https://blog.x.com/

https://business.x.com/en/blog

https://docs.x.com/x-api/changelog

[XChat]

(Google Query)

[BlueSky]

https://bsky.social/about/blog

https://github.com/bluesky-social

https://github.com/bluesky-social/atproto

[Twitch]

https://blog.twitch.tv/en/

https://dev.twitch.tv/docs/change-log/

https://safety.twitch.tv/s/

[BeReal]

(Google Query)

[Discord]

https://discord.com/blog

https://discord.com/newsroom

https://discord.com/safety

https://discord.com/developers/docs/change-log

https://github.com/discord

[LinkedIn]

https://news.linkedin.com/

https://www.linkedin.com/business/marketing/blog

보조: https://www.socialmediatoday.com/

[Reddit]

https://redditinc.com/news

https://redditinc.com/blog

https://www.redditinc.com/policies/transparency-report

[PayPal]

https://newsroom.paypal-corp.com/

https://www.paypal.com/us/brc/article/

[VSCO]

https://vsco.co/vsco/journal

보조: Google Query

[Spotify]

https://newsroom.spotify.com/

https://engineering.atspotify.com/

---

### Enterprise / Agentic AI / Security / Infra

[Oracle]

https://blogs.oracle.com/

https://blogs.oracle.com/ai-and-datascience/

https://blogs.oracle.com/machinelearning/

https://www.oracle.com/news/

[ServiceNow]

https://newsroom.servicenow.com/

https://www.servicenow.com/blogs.html

[Snowflake]

https://www.snowflake.com/en/news/

https://www.snowflake.com/en/blog/

https://docs.snowflake.com/en/release-notes/overview

[Okta]

https://www.okta.com/newsroom/

https://www.okta.com/blog/

[Snyk]

https://snyk.io/news/

https://snyk.io/blog/

https://docs.snyk.io/snyk-release-notes

[Zscaler]

https://www.zscaler.com/press

https://www.zscaler.com/blogs

[Palo Alto Networks]

https://www.paloaltonetworks.com/blog/

https://www.paloaltonetworks.com/company/press

[Cloudflare]

https://blog.cloudflare.com/

https://www.cloudflare.com/press-releases/

https://developers.cloudflare.com/release-notes/

[Cisco]

https://newsroom.cisco.com/

https://blogs.cisco.com/

[SAP]

https://news.sap.com/

https://community.sap.com/

[Datadog]

https://www.datadoghq.com/about/latest-news/

https://www.datadoghq.com/blog/

[Workday]

https://newsroom.workday.com/

https://blog.workday.com/

[Cognizant]

https://news.cognizant.com/

https://www.cognizant.com/us/en/insights

[HPE]

https://www.hpe.com/us/en/newsroom.html

https://www.hpe.com/us/en/newsroom/blog-post.html

[Red Hat]

https://www.redhat.com/en/blog

https://www.redhat.com/en/about/press-releases

[GitHub / GitHub Copilot]

https://github.blog/changelog/

https://github.blog/ai-and-ml/

https://docs.github.com/en/copilot

https://github.com/features/copilot

[Replit]

https://blog.replit.com/

https://docs.replit.com/updates

[JetBrains]

https://blog.jetbrains.com/

https://www.jetbrains.com/ai/

https://www.jetbrains.com/help/

[Getty Images]

https://newsroom.gettyimages.com/

보조: Google Query

[RightCapital]

https://www.rightcapital.com/

https://www.rightcapital.com/news

보조: Google Query

[Maxima]

(Google Query)

[MoEngage]

https://www.moengage.com/newsroom/

https://www.moengage.com/blog/

[Fika Jobs]

(Google Query)

[DaVinci Commerce]

https://davincicommerce.ai/

보조: Google Query

[Moneris]

https://www.moneris.com/en/about-moneris/news

보조: Google Query

[Verint]

https://www.verint.com/press-room/

https://www.verint.com/blog/

[Five9]

https://www.five9.com/newsroom

https://www.five9.com/blog

[Zuora]

https://www.zuora.com/press-room/

https://www.zuora.com/resource/

[Sakana AI]

https://sakana.ai/

https://sakana.ai/news/

https://sakana.ai/blog/

https://github.com/SakanaAI

[Nokia]

https://www.nokia.com/newsroom/

https://www.nokia.com/blog/

[Linux Foundation]

https://www.linuxfoundation.org/press

https://www.linuxfoundation.org/blog

[Coinbase]

https://www.coinbase.com/blog

https://www.coinbase.com/newsroom

https://docs.cdp.coinbase.com/

[Visa]

https://usa.visa.com/about-visa/newsroom.html

https://developer.visa.com/pages/release-notes

[Mastercard]

https://www.mastercard.com/news/

https://developer.mastercard.com/release-notes/

[Robinhood]

https://newsroom.aboutrobinhood.com/

https://robinhood.com/us/en/newsroom/

[Asana]

https://asana.com/press

https://asana.com/inside-asana

https://developers.asana.com/docs/changelog

---

### Theme / Market Query

[AI Startup]

(Google Query)

[TechCrunch AI Startup]

https://techcrunch.com/category/artificial-intelligence/

https://techcrunch.com/category/startups/

[Generative AI]

(Google Query)

[AI Agent / Agentic AI]

(Google Query)

[AI Infrastructure]

(Google Query)

[AI Security]

(Google Query)

[AI Regulation]

(Google Query)

[AI Layoffs]

(Google Query)

[AI Bubble / AI Investment]

(Google Query)

[AI IPO]

(Google Query)

[AI Copyright]

(Google Query)

[AI Safety]

(Google Query)

[Open Source AI]

(Google Query)

[AI Search]

(Google Query)

[AI Advertising]

(Google Query)

[AI Commerce / Agentic Commerce]

(Google Query)

[AI Payments]

(Google Query)

[AI Healthcare]

(Google Query)

[AI Education]

(Google Query)

[AI Browser]

(Google Query)

[Social Media Search]

(Google Query)

[Creator Economy]

(Google Query)

[Gen Z / MZ Trend]

(Google Query)

[Virtual Consumption / 가상 소비]

(Google Query)

## Query List 적용 방식

- Query List는 Weekly Archiving 기본 검색 대상 목록으로 사용
- 모든 Query는 작업자 입력 날짜 범위 `YYYY/MM/DD~YYYY/MM/DD` 기준으로 검색
- `(Google Query)` 표시 항목:
  - Official Source 확인 대상 아님
  - Google Search 또는 Google News에서만 검색
- `(Google Query)` 표시가 없는 기업명, 서비스명, 기능명:
  - Official Sources 우선 확인
  - GitHub, Changelog, Release Notes, Docs, Blogs 우선 확인
  - 이후 Google Query로 보완 검색
- Official Source가 없거나 확인이 어려운 일반 키워드성 Query:
  - Google Query만 진행
- Query별 검색 결과 판단 기준:
  - 기사 선별 기준
  - 국가 중요도
  - 중복 여부
  - Paywall 여부
  - URL 언어 기준
- Query List 포함 항목도 중요도가 낮거나 단순 PR성이면 제외
- Query List 외 항목도 주요 IT/AI/플랫폼 트렌드면 추가 검토 가능
- 동일 Query가 여러 카테고리에 반복되면 공통 Query로 관리
- AI Agent 및 AI Query는 Weekly AI Trend Report와 Global IT Trend Report 공통 참고 가능
- Global IT Trend Report는 AI 외 Big Tech, Asia Big Tech, Social, Theme 관련 IT 트렌드 기사 포함 가능

## Official Source 확인 방식

- 기업별 공식 채널 먼저 확인:
  - Blog
  - Newsroom
  - Developer Blog
  - Product Update Page
- Official Source 정보는 신뢰도 높게 우선순위 부여
- Official Source와 외부 기사 내용이 겹치면 Official Source 기준으로 내용 확인
- 외부 기사는 아래 용도로 활용:
  - 보완 설명
  - 시장 반응
  - 투자 규모
  - 파트너십 맥락
- 영어 Official Source가 있으면 영어 페이지 우선 사용
- 영어 페이지가 없고 한국어/일본어 공식 링크만 있으면 현지어 공식 링크 사용 가능
- `(Google Query)` 표시 항목은 Official Source 확인 없이 Google Query만 진행

## Google Query 및 외부 기사 검색 방식

- Official Source 및 우선 확인 소스 확인 후 Google News 또는 Google Search 활용
- `(Google Query)` 표시 항목은 Google News 또는 Google Search만 활용
- 검색어 조합 예시:
  - 기업명
  - 서비스명
  - AI
  - update
  - launch
  - partnership
  - funding
  - regulation
- 검색 기간은 작업자 입력 `YYYY/MM/DD~YYYY/MM/DD` 범위 적용
- 검색 결과는 최신순과 관련도 기준으로 확인
- 동일 내용이 여러 매체에 반복되면 아래 우선순위 적용:
  1. 원출처에 가까운 기사
  2. Official Source
  3. 신뢰도 높은 Tech Media
  4. 본문 접근 가능한 영어 기사
- Google Query 신규 발견 기사는 과거 중복 여부 확인 후 Sheet 입력

## Google Query 기사 중복 확인 방식

- Sheet 입력 전 반드시 과거 중복 여부 확인
- 확인 방식:
  1. 기존 검색 날짜 필터 해제
  2. 기사 타이틀로 재검색
  3. 핵심 키워드로 재검색
  4. 동일 기사 또는 동일 이슈의 과거 주차 사용 여부 확인
- 최신 발행 기사라도 아래 경우 제외:
  - 과거 기사 재사용
  - 재배포
  - 업데이트 없는 반복 보도
- 과거 동일 기사 또는 동일 이슈가 있으면 `중복` 표시 후 제외
- 신규 기사로 유지 가능한 경우:
  - 후속 발표
  - 신규 기능 추가
  - 새로운 수치
  - 새로운 지역 출시
  - 새로운 파트너십
- 애매한 경우 비고란 표시:
  - `중복 가능성`
  - `후속 기사`
  - `기존 이슈 업데이트`

## 기사 선별 기준

- 아래 기준에 해당하면 선별 가능:
  - AI 기능 출시
  - AI Agent
  - 생성형 AI
  - LLM
  - 모델 업데이트
  - AI 인프라
  - Big Tech 주요 제품 업데이트
  - 플랫폼 전략
  - 광고
  - 커머스
  - 검색
  - OS
  - Social 서비스 신규 기능
  - 유저 성장
  - 커뮤니티 기능
  - 크리에이터 기능
  - Asia Big Tech의 AI, 플랫폼, 콘텐츠, 커머스, 메신저, 앱 서비스
  - 시장 구조 변화
  - 유저 행동 변화
  - 규제
  - 투자
  - 파트너십
  - 플랫폼 수익화
  - 광고 상품
  - 구독 모델
  - 크리에이터 생태계 변화
  - 국가별 정책, 법안, 보안, 개인정보 이슈
  - 시장 전반에 영향을 줄 수 있는 기사

## 기사 제외 기준

- 아래 기준에 해당하면 제외:
  - AI/GPT 카테고리에서 AI 또는 AI Agent 관련성이 약한 기사
  - Global IT Trend Report 관점에서 IT, 플랫폼, social media, 커머스, 광고, 콘텐츠, 규제, 유저 행동 변화와 연결성이 낮은 기사
  - Naver 단독 기사
  - LINE 단독 기사
  - LY Corporation 단독 기사
  - 단순 이벤트 안내
  - 단순 할인
  - 단순 인사 이동 기사
  - 의미 있는 기능 변화 없는 홍보성 기사
  - 동일 내용 반복 보도
  - 과거 주차 사용 기사
  - 동일 이슈 단순 재사용 기사
  - 출처 신뢰도가 낮은 기사
  - 원문 확인이 어려운 기사
  - Weekly AI Trend Report 또는 Global IT Trend Report 활용이 어려운 기사
  - 본문 접근 불가능한 Paywall 기사
  - 제목만 확인 가능한 기사

## 국가 중요도 우선순위

- 국가 우선순위는 절대 제외 기준이 아님
- 기사 중요도와 리포트 반영 우선순위 판단 기준으로 사용

### 1순위

- US
- Global

### 2순위

- China
- Japan
- Korea

### 3순위

- Taiwan
- Thailand
- Singapore
- India

### 4순위

- UK
- EU
- Canada
- Australia

### 5순위

- Indonesia
- Vietnam
- Malaysia
- Philippines

### 6순위

- Middle East
- LATAM
- Africa
- 기타 지역

## 국가 우선순위 적용 방식

- US, Global:
  - Big Tech, AI, 플랫폼 전략, 광고, 커머스, social media 변화와 연결 시 우선 검토
- China, Japan, Korea:
  - Asia Big Tech 및 주요 플랫폼 변화와 연결 시 우선 검토
- Taiwan, Thailand, Singapore, India:
  - AI, social media, 커머스, 메신저, 슈퍼앱, 플랫폼 성장 관련 시 적극 검토
- UK, EU:
  - 규제, AI 법안, 플랫폼 정책, 개인정보, 광고 정책 변화 관련 시 우선 검토
- Southeast Asia:
  - Grab, TikTok, LINE, Shopee, Lazada, social commerce, creator economy 관련 시 검토
- 낮은 우선순위 국가라도 포함 가능한 경우:
  - 글로벌 확산 가능성
  - 신규 시장 진입
  - Big Tech 전략 변화
  - 대규모 투자
  - 규제 영향
- 높은 우선순위 국가라도 제외 가능한 경우:
  - 단순 이벤트
  - 단순 PR
  - 영향도 낮은 기사

## Cluster 처리 방식

- 동일 이벤트 기사는 하나의 Cluster로 묶어 관리
- Cluster 판단 기준:
  - 같은 기업
  - 같은 기능
  - 같은 발표
  - 같은 파트너십
  - 같은 투자
  - 같은 규제 이슈
- Cluster 내 최종 유지 원칙:
  1. Official Source 우선
  2. 접근 가능한 영어 원문 기사
  3. 신뢰도 높은 Tech Media
- 제외:
  - 단순 재보도
  - 내용 반복
  - 출처 불명확 기사
- 보완 기사 유지 가능 조건:
  - 새로운 수치
  - 신규 지역 출시
  - 후속 발표
  - 추가 기능
  - 시장 반응
- 비고란 표시 예시:
  - `대표 기사 유지`
  - `중복 제외`
  - `보완 기사 유지`

## Paywall 기사 처리 방식

- Bloomberg, Reuters, NYTimes 등은 본문 접근 가능 여부 확인
- 본문 확인이 어려운 Paywall 기사는 최종 URL로 사용 금지
- Paywall 기사는 이슈 파악용 Seed로만 활용
- 접근 불가 시 처리 순서:
  1. 동일 타이틀로 Google Query 재검색
  2. 핵심 키워드로 Google Query 재검색
  3. 동일 이슈의 접근 가능한 기사 확인
  4. 원문성과 신뢰도 확인
  5. 최종 URL 교체
- 대체 기사도 단순 인용이면 원출처 또는 공식 발표 재확인
- 최종 URL은 작업자가 실제 열람 가능한 링크만 입력

## URL 언어 기준

- 기본 원칙:
  - 영어 원문 기사 우선
  - 영어 공식 링크 우선
- 동일 이슈에 영어 기사와 비영어 기사가 모두 있으면 영어 기사 우선
- 기업 공식 Blog, Newsroom, Docs에 영어 페이지가 있으면 영어 페이지 사용
- 한국/일본 기업 관련 기사는 한국어/일본어 링크 사용 가능
- 예외 기업 예시:
  - Coupang
  - Kakao
  - Toss
  - DeNA
  - Mercari
  - Rakuten
  - Note
  - Gree
  - Gunosy
- 영어 링크가 없고 현지어 공식 링크만 있으면 현지어 공식 링크 사용 가능
- 단순 번역 기사보다 기업 공식 발표 또는 원출처에 가까운 링크 우선
- 최종 URL은 실제 접속 가능하고 본문 확인 가능한 링크 사용

## Sheet 정리 방식

- 주차별 새 탭 생성
- 기존 템플릿 서식 유지
- 카테고리별 기사 정리
- 입력 기준:
  - 기사 제목: 원문 제목
  - 날짜: 기사 발행일
  - URL: 바로 접근 가능한 원문 링크
  - 카테고리: AI/GPT, Global Big Tech, Asia Big Tech, Social, Theme 중 선택
  - 주요 내용: 핵심 변화 중심으로 간단히 작성
  - 포함 여부/비고: 상태값 입력
- 상태값 예시:
  - `PASS`
  - `중복`
  - `보류`
  - `Paywall 대체`
  - `대표 기사 유지`
  - `중복 가능성`
  - `후속 기사`
  - `기존 이슈 업데이트`
- 필요한 경우 선정 사유 또는 제외 사유 작성
- Cluster 처리 기사는 대표 기사와 제외 기사 구분 표시
- 과거 중복 확인 필요 기사는 비고란에 확인 결과 작성

## 중복 기사 처리 방식

- 같은 기업, 같은 기능, 같은 발표 내용은 중복 처리
- 동일 이벤트 기사는 Cluster 단위로 관리
- 각 Cluster에서 가장 적합한 Source 1개만 최종 유지
- Official Source와 외부 기사 중복 시 Official Source 우선
- Paywall 기사는 최종 URL로 사용하지 않고 접근 가능한 기사로 대체
- 외부 기사 우선순위 예시:
  - TechCrunch
  - The Verge
  - 9to5Mac
  - 9to5Google
  - Social Media Today
- Google Query 기사는 날짜 필터 해제 후 타이틀 또는 핵심 키워드로 과거 사용 여부 확인
- 과거 사용 기사 또는 동일 이슈 단순 재사용 기사는 제외
- 실질적 업데이트가 있으면 신규 기사로 유지:
  - 후속 발표
  - 신규 수치
  - 신규 지역 출시
  - 신규 기능 추가
- 중복 기사 삭제 전 비고란에 남길 기사와 제외 기사 표시

## 최종 Title 작성 방식

- 최종 선별 기사에는 Korean Title 필수 작성

### Title 기본 형식

- `[Company Name] Korean Title (YYYY/M/DD) - URL`

### Title 작성 규칙

- Company Name은 English로 작성
- Title 본문은 Korean으로 작성
- 날짜는 기사 발행일 기준으로 작성
- 날짜는 0 padding 없이 작성
  - 예시: `2026/6/24`
- Title은 항상 명사형 종결
- 문장 끝 금지 표현:
  - `함`
  - `있음`
  - `없음`
  - `됨`
- 기업명, 서비스명, 기능명은 English로 작성
- 신규 기능명 또는 신규 서비스명은 필요한 경우 큰따옴표 사용 가능
- 기존 서비스명, 기존 기능명에는 불필요한 큰따옴표 사용 금지
- 제목은 핵심 변화 중심으로 간결하게 작성
- 쉼표는 가급적 1개 이하로 사용

### `[Market]` 사용 기준

- 아래 기사에는 `[Company Name]` 대신 `[Market]` 사용:
  - 여러 기업을 함께 다루는 기사
  - market-wide trends 기사
  - country-level trends 기사
  - industry changes 기사
  - company strategy comparisons 기사
  - 특정 기업보다 시장 구조 변화가 더 중요한 기사
  - 특정 국가의 유저 행동, 규제, 산업 변화, 소비 트렌드 기사

### Title 예시

- `[Google] Gemini 기반 Search AI Mode 확장과 광고 노출 테스트 본격화 (2026/6/24) - URL`
- `[Meta] WhatsApp Channels 광고 도입으로 메신저 수익화 전략 확대 (2026/6/24) - URL`
- `[Kakao] ChatGPT 기반 AI 챗봇 도입으로 KakaoTalk 내 검색·대화 경험 강화 (2026/6/24) - URL`
- `[Market] US Gen Z의 social media 검색 증가로 기존 Search 중심 정보 탐색 구조 변화 (2026/6/24) - URL`

## Query 전체 리스트

### Weekly IT Trend Report

#### AI Agent - Google Query

- OpenClaw
- Moltbot
- Clawdbot
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

#### AI - Google Query

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
- Microsoft
- Microsoft Edge
- Bing
- Copilot
- Apple AI
- Safari
- Databricks
- Thinking Machines Lab
- Perplexity AI
- Comet
- Stability.ai
- Anysphere
- Cursor
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
- Sigma Browser
- SigmaOS
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
- TechCrunch AI Startup
- Stable Diffusion
- DALL-E
- Content Generator
- Craiyon
- Midjourney
- MyHeritage
- Voice Synthesis(Google Query)
- Dream Fusion
- AI Bot(Google Query)
- AI Healthcare(Google Query)
- Image AI(Google Query)
- AI Assistant(Google Query)
- AI Plugin(Google Query)
- Sam Altman(Google Query)
- LLM(Google Query)
- Inflection AI
- Inflection AI Pi
- Chatbot(Google Query)
- Adobe AI
- Adobe Firefly
- character.ai
- MDM
- yandex
- Kakao Brain
- Kakao AI
- Japan AI(Google Query)
- Korea AI(Google Query)
- China AI(Google Query)
- US AI(Google Query)
- AI Character(Google Query)
- Copyright Shield(Google Query)
- Microsoft Industry Blogs
- blog.google

### Global IT Trend Report

#### AI Agent - Google Query

- OpenClaw
- Moltbot
- Clawdbot
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

#### AI - Google Query

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
- Microsoft
- Microsoft Edge
- Bing
- Copilot
- Apple AI
- Safari
- Databricks
- Thinking Machines Lab
- Perplexity AI
- Comet
- Stability.ai
- Anysphere
- Cursor
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
- Sigma Browser
- SigmaOS
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
- TechCrunch AI Startup
- Stable Diffusion
- DALL-E
- Content Generator
- Craiyon
- Midjourney
- MyHeritage
- Voice Synthesis(Google Query)
- Dream Fusion
- AI Bot(Google Query)
- AI Healthcare(Google Query)
- Image AI(Google Query)
- AI Assistant(Google Query)
- AI Plugin(Google Query)
- Sam Altman(Google Query)
- LLM(Google Query)
- Inflection AI
- Inflection AI Pi
- Chatbot(Google Query)
- Adobe AI
- Adobe Firefly
- character.ai
- MDM
- yandex
- Kakao Brain
- Kakao AI
- Japan AI(Google Query)
- Korea AI(Google Query)
- China AI(Google Query)
- US AI(Google Query)
- AI Character(Google Query)
- Copyright Shield(Google Query)
- Microsoft Industry Blogs
- blog.google

#### Global Big Tech

- [Meta] Meta
- [Meta] Facebook
- [Meta] Instagram
- [Meta] WhatsApp
- [Amazon] Amazon
- [Amazon] Amazon Prime
- [Apple] Apple
- [Apple] iOS
- [Netflix] Netflix
- [Google] Google
- [Google] YouTube
- [Google] Android
- [Google] Gmail
- [Microsoft] Microsoft
- [Grab] Grab

#### Asia Big Tech

- [Rakuten] Rakuten
- [Rakuten] 楽天市場
- [Note] note
- [Note] ノート
- [DeNA] DeNA
- [Gree] Gree
- [Gree] グリー
- [Gunosy] Gunosy
- [Gunosy] グノシー
- [Time Tree] Time Tree
- [Time Tree] タイムツリ
- [Mercari] Mercari
- [Mercari] メルカリ
- The Bridge(Query)
- Ascii Startup(Query)
- CNET(Query)
- Diamond(Query)
- [Kakao] Kakao
- [Kakao] 카카오
- [Kakao] 카카오톡
- [Coupang] Coupang
- [Coupang] 쿠팡
- [Toss] Toss
- [Toss] 토스
- [Tencent] Tencent
- [Tencent] WeChat
- [Tencent] 微信
- [ByteDance] ByteDance
- [Alibaba] Alibaba

#### Asia Big Tech 제외 대상

- [Naver] Naver 단독 기사 제외
- [Naver] 네이버 단독 기사 제외
- [LINE] LINE 단독 기사 제외
- [LY Corporation] LY Corporation 단독 기사 제외
- 시장 전체 트렌드나 여러 기업 비교 기사에서 일부로 언급되는 경우 `[Market]` 기준으로만 검토

#### Social

- [TikTok] TikTok
- [TikTok] Douyin
- [Snap] Snapchat
- [Telegram] Telegram
- [Pinterest] Pinterest
- [x] X
- [x] XChat
- [BlueSky] BlueSky
- [Twitch] Twitch
- [BeReal] BeReal
- [Discord] Discord

#### Theme

- Super App
- Reddit
- Spotify
- VSCO
- LinkedIn
- MZ Gen
- Gen Z
- 1020 trend
- Social app
- TechCrunch Startup

## Query별 검색 결과 정리 방식

1. 날짜 범위 적합 여부 확인
2. 기사 원문 접근 가능 여부 확인
3. Paywall 여부 확인
4. 영어 URL 존재 여부 확인
5. 과거 동일 기사 또는 동일 이슈 사용 여부 확인
6. 동일 이벤트 기사 Cluster 처리
7. 가장 적합한 Source 1개 최종 유지
8. Naver, LINE, LY Corporation 단독 기사 여부 확인
9. Sheet 입력
10. 최종 Korean Title 작성

## 최종 검수 체크리스트

- [ ] Google Query 전 우선 확인 링크의 공식 사이트, Blog, Newsroom, GitHub, release notes, changelog 확인
- [ ] 입력한 날짜 범위에 맞는 기사만 포함
- [ ] Google Query 전 우선 확인 소스 먼저 확인
- [ ] `(Google Query)` 표기 항목은 Official Source 확인 없이 Google Query로만 검색
- [ ] Official Source, GitHub, Changelog, Release Notes, Docs, Blogs 확인
- [ ] 9to5Mac, 9to5Google, TechCrunch, Social Media Today 등 주요 Tech Media 확인
- [ ] 카테고리 분류 정확성 확인
- [ ] Global IT Trend Report에 AI 외 IT, 플랫폼, social media, 커머스, 규제, 유저 트렌드 기사 포함 여부 확인
- [ ] AI/GPT 기사가 별도 시트에 반영
- [ ] Naver, LINE, LY Corporation 단독 기사 제외
- [ ] Google Query 기사 날짜 필터 해제 후 과거 중복 여부 확인
- [ ] 동일 이벤트 기사 Cluster 단위 정리
- [ ] 각 Cluster에서 가장 적합한 Source 1개만 유지
- [ ] Paywall 기사를 접근 가능한 기사로 대체
- [ ] URL이 영어 원문 또는 영어 공식 링크 기준으로 정리
- [ ] 한국어/일본어 링크가 예외 기업 또는 현지어 공식 링크 기준에 부합
- [ ] 단순 PR성 기사나 비대상 기사 제외
- [ ] URL 정상 접속 확인
- [ ] 기사 날짜와 출처 정확성 확인
- [ ] 최종 Korean Title 작성
- [ ] Title이 `[Company Name] Korean Title (YYYY/M/DD) - URL` 형식에 부합
- [ ] Title이 명사형 종결
- [ ] `[Market]` 사용 기준 정확히 적용
- [ ] Weekly AI Trend Report와 Global IT Trend Report에 활용 가능한 기사만 유지

## 최종 산출물

- 기사 리스트업 Sheet의 주차별 탭
- Weekly AI Trend Report 작성용 AI/GPT 기사 리스트
- Global IT Trend Report 작성용 카테고리별 기사 리스트
- Cluster 처리된 대표 기사 리스트
- 제외 기사 및 중복 기사 확인 기록
- Paywall 대체 기사 기록
- 최종 Korean Title 리스트

## 산출물 활용 방식

- AI/GPT 기사는 Weekly AI Trend Report 작성에 활용
- Global Big Tech, Asia Big Tech, Social, Theme 기사는 Global IT Trend Report 작성에 활용
- Cluster 대표 기사는 최종 리포트 기사 후보로 활용
- 제외 기사와 중복 기사 기록은 이후 중복 방지용으로 활용
- 최종 Korean Title은 리포트 작성 및 Sheet 정리 시 그대로 활용 가능
