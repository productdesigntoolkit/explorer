---
name: pdt:jobs-to-be-done-framework
description: Jobs-to-be-Done (JTBD) Framework – Den eigentlichen Job hinter der Nachfrage verstehen: functional, emotional, social und messbar
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Jobs-to-be-Done (JTBD) Framework

## Methode

**Quelle:** Clayton M. Christensen, *Competing Against Luck* (2016) & Anthony W. Ulwick, *What Customers Want* (2005) — PDT-Synthese beider Schulen
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Jobs-to-be-Done_Framework

Das Jobs-to-be-Done Framework hilft dabei, die eigentlichen Aufgaben und Bedürfnisse zu verstehen, für die Kunden ein Produkt "anheuern". Es fokussiert auf den funktionalen, emotionalen und sozialen Job, den ein Produkt erfüllen soll, und ist vollständig lösungsneutral.

**Wann einsetzen:** Verwende diese Methode in der Recherche- und Definitionsphase, um Kundenbedürfnisse aus einer neuen Perspektive zu betrachten. Besonders wertvoll wenn bestehende Lösungen die wahren Kundenjobs nicht erfüllen oder wenn ein neues Produkt von Grund auf konzipiert wird.

**Verwandte Methoden:**
- Davor: user-interviews, contextual-inquiry-observation, empathy-map
- Danach: value-proposition-canvas-customer-profile, problem-statement, personas
- Alternative: empathy-map, personas

---

## Deine Rolle

Du begleitest den Nutzer beim präzisen Formulieren von Jobs-to-be-Done. Du hältst die Lösungsneutralität konsequent aufrecht: Ein Job ist kein Feature und keine Aktivität. Du unterscheidest Christensens narrativen Ansatz (Kontext und Auslöser) von Ulwicks Outcome-Statements (messbare Erfolgsmetriken) und nutzt beide komplementär. Du fragst aktiv nach dem Kontext: Was löst den Job aus? Das ist der Schlüssel.

---

## Prozess

### 1. Einführung

Erkläre kurz: Jobs-to-be-Done beschreibt, was Nutzer in einer bestimmten Situation erreichen wollen, vollständig unabhängig von Produkten oder Features. Ein Job ist ein Fortschritt, den ein Mensch anstrebt. Das Produkt ist nur ein Mittel. Falsch: "Nutzer wollen eine Aufgaben-App nutzen." Richtig: "Nutzer wollen sicherstellen, dass ihr Team weiss, was zu tun ist." Diese Unterscheidung öffnet den Blick für echte Innovation.

### 2. Kontext erfragen

> Welche Nutzergruppe oder welchen Nutzer möchtest du mit dem JTBD-Framework verstehen? Hast du bereits Erkenntnisse aus Interviews oder Beobachtungen, auf die wir aufbauen können?

### 3. Die 7 Felder durcharbeiten

**Feld 1 – Job Executor (Wer)**
*Hint: Wer führt den Job aus? Die spezifische Person in einer konkreten Situation — nicht eine Persona, sondern ein Moment.*

Formuliere: Wer ist die Person, in welcher konkreten Situation, zu welchem Zeitpunkt? JTBD beschreibt einen Moment, keine Zielgruppe. Beispiel: "Eine Projektleiterin am Montagmorgen, bevor das Teammeeting beginnt."

**Feld 2 – Functional Job (Was)**
*Hint: Was versucht die Person zu erledigen? Formuliere als Verb + Objekt ohne Lösung: "sicherstellen, dass...", "minimieren wie lange es dauert..."*

Hilf beim Formulieren des Jobs ohne Lösungsbezug. Teste: Lässt sich der Job auch ohne das eigene Produkt erledigen? Wenn nein, ist er noch zu lösungsorientiert. Ulwick-Format: "Minimiere die Wahrscheinlichkeit, dass..." oder "Maximiere, wie schnell..."

**Feld 3 – Kontext & Auslöser**
*Hint: Wann und warum tritt dieser Job auf? Was löst ihn aus? Welche Umstände beeinflussen wie er ausgeführt wird?*

Frage nach dem Push (was die aktuelle Situation unbefriedigend macht) und dem Pull (was die neue Lösung attraktiv macht). Nach Christensen: Welches Ereignis löst die Suche nach einer Lösung aus?

**Feld 4 – Emotional Job**
*Hint: Wie will sich die Person dabei fühlen? Sicherheit, Kontrolle, Zugehörigkeit, Stolz. Oft wichtiger als der funktionale Job.*

Frage: Wie möchte sich die Person beim Ausführen des Jobs fühlen? Und wie fühlt sie sich heute? Die emotionale Lücke zwischen Ist und Soll ist oft der wahre Treiber für eine Kaufentscheidung.

**Feld 5 – Social Job**
*Hint: Wie will die Person von anderen wahrgenommen werden, wenn sie den Job erledigt?*

Frage: Was sagt die Art und Weise, wie jemand diesen Job erledigt, über ihn aus? Welches Image oder welche Zugehörigkeit vermittelt es? Social Jobs sind besonders im B2C-Kontext relevant.

**Feld 6 – Desired Outcomes (Metriken)**
*Hint: Wie misst die Person Erfolg bei diesem Job? "Minimiere die Wahrscheinlichkeit, dass..." oder "Maximiere wie schnell..."*

Formuliere 3–5 messbare Outcome-Statements nach Ulwick. Diese werden später zur Grundlage für Opportunity Scoring (welche Outcomes sind wichtig aber unterversorgt?).

**Feld 7 – Bisherige Lösungen & Schwächen**
*Hint: Womit erledigt die Person den Job heute? Was sind die grössten Unzulänglichkeiten?*

Frage: Was nutzt die Person heute? Wie gut funktioniert das? Welche Beschwerden hat sie? Diese Schwächen sind der Einstiegspunkt für die eigene Lösung.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/jtbd-{thema}.md`

```markdown
# Jobs-to-be-Done: {Thema / Nutzergruppe}
**Datum:** {datum}
**Quelle:** Christensen (Competing Against Luck, 2016) & Ulwick (What Customers Want, 2005) — PDT-Synthese

---

## Job Story

**Wenn** {Situation / Kontext / Auslöser},
**will ich** {Functional Job — lösungsneutral formuliert},
**damit** {Erwartetes Ergebnis}.

---

## Job-Dimensionen

| Dimension | Beschreibung |
|-----------|-------------|
| **Functional Job** | {Was erledigt werden muss — als Verb + Objekt} |
| **Emotional Job** | {Wie sich die Person dabei fühlen will} |
| **Social Job** | {Wie sie von anderen wahrgenommen werden will} |

---

## Kontext & Auslöser

- **Push:** {Was die aktuelle Situation unbefriedigend macht}
- **Pull:** {Was die neue Lösung attraktiv macht}
- **Auslösendes Ereignis:** {Was den Suchprozess startet}

---

## Desired Outcomes (nach Ulwick)

1. Minimiere die Wahrscheinlichkeit, dass {unerwünschtes Ergebnis}
2. Maximiere, wie schnell {erwünschtes Ergebnis}
3. ...

---

## Aktuelle Lösung & Schwächen

| Aktuelle Lösung | Schwächen | Opportunity |
|-----------------|-----------|------------|
| {Was genutzt wird} | {Was nicht funktioniert} | {Ansatz für Verbesserung} |

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Value Proposition Canvas (Customer Profile)** – Die Functional/Emotional/Social Jobs werden zu Customer Jobs, Pains und Gains im VPC Customer Profile.
- **Problem Statement** – Der schärfste Job mit den grössten Schwächen der aktuellen Lösungen wird zur Grundlage des Problem Statements.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
