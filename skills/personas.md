---
name: pdt:personas
description: Personas – Datenbasierte Nutzerprofile erstellen, die das Team fokussiert und Designentscheidungen verankert
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Personas

## Methode

**Quelle:** Alan Cooper, *The Inmates Are Running the Asylum* (1999)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Personas

Personas sind fiktive, aber datenbasierte Charaktere, die typische Nutzergruppen eines Produkts repräsentieren. Sie helfen dabei, Designentscheidungen zu treffen und das Team auf die tatsächlichen Bedürfnisse der Zielgruppe zu fokussieren.

**Wann einsetzen:** Verwende Personas in der Konzeptphase, um ein gemeinsames Verständnis der Zielgruppe zu schaffen. Sie eignen sich besonders für Produktstrategie-Meetings, Feature-Priorisierung und als Entscheidungshilfe bei Designfragen.

**Verwandte Methoden:**
- Davor: user-interviews, empathy-map, surveys-questionnaires
- Danach: user-journey-mapping, problem-statement, value-proposition-canvas-customer-profile
- Alternative: empathy-map, jobs-to-be-done-framework

---

## Deine Rolle

Du hilfst beim Entwickeln einer vollständigen, verhaltensbasierten Persona, die das Team wirklich nutzt. Du betonst, dass Demografics Kontext sind, nicht Kern: Verhaltensmuster und Motivationen stehen im Vordergrund. Im PDT starten Personas als Proto-Personas (Hypothesen) und werden mit echten Daten verfeinert. Du fragst aktiv nach echten Zitaten aus Interviews, denn diese machen Personas lebendig.

---

## Prozess

### 1. Einführung

Erkläre kurz: Personas verdichten Nutzerforschung in ein kommunizierbares Profil, das das gesamte Team im Kopf behält. Der häufigste Fehler ist, demografische Daten in den Vordergrund zu stellen. Alter und Beruf sind Kontext, nicht Kern. Was eine Persona treibt, frustriert und wie sie sich verhält, das ist das Herzstück. Im PDT: maximal 3 Personas, eine pro primäres Nutzersegment.

### 2. Kontext erfragen

> Für welches Produkt oder welchen Service erstellen wir die Persona? Welche Nutzergruppe soll abgebildet werden, und hast du bereits Erkenntnisse aus Interviews, Empathy Maps oder Research, auf die wir aufbauen können?

### 3. Die 7 Felder durcharbeiten

**Feld 1 – Name & Repräsentationsfoto**
*Hint: Gib der Persona einen realen Namen und beschreibe ein passendes Foto. Das macht die Persona greifbar und im Team diskutierbar.*

Wähle einen realitätsnahen Namen (kein Klischee). Beschreibe das Foto kurz: echte Person, kein Stockfoto-Klischee. Das macht die Persona im Team lebendig und einprägsam.

**Feld 2 – Demografische Daten**
*Hint: Alter, Beruf, Ausbildung, Wohnort, Familiensituation — nur was für das Produkt relevant ist.*

Halte Demografics knapp: Nur Details, die das Nutzungsverhalten tatsächlich erklären. Frage: Warum ist dieses Datum relevant? Wenn keine Antwort: weglassen.

**Feld 3 – Ziele & Motivationen**
*Hint: Was will die Persona erreichen? Funktionale Ziele und emotionale Ziele.*

Das ist das Herzstück. Frage nach zwei Ebenen: Was will sie konkret tun (funktional)? Und wie will sie sich dabei fühlen oder was will sie damit signalisieren (emotional)?

**Feld 4 – Frustrationen & Pain Points**
*Hint: Was nervt die Persona heute? Welche Hindernisse erlebt sie bei der Zielerreichung?*

Frage nach konkreten Situationen, in denen die Persona frustriert ist. Zitate aus Interviews sind hier Gold wert. Direkte Verbindung zu Pains in der Empathy Map.

**Feld 5 – Verhaltensmuster**
*Hint: Welche Tools, Kanäle und Gewohnheiten hat die Persona? Was tut sie täglich, wöchentlich?*

Beschreibe typische Verhaltensweisen: Welche Tools nutzt sie? Wie informiert sie sich? Welche Routinen hat sie, die für das Produkt relevant sind?

**Feld 6 – Nutzungskontext**
*Hint: In welcher Situation nutzt die Persona das Produkt? Wo, wann, mit wem? Mobil oder Desktop? Gestresst oder entspannt?*

Frage nach dem Nutzungskontext: Wann würde die Persona das Produkt öffnen? Wo (unterwegs, Büro, Zuhause)? In welchem emotionalen Zustand? Das bestimmt UX-Anforderungen.

**Feld 7 – Charakteristisches Zitat**
*Hint: Ein O-Ton der Persona — idealerweise aus echten Interviews. Fasst ihre Haltung oder ihr grösstes Problem in einem Satz.*

Finde einen Satz, der die Persona auf den Punkt bringt. Wenn echte Zitate vorhanden sind, nutze diese. Wenn nicht: formuliere einen Satz, der ihre wichtigste Frustration oder Motivation ausdrückt.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/persona-{name}.md`

```markdown
# Persona: {Name}
**Datum:** {datum}
**Quelle:** Alan Cooper, The Inmates Are Running the Asylum (1999)
**Status:** Proto-Persona (Hypothese) / Validiert

---

## Steckbrief

| | |
|---|---|
| **Name** | {Vorname Nachname} |
| **Alter** | {Alter} |
| **Beruf** | {Titel / Rolle} |
| **Wohnort** | {Stadt / Region} |
| **Familiensituation** | {Relevant oder weglassen} |

---

> "{Charakteristisches Zitat aus echten Interviews oder als Synthese}"

---

## Ziele & Motivationen

**Funktional:** {Was sie konkret erreichen will}
**Emotional:** {Wie sie sich dabei fühlen will}

---

## Frustrationen & Pain Points

- {Konkreter Schmerzpunkt 1}
- {Konkreter Schmerzpunkt 2}
- ...

---

## Verhaltensmuster

- **Tools:** {Was sie täglich nutzt}
- **Informationsquellen:** {Wie sie sich informiert}
- **Routinen:** {Relevante Gewohnheiten}

---

## Nutzungskontext

- **Wann:** {Typischer Zeitpunkt der Produktnutzung}
- **Wo:** {Ort / Gerät}
- **Zustand:** {Emotional / kognitiv beim Nutzen}

---

## Verbindung zu Research

*Diese Persona basiert auf:* {Anzahl Interviews / Surveys / Beobachtungen}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **User Journey Mapping** – Die Persona wird durch eine Journey geführt, um Schmerzpunkte in konkreten Situationen zu verorten.
- **Problem Statement** – Die Frustration der Persona wird in ein scharf formuliertes Problemstatement überführt.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
