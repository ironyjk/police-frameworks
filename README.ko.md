# Police Frameworks (경찰 프레임워크 툴킷)

> Claude Code를 위한 19개 근거 기반(Evidence-Based) 경찰활동 프레임워크 메타 라우터

**작성자**: **최희철** — 소프트웨어 개발자 / **경주경찰서 경찰발전협의회 회원**
**만든 이유**: 한국 경찰 실무자에게 드리는 **참고 자료**. 경찰발전협의회는 봉사단체이며, 실제 범죄 분석·수사·집행은 경찰의 몫입니다. 이 프로젝트는 경발협이 쓰는 도구가 아니라, 경발협 회원인 소프트웨어 개발자가 해외 학술 프레임워크를 경찰 실무 맥락으로 정리해 **경찰관에게 드리는 참고 자료**입니다.

**Police Frameworks**는 경찰 실무에서 쓰이는 검증된 분석 도구들을 한곳에 모은 프로젝트입니다. `/think`가 경영 전략, `/howtotalk`가 의사소통을 위한 것이라면, 이 프로젝트는 일선 경찰관, 지구대장, 경찰서 생활안전계·여성청소년과·범죄예방진단팀을 위한 지능형 라우팅 계층입니다.

상황을 설명하면(반복되는 핫스팟, 까다로운 조사 면담, 위기 신고, 민원), 메타 라우터가 적합한 프레임워크(들)를 선택하고 순서를 잡아 적용 방법을 안내합니다.

---

## 왜 만들었나

한국 경찰 현장에는 뛰어난 실무 지식이 있지만, 이를 체계화한 분석 도구가 개별 경찰관의 머릿속에만 존재하는 경우가 많습니다. 한편 영미권에서는 40년 이상 축적된 POP(문제지향 경찰활동), 정보기반 경찰활동, 절차적 정의 연구가 있지만 한국어 자료가 적고 산재되어 있습니다.

이 프로젝트는:
- **학술/교리 자료를 한국 맥락에 맞게 재구성**합니다 (단순 번역이 아님)
- **강압적 기법(Reid 자백유도 등)은 배제**합니다 — 근거기반 비강압 기법(PEACE)만 수록
- **경찰 실무자(지구대·경찰서 각 과)가** 자료가 산재되어 생기는 접근 장벽 없이 프레임워크를 참고할 수 있도록 한 곳에 정리

> 작성자는 경찰 실무자가 아닌 소프트웨어 개발자입니다. 이 자료의 모든 내용은 소속 기관의 지침·법령·현장 판단과 결합하여 **경찰이 검증·적용**해야 합니다.

---

## 구성 (4개 축 × 19개 프레임워크)

### 축 1 — 문제 분석·예방 (7)

| 프레임워크 | 창시자 | 쓸 때 |
|---|---|---|
| [`sara`](sara/SKILL.md) | Goldstein, Eck & Spelman | 반복 민원/신고 분석 및 근본 해결 |
| [`crime-triangle`](crime-triangle/SKILL.md) | Cohen & Felson, Clarke & Eck | 범죄 발생 조건 분해(가해자-대상-장소) |
| [`scp`](scp/SKILL.md) | **Ronald Clarke** | **상황적 범죄예방 25기법 — 모든 범죄 유형에 기회 감소** |
| [`cpted`](cpted/SKILL.md) | Jeffery, Newman | 환경설계로 범죄기회 제거 |
| [`hot-spots`](hot-spots/SKILL.md) | Sherman, Weisburd | 범죄 집중 지점 기반 순찰 배치 |
| [`ilp`](ilp/SKILL.md) | Ratcliffe | 정보분석 → 의사결정 → 영향 |
| [`repeat-victimization`](repeat-victimization/SKILL.md) | **Farrell & Pease** | **반복 피해자 보호 — 한 번 당하면 또 당한다** |

### 축 2 — 조사·면담·피해자 (5)

| 프레임워크 | 창시자 | 쓸 때 |
|---|---|---|
| [`peace-model`](peace-model/SKILL.md) | 영국 경찰청 (1992) | 피의자/참고인 윤리적 조사면담 |
| [`cognitive-interview`](cognitive-interview/SKILL.md) | Fisher & Geiselman | 피해자/목격자 기억 인출 최대화 |
| [`trauma-informed`](trauma-informed/SKILL.md) | **SAMHSA** | **트라우마 인식 — 피해자 2차 가해 방지, 4R 원칙** |
| [`risk-assessment`](risk-assessment/SKILL.md) | **Campbell, SafeLives** | **피해자 위험성 평가 — DASH/DA, 가정폭력 살인 위험도** |
| [`nichd-protocol`](nichd-protocol/SKILL.md) | **Michael Lamb** | **NICHD 아동면담 — 3~14세 비유도적 면담 국제 표준** |

### 축 3 — 현장대응·위기 (2)

| 프레임워크 | 창시자 | 쓸 때 |
|---|---|---|
| [`bcsm`](bcsm/SKILL.md) | FBI (Vecchi, Van Hasselt) | 자살/인질/농성 등 위기협상 |
| [`icat`](icat/SKILL.md) | PERF (미국경찰연구포럼) | 단계적 대응, 디에스컬레이션 |

### 축 4 — 지역·정당성·회복 (5)

| 프레임워크 | 창시자 | 쓸 때 |
|---|---|---|
| [`procedural-justice`](procedural-justice/SKILL.md) | Tom Tyler | 경찰 신뢰·정당성 진단 및 개선 |
| [`cop`](cop/SKILL.md) | Goldstein, Trojanowicz | 지역사회 협력 치안 설계 |
| [`restorative-justice`](restorative-justice/SKILL.md) | **Zehr, Braithwaite** | **회복적 경찰활동 — 처벌 대신 피해 회복·대화** |
| [`third-party`](third-party/SKILL.md) | **Mazerolle & Ransley** | **제3자(건물주·학교·플랫폼) 통한 범죄기회 제거** |
| [`broken-windows`](broken-windows/SKILL.md) | Wilson & Kelling (비판적 재해석) | 무질서 대응의 함정 이해 |

### 메타 라우터
- [`peel`](peel/SKILL.md) — 상황 입력 → 프레임워크 선택/시퀀싱. Sir Robert Peel(1829)의 이름을 땄습니다.

> **왜 `/peel`인가?** 1829년 런던경찰청을 창설한 Robert Peel은 현대 경찰의 창시자입니다. 그의 9대 원칙(특히 제7원칙 *"경찰은 시민이고 시민은 경찰이다"*)은 이 툴킷의 절차적 정의·COP·정당성 이론의 뿌리입니다. 또한 경찰관이 `/police`를 쳐서 자기 자신을 호출하는 어색함을 피합니다.

---

## 설치

**가장 쉬운 방법 — Claude Code 에게 부탁하세요.**

**Claude Desktop** 을 여시고 사이드바의 `</>` Code 아이콘을 클릭해 Code 화면으로 전환, 아무 폴더나 하나 선택하신 다음 채팅창에 아래 한 줄을 붙여넣으세요 (Claude Code CLI 를 쓰시는 경우에도 동일):

> "https://github.com/ironyjk/police-frameworks 플러그인을 저한테 설치해 주세요."

Claude 가 `/plugin marketplace add ironyjk/police-frameworks` 와 `/plugin install police-frameworks@police-frameworks` 를 자동으로 실행해 12개 프레임워크와 `/peel` 메타 라우터를 한 번에 등록합니다. 설치 중 권한 팝업이 뜨면 **"허용"** 또는 **"한 번만 허용"** 을 클릭하세요.

**필수 조건:**
- **Claude Pro** (월 ~2.8만원) 또는 **Claude Max** (월 ~14만원, 실전용 권장) 구독
- Claude Desktop 앱 (`claude.com/download`) — 설치는 반드시 사이드바의 `</>` Code 화면에서 진행
- 일반 Chat 화면 또는 Cowork 샌드박스에서는 스킬 폴더가 읽기 전용이라 설치 불가

<details>
<summary>수동 설치 (고급 사용자)</summary>

```bash
# 전체 툴킷 클론
git clone https://github.com/ironyjk/police-frameworks.git ~/.claude/skills/police-frameworks

# 또는 install.sh 사용
curl -sL https://raw.githubusercontent.com/ironyjk/police-frameworks/main/install.sh | bash
```

</details>

각 프레임워크는 독립적인 Claude Code Skill입니다. 개별 호출하거나 `/peel` 메타 라우터를 통해 사용할 수 있습니다. 샘플 테스트는 [docs/sample-test.md](docs/sample-test.md)를 참조하세요.

---

## 사용 예시

### 메타 라우터 사용

```
/peel
situation: 경주시 성건동 ○○근린공원에서 야간 청소년 집단 음주·소란 민원이
           3개월째 반복되고 있습니다. 순찰 접근 시 흩어지고 이탈 시 복귀.
```

→ 라우터가 "반복 패턴 + 장소 집중 + 청소년 + 주민 분열 + 무관용 요구"로 판단하고
**SARA → Crime Triangle → Hot Spots → CPTED → COP → Procedural Justice + Broken Windows 비판 필터** 순서로 파이프라인을 구성합니다.
상세 walkthrough: [docs/sample-test.md](docs/sample-test.md)

### 개별 프레임워크 사용

```
/sara
problem: 경주역 주변 야간 취객 민원 반복
```

---

## 누구를 위한 도구인가

**주 사용자 — 경주 및 전국의 일선 경찰 실무자**
- **지구대·파출소**: 반복 민원 분석, 핫스팟 순찰 설계
- **경찰서 생활안전계 / 여성청소년과**: 구조화된 문제해결·절차적 정의 적용
- **경찰서 범죄예방진단팀**: CPTED 적용, Crime Triangle 분석
- **경찰서 위기협상요원**: BCSM 위기협상 참고
- **수사과 조사관**: PEACE 및 Cognitive Interview 참고

**이 도구가 아닌 것:**
- **경찰발전협의회가 직접 쓰는 도구가 아닙니다.** 경발협은 봉사·지원 단체이며, 범죄 분석·수사·집행은 경찰의 역할입니다.
- 작성자는 소프트웨어 개발자로서 참고 자료를 제공하는 것이지, 법 집행 권한이나 경찰 전문성을 가진 것이 아닙니다.
- 모든 프레임워크는 실제 적용 전에 소속 기관 정책·법령·현장 실정에 비추어 자격 있는 경찰관이 검증해야 합니다.

### 참고 활용 예시 (경찰 실무 관점)

**1. 반복 민원 안건 분석** — `sara`로 문제 정의 → `crime-triangle`로 원인 분해 → 개입 대안 도출. 단순 "순찰 강화" 결론에서 벗어나 환경·대상·가해자 측 개입 옵션 비교.

**2. 환경 안전 점검** — `cpted` 체크리스트로 사각지대·조명·시야·영역성 진단.

**3. 지역사회 신뢰 진단** — `procedural-justice` 4요소(발언권·중립성·존중·신뢰)로 사례 평가.

**4. 순찰 배치 설계** — `hot-spots` + `ilp`로 데이터 기반 배치 (KICS 데이터가 있어야 가능).

---

## 설계 원칙

1. **근거 기반만** — 수록된 모든 프레임워크는 동료심사 연구 또는 공식 교리(FBI, 영국 경찰청, PERF, 내무부)에 기반함
2. **강압 기법 배제** — Reid 기법 등 자백 유도형 기법은 의도적으로 제외. PEACE 모델이 윤리적 대안
3. **한국 맥락 우선** — 예시, 용어, 적용 노트는 단순 번역이 아닌 한국 경찰(경찰청, 경찰서, 지구대, 파출소) 맥락으로 재작성
4. **효율보다 정당성** — 절차적 정의 연구는 "경찰이 *어떻게* 행동하는가"가 "*무엇*을 달성하는가"보다 중요하다는 것을 보여줌. 이 툴킷은 그 원칙을 반영

---

## 면책 조항

이 프로젝트는 **학습·토의 도구**입니다. 실제 법집행 상황에서는 소속 기관의 지침, 훈령, 법령이 우선합니다. 위기 상황에서는 반드시 훈련된 협상관, 정신건강 전문가, 지휘부의 판단을 따라야 합니다.

---

## 기여

이 프로젝트는 경주경찰서 경찰발전협의회 회원인 소프트웨어 개발자(최희철)가 **경찰 실무자에게 드리는 참고 자료**로 시작되었습니다. 한국 경찰 현장에서 쓸만한 프레임워크 추가, 사례 개선, 한국 사례 반영, 번역 수정 등 경찰 실무자·연구자의 모든 기여를 환영합니다.

## 라이선스

MIT — [LICENSE](LICENSE) 참조
