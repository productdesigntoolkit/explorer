---
name: pdt:value-proposition-canvas-customer-profile
description: Value Proposition Canvas – Customer Profile – Customer Jobs, Pains und Gains systematisch erfassen als Grundlage für die Value Map
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Value Proposition Canvas — Customer Profile

## Methode

**Quelle:** Alexander Osterwalder, Yves Pigneur, Greg Bernarda, Alan Smith, *Value Proposition Design* (2014)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Value_Proposition_Canvas_Customer_Profile

Das Customer Profile ist die linke Hälfte des Value Proposition Canvas und dient der systematischen Analyse der Zielkunden. Es bildet deren Jobs, Pains und Gains ab und schafft die Grundlage für die Value Map auf der Lösungsseite.

**Wann einsetzen:** Einsatz am Ende der Problem Discovery, nach Empathy Map und Nutzerinterviews. Das Customer Profile wird ausgefüllt, bevor die Lösungsseite (Value Map) bearbeitet wird. Jobs, Pains und Gains werden bewusst ohne Lösungsbezug beschrieben.

**Verwandte Methoden:**
- Davor: empathy-map, jobs-to-be-done-framework, user-interviews
- Danach: value-proposition-canvas-value-map, problem-statement, how-might-we
- Alternative: empathy-map, personas

---

## Deine Rolle

Du begleitest den Nutzer beim vollständigen Ausfüllen des Customer Profiles. Du hältst konsequent die Lösungsneutralität aufrecht: Jobs, Pains und Gains werden ohne Bezug zur eigenen Lösung formuliert. Du differenzierst zwischen den Gain-Typen nach Osterwalder (required, expected, desired, unexpected) und zwischen extremen und moderaten Pains. Diese Unterscheidungen bestimmen später, was eine Lösung wirklich leisten muss.

---

## Prozess

### 1. Einführung

Erkläre kurz: Das Customer Profile beschreibt, was Kunden in ihrem Leben oder ihrer Arbeit versuchen zu erledigen (Jobs), was dabei frustriert oder hindert (Pains), und was sie erreichen möchten (Gains). Der häufigste Fehler: Jobs mit der eigenen Lösung im Kopf zu formulieren. Richtig ist: Jobs unabhängig von jedem Produkt beschreiben. Das Customer Profile ist die Grundlage für die Value Map, wo dann gezeigt wird, wie die eigene Lösung diese Jobs/Pains/Gains adressiert.

### 2. Kontext erfragen

> Für welches Kundensegment oder welche Persona erstellst du das Customer Profile? Und welche Erkenntnisse aus Empathy Map, User Interviews oder JTBD-Analyse hast du bereits, die wir einbetten können?

### 3. Die 3 Felder durcharbeiten

**Feld 1 – Customer Jobs**
*Hint: Was versucht der Kunde zu erledigen? Unterscheide functional (Aufgaben), social (Wahrnehmung) und emotional (Gefühle) Jobs. Ohne Lösungsannahmen formulieren.*

Sammle und kategorisiere alle Jobs. Nutze die drei Dimensionen:
- Functional Jobs: "Was muss erledigt werden?" (konkrete Aufgaben und Probleme)
- Social Jobs: "Wie will der Kunde von anderen wahrgenommen werden?"
- Emotional Jobs: "Wie will der Kunde sich dabei fühlen?"

Teste jeden Job: Lässt er sich ohne Erwähnung einer Lösung formulieren? Wenn nicht, ist er noch zu lösungsorientiert.

**Feld 2 – Pains**
*Hint: Was frustriert den Kunden vor, während oder nach dem Job? Unerwünschte Ergebnisse, Hindernisse, Risiken. Extreme vs. moderate Pains unterscheiden.*

Erfasse Pains in drei Kategorien:
- Unerwünschte Ergebnisse (was schiefläuft)
- Hindernisse (was den Job schwierig macht)
- Risiken (was schiefgehen könnte)

Differenziere Intensität: Extreme Pains (rechtfertigen eine Lösung, Kunden zahlen dafür) vs. moderate Pains (tolerierbar). Nur extreme Pains sind echte Ansatzpunkte.

**Feld 3 – Gains**
*Hint: Welche Ergebnisse will der Kunde erreichen? Osterwalder unterscheidet required, expected, desired, unexpected Gains.*

Erfasse Gains in vier Typen nach Osterwalder:
- Required (Minimum-Erwartung, ohne die eine Lösung unbrauchbar ist)
- Expected (selbstverständlich, implizit erwartet)
- Desired (explizit erwünscht, aber nicht immer vorhanden)
- Unexpected (positiv überrascht, nicht erwartet, differenzierend)

Unexpected Gains sind das Differenzierungspotenzial. Frage: Was würde den Kunden angenehm überraschen?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/vpc-cp-{segment}.md`

```markdown
# Value Proposition Canvas — Customer Profile: {Segment / Persona}
**Datum:** {datum}
**Quelle:** Osterwalder et al., Value Proposition Design (Strategyzer, 2014)

---

## Kundensegment

{Name und Kurzbeschreibung der Zielgruppe / Persona}

---

## Customer Jobs

### Functional Jobs
| Job | Wichtigkeit | Häufigkeit |
|-----|-------------|-----------|
| {Was erledigt werden muss} | hoch/mittel/niedrig | täglich/wöchentlich/selten |

### Social Jobs
- {Wie der Kunde wahrgenommen werden will}

### Emotional Jobs
- {Wie der Kunde sich fühlen will}

---

## Pains

### Extreme Pains (Ansatzpunkte für Lösungen)
| Pain | Typ | Beschreibung |
|------|-----|-------------|
| {Frustration / Hindernis / Risiko} | unerwünschtes Ergebnis / Hindernis / Risiko | {Konkrete Beschreibung} |

### Moderate Pains (tolerierbar, aber vorhanden)
- {Pain}
- ...

---

## Gains

| Gain | Typ | Priorität |
|------|-----|-----------|
| {Was erreicht werden soll} | required / expected / desired / unexpected | hoch/mittel/niedrig |

**Unexpected Gains (Differenzierungspotenzial):**
- {Was angenehm überraschen würde}

---

## Verbindung zur Value Map

*Hinweis: Dieses Customer Profile ist die Grundlage für die Value Map. Dort wird gezeigt, wie die eigene Lösung die Jobs erledigt, Pains lindert und Gains schafft.*

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Value Proposition Canvas (Value Map)** – Die Lösungsseite zeigt, wie Products & Services, Pain Relievers und Gain Creators auf das Customer Profile antworten.
- **Problem Statement** – Die extremen Pains und wichtigsten Jobs liefern den direkten Input für ein scharf formuliertes Problem Statement.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
