---
name: pdt:service-blueprints
description: Service Blueprints – Komplexe Services in horizontalen Layern visualisieren, Fail Points finden und Übergaben zwischen Frontstage und Backstage optimieren
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Service Blueprints

## Methode

**Quelle:** G. Lynn Shostack, *Designing Services That Deliver, Harvard Business Review* (1984)
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/Service_Blueprints

Ein Service Blueprint visualisiert einen Service-Prozess in horizontalen Layern: Physical Evidence, Customer Actions, Onstage Actions, Backstage Actions und Support Processes. Drei Trennlinien — Line of Interaction, Line of Visibility und Line of Internal Interaction — machen sichtbar, wer mit wem wann interagiert und welche Prozesse unsichtbar bleiben.

**Wann einsetzen:** Einsatz im Solution Space bei der Entwicklung oder Optimierung von Services, bei denen mehrere Abteilungen koordiniert werden müssen. Service Blueprints sind besonders wertvoll für hybride Services (digital + physisch) und wenn Pain Points systematisch entlang der gesamten Wertschöpfungskette identifiziert werden sollen.

**Verwandte Methoden:**
- Davor: User Journey Mapping, Stakeholder Mapping, Prototyping
- Danach: Product Vision Board, PRD Document
- Alternative: User Journey Mapping, Customer Journey Mapping

---

## Deine Rolle

Du strukturierst den Service Blueprint als Textrepräsentation der 5 Layer mit den 3 Trennlinien. Da visuelle Canvas-Tools fehlen, arbeitest du in tabellarischer und strukturierter Textform. Du prüfst jeden Layer auf Vollständigkeit und markierst Fail Points und Optimierungspotenziale explizit. Der Fokus liegt auf Klarheit der Übergaben — nicht auf Vollständigkeit aller Details.

---

## Prozess

### 1. Einführung

Erkläre das Shostack-Modell: drei Trennlinien separieren die 5 Layer. Die Line of Interaction trennt Customer Actions von Onstage. Die Line of Visibility trennt Onstage von Backstage. Die Line of Internal Interaction trennt Backstage von Support Processes. Fail Points entstehen typischerweise an diesen Linien — dort brechen Services.

### 2. Kontext erfragen

> Welchen Service oder Prozess soll der Blueprint abbilden — und welche Persona oder Nutzergruppe steht im Fokus?

### 3. Die 7 Felder durcharbeiten

**Feld 1 – Service-Szenario**
*Hint: Welcher Service oder Prozess wird blueprintet? Welche Persona und welcher spezifische Service-Touchpoint steht im Fokus?*

Grenze den Scope klar ab: welcher Service von Anfang bis Ende? Nicht der gesamte Unternehmens-Prozess.

**Feld 2 – Physical Evidence**
*Hint: Welche physischen oder digitalen Artefakte nimmt der Kunde wahr? Website, App-UI, Verpackung, Quittung, Räumlichkeiten, E-Mail, Ticket.*

Dies ist der oberste Layer. Liste alle Artefakte die der Kunde sieht, berührt oder erhält.

**Feld 3 – Customer Actions**
*Hint: Was tut der Kunde sichtbar? Aktionen, die direkt mit dem Service interagieren. Getrennt von Frontstage durch die Line of Interaction.*

Liste alle Schritte des Kunden chronologisch. Klar trennen: was tut der Kunde, was passiert mit ihm?

**Feld 4 – Frontstage (Onstage) Actions**
*Hint: Welche Handlungen von Service-Mitarbeitern oder Systemen sind für den Kunden sichtbar?*

--- LINE OF INTERACTION --- (Trennlinie zwischen Kunde und Service)

Was sieht der Kunde vom Service? Direkte Interaktionen, sichtbare Systemreaktionen, Mitarbeitende im direkten Kontakt.

**Feld 5 – Backstage Actions**
*Hint: Welche Handlungen von Mitarbeitern oder Systemen sind für den Kunden unsichtbar, aber notwendig?*

--- LINE OF VISIBILITY --- (Trennlinie zwischen sichtbar und unsichtbar)

Was passiert hinter den Kulissen? Bearbeitung, interne Prüfungen, unsichtbare Systemaktionen.

**Feld 6 – Support Processes**
*Hint: Welche internen Systeme, Datenbanken, APIs, Tools und Drittprozesse stützen den Service?*

--- LINE OF INTERNAL INTERACTION --- (Trennlinie zwischen direkt Beteiligten und Infrastruktur)

IT-Infrastruktur, externe APIs, Drittsysteme, interne Tools die den Service ermöglichen.

**Feld 7 – Fail Points & Optimierungschancen**
*Hint: Wo sind die kritischen Übergaben zwischen den Layern? Wo entstehen Verzögerungen, Fehler oder Brüche?*

Markiere alle Fail Points und priorisiere sie nach Kundenimpact. Was sind die 3 wichtigsten Verbesserungen?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/sbp-{kontextname}.md`

```markdown
# Service Blueprint: {Service-Name}
**Datum:** {datum}
**Persona:** {Hauptfigur im Blueprint}
**Quelle:** G. Lynn Shostack — HBR (1984)

---

## Service-Szenario
{Kurze Beschreibung: welcher Service, von wo bis wo}

---

## PHYSICAL EVIDENCE (oberster Layer)
{Liste aller Artefakte die der Kunde wahrnimmt}

## CUSTOMER ACTIONS
{Chronologische Liste der Kundenschritte}

--- LINE OF INTERACTION ---

## FRONTSTAGE (ONSTAGE) ACTIONS
{Sichtbare Service-Aktivitäten}

--- LINE OF VISIBILITY ---

## BACKSTAGE ACTIONS
{Unsichtbare interne Aktivitäten}

--- LINE OF INTERNAL INTERACTION ---

## SUPPORT PROCESSES
{IT, APIs, Drittsysteme, Infrastruktur}

---

## Fail Points & Optimierungen

| # | Fail Point | Layer | Kundenimpact | Optimierung |
|---|-----------|-------|-------------|------------|
| 1 | {Beschreibung} | {Layer} | Hoch/Mittel/Tief | {Massnahme} |
| 2 | | | | |
| 3 | | | | |

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: die identifizierten Fail Points als User Stories oder Anforderungen ins PRD Document überführen, oder das Blueprint als Input für das Product Vision Board nutzen.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
