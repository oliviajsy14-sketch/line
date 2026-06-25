# Weekly Archiving Process

## 목차

- [업무 목적](#업무-목적)
- [기본 작업 단위](#기본-작업-단위)
- [카테고리 구분](#카테고리-구분)
- [AI Agent 구역 처리 방식](#ai-agent-구역-처리-방식)
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
- [Global IT Trend Report 기사 중요도 및 정렬 기준](#global-it-trend-report-기사-중요도-및-정렬-기준)
- [수집과 최종 선택의 구분](#수집과-최종-선택의-구분)
- [기사 제외 기준](#기사-제외-기준)
- [국가 중요도 우선순위](#국가-중요도-우선순위)
- [국가 우선순위 적용 방식](#국가-우선순위-적용-방식)
- [Cluster 처리 방식](#cluster-처리-방식)
- [Paywall 기사 처리 방식](#paywall-기사-처리-방식)
- [URL 언어 기준](#url-언어-기준)
- [Sheet 정리 방식](#sheet-정리-방식)
- [Sheet 입력 권장 컬럼](#sheet-입력-권장-컬럼)
- [Check Box 운영 기준](#check-box-운영-기준)
- [n/a 입력 기준](#na-입력-기준)
- [URL 입력 기준](#url-입력-기준)
- [중복 기사 및 보조 출처 처리 방식](#중복-기사-및-보조-출처-처리-방식)
- [대분류별 기사 수 표기 방식](#대분류별-기사-수-표기-방식)
- [자동화 입력값](#자동화-입력값)
- [자동화 출력값](#자동화-출력값)
- [중복 기사 처리 방식](#중복-기사-처리-방식)
- [최종 Title 작성 방식](#최종-title-작성-방식)
- [Query 전체 리스트](#query-전체-리스트)
- [Query별 검색 결과 정리 방식](#query별-검색-결과-정리-방식)
- [최종 검수 체크리스트](#최종-검수-체크리스트)
- [최종 산출물](#최종-산출물)
- [산출물 활용 방식](#산출물-활용-방식)
- [수정 요약](#수정-요약)

## 업무 목적

- 주간 단위로 주요 IT 및 AI 관련 뉴스 수집
- 수집 기사를 기사 리스트업 Sheet에 카테고리별 정리
- Weekly AI Trend Report 및 Global IT Trend Report 작성에 활용
- 중복 기사, 비대상 기사, 단순 PR성 기사 제외
- Query별 관련 기사를 넓게 수집하고 최종 리포트 반영 여부는 작업자가 Check Box로 선택

## 기본 작업 단위

- 작업 주기: 주 1회
- 검색 기간: 작업자가 `yyyy.mm.dd~yyyy.mm.dd` 형식으로 직접 입력
- 검색 기간 예시: `2026.6.18~2026.6.24`
- 작업 위치: 기사 리스트업 Sheet
- 탭 생성 방식: 주차별 새 탭 생성
- 탭명 예시: `4월 3주`, `4월 4주`, `6월 4주`
- 템플릿 관리: 기존 서식 유지 후 새 탭에 복사
- 저장 인코딩: UTF-8

## 카테고리 구분

- AI Agent
- AI/GPT
- Global Big Tech
- Asia Big Tech
- Social
- Theme

## 카테고리별 기준

### AI Agent

- AI Agent는 Weekly AI Trend Report에서 별도 상단 구역으로 관리 가능
- 리포트 카테고리 기준으로는 AI/GPT에 포함
- Sheet에서는 AI Agent 관련 Query가 많기 때문에 `AI Agent`를 별도 대분류로 배치 가능
- 포함 범위:
  - OpenClaw
  - AutoGPT
  - AgentGPT
  - CrewAI
  - LangGraph
  - Claude Code
  - agentic workflow
  - enterprise AI agent
  - agentic commerce
  - AI payment
  - AI security
- AI Agent 관련 기사는 원문 제목과 본문을 참고하되, Sheet에는 최종 리포트용 `Korean Title`만 입력
- Check Box는 자동화 agent가 임의로 체크하지 않고 기본 미체크 상태로 생성

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
- AI/GPT 기사는 원문 제목과 본문을 참고하되, Sheet에는 최종 리포트용 `Korean Title`만 입력
- 원문 제목은 기사 이해와 제목 작성 참고용으로만 사용하고, 별도 `Original Title` 컬럼으로 입력하지 않음
- AI/GPT도 다른 카테고리와 동일하게 최종 Sheet에는 국문 제목 중심으로 정리
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
- [ ] 검색 기간이 `yyyy.mm.dd~yyyy.mm.dd` 형식인지 확인
- [ ] 기사 리스트업 Sheet의 기존 템플릿 확인
- [ ] 새 주차 탭 생성
- [ ] 기존 서식 유지
- [ ] 카테고리별 입력 영역 확인
- [ ] 이전 주차 기사와 중복 확인이 가능하도록 기존 Sheet 접근 상태 확인

## 날짜 입력 방식

- 입력 형식: `yyyy.mm.dd~yyyy.mm.dd`
- 입력 예시: `2026.6.18~2026.6.24`
- 개별 기사 발행일 형식: `yyyy.mm.dd`
- 적용 범위:
  - Official Source 확인
  - Google News 검색
  - Google Search 검색
  - 기사 발행일 검수
- 주의사항:
  - Sheet 최종 Title 날짜는 0 padding 없이 `yyyy.m.d` 형식으로 작성
  - 최종 Title 날짜 예시: `2026.6.24`
  - 날짜에는 `/`를 사용하지 않음

## 전체 작업 순서

1. 작업자가 입력한 날짜 범위 확인
2. 기존 Sheet 템플릿 복사 후 새 주차 탭 생성
3. 카테고리별 Query List 확인
4. Google Query 전 우선 확인 링크에서 Official Source, Blog, Newsroom, GitHub, Release Notes, Changelog 먼저 확인
5. `(Google Query)` 표시 항목은 Google Search 또는 Google News에서 검색
6. 공식 링크에서 누락 가능성이 있는 항목은 Google News / Google Search로 보완 검색
7. 공통 Tech / AI / Social Source에서 주요 기사 추가 확인
8. Naver / LINE / LY Corporation 단독 기사 제외
9. Paywall 기사, 완전 중복 기사, 단순 재보도 기사 정리
10. 관련 기사를 Query / Service별로 중요도 순 정렬
11. 실제 Sheet 구조에 맞춰 Korean Title, Check Box, URL 입력
12. 기사 없음이 확인된 Query / Service는 `n/a` 입력
13. 자동화 agent는 Check Box를 미체크 상태로 둠
14. 작업자가 최종 검토 후 리포트 후보 기사만 Check Box 직접 체크

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
- 모든 Query는 작업자 입력 날짜 범위 `yyyy.mm.dd~yyyy.mm.dd` 기준으로 검색
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
- 검색 기간은 작업자 입력 `yyyy.mm.dd~yyyy.mm.dd` 범위 적용
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
- 과거 동일 기사 또는 동일 이슈가 있으면 `중복` 또는 `보조 출처`로 표시하고 대표 기사 아래 기록
- 신규 기사로 유지 가능한 경우:
  - 후속 발표
  - 신규 기능 추가
  - 새로운 수치
  - 새로운 지역 출시
  - 새로운 파트너십
- 애매한 경우 내부 판단 기준으로만 활용:
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

## Global IT Trend Report 기사 중요도 및 정렬 기준

Global IT Trend Report의 기사 리스트업 목적은 중요한 기사만 선별하는 것이 아니라, Global IT / AI / Big Tech / Social / Asia Tech / Market Trend와 관련된 기사를 빠짐없이 수집한 뒤, 검토자가 보기 쉽도록 중요도에 따라 시트 내 배치 순서를 정리하는 것이다.

- 중요도는 기사 포함/제외 기준이 아님
- 중요도는 해당 Query 섹션 안에서 어떤 기사를 위에 배치할지 판단하기 위한 정렬 기준으로만 사용
- 중요도가 낮아 보이는 기사라도 Global IT Trend Report의 카테고리와 관련성이 있으면 절대 누락하지 않고 반드시 리스트업

### 기본 원칙

- Global IT / AI / Big Tech / Asia Tech / Social / Market Trend 관련 기사는 중요도와 관계없이 모두 리스트업
- 중요한 기사는 해당 Query 섹션의 위쪽에 배치
- 중요도가 낮거나 단순 PR성 기사라도 관련성이 있으면 아래쪽에 배치
- 자동으로 중요하지 않다고 판단해 기사 제외 금지
- 최종적으로 각 Query 안에서는 `시장 영향이 큰 기사 → 기업/서비스 변화 기사 → 일반 관련 기사 → 중복/보조 출처` 순서로 정렬
- 같은 내용의 중복 기사도 완전히 삭제하지 않고 대표 기사와 함께 보조 출처 또는 중복으로 기록
- 공식 Newsroom, Blog, Release Notes, Changelog, GitHub Release도 제품·서비스·기능·시장 변화가 있으면 일반 기사처럼 리스트업
- Weekly AI Trend Report보다 더 넓게 보되, Global IT Trend Report에서는 기술 자체보다 서비스화, 사업화, 시장 변화, 유저 접점 변화, 글로벌 경쟁 구도를 우선적으로 상단 배치

### 상단 배치해야 하는 중요 기사 기준

아래 내용에 해당하는 기사는 해당 Query 섹션의 위쪽에 배치한다.

#### 1. 글로벌 Big Tech의 주요 제품·서비스 변화

아래 기업의 주요 제품 출시, 기능 확장, 정책 변화, 수익화, 글로벌 확장, 파트너십, 규제 이슈는 상단에 배치한다.

- Google
- Apple
- Meta
- Amazon
- Microsoft
- Netflix
- YouTube
- Instagram
- Facebook
- WhatsApp
- Android
- iOS
- Gmail
- Chrome
- AWS
- OpenAI
- Anthropic
- NVIDIA
- Salesforce
- Adobe
- Databricks
- Cloudflare

특히 기존 대규모 유저 기반 서비스에 AI, Agent, Search, Ads, Commerce, Creator, Payment, Productivity 기능이 들어가는 기사는 상단에 배치한다.

#### 2. AI가 실제 서비스와 유저 접점으로 확장되는 기사

AI 기술 자체보다 실제 앱, 서비스, 플랫폼, 업무 흐름에 적용되는 기사를 중요하게 본다.

아래 내용은 상단에 배치한다.

- ChatGPT, Gemini, Claude, Meta AI, Copilot, Grok 등 AI 서비스가 기존 앱이나 업무 도구에 통합되는 기사
- Google Search, Chrome, Android, Gmail, Workspace, YouTube에 AI 기능이 들어가는 기사
- Meta AI가 WhatsApp, Instagram, Facebook, Ads, Business tools, smart glasses에 적용되는 기사
- Amazon Alexa, Rufus, Bedrock, AWS 기반 AI 서비스 확장 기사
- Microsoft Copilot, Agent 365, Windows, Microsoft 365, Power Platform에 AI 기능이 들어가는 기사
- Apple Intelligence, Siri, iOS, App Store, Safari, Messages 등 Apple 생태계 내 AI 변화 기사
- Adobe, Canva, Figma, Notion, Roblox, Atlassian, Zoom 등 기존 대형 앱의 AI workflow 변화 기사
- Kakao, SK Telecom, Samsung, Alibaba, Tencent, ByteDance, Huawei 등 Asia Big Tech의 AI 서비스 적용 기사

#### 3. AI Agent / Agentic AI의 산업 적용 기사

AI Agent 관련 기사는 Global IT Trend Report에서도 매우 중요하게 다룬다.
다만 기술 자체보다 실제 산업과 기업 업무에 적용되는 의미가 큰 기사를 위에 배치한다.

아래 내용은 상단에 배치한다.

- AI Agent가 기업 업무, 고객 응대, 마케팅, 금융, 제조, 통신, 의료, 교육, 커머스, 리테일, 보안에 적용되는 기사
- AI Agent가 결제, 거래, 구매, 예약, 주문, 데이터 분석, 코드 작성, 고객 상담, workflow 자동화를 수행하는 기사
- AI Agent 플랫폼, agentic commerce, AI payment, AI shopping, AI trading 관련 기사
- 기업이 AI Agent를 도입해 비용 절감, 매출 증가, 업무 시간 단축, 자동화 확대 효과를 공개한 기사
- 대기업이 AI Agent를 전사 도입하거나 주요 산업 파트너십으로 확장하는 기사
- AI Agent가 assistant에서 coworker, autonomous worker, digital employee, operating platform으로 진화하는 기사

중소 기업 기사라도 AI Agent가 실제 산업 use case를 명확히 보여주면 반드시 리스트업하고, 산업 변화 의미가 크면 상단에 배치한다.

#### 4. 시장 구조와 경쟁 구도를 보여주는 기사

단순 제품 소식보다 시장 방향성을 설명할 수 있는 기사는 상단에 배치한다.

아래 내용은 중요하게 본다.

- AI Agent Loop, Agentic Web, AI Agent Identity, Agentic Commerce처럼 새로운 시장 개념이 등장하는 기사
- OpenClaw, Codex, Claude Code, Cursor, Gemini, Grok 등 agentic coding 경쟁 구도 기사
- Google, Apple, Meta, Microsoft, Amazon, OpenAI, Anthropic, xAI 간 AI 플랫폼 경쟁 기사
- Big Tech의 AI 인프라 투자, 데이터센터, 반도체, GPU, AI PC, on-device AI 경쟁 기사
- AI search, AI browser, AI shopping, AI ads, AI content creation처럼 기존 인터넷 사용 방식이 바뀌는 기사
- AI 규제, 데이터 보호, 저작권, 청소년 안전, privacy, security 이슈가 시장 구조에 영향을 주는 기사
- AI adoption, enterprise adoption, user growth, revenue, ARR, valuation 등 정량 지표가 포함된 기사

#### 5. Asia Big Tech / 지역별 AI 확산 기사

Global IT Trend Report에서는 Asia Big Tech와 지역별 서비스 확산도 중요하다.

아래 내용은 상단에 배치한다.

- Alibaba, Qwen, Alibaba Cloud, Tencent, ByteDance, Huawei, Baidu, Samsung, Kakao, SK Telecom, Rakuten, Mercari 등 주요 Asia Tech 기업의 AI·서비스 변화
- China, Japan, Korea, India, Southeast Asia 지역에서 AI 서비스가 출시되거나 확장되는 기사
- AI 모델, AI assistant, AI Agent, AI cloud, AI commerce, AI payment, AI device 관련 지역별 경쟁 기사
- India, Japan, Korea, China, Southeast Asia 등 특정 시장 현지화 전략
- Alexa+ Hindi 지원, Kakao AI 서비스, Alibaba Qwen, Tencent AI Agent, Huawei Cloud, SK Telecom AI Agent 등 지역 기반 서비스 변화
- Asia 기업이 글로벌 AI 생태계나 Big Tech 경쟁에 영향을 주는 기사

단순 로컬 PR이라도 AI, Big Tech, platform, commerce, social, cloud, device, regulation과 연결되면 리스트업한다.

#### 6. Social / Creator / Ads / Commerce 변화 기사

Social 및 creator platform 관련 기사는 유저 행동, 광고, 커머스, 콘텐츠 제작 방식 변화가 있으면 상단에 배치한다.

아래 내용은 중요하게 본다.

- Instagram, Facebook, WhatsApp, TikTok, Snapchat, Pinterest, Reddit, LinkedIn, X, Discord, Twitch 등의 AI 기능 추가
- Creator tool, AI video editing, AI ad tool, AI sponsored content, AI recommendation, AI search, AI shopping 관련 기사
- social media 내 광고 상품, measurement, creator monetization, shopping, brand safety 변화
- AI가 콘텐츠 제작, 유통, 추천, 광고 집행, 쇼핑 전환에 적용되는 기사
- 플랫폼 정책 변화, teen safety, privacy, moderation, misinformation, bot, synthetic content 관련 기사
- user engagement, MAU, creator economy, Gen Z/MZ trend와 연결되는 기사

단순 캠페인이나 이벤트성 기사라도 social platform의 광고, creator, commerce, AI 기능 변화와 연결되면 리스트업한다.

#### 7. AI 인프라, 반도체, 클라우드, 디바이스 기사

AI 서비스 변화와 연결되는 인프라 기사는 상단에 배치한다.

아래 내용은 중요하게 본다.

- NVIDIA, AMD, Intel, Qualcomm, Apple Silicon, Google TPU, AWS Trainium 등 AI chip 관련 기사
- AI PC, AI smartphone, smart glasses, wearable AI, edge AI, on-device AI 관련 기사
- AWS, Google Cloud, Microsoft Azure, Alibaba Cloud, Oracle Cloud, Cloudflare 등 AI cloud infrastructure 기사
- 데이터센터, GPU cluster, AI factory, sovereign AI, energy, water, cooling, compute shortage 관련 기사
- AI Agent 실행을 위한 local runtime, edge deployment, secure runtime, sandbox, memory, gateway 관련 기사
- AI infrastructure가 비용, 성능, 기업 도입, 생태계 경쟁에 영향을 주는 기사

단순 하드웨어 기사라도 AI 서비스 확장, AI Agent, on-device AI, cloud AI, model deployment와 연결되면 리스트업한다.

#### 8. 보안, 개인정보, 규제, 저작권 기사

Global IT Trend Report에서는 AI와 플랫폼 확산에 따른 리스크 기사도 중요하게 다룬다.

아래 내용은 상단에 배치한다.

- AI Agent 보안, agent identity, access control, governance, compliance
- prompt injection, RCE, MCP vulnerability, browser agent takeover, extension takeover
- AI 모델의 개인정보, 학습 데이터, 저작권, content provenance, synthetic media 이슈
- App Store, Android, social platform, browser, cloud, AI service 관련 규제
- EU, US, China, Korea, Japan 등 주요 지역의 AI regulation 또는 platform regulation
- 청소년 보호, AI companion safety, chatbot lawsuit, moderation, privacy 관련 기사
- 데이터 유출, 보안 사고, 취약점, 계정 탈취, 인증, payment fraud 관련 기사

보안·규제 기사는 제품 출시가 아니더라도 시장 영향이나 플랫폼 운영 방식 변화와 연결되면 상단에 배치한다.

#### 9. 수치가 있는 기사

정량 지표가 포함된 기사는 중요하게 배치한다.

아래 지표가 있으면 상단 배치 우선순위를 높인다.

- 사용자 수
- MAU / WAU
- paid users
- revenue
- ARR
- enterprise revenue
- adoption rate
- valuation
- funding 규모
- usage growth
- market share
- 비용 절감 수치
- 생산성 향상 수치
- 업무 시간 단축 수치
- 성능 개선 수치
- 처리량, 속도, latency, throughput
- 파트너 수, 고객사 수, 국가 수, rollout 범위

단순 funding 기사라도 기업이 AI 시장 구조에 영향을 줄 가능성이 있거나, Big Tech/AI platform/Agentic AI와 연결되면 리스트업한다.

#### 10. Release Notes / Changelog / GitHub Release

Global IT Trend Report에서도 Release Notes, Changelog, GitHub Release는 누락하면 안 된다.

아래 내용이 있으면 리스트업한다.

- AI 기능 추가
- AI Agent 기능 추가
- 모델 업데이트
- 검색, 브라우저, 광고, 커머스, 크리에이터 도구 기능 변화
- developer workflow 변화
- API, SDK, MCP, plugin, connector, integration 변화
- security, identity, permission, compliance 관련 변화
- 성능 개선, 비용 절감, 배포 안정성 개선
- provider integration, channel integration, memory, runtime, gateway 개선

작은 업데이트라도 Global IT Trend Report 카테고리와 관련성이 있으면 하단에 배치하되 누락하지 않는다.
시장 영향이 크거나 핵심 기업/서비스와 연결되면 상단에 배치한다.

### 하단 배치하되 누락하면 안 되는 기사

아래 유형은 상대적으로 중요도가 낮을 수 있지만, 관련성이 있으면 반드시 리스트업하고 해당 Query 섹션의 아래쪽에 배치한다.

- 중소 SaaS 기업의 AI 기능 출시
- 특정 산업용 AI Agent 또는 AI workflow 발표
- PRNewswire, BusinessWire, GlobeNewswire 기반 제품 출시 기사
- 단순 funding 기사
- 기업 내부 AI 도입 사례
- survey / report / thought leadership 기사
- 특정 vertical use case 기사
- AI Healthcare, AI Education, AI Advertising, AI Shopping, AI Browser, AI Security 관련 기사
- Asia 지역 로컬 기업의 AI 서비스 출시
- social platform의 작은 기능 변화
- 공식 블로그의 작은 product update
- release note / changelog의 작은 기능 변화

주의:

- 하단 배치 대상이라는 이유로 기사를 제외하지 않음
- 중요도가 낮아 보여도 Global IT Trend Report 카테고리와 관련성이 있으면 반드시 기사 리스트에 포함

### 중복 기사 처리 기준

같은 내용을 여러 출처가 보도한 경우에도 완전히 삭제하지 않는다.

- 공식 발표가 있으면 공식 출처를 대표 URL로 둠
- TechCrunch, Reuters, CNBC, Bloomberg, 9to5Google, 9to5Mac, Social Media Today 등 해설 가치가 있는 기사는 보조 URL로 함께 둠
- 같은 내용을 반복한 기사라면 `중복` 또는 `보조 출처`로 표시
- 중복 기사라도 나중에 검토자가 판단할 수 있도록 기록은 남김
- 완전히 동일하고 정보 가치가 없는 경우에만 대표 URL 아래에 묶음

### 절대 누락하면 안 되는 주제

아래 주제와 직접 관련된 기사는 중요도와 관계없이 반드시 확인하고, 관련성이 있으면 리스트업한다.

- AI
- Generative AI
- AI Agent
- Agentic AI
- ChatGPT
- OpenAI
- Codex
- Claude
- Claude Code
- Gemini
- Google AI Mode
- DeepMind
- Meta AI
- Copilot
- Grok
- OpenClaw
- MCP
- AI coding
- AI browser
- AI search
- AI commerce
- AI payment
- AI shopping
- AI advertising
- AI security
- AI governance
- AI model release
- AI assistant
- AI companion
- AI character
- AI healthcare
- AI education
- enterprise AI adoption
- Big Tech AI partnership
- AI cloud
- AI chip
- AI PC
- on-device AI
- social platform AI
- creator AI tools
- AI regulation
- AI privacy
- AI copyright
- platform policy change
- app ecosystem change
- release notes
- changelog
- GitHub release

### 제외 기준

아래에 해당하는 경우에만 제외한다.

- IT/AI/Big Tech/Social/Market Trend와 직접 관련이 없는 기사
- AI 관련성이 전혀 없는 일반 기업 홍보 기사
- 단순 인사, 채용, 행사, 프로모션 기사
- 제품·시장·기술 변화가 없는 단순 이벤트 안내
- Naver/LINE 단독 기사
- 동일 내용이 이미 대표 기사로 정리되어 있고, 보조 출처로도 가치가 없는 완전 중복 기사

주의:

- `중요도가 낮아 보인다`는 제외 사유가 아님
- 관련성이 있으면 반드시 리스트업하고, 중요도에 따라 아래쪽에 배치

### 한 줄 원칙

Global IT Trend Report 아카이빙에서는 관련 기사를 절대 누락하지 않는다.
중요도는 제외 기준이 아니라, 해당 Query 섹션 안에서 어떤 기사를 위에 배치할지 판단하는 정렬 기준이다.

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
- 내부 판단 기준으로만 활용 예시:
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
- 대분류 카테고리별 구역 생성
- 각 대분류 아래 Query List 또는 세부 서비스명 배치
- 각 Query List 항목 아래 해당 기간 내 확인된 기사 입력
- 최종 Sheet는 Include 기사 중심으로 입력
- 제외 기사나 중복 제외 기사는 별도 컬럼으로 관리하지 않음
- 기사 원문 제목은 별도 컬럼으로 입력하지 않고, 최종 리포트용 `Korean Title` 중심으로 정리
- URL은 실제 접속 가능하고 본문 확인 가능한 링크만 입력
- 기사 없음 또는 해당 기간 업데이트 없음은 `n/a`로 입력
- 기존 `O` 표시 방식은 사용하지 않고 `Check Box` 컬럼 사용
- 중복 제거, Cluster 처리, 제외 판단, AI 관련성 판단은 업무 프로세스 기준으로 수행하되 Sheet 컬럼으로 입력하지 않음

## Sheet 입력 권장 컬럼

### Sheet 입력 기본 원칙

기사 리스트업 Sheet는 일반적인 데이터베이스형 테이블이 아니라, 카테고리와 Query List를 기준으로 기사 제목과 URL을 입력하는 구조로 관리한다.

- 대분류 카테고리별로 구역을 나눔
- 대분류 카테고리 예시: `AI Agent`, `AI/GPT`, `Global Big Tech`, `Asia Big Tech`, `Social`, `Theme`
- 각 대분류 아래에 Query List 또는 세부 서비스명을 배치
- 각 Query List 항목 아래에 해당 기간 내 확인된 기사 입력
- 기사 입력 시 원문 제목은 입력하지 않고, 최종 리포트용 국문 제목만 입력
- 기사 제목은 반드시 기존 제목 작성 규칙에 맞춰 작성
- URL은 실제 접속 가능하고 본문 확인 가능한 링크만 입력
- 기사 없음 또는 해당 기간 업데이트 없음은 `n/a`로 입력
- 기존 `O` 표시 방식은 사용하지 않고, 실제 Sheet에서 클릭 가능한 체크박스 컬럼 사용
- 체크박스는 사람이 최종 선정 여부나 검토 완료 여부를 직접 체크할 수 있도록 구성
- 체크박스 컬럼은 `Status`, `Note`, `AI Relevance`, `Report Relevance` 같은 판단용 컬럼으로 확장하지 않음

### Sheet 입력 시 사용하지 않는 컬럼

아래 컬럼들은 실제 기사 리스트업 Sheet에서 사용하지 않는다.

- Original Title
- Key Update
- AI Relevance
- Report Relevance
- Cluster ID
- Duplicate Check Keyword
- Status
- Note

### Sheet 입력 권장 구조

Sheet 입력 구조는 아래 형태를 따른다.

| 대분류 | Query / Service | Korean Title | Check Box | URL |
| --- | --- | --- | --- | --- |
| AI Agent | AI Agent | [Agentshub.AI] 완전한 노코드 기반 AI Agent Platform 공개하며 기업용 AI 워크포스 구축 지원 (2026.4.6) | ☐ | https://finance.yahoo.com/sectors/technology/articles/agentshub-ai-launches-complete-no-130800495.html |
|  |  | [Razorpay] Codex 및 ChatGPT 연동 통해 자연어 명령만으로 결제 설정과 데이터 분석 수행하는 Agentic 결제 인프라 확장 (2026.4.7) | ☐ | https://razorpay.com/blog/ai-app-monetisation-razorpay-codex/ |
|  |  | [Meta] 내부 데이터 파이프라인에 50+ AI Agent 투입해 4.1K+ 파일 분석 및 59개 컨텍스트 파일 기반 지식 구조화 사례 공개 (2026.4.6) | ☐ | https://engineering.fb.com/2026/04/06/developer-tools/how-meta-used-ai-to-map-tribal-knowledge-in-large-scale-data-pipelines/ |
|  | OpenClaw (Moltbot, Clawdbot) | [OpenClaw] 38M 월간 방문자와 3.2M MAU 기록하며 글로벌 AI Agent 플랫폼 성장 가속 (2026.4.7) | ☐ | https://www.trendingtopics.eu/openclaw-numbers/ |
|  | OpenClaw (Moltbot, Clawdbot) | [OpenClaw] 2026.4.7 버전 업데이트, Gemma 4 지원 추가와 memory-wiki 복원 적용 (2026.4.7) | ☐ | https://github.com/openclaw/openclaw/releases/tag/v2026.4.7 |
|  | Paperclip | n/a |  |  |
|  | BabyAGI | n/a |  |  |
|  | Microsoft AutoGen | n/a |  |  |
| AI/GPT | AI | [Zero Shot] Ex-OpenAI 창업자들, $100M 목표 AI 투자 펀드 조성하며 초기 투자 집행 (2026.4.6) | ☐ | https://techcrunch.com/2026/04/06/openai-alums-have-been-quietly-investing-from-a-new-potentially-100m-fund/ |
|  | OpenAI | [OpenAI] "Safety Fellowship" 공개하며 AI 안전과 정렬 연구 인재 육성 프로그램 운영 (2026.4.6) | ☐ | https://openai.com/index/introducing-openai-safety-fellowship/ |
|  | Google AI | [Google] 오프라인 Dictation 앱 "AI Edge Eloquent" 공개하며 음성 입력 생산성 기능 강화 (2026.4.6) | ☐ | https://techcrunch.com/2026/04/06/google-quietly-releases-an-offline-first-ai-dictation-app-on-ios/ |
|  | Gemini | [Google] Gemini overlay와 Gemini Live UI 통합 재설계 통해 AOS 상호작용 방식과 Multi-modal 접근성 개선 (2026.4.7) | ☐ | https://9to5google.com/2026/04/07/gemini-live-redesign-android/ |
|  | Nova AI | [Amazon] Nova 2 Sonic, 실시간 대화형 Podcast 생성 가능한 음성 기반 AI 모델 활용 아키텍처 공개 (2026.4.7) | ☐ | https://aws.amazon.com/ko/blogs/machine-learning/building-real-time-conversational-podcasts-with-amazon-nova-2-sonic/ |

### 체크박스 컬럼 적용 기준

md 파일에는 체크박스 컬럼을 `Check Box`로 표기하되, 실제 Google Sheet 또는 Excel 템플릿을 생성할 때는 해당 열을 반드시 클릭 가능한 체크박스 형식으로 설정한다.

- Google Sheets 기준: `Insert > Checkbox` 기능이 적용된 열로 구성
- Excel 기준: 실제 체크박스 삽입이 어렵다면 `TRUE/FALSE` 또는 빈 체크박스 기호 `☐` 사용 가능
- 단순히 `O` 문자로 표시하지 않음
- 사람이 직접 클릭하거나 선택할 수 있는 체크용 컬럼으로 구성
- 체크박스는 최종 포함 여부 또는 검토 완료 여부를 사람이 확인하기 위한 용도
- 자동화 agent가 임의로 체크하지 않도록 관리

### Sheet 입력 예시 작성 방식

- 원문 제목 컬럼은 만들지 않음
- 핵심 요약 컬럼은 만들지 않음
- AI Relevance, Report Relevance, Status, Note 등 판단용 컬럼은 만들지 않음
- 기존 `O` 표시 컬럼은 사용하지 않고 `Check Box` 컬럼 사용
- 국문 제목은 `[회사명] 핵심 내용 (yyyy.m.d)` 형식 적용
- 산업 전반 또는 특정 기업 중심이 아닌 경우 `[Market]` 사용
- 날짜는 `2026.4.7`처럼 0 padding 없이 작성
- 신규 공개 서비스나 기능명에만 큰따옴표 사용
- URL이 여러 개인 경우 한 셀에 줄바꿈으로 입력 가능
- 해당 Query 항목에서 기사 없음 또는 업데이트 없음은 `n/a`로 입력

## Check Box 운영 기준

- Check Box는 사람이 최종 리포트 반영 후보를 선택하기 위한 용도다.
- 자동화 agent는 신규 입력 기사의 Check Box를 기본 미체크 상태로 생성한다.
- 자동화 agent가 기사 중요도를 판단해 임의로 체크하지 않는다.
- 작업자는 기사 중요도, 중복 여부, 리포트 활용 가능성을 검토한 뒤 직접 체크한다.
- Google Sheets에서는 실제 클릭 가능한 체크박스 형식으로 설정한다.
- Google Sheets 기준으로는 `Insert > Checkbox` 또는 데이터 유효성 체크박스를 사용한다.
- Excel에서 실제 체크박스 구현이 어려운 경우 `TRUE/FALSE` 또는 빈 체크박스 기호 `☐`를 임시로 사용할 수 있다.
- 기존 `O` 표시는 사용하지 않는다.

## n/a 입력 기준

- Query / Service 항목을 확인했지만 해당 기간 내 입력할 기사가 없으면 Korean Title 칸에 `n/a`를 입력한다.
- `n/a`가 입력된 행은 Check Box와 URL을 비워둔다.
- 검색 자체를 수행하지 않은 항목에는 `n/a`를 입력하지 않는다.
- `n/a`는 “확인 완료 후 해당 기간 업데이트 없음”을 의미한다.

## URL 입력 기준

- URL은 실제 접속 가능하고 본문 확인 가능한 링크만 입력한다.
- Official Source와 Tech Media가 모두 중요한 경우 URL 셀에 공식 링크를 첫 줄, 보완 기사 링크를 두 번째 줄에 입력할 수 있다.
- URL이 여러 개인 경우 한 셀 안에서 줄바꿈으로 입력한다.
- 단순 재보도 링크는 여러 개 넣지 않는다.
- Paywall 링크는 최종 URL로 사용하지 않고, 접근 가능한 대체 링크를 입력한다.
- 공식 발표와 외부 보완 기사가 같은 이슈를 다루지만 각각 정보 가치가 있으면 함께 입력할 수 있다.

## 중복 기사 및 보조 출처 처리 방식

- 중복 기사나 보조 출처는 별도 `Status`, `Note`, `Cluster ID` 컬럼으로 관리하지 않는다.
- 같은 이슈를 다룬 기사 중 공식 발표가 있으면 공식 발표를 대표 URL로 우선 사용한다.
- Tech Media 기사에 시장 반응, 수치, 경쟁사 맥락 등 추가 정보가 있으면 같은 URL 셀에 줄바꿈으로 함께 입력한다.
- 단순 재보도나 정보 가치가 낮은 중복 기사는 Sheet에 별도로 입력하지 않는다.
- 완전히 동일한 내용의 반복 보도는 대표 기사 1개만 유지한다.
- 후속 기사로 볼 수 있는 경우에는 별도 기사로 입력할 수 있다.
- 후속 기사 판단 기준은 신규 수치, 신규 지역 출시, 신규 기능 추가, 신규 파트너십, 신규 규제 변화가 있는지 여부다.
- Paywall 기사는 최종 URL로 사용하지 않고, 본문 접근 가능한 대체 기사 또는 공식 발표로 대체한다.

## 수집과 최종 선택의 구분

- 기사 리스트업 Sheet의 목적은 처음부터 최종 리포트 기사만 남기는 것이 아니라, Query별 관련 기사를 수집한 뒤 검토자가 빠르게 판단할 수 있도록 정리하는 것이다.
- 1차 수집 단계에서는 Global IT / AI / Big Tech / Asia Tech / Social / Market Trend와 관련된 기사를 넓게 리스트업한다.
- 관련성이 있는 기사는 중요도가 낮아 보여도 누락하지 않고 Query 섹션 안에 입력한다.
- 중요한 기사는 해당 Query 섹션의 위쪽에 배치한다.
- 중요도가 낮거나 단순 PR성에 가까운 기사는 아래쪽에 배치한다.
- 최종 리포트 반영 여부는 사람이 Check Box로 선택한다.
- 단, 명백한 비대상 기사, Naver/LINE/LY Corporation 단독 기사, 완전 중복 기사, 본문 확인 불가 기사, AI/IT/플랫폼 관련성이 거의 없는 기사는 입력하지 않는다.

## AI Agent 구역 처리 방식

- `AI Agent`는 Weekly AI Trend Report에서 별도 상단 구역으로 관리할 수 있다.
- 리포트 카테고리 기준으로는 `AI/GPT`에 포함된다.
- Sheet에서는 AI Agent 관련 Query가 많기 때문에 `AI Agent`를 별도 대분류처럼 배치할 수 있다.
- AI Agent 구역에는 OpenClaw, AutoGPT, AgentGPT, CrewAI, LangGraph, Claude Code, agentic workflow, enterprise AI agent, agentic commerce, AI payment, AI security 등 관련 기사를 입력한다.

## 대분류별 기사 수 표기 방식

대분류 행에는 필요 시 선정 기사 수와 전체 후보 기사 수를 표시한다.

예시:

- `AI Agent 5 14`
- `AI/GPT 12 37`

의미:

- 앞 숫자: 사람이 Check Box로 선택한 주요 후보 기사 수
- 뒤 숫자: 해당 대분류에서 수집된 전체 기사 수
- 자동화 agent가 숫자를 정확히 계산할 수 있는 경우 자동 입력한다.
- 자동 계산이 어렵다면 숫자 칸은 비워두고 작업자가 최종 검토 후 수동 업데이트한다.

## 자동화 입력값

자동화 agent가 작업을 수행할 때 필요한 입력값은 아래와 같다.

- 검색 기간: `yyyy.mm.dd~yyyy.mm.dd`
- 입력 예시: `2026.6.18~2026.6.24`
- 작업 주차명: 예: `6월 4주`
- 작업 대상 Sheet 또는 파일
- 적용 Query List
- Google Query 전 우선 확인 링크 목록
- 제외 대상: Naver / LINE / LY Corporation 단독 기사
- 기존 주차 Sheet 또는 과거 기사 목록
- 기존 Sheet 템플릿

## 자동화 출력값

자동화 agent는 아래 구조로 결과를 생성한다.

- 대분류
- Query / Service
- Korean Title
- Check Box
- URL

출력 기준:

- Check Box는 기본 미체크 상태로 생성한다.
- URL은 실제 접속 가능하고 본문 확인 가능한 링크만 입력한다.
- 원문 제목은 별도 컬럼으로 출력하지 않는다.
- Status, Note, AI Relevance, Report Relevance 등 판단용 컬럼은 출력하지 않는다.
- 기사 없음이 확인된 Query / Service 항목은 `n/a`로 입력한다.

## 중복 기사 처리 방식

- 같은 기업, 같은 기능, 같은 발표 내용은 중복 처리하되 Sheet 기록은 남김
- 동일 이벤트 기사는 Cluster 단위로 관리
- 각 Cluster에서 가장 적합한 Source 1개를 대표 기사로 유지하고 나머지는 `중복` 또는 `보조 출처`로 기록
- Official Source와 외부 기사 중복 시 Official Source 우선
- Paywall 기사는 최종 URL로 사용하지 않고 접근 가능한 기사로 대체
- 외부 기사 우선순위 예시:
  - TechCrunch
  - The Verge
  - 9to5Mac
  - 9to5Google
  - Social Media Today
- Google Query 기사는 날짜 필터 해제 후 타이틀 또는 핵심 키워드로 과거 사용 여부 확인
- 과거 사용 기사 또는 동일 이슈 단순 재사용 기사는 신규 정보가 없으면 대표 기사 아래 중복 기록
- 실질적 업데이트가 있으면 신규 기사로 유지:
  - 후속 발표
  - 신규 수치
  - 신규 지역 출시
  - 신규 기능 추가
- 중복 기사 정리 시 내부 판단 기준으로 대표 기사와 보조 출처를 구분

## 최종 Title 작성 방식

최종 선별된 기사에는 `Korean Title`을 반드시 작성한다.

### Title 기본 형식

- `[회사명] 핵심 내용 (yyyy.m.d)`

### Title 작성 규칙

- 회사명은 English로 작성
- Title 본문은 Korean으로 작성
- 날짜는 기사 발행일 기준으로 작성
- 날짜는 0 padding 없이 작성
  - 예시: `2026.4.7`
- 제목 안 날짜에는 `/`를 사용하지 않음
- URL은 제목 뒤에 붙이지 않고 별도 URL 칸에 입력
- Title은 항상 명사형 종결
- 문장 끝 금지 표현:
  - `함`
  - `있음`
  - `없음`
  - `됨`
- 기업명, 서비스명, 기능명은 English로 작성
- 신규 공개 서비스나 기능명에만 필요한 경우 큰따옴표 사용
- 기존 서비스명, 기존 기능명에는 불필요한 큰따옴표 사용 금지
- 제목은 핵심 변화 중심으로 간결하게 작성
- 쉼표는 최대 1개만 사용

### `[Market]` 사용 기준

- 여러 기업을 함께 다루는 기사
- market-wide trends 기사
- country-level trends 기사
- industry changes 기사
- company strategy comparisons 기사
- 특정 기업보다 시장 구조 변화가 더 중요한 기사
- 특정 국가의 유저 행동, 규제, 산업 변화, 소비 트렌드 기사

### Title 예시

- `[OpenAI] "Safety Fellowship" 공개하며 AI 안전과 정렬 연구 인재 육성 프로그램 운영 (2026.4.6)`
- `[Google] Gemini overlay와 Gemini Live UI 통합 재설계 통해 AOS 상호작용 방식과 Multi-modal 접근성 개선 (2026.4.7)`
- `[Market] AI data center, 투자자 요구로 Big Tech 대상 전력과 수자원 사용량 공개 압박 확대 (2026.4.8)`

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

- [ ] Global IT / AI / Big Tech / Asia Tech / Social / Market Trend 관련 기사를 중요도와 관계없이 모두 리스트업했는지 확인
- [ ] 각 Query 섹션 안에서 `시장 영향이 큰 기사 → 기업/서비스 변화 기사 → 일반 관련 기사 → 중복/보조 출처` 순서로 정렬했는지 확인
- [ ] 공식 Newsroom, Blog, Release Notes, Changelog, GitHub Release 중 제품·서비스·기능·시장 변화가 있는 항목을 누락하지 않았는지 확인
- [ ] 중복 기사도 완전히 삭제하지 않고 대표 기사 아래 보조 출처 또는 중복으로 기록했는지 확인
- [ ] 절대 누락하면 안 되는 Global IT / AI / Big Tech / Social / Market Trend 주제를 확인했는지 점검
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
- [ ] 각 Cluster에서 대표 Source를 구분하고 보조 출처 또는 중복 기사 기록
- [ ] Paywall 기사를 접근 가능한 기사로 대체
- [ ] URL이 영어 원문 또는 영어 공식 링크 기준으로 정리
- [ ] 한국어/일본어 링크가 예외 기업 또는 현지어 공식 링크 기준에 부합
- [ ] 단순 PR성 기사나 비대상 기사 제외
- [ ] URL 정상 접속 확인
- [ ] 기사 날짜와 출처 정확성 확인
- [ ] 최종 Korean Title 작성
- [ ] Sheet 입력용 Korean Title이 `[회사명] 핵심 내용 (yyyy.m.d)` 형식에 부합
- [ ] 기존 `O` 표시 방식 대신 클릭 가능한 `Check Box` 컬럼을 사용했는지 확인
- [ ] 기사 없음 또는 해당 기간 업데이트 없음이 `n/a`로 입력되었는지 확인
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

## 수정 요약

- 자동화 agent 실행 기준에 맞춰 전체 작업 순서를 공식 링크 우선 확인, 보완 검색, Sheet 입력, 사람의 Check Box 검토 순서로 정리
- Sheet 입력 구조를 `대분류`, `Query / Service`, `Korean Title`, `Check Box`, `URL` 중심으로 통일
- `Original Title`, `Status`, `Note`, `AI Relevance`, `Report Relevance`, `Cluster ID`, `Duplicate Check Keyword`, `Key Update`를 Sheet 컬럼으로 만들지 않도록 정리
- Korean Title 날짜 형식을 `[회사명] 핵심 내용 (yyyy.m.d)`로 통일하고 URL은 별도 URL 칸에 입력하도록 수정
- Check Box, `n/a`, URL 복수 입력, 중복 기사 및 보조 출처 처리, 자동화 입력값/출력값 기준을 추가
- Naver / LINE / LY Corporation 단독 기사 제외 기준과 공식 링크 우선 확인 후 Google Query 실행 원칙은 유지
