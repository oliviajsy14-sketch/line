# Weekly Archiving Process

## 목차

- [자동화 실행 개요](#자동화-실행-개요)
- [자동화 실행 모드](#자동화-실행-모드)
- [업무 목적](#업무-목적)
- [자동화 입력값](#자동화-입력값)
- [자동화 출력값](#자동화-출력값)
- [Output Schema](#output-schema)
- [Sheet 입력 방식](#sheet-입력-방식)
- [기본 작업 단위](#기본-작업-단위)
- [날짜 입력 방식](#날짜-입력-방식)
- [Weekly IT Trend Sheet와 Global IT Trend Sheet 구분](#weekly-it-trend-sheet와-global-it-trend-sheet-구분)
- [Query List 적용 방식](#query-list-적용-방식)
- [Query 전체 리스트](#query-전체-리스트)
- [AI Agent 구역 처리 방식](#ai-agent-구역-처리-방식)
- [AI Agent 세부 Query 우선 배치 기준](#ai-agent-세부-query-우선-배치-기준)
- [AI Agent 기본 Query 배치 기준](#ai-agent-기본-query-배치-기준)
- [Claude Code / Claude Cowork 배치 기준](#claude-code--claude-cowork-배치-기준)
- [AI Agent 기사 배치 예시](#ai-agent-기사-배치-예시)
- [Query별 Sheet 입력 방식](#query별-sheet-입력-방식)
- [Check Box 운영 기준](#check-box-운영-기준)
- [n/a 입력 기준](#na-입력-기준)
- [검색 실패 및 예외 처리](#검색-실패-및-예외-처리)
- [자동화 실행 로그](#자동화-실행-로그)
- [기사 수집 기준](#기사-수집-기준)
- [카테고리별 기준](#카테고리별-기준)
- [카테고리별 우선 포함 기준](#카테고리별-우선-포함-기준)
- [AI 중심성 판단 기준](#ai-중심성-판단-기준)
- [Global IT Trend Report 기사 범위](#global-it-trend-report-기사-범위)
- [기사 중요도 및 정렬 기준](#기사-중요도-및-정렬-기준)
- [수집과 최종 선택의 구분](#수집과-최종-선택의-구분)
- [포함과 제외의 기본 원칙](#포함과-제외의-기본-원칙)
- [중복 기사 처리 방식](#중복-기사-처리-방식)
- [후속 기사와 중복 기사 구분 기준](#후속-기사와-중복-기사-구분-기준)
- [Paywall 기사 처리 방식](#paywall-기사-처리-방식)
- [URL 입력 및 검증 기준](#url-입력-및-검증-기준)
- [URL 언어 기준](#url-언어-기준)
- [Naver / LINE 아카이빙 제외 기준](#naver--line-아카이빙-제외-기준)
- [Korean Title 작성 방식](#korean-title-작성-방식)
- [Korean Title 품질 체크](#korean-title-품질-체크)
- [Korean Title 자동 검증 기준](#korean-title-자동-검증-기준)
- [신기능명 큰따옴표 적용 기준](#신기능명-큰따옴표-적용-기준)
- [최종 검수 체크리스트](#최종-검수-체크리스트)
- [최종 산출물](#최종-산출물)
- [산출물 활용 방식](#산출물-활용-방식)
- [Appendix A. Google Query 전 우선 확인 링크](#appendix-a-google-query-전-우선-확인-링크)
- [Appendix B. Official Source Map](#appendix-b-official-source-map)
- [Appendix C. Source 우선순위 세부 기준](#appendix-c-source-우선순위-세부-기준)
- [수정 요약](#수정-요약)


## 자동화 실행 개요

이 문서는 Weekly IT Trend Sheet와 Global IT Trend Sheet 기사 아카이빙 자동화를 위한 실행 기준이다.

자동화 agent는 아래 흐름으로 작업한다.

1. 작업자가 입력한 날짜 범위와 실행 모드 확인
2. 실행 모드에 맞는 Query List 선택
3. Query별 Official Source, Blog, Newsroom, GitHub, Release Notes, Changelog 우선 확인
4. Google Query 또는 Google News/Search로 누락 기사 보완
5. 기사 날짜, 중복 여부, Paywall 여부, 제외 대상 여부 검수
6. Query별로 관련 기사를 중요도 순으로 정렬
7. Sheet 출력 Schema에 맞춰 Korean Title, Check Box, URL 입력
8. Check Box는 기본 미체크 상태로 생성
9. 작업자가 최종 검토 후 직접 Check Box 선택
10. 검색 실패, 제외 기사, Paywall, 중복 등은 Sheet 본문이 아니라 실행 로그에 기록

## 자동화 실행 모드

자동화 agent는 실행 전 반드시 아래 모드 중 하나를 선택한다.

| run_mode | 작업 대상 | 사용 Query List | 출력 대상 |
|---|---|---|---|
| weekly | Weekly IT Trend Sheet | Weekly Sheet Query | Weekly IT Trend Sheet |
| global | Global IT Trend Sheet | Global IT Trend Sheet Query | Global IT Trend Sheet |

운영 기준:

- `run_mode=weekly`인 경우 Weekly Sheet Query만 사용한다.
- `run_mode=global`인 경우 Global IT Trend Sheet Query만 사용한다.
- 두 Query List를 임의로 병합하지 않는다.
- 선택된 run_mode와 다른 Query List는 사용하지 않는다.
- 작업자가 run_mode를 명시하지 않은 경우 자동화 agent는 작업을 시작하지 않고 run_mode 확인이 필요하다고 표시한다.

## 업무 목적

- 주간 단위로 주요 IT 및 AI 관련 뉴스 수집
- 수집 기사를 기사 리스트업 Sheet에 카테고리별 정리
- Weekly AI Trend Report 및 Global IT Trend Report 작성에 활용
- 중복 기사, 비대상 기사, 단순 PR성 기사 제외
- Query별 관련 기사를 넓게 수집하고 최종 리포트 반영 여부는 작업자가 Check Box로 선택

## 자동화 입력값

자동화 agent가 작업을 수행할 때 필요한 입력값은 아래와 같다.

| 입력값 | 필수 여부 | 설명 | 예시 |
|---|---|---|---|
| run_mode | 필수 | 작업 대상 시트 구분 | `weekly` 또는 `global` |
| date_range | 필수 | 검색 기간 | `2026.6.18~2026.6.24` |
| sheet_name | 필수 | 작업할 Sheet 이름 또는 탭명 | `6월 4주` |
| source_sheet_template | 권장 | 기존 Sheet 템플릿 | 이전 주차 Sheet |
| query_list | 자동 선택 | run_mode에 따라 자동 선택 | Weekly Sheet Query / Global IT Trend Sheet Query |
| official_source_links | 필수 | Google Query 전 우선 확인 링크 | Appendix A |
| previous_archive | 권장 | 과거 중복 확인용 기존 아카이브 | 이전 주차 Sheet |
| exclude_companies | 필수 | 제외 대상 기업 | Naver / LINE / LY Corporation 단독 기사 |

입력 기준:

- 검색 기간은 `yyyy.m.d~yyyy.m.d` 형식으로 입력한다.
- 날짜에는 `/`를 사용하지 않는다.
- 월/일에는 0 padding을 사용하지 않는다.
- 예: 월/일 두 자리 0 padding 입력이 아니라 `2026.6.8~2026.6.14`처럼 입력한다.

## 자동화 출력값

자동화 agent는 아래 구조로 결과를 생성한다.

- 대분류
- Query / Service
- Korean Title
- Check Box
- URL

자동화 agent는 아래 컬럼 외의 컬럼을 임의로 추가하지 않는다.

## Output Schema

| Field | Required | 입력 규칙 |
|---|---|---|
| 대분류 | 필수 | Query List의 Category와 동일하게 입력 |
| Query / Service | 필수 | Query List 표기 그대로 입력 |
| Korean Title | 필수 | 기사 제목 입력, 기사 없음 확인 시 `n/a` 입력 |
| Check Box | 필수 | 신규 기사는 기본 미체크 상태 |
| URL | 조건부 필수 | Korean Title이 `n/a`이면 빈칸, 기사 있으면 필수 |

출력 금지 컬럼:

- Original Title
- Key Update
- AI Relevance
- Report Relevance
- Cluster ID
- Duplicate Check Keyword
- Status
- Note
- Source Type
- Published Date
- Country / Region

주의:

- 원문 제목은 참고용으로만 사용하고 Sheet에는 출력하지 않는다.
- 기사 발행일은 Korean Title 끝의 `(yyyy.m.d)` 안에 포함한다.
- URL은 Korean Title 안에 넣지 않고 URL 칸에만 입력한다.
- Check Box는 자동화 agent가 임의로 체크하지 않는다.

## Sheet 입력 방식

Sheet 입력 구조는 아래 형식을 따른다.

| 대분류 | Query / Service | Korean Title | Check Box | URL |
|---|---|---|---|---|

입력 기준:

- 대분류와 Query / Service 순서는 해당 run_mode의 Query List 순서를 strict하게 따른다.
- Query 이름은 임의로 수정하지 않는다.
- 특정 Query에서 기사가 여러 개 발견되면 같은 Query 아래 여러 행으로 입력한다.
- 특정 Query를 확인했지만 입력할 기사가 없으면 Korean Title 칸에 `n/a`를 입력한다.
- 검색 실패 또는 접속 실패는 `n/a`로 처리하지 않고 실행 로그에 기록한다.
- Check Box는 기본 미체크 상태로 생성한다.
- URL이 여러 개인 경우 같은 URL 셀 안에서 줄바꿈으로 입력한다.

## 기본 작업 단위

- 작업 주기: 주 1회
- 검색 기간: 작업자가 `yyyy.m.d~yyyy.m.d` 형식으로 직접 입력
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
- [ ] 검색 기간이 `yyyy.m.d~yyyy.m.d` 형식인지 확인
- [ ] 기사 리스트업 Sheet의 기존 템플릿 확인
- [ ] 새 주차 탭 생성
- [ ] 기존 서식 유지
- [ ] 카테고리별 입력 영역 확인
- [ ] 이전 주차 기사와 중복 확인이 가능하도록 기존 Sheet 접근 상태 확인

## 날짜 입력 방식

- 입력 형식: `yyyy.m.d~yyyy.m.d`
- 입력 예시: `2026.6.18~2026.6.24`
- 개별 기사 발행일 형식: `yyyy.m.d`
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
4. Appendix A. Google Query 전 우선 확인 링크에서 Official Source, Blog, Newsroom, GitHub, Release Notes, Changelog 먼저 확인
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

자세한 공식 링크 목록은 `Appendix A. Google Query 전 우선 확인 링크`를 참고한다.
공식 소스 매핑은 `Appendix B. Official Source Map`을 참고한다.
Source 우선순위 세부 기준은 `Appendix C. Source 우선순위 세부 기준`을 참고한다.

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

## Query List 적용 방식

- 자동화 agent는 작업 대상 시트에 맞는 Query List만 사용한다.
- Weekly IT Trend Sheet 작업 시 `Weekly Sheet Query`만 사용한다.
- Global IT Trend Sheet 작업 시 `Global IT Trend Sheet Query`만 사용한다.
- 두 Query List를 임의로 병합하지 않는다.
- Query 순서는 아래에 정의된 순서를 strict하게 따른다.
- Query 이름은 임의로 수정하지 않는다.
- Query별 공식 링크가 있으면 Google Query 전 우선 확인 링크를 먼저 확인한다.
- Query에 `Google Query`가 표시되어 있으면 Google Search 또는 Google News 중심으로 검색한다.
- Query별 기사 입력 시 Sheet에는 `Korean Title`, `Check Box`, `URL` 중심으로 입력한다.

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
- 검색 기간은 작업자 입력 `yyyy.m.d~yyyy.m.d` 범위 적용
- 검색 결과는 최신순과 관련도 기준으로 확인
- 동일 내용이 여러 매체에 반복되면 아래 우선순위 적용:
  1. 원출처에 가까운 기사
  2. Official Source
  3. 신뢰도 높은 Tech Media
  4. 본문 접근 가능한 영어 기사
- Google Query 신규 발견 기사는 과거 중복 여부 확인 후 Sheet 입력

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

## 기사 중요도 및 정렬 기준

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
- 같은 내용을 반복한 기사라면 Sheet에 별도 행으로 반복 입력하지 않는다.
- 보완 가치가 있는 URL은 대표 기사 URL 셀에 줄바꿈으로 함께 입력한다.
- 정보 가치가 낮은 중복 기사는 Sheet에 입력하지 않고 실행 로그에 기록할 수 있다.

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

## 중복 기사 처리 방식

중복 판단은 자동화 내부 로직으로만 사용한다.
Sheet에는 `Cluster ID`, `Status`, `Note`, `Duplicate Check Keyword` 컬럼을 만들지 않는다.

Cluster는 Sheet 컬럼이 아니라 자동화 내부 중복 판단 기준이다. 자동화 agent는 동일 이슈를 내부적으로 Cluster처럼 판단할 수 있지만, Sheet에는 Cluster ID를 출력하지 않는다. Cluster 판단 결과는 필요 시 실행 로그에만 남긴다.

### 중복 판단 기준

아래 조건이 같으면 동일 이슈 또는 중복 기사로 판단한다.

- 같은 기업 또는 서비스
- 같은 기능 또는 제품 업데이트
- 같은 발표
- 같은 파트너십
- 같은 투자
- 같은 규제 이슈
- 같은 수치 또는 같은 보고서 기반 보도
- 같은 원출처를 재가공한 기사

### Sheet 처리 기준

- 동일 이슈에서는 대표 기사 1개만 Sheet에 입력한다.
- 공식 발표가 있으면 공식 발표를 대표 URL로 우선 사용한다.
- Tech Media 기사에 시장 반응, 신규 수치, 경쟁사 맥락, 추가 설명이 있으면 같은 URL 셀에 줄바꿈으로 함께 입력한다.
- 정보 가치가 낮은 단순 재보도는 Sheet에 입력하지 않는다.
- 완전히 동일한 내용의 반복 보도는 대표 기사 1개만 유지한다.
- 과거 동일 기사 또는 동일 이슈가 있으면 Sheet에 별도 행으로 반복 입력하지 않는다.
- 보완 가치가 있는 URL은 대표 기사 URL 셀에 줄바꿈으로 함께 입력한다.
- 정보 가치가 낮은 중복 기사는 Sheet에 입력하지 않고 실행 로그에 기록할 수 있다.
- 중복으로 제외한 기사 URL은 Sheet 본문이 아니라 실행 로그에 기록할 수 있다.

### 보조 URL 입력 기준

- 공식 발표와 외부 보완 기사가 모두 정보 가치가 있으면 URL 셀에 줄바꿈으로 함께 입력한다.
- URL 셀에서는 공식 발표를 첫 줄에 입력한다.
- Tech Media 보완 링크는 두 번째 줄부터 입력한다.
- 단순 재보도 링크는 URL 셀에 추가하지 않는다.

### 후속 기사로 별도 입력 가능한 경우

아래 중 하나라도 해당하면 중복이 아니라 후속 기사로 별도 입력할 수 있다.

- 신규 기능 추가
- 신규 지역 출시
- 신규 수치 공개
- 신규 파트너십 발표
- 신규 규제 변화
- 후속 제품 출시
- 기존 이슈 이후 기업 공식 입장 변화
- 기존 발표 이후 실제 유저 영향 또는 시장 반응이 새롭게 확인된 경우

### Sheet와 실행 로그 구분

| 상황 | Sheet 처리 | 실행 로그 |
|---|---|---|
| 공식 발표 + 보완 기사 | 대표 Korean Title 1개, URL 셀에 링크 줄바꿈 | 선택 |
| 단순 재보도 | 입력하지 않음 | 선택 |
| 완전 동일 기사 | 대표 기사만 입력 | 선택 |
| 후속 업데이트 | 별도 기사로 입력 가능 | 선택 |
| 중복 여부 불확실 | 대표 URL 중심으로 입력 가능 | 실행 로그에 기록 |
| Paywall 원출처만 존재 | 대체 링크 찾은 경우만 Sheet 입력 | 필수 |

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

## URL 입력 및 검증 기준

URL은 실제 접속 가능하고 본문 확인 가능한 링크만 입력한다.

자동화 agent는 URL 입력 전 아래 조건을 확인한다.

- URL이 빈 값이 아닌지 확인
- URL이 `http://` 또는 `https://`로 시작하는지 확인
- 접속 가능한지 확인
- 본문 확인이 가능한지 확인
- 로그인 필요, Paywall, 본문 미확인 링크는 최종 URL로 사용하지 않음
- 동일 URL이 같은 Sheet 내에 이미 있는 경우 중복 입력하지 않음
- URL이 여러 개인 경우 공식 링크를 첫 줄에 입력하고, 보완 링크를 두 번째 줄부터 입력
- 단순 재보도 링크는 여러 개 넣지 않음
- 공식 발표와 외부 보완 기사가 같은 이슈를 다루지만 각각 정보 가치가 있으면 함께 입력 가능

URL 우선순위:

1. Official Source
2. GitHub Release / Changelog / Release Notes
3. 신뢰도 높은 Tech Media
4. 현지 전문 매체
5. 일반 매체
6. 단순 재보도 매체는 후순위 또는 제외

## Korean Title 자동 검증 기준

Korean Title은 아래 조건을 모두 만족해야 한다.

- `[회사명]` 또는 `[Market]`으로 시작
- 제목 끝에 `(yyyy.m.d)` 포함
- 날짜에 `/` 사용 금지
- 월/일 0 padding 금지
- URL을 제목 안에 포함하지 않음
- 원문 제목을 그대로 번역하지 않음
- 쉼표는 최대 1개만 사용
- 정식 릴리스, 정식 출시, public beta, 공식 출시 예정인 신규 기능명·서비스명에는 큰따옴표 사용
- 기존 서비스명이나 기존 기능명에는 불필요한 큰따옴표를 사용하지 않음
- 기업명은 기사 주체 기준으로 작성
- 산업 전반 또는 특정 기업 중심이 아닌 경우 `[Market]` 사용
- 문장 끝은 명사형 중심으로 정리
- 정식 릴리스, 정식 출시, public beta, 공식 출시 예정인 신규 기능명·서비스명에는 큰따옴표를 사용한다.
- 내부 테스트, 비공개 테스트, 루머, 기존 기능 업데이트·확대, 기능명이 정확하지 않은 경우, 버튼명에는 큰따옴표를 사용하지 않는다.
- beta라고 표현되어도 public beta인지 명확하지 않으면 큰따옴표를 사용하지 않는다.
- 기존 기능명에는 불필요한 큰따옴표를 사용하지 않는다.

### 올바른 예시

- [OpenAI] "Safety Fellowship" 공개하며 AI 안전과 정렬 연구 인재 육성 프로그램 운영 (2026.4.6)
- [Google] Gemini overlay와 Gemini Live UI 통합 재설계 통해 AOS 상호작용 방식과 Multi-modal 접근성 개선 (2026.4.7)
- [Market] AI data center, 투자자 요구로 Big Tech 대상 전력과 수자원 사용량 공개 압박 확대 (2026.4.8)

### 잘못된 예시

- [Google] Gemini 업데이트 (2026.4.7)
- Google announces Gemini updates
- [OpenAI] Safety Fellowship 공개 (2026.4.6) - https://example.com


## 신기능명 큰따옴표 적용 기준

Korean Title 작성 시 신규 기능명 또는 신규 서비스명에는 큰따옴표를 붙인다.
단, 기능명처럼 보인다고 모두 큰따옴표를 붙이지 않고, 아래 기준에 따라 제한적으로 적용한다.

### 큰따옴표를 붙이는 경우

아래에 해당하면 기능명 또는 서비스명에 큰따옴표를 붙인다.

- 정식 릴리스된 신규 기능명
- 정식 출시된 신규 서비스명
- public beta로 공개된 신규 기능명
- public beta로 공개된 신규 서비스명
- 공식 발표 기준 출시 예정인 신규 기능명
- 공식 발표 기준 출시 예정인 신규 서비스명
- 새롭게 공개된 제품명, 기능명, 프로그램명, 모델명

### 큰따옴표를 붙이지 않는 경우

아래에 해당하면 기능명처럼 보이더라도 큰따옴표를 붙이지 않는다.

- 내부 테스트 중인 기능
- 비공개 테스트 중인 기능
- 루머 단계의 기능
- 출시 여부가 공식 확인되지 않은 기능
- 이미 출시된 기존 기능의 업데이트
- 기존 기능의 적용 범위 확대
- 기존 기능의 지역 확대
- 기존 기능의 UI 개선
- 기능명이 정확하지 않거나 기사에서 임시 명칭처럼 언급된 경우
- 단순 버튼명
- 메뉴명
- 일반 UX 요소명
- 기능 카테고리명
- 기사 작성자가 임의로 표현한 설명형 명칭

## public beta / 내부 테스트 큰따옴표 구분

- public beta는 외부 유저, 개발자, 일부 공개 대상에게 공식적으로 공개된 베타 테스트를 의미한다.
- public beta로 공개된 신규 기능명 또는 서비스명은 큰따옴표를 붙인다.
- 내부 테스트는 회사 내부 직원, 제한된 비공개 그룹, 초대 기반 비공개 테스트, 루머성 테스트를 의미한다.
- 내부 테스트 또는 비공개 테스트 단계의 기능명에는 큰따옴표를 붙이지 않는다.
- 기사에서 beta라고 표현되어도 public beta인지 명확하지 않으면 큰따옴표를 붙이지 않는다.
- 공식 Blog, 공식 Release Notes, 공식 Newsroom에서 public beta라고 명시된 경우에만 큰따옴표를 붙인다.

## 출시 예정 기능 큰따옴표 기준

- 공식 발표에서 특정 기능명 또는 서비스명이 출시 예정이라고 명확히 공개된 경우 큰따옴표를 붙인다.
- 출시 예정이지만 기능명이 정확하지 않거나 설명형 표현에 가까운 경우 큰따옴표를 붙이지 않는다.
- 루머, 유출, 비공식 보도 기반 출시 예정 기능에는 큰따옴표를 붙이지 않는다.

## 큰따옴표 적용 예시

| 상황 | 큰따옴표 | 예시 |
|---|---|---|
| 신규 기능 정식 릴리스 | O | [Snap] "Snap Smart Assistant" 공개하며 AI 광고 제작 기능 확대 (2026.6.18) |
| 신규 서비스 정식 출시 | O | [OpenAI] "Safety Fellowship" 공개하며 AI 안전 연구 인재 육성 프로그램 운영 (2026.4.6) |
| public beta 공개 | O | [Google] "AI Edge Eloquent" public beta 공개하며 오프라인 Dictation 기능 테스트 확대 (2026.4.6) |
| 공식 출시 예정 기능 | O | [Apple] "Personalized Siri" 출시 예정 발표하며 Apple Intelligence 기반 개인화 기능 강화 (2026.6.18) |
| 내부 테스트 | X | [Apple] Siri 기반 앱 간 작업 수행 기능 내부 테스트 진행 (2026.6.18) |
| 비공개 테스트 | X | [Meta] Threads 알고리즘 조정 기능 비공개 테스트 진행 (2026.6.18) |
| 루머 | X | [Google] Gemini 기반 검색 Agent 출시 가능성 부상 (2026.6.18) |
| 기존 기능 업데이트 | X | [Google] Gemini overlay와 Gemini Live UI 통합 재설계 (2026.4.7) |
| 기존 기능 확대 | X | [Meta] WhatsApp AI 요약 기능 적용 범위 확대 (2026.6.18) |
| 기능명이 정확하지 않음 | X | [Amazon] AI 쇼핑 보조 기능 개선하며 구매 전환 UX 강화 (2026.6.18) |
| 버튼명 | X | [TikTok] Shop Now 버튼 테스트 확대하며 광고 전환 UX 개선 (2026.6.18) |

## Query Source Mapping 예시

| Query | Primary Source | Secondary Source | Fallback |
|---|---|---|---|
| OpenAI | OpenAI News | OpenAI Docs / Changelog | Google Query |
| ChatGPT | ChatGPT Release Notes | OpenAI News | Google Query |
| Codex | Codex Changelog | OpenAI News | Google Query |
| Gemini | Gemini Release Notes | Google Blog / DeepMind Blog | Google Query |
| Google AI | Google AI Blog | DeepMind Blog / Google Research Blog | Google Query |
| OpenClaw (Moltbot, Clawdbot) | OpenClaw Blog | GitHub Releases | Google Query |
| Claude Code | Claude Docs | Anthropic Engineering / Claude Blog | Google Query |
| Meta AI | Meta AI Blog | Meta Newsroom / Engineering Blog | Google Query |
| Microsoft Edge | Microsoft Edge Blog | Bing Blog | Google Query |
| Arc Browser | Browser Company Blog |  | Google Query |
| Douyin | Google Query |  | Google News |
| Kakao AI | Kakao Newsroom | Kakao Press | Google Query |
| LINE / LY Corporation | 아카이빙 제외 |  | 단독 기사 제외 |

운영 기준:

- 위 표는 예시이며, 전체 Query List 표기는 변경하지 않는다.
- Query 이름과 Source 이름이 다르더라도 동일 서비스로 판단 가능한 경우 연결한다.
- 단, Sheet Query 표기는 절대 변경하지 않는다.

## Machine-readable Query Table

| Sheet | Category | Query | Search Type |
|---|---|---|---|
| weekly | AI Agent | AI Agent | Google Query |
| weekly | AI Agent | OpenClaw (Moltbot, Clawdbot) | Official First |
| weekly | AI Agent | Paperclip | Official First |
| weekly | AI | OpenAI | Official First |
| weekly | AI | Gemini | Official First |
| weekly | Browser | Arc Browser | Official First |
| weekly | Browser | Voice Synthesis | Google Query |
| global | AI Agent | AI Agent - Google Query | Google Query |
| global | AI/GPT | AI - Google Query | Google Query |
| global | AI/GPT | OpenAI | Official First |
| global | Global Big Tech | Meta | Official First |
| global | Social | TikTok | Official First |
| global | Theme | Gen Z - Google Query | Google Query |

기준:

- 기존 Query List 전체를 이 표로 모두 재작성하지 않고, 자동화 예시로만 사용한다.
- `Search Type`은 `Official First` 또는 `Google Query` 중 하나를 사용한다.
- `Google Query`가 이름에 포함된 항목은 `Search Type=Google Query`로 처리한다.
- 공식 링크가 있는 항목은 `Search Type=Official First`로 처리한다.
- 공식 링크가 없거나 불명확한 항목은 `Search Type=Google Query`로 처리한다.

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
- 정식 릴리스, 정식 출시, public beta, 공식 출시 예정인 신규 기능명·서비스명에는 큰따옴표 사용
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

- `n/a`는 해당 Query를 검색했고, 날짜 범위 내 입력할 기사가 없음을 의미한다.
- Query / Service 항목을 확인했지만 해당 기간 내 입력할 기사가 없으면 Korean Title 칸에 `n/a`를 입력한다.
- `n/a`가 입력된 행은 Check Box와 URL을 비워둔다.
- 검색 자체를 수행하지 않은 항목에는 `n/a`를 입력하지 않는다.
- 검색 실패, 접속 오류, 차단, 네트워크 오류는 `n/a`로 처리하지 않는다.
- 검색 실패 상태는 Sheet 본문이 아니라 실행 로그에 기록한다.

## n/a와 미검색 상태 구분

| 상태 | Sheet 입력 | 실행 로그 |
|---|---|---|
| 검색 완료, 기사 없음 | Korean Title에 `n/a` | 선택 |
| 검색 실패 | Sheet 입력하지 않음 | 필수 |
| 접속 실패 | Sheet 입력하지 않음 | 필수 |
| Paywall만 존재 | 대체 링크 없으면 입력하지 않음 | 필수 |
| 날짜 범위 밖 기사만 존재 | Korean Title에 `n/a` | 선택 |

## 검색 실패 및 예외 처리

자동화 agent는 검색 과정에서 아래 예외 상황을 구분한다.

| 상황 | 처리 방식 |
|---|---|
| 검색 결과 없음 | 해당 Query를 `n/a`로 입력 |
| 검색 실패 | Sheet에 `n/a` 입력 금지, 실행 로그에 기록 |
| URL 접속 실패 | 대체 링크 검색, 실패 시 실행 로그에 기록 |
| Paywall 기사만 발견 | 접근 가능한 대체 링크 추가 검색 |
| 날짜 범위 밖 기사만 발견 | `n/a` 입력 가능 |
| 공식 링크 업데이트 없음 | 필요 시 `n/a` 입력 |
| Query와 무관한 기사만 발견 | `n/a` 입력 가능 |
| Naver / LINE / LY Corporation 단독 기사 | Sheet 입력 금지, 실행 로그 기록 |
| 중복 기사만 발견 | 대표 기사 이미 있으면 추가 입력하지 않음 |

주의:

- 검색 실패와 기사 없음은 다르게 처리한다.
- 자동화 agent는 실패 상황을 임의로 `n/a` 처리하지 않는다.
- 본문 확인이 안 되는 기사는 최종 URL로 사용하지 않는다.

## 자동화 실행 로그

자동화 agent는 Sheet 본문에는 Status/Note를 만들지 않지만, 실행 과정에서 아래 항목을 별도 로그로 남길 수 있다.

로그에 남길 항목:

- 검색 실패 Query
- 접속 실패 URL
- Paywall로 제외한 URL
- 날짜 범위 밖 기사
- 중복으로 제외한 기사
- Query List에 없는 기사
- Naver / LINE / LY Corporation 단독 기사로 제외한 기사
- 공식 링크는 있으나 업데이트가 없는 Query
- Google Query 결과가 없었던 Query
- 제목 생성 실패 기사
- 날짜 확인이 어려운 기사

로그 형식 예시:

| Type | Query | URL | Reason | Action |
|---|---|---|---|---|
| search_failed | Gemini |  | Google Search 결과 확인 실패 | 재검색 필요 |
| paywall | OpenAI | https://example.com | 본문 확인 불가 | 대체 링크 검색 |
| duplicate | Claude Code | https://example.com | 이전 주차 동일 이슈 | Sheet 입력 제외 |
| excluded_company | LINE | https://example.com | LINE 단독 기사 | 제외 |
| out_of_range | Meta AI | https://example.com | 날짜 범위 밖 기사 | 제외 |

운영 기준:

- 실행 로그는 Sheet 본문에 입력하지 않는다.
- 실행 로그는 별도 `run_log`, 작업 요약, 또는 자동화 결과 보고에만 남긴다.
- 실행 로그는 작업자가 자동화 결과를 검수하기 위한 참고 자료다.

## 수집과 최종 선택의 구분

- 기사 리스트업 Sheet의 목적은 처음부터 최종 리포트 기사만 남기는 것이 아니라, Query별 관련 기사를 수집한 뒤 검토자가 빠르게 판단할 수 있도록 정리하는 것이다.
- 1차 수집 단계에서는 Global IT / AI / Big Tech / Asia Tech / Social / Market Trend와 관련된 기사를 넓게 리스트업한다.
- 관련성이 있는 기사는 중요도가 낮아 보여도 누락하지 않고 Query 섹션 안에 입력한다.
- 중요한 기사는 해당 Query 섹션의 위쪽에 배치한다.
- 중요도가 낮거나 단순 PR성에 가까운 기사는 아래쪽에 배치한다.
- 최종 리포트 반영 여부는 사람이 Check Box로 선택한다.
- 단, 명백한 비대상 기사, Naver/LINE/LY Corporation 단독 기사, 완전 중복 기사, 본문 확인 불가 기사, AI/IT/플랫폼 관련성이 거의 없는 기사는 입력하지 않는다.


## 포함과 제외의 기본 원칙

- 관련성이 있는 기사는 중요도가 낮아도 리스트업한다.
- 중요도는 제외 기준이 아니라 Query 섹션 안에서의 정렬 기준으로 사용한다.
- 단, IT/AI/플랫폼/시장 변화와 직접 관련이 없거나, 단순 PR/이벤트/본문 확인 불가/완전 중복이면 제외한다.
- Naver / LINE / LY Corporation 단독 기사는 기존 제외 기준에 따라 Sheet에 입력하지 않는다.
- 기사 수 조정이 필요한 경우에도 관련성이 낮은 기사부터 하단 배치 또는 제외 검토하되, 단순히 중요도가 낮다는 이유만으로 자동 제외하지 않는다.
## AI Agent 구역 처리 방식

- `AI Agent`는 Weekly AI Trend Report에서 별도 상단 구역으로 관리할 수 있다.
- 리포트 카테고리 기준으로는 `AI/GPT`에 포함된다.
- Sheet에서는 AI Agent 관련 Query가 많기 때문에 `AI Agent`를 별도 대분류처럼 배치할 수 있다.
- AI Agent 구역에는 OpenClaw, AutoGPT, AgentGPT, CrewAI, LangGraph, Claude Code, agentic workflow, enterprise AI agent, agentic commerce, AI payment, AI security 등 관련 기사를 입력한다.
- AI Agent 관련 기사의 최종 배치 위치는 아래 우선순위를 따른다.
  1. AI Agent 구역 내 세부 Query와 직접 매칭되는 경우 해당 세부 Query 아래에 입력하고, `AI Agent` 기본 Query로 올리지 않는다.
  2. AI Agent 관련 기사이지만 AI Agent 구역 내 세부 Query와 직접 매칭되지 않는 경우 `AI Agent` 대분류의 기본 Query인 `AI Agent` 아래에 입력한다.
  3. AI Agent가 단순 언급 수준인 경우 AI Agent 구역으로 이동하지 않고 원래 회사/서비스 Query에 입력한다.

## AI Agent 세부 Query 우선 배치 기준

- AI Agent 관련 기사라도 AI Agent 구역 안에 이미 해당 세부 Query가 있으면, `AI Agent` 기본 Query가 아니라 해당 세부 Query 아래에 입력한다.
- 기사 발견 위치나 검색 Query보다 최종 배치 Query를 우선하되, AI Agent 구역 내부에서는 세부 Query 매칭을 최우선으로 한다.
- 예를 들어 Claude Cowork 관련 기사는 Anthropic, Claude, Claude Code, AI/GPT 쪽에서 발견되더라도 `AI Agent > Claude Cowork`에 입력한다.
- OpenClaw 관련 기사는 `AI Agent > OpenClaw (Moltbot, Clawdbot)`에 입력한다.
- AutoGen 관련 기사는 `AI Agent > Microsoft AutoGen` 또는 `AI Agent > AutoGen` 중 실제 Query와 더 가까운 항목에 입력한다.
- CrewAI 관련 기사는 `AI Agent > CrewAI`에 입력한다.
- LangGraph 관련 기사는 `AI Agent > LangGraph`에 입력한다.
- KIRA 관련 기사는 `AI Agent > KIRA`에 입력한다.
- Wrtn Crack 또는 Crack 관련 기사는 해당 시트의 Query 표기에 맞춰 `Wrtn Crack` 또는 `Crack (크랙)`에 입력한다.
- Nomi, Kindroid, Paradot, Replika, Poketomo, Hume AI 등 AI Agent 구역 내 세부 Query와 직접 관련된 기사는 각각의 세부 Query 아래에 입력한다.
- AI Agent 구역 안에 동일하거나 더 구체적인 세부 Query가 존재하면 `AI Agent > AI Agent` 기본 Query에 넣지 않는다.
- AI Agent 기본 Query는 세부 Query와 직접 매칭되지 않는 AI Agent 기사만 입력하는 fallback Query다.
- 예: Spotify, Apple, Google, Meta, Amazon 등 일반 회사 Query에서 AI Agent 관련 기능이 발견되었지만 AI Agent 세부 Query와 직접 매칭되지 않는 경우 `AI Agent > AI Agent`에 입력한다.
- 예: CrewAI, LangGraph, OpenClaw처럼 세부 Query가 이미 존재하면 해당 세부 Query 아래에 입력한다.

## AI Agent 기본 Query 배치 기준

- AI Agent 관련 기사이지만 AI Agent 구역 내 세부 Query와 직접 매칭되지 않는 경우에만 `AI Agent > AI Agent` 기본 Query 아래에 입력한다.
- 특히 Spotify, Apple, Google, Meta, Amazon, Microsoft, OpenAI, Anthropic, TikTok, Snapchat, Discord 등 일반 회사/서비스 Query에서 발견된 기사라도, 기사 핵심이 새로운 AI Agent / Agentic AI / autonomous task / tool-use / workflow automation / agentic commerce / agentic payment / coding agent / enterprise agent라면 `AI Agent > AI Agent`에 배치한다.
- 단, 해당 기사 내용이 AI Agent 구역 내 기존 세부 Query와 직접 매칭되면 `AI Agent > AI Agent`가 아니라 해당 세부 Query에 입력한다.
- 단순히 AI Agent가 홍보 문구로 언급되었거나 실제 autonomous task, tool-use, workflow automation 기능이 없는 기사는 AI Agent 기본 Query로 이동하지 않는다.


## Claude Code / Claude Cowork 배치 기준

- Claude Cowork 관련 기사는 `AI Agent > Claude Cowork`에 입력한다.
- Claude Code 관련 기사 중 coding agent, tool-use, autonomous coding workflow, MCP 기반 agent workflow가 핵심이면 AI Agent 관련 기사로 판단한다.
- 단, Claude Code는 AI Agent 구역의 세부 Query에 직접 존재하지 않는 경우가 있으므로, AI Agent 세부 Query와 직접 매칭되지 않으면 `AI Agent > AI Agent` 기본 Query에 입력한다.
- 일반 Claude Code 업데이트, 일반 개발자 도구 업데이트, 단순 docs 업데이트는 `AI/GPT > Claude Code`에 입력한다.
- Claude Code와 Claude Cowork를 자동으로 같은 Query로 병합하지 않는다.

## AI Agent 기사 배치 예시

| 발견 Query | 기사 핵심 내용 | 최종 배치 |
|---|---|---|
| Anthropic | Claude Cowork 관련 AI Agent 업데이트 | AI Agent > Claude Cowork |
| Claude | Claude Cowork 기반 업무 자동화 기능 확장 | AI Agent > Claude Cowork |
| Microsoft | AutoGen 관련 multi-agent workflow 업데이트 | AI Agent > Microsoft AutoGen 또는 AutoGen |
| OpenClaw | OpenClaw 버전 업데이트 | AI Agent > OpenClaw (Moltbot, Clawdbot) |
| CrewAI | CrewAI 신규 기능 또는 release note | AI Agent > CrewAI |
| LangGraph | LangGraph agent workflow 업데이트 | AI Agent > LangGraph |
| Spotify | Spotify가 AI Agent 기반 음악 추천 또는 creator workflow 자동화 기능 공개 | AI Agent > AI Agent |
| Apple | Apple이 Siri 기반 agentic task automation 기능 발표 | AI Agent > AI Agent |
| Google AI | Google이 Gemini 기반 범용 task automation agent 공개 | AI Agent > AI Agent |
| Meta AI | Meta가 광고 운영 자동화 business AI agent 공개 | AI Agent > AI Agent |
| Amazon AI | Amazon이 agentic shopping 또는 Bedrock Agent 기반 workflow 자동화 공개 | AI Agent > AI Agent |
| Gemini | 일반 Gemini UI 업데이트 | AI/GPT > Gemini |
| Apple | 일반 iOS 기능 업데이트 또는 Apple Intelligence 일반 기능 개선 | AI/GPT 또는 Global Big Tech > Apple / iOS |
| Spotify | 일반 social/audio platform 업데이트 | Theme 또는 해당 관련 Query |

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

## Korean Title 작성 방식

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
- 정식 릴리스, 정식 출시, public beta, 공식 출시 예정인 신규 기능명·서비스명에만 큰따옴표 사용
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

## Weekly IT Trend Sheet와 Global IT Trend Sheet 구분

Weekly IT Trend Sheet와 Global IT Trend Sheet는 서로 다른 시트이며, 사용하는 Query List도 다르다.

- Weekly IT Trend Sheet:
  - AI Agent, AI, Browser 중심 Query를 사용한다.
  - Weekly AI Trend Report 및 AI 중심 아카이빙에 활용한다.
  - AI Agent / AI / Browser 관련 항목을 넓게 확인한다.

- Global IT Trend Sheet:
  - AI Agent, AI/GPT, Global Big Tech, Asia Big Tech, Social, Theme Query를 사용한다.
  - Global IT Trend Report 작성에 활용한다.
  - AI뿐 아니라 Big Tech, Asia Big Tech, Social, Theme 관련 IT/플랫폼/시장 트렌드까지 포함한다.

두 시트의 Query List는 서로 섞지 않는다.
자동화 agent는 작업 대상 시트가 Weekly IT Trend Sheet인지 Global IT Trend Sheet인지 먼저 확인한 뒤, 해당 시트의 Query List만 사용한다.

## Query 전체 리스트

Query 전체 리스트는 `Weekly Sheet Query`와 `Global IT Trend Sheet Query`로 분리한다.
자동화 agent는 작업 대상 시트에 해당하는 Query List만 사용하고, 두 Query List를 임의로 병합하지 않는다.

### Weekly Sheet Query

아래 Query List는 `Weekly IT Trend Sheet`에 사용하는 Query이다.
아래 순서와 표기를 strict하게 유지한다.

#### AI Agent

[AI Agent]
- AI Agent
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

#### AI

[AI]
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

#### Browser

[Browser]
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
- Microsoft Industry Blogs
- blog.google

### Global IT Trend Sheet Query

아래 Query List는 `Global IT Trend Sheet`에 사용하는 Query이다.
아래 순서와 표기를 strict하게 유지한다.

#### AI Agent

[AI Agent]
- AI Agent - Google Query
- OpenClaw (Moltbot, Clawdbot)
- Paperclip
- BabyAGI
- Microsoft AutoGen
- AutoGPT
- AgentGPT
- Claude Cowork
- A.(에이닷)
- KIRA
- Crack (크랙)
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

#### AI/GPT

[AI/GPT]
- AI - Google Query
- OpenAI
- ChatGPT
- Sora
- Codex
- Meta AI
- Google AI
- GeminI
- Amazon AI
- Nova AI
- Anthropic
- Claude
- Claude Code
- Kakao AI
- Microsoft AI
- Databricks
- Perplexity AI
- Cohere
- ElevenLabs
- Lovable
- Stability AI
- Inflection AI
- Ayar Labs
- Canva AI
- Speak AI
- Anysphere (Cursor)
- Physical Intelligence
- Thinking Machines Lab
- Moonshot AI
- Le Chat
- Leonardo AI
- Writer AI
- Zeta
- Kling AI
- Seedance
- Arc Browser
- Dia Browser
- Brave Browser
- Microsoft Edge
- Google Chrome
- Comet Browser
- Opera One
- Sigma Browser (SigmaOS)
- Zen Browser
- Wavebox
- Vivaldi Browser
- Safari
- Sidekick Browser
- Shift Browser
- Orion Browser
- Maxthon Browser
- Firefox
- Samsung Internet
- UC Browser
- CryptoTab Browser

#### Global Big Tech

[Global Big Tech]
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

#### Asia Big Tech

[Asia Big Tech]
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

#### Social

[Social]
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

#### Theme

[Theme]
- Super App (LinkedIn, Reddit, Spotify, VSCO, Paypal)
- MZ Gen - Google Query
- Gen Z - Google Query
- 1020 trend - Google Query
- Social app - Google Query
- Tech Crunch Startup

## Query와 우선 확인 링크 연결 방식

- Query List의 각 항목은 먼저 `Google Query 전 우선 확인 링크`에 동일하거나 유사한 항목이 있는지 확인한다.
- 동일한 이름의 공식 링크가 있으면 해당 링크를 1차 확인한다.
- 이름이 약간 다른 경우에도 같은 서비스로 판단 가능한 경우 연결한다.
  - 예: `Stability AI` ↔ `Stability.ai`
  - 예: `Comet Browser` ↔ `Comet`
  - 예: `Microsoft AI` ↔ `Microsoft`
  - 예: `Kakao AI` ↔ `Kakao Brain / Kakao AI`
  - 예: `Crack (크랙)` ↔ `Wrtn Crack`
- 단, Sheet Query 표기는 변경하지 않는다.
- 공식 링크가 없는 Query는 Google Query로 검색한다.
- Query List에 없는 링크 항목은 링크 목록에는 유지할 수 있지만, 해당 시트의 Query 배열에는 임의로 추가하지 않는다.

## Query별 Sheet 입력 방식

- Sheet는 대분류 → Query / Service → 기사 리스트 순서로 입력한다.
- 대분류와 Query / Service 순서는 해당 시트의 Query List 순서를 strict하게 따른다.
- 기사 입력 시 Query / Service 순서를 바꾸지 않는다.
- 기사 발견 Query와 최종 배치 Query는 다를 수 있다.
- 최종 배치 Query는 검색된 위치가 아니라 기사 핵심 내용과 기존 Query List 매칭 여부를 기준으로 결정한다.
- AI Agent 관련 기사라도 AI Agent 구역 내 세부 Query와 직접 매칭되면 해당 세부 Query에 입력한다.
- AI Agent 관련 기사이지만 AI Agent 구역 내 세부 Query와 직접 매칭되지 않는 경우에만 `AI Agent > AI Agent` 기본 Query에 입력한다.
- 회사명 Query와 AI Agent Query가 동시에 해당될 경우, 먼저 AI Agent 세부 Query 매칭 여부를 확인하고, 세부 Query가 없을 때만 `AI Agent > AI Agent`로 배치한다.
- 단순히 AI Agent가 홍보 문구로 언급된 기사나 실제 autonomous task, tool-use, workflow automation 기능이 없는 기사는 AI Agent 구역으로 이동하지 않는다.
- 특정 Query에서 기사가 여러 개 발견되면 해당 Query 아래에 여러 행으로 입력한다.
- 특정 Query에서 해당 기간 기사가 없으면 `n/a`를 입력한다.
- Query를 찾지 못했다고 임의로 삭제하지 않는다.
- Query List에 없는 기사를 발견한 경우:
  - Weekly IT Trend Sheet에서는 관련 Query 아래에 배치 가능한 경우에만 입력한다.
  - Global IT Trend Sheet에서는 해당 카테고리와 가장 가까운 Query 아래에 배치한다.
  - 어디에도 배치하기 어려우면 작업자 검토 대상으로 별도 보류하지 말고 입력하지 않는다.

## Query별 검색 결과 정리 방식

Query에서 발견한 기사는 반드시 아래 순서로 확인한다.

1. 작업 대상 시트가 Weekly IT Trend Sheet인지 Global IT Trend Sheet인지 확인
2. 해당 시트의 Query List 순서와 표기 확인
3. 날짜 범위 적합 여부 확인
4. 기사 원문 접근 가능 여부 확인
5. Paywall 여부 확인
6. 영어 URL 또는 공식 링크 존재 여부 확인
7. 과거 동일 기사 또는 동일 이슈 사용 여부 확인
8. 동일 이벤트 기사 Cluster 처리
9. 대표 URL과 보조 출처 URL 판단
10. Naver, LINE, LY Corporation 단독 기사 여부 확인
11. Sheet 구조에 맞춰 `대분류`, `Query / Service`, `Korean Title`, `Check Box`, `URL` 입력
12. 기사 없음이 확인된 Query / Service는 `n/a` 입력

## 최종 검수 체크리스트

- [ ] run_mode가 `weekly` 또는 `global` 중 하나로 지정되었는지 확인
- [ ] run_mode에 맞는 Query List만 사용했는지 확인
- [ ] Weekly Query와 Global Query를 섞지 않았는지 확인
- [ ] 검색 기간이 `yyyy.m.d~yyyy.m.d` 형식인지 확인
- [ ] Sheet 출력 컬럼이 `대분류 / Query / Service / Korean Title / Check Box / URL`만 포함하는지 확인
- [ ] Original Title, Status, Note, Cluster ID 등 금지 컬럼이 없는지 확인
- [ ] Check Box가 기본 미체크 상태인지 확인
- [ ] `n/a`가 검색 완료 후 기사 없음에만 사용되었는지 확인
- [ ] 검색 실패가 `n/a`로 처리되지 않았는지 확인
- [ ] URL이 접속 가능하고 본문 확인 가능한지 확인
- [ ] Paywall URL이 최종 URL로 사용되지 않았는지 확인
- [ ] 중복 기사가 별도 행으로 반복 입력되지 않았는지 확인
- [ ] 보완 링크는 URL 셀 줄바꿈으로 정리되었는지 확인
- [ ] Korean Title이 `[회사명] 핵심 내용 (yyyy.m.d)` 형식인지 확인
- [ ] 날짜에 `/` 또는 0 padding이 없는지 확인
- [ ] Naver / LINE / LY Corporation 단독 기사가 제외되었는지 확인
- [ ] 실행 로그에 검색 실패, Paywall, 제외 기사 등이 기록되었는지 확인
- [ ] Weekly IT Trend Sheet Query와 Global IT Trend Sheet Query가 분리되어 있는지 확인
- [ ] Weekly Query 순서가 제공된 순서와 일치하는지 확인
- [ ] Global IT Trend Query 순서가 제공된 순서와 일치하는지 확인
- [ ] Query 표기가 임의로 변경되지 않았는지 확인
- [ ] `Wrtn Crack`과 `Crack (크랙)`의 시트별 표기가 구분되어 있는지 확인
- [ ] Weekly Sheet Query와 Global IT Trend Sheet Query가 합쳐져 있지 않은지 확인
- [ ] Query List에 없는 항목이 임의로 Query로 추가되지 않았는지 확인
- [ ] Global IT / AI / Big Tech / Asia Tech / Social / Market Trend 관련 기사를 중요도와 관계없이 모두 리스트업했는지 확인
- [ ] 각 Query 섹션 안에서 `시장 영향이 큰 기사 → 기업/서비스 변화 기사 → 일반 관련 기사 → 중복/보조 출처` 순서로 정렬했는지 확인
- [ ] 공식 Newsroom, Blog, Release Notes, Changelog, GitHub Release 중 제품·서비스·기능·시장 변화가 있는 항목을 누락하지 않았는지 확인
- [ ] 보완 가치가 있는 중복 URL은 URL 셀 줄바꿈으로 정리하고, 정보 가치가 낮은 중복은 실행 로그 기준으로 처리했는지 확인
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
- [ ] 동일 이벤트는 내부 중복 판단 기준으로 정리했는지 확인
- [ ] 대표 URL과 보완 URL이 URL 셀 줄바꿈 기준으로 정리되었는지 확인
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
- [ ] 날짜 형식이 문서 전체에서 `yyyy.m.d` 기준으로 통일되었는지 확인
- [ ] 이전 날짜 형식이나 0 padding 날짜 표현이 남아 있지 않은지 확인
- [ ] Cluster가 Sheet 컬럼이 아니라 내부 중복 판단 기준으로만 설명되어 있는지 확인
- [ ] 중복 기사 처리 섹션이 하나로 통합되었는지 확인
- [ ] 깨진 백틱이나 중간에 끊긴 문장이 없는지 확인
- [ ] 긴 링크 목록이 Appendix A로 이동되었는지 확인
- [ ] Official Source Map이 Appendix B로 이동되었는지 확인
- [ ] Source 우선순위 세부 기준이 Appendix C로 이동되었는지 확인
- [ ] Claude Code와 Claude Cowork 배치 기준이 혼동되지 않게 정리되었는지 확인
- [ ] AI Agent 기본 Query가 fallback Query로 설명되어 있는지 확인
- [ ] 최종 산출물에 Status/Note/Cluster ID 등 금지 컬럼이 포함되지 않았는지 확인
- [ ] Korean Title 내 신기능명 큰따옴표 적용 기준이 반영되었는지 확인
- [ ] public beta에만 큰따옴표를 붙이고 내부 테스트·비공개 테스트에는 붙이지 않는 기준이 반영되었는지 확인
- [ ] 기존 기능 업데이트·확대, 루머, 버튼명에는 큰따옴표를 붙이지 않는 기준이 반영되었는지 확인

## 최종 산출물

최종 산출물은 아래와 같다.

- 주차별 기사 리스트업 Sheet 탭
- Weekly IT Trend Sheet 결과
- Global IT Trend Sheet 결과
- 최종 Korean Title 리스트
- URL이 포함된 기사 후보 리스트
- 자동화 실행 로그

Sheet 본문에는 아래 컬럼만 포함한다.

- 대분류
- Query / Service
- Korean Title
- Check Box
- URL

Sheet 본문에는 아래 항목을 포함하지 않는다.

- Original Title
- Status
- Note
- Cluster ID
- AI Relevance
- Report Relevance
- Duplicate Check Keyword

중복 제외 기사, Paywall 대체 과정, 검색 실패 Query, 제외 기사 기록은 Sheet 본문이 아니라 자동화 실행 로그에 남긴다.

## 산출물 활용 방식

- AI/GPT 기사는 Weekly AI Trend Report 작성에 활용
- Global Big Tech, Asia Big Tech, Social, Theme 기사는 Global IT Trend Report 작성에 활용
- 대표 Korean Title과 URL은 최종 리포트 기사 후보로 활용
- 제외 기사와 중복 기사 기록은 Sheet 본문이 아니라 자동화 실행 로그에서 이후 중복 방지용으로 활용
- 최종 Korean Title은 리포트 작성 및 Sheet 정리 시 그대로 활용 가능

## Appendix A. Google Query 전 우선 확인 링크

Google Query를 실행하기 전에 아래 공식 링크, 블로그, 뉴스룸, GitHub, release notes, changelog를 우선 확인한다. 공식 링크에서 관련 기사를 먼저 수집한 뒤, 공식 링크가 없거나 추가 확인이 필요한 항목만 Google Query를 사용한다.

### 적용 순서

1. 1차: 아래 우선 확인 링크 검토
2. 2차: 공식 링크가 없거나 누락 가능성이 있는 항목 Google Query 실행
3. 3차: 공통 Tech / AI / Social Source 확인
4. 4차: 중복 제거, 제외 대상 필터링, AI 관련성 판단
5. 5차: 기사 리스트업 Sheet 입력

### 공통 Tech / AI / Social Source

[TechCrunch]

https://techcrunch.com/latest/

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

## Appendix B. Official Source Map

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

## Appendix C. Source 우선순위 세부 기준

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

## 수정 요약

- AI Agent 기사는 세부 Query 매칭 우선, 세부 Query가 없을 때만 AI Agent 기본 Query에 배치하는 기준 추가
- 자동화 실행 모드(`weekly`, `global`) 추가
- 자동화 입력값과 Output Schema 구체화
- 중복 기사 처리 방식 통합
- 검색 실패와 `n/a` 상태 구분
- 자동화 실행 로그 기준 추가
- URL 입력 및 검증 기준 보강
- Korean Title 자동 검증 기준 추가
- Query Source Mapping 예시 추가
- 긴 공식 링크 목록을 Appendix로 이동
- Sheet 금지 컬럼 기준 재정리
- 날짜 형식을 `yyyy.m.d` 기준으로 전체 통일
- 중복 / Cluster 관련 섹션을 중복 기사 처리 방식으로 통합
- Cluster를 Sheet 컬럼이 아닌 내부 중복 판단 기준으로 재정의
- 깨진 문장과 백틱 오류 수정
- 긴 링크 목록을 Appendix A로 이동
- Official Source Map을 Appendix B로 이동
- Source 우선순위 세부 기준을 Appendix C로 이동
- Claude Code / Claude Cowork 배치 기준 명확화
- AI Agent 기본 Query를 세부 Query 미매칭 시 사용하는 fallback Query로 명확화
- Korean Title 내 신기능명 큰따옴표 적용 기준 구체화
- 정식 릴리스, public beta, 공식 출시 예정 기능에는 큰따옴표 적용
- 내부 테스트, 비공개 테스트, 루머, 기존 기능 업데이트·확대, 버튼명에는 큰따옴표 미적용 기준 추가
- 최종 산출물 기준에서 금지 컬럼 재정리
