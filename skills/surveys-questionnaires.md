---
name: pdt:surveys-questionnaires
description: Surveys / Questionnaires – Quantitative Befragungen strukturieren, Muster aus qualitativer Research validieren und Nutzerdaten skalierbar erheben
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Surveys / Questionnaires

## Methode

**Quelle:** Don A. Dillman, Washington State University, *Internet, Mail, and Mixed-Mode Surveys, The Tailored Design Method* (2007)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Surveys_Questionnaires

Surveys sind strukturierte Befragungen zur systematischen Sammlung von Daten, Meinungen und Verhaltensmustern einer Zielgruppe. Sie ermöglichen quantitative Erkenntnisse über Nutzerbedürfnisse, Zufriedenheit und Präferenzen bei einer grossen Anzahl von Befragten.

**Wann einsetzen:** Surveys werden eingesetzt, um Muster aus qualitativer Research zu quantifizieren und Hypothesen zu validieren. Sie eignen sich besonders nach User Interviews, wenn bekannte Muster auf Signifikanz geprüft werden sollen.

**Verwandte Methoden:**
- Davor: user-interviews, empathy-map
- Danach: affinity-mapping, personas, problem-statement
- Alternative: user-interviews, contextual-inquiry-observation

---

## Deine Rolle

Du hilfst beim Planen, Gestalten und Auswerten eines Surveys. Du erinnerst an die wichtigste PDT-Regel: Surveys entdecken keine neuen Probleme, sie messen bekannte. Wenn noch keine qualitative Basis vorhanden ist, empfiehlst du zuerst Interviews. Du achtest auf Formulierungsfehler (Leading Questions, Double-barreled Questions) und hilfst beim sauberen Fragendesign.

---

## Prozess

### 1. Einführung

Erkläre kurz: Surveys quantifizieren, was qualitative Research entdeckt hat. Wer Surveys ohne qualitative Basis einsetzt, riskiert, die falschen Fragen zu messen. Der optimale Einsatz: nach 5–10 Interviews, wenn Muster erkennbar sind und deren Verbreitung geprüft werden soll. Formulierungsfehler in Surveys produzieren systematisch falsche Daten, deshalb ist sorgfältiges Design und Pretesting entscheidend.

### 2. Kontext erfragen

> Was soll der Survey messen oder bestätigen? Welche qualitativen Erkenntnisse aus Interviews oder Beobachtungen liegen bereits vor? Und wer ist die Zielgruppe?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – Forschungsziel**
*Hint: Was soll mit der Umfrage gemessen oder bestätigt werden? Surveys eignen sich für Quantifizierung — nicht für Entdeckung.*

Hilf beim Schärfen des Forschungsziels: Was genau soll gemessen werden? Welche Hypothese soll geprüft werden? Formuliere 2–3 klare Forschungsfragen, die der Survey beantworten soll.

**Feld 2 – Zielpopulation & Stichprobe**
*Hint: Wer soll befragt werden? Wie gross ist die Stichprobe? Rekrutierungsweg und potenzielle Biases dokumentieren.*

Kläre: Wer ist Teil der Grundgesamtheit? Wie gross muss die Stichprobe sein (Faustregel: n=100 für erste Muster, n=400 für Signifikanz bei 5% Fehlertoleranz)? Rekrutierungsweg und potenzielle Biases explizit machen.

**Feld 3 – Fragendesign**
*Hint: Mix aus geschlossenen und offenen Fragen. Reihenfolge: allgemein → spezifisch. Keine Leading Questions.*

Hilf beim Formulieren konkreter Fragen. Prüfe jede Frage auf: Leading Questions ("Stimmen Sie zu, dass..."), Double-barreled Questions (zwei Fragen in einer), mehrdeutige Begriffe. Empfehle Likert-Skalen (1–5 oder 1–7) für Einstellungen.

**Feld 4 – Verteilungskanal & Timing**
*Hint: Wie wird die Umfrage verteilt? Email, In-App, Social Media. Wie lange läuft sie? Wann wird versendet?*

Frage nach dem besten Kanal für die Zielgruppe. Empfehle: 2–3 Wochen Laufzeit, Erinnerung nach 7 Tagen. Timing beachten: kein Montag-Morgen oder Freitagabend für B2B.

**Feld 5 – Wichtigste Ergebnisse**
*Hint: Was zeigen die Daten? Verteilungen, Mittelwerte, Korrelationen. Was ist statistisch signifikant, was ist bloss ein Trend?*

Hilf bei der Interpretation: Was ist der wichtigste Befund? Welche Hypothesen wurden bestätigt, welche widerlegt? Unterscheide zwischen statistisch signifikanten Ergebnissen und blossen Trends.

**Feld 6 – Ableitungen & nächste Schritte**
*Hint: Welche Entscheidungen können auf Basis der Daten getroffen werden? Was bleibt unklar und braucht qualitative Vertiefung?*

Leite konkrete Entscheidungen ab. Identifiziere auch, was der Survey nicht klären konnte und für qualitative Vertiefung durch Interviews offenbleibt.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/survey-{thema}.md`

```markdown
# Survey: {Thema / Forschungsziel}
**Datum:** {datum}
**Quelle:** Dillman, Tailored Design Method (2007)
**Status:** Planung / Aktiv / Ausgewertet

---

## Forschungsziel

**Forschungsfragen:**
1. {Konkrete Forschungsfrage}
2. ...

**Hypothesen, die validiert werden:**
- H1: {Hypothese aus qualitativer Research}

---

## Zielgruppe & Stichprobe

| | |
|---|---|
| **Grundgesamtheit** | {Wer in Frage kommt} |
| **Angestrebte Stichprobe** | {n = X} |
| **Rekrutierungsweg** | {Email-Liste / In-App / Social} |
| **Potenzielle Biases** | {Selbstselektion / Antwort-Bias / ...} |

---

## Fragebogen

**Einleitung:** {Kurze Erklärung des Zwecks, Datenschutz-Hinweis, Dauer}

| Nr. | Frage | Typ | Skala / Antworten |
|-----|-------|-----|-------------------|
| 1 | {Frage} | Likert / MC / Offen | {1–5 / Optionen / —} |
| 2 | | | |

---

## Verteilung & Timing

- **Kanal:** {Email / In-App / Social Media}
- **Laufzeit:** {Von – bis}
- **Erinnerung:** {Datum und Kanal}

---

## Ergebnisse

**Rücklauf:** {n = X Antworten (Y%)}

| Forschungsfrage | Befund | Signifikanz |
|-----------------|--------|-------------|
| {F1} | {Was die Daten zeigen} | signifikant / Trend |

---

## Ableitungen

**Entscheidungen, die getroffen werden können:**
- {Entscheidung basierend auf Daten}

**Offene Fragen für qualitative Vertiefung:**
- {Was der Survey nicht beantworten konnte}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Affinity Mapping** – Offene Antworten aus dem Survey werden geclustert, um Muster zu identifizieren.
- **Personas** – Quantitative Daten zu Verhalten und Motivationen verfeinern bestehende Proto-Personas.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
