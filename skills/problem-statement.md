---
name: pdt:problem-statement
description: Problem Statement – Das zentrale Nutzerproblem präzise und lösungsneutral formulieren, Voraussetzung für den Solution Space
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Problem Statement

## Methode

**Quelle:** IDEO; Stanford d.school, *Design Thinking Bootleg, Define Phase* (2010/2018)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Problem_Statement

Ein Problem Statement ist eine präzise, nutzerzentrierte Formulierung eines Design-Problems, die das "Was", "Wer" und "Warum" klar definiert. Es dient als Grundlage für alle nachfolgenden Design-Entscheidungen und hält das Team fokussiert.

**Wann einsetzen:** Das Problem Statement wird nach der Recherche- und Analysephase eingesetzt, um die gesammelten Erkenntnisse in eine klare Problemdefinition zu überführen. Es ist die Voraussetzung für den Einstieg in den Solution Space.

**Verwandte Methoden:**
- Davor: personas, user-journey-mapping, user-interviews, empathy-map
- Danach: value-proposition-canvas-customer-profile, how-might-we, product-vision-statement
- Alternative: jobs-to-be-done-framework

---

## Deine Rolle

Du hilfst beim Schärfen und Formulieren eines Problem Statements, das das gesamte Team ausrichten kann. Du hältst den entscheidenden Test aufrecht: Lässt sich das Statement ohne Erwähnung eines Produkts oder einer Lösung formulieren? Du prüfst auch, ob das Problem messbar und für die Zielgruppe wirklich relevant ist. Im PDT gilt: Kein Solution Space ohne validiertes Problem Statement.

---

## Prozess

### 1. Einführung

Erkläre kurz: Das Problem Statement schliesst die Problem Discovery ab. Es ist der Vertrag des Teams, auf welches Problem wir uns fokussieren. Ein häufiger Fehler ist das Überspringen dieses Schritts, direkt von Research zur Lösung zu springen. Gutes Problem Statement: spezifisch, lösungsneutral, validiert. Es soll auf einer A4-Seite passen und von allen Stakeholdern unterschrieben werden können.

### 2. Kontext erfragen

> Welche Research-Erkenntnisse oder Personas hast du bereits? Oder möchtest du das Problem Statement von Grund auf entwickeln? Schildere kurz, worum es geht, damit wir das Problem gemeinsam schärfen können.

### 3. Die 7 Felder durcharbeiten

**Feld 1 – Zielgruppe**
*Hint: Für wen besteht dieses Problem? Nicht "alle" oder "KMUs", sondern spezifisch, z.B. "Produktmanager in Series-A-Startups ohne dediziertes Designteam".*

Hilf beim Schärfen der Zielgruppe: Je spezifischer, desto besser. Frage: Wer leidet am stärksten unter diesem Problem? Wer hat den dringendsten Bedarf?

**Feld 2 – Das Problem**
*Hint: Was ist das eigentliche Problem? Als Beobachtung formulieren, nicht als Lösung. Test: Lässt sich das Statement ohne Produkt formulieren?*

Führe den Lösungsneutralitäts-Test durch: Wenn das Problem "kein X haben" ist, ist es noch lösungsorientiert. Das echte Problem ist das Ergebnis, das fehlt, oder die Situation, die nicht funktioniert.

**Feld 3 – Kontext & Auslöser**
*Hint: In welcher konkreten Situation tritt das Problem auf? Welcher Trigger löst es aus?*

Frage: Wann genau passiert das Problem? Was geht dem voraus? Je konkreter der Kontext, desto klarer wird die Lösungsrichtung. "Jeden Montagmorgen, wenn das Team..."

**Feld 4 – Relevanz & Konsequenzen**
*Hint: Was sind die Folgen, wenn das Problem nicht gelöst wird? Quantifiziere wenn möglich: Zeitverlust, Kosten, Frustration.*

Frage: Was kostet das Problem konkret? Zeit, Geld, Reputation, Stress? Quantifizierung macht das Problem für Stakeholder greifbarer und priorisierbar.

**Feld 5 – Aktuelle Lösungsversuche**
*Hint: Was tun Nutzer heute, um das Problem zu umgehen? Warum sind diese Workarounds unzureichend?*

Workarounds zeigen die Schmerzintensität: Wenn jemand einen aufwändigen Umweg geht, ist der Schmerz real. Was funktioniert daran nicht? Das ist der Ansatzpunkt.

**Feld 6 – Erfolgskriterien**
*Hint: Woran erkennen wir, dass das Problem gelöst ist? Messbare Kriterien formulieren.*

Hilf beim Formulieren messbarer Erfolgskriterien: "Bearbeitungszeit sinkt von X auf Y", "Fehlerrate unter Z%", "Nutzer schaffen Onboarding in unter 5 Minuten."

**Feld 7 – Problem Statement (1 Satz)**
*Hint: Fasse alles in einem Satz zusammen: "[Zielgruppe] hat das Problem [Problem], weil [Ursache], was zu [Konsequenz] führt."*

Formuliere gemeinsam den finalen Satz. Teste ihn: Ist er spezifisch? Lösungsneutral? Validiert durch Research? Dieser Satz ist der Vertrag mit dem Team.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/ps-{projektname}.md`

```markdown
# Problem Statement: {Projektname}
**Datum:** {datum}
**Quelle:** IDEO / Stanford d.school, Design Thinking Bootleg (2010/2018)
**Research-Basis:** {Grundlage des Statements}

---

## Das Problem Statement

> **[Zielgruppe]** hat das Problem, **[Problem]**, weil **[Ursache]**, was zu **[Konsequenz]** führt.

---

## Zielgruppe

{Wer, konkret und spezifisch}

---

## Das Problem

{Lösungsneutrale Beschreibung, als Beobachtung formuliert}

---

## Kontext & Auslöser

- **Wann:** {Konkrete Situation}
- **Auslöser:** {Was das Problem triggert}

---

## Konsequenzen

| Für den Nutzer | Für das Business |
|----------------|-----------------|
| {Zeitverlust / Kosten / Stress} | {Impact auf Kennzahlen} |

---

## Aktuelle Lösungsversuche

| Workaround | Warum unzureichend |
|------------|-------------------|
| {Was Nutzer heute tun} | {Wo es scheitert} |

---

## Erfolgskriterien

- {Messbares Kriterium 1: "Von X auf Y"}
- {Messbares Kriterium 2}
- ...

---

## Stakeholder-Sign-off

☐ {Name} (Rolle) · ☐ {Name} (Rolle) · ☐ {Name} (Rolle)

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **How Might We** – Das Problem Statement wird in "Wie könnten wir..."-Fragen umgewandelt, um die Ideation zu starten.
- **Value Proposition Canvas (Customer Profile)** – Das validierte Problem bildet die Grundlage für das Customer Profile.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
