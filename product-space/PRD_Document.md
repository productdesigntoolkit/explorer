---
title: "PRD Document"
space: product-space
description: "Das PRD (Product Requirements Document) ist ein zentrales Dokument, das die Vision, Ziele, Funktionen und Anforderungen eines Produkts strukturiert definiert."
skill: prd-document
---

# PRD Document

## Kurzbeschreibung

Das PRD (Product Requirements Document) ist ein zentrales Dokument, das die Vision, Ziele, Funktionen und Anforderungen eines Produkts strukturiert definiert. Es dient als gemeinsame Referenz für alle Beteiligten und stellt sicher, dass das Entwicklungsteam ein einheitliches Verständnis des zu bauenden Produkts hat.

## Einsatzzweck

Das PRD wird zu Beginn der Produktentwicklung erstellt, wenn die grundlegende Produktidee definiert ist, aber vor der technischen Umsetzung. Es eignet sich besonders für komplexere Produkte oder Features, bei denen mehrere Teams zusammenarbeiten und eine klare Dokumentation der Anforderungen erforderlich ist.

## Kurzanleitung

1. **Problemdefinition:** Beschreibe das zu lösende Problem und die Zielgruppe → "Nutzer können ihre Ausgaben nicht effizient verfolgen"
2. **Produktvision:** Definiere die übergeordnete Vision und die Ziele des Produkts → "Eine intuitive App für automatisches Expense-Tracking"
3. **Zielgruppe:** Spezifiziere die Hauptnutzer und ihre Bedürfnisse → Berufstätige zwischen 25-45 Jahren mit regelmässigen Geschäftsausgaben
4. **Funktionale Anforderungen:** Liste alle Features und Funktionen auf → Ausgaben fotografieren, Kategorien zuweisen, Reports erstellen
5. **Nicht-funktionale Anforderungen:** Definiere Performance, Sicherheit und Usability-Kriterien → App startet in unter 2 Sekunden
6. **User Stories:** Formuliere Anforderungen aus Nutzersicht → "Als Geschäftsreisender möchte ich Belege fotografieren können"
7. **Akzeptanzkriterien:** Bestimme messbare Erfolgskriterien für jede Funktion → Foto wird in unter 5 Sekunden verarbeitet
8. **Prioritäten:** Kategorisiere Features nach Must-have, Should-have und Nice-to-have
9. **Technische Constraints:** Dokumentiere technische Einschränkungen und Abhängigkeiten → iOS 14+, DSGVO-Konformität
10. **Timeline:** Erstelle einen groben Zeitplan mit Meilensteinen und Releases

## Beispielprompt

{% code overflow="wrap" %}
```
# PRD Generator Prompt

## Rolle
Du bist Senior Product Manager mit 10+ Jahren Erfahrung in B2B SaaS. Du hast PRDs für Teams bei Stripe, Linear und Notion geschrieben. Du folgst dem Prinzip "ruthless prioritization" und schreibst PRDs, die Engineering-Teams tatsächlich lesen.

## Kontext
**Produkt/Feature:** [Name einfügen]
**Zielgruppe:** [Welcher ICP, welche Persona]
**Strategischer Kontext:** [Warum jetzt? Welches Company OKR?]
**Bisherige Lösung:** [Status quo, Workarounds der Nutzer]
**Tech-Stack:** [Relevante Technologien, Constraints]
**Team:** [Grösse, Skills, verfügbare Kapazität]

## Aufgabe
Erstelle ein vollständiges Product Requirements Document, das Engineering, Design und Stakeholder als Single Source of Truth nutzen können.

## Struktur des Outputs

### 1. TL;DR
Maximal 5 Sätze. Muss alleine verständlich sein. Antwortet auf: Was, für wen, warum, bis wann.

### 2. Problem Statement
- Welches Nutzerproblem lösen wir?
- Evidenz: Daten, Interviews, Support-Tickets, NPS-Kommentare.
- Kosten des Nichtstuns: Was passiert, wenn wir es nicht lösen?

### 3. Goals und Non-Goals
**Goals**
- 3 bis 5 messbare Ziele mit Erfolgskriterien.

**Non-Goals**
- Was wir bewusst NICHT machen und warum.
- Verhindert Scope Creep.

### 4. Success Metrics
- North Star Metric für dieses Feature.
- 2 bis 3 Leading Indicators (verhaltensbasiert).
- 1 bis 2 Guardrail Metrics (was darf nicht schlechter werden?).
- Baseline-Werte und Zielwerte mit Zeitrahmen.

### 5. User Stories
Format: "Als [Persona] möchte ich [Aktion], damit [Outcome]."
- Priorisiert nach MoSCoW (Must, Should, Could, Won't).
- Jede Story mit Akzeptanzkriterien (Given/When/Then).

### 6. Functional Requirements
- Detaillierte Anforderungen pro User Story.
- Edge Cases und Error States.
- Empty States, Loading States, Success States.

### 7. Non-Functional Requirements
- Performance (Latenz, Throughput).
- Security und Compliance (DSGVO, FINMA falls relevant).
- Accessibility (WCAG Level).
- Internationalisierung (Sprachen, Zeitzonen).

### 8. UX und Design
- Verlinkung zu Figma/Mockups.
- Information Architecture.
- Interaction Patterns.
- Open Design Questions.

### 9. Technical Considerations
- Architektur-Skizze (high-level).
- Datenmodell-Änderungen.
- API-Endpoints (neu/geändert).
- Dependencies (intern und extern).
- Migration Strategy falls nötig.

### 10. Rollout Plan
- Phasen: Internal Alpha, Closed Beta, Open Beta, GA.
- Feature Flags und Targeting.
- Kill Switch Strategie.
- Kommunikation: Release Notes, Help Center, Sales Enablement.

### 11. Risks und Mitigations
Tabelle mit:
- Risiko
- Wahrscheinlichkeit (low/medium/high)
- Impact (low/medium/high)
- Mitigation
- Owner

### 12. Open Questions
- Ungeklärte Punkte mit Owner und Deadline.
- Annahmen, die noch validiert werden müssen.

### 13. Appendix
- Customer Interview Highlights.
- Competitive Analysis (3 bis 5 Konkurrenzprodukte).
- Verwandte Dokumente und Decision Logs.

## Format
- Markdown mit klarer Heading-Hierarchie.
- Tabellen für Vergleiche und Risiko-Matrix.
- Bullet Points statt Fliesstext, wo möglich.
- Versionierung im Header (v0.1 Draft, v1.0 Approved).
- Stakeholder-Liste mit Status (Draft/Review/Approved).

## Einschränkungen
- Keine Lösung beschreiben, bevor das Problem klar ist.
- Jede Anforderung muss testbar sein.
- Keine Adjektive ohne Zahlen ("schnell" ist kein Requirement, "p95 unter 200ms" schon).
- Wenn etwas unklar ist, als Open Question markieren statt zu erfinden.
- Schweizer Rechtschreibung; deutsche Fachbegriffe wo etabliert.
```
{% endcode %}

## Quellen

**Autor:** Industrie-Praxis (Product Management, Marty Cagan, Lenny Rachitsky u.a.) **Werk:** Etablierte Praxis aus Produktmanagement und Requirements Engineering **Link:** [Lenny's Newsletter — How to Write a Great PRD](https://www.lennysnewsletter.com/p/how-to-write-a-great-prd) **Typ:** industrie-praxis

**Ergänzende Quellen:**

* Buch: Marty Cagan — _Inspired: How to Create Tech Products Customers Love_, Wiley (2017)
* Artikel: [Lenny Rachitsky — How to Write a Great PRD](https://www.lennysnewsletter.com/p/how-to-write-a-great-prd)
* Website: [ProductPlan — PRD Guide](https://www.productplan.com/glossary/product-requirements-document/)
