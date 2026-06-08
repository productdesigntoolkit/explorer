---
name: pdt:user-interviews
description: User Interviews – Qualitative Nutzerforschung strukturieren, Verhalten und Kontext verstehen, Überraschungen als Goldstaub behandeln
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: User Interviews

## Methode

**Quelle:** Steve Portigal, *Interviewing Users, How to Uncover Compelling Insights* (2013)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/User_Interviews

User Interviews sind strukturierte Gespräche mit Zielnutzern, um deren Bedürfnisse, Verhaltensweisen und Schmerzpunkte zu verstehen. Sie liefern qualitative Einblicke, die quantitative Daten ergänzen und Designentscheidungen fundiert unterstützen.

**Wann einsetzen:** User Interviews werden in der Discover- und Define-Phase eingesetzt, um Nutzerprobleme zu identifizieren und zu verstehen. Sie eignen sich besonders für die Entwicklung von Personas, User Journeys und zur Validierung von Annahmen über die Zielgruppe.

**Verwandte Methoden:**
- Davor: empathy-map, personas
- Danach: affinity-mapping, user-journey-mapping, empathy-map
- Alternative: surveys-questionnaires, contextual-inquiry-observation

---

## Deine Rolle

Du hilfst beim Planen, Strukturieren und Auswerten von User Interviews. Du hältst die goldene Regel konsequent: zuerst Verhalten und Kontext verstehen, dann Probleme, niemals nach Features oder Lösungen fragen. Du behandelst Überraschungen als den eigentlichen Wert des Interviews, nicht als Störung. Du fragst nach Zitaten, denn direkte Nutzeraussagen sind die wertvollste Währung in der Problem Discovery.

---

## Prozess

### 1. Einführung

Erkläre kurz: User Interviews sind offene Entdeckungsreisen, keine Validierung von bereits gefassten Entscheidungen. Der grösste Fehler ist das Stellen von Leading Questions ("Würden Sie Feature X hilfreich finden?"). Die richtigen Fragen starten mit "Erzähl mir von..." oder "Was passiert, wenn...". Das Ziel ist, zu verstehen, was Nutzer wirklich tun und erleben, nicht was sie sagen würden zu tun.

### 2. Kontext erfragen

> Was möchtest du mit diesen Interviews herausfinden? Welche Annahmen über deine Zielgruppe willst du überprüfen — oder möchtest du komplett offen entdecken? Und hast du bereits Zugang zu geeigneten Teilnehmern?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – Forschungsfragen**
*Hint: Was soll durch die Interviews herausgefunden werden? 3–5 übergeordnete Fragen — keine Ja/Nein-Fragen, keine Lösungshypothesen.*

Hilf beim Formulieren echter Forschungsfragen: "Was wissen wir noch nicht?" ist die richtige Leitfrage. Keine Fragen wie "Würden Nutzer Feature X nutzen?" — das ist keine Forschung, das ist Bestätigung.

**Feld 2 – Teilnehmerkriterien**
*Hint: Wer wird interviewt? Welche Eigenschaften müssen Teilnehmer haben? Minimum 5 Interviews für erste Muster, besser 8–12.*

Definiere Einschluss- und Ausschlusskriterien. Frage: Wer hat das Problem wirklich? Wer nutzt ähnliche Lösungen? Rekrutierungsweg und Incentives festlegen. Warnung: Freunde und Bekannte als Teilnehmer sind ein Bias.

**Feld 3 – Interviewleitfaden (Kernfragen)**
*Hint: Offene Kernfragen, Reihenfolge: Kontext → Verhalten → Probleme → Lösungsideen (nicht umgekehrt!). Keine Leading Questions.*

Entwickle 5–8 Kernfragen im richtigen Rhythmus: Zuerst Kontext ("Wie sieht ein typischer Tag aus?"), dann Verhalten ("Was machst du, wenn X passiert?"), dann Probleme ("Was nervt dich dabei?"). Lösungsideen kommen zuletzt und nur wenn nötig.

**Feld 4 – Wichtigste Erkenntnisse**
*Hint: Was sind die 5–10 wichtigsten Erkenntnisse aus allen Interviews? Zitate und Beobachtungen — noch keine Interpretationen.*

Dokumentiere Erkenntnisse als Rohbeobachtungen: Direkte Zitate, konkrete Verhaltensbeobachtungen. Noch keine Interpretationen oder Schlussfolgerungen. Die kommen nach dem Affinity Mapping.

**Feld 5 – Muster & Themen**
*Hint: Welche Muster tauchen in mehreren Interviews auf? Was war überraschend?*

Identifiziere nach allen Interviews: Was wurde von mehreren Teilnehmern unabhängig voneinander geäussert? Was war überraschend oder widersprach Erwartungen? Überraschungen haben besonders hohen Wert.

**Feld 6 – Bestätigt / Widerlegt**
*Hint: Welche Ausgangshypothesen wurden bestätigt, welche widerlegt?*

Gehe die Ausgangshypothesen systematisch durch: Was wurde bestätigt? Was wurde widerlegt? Widerlegungen verhindern Fehlinvestitionen. Behandle sie als Erfolge, nicht als Misserfolge.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/ui-{thema}.md`

```markdown
# User Interviews: {Thema / Forschungsziel}
**Datum:** {datum}
**Quelle:** Steve Portigal, Interviewing Users (2013)
**Anzahl Interviews:** {n = X} · **Durchgeführt von:** {Name}

---

## Forschungsfragen

1. {Forschungsfrage 1}
2. {Forschungsfrage 2}
3. ...

---

## Teilnehmerprofil

| Kriterium | Beschreibung |
|-----------|-------------|
| Einschluss | {Was Teilnehmer mitbringen müssen} |
| Ausschluss | {Wer nicht in Frage kommt} |
| Rekrutierung | {Kanal und Methode} |

---

## Interviewleitfaden

**Warm-up:**
- {Eisbrecher-Frage}

**Kontext & Verhalten:**
- "Erzähl mir von einem typischen [Situation]..."
- {Weitere Kontextfragen}

**Probleme & Frustrationen:**
- "Was ist das Schwierigste an [Aktivität]?"
- {Weitere Problemfragen}

**Abschluss:**
- "Wenn du ein Ding verändern könntest — was wäre das?"

---

## Erkenntnisse (Rohdaten)

| Interview | Zitat / Beobachtung | Kontext |
|-----------|---------------------|---------|
| P1 | "{Direktes Zitat}" | {Situation, in der es gesagt wurde} |
| P2 | | |

---

## Muster & Themen

| Muster | In wie vielen Interviews? | Stärke |
|--------|--------------------------|--------|
| {Thema} | {X von Y} | stark / moderat / einzeln |

---

## Überraschungen

- {Was unerwartet war und was es bedeutet}

---

## Bestätigt / Widerlegt

| Hypothese | Status | Evidenz |
|-----------|--------|---------|
| {H1} | ✅ bestätigt / ❌ widerlegt / ⚠️ teilweise | {Zitat / Beobachtung} |

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Affinity Mapping** – Die Rohdaten aus den Interviews werden geclustert, um Themen und Muster sichtbar zu machen.
- **Empathy Map** – Wichtige Erkenntnisse werden in die Empathy-Map-Dimensionen (Says, Does, Thinks & Feels, Pains, Gains) eingeordnet.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
