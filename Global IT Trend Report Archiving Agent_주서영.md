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
- [Official Source Map](#official-source-map)
- [Query List 적용 방식](#query-list-적용-방식)
- [Official Source 확인 방식](#official-source-확인-방식)
- [Google Query 및 외부 기사 검색 방식](#google-query-및-외부-기사-검색-방식)
- [Source 우선순위 세부 기준](#source-우선순위-세부-기준)
- [Google Query 기사 중복 확인 방식](#google-query-기사-중복-확인-방식)
- [기사 선별 기준](#기사-선별-기준)
- [기사 포함 여부 판단 점수표](#기사-포함-여부-판단-점수표)
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
3. Google Query 전 Official Source가 존재하는 기업·서비스·제품 우선 확인
4. Query List에서 `(Google Query)` 표시 항목은 Google Search 또는 Google News에서만 검색
5. 우선 확인 소스의 주요 업데이트 먼저 기록
6. Google News 및 Google Search로 추가 기사 검색
7. Google Query 기사 Sheet 입력 전 과거 중복 여부 확인
8. 중복 확인 시 날짜 필터 해제 후 기사 타이틀 또는 핵심 키워드로 재검색
9. 동일 기사 또는 동일 이슈의 과거 주차 사용 여부 확인
10. 동일 이벤트 기사는 하나의 Cluster로 묶기
11. Cluster별 가장 적합한 Source 1개만 최종 유지
12. Bloomberg, Reuters, NYTimes 등 Paywall 기사는 접근 가능한 기사로 대체
13. Naver, LINE, LY Corporation 단독 기사 제외
14. 기사 제목, 출처, 날짜, URL, 카테고리, 주요 내용, 포함 여부 Sheet 정리
15. 최종 선별 기사별 Korean Title 작성
16. Weekly AI Trend Report와 Global IT Trend Report에 활용 가능한 기사만 최종 유지

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

- 7점 이상: 포함
- 4~6점: 보류
- 3점 이하: PASS
- AI/GPT 카테고리는 AI/IT 관련성이 2점이 아니면 원칙적으로 PASS
- Global Big Tech, Asia Big Tech, Social, Theme 카테고리는 AI 관련성이 약해도 플랫폼, 광고, 커머스, 콘텐츠, 규제, 유저 행동 변화와 연결되면 포함 가능
- 점수는 절대 기준이 아니라 1차 필터링 기준으로 사용
- 애매한 경우 비고란에 판단 사유 작성

### 비고란 작성 예시

- `AI 핵심 기사`
- `Global IT 후보`
- `Theme 후보`
- `단순 PR 가능성`
- `중복 가능성`
- `보류 후 재검토`
- `리포트 활용성 낮음`

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

## 후속 기사와 중복 기사 구분 기준

### 후속 기사로 유지 가능한 경우

- 기존 발표 이후 신규 수치가 추가된 경우
- 신규 국가 또는 지역 출시가 확인된 경우
- 새로운 파트너십, 고객사, 적용 범위가 추가된 경우
- 기존 기능의 정식 출시, 베타 종료, 글로벌 확장 등 단계 변화가 있는 경우
- 규제, 소송, 정책 이슈에서 새로운 결정이나 결과가 나온 경우
- 기존 이슈에 대한 기업 공식 입장, 제품 업데이트, 기능 변경이 새롭게 확인된 경우
- 이전 기사와 같은 주제라도 리포트 메시지가 달라지는 신규 정보가 있는 경우

### 중복 기사로 제외하는 경우

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
6. 신규 정보가 없으면 중복 기사로 제외

### 비고란 표기

- 신규 정보 있음: `후속 기사 유지`
- 신규 정보 없음: `중복 제외`
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
