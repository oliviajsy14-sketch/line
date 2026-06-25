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
