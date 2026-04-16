---
name: peel
version: "0.2.0"
description: "Peel — 경찰 프레임워크 메타 라우터. Sir Robert Peel(1829)의 9대 원칙을 뿌리로 하며, 상황을 입력하면 19개 근거기반 경찰활동 프레임워크(SARA, Crime Triangle, CPTED, Hot Spots, ILP, PEACE, Cognitive Interview, BCSM, ICAT, Procedural Justice, COP, Broken Windows)에서 최적 조합을 선택·시퀀싱해 안내합니다. /think가 경영전략용, /counsel이 심리상담용이라면 /peel은 경찰활동용입니다. 한국 경찰 및 경찰발전협의회 실무 맥락에 맞게 재작성됨."
tools:
  - Read
  - Write
  - Edit
  - WebSearch
  - Skill
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

## 왜 이름이 /peel 인가

1829년 영국 런던경찰청(Metropolitan Police)을 창설한 Sir Robert Peel은 **현대 경찰의 창시자**로 불립니다. 그의 9대 원칙(Peelian Principles)은 200년이 지난 지금도 절차적 정의·지역사회 경찰활동·정당성 이론의 뿌리입니다.

경찰관이 자기 자신을 "경찰"이라고 호출하는 것은 어색합니다. `/peel`은 이 툴킷의 철학적 기원이자, 자기지시어를 피한 호출어입니다. 그리고 이 툴킷 안의 절차적 정의, COP, Broken Windows 재해석, PEACE, ICAT 모두 결국 Peel의 제7원칙 — **"경찰은 시민이고 시민은 경찰이다"** — 로 수렴합니다.

### Peel의 9대 원칙 (1829)

1. 경찰의 기본 임무는 범죄와 무질서의 **예방**이다 — 무력 진압이 아니다
2. 경찰의 권위는 시민의 **승인·협력·존경**에 기반한다
3. 시민 협력 확보는 경찰이 물리력을 쓸 필요를 줄인다
4. 협력의 정도는 경찰이 시민권을 얼마나 존중하느냐에 달렸다
5. 여론에 영합하지 않고 **일관되고 공평한 법 집행**으로 승인을 얻는다
6. 물리력은 설득·조언·경고가 실패한 경우에만, **최소한으로**
7. **경찰은 시민이고 시민은 경찰이다** — 경찰은 시민의 대리인일 뿐
8. 경찰은 법 집행자이지 재판관이 아니다
9. 경찰 효율성의 척도는 **범죄 발생의 부재**이지 가시적 경찰 활동이 아니다

---

## 이것이 무엇인가

`peel`은 프레임워크 자체가 아닙니다. 19개 근거기반 경찰활동 프레임워크 **위에 얹힌 지능형 라우팅 계층**입니다.

일선 경찰관, 지구대장, 경찰서 생활안전계·여성청소년과·범죄예방진단팀이 상황을 설명하면 — 반복 민원, 핫스팟 의심 지역, 까다로운 조사 면담, 자살 시도 신고, 지역 불신 문제 — 이 에이전트가 상황을 분석하고 적절한 프레임워크(들)를 선택해 파이프라인으로 구성한 뒤 적용 접근을 안내합니다.

> **주의**: 이 도구는 소프트웨어 개발자(경주경찰서 경찰발전협의회 회원 최희철)가 제작한 **참고 자료**입니다. 경찰발전협의회는 봉사단체이며, 이 도구 역시 경발협 자체 활동 도구가 아니라 경찰 실무자에게 드리는 참고용입니다. 실제 분석·판단·개입은 경찰 고유의 권한이며, 이 라우터 출력은 경찰의 의사결정을 대체하지 않습니다.

**어떤 프레임워크를 써야 할지 몰라도 됩니다. 문제만 설명하면 됩니다.**

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

## 시나리오 예시

### 예시 1 — 반복 절도 민원

**입력:**
```
situation: 경주시 외동읍 산업단지 공장 주차장에서 새벽 시간대 차량 내 물품 절도 신고가
지난 3개월간 12건 접수됨. 지금까지 순찰 강화 외에는 뚜렷한 대책 없음.
reporter: 외동파출소 / 경주경찰서 생활안전계
urgency: 주의
goal: 장기적으로 재발 방지
```

**라우터 응답:**
```
# 문제 유형
반복 패턴(3개월, 12건) + 장소 집중(산업단지 주차장) + 사전 예방 필요
→ 축 1(문제지향 경찰활동)

# 선정
SARA → Crime Triangle → Hot Spots → CPTED
제외: BCSM, ICAT (위기 아님) / PEACE, Cognitive (조사 단계 아님)

# 파이프라인
1. SARA-Scanning: 12건 신고 데이터 정리, 시공간 분포 확인
2. SARA-Analysis + Crime Triangle: 가해자/대상/장소 3요소 분해
   - 가해자: 누구? 조직? 유동적?
   - 대상: 어떤 차량? 어떤 물품? 공통점?
   - 장소: 특정 구역? 조명/시야/출입 통제?
3. Hot Spots: 12건을 지도 위에 점찍어 집중도 확인
4. CPTED 체크리스트:
   - 자연감시(조명, 시야) 가능한가?
   - 접근통제(차단기, 출입구) 있는가?
   - 영역성(경고판, 구역 표시) 명확한가?
   - 활동지원(CCTV, 주기적 인원) 있는가?
5. SARA-Response: 위 3요소 중 가장 저렴·효과적 개입 선택
6. SARA-Assessment: 3개월 뒤 신고 건수 재측정

# 구체적 실행 방안
카드 1. SARA + Crime Triangle 진단 TF
  - 책임: 외동파출소 + 범죄예방진단팀
  - 기한: 1주
  - 단계: KICS로 12건 추출 / 6박스 분해 / 지도화
카드 2. Hot Spots 새벽 집중 순찰
  - 책임: 외동파출소
  - 기한: 2주
  - 단계: 상위 핫스팟 특정 / Koper 15분 룰 / 로그 공유
카드 3. CPTED 합동 현장 점검 ★ 가장 효율적
  - 책임: 경주서 범죄예방진단팀 + 단지 관리공단
  - 기한: 1개월
  - 단계: 조명·CCTV·차단기 점검 / 사각지대 매핑 / 개선 우선순위
  - ★ 이유: 점검 한 번의 결과가 이후 모든 개선 공사의 근거가 되고, 환경이 바뀌면 순찰 빠져도 범죄가 줄어들어 가장 지속가능한 개입.
카드 4. COP 관리공단·기업 협력
  - 책임: 외동파출소장
  - 기한: 2주
  - 단계: MOU 추진 / 방범 담당자 연락망 / 월 브리핑
카드 5. 환경 개선 예산 확보
  - 책임: 경주서 생활안전과
  - 기한: 2개월
  - 단계: 견적 확보 / 예산 협의 / 시공 일정
카드 6. SARA Assessment 3개월 재측정
  - 책임: 생활안전계
  - 기한: 3개월 후
  - 단계: 신고·피해액 재측정 / 이동 확인 / 사이클 재시작 판단

# 주의
- "순찰 강화" 결론으로 직행하지 말 것 — CPTED 개입이 장기적으로 우월할 수 있음
- 절차적 정의: 주차장 관리주체·이용자에게 왜 이런 조치를 하는지 설명
```

### 예시 2 — 정신질환 의심자 112 신고

**입력:**
```
situation: 아파트 복도에서 50대 남성이 소리 지르며 자해 위협. 가족이 112 신고.
urgency: 생명위협
```

**라우터 응답:**
```
# 문제 유형
단일 사건 + 현장 대응 + 정신건강 요소
→ 축 3(현장 대응/위기)

# 선정
ICAT → (필요시) BCSM
제외: 반복 패턴 프레임워크 전부 (지금 이 순간 대응해야 함)

# 파이프라인
1. ICAT 개요 적용:
   - Critical Decision-Making Model: Collect info → Threat assessment → Authority → Goal → Options → Action → Review
   - 위해 요소: 칼/무기 소지 여부, 공간 폐쇄성, 가족/시민 근접도
   - 물리력 사용 피할 수 있는 옵션 우선
2. 시간을 만들어라 (Time, Distance, Cover)
   - 물러서고, 공간 확보하고, 엄폐
3. 대화 개시: 이름 묻기, 경청, 판단 금지
4. 필요시 BCSM 진입:
   - Active Listening → Empathy → Rapport → Influence → Behavioral Change
   - 첫 30분은 거의 듣기만 — 말로 설득하려 들지 말 것
5. 정신건강 전문가·구급대 조기 요청

# 주의
- 물리적 제압은 최후의 수단 — ICAT의 핵심 메시지
- 모든 대응은 절차적 정의 원칙 삽입: 설명, 존중, 투명성
- 상급자/협상관 도착 전까지 상황 안정화가 목표 (해결이 아님)
```

### 예시 3 — 주민이 "경찰이 무례하다"고 민원

**입력:**
```
situation: 지구대에서 주취자 처리 후 주민이 "경찰이 고압적이고 설명도 없었다"고 민원 제기. 
내부적으로는 규정대로 처리했다는 입장.
goal: 재발 방지, 지역 신뢰 회복
```

**라우터 응답:**
```
# 문제 유형
사후 분석 + 정당성/신뢰 문제
→ 축 4(정당성·지역사회)

# 선정
Procedural Justice → COP → (필요시) SARA(재발 방지 차원)
제외: 현장 대응 프레임워크 (이미 종결)

# 파이프라인
1. Procedural Justice 4요소로 사건 분석:
   - Voice (발언권): 주민이 말할 기회를 충분히 받았나?
   - Neutrality (중립성): 설명과 근거가 투명했나?
   - Respect (존중): 언어와 태도가 존엄을 침해하지 않았나?
   - Trustworthiness (신뢰): 경찰이 선의로 행동한다는 인상을 주었나?
2. 핵심 통찰: "규정대로 처리"했더라도 4요소 중 하나라도 미흡하면 신뢰는 훼손됨
   — 절차적 정의 연구의 핵심: 결과보다 과정의 체감이 정당성을 좌우함
3. COP 차원의 후속:
   - 지구대장이 직접 주민 방문/연락
   - 민원 처리 절차 설명 및 사과(필요시)
   - 지역 협의체에 사례 공유
4. SARA로 구조적 재발 방지:
   - 해당 유형 민원의 빈도 확인
   - 교육/절차/기록 체계 점검

# 주의
- "규정대로" 방어 논리는 정당성 문제에서 역효과
- 민원인이 "졌다"는 느낌이 들지 않도록 해야 장기적 신뢰 회복 가능
```

---

## 경찰 실무 활용 가이드

지구대·경찰서 실무자가 이 라우터를 쓸 수 있는 전형적 상황과 권장 프레임워크 조합:

| 실무 상황 | 권장 파이프라인 |
|---|---|
| 특정 지역 반복 민원·치안 우려 | SARA → Crime Triangle → Hot Spots → CPTED |
| 종결 민원 사후 분석 | SARA → Procedural Justice(사후) → COP |
| 주민·지역 협력 사업 설계 | COP → Procedural Justice → (SARA로 효과 추적) |
| 경찰 신뢰도 개선 | Procedural Justice → COP → ILP(데이터 수집) |
| 환경 개선 필요 지역 | CPTED → Crime Triangle → 행정 협조 |
| 경범죄·무질서 민원 | Broken Windows 비판적 검토 → COP → Procedural Justice |
| 순찰 배치 재설계 | Hot Spots → ILP → CPTED |
| 피해자 진술 확보 | Cognitive Interview → PEACE |
| 피의자 조사 | PEACE (+전략적 증거 사용) |
| 정신건강 위기 현장 | ICAT → (필요 시) BCSM |

**실무 적용 팁:**
1. 사건 분석 시작 전 라우터를 돌려 권장 프레임워크를 미리 선정
2. 토의 시 프레임워크 체크리스트를 프로젝터에 띄우고 항목별 의견 수렴
3. "느낌" 발언 대신 프레임워크 항목에 대한 답변으로 정리
4. 결론은 프레임워크가 제시하는 다음 단계 형태로 기록

---

## 언제 이 도구를 쓰지 말아야 하나

- **실제 위기 현장**에서 휴대폰 켜고 이 문서를 읽지 마세요. 훈련과 기관 지침이 우선합니다.
- **법적 판단**이 필요한 경우 — 변호사·법무관·감찰과 상의하세요.
- **정신건강 위기**에서 단독 대응 — 반드시 정신건강 전문가/위기개입팀 요청
- **강압/불법적 목적** — 이 툴킷은 거부합니다. 절차적 정의와 인권이 모든 프레임워크의 전제조건입니다.

---

## 참고 문헌 (요약)

각 프레임워크의 상세 출처는 해당 `SKILL.md` 참조. 핵심 문헌만 여기 요약:

- Goldstein, H. (1979). *Improving Policing: A Problem-Oriented Approach*
- Eck, J. & Spelman, W. (1987). *Problem Solving: Problem-Oriented Policing in Newport News*
- Sherman, L. (1989). *Hot Spots of Predatory Crime*
- Tyler, T. (1990). *Why People Obey the Law*
- Ratcliffe, J. (2016). *Intelligence-Led Policing* (2nd ed.)
- Fisher, R. & Geiselman, E. (1992). *Memory-Enhancing Techniques for Investigative Interviewing*
- UK Home Office (1992). *PEACE Model of Investigative Interviewing*
- PERF (2016). *ICAT: Integrating Communications, Assessment, and Tactics*
- Vecchi, G., Van Hasselt, V., & Romano, S. (2005). *Crisis (Hostage) Negotiation: Current Strategies and Issues*
- Wilson, J. & Kelling, G. (1982). *Broken Windows* (비판적 재해석 필수)
