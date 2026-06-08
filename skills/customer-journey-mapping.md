---
name: pdt:customer-journey-mapping
description: Customer Journey Mapping – Die gesamte Kundenbeziehung über alle Touchpoints hinweg visualisieren und Optimierungspotenziale finden
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Customer Journey Mapping

## Methode

**Quelle:** Industrie-Praxis (systematisch aufgearbeitet von Jim Kalbach, *Mapping Experiences*, O'Reilly, 2016)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Customer_Journey_Mapping

Customer Journey Mapping visualisiert die gesamte Erfahrung eines Kunden mit einem Produkt oder Service über alle Berührungspunkte hinweg. Die Methode hilft dabei, Schmerzpunkte zu identifizieren und Optimierungspotenziale aufzudecken.

**Wann einsetzen:** Diese Methode wird eingesetzt, um die Kundenperspektive zu verstehen und Verbesserungsmöglichkeiten in der Customer Experience zu finden. Sie eignet sich besonders für die Analyse bestehender Services oder die Entwicklung neuer Kundenerlebnisse.

**Verwandte Methoden:**
- Davor: user-journey-mapping, personas, user-interviews
- Danach: problem-statement, crm-funnel-mapping, go-to-market-strategy
- Alternative: user-journey-mapping

---

## Deine Rolle

Du hilfst beim Aufbau einer umfassenden Customer Journey Map, die die gesamte Geschäftsbeziehung abbildet, von der ersten Wahrnehmung bis zur Weiterempfehlung. Du fragst aktiv nach emotionalen Tiefpunkten, denn diese sind die prioritären Optimierungsfelder. Du klärst den Unterschied zur User Journey Map: Customer Journey umfasst die Beziehung zum Unternehmen, nicht nur die Produktnutzung.

---

## Prozess

### 1. Einführung

Erkläre kurz: Die Customer Journey Map unterscheidet sich von der User Journey Map darin, dass sie die gesamte Geschäftsbeziehung abbildet, also auch Pre-Sales, Marketing-Touchpoints, Onboarding und After-Sales. Sie verbindet Problem Space und Market Space. Die emotionalen Tiefpunkte in der Journey sind die wichtigsten Ansatzpunkte für Verbesserungen.

### 2. Kontext erfragen

> Für welches Kundensegment und welches Szenario soll die Customer Journey abgebildet werden? Gibt es bereits Personas oder Daten aus Nutzerinterviews, auf die wir aufbauen können?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – Kundensegment & Szenario**
*Hint: Welches Kundensegment und welches Kaufszenario wird abgebildet? Customer Journey fokussiert auf die gesamte Kundenbeziehung inkl. Pre- und Post-Sales.*

Definiere klar, wessen Journey abgebildet wird und in welchem Szenario. Eine Journey pro Segment und Szenario. Wenn mehrere Segmente relevant sind, priorisiere.

**Feld 2 – Journey-Phasen**
*Hint: Welche Phasen durchläuft der Kunde von Awareness bis Advocacy? Typisch: Awareness → Research → Evaluation → Purchase → Onboarding → Use → Renewal → Advocacy.*

Erarbeite gemeinsam die Phasen, die zum spezifischen Kontext passen. Nicht alle Phasen sind immer relevant. Frage nach: Gibt es eine Vor-Sales-Phase? Wie lange dauert Onboarding?

**Feld 3 – Touchpoints pro Phase**
*Hint: Welche Kontaktpunkte mit dem Unternehmen gibt es in jeder Phase? Digital, Sales, Product.*

Liste pro Phase alle relevanten Touchpoints auf. Unterscheide nach Kanal: digital (Website, Email, App), Sales (Demo, Gespräch), Product (Onboarding, In-App), Support.

**Feld 4 – Kundenerfahrung & Emotionen**
*Hint: Wie erlebt der Kunde jede Phase? Wo sind emotionale Hochpunkte, wo Tiefpunkte?*

Zeichne die Emotions-Kurve verbal nach. Frage besonders nach Tiefpunkten: Was frustriert, verwirrt oder enttäuscht? Diese Punkte sind die wichtigsten Designchancen.

**Feld 5 – Interne Prozesse & Verantwortlichkeiten**
*Hint: Welche internen Teams und Prozesse stehen hinter jedem Touchpoint? Wo gibt es Übergaben, die zu schlechter Customer Experience führen?*

Kartiere die Backstage-Prozesse: Welches Team ist für welche Phase zuständig? Wo passieren Übergaben zwischen Abteilungen? Übergaben sind häufig die Ursache für schlechte CX.

**Feld 6 – Optimierungsprioritäten**
*Hint: Welche 3–5 Verbesserungen hätten den grössten Impact auf die Gesamterfahrung?*

Destilliere aus den Tiefpunkten und Übergabeproblemen die 3–5 Prioritäten, priorisiert nach Schmerz (für den Kunden) und Machbarkeit (für das Unternehmen).

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/cjm-{projektname}.md`

```markdown
# Customer Journey Map: {Kundensegment – Szenario}
**Datum:** {datum}
**Quelle:** Industrie-Praxis (Kalbach, Mapping Experiences, 2016)

---

## Journey-Übersicht

| Phase | Touchpoints | Kundenaktionen | Emotionen | Interne Prozesse |
|-------|-------------|----------------|-----------|-----------------|
| Awareness | {Kanäle} | {Was der Kunde tut} | 😐 / 😊 / 😤 | {Team / Prozess} |
| Research | | | | |
| Evaluation | | | | |
| Purchase | | | | |
| Onboarding | | | | |
| Use | | | | |
| Renewal | | | | |
| Advocacy | | | | |

---

## Emotionskurve

{Kurve in Worten: Hoch- und Tiefpunkte der Kundenerfahrung über die Phasen}

---

## Kritische Tiefpunkte

1. {Phase + Beschreibung des Tiefpunkts + Ursache}
2. ...

---

## Optimierungsprioritäten

| Priorität | Phase | Problem | Massnahme | Impact |
|-----------|-------|---------|-----------|--------|
| 1 | {Phase} | {Problem} | {Idee} | hoch/mittel |

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Problem Statement** – Die kritischen Tiefpunkte werden in ein scharf formuliertes Problemstatement überführt.
- **CRM Funnel Mapping** – Die Touchpoints in der Customer Journey können direkt in die CRM-Struktur überführt werden.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
