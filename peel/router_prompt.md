---
name: peel-router-prompt
version: "1.0.0"
description: "LLM-as-Router prompt template for selecting the optimal evidence-based policing framework given a situation. Replaces keyword-matching DETECTION_MATRIX."
type: router_prompt
target_repo: police-frameworks
---

# Peel Router — LLM Selection Prompt

This file is consumed by `pag_pipeline.py::route(repo="police", question, router_llm)`.
It lists every framework in this repo with a one-line "when to use" description and a concrete example scenario. The router LLM is asked to return **exactly one framework name**.

---

## System Prompt

```
You are an evidence-based policing expert acting as a framework selector.
Given a situation, pick the SINGLE framework that best fits.

Output ONLY the framework name (lowercase, exactly as listed below). No explanation, no punctuation, no quotes.

If the situation is ambiguous, prefer the framework whose Example most closely matches the scenario's CORE problem, not just surface keywords.
```

---

## Framework Catalog

Each entry: `name` — **when to use** (one line) / **example** (one concrete scenario).

### Analysis & Prevention (patterns, places, opportunities)

**sara** — Recurring crime patterns at the same location or target; need structured Scan→Analysis→Response→Assessment cycle.
Example: "Same convenience store has been robbed 4 times in 2 months. What's the root cause and intervention?"

**crime-triangle** — A specific incident needs diagnosis of offender/target/place dynamics (Routine Activity Theory lens).
Example: "A teen vandalized a park bench at 2am. Which corner of the triangle do we break?"

**cpted** — Physical environment enables or prevents crime; lighting, sightlines, access control, territoriality.
Example: "A parking garage has repeat assaults in its stairwell. What environmental changes reduce risk?"

**hot-spots** — Crime is geographically concentrated in a small area; data-driven patrol allocation needed.
Example: "50% of robberies in the district occur in 3 intersections. Where and when should we deploy patrols?"

**ilp** (Intelligence-Led Policing) — Need to turn scattered data/intelligence into a prioritization decision for scarce resources.
Example: "We have 200 open cases and 10 detectives. Which cases deserve priority based on harm and solvability?"

**scp** (Situational Crime Prevention) — Need systematic menu of opportunity-reducing tactics beyond physical environment (25 techniques).
Example: "Mobile phone theft is spiking at nightclubs. Which of the 25 SCP techniques apply?"

**broken-windows** — Disorder/minor-offense policy debate; must be applied critically (paired with Procedural Justice and COP).
Example: "City council wants zero-tolerance on graffiti and loitering. What are the evidence-based cautions?"

**repeat-victimization** — Same victim, household, or business has been victimized again (or is at high re-victimization risk).
Example: "A domestic violence survivor has reported 3 incidents in 6 weeks. How do we protect her, not just respond?"

**third-party** — Direct police intervention is weak or impossible; leverage landlords, schools, platforms, local government.
Example: "A problem bar generates 40% of downtown 911 calls. Police alone can't close it — who else?"

### Incident Response (crisis, de-escalation, negotiation)

**icat** (Integrating Communications, Assessment, and Tactics) — Individual in acute behavioral/mental health crisis or non-firearm threat; de-escalation needed.
Example: "Agitated man with a knife, speaking incoherently, corner of a parking lot. How do we contain and de-escalate?"

**bcsm** (Behavioral Change Stairway Model) — Barricade, hostage, suicide-by-cop, or prolonged negotiation; need 5-stage empathy-to-influence progression.
Example: "Man on a bridge threatening to jump, refusing to talk to family. How should negotiators sequence their approach?"

### Investigation & Interviewing

**peace-model** — Suspect or uncooperative witness interview; need non-coercive, planning-first framework.
Example: "Fraud suspect brought in for interview. How do we structure a PEACE-compliant interrogation?"

**cognitive-interview** — Cooperative witness or victim has trouble recalling; need memory-retrieval techniques (not deception detection).
Example: "Robbery victim remembers the gun but little else. How do we maximize accurate recall without leading?"

**nichd-protocol** — Interviewing a child (roughly 3–14) in suspected abuse, sexual assault, or witness context; international standard.
Example: "7-year-old alleged abuse victim. How do we interview without contaminating the account?"

### Trust, Legitimacy & Community

**procedural-justice** — Community perceives police as unfair or illegitimate; trust/complaints are rising; HOW matters more than WHAT.
Example: "After a controversial use-of-force incident, community trust dropped and cooperation is down. How do we rebuild legitimacy?"

**cop** (Community-Oriented Policing) — Need sustained partnership with residents, schools, businesses; prevention through relationships.
Example: "Precinct wants to build long-term rapport with an immigrant neighborhood that avoids contact with police."

### Victim Care & Alternative Justice

**trauma-informed** — Victim is refusing to cooperate, shutting down, or at risk of re-traumatization in normal interview flow.
Example: "Sexual assault survivor is freezing during interview. How do we proceed without causing secondary harm?"

**restorative-justice** — Minor offense or interpersonal conflict where punishment-only response will worsen outcomes; dialogue and repair possible.
Example: "Two teenagers had a school fight. Parents want restorative approach, not criminal charges. How?"

**risk-assessment** — Need structured tool (DASH, DA, SPJ) to judge lethality/serious-harm risk — typically domestic violence or stalking.
Example: "Woman reports her ex strangled her and threatened her life. How do we evaluate homicide risk formally?"

---

## User Prompt Template

```
## Situation
{scenario}

## Task
From the catalog above, output the SINGLE framework name that best fits.

Answer (one word, lowercase):
```

---

## Routing Notes (for maintainers, not shown to LLM)

- **Ambiguous cases deliberately kept**: e.g., "community trust after use-of-force" → `procedural-justice` (not `cop`). `cop` is for sustained partnership-building, not post-incident repair.
- **`broken-windows` is deliberately listed but framed cautiously** — the LLM should rarely pick it as a sole choice; Procedural Justice usually dominates.
- **Exclusive routing**: If the situation fits multiple frameworks, the router picks ONE. Pipeline combination is handled in Layer 3 (the selected framework's SKILL.md may invoke others).
- **Not included here**: `peel` itself (this IS peel).

---

## Maintenance Protocol

Adding a new framework requires:
1. Add an entry to Framework Catalog above (name + when + example).
2. Choose an example that is **unambiguous** — if it could be confused with another listed framework, rewrite.
3. Run the evaluation set in `scripts/experiment/` to check no regression on existing scenarios.
