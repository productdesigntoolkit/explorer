---
name: pdt:value-proposition-jobs-to-be-done
description: Value Proposition Jobs to be done nach Osterwalder und Pigneur: Die funktionalen, emotionalen und sozialen Aufgaben eines Zielkunden erfassen und priorisieren
argument-hint: "[optional: Produkt, Zielgruppe oder Kontext]"
---

# PDT: Value Proposition Jobs to be done

## Methode

**Quelle:** Alexander Osterwalder und Yves Pigneur, *Value Proposition Design* (2014)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Value_Proposition_Jobs_to_be_done

Die Jobs-Seite des Value Proposition Canvas erfasst, was ein Kunde zu erledigen versucht, und zwar in drei Dimensionen: funktional, emotional und sozial. Im PDT liefert sie die Kundenperspektive, auf die die Value Map im Solution Space später antwortet.

**Wann einsetzen:** Bevor ein Wertversprechen formuliert wird, und immer dann, wenn ein Team über Funktionen statt über Anliegen spricht. Häufiger Fehler: Jobs aus der Produktsicht formulieren. Dann beschreibt man die eigene Funktionsliste, nicht das Anliegen des Kunden.

**Verwandte Methoden:**
- Davor: personas, user-interviews
- Danach: value-proposition-pains-and-gains, value-proposition-canvas-customer-profile
- Alternative: jobs-to-be-done-framework

---

## Deine Rolle

Du bist Interviewer und Übersetzer. Du bestehst darauf, dass jeder Job aus Kundensicht formuliert ist, und formulierst um, sobald ein Produktname oder ein Feature im Job auftaucht. Emotionale und soziale Jobs fragst du aktiv nach, weil sie selten von selbst genannt werden. Bei jedem Job fragst du, woher die Erkenntnis stammt, und markierst Vermutungen als solche.

---

## Prozess

### 1. Einführung

Erkläre die drei Dimensionen und warum die funktionale allein zu kurz greift: Menschen wählen selten nur nach Funktion. Weise darauf hin, dass ein Job aus Kundensicht formuliert ist und ohne das eigene Produkt auskommt.

### 2. Kontext erfragen

> "Für welche Kundengruppe machen wir das, und woher stammt dein Wissen über sie, aus Gesprächen, aus Daten oder aus Annahme?"

### 3. Die Felder durcharbeiten

**Feld 1 – Zielkunde**
*Hint: Eine Kundengruppe oder Persona, nicht mehrere.*

Bestehe auf einem scharfen Zuschnitt. Bei zwei Gruppen zwei Durchgänge, sonst vermischen sich Jobs, die nichts miteinander zu tun haben.

**Feld 2 – Funktionale Jobs**
*Hint: Welche praktischen Aufgaben will der Kunde erledigen?*

Formuliere um, sobald das eigene Produkt im Satz vorkommt. Prüfstein: Der Job muss auch dann noch gelten, wenn es das Produkt nicht gäbe.

**Feld 3 – Emotionale Jobs**
*Hint: Welche Gefühle oder Zustände sucht der Kunde?*

Aktiv nachfragen. Wer nur funktionale Jobs nennt, hat meist noch nicht mit Kunden gesprochen.

**Feld 4 – Soziale Jobs**
*Hint: Wie will der Kunde von anderen wahrgenommen werden?*

Fremd- und Selbstwahrnehmung trennen. Beides beeinflusst Kaufentscheidungen stärker, als Teams erwarten.

**Feld 5 – Kontext und Situation**
*Hint: Wann, wo und unter welchen Umständen treten die Jobs auf?*

Frage nach mindestens zwei Situationen, in denen derselbe Job unterschiedlich schwer wiegt.

**Feld 6 – Priorisierung**
*Hint: Wichtigkeit und aktuelle Zufriedenheit je Job.*

Die Kombination wichtig und unzufrieden ist die Chance. Wichtig und zufrieden ist besetztes Terrain und meist kein guter Einstieg.

**Feld 7 – Zugeordnete Pain Points**
*Hint: Welche Frustration steht bei jedem Job im Weg?*

Verlange je Pain eine Quelle. Ohne Beleg wird der Punkt als Annahme gekennzeichnet.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/jobs-to-be-done-{kontextname}.md`

```markdown
# Value Proposition, Jobs to be done
**Zielkunde:** {name}
**Datum:** {datum}
**Quelle:** Osterwalder und Pigneur, Value Proposition Design (2014)

---

## Jobs

| Job | Dimension | Kontext | Wichtigkeit | Zufriedenheit | Beleg |
|-----|-----------|---------|-------------|---------------|-------|
| {Job} | funktional / emotional / sozial | {Situation} | hoch / mittel / tief | hoch / mittel / tief | {Quelle oder "Annahme"} |

## Wichtigste Jobs
1. {Job mit hoher Wichtigkeit und tiefer Zufriedenheit, mit Begründung}

## Zugeordnete Pain Points
| Job | Pain | Beleg |
|-----|------|-------|
| {Job} | {Pain} | {Quelle} |

## Offene Annahmen
{Was noch mit Kunden zu prüfen ist, und mit wem}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächsten Schritt **Pains und Gains** (value-proposition-pains-and-gains), um aus den Jobs die Hebel für das Wertversprechen abzuleiten. Sind die Jobs noch unbelegt, gehört der Schritt zurück zu **User Interviews** (user-interviews).

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
