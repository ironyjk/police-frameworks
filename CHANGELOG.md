# Changelog

모든 주요 변경사항을 기록합니다.

## [0.3.0] — 2026-04-16

### 추가
- **회복적 경찰활동** (`restorative-justice`) — Zehr, Braithwaite. 처벌 대신 피해 회복·관계 복원. 한국 경찰청 2019년 공식 추진. 학교폭력·이웃 분쟁·경미 사건 대상.
- **상황적 범죄예방 SCP 25기법** (`scp`) — Clarke. CPTED의 상위 확장. 5범주 × 5기법 = 25가지 기회 감소. 사기·사이버·약물 등 장소 독립 범죄까지.
- **반복 피해자 이론** (`repeat-victimization`) — Farrell & Pease. 재피해 확률 4~8배. Flag(취약특성) vs Boost(가해자 재방문). 코쿤 워치. ILP의 대칭 축.
- **트라우마 인식 경찰활동** (`trauma-informed`) — SAMHSA 4R. 피해자 첫 접촉의 태도가 장기 회복 분기점. "왜 도망 안 갔어요?" 금기 목록.
- **제3자 경찰활동** (`third-party`) — Mazerolle & Ransley. 건물주·학교·플랫폼의 법적 의무로 범죄 기회 제거. 에스컬레이션 4단계.

### 변경
- 총 프레임워크 수: 12 → **17**
- peel 메타 라우터: 감지 매트릭스 6행, 라우팅 조합 6개 추가
- PPT 슬라이드 19: "12개 공구" → "17개 공구"
- README 한/영: 프레임워크 테이블 전면 업데이트

## [0.2.0] — 2026-04-16

### 추가
- **거래처 사칭 사기 사례** (PPT 사례 5) — SARA → ILP → Crime Triangle → COP → Cognitive → PEACE 6단계 파이프라인
- **★ 가장 효율적 강조 시스템** — peel 라우터 원칙 #5. 실행 방안 목록에서 노력 대비 효과 최고 1개를 반드시 ★ 표시
- **Claude Desktop `</>` Code 화면 설치 가이드** — 사이드바 스크린샷 + 빨간 원 강조 + 권한 허용 안내
- `.claude-plugin/marketplace.json` — Anthropic 공식 플러그인 마켓플레이스 등록
- ComfyUI Flux Schnell 이미지 생성기 (`scripts/generate_ppt_images.py`) — 8장 일러스트

### 변경
- PPT 15장 → 22장 → **27장** (사례당 3장: 상황/분석/실행방안)
- 설치 경로: zip 업로드 → Claude Desktop `</>` Code 화면에서 링크 전달 방식으로 변경
- "AI 전문가" → "소프트웨어 개발자" (모든 문서)
- "60대" → "비전문가" (PPT)
- Claude Pro/Max 구독 필수 안내 배너 추가 (슬라이드 24)

### 보안
- `docs/intro.pptx`, `docs/intro.pdf`, `docs/gyeongju-hotspots.md`, `docs/images/` 를 git history에서 완전 제거 (`git filter-repo`)
- `.gitignore`에 배포물·내부 참고자료·이미지 경로 추가

## [0.1.0] — 2026-04-15

### 초기 릴리스
- **12개 근거기반 경찰활동 프레임워크** + `/peel` 메타 라우터
- 4개 축: 문제지향 / 조사면담 / 현장대응 / 정당성·지역사회
- 한국 경찰(경찰청, 경찰서, 지구대, 파출소) 실무 맥락에 맞게 재작성
- Reid 기법 등 강압적 기법 의도적 배제
- Sir Robert Peel 9대 원칙을 라우터 이름(`/peel`)과 철학의 뿌리로
- `docs/sample-test.md` — 경주시 성건동 시나리오 시뮬레이션
- MIT 라이선스
- 작성자: 최희철 (Choi Hee Chul) — 경주경찰서 경찰발전협의회 회원, 소프트웨어 개발자

## 버전 체계

- **Major (X.0.0)**: 구조 변경, 축 재편, 라우팅 알고리즘 대폭 수정
- **Minor (0.X.0)**: 프레임워크 추가/삭제, 주요 기능 변경
- **Patch (0.0.X)**: 오탈자, 참고 문헌 추가, 사례 보강
