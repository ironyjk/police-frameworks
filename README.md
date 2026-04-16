# Police Frameworks

> A meta-router and collection of 17 evidence-based policing frameworks for Claude Code.

**Created by 최희철 (Choi Hee Chul)** — software engineer, member of the **경주경찰서 경찰발전협의회 (Gyeongju Police Station Police Development Council — a volunteer support organization)**. Built as a **reference resource for frontline Korean police officers**, not as an operational tool for the council itself. The council is a community support body; crime analysis and enforcement are the work of police officers.

**Police Frameworks** is to policing what [/think](https://github.com/) is to business strategy and [/howtotalk](https://github.com/) is to communication — an intelligence layer that helps police officers and supervisors select the right analytical tool for the situation.

You describe a situation (a hot spot, a difficult interview, a crisis call, a community complaint), and the meta-router selects the appropriate framework(s), sequences them, and walks you through application.

---

## What's Inside

### 4 Axes × 17 Frameworks

**Axis 1 — Problem Analysis & Prevention (7)**
- `sara` — SARA model (Scanning, Analysis, Response, Assessment)
- `crime-triangle` — Routine Activity Theory + Problem Analysis Triangle
- `scp` — **Situational Crime Prevention 25 Techniques** (Clarke) — all crime types
- `cpted` — Crime Prevention Through Environmental Design
- `hot-spots` — Hot Spots Policing (Sherman, Weisburd)
- `ilp` — Intelligence-Led Policing (Ratcliffe)
- `repeat-victimization` — **Repeat Victimization** (Farrell & Pease) — protect past victims

**Axis 2 — Investigation, Interview & Victim (3)**
- `peace-model` — PEACE investigative interviewing (UK College of Policing)
- `cognitive-interview` — Enhanced Cognitive Interview (Fisher & Geiselman)
- `trauma-informed` — **Trauma-Informed Policing** (SAMHSA 4R) — prevent secondary harm

**Axis 3 — Field Response & Crisis (2)**
- `bcsm` — Behavioral Change Stairway Model (FBI crisis negotiation)
- `icat` — Integrating Communications, Assessment, and Tactics (PERF de-escalation)

**Axis 4 — Legitimacy, Community & Recovery (5)**
- `procedural-justice` — Procedural Justice & Legitimacy (Tyler)
- `cop` — Community-Oriented Policing
- `restorative-justice` — **Restorative Justice Policing** (Zehr, Braithwaite) — repair over punishment
- `third-party` — **Third-Party Policing** (Mazerolle & Ransley) — leverage landlords, schools, platforms
- `broken-windows` — Broken Windows Theory (re-examined)

### Meta-Router
- `peel` — the orchestrator that routes situations to the right framework(s). Named after Sir Robert Peel (1829), founder of modern policing.

---

## Installation

**Easiest — just ask Claude Code to do it.**

In **Claude Desktop** (click the `</>` Code view in the sidebar, open any folder) or **Claude Code CLI**, paste:

> "Install this plugin for me: https://github.com/ironyjk/police-frameworks"

Claude will run `/plugin marketplace add ironyjk/police-frameworks` and `/plugin install police-frameworks@police-frameworks` for you. Approve permission prompts with "Allow" when asked.

**Requirements:** Claude **Pro** (~$20/mo) or **Max** (~$100/mo, recommended for real work). Plain `claude.ai` web chat or the sandboxed Cowork view cannot install skills — use Claude Desktop's Code view or Claude Code CLI.

<details>
<summary>Manual install (advanced)</summary>

```bash
# Clone the full toolkit
git clone https://github.com/ironyjk/police-frameworks.git ~/.claude/skills/police-frameworks

# Or use the install script
curl -sL https://raw.githubusercontent.com/ironyjk/police-frameworks/main/install.sh | bash
```

</details>

Each framework is a Claude Code Skill with its own `SKILL.md`. You can use them individually or through the `/peel` meta-router.

> **Why `/peel`?** Sir Robert Peel founded modern policing in 1829. His 9 Principles — especially Principle 7, *"the police are the public and the public are the police"* — are the philosophical root of procedural justice, community policing, and the legitimacy theory that underlies this entire toolkit. It also avoids the awkwardness of officers typing `/police` to refer to themselves.

---

## Usage

### Via the meta-router

```
/peel
situation: 경주시 성건동 ○○근린공원에서 야간 청소년 집단 음주·소란 민원이
           3개월째 반복되고 있습니다. 순찰 접근 시 흩어지고 이탈 시 복귀.
```

The router analyzes the signal (pattern-based problem, not single incident) and routes to **SARA + Crime Triangle + Hot Spots + CPTED + COP + Procedural Justice + Broken Windows (critical filter)**. See [docs/sample-test.md](docs/sample-test.md) for the full walkthrough.

### Direct framework invocation

```
/sara
problem: 경주역 주변 야간 취객 민원 반복
```

---

## Design Principles

1. **Evidence-based only.** Every framework here has peer-reviewed research or official doctrine backing it (FBI, UK College of Policing, PERF, Home Office).
2. **No coercive techniques.** We deliberately exclude the Reid technique and similar confession-pressure methods. The PEACE model is the modern, ethical alternative.
3. **Korean context first.** Examples, vocabulary, and application notes are written for Korean police (경찰청, 경찰서, 지구대, 파출소) — not just translated from Western doctrine.
4. **Legitimacy over efficiency.** Procedural justice research shows that *how* police act matters more than *what* they accomplish. This toolkit reflects that.

---

## Who this is for

**Primary users — frontline Korean police:**
- 지구대·파출소 — recurring complaint analysis, hot-spot patrol design
- 경찰서 생활안전계 / 여성청소년과 — structured problem-solving framework, procedural justice grounding
- 경찰서 범죄예방진단팀 — CPTED application, Crime Triangle analysis
- 경찰서 위기협상요원 — BCSM crisis negotiation reference
- 수사과 조사관 — PEACE and Cognitive Interview reference

**Who this is NOT for:**
- This is **not a tool for police development councils** (경찰발전협의회) to use directly. The council is a volunteer support body — crime analysis, investigation, and enforcement are police work, not the council's.
- The creator is a council member acting as an **software engineer contributing a reference resource**, not as a law enforcement practitioner.
- All frameworks should be validated against department policy, Korean law, and operational reality by qualified police personnel before application.

---

## License

MIT — see [LICENSE](LICENSE).

한국어 문서: [README.ko.md](README.ko.md)
