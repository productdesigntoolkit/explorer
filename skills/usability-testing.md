---
name: pdt:usability-testing
description: Usability Testing – 5 echte Nutzer reichen für 80% der kritischen Probleme. Früh testen, systematisch beobachten, gezielt priorisieren
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Usability Testing

## Methode

**Quelle:** Jakob Nielsen, *Usability Engineering* (1993)
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/Usability_Testing

Beim Usability Testing testest du dein Produkt mit echten Nutzern, um Bedienungsprobleme und Verbesserungsmöglichkeiten zu identifizieren. Die Methode deckt Schwachstellen in der Benutzerführung auf, bevor das Produkt auf den Markt kommt.

**Wann einsetzen:** Du setzt Usability Testing ein, wenn du die Benutzerfreundlichkeit deines Produkts validieren möchtest. Die Methode eignet sich besonders vor wichtigen Produktentscheidungen oder vor dem Launch, um kostspielige Nachbesserungen zu vermeiden.

**Verwandte Methoden:**
- Davor: Prototyping, Wireframes / Mockups, MVP — Minimal Viable Product
- Danach: Pilot / Beta, Product Vision Board, KPI & Success Metrics Definition
- Alternative: Pilot / Beta, A/B Testing

---

## Deine Rolle

Du begleitest die Planung und Auswertung eines Usability Tests — von der Zieldefinition über das Testprotokoll bis zur priorisierten Issue-Liste. Du stellst sicher, dass Aufgaben als realistische Szenarien formuliert sind (nicht als Anweisungen), und dass Beobachtungen von Interpretationen getrennt bleiben. 5 Teilnehmer sind für qualitative Tests genug — du hilfst, diesen Grundsatz gegen interne Widerstände zu verteidigen.

---

## Prozess

### 1. Einführung

Erkläre Nielsens Grundsatz: 5 Teilnehmer finden 80% der kritischen Usability-Probleme. Der grösste Fehler: zu spät testen wenn der Prototyp zu ausgereift ist um noch grundlegende Änderungen vorzunehmen. Auch Guerrilla-Tests (5 Minuten, Café, informell) sind besser als gar keine Tests.

### 2. Kontext erfragen

> Was wird getestet (Prototyp, MVP, Feature), und welche spezifischen Fragen über die Usability sollen beantwortet werden?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – Testziele**
*Hint: Was soll der Test herausfinden? Nicht "ist es gut?", sondern "können Nutzer Task X in unter 2 Minuten erledigen?"*

Formuliere 2–3 konkrete Testfragen. Nicht "ist das Design gut?" — sondern messbare Verhaltensbeobachtungen.

**Feld 2 – Teilnehmer**
*Hint: Wie viele? (5 für qualitative Erkenntnisse ausreichend) Welche Eigenschaften? Echte Nutzer aus der Zielgruppe, keine Kollegen.*

Definiere Screening-Kriterien. Warum sind das die richtigen Tester? Wie werden sie rekrutiert?

**Feld 3 – Aufgaben (Task Scenarios)**
*Hint: Welche 3–5 Aufgaben werden gestellt? Realistische Szenarien formulieren, keine Anweisungen wie "Klicke auf X". Beispiel: "Du möchtest Y — wie würdest du vorgehen?"*

Erarbeite 3–5 Szenarien als realistische Aufgaben. Prüfe jede: impliziert sie die Lösung? Falls ja: umformulieren.

**Feld 4 – Beobachtungen**
*Hint: Was tun Nutzer, wo stocken sie, was sagen sie? Think-Aloud-Protokoll. Beobachten ohne einzugreifen.*

Definiere was beobachtet wird: wo stockt der Nutzer, welche Abweichungen vom erwarteten Pfad, welche Fragen entstehen. Trenne Beobachtung von Interpretation.

**Feld 5 – Usability-Metriken**
*Hint: Task Completion Rate, Time-on-Task, Error Rate, SUS-Score (System Usability Scale).*

Welche quantitativen Metriken werden erhoben? Mindestens Task Completion Rate und eine qualitative Bewertung.

**Feld 6 – Priorisierte Issues**
*Hint: Priorisiert nach Schwere (Critical, Major, Minor) und Häufigkeit. Was muss vor Launch behoben werden?*

Erstelle eine priorisierte Issue-Liste nach Critical / Major / Minor. Was muss vor dem nächsten Test oder Launch behoben sein?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/ut-{kontextname}.md`

```markdown
# Usability Test: {Produkt / Feature}
**Datum:** {datum}
**Quelle:** Jakob Nielsen — Usability Engineering (1993)

---

## Testziele
1. {Konkrete Frage über Nutzerverhalten}
2. {Konkrete Frage}

## Teilnehmer
- **Anzahl:** {5–8}
- **Profil:** {Screening-Kriterien}
- **Rekrutierung:** {Wie}

## Aufgaben (Task Scenarios)

**Aufgabe 1:** {Realistisches Szenario ohne Lösung zu nennen}
**Aufgabe 2:** {Szenario}
**Aufgabe 3:** {Szenario}

## Beobachtungsprotokoll
| Aufgabe | Beobachtung | Zitat | Interpretation |
|---------|------------|-------|---------------|
| 1 | | | |
| 2 | | | |

## Metriken
| Metrik | Zielwert | Ergebnis |
|--------|---------|---------|
| Task Completion Rate | >80% | |
| Time-on-Task | {Ziel} | |
| SUS-Score | >68 (Benchmark) | |

## Priorisierte Issues

### Critical (vor Launch beheben)
- {Issue}: {Beobachtung} — Betroffen: {X/5 Nutzer}

### Major (vor nächstem Test beheben)
- {Issue}: {Beobachtung}

### Minor (Backlog)
- {Issue}: {Beobachtung}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: kritische Issues im Prototypen beheben und einen weiteren Testdurchgang planen, oder bei ausreichender Confidence in den Pilot / Beta übergehen.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
