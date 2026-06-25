# Weekly Archiving Process

## 목차

- [업무 목적](#업무-목적)
- [기본 작업 단위](#기본-작업-단위)
- [카테고리 구분](#카테고리-구분)
- [카테고리별 기준](#카테고리별-기준)
- [카테고리별 우선 포함 기준](#카테고리별-우선-포함-기준)
- [Global IT Trend Report 기사 범위](#global-it-trend-report-기사-범위)
- [AI 중심성 판단 기준](#ai-중심성-판단-기준)
- [Naver / LINE 아카이빙 제외 기준](#naver--line-아카이빙-제외-기준)
- [작업 전 준비사항](#작업-전-준비사항)
- [날짜 입력 방식](#날짜-입력-방식)
- [전체 작업 순서](#전체-작업-순서)
- [Google Query 전 우선 확인 소스](#google-query-전-우선-확인-소스)
- [Google Query 전 우선 확인 링크](#google-query-전-우선-확인-링크)
- [Official Source Map](#official-source-map)
- [Query List 적용 방식](#query-list-적용-방식)
- [Official Source 확인 방식](#official-source-확인-방식)
- [Google Query 및 외부 기사 검색 방식](#google-query-및-외부-기사-검색-방식)
- [Source 우선순위 세부 기준](#source-우선순위-세부-기준)
- [Google Query 기사 중복 확인 방식](#google-query-기사-중복-확인-방식)
- [기사 선별 기준](#기사-선별-기준)
- [기사 포함 여부 판단 점수표](#기사-포함-여부-판단-점수표)
- [Global IT Trend Report 기사 중요도 및 정렬 기준](#global-it-trend-report-기사-중요도-및-정렬-기준)
- [기사 제외 기준](#기사-제외-기준)
- [기사 수 조정 기준](#기사-수-조정-기준)
- [국가 중요도 우선순위](#국가-중요도-우선순위)
- [국가 우선순위 적용 방식](#국가-우선순위-적용-방식)
- [Cluster 처리 방식](#cluster-처리-방식)
- [Paywall 기사 처리 방식](#paywall-기사-처리-방식)
- [URL 언어 기준](#url-언어-기준)
- [Sheet 정리 방식](#sheet-정리-방식)
- [Sheet 입력 권장 컬럼](#sheet-입력-권장-컬럼)
- [중복 기사 처리 방식](#중복-기사-처리-방식)
- [후속 기사와 중복 기사 구분 기준](#후속-기사와-중복-기사-구분-기준)
- [최종 Title 작성 방식](#최종-title-작성-방식)
- [Korean Title 품질 체크](#korean-title-품질-체크)
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

## 카테고리별 우선 포함 기준

### AI/GPT

- AI Agent, Agentic Platform, LLM, 생성형 AI, AI 인프라, AI Search 관련 기사 우선
- OpenAI, Anthropic, Google, Microsoft, Meta, Amazon, Apple 등 주요 AI 기업의 제품 변화 우선
- AI 기능이 실제 유저 경험, 업무 자동화, 개발자 경험, 광고, 검색, 커머스, 콘텐츠 제작에 영향을 주는 기사 우선
- 단순 투자, 인터뷰, 행사성 기사보다 제품 출시, 기능 업데이트, 규제, 시장 구조 변화 기사 우선
- AI 관련성이 약한 일반 IT 기사는 AI/GPT 카테고리에서 제외

### Global Big Tech

- AI 기능 출시, 광고 수익화, OS, 검색, 브라우저, 메신저, 커머스, 콘텐츠 전략 변화 우선
- Meta, Google, Microsoft, Amazon, Apple 관련 기사는 플랫폼 전략 변화가 있으면 우선 검토
- 단순 앱 UI 변경, 이벤트, 할인, 일반 콘텐츠 편성 기사는 후순위
- 기존 기능의 글로벌 확장, 신규 광고 상품, 구독 모델, 크리에이터 생태계 변화는 포함 가능
- 여러 서비스에 영향을 주는 정책, 개인정보, 보안, 규제 변화는 우선 포함

### Asia Big Tech

- Kakao, Coupang, Toss, Tencent, ByteDance, Alibaba, Rakuten, Mercari, DeNA 등 주요 기업의 AI, 커머스, 메신저, 광고, 콘텐츠 변화 우선
- Japan, Korea, China, Taiwan, Thailand, Singapore, India 등 주요 지역의 플랫폼 변화 우선
- 일본 서비스는 신규 기능, 유저 성장, 커뮤니티, creator economy, 앱 서비스 변화 중심으로 검토
- 단순 캠페인, 오프라인 이벤트, 일반 브랜드 제휴성 기사는 후순위
- Naver, LINE, LY Corporation 단독 기사는 기존 제외 기준에 따라 제외

### Social

- 메시징, 커뮤니티, 크리에이터 수익화, 광고, 안전 기능, 유저 성장 변화 우선
- TikTok, Douyin, Snapchat, Telegram, Pinterest, X, BlueSky, Twitch, BeReal, Discord 관련 주요 기능 변화 우선
- 그룹 기능, 채널, 커뮤니티, DM, 광고 상품, 구독 모델, moderation, safety 관련 기사 포함 가능
- 단순 디자인 변경, 챌린지, 일회성 캠페인, 밈성 콘텐츠는 후순위
- Social 플랫폼의 유저 행동 변화나 검색·커머스·콘텐츠 소비 방식 변화는 Theme로도 검토 가능

### Theme

- 특정 기업 하나보다 시장 구조나 유저 행동 변화가 중요한 기사 우선
- Gen Z/MZ, 검색 행동 변화, social commerce, creator economy, AI adoption, 규제 변화는 우선 검토
- 여러 기업을 비교하거나 특정 국가·세대·산업 전반 변화를 다루는 기사 포함 가능
- 단순 앱 추천 리스트, 다운로드 유도형 콘텐츠, 개인 의견 중심 칼럼은 제외
- Naver/LINE이 일부 언급되더라도 기사 전체가 시장 변화 중심이면 `[Market]` 기준으로 검토 가능

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

## AI 중심성 판단 기준

- AI/GPT 카테고리는 AI가 기사 핵심인 경우만 포함
- 단순히 AI라는 단어가 언급된 기사만으로는 포함하지 않음
- AI 기능, AI Agent, LLM, 생성형 AI, AI 인프라, AI 규제, AI 보안, AI 투자 등과 직접 연결된 기사 우선 검토
- AI가 기존 서비스의 핵심 UX, 수익화 구조, 업무 방식, 플랫폼 전략을 바꾸는 경우 포함 가능
- AI가 보조적으로만 언급되거나 홍보 문구 수준에 그치는 경우 제외 검토

### 포함 가능

- AI 모델, LLM, AI Agent, 생성형 AI 기능 출시
- AI가 기존 서비스의 핵심 UX를 바꾸는 업데이트
- AI 인프라, AI 칩, AI 데이터센터, AI 비용 구조 변화
- AI 규제, 저작권, 보안, 개인정보 이슈
- 기업용 AI 도입, Agentic workflow, 업무 자동화 관련 기사
- AI 기능이 광고, 검색, 커머스, 콘텐츠 제작 방식에 직접 영향을 주는 기사
- AI Search, AI Browser, AI Assistant, AI Plugin 등 유저 접점 변화가 큰 기사
- AI Startup 중 제품, 시장, 투자, 기술 변화가 명확한 기사

### 제외 가능

- AI 기업의 단순 투자 유치 기사이나 서비스 변화가 약한 경우
- AI가 홍보 문구 수준으로만 언급된 기사
- 게임, 엔터테인먼트, 브랜드 캠페인 중심이고 AI는 보조 요소인 기사
- CEO 인터뷰, 인사 이동, 행사 참석 등 AI 제품 변화가 없는 기사
- 기존 기능을 AI라고 재포장한 단순 PR성 기사
- AI와 직접 관련 없는 일반 플랫폼 업데이트 기사
- 단순 의견성 칼럼이나 예측 기사 중 구체적 변화가 부족한 기사

### AI/GPT 카테고리 적용 원칙

- AI/GPT 카테고리는 다른 카테고리보다 포함 기준을 더 엄격하게 적용
- AI 관련성이 약하면 Global IT Trend Report의 다른 카테고리로 이동 검토
- AI가 핵심이 아닌데 Big Tech, Social, Asia Big Tech 측면에서 의미가 있으면 해당 카테고리로 재분류
- AI/GPT에 넣기 애매한 경우 비고란에 `AI 관련성 약함`, `카테고리 재검토`, `Global IT 후보` 등으로 표시

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

## Official Source Map

아래 표는 Google Query 전 우선 확인할 공식 채널과 보완 소스를 정리한 기준이다.
공식 채널이 존재하는 기업, 서비스, 제품은 Google Search 또는 Google News 검색 전 아래 소스를 먼저 확인한다.

| 대상 | 1차 확인 소스 | 2차 확인 소스 | Google Query 필요 여부 |
| --- | --- | --- | --- |
| OpenAI | OpenAI Blog / News | OpenAI Docs / Changelog | 필요 |
| ChatGPT / Codex / Sora | OpenAI Blog | OpenAI Help Center / Docs | 필요 |
| Anthropic / Claude | Anthropic News | Claude Docs | 필요 |
| Google AI / Gemini | Google Blog / DeepMind Blog | Google Workspace Blog / Android Developers Blog | 필요 |
| Microsoft / Copilot | Microsoft Blog | Microsoft 365 Blog / Azure Blog | 필요 |
| Amazon AI / Bedrock / Nova | AWS Blog / Amazon News | Bedrock Docs / AWS What's New | 필요 |
| Meta AI | Meta Newsroom | Meta AI Blog / Engineering Blog | 필요 |
| Facebook / Instagram / WhatsApp | Meta Newsroom | 각 서비스 Help Center / Business Blog | 필요 |
| Apple / iOS / Safari | Apple Newsroom | Apple Developer Release Notes | 필요 |
| Netflix | Netflix Newsroom | Netflix Tech Blog | 필요 |
| TikTok / Douyin | TikTok Newsroom | TikTok for Business / ByteDance Blog | 필요 |
| Snapchat | Snap Newsroom | Snap for Business / Developer Docs | 필요 |
| Telegram | Telegram Blog | Telegram FAQ / GitHub | 필요 |
| Discord | Discord Blog | Discord Safety / Developer Docs | 필요 |
| Pinterest | Pinterest Newsroom | Pinterest Business Blog | 필요 |
| X / XChat | X Blog | Help Center / 공식 계정 | 필요 |
| Kakao | Kakao Newsroom | Kakao Developers | 필요 |
| Coupang | Coupang Newsroom | Coupang 공식 보도자료 | 필요 |
| Toss | Toss Newsroom | Toss Tech Blog | 필요 |
| Tencent / WeChat | Tencent News | WeChat Blog / 현지 Tech Media | 필요 |
| ByteDance | ByteDance 공식 채널 | TikTok Newsroom / 현지 Tech Media | 필요 |
| Alibaba | Alibaba News | Alibaba Cloud Blog | 필요 |
| Rakuten | Rakuten Newsroom | Rakuten Tech Blog / 일본어 공식 발표 | 필요 |
| Mercari | Mercari Newsroom | Mercari Engineering Blog | 필요 |
| DeNA | DeNA News | DeNA Tech Blog | 필요 |
| Note | note 공식 발표 | note pro / 일본어 공식 발표 | 필요 |

### 적용 방식

- Official Source에서 확인한 업데이트는 신뢰도 높게 우선 반영
- Official Source와 외부 기사 내용이 겹치면 Official Source 기준으로 내용 확인
- 외부 기사는 시장 반응, 보완 설명, 투자 규모, 파트너십 맥락 확인용으로 활용
- Official Source가 없거나 업데이트가 늦은 서비스는 Google Query와 신뢰도 높은 외부 기사로 보완
- `(Google Query)` 표시 항목은 기존 규칙대로 Official Source 확인 없이 Google Query만 진행

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

## Source 우선순위 세부 기준

### 공통 우선순위

1. Official Blog / Newsroom / Docs / Changelog
2. 원출처에 가까운 전문 매체
3. 신뢰도 높은 Tech Media
4. 현지 전문 매체
5. 일반 경제지 또는 종합지
6. 단순 재보도 매체

### Global Big Tech / AI

- TechCrunch
- The Verge
- 9to5Google
- 9to5Mac
- VentureBeat
- SiliconANGLE
- ZDNET
- CNBC
- Bloomberg, Reuters, NYTimes, The Information은 Paywall 여부 확인 후 접근 가능한 대체 기사 검토

### Social / Platform

- Social Media Today
- TechCrunch
- The Verge
- 9to5Google
- 9to5Mac
- 공식 Help Center
- 공식 Product Blog
- 공식 Business Blog

### Asia Big Tech

- 기업 공식 Newsroom
- 기업 공식 Blog
- The Bridge
- CNET Japan
- ASCII Startup
- 현지 공식 보도자료
- 현지 Tech Media
- 영어 기사 존재 시 영어 링크 우선

### Theme

- 신뢰도 높은 Tech Media
- 시장조사기관 발표
- 정부, 규제기관, 공식 통계
- 주요 경제지 또는 산업 전문 매체
- 단순 블로그, 광고성 콘텐츠, 출처 불명확 콘텐츠는 제외

### Source 선택 원칙

- 최종 URL은 실제 접속 가능하고 본문 확인 가능한 링크만 사용
- Paywall 기사는 최종 URL로 사용하지 않음
- 동일 이슈에서 Official Source와 외부 기사가 모두 있으면 Official Source 우선
- 단, 외부 기사에 신규 수치, 시장 반응, 경쟁사 맥락이 추가되어 있으면 보완 기사로 검토 가능
- 단순 재보도 기사보다 원출처에 가까운 기사 우선
- 영어 URL이 있으면 영어 URL 우선 사용
- 한국어/일본어 기업 공식 발표만 존재하는 경우 현지어 공식 링크 사용 가능

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

## 기사 포함 여부 판단 점수표

각 기사는 아래 기준으로 포함 여부를 판단한다.

| 기준 | 2점 | 1점 | 0점 |
| --- | --- | --- | --- |
| 중요도 | Big Tech, 주요 AI 기업, 대형 플랫폼 변화 | 중견 서비스 또는 특정 지역 중심 변화 | 영향도 낮은 단순 업데이트 |
| 신규성 | 신규 출시, 신규 기능, 신규 지역, 신규 수치 | 기존 이슈의 후속 업데이트 | 과거 이슈 반복 |
| AI/IT 관련성 | AI, 플랫폼, 광고, 커머스, social media 변화와 직접 연결 | 간접 연결 | 연결성 약함 |
| 리포트 활용성 | Weekly/Global Report에서 바로 활용 가능 | 보류 후 검토 가능 | 활용 어려움 |
| 출처 신뢰도 | Official Source 또는 신뢰도 높은 Tech Media | 일반 매체 | 출처 불명확 또는 본문 확인 어려움 |

### 판단 기준

- 7점 이상: 상단 배치 후보
- 4~6점: 일반 배치 또는 보류 검토
- 3점 이하: 하단 배치 또는 PASS 검토
- AI 관련성이 있는 기사는 점수가 낮아도 누락하지 않고 하단에 리스트업
- AI/GPT 카테고리는 AI/IT 관련성이 2점이 아니면 AI/GPT 제외 또는 다른 카테고리 재분류 검토
- Global Big Tech, Asia Big Tech, Social, Theme 카테고리는 AI 관련성이 약해도 플랫폼, 광고, 커머스, 콘텐츠, 규제, 유저 행동 변화와 연결되면 포함 가능
- 점수는 절대적인 포함/제외 기준이 아니라 Query 섹션 내 정렬과 1차 검토 기준으로 사용
- 애매한 경우 비고란에 판단 사유 작성

### 비고란 작성 예시

- `AI 핵심 기사`
- `Global IT 후보`
- `Theme 후보`
- `단순 PR 가능성`
- `중복 가능성`
- `보류 후 재검토`
- `리포트 활용성 낮음`

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

## 기사 수 조정 기준

기사 수가 많을 경우 아래 순서로 우선 제외한다.

1. 동일 이슈의 단순 재보도 기사
2. 단순 투자 유치 기사 중 서비스 변화가 약한 기사
3. 특정 지역 한정 이벤트성 기사
4. 단순 UI 변경 또는 소규모 기능 업데이트
5. 출처 신뢰도가 낮거나 본문 접근이 어려운 기사
6. 리포트 내 다른 기사와 메시지가 겹치는 기사
7. AI/GPT 카테고리에서 AI가 핵심이 아닌 기사
8. 단순 인터뷰, 전망, 의견성 기사 중 구체적 변화가 부족한 기사
9. 단기 캠페인, 프로모션, 브랜드 협업 중심 기사
10. 과거 이슈를 날짜만 바꿔 반복 보도한 기사

기사 수가 적을 경우 아래 기사를 추가 검토한다.

1. Official Source의 주요 업데이트
2. Big Tech의 제품 전략 변화
3. Social / 커뮤니티 / 메시징 기능 변화
4. 국가 단위 규제 또는 유저 행동 변화
5. Asia Big Tech의 AI, 커머스, 메신저, 광고 관련 업데이트
6. Theme 관점의 시장 구조 변화 기사
7. AI Startup 중 제품 출시, 투자, 기술 변화가 명확한 기사
8. 기존 이슈의 후속 업데이트 중 신규 수치나 지역 확장이 있는 기사

### 기사 수 조정 원칙

- 기사 수를 줄일 때는 카테고리 균형을 함께 고려
- AI/GPT 기사는 AI 중심성을 가장 우선 검토
- Global Big Tech와 Social은 플랫폼 전략, 광고, 커뮤니티, 유저 경험 변화 중심으로 유지
- Theme 기사는 시장 변화나 유저 행동 변화가 명확한 경우만 유지
- 기사 수가 적어도 단순 PR성 기사는 억지로 포함하지 않음

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

## Sheet 입력 권장 컬럼

기사 리스트업 Sheet에는 아래 컬럼을 기준으로 입력한다.

| 컬럼명 | 입력 내용 |
| --- | --- |
| Search Query | 기사를 발견한 검색어 또는 Query List 항목 |
| Category | AI/GPT, Global Big Tech, Asia Big Tech, Social, Theme 중 선택 |
| Company / Service | 기업명 또는 서비스명 |
| Original Title | 기사 원문 제목 |
| Korean Title | 최종 리포트용 국문 제목 |
| Published Date | 기사 발행일 |
| Source | 매체명 또는 공식 소스명 |
| Source Type | Official / Tech Media / Local Media / General Media / Paywall Seed 등 |
| URL | 실제 접속 가능하고 본문 확인 가능한 링크 |
| Country / Region | 관련 국가 또는 지역 |
| Key Update | 핵심 변화 요약 |
| AI Relevance | High / Medium / Low |
| Report Relevance | High / Medium / Low |
| Cluster ID | 동일 이슈 묶음 식별용 값 |
| Duplicate Check Keyword | 중복 확인에 사용한 핵심 키워드 |
| Status | Include / PASS / 보류 / 중복 제외 / 대표 기사 유지 등 |
| Note | 선정 사유, 제외 사유, 대체 기사 여부 등 |

### Status 값

- `Include`
- `PASS`
- `보류`
- `중복 제외`
- `대표 기사 유지`
- `후속 기사 유지`
- `Paywall 대체`
- `Source 교체 필요`
- `중복 가능성`
- `기존 이슈 업데이트`
- `AI 관련성 약함`
- `리포트 활용성 낮음`

### 입력 원칙

- Search Query는 추후 검색 루트 확인을 위해 반드시 입력
- Cluster ID는 동일 이슈 기사끼리 같은 값으로 입력
- Duplicate Check Keyword는 과거 중복 확인에 사용한 키워드 입력
- AI Relevance는 AI/GPT 카테고리에서 특히 중요하게 작성
- Report Relevance는 최종 리포트 활용 가능성을 기준으로 판단
- PASS 기사도 필요한 경우 제외 사유를 Note에 간단히 기록
- Paywall 대체 기사는 원 Paywall 기사와 대체 URL을 구분해 기록

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
- 중복 기사 정리 전 비고란에 대표 기사와 보조 출처 또는 중복 기사 표시

## 후속 기사와 중복 기사 구분 기준

### 후속 기사로 유지 가능한 경우

- 기존 발표 이후 신규 수치가 추가된 경우
- 신규 국가 또는 지역 출시가 확인된 경우
- 새로운 파트너십, 고객사, 적용 범위가 추가된 경우
- 기존 기능의 정식 출시, 베타 종료, 글로벌 확장 등 단계 변화가 있는 경우
- 규제, 소송, 정책 이슈에서 새로운 결정이나 결과가 나온 경우
- 기존 이슈에 대한 기업 공식 입장, 제품 업데이트, 기능 변경이 새롭게 확인된 경우
- 이전 기사와 같은 주제라도 리포트 메시지가 달라지는 신규 정보가 있는 경우

### 중복 기사로 대표 선정에서 제외하는 경우

- 같은 발표를 다른 매체가 단순 재보도한 경우
- 제목만 다르고 본문 핵심 내용이 같은 경우
- 기존 Official Blog 내용을 요약한 기사에 불과한 경우
- 새로운 수치, 지역, 기능, 정책 변화가 없는 경우
- 날짜만 최신이고 실제 내용은 과거 이슈 반복인 경우
- 원문 기사보다 늦게 발행된 단순 인용 기사인 경우
- 동일 기업, 동일 기능, 동일 발표 내용을 반복하는 기사인 경우

### 판단 절차

1. 기사 타이틀로 과거 Sheet 전체 검색
2. 기업명 + 기능명 또는 핵심 키워드로 재검색
3. 같은 이슈의 기존 사용 여부 확인
4. 신규 수치, 신규 지역, 신규 기능, 신규 정책 변화 여부 확인
5. 신규 정보가 있으면 후속 기사로 유지
6. 신규 정보가 없으면 대표 기사 아래 `중복` 또는 `보조 출처`로 기록

### 비고란 표기

- 신규 정보 있음: `후속 기사 유지`
- 신규 정보 없음: `중복` 또는 `보조 출처`
- 대표 기사만 유지: `대표 기사 유지`
- 판단 애매함: `중복 가능성`
- 기존 이슈에 추가 정보 있음: `기존 이슈 업데이트`

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

## Korean Title 품질 체크

최종 Korean Title 작성 후 아래 항목을 검수한다.

- [ ] `[Company]` 또는 `[Market]` 형식인지 확인
- [ ] 날짜가 `(YYYY/M/DD)` 형식인지 확인
- [ ] 문장 끝이 `함`, `있음`, `없음`, `됨`으로 끝나지 않는지 확인
- [ ] 제목이 명사형으로 자연스럽게 끝나는지 확인
- [ ] 쉼표가 1개 이하인지 확인
- [ ] 기업명, 서비스명, 기능명은 English로 유지했는지 확인
- [ ] 신규 기능명 또는 신규 서비스명에만 큰따옴표를 사용했는지 확인
- [ ] 기존 기능명에 불필요한 큰따옴표를 쓰지 않았는지 확인
- [ ] 단순 직역투가 아닌 리포트용 문장인지 확인
- [ ] 핵심 변화가 제목만 봐도 드러나는지 확인
- [ ] 기사 본문에 없는 과장된 표현을 넣지 않았는지 확인
- [ ] 단순 기능 설명이 아니라 플랫폼, 유저 경험, 수익화, 시장 변화 관점이 드러나는지 확인

### Title 작성 시 피해야 할 표현

- `~함`
- `~있음`
- `~없음`
- `~됨`
- `~했다`
- `~한다고 밝혔다`
- `~할 예정이다`
- 과도한 직역투
- 불필요하게 긴 수식어
- 기사 본문에 없는 추정 표현
- 신규 기능이 아닌 기존 기능명에 큰따옴표 사용

### Title 작성 예시 방향

- 단순 출시 사실보다 변화의 의미를 중심으로 작성
- 기능명보다 유저 경험, 플랫폼 전략, 수익화, 커뮤니티, 광고, 검색, 커머스 변화가 드러나게 작성
- 특정 기업 하나의 업데이트가 아닌 시장 변화 기사라면 `[Market]` 사용
- AI 기능 기사에서는 AI가 바꾸는 작업 방식, 검색 방식, 콘텐츠 제작 방식, 광고 방식 등을 제목에 반영

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
- [ ] AI/GPT 기사의 AI 중심성 확인
- [ ] 기사 포함 여부 판단 점수표 기준으로 Include / PASS / 보류 판단
- [ ] 후속 기사와 중복 기사 구분 기준 적용
- [ ] Search Query, Cluster ID, Duplicate Check Keyword 입력 여부 확인
- [ ] Source Type 구분 여부 확인
- [ ] Official Source Map 기준으로 1차 소스 확인 여부 검토
- [ ] Source 우선순위 기준으로 최종 URL 선택 여부 확인
- [ ] 카테고리별 우선 포함 기준에 맞는 기사인지 확인
- [ ] 기사 수가 많거나 적을 때 기사 수 조정 기준 적용
- [ ] Korean Title 품질 체크 항목 검수
- [ ] 기존 기능명에 불필요한 큰따옴표가 들어가지 않았는지 확인
- [ ] 단순 PR성 기사, 이벤트성 기사, 반복 보도 기사 제외 여부 확인
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
