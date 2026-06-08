---
title: "Ideal Customer Profile (ICP)"
space: problem-space
skill: ideal-customer-profile-icp
---

# Ideal Customer Profile (ICP)

### Kurzbeschreibung:

Ein strategisches Profil deines perfekten Kunden, das die Merkmale jener Unternehmen oder Personen beschreibt, die den höchsten Nutzen aus deinem Produkt ziehen und gleichzeitig den grössten Wert für dein Geschäft generieren.

### Einsatzzweck:

Einsatz in frühen Phasen der Produktentwicklung, im Go-to-Market und in der kontinuierlichen Verfeinerung der Vertriebs- und Marketingstrategie. Das ICP fokussiert Ressourcen auf jene Zielgruppe, bei der Produkt-Market-Fit am wahrscheinlichsten ist und schärft Positionierung, Messaging sowie Lead-Qualifizierung. Besonders relevant für B2B-Geschäftsmodelle, SaaS und Account-Based Marketing.

### Kurzanleitung:

1. **Datenbasis schaffen:** Sammle Informationen über deine besten bestehenden Kunden. Nutze CRM-Daten, Interviews und Nutzungsdaten. Bei neuen Produkten arbeitest du mit Hypothesen und Marktanalysen.
2. **Best Customer Analyse:** Identifiziere deine Top-Kunden anhand von Kriterien wie Customer Lifetime Value, Retention, Weiterempfehlungsrate und geringem Support-Aufwand.
3. **Firmographische Merkmale definieren:** Beschreibe Branche, Unternehmensgrösse, Mitarbeiterzahl, Umsatz, Standort und Reifegrad. Beispiel: Schweizer KMU im Finanzsektor mit 50 bis 250 Mitarbeitenden.
4. **Technographische Merkmale ergänzen:** Halte fest, welche Tools, Plattformen oder Tech-Stacks deine Idealkunden nutzen. Das hilft bei Integrationsfragen und Kanalwahl.
5. **Pain Points und Trigger identifizieren:** Definiere die zentralen Probleme, die dein Produkt löst. Beschreibe auslösende Ereignisse wie Wachstum, Regulierungsänderungen oder neue Konkurrenz.
6. **Buying Center mappen:** Identifiziere relevante Rollen im Kaufprozess; Entscheider, Beeinflusser, User und Budget-Owner. Das ICP beschreibt das Unternehmen, die Buyer Persona ergänzt die einzelnen Personen.
7. **Negativkriterien festhalten:** Definiere bewusst, wer NICHT zu deinem ICP gehört. Das verhindert verschwendete Vertriebsressourcen und schärft den Fokus.
8. **ICP dokumentieren:** Fasse alle Merkmale in einem One-Pager zusammen. Nutze klare Kategorien und konkrete Werte statt vager Beschreibungen.
9. **Validieren und iterieren:** Teste das ICP an realen Sales-Pipelines und Marketing-Kampagnen. Überprüfe alle 6 bis 12 Monate, ob die Definition noch zur Realität passt und passe sie an.
10. **Operationalisieren:** Übersetze das ICP in konkrete Filter für Lead-Scoring, Account-Listen, Targeting-Kriterien und Sales-Qualifikation. Nur ein gelebtes ICP entfaltet seinen Nutzen.

### Link auf Miro-Template:

{% embed url="https://miro.com/templates/b2b-ideal-customer-profile-icp-template/" %}

### Beispielprompt:

{% code overflow="wrap" %}
```
# ICP Generator Prompt

## Rolle
Du bist Senior Strategy Consultant mit Fokus auf B2B SaaS und Go-to-Market. Du hast für Firmen wie HubSpot, Salesforce und Atlassian Ideal Customer Profiles entwickelt.

## Kontext
**Unternehmen:** [Name einfügen]
**Produkt/Service:** [Kurze Beschreibung, max. 3 Sätze]
**Aktuelle Kunden (falls vorhanden):** [Top 5 Kunden mit Branche und Grösse]
**Markt:** [Geografie, Branche]
**Preisgestaltung:** [ARR/MRR Range oder Lizenzmodell]

## Aufgabe
Erstelle ein detailliertes Ideal Customer Profile basierend auf dem JTBD-Framework und den klassischen Firmographics/Technographics Dimensionen.

## Struktur des Outputs

### 1. Firmographics
- Branche (NACE/NOGA Codes wenn möglich)
- Unternehmensgrösse (Mitarbeitende, Umsatz)
- Geografie und Sprachregion
- Reifegrad/Lebenszyklus des Unternehmens

### 2. Technographics
- Bestehender Tech-Stack (Must-have, Nice-to-have)
- Digitaler Reifegrad
- Integrationsanforderungen

### 3. Buying Center
- Economic Buyer (Rolle, KPIs, typische Einwände)
- Champion (Rolle, persönliche Motivation)
- End User (Rolle, tägliche Pain Points)
- Blocker (typische Skeptiker)

### 4. Jobs to be Done
- Functional Job: Was muss erledigt werden?
- Emotional Job: Wie soll sich der Kunde fühlen?
- Social Job: Wie soll der Kunde wahrgenommen werden?

### 5. Trigger Events
- 3 bis 5 konkrete Ereignisse, die den Kaufprozess auslösen.

### 6. Disqualifier
- Welche Kunden sind explizit NICHT im ICP und warum?

### 7. Hypothesen zur Validierung
- 5 testbare Hypothesen mit Methode (Interview, Survey, Datenanalyse).

## Format
- Klar strukturiert mit Headings.
- Bullet Points für Listen.
- Eine prägnante Executive Summary am Anfang (max. 5 Sätze).

## Einschränkungen
- Keine generischen Aussagen wie "alle KMU".
- Jedes Attribut muss konkret und messbar sein.
- Wenn Annahmen getroffen werden, explizit als Annahme markieren.
```
{% endcode %}

### Credits

**Autor:** Lincoln Murphy (popularisiert im SaaS-Kontext)\
**Framework:** Ideal Customer Profile (ICP)\
**Jahr:** ca. 2014\
**Quellen:**

* Website: [sixteenventures.com/ideal-customer-profile](https://sixteenventures.com/ideal-customer-profile)
* Buch: _Customer Success_ von Nick Mehta, Dan Steinman, Lincoln Murphy (2016)
