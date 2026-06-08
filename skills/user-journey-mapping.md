---
name: pdt:user-journey-mapping
description: User Journey Mapping – Die Nutzererfahrung über Zeit visualisieren, Schmerzpunkte priorisieren und Designchancen aufdecken
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: User Journey Mapping

## Methode

**Quelle:** Industrie-Praxis (systematisch aufgearbeitet von Jim Kalbach, *Mapping Experiences*, O'Reilly, 2016)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/User_Journey_Mapping

User Journey Mapping visualisiert die komplette Erfahrung eines Nutzers mit einem Produkt oder Service über alle Berührungspunkte hinweg. Die Methode hilft dabei, Schmerzpunkte zu identifizieren und die Nutzererfahrung ganzheitlich zu verbessern.

**Wann einsetzen:** Diese Methode wird eingesetzt, um bestehende Nutzererfahrungen zu analysieren, Verbesserungspotenziale zu identifizieren und ein gemeinsames Verständnis für die Nutzererfahrung im Team zu schaffen. Besonders wertvoll in der Analyse- und Konzeptionsphase.

**Verwandte Methoden:**
- Davor: user-interviews, empathy-map, personas
- Danach: problem-statement, value-proposition-canvas-customer-profile, stakeholder-mapping
- Alternative: empathy-map, customer-journey-mapping

---

## Deine Rolle

Du hilfst beim Aufbau einer User Journey Map, die wirklich als Werkzeug zur Priorisierung von Problemen dient, nicht als dekorative Infografik. Du fokussierst auf die emotionale Kurve und die Tiefpunkte, denn dort sind die Designchancen. Du klärst den Unterschied zur Customer Journey Map: User Journey fokussiert auf die Produktnutzung, Customer Journey auf die gesamte Geschäftsbeziehung.

---

## Prozess

### 1. Einführung

Erkläre kurz: Die User Journey Map macht die Nutzererfahrung über Zeit sichtbar — im Unterschied zur Empathy Map, die einen einzelnen Moment fokussiert. Nach ersten Interviews erstellt, zeigt sie systematisch, wo die grössten Reibungspunkte liegen. Im PDT gilt: Eine gute Journey Map ist kein schönes Bild, sondern ein Entscheidungsrahmen. Die Tiefpunkte in der Emotionskurve sind die Orte, an denen Produktarbeit den grössten Impact hat.

### 2. Kontext erfragen

> Für welche Persona und welches Szenario erstellen wir die User Journey Map? Hast du bereits Erkenntnisse aus Interviews oder Beobachtungen, die wir einbetten können?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – Persona & Szenario**
*Hint: Welche Persona wird abgebildet? In welchem spezifischen Szenario? Eine Journey pro Persona und Szenario.*

Definiere klar: Wessen Journey wird abgebildet, und in welchem konkreten Szenario? Beispiel: "Anna (Persona Freelance-Designerin), erstmalige Buchung eines Co-Working-Platzes." Nicht zu breit: Eine Journey pro Persona und Szenario.

**Feld 2 – Phasen der Journey**
*Hint: Welche zeitlichen Phasen durchläuft der Nutzer? Phasen benennen die zum Produkt passen.*

Erarbeite gemeinsam die Phasen, die zum Szenario passen. Nicht immer sind alle klassischen Phasen (Awareness, Consideration, Purchase...) relevant. Frage: Wo fängt die Journey für diesen Nutzer wirklich an?

**Feld 3 – Aktionen pro Phase**
*Hint: Was tut der Nutzer konkret in jeder Phase? Beobachtbare Handlungen — nicht was er denkt oder fühlt.*

Liste konkrete, beobachtbare Handlungen auf: Was klickt die Person? Was sucht sie? Was schreibt sie? Handlungen sind das Gerüst der Journey. Gedanken und Gefühle kommen später.

**Feld 4 – Touchpoints & Kanäle**
*Hint: Wo interagiert der Nutzer mit dem Produkt oder der Marke? Digital, physisch, sozial.*

Erfasse alle Kontaktpunkte: Wo berührt die Nutzerreise das Produkt oder die Marke? Website, App, Email, Support-Chat, Empfehlung von Bekannten. Touchpoints offenbaren auch, wo Kontrolle über die Erfahrung fehlt.

**Feld 5 – Emotionen & Schmerzpunkte**
*Hint: Wie fühlt sich der Nutzer in jeder Phase? Wo sind die grössten Frustrationspunkte?*

Zeichne die Emotionskurve: Hoch- und Tiefpunkte benennen. Frage besonders nach Frustrationsmomenten: Was macht den Nutzer ungeduldig, verwirrt oder enttäuscht? Diese Tiefpunkte sind die Designchancen.

**Feld 6 – Verbesserungsmöglichkeiten**
*Hint: Wo sind die grössten Lücken zwischen Erwartung und Erlebnis?*

Leite aus den Tiefpunkten konkrete Verbesserungsmöglichkeiten ab. Priorisiere: Welche Lücken haben den grössten negativen Impact? Welche können mit vertretbarem Aufwand geschlossen werden?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/ujm-{persona}-{szenario}.md`

```markdown
# User Journey Map: {Persona} – {Szenario}
**Datum:** {datum}
**Quelle:** Industrie-Praxis (Kalbach, Mapping Experiences, 2016)

---

## Kontext

| | |
|---|---|
| **Persona** | {Name + Kurzbeschreibung} |
| **Szenario** | {Was die Person versucht zu erreichen} |
| **Research-Basis** | {Interviews / Beobachtungen als Grundlage} |

---

## Journey Map

| Phase | Aktionen | Touchpoints | Emotionen | Schmerzpunkte |
|-------|----------|-------------|-----------|---------------|
| {Phase 1} | {Was getan wird} | {App / Web / Email} | 😊 / 😐 / 😤 | {Was frustriert} |
| {Phase 2} | | | | |
| {Phase 3} | | | | |

---

## Emotionskurve

```
Positiv   ↑  
          |    ●                      ●
          |  ●   ●      ●          ●
----------+--------●--------●●●●●---------→ Zeit
          |              ●
Negativ   ↓
          {Phase 1}  {Phase 2}  {Phase 3}
```

{Narrative Beschreibung der Kurve: Wo sind Hochpunkte, wo Tiefpunkte und warum}

---

## Grösste Schmerzpunkte (priorisiert)

| Priorität | Phase | Schmerzpunkt | Ursache | Lösungsrichtung |
|-----------|-------|-------------|---------|----------------|
| 1 (hoch) | {Phase} | {Konkreter Schmerz} | {Warum er auftritt} | {Erste Idee} |
| 2 | | | | |

---

## Verbesserungsmöglichkeiten

- {Konkrete Massnahme 1 mit Impact-Einschätzung}
- {Konkrete Massnahme 2}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Problem Statement** – Die grössten Schmerzpunkte aus der Journey werden in ein präzises Problem Statement überführt.
- **Value Proposition Canvas (Customer Profile)** – Die Pains aus der Journey fliessen direkt ins Customer Profile ein.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
