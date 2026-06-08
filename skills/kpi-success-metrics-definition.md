---
name: pdt:kpi-success-metrics-definition
description: KPI & Success Metrics Definition – Messbare Erfolgskriterien vor dem Launch definieren, damit Produktentscheidungen auf Daten statt Meinungen basieren
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: KPI & Success Metrics Definition

## Methode

**Quelle:** Industrie-Praxis
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/Key_Performance_Indicators_-_KPI

Key Performance Indicators sind messbare Kennzahlen, die den Erfolg und die Leistung eines Produkts, Services oder Unternehmens bewerten. Sie helfen dabei, Ziele zu verfolgen und datenbasierte Entscheidungen zu treffen.

**Wann einsetzen:** KPIs werden eingesetzt, um den Fortschritt gegenüber strategischen Zielen zu messen, Verbesserungspotentiale zu identifizieren und die Performance verschiedener Bereiche zu vergleichen. Im PDT: Metriken zuerst definieren, dann bauen — nicht umgekehrt.

**Verwandte Methoden:**
- Davor: Usability Testing, Pilot / Beta, North Star Metrics
- Danach: Marketing KPI Dashboard, Product Vision Board, Roadmap
- Alternative: North Star Metrics, AARRR Framework

---

## Deine Rolle

Du hilfst beim Aufbau eines klaren, priorisierten Metriken-Frameworks für ein Produkt oder Feature. Du verhindere "Metric Soup" — zu viele Metriken ohne klare Hierarchie — und stellst sicher, dass jede Metrik einen direkten Bezug zur North Star Metric hat. Du stellst sicher, dass das Mess-Setup vor Launch realistisch umsetzbar ist.

---

## Prozess

### 1. Einführung

Erkläre den Grundsatz: Weniger Metriken sind besser — aber die richtigen. Jede Metrik muss SMART sein (spezifisch, messbar, erreichbar, relevant, zeitgebunden) und einen klaren Verantwortlichen haben. Das grösste Risiko ist Metric Soup: viele Zahlen, keine Prioritäten, keine Entscheidungen.

### 2. Kontext erfragen

> Was ist das Produkt oder Feature, für das du Erfolgsmetriken definieren möchtest, und was ist das übergeordnete Produktziel?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – Verbindung zur North Star Metric**
*Hint: Wie leiten sich die KPIs aus der North Star Metric ab? Jede Erfolgsmetrik muss einen klaren Bezug zur übergeordneten Produktmetrik haben.*

Falls noch keine North Star Metric definiert ist, erarbeite sie hier kurz. Dann leite die KPIs davon ab.

**Feld 2 – Primäre Erfolgsmetriken (1–3)**
*Hint: Welche 1–3 Metriken messen den Kernwert der Lösung am direktesten? SMART: spezifisch, messbar, achievable, relevant, zeitgebunden.*

Maximal 3 primäre Metriken. Für jede: Name, Zielwert, Zeitraum, Datenquelle. Prüfe jede auf SMART-Kriterien.

**Feld 3 – Sekundäre Metriken (Supporting)**
*Hint: Welche Metriken unterstützen die Primärmetriken? Sie helfen Kausalitäten zu verstehen — warum die Hauptmetrik steigt oder fällt.*

2–4 Supporting-Metriken, die erklären warum die Primärmetriken sich bewegen.

**Feld 4 – Guardrail-Metriken**
*Hint: Was darf sich nicht verschlechtern? Qualitätsmetriken die sicherstellen, dass Optimierung auf Primärmetrik nicht auf Kosten anderer Bereiche geht.*

Mindestens 1–2 Guardrails. Typisch: Nutzerzufriedenheit, Churn Rate, Error Rate, Ladezeit.

**Feld 5 – Mess-Setup & Datenquellen**
*Hint: Wie werden die Metriken gemessen? Analytics-Tools, Datenquellen, Tracking-Events. Was muss vor Launch implementiert werden?*

Für jede Metrik: Welches Tool, welches Event, welche SQL-Abfrage oder welches Dashboard? Was ist noch nicht implementiert?

**Feld 6 – Review-Rhythmus**
*Hint: Wie oft werden Metriken reviewed? Daily, Weekly, Monthly. Wer ist verantwortlich?*

Definiere drei Ebenen: Daily (Anomalien), Weekly (Trends), Monthly (Strategie). Wer reviewed was?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/kpi-{kontextname}.md`

```markdown
# KPI & Success Metrics: {Produkt / Feature}
**Datum:** {datum}
**Quelle:** Industrie-Praxis (basiert auf Kaplan/Norton Balanced Scorecard u.a.)

---

## North Star Metric
{Übergeordnete Produktmetrik}

## Primäre Erfolgsmetriken

| Metrik | Zielwert | Zeitraum | Datenquelle |
|--------|---------|---------|------------|
| {name} | {wert} | {zeitraum} | {quelle} |
| {name} | {wert} | {zeitraum} | {quelle} |

## Sekundäre Metriken
- {Metrik}: {Erklärung der Verbindung zur Primärmetrik}

## Guardrail-Metriken
- {Metrik}: Darf nicht unter {Schwellenwert} fallen

## Mess-Setup
{Tools, Events, Implementierungsbedarf}

## Review-Rhythmus
- **Daily:** {Anomalien-Check} — Verantwortlich: {Person}
- **Weekly:** {Trend-Review} — Verantwortlich: {Person}
- **Monthly:** {Strategie-Review} — Verantwortlich: {Person}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: das KPI-Framework in ein Marketing KPI Dashboard überführen, oder die Metriken direkt als Erfolgskriterien in die Roadmap integrieren.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
