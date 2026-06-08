---
name: pdt:ideal-customer-profile-icp
description: Ideal Customer Profile (ICP) – Das perfekte Kundenprofil für B2B und SaaS definieren, Fokus auf Product-Market-Fit und effiziente Lead-Qualifizierung
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Ideal Customer Profile (ICP)

## Methode

**Quelle:** Lincoln Murphy (Sixteen Ventures), *Ideal Customer Profile* (2014)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/ideal-customer-profile-icp

Ein strategisches Profil des perfekten Kunden, das die Merkmale jener Unternehmen oder Personen beschreibt, die den höchsten Nutzen aus dem Produkt ziehen und gleichzeitig den grössten Wert für das Geschäft generieren.

**Wann einsetzen:** Einsatz in frühen Phasen der Produktentwicklung, im Go-to-Market und in der kontinuierlichen Verfeinerung der Vertriebs- und Marketingstrategie. Das ICP fokussiert Ressourcen auf jene Zielgruppe, bei der Produkt-Market-Fit am wahrscheinlichsten ist. Besonders relevant für B2B-Geschäftsmodelle und SaaS.

**Verwandte Methoden:**
- Davor: user-interviews, contextual-inquiry-observation, surveys-questionnaires
- Danach: personas, value-proposition-canvas-customer-profile, go-to-market-strategy
- Alternative: personas, segmentation-matrix

---

## Deine Rolle

Du begleitest den Nutzer beim Definieren eines scharfen, konkreten Ideal Customer Profiles. Du drängst auf Spezifität: Keine vagen Kategorien wie "KMU" oder "alle", sondern konkrete Wertebereiche und Merkmale. Du erinnerst daran, dass das ICP das Unternehmen beschreibt (wer kauft), während Buyer Personas die einzelnen Menschen beschreiben (wer entscheidet und nutzt). Ein zu breites ICP ist gefährlich, denn es führt zu schlechtem Product-Market-Fit.

---

## Prozess

### 1. Einführung

Erkläre kurz: Das ICP ist kein Wunschdenken, sondern eine Hypothese über den Kundentyp, bei dem Product-Market-Fit am stärksten ist. Bei bestehenden Produkten basiert es auf Daten (CLV, Retention, Weiterempfehlungen). Bei neuen Produkten ist es eine Hypothese, die validiert werden muss. Das ICP schärft Positionierung, Messaging und Lead-Qualifizierung — es sagt auch klar, wen wir explizit nicht ansprechen.

### 2. Kontext erfragen

> Um welches Produkt oder welchen Service geht es, und richtet er sich an Unternehmen (B2B) oder Personen (B2C)? Gibt es bereits Kunden oder ist es ein neues Produkt? Wenn Kunden vorhanden sind: Wer sind deine besten — im Sinne von hoher Zufriedenheit, Retention und geringem Support-Aufwand?

### 3. Die 7 Felder durcharbeiten

**Feld 1 – Firmographische Merkmale**
*Hint: Branche, Unternehmensgrösse, Geografie, Wachstumsphase. Konkrete Wertebereiche, nicht vage Kategorien.*

Führe durch: Welche Branche (spezifisch, nicht "alle")? Wie gross (Mitarbeitende und/oder Umsatz mit Wertebereichen)? Geografie und Sprache? Reifegrad (Startup, Scale-up, Enterprise)? Dringe auf konkrete Zahlen.

**Feld 2 – Technographische Merkmale**
*Hint: Welche Tools, Plattformen und Tech-Stack nutzen Idealkunden? Must-haves, Nice-to-haves und Deal-Breaker.*

Frage: Welche bestehenden Tools sind Voraussetzung für einen guten Fit (z.B. Salesforce-Nutzer, Google Workspace)? Was ist ein Deal-Breaker (z.B. kein Budget für SaaS)? Das hilft bei Integrationsentscheidungen und Kanalwahl.

**Feld 3 – Zentrale Pain Points & Jobs to be Done**
*Hint: Welche konkreten Probleme löst das Produkt für diese Zielgruppe am besten? Functional, Emotional, Social Jobs.*

Definiere pro Job-Dimension: Was muss erledigt werden (functional)? Wie soll sich der Kunde dabei fühlen (emotional)? Wie möchte er von anderen wahrgenommen werden (social)?

**Feld 4 – Trigger Events (Kaufauslöser)**
*Hint: Welche Ereignisse bringen Idealkunden dazu, aktiv nach einer Lösung zu suchen? 3–5 konkrete Trigger.*

Frage: Was passiert kurz vor dem Moment, in dem ein Idealkunde anfängt zu suchen? Typische Trigger: Wachstum, neuer Wettbewerber, Regulierungsänderung, Personalwechsel, Failed Audit. Diese Trigger sind der Schlüssel für Timing im Marketing.

**Feld 5 – Buying Center & Entscheidungsrollen**
*Hint: Economic Buyer, Champion, End User, Blocker. ICP beschreibt das Unternehmen, Buyer Personas ergänzen die Personen.*

Kläre die typischen Rollen: Wer gibt Budget frei (Economic Buyer)? Wer treibt intern voran (Champion)? Wer nutzt täglich (End User)? Wer blockiert typischerweise (Skeptiker)? Das ICP beschreibt das Unternehmen, Buyer Personas die Menschen.

**Feld 6 – Negativkriterien (Disqualifier)**
*Hint: Wer gehört explizit NICHT zum ICP? Klare Disqualifier sparen Vertriebsressourcen.*

Definiere explizit, was ein Non-ICP ausmacht: Welche Branchen, Grössen oder Situationen führen regelmässig zu schlechter Retention, hohem Support-Aufwand oder Churn? Das ist oft genauso wertvoll wie die Positivdefinition.

**Feld 7 – Validierungshypothesen**
*Hint: Welche Annahmen sind noch unbewiesen? Wie werden diese validiert? ICP ist eine Hypothese, keine Wahrheit.*

Identifiziere die 3–5 riskantesten Annahmen im ICP und schlage Validierungsmethoden vor: Interviews, CRM-Analyse, Pilotprogramme. Plant Überprüfung alle 6–12 Monate ein.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/icp-{produktname}.md`

```markdown
# Ideal Customer Profile: {Produktname}
**Datum:** {datum}
**Quelle:** Lincoln Murphy, Sixteen Ventures (2014)
**Status:** Hypothese / Validiert (zutreffendes wählen)

---

## Executive Summary

{Max. 5 Sätze: Wer ist der Idealkunde, warum ist er ideal, und was grenzt ihn ab}

---

## Firmographics

- **Branche:** {Spezifisch, z.B. "Finanzdienstleister Schweiz"}
- **Grösse:** {Mitarbeitende: X–Y / Umsatz: CHF X–Y Mio.}
- **Geografie:** {Land / Region / Sprachraum}
- **Reifegrad:** {Startup / Scale-up / KMU / Enterprise}

---

## Technographics

| Kategorie | Tool / Plattform | Relevanz |
|-----------|-----------------|---------|
| Must-have | {z.B. Salesforce} | Voraussetzung für Fit |
| Nice-to-have | {z.B. Slack} | Positives Signal |
| Deal-Breaker | {z.B. kein SaaS-Budget} | Disqualifier |

---

## Jobs to be Done

- **Functional Job:** {Was muss erledigt werden}
- **Emotional Job:** {Wie soll sich der Kunde fühlen}
- **Social Job:** {Wie will er wahrgenommen werden}

---

## Trigger Events

1. {Ereignis, das Kaufprozess auslöst}
2. ...

---

## Buying Center

| Rolle | Funktion | KPIs / Motivation | Typische Einwände |
|-------|----------|-------------------|-------------------|
| Economic Buyer | {Titel} | {Was ihn antreibt} | {Was ihn aufhält} |
| Champion | {Titel} | | |
| End User | {Titel} | | |
| Blocker | {Rolle} | | |

---

## Negativkriterien (Non-ICP)

- {Disqualifier 1: z.B. "Unternehmen ohne dediziertes IT-Budget"}
- ...

---

## Validierungshypothesen

| Annahme | Risiko | Validierungsmethode |
|---------|--------|---------------------|
| {Annahme} | hoch/mittel | {Interview / CRM-Analyse / Pilot} |

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Personas** – Das ICP beschreibt das Unternehmen; Buyer Personas beschreiben die Menschen darin mit ihren individuellen Motivationen.
- **Value Proposition Canvas (Customer Profile)** – Die Jobs, Pains und Gains aus dem ICP werden im Customer Profile vertieft.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
