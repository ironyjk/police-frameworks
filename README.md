# Police Frameworks

> A meta-router and collection of 12 evidence-based policing frameworks for Claude Code.

**Created by 최희철 (Choi Hee-cheol)**, member of the **경주경찰서 경찰발전협의회 (Gyeongju Police Station Police Development Council)**, as a contribution to the advancement of Korean policing.

**Police Frameworks** is to policing what [/think](https://github.com/) is to business strategy and [/howtotalk](https://github.com/) is to communication — an intelligence layer that helps officers, supervisors, and police councils select the right analytical tool for the situation.

You describe a situation (a hot spot, a difficult interview, a crisis call, a community complaint), and the meta-router selects the appropriate framework(s), sequences them, and walks you through application.

---

## What's Inside

### 4 Axes × 12 Frameworks

**Axis 1 — Problem-Oriented Policing**
- `sara` — SARA model (Scanning, Analysis, Response, Assessment)
- `crime-triangle` — Routine Activity Theory + Problem Analysis Triangle
- `cpted` — Crime Prevention Through Environmental Design
- `hot-spots` — Hot Spots Policing (Sherman, Weisburd)
- `ilp` — Intelligence-Led Policing (Ratcliffe)

**Axis 2 — Investigation & Interview**
- `peace-model` — PEACE investigative interviewing (UK College of Policing)
- `cognitive-interview` — Enhanced Cognitive Interview (Fisher & Geiselman)

**Axis 3 — Field Response & Crisis**
- `bcsm` — Behavioral Change Stairway Model (FBI crisis negotiation)
- `icat` — Integrating Communications, Assessment, and Tactics (PERF de-escalation)

**Axis 4 — Legitimacy & Community**
- `procedural-justice` — Procedural Justice & Legitimacy (Tyler)
- `cop` — Community-Oriented Policing
- `broken-windows` — Broken Windows Theory (re-examined)

### Meta-Router
- `peel` — the orchestrator that routes situations to the right framework(s). Named after Sir Robert Peel (1829), founder of modern policing.

---

## Installation

```bash
# Clone the full toolkit
git clone https://github.com/ironyjk/peel-frameworks.git ~/.claude/skills/peel-frameworks

# Or use the install script
curl -sL https://raw.githubusercontent.com/ironyjk/peel-frameworks/main/install.sh | bash
```

Each framework is a Claude Code Skill with its own `SKILL.md`. You can use them individually or through the `/peel` meta-router.

> **Why `/peel`?** Sir Robert Peel founded modern policing in 1829. His 9 Principles — especially Principle 7, *"the police are the public and the public are the police"* — are the philosophical root of procedural justice, community policing, and the legitimacy theory that underlies this entire toolkit. It also avoids the awkwardness of officers typing `/police` to refer to themselves.

---

## Usage

### Via the meta-router

```
/peel
situation: 이천 산업단지에서 새벽 시간대 절도 신고가 3개월째 증가 중입니다.
```

The router analyzes the signal (pattern-based problem, not single incident) and routes to **SARA + Crime Triangle + Hot Spots + CPTED**.

### Direct framework invocation

```
/sara
problem: 역 앞 노숙인 관련 민원 반복
```

---

## Design Principles

1. **Evidence-based only.** Every framework here has peer-reviewed research or official doctrine backing it (FBI, UK College of Policing, PERF, Home Office).
2. **No coercive techniques.** We deliberately exclude the Reid technique and similar confession-pressure methods. The PEACE model is the modern, ethical alternative.
3. **Korean context first.** Examples, vocabulary, and application notes are written for Korean police (경찰청, 지구대, 경찰발전협의회) — not just translated from Western doctrine.
4. **Legitimacy over efficiency.** Procedural justice research shows that *how* police act matters more than *what* they accomplish. This toolkit reflects that.

---

## For 경찰발전협의회 (Police Development Councils)

This project was built to support 경찰발전협의회 activities in Korea. The frameworks here help councils move beyond anecdotal discussion toward structured analysis:

- Use **SARA** when analyzing a recurring local problem (민원 패턴)
- Use **CPTED** when reviewing environmental safety of an area
- Use **Procedural Justice** when evaluating community trust
- Use **Hot Spots + ILP** when proposing targeted patrol deployment

---

## License

MIT — see [LICENSE](LICENSE).

한국어 문서: [README.ko.md](README.ko.md)
