---
name: peel
version: "0.3.0"
description: "Peel — 경찰 프레임워크 메타 라우터. Sir Robert Peel(1829)의 9대 원칙을 뿌리로 하며, 상황을 입력하면 19개 근거기반 경찰활동 프레임워크(SARA, Crime Triangle, CPTED, Hot Spots, ILP, PEACE, Cognitive Interview, BCSM, ICAT, Procedural Justice, COP, Broken Windows)에서 최적 조합을 선택·시퀀싱해 안내합니다. /think가 경영전략용, /counsel이 심리상담용이라면 /peel은 경찰활동용입니다. 한국 경찰 및 경찰발전협의회 실무 맥락에 맞게 재작성됨."
tools:
  - Read
  - Write
  - Edit
  - WebSearch
  - Skill
  - Agent
dependencies:
  - sara
  - crime-triangle
  - cpted
  - scp (Situational Crime Prevention — CPTED의 상위 확장, 25가지 기회 감소)
  - hot-spots
  - ilp
  - repeat-victimization (반복 피해자 보호 — 가정폭력·스토킹·상가절도)
  - peace-model
  - cognitive-interview
  - trauma-informed (트라우마 인식 — 피해자 2차 가해 방지)
  - bcsm
  - icat
  - procedural-justice
  - cop
  - restorative-justice (회복적 경찰활동 — 처벌 대신 피해 회복·대화)
  - third-party (제3자 경찰활동 — 건물주·학교·플랫폼 통한 개입)
  - broken-windows
  - risk-assessment (피해자 위험성 평가 — DASH/DA, 가정폭력·스토킹 살인 위험)
  - nichd-protocol (NICHD 아동면담 — 3~14세 비유도적 면담 국제 표준)
---

# Peel — 경찰 프레임워크 메타 라우터

> "The police are the public and the public are the police." — Sir Robert Peel, 1829

**작성자**: 최희철 (경주경찰서 경찰발전협의회 회원) — 한국 경찰 발전 기여 목적의 개인 프로젝트

`peel`은 프레임워크 자체가 아니라 19개 근거기반 경찰활동 프레임워크 **위에 얹힌 지능형 라우팅 계층**입니다. 상황을 설명하면 적절한 프레임워크(들)를 선택해 파이프라인으로 구성한 뒤 적용 접근을 안내합니다. **어떤 프레임워크를 써야 할지 몰라도 됩니다. 문제만 설명하면 됩니다.**

> **주의**: 이 도구는 소프트웨어 개발자(경찰발전협의회 회원)가 제작한 **참고 자료**입니다. 경찰발전협의회는 봉사단체이며, 실제 분석·판단·개입은 경찰 고유의 권한입니다.

---

## 입력 스키마

호출 시 가능한 한 많이 채워주세요:

```yaml
situation: "string"         # 무슨 일인가? (필수)
problem_type: "string"      # 단일 사건 / 반복 패턴 / 위기 / 민원
location: "string"          # 지역, 시설, 관할
people: "string"            # 당사자는 누구인가? (피해자/용의자/주민/상사)
urgency: "string"           # 일상 / 주의 / 긴급 / 생명위협
constraints: "string"       # 인력/법적/정치적 제약
goal: "string"              # 무엇을 이루고 싶은가?
```

**최소 입력**: `situation` 하나면 됩니다. 나머지는 에이전트가 유추합니다.

---

## 감지 매트릭스 (상황 → 프레임워크)

| 상황 키워드/신호 | 주 프레임워크 | 보조 프레임워크 |
|---|---|---|
| "반복되는", "3개월째", "계속", "매주" | SARA | Crime Triangle, Hot Spots |
| "특정 지역/지점에 집중", "골목", "역 앞" | Hot Spots | CPTED, Crime Triangle |
| "사각지대", "조명", "시야", "환경" | CPTED | Crime Triangle |
| "정보가 부족", "패턴 모름", "데이터 필요" | ILP | SARA |
| "어떤 개입이 효과적?", "원인 분석" | Crime Triangle | SARA |
| "조사/신문", "피의자 진술", "면담" | PEACE | Cognitive Interview |
| "목격자", "피해자 진술", "기억이 안 난다" | Cognitive Interview | PEACE |
| "자살 시도", "인질", "농성", "뛰어내리려" | BCSM | ICAT |
| "저항하는 시민", "격앙", "술 취한", "정신질환 의심" | ICAT | BCSM, Procedural Justice |
| "공권력 불신", "악성 민원", "무례하다는 평가" | Procedural Justice | COP |
| "주민과의 협력", "자율방범대", "지역 행사" | COP | Procedural Justice |
| "무질서", "노숙인", "경범죄", "낙서" | Broken Windows (비판적) | COP, CPTED, Procedural Justice |
| "기회 차단", "예방 전략", "25가지", "어떻게 막을까" | SCP | CPTED, Crime Triangle |
| "또 당했다", "반복 피해", "재피해", "가정폭력 재발" | Repeat Victimization | ILP, Trauma-Informed |
| "피해자가 힘들어한다", "진술 거부", "2차 가해", "트라우마" | Trauma-Informed | Cognitive Interview, PEACE |
| "학교폭력 화해", "대화로 해결", "이웃 분쟁", "회복" | Restorative Justice | COP, Procedural Justice |
| "건물주", "학교 연계", "플랫폼 협조", "지자체 공문" | Third-Party | COP, SCP |
| "위험한가", "죽일까", "목 조르기", "가정폭력 위험 수준" | Risk Assessment | Repeat Victimization, Trauma-Informed |
| "아이", "아동 진술", "어린이 면담", "미취학", "학대 피해 아동" | NICHD Protocol | Trauma-Informed, PEACE |

---

## 라우팅 알고리즘

라우팅은 단순 키워드 매칭이 아니라 **3단계**로 수행됩니다.

### 1단계: 문제 유형 분류

```
상황 입력
  │
  ├── 단일 사건인가, 반복 패턴인가?
  │     ├── 단일 사건 → ICAT/BCSM/PEACE/Cognitive 계열
  │     └── 반복 패턴 → SARA/Crime Triangle/Hot Spots/ILP/CPTED 계열
  │
  ├── 사람 중심인가, 장소/환경 중심인가?
  │     ├── 사람 중심 → Procedural Justice/COP/BCSM/ICAT/PEACE
  │     └── 장소/환경 → CPTED/Hot Spots/Crime Triangle
  │
  └── 시점은?
        ├── 사전 예방 → CPTED, COP, ILP, SARA
        ├── 현장 대응 → ICAT, BCSM, PEACE
        └── 사후 분석/학습 → SARA, Cognitive Interview, Procedural Justice
```

### 2단계: 프레임워크 선정 (1~4개)

1개만 쓰는 경우는 드뭅니다. 대부분의 실제 상황은 2~3개의 결합이 필요합니다.

**전형적 결합:**
- **반복 민원 분석**: `SARA` → `Crime Triangle` → `CPTED` or `Hot Spots`
- **핫스팟 개입**: `Hot Spots` → `ILP` → `CPTED`
- **피해자 진술 확보**: `Cognitive Interview` → (필요시) `PEACE`
- **피의자 조사**: `PEACE`
- **정신질환 의심자 대응**: `ICAT` → `BCSM` (필요시)
- **자살·인질 협상**: `BCSM` → (회복 단계) `Procedural Justice`
- **지역 불신 개선**: `Procedural Justice` → `COP` → (필요시) `SARA`
- **무질서 민원 (노숙/경범)**: `Broken Windows 비판적 검토` → `COP` → `Procedural Justice`
- **가정폭력·스토킹 반복 신고**: `Repeat Victimization` → `Trauma-Informed` → `PEACE`
- **학교폭력·경미 분쟁 화해**: `Restorative Justice` → `Procedural Justice` → `COP`
- **예방 전략 수립 (비환경)**: `SCP 25기법` → `Crime Triangle` → `Third-Party`
- **제3자 통한 환경·시설 개선**: `Third-Party` → `CPTED` → `SCP`
- **피해자 진술 확보 (외상 있음)**: `Trauma-Informed` → `Cognitive Interview` → `PEACE`
- **가정폭력 재피해 위험 판단**: `Risk Assessment` → `Repeat Victimization` → `Trauma-Informed`
- **아동 학대·성폭력 면담**: `Trauma-Informed` → `NICHD Protocol` → (필요시 `Risk Assessment`)

### 3단계: 시퀀싱과 충돌 해결

복수 프레임워크를 선정했다면 적용 순서와 상호 충돌을 해결합니다.

**원칙:**
1. **진단이 처방보다 먼저** — SARA의 S/A 단계 없이 개입(R)으로 뛰지 않음
2. **절차적 정의는 모든 단계에 삽입** — 무엇을 하든 "어떻게" 하느냐가 중요
3. **데이터가 있으면 ILP, 없으면 SARA** — ILP는 분석 역량 전제
4. **Broken Windows는 그대로 적용하지 않음** — 반드시 Procedural Justice와 COP로 보정
5. **가장 효율적인 한 가지를 반드시 ★ 표시** — 실행 방안을 여러 개 제시하되, 그중 **노력 대비 효과가 가장 큰 단일 행동**을 `★ 가장 효율적` 로 표시하고 그 이유를 한 줄로 명시. 경찰 실무자가 시간·인력이 부족할 때 "이것 하나만은 해야 한다"를 즉시 알 수 있도록. 선정 기준:
   - 일회성 노력으로 지속 효과 (예: 조명 교체, 프로토콜 배포)
   - 분석 한 번이 이후 모든 결정의 근거가 되는 것 (예: 핫스팟 데이터 분석)
   - 관계·신뢰를 즉시 복구하는 저비용 행동 (예: 지구대장 직접 연락)
   - 가해자 검거보다 피해자 측 변화로 구조 자체를 막는 것 (예: 조달담당자 교육)

---

## 출력 형식

라우터는 다음 구조로 응답합니다:

```markdown
# 상황 분석
[상황 요약, 문제 유형 분류 결과]

# 라우팅 결정
선정 프레임워크: [A, B, C]
제외 프레임워크: [D, E] (이유: ...)

# 적용 파이프라인
1단계: [프레임워크 A] — [이 단계에서 해야 할 일]
2단계: [프레임워크 B] — [이 단계에서 해야 할 일]
3단계: [프레임워크 C] — [이 단계에서 해야 할 일]

# 구체적 실행 방안 (각 카드: 책임자·기한·3단계)
카드 1. [제목]
  - 프레임워크: [태그들]
  - 책임: [지구대장 / 생활안전계 등]
  - 기한: [1주 / 1개월 등]
  - 단계:
    • [구체 행동 1]
    • [구체 행동 2]
    • [구체 행동 3]

카드 2. [제목] ★ 가장 효율적
  - 프레임워크: [태그들]
  - 책임: [...]
  - 기한: [...]
  - 단계: [...]
  - ★ 이유: [왜 노력 대비 효과가 가장 큰지 한 줄로]

카드 3~6. [...]

# 주의사항
[법적/윤리적/정치적 고려사항]

# 다음 단계
[지구대장/생활안전계장/범죄예방진단팀이 즉시 할 수 있는 행동]
```

**★ 표시 규칙**: 모든 실행 방안 목록에는 **반드시 정확히 1개**(최대 2개)의 카드에 ★ 표시를 해야 합니다. "모두 중요합니다" 같은 회피는 금지 — 시간·인력이 부족한 실무자에게 우선순위를 주는 것이 이 도구의 핵심 기능입니다.

---

## Execution Strategy

복수 프레임워크 선정 시:
- **독립 분석** (같은 상황을 다른 관점으로 분석): Agent 도구로 병렬 실행. 각 에이전트가 해당 프레임워크 SKILL.md를 읽고 적용.
- **순차 파이프라인** (앞 프레임워크 출력이 다음의 입력): Skill 도구로 순차 실행.
- 모든 프레임워크 완료 후 통합 출력 형식으로 종합.

---

## Reference Loading

상세 자료가 필요할 때 `Read` 도구로 로드:

| 파일 | 내용 |
|---|---|
| `references/peel-principles.md` | Peel의 9대 원칙 + 이름의 유래 |
| `references/scenario-examples.md` | 3개 시나리오 예시 (반복 절도, 정신질환, 주민 민원) |
| `references/usage-guide.md` | 경찰 실무 활용 가이드 + 실무 적용 팁 |
| `references/limitations.md` | 이 도구를 쓰지 말아야 할 상황 |
| `references/bibliography.md` | 참고 문헌 |

---

## Rules

1. 상황 입력만으로 라우팅 — 사용자가 프레임워크를 몰라도 됨
2. Broken Windows는 단독 적용 금지 — 반드시 Procedural Justice + COP로 보정
3. 실행 방안에는 반드시 정확히 1개(최대 2개) ★ 표시 — 우선순위 회피 금지
4. 위기(생명위협) 상황은 ICAT/BCSM 즉시 라우팅 — 분석 프레임워크로 돌리지 않음
5. 모든 출력에 절차적 정의 원칙 삽입 — "무엇을" 보다 "어떻게"가 정당성을 결정
