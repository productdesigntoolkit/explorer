---
name: pdt:product-vision-statement
description: Product Vision Statement – Das erste Deliverable im Solution Space, das die Produktidee in ein kommunizierbares Format bringt und dem Team eine gemeinsame Sprache gibt
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Product Vision Statement

## Methode

**Quelle:** Geoffrey A. Moore, *Crossing the Chasm, Marketing and Selling High-Tech Products to Mainstream Customers* (1991)
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/Product_Vision_Statement

Ein Product Vision Statement ist eine prägnante Aussage, die die langfristige Zielrichtung und den gewünschten Impact eines Produkts beschreibt. Es dient als Nordstern für alle Produktentscheidungen und kommuniziert die Motivation hinter der Produktentwicklung.

**Wann einsetzen:** Diese Methode wird zu Beginn des Solution Space eingesetzt, um Klarheit über die strategische Ausrichtung zu schaffen. Sie hilft bei der Fokussierung des Teams, der Kommunikation mit Stakeholdern und als Entscheidungshilfe während des gesamten Entwicklungsprozesses.

**Verwandte Methoden:**
- Davor: Problem Statement, Value Proposition Canvas Value Map, How Might We Questions
- Danach: MVP — Minimal Viable Product, Value Proposition Canvas Value Map, Product Vision Board
- Alternative: Product Vision Board

---

## Deine Rolle

Du führst durch das Geoffrey-Moore-Format und stellst sicher, dass das Vision Statement in 1 Minute erklärbar ist — der Elevator-Pitch-Test. Du hinterfragst vage Formulierungen und hilfst, alle 7 Felder präzise zu füllen. Das Ergebnis ist ein Statement, das Klarheit schafft: Wer, Was, Wie und Warum besser.

---

## Prozess

### 1. Einführung

Erkläre das Geoffrey-Moore-Format: "Für [Zielkunde], der [Bedürfnis], ist [Produkt] ein [Kategorie], das [Schlüsselvorteil]. Im Gegensatz zu [Alternative] hat unser Produkt [Differenzierung]." Dieses Format erzwingt Klarheit — vage Antworten funktionieren nicht. Der Elevator-Pitch-Test: kann das Statement in 60 Sekunden überzeugend erklärt werden?

### 2. Kontext erfragen

> Welches Produkt oder welche Produktidee soll mit einem Vision Statement beschrieben werden — und gibt es bereits ein Problem Statement oder eine Value Proposition als Ausgangsbasis?

### 3. Die 7 Felder durcharbeiten

**Feld 1 – Zielkunde**
*Hint: Für wen ist das Produkt? Der primäre Nutzer in einem Satz — spezifisch und erkennbar.*

Sei konkret: nicht "Unternehmen", sondern "mittelgrosse E-Commerce-Teams ohne dedizierte Data-Analysten".

**Feld 2 – Kundenbedürfnis**
*Hint: Was ist das zentrale Bedürfnis oder Problem, das adressiert wird? Direkt aus dem Problem Statement.*

Muss aus dem Problem Statement stammen. Falls keins vorliegt: kurz erarbeiten.

**Feld 3 – Produktname**
*Hint: Wie heisst das Produkt? Auch Arbeitstitel sind ok — Hauptsache konsistent im Team.*

Auch Arbeitstitel sind wertvoll — sie geben dem Team eine gemeinsame Sprache.

**Feld 4 – Produktkategorie**
*Hint: Was ist es? (Web-App, Mobile App, B2B-SaaS, Hardware, Service...) Die Kategorie setzt Erwartungen.*

Frage: Welche Erwartungen setzt diese Kategorie? Sind sie korrekt?

**Feld 5 – Schlüsselvorteil**
*Hint: Was ist der primäre Nutzen für den Kunden? Der eine Grund, warum er das Produkt nutzen wird.*

Nur ein Vorteil — der wichtigste. Falls mehrere genannt werden: priorisieren.

**Feld 6 – Differenzierung**
*Hint: Was unterscheidet das Produkt von bestehenden Alternativen? Warum ist diese Lösung besser?*

Konkret: im Vergleich zu welcher Alternative ist das Produkt besser, und worin genau?

**Feld 7 – Vision Statement (Geoffrey Moore Format)**
*Hint: "Für [Zielkunde], der [Bedürfnis], ist [Produkt] ein [Kategorie], das [Schlüsselvorteil]. Im Gegensatz zu [Alternative] hat unser Produkt [Differenzierung]."*

Fülle das Template mit den erarbeiteten Antworten. Dann: Elevator-Pitch-Test — liest es sich in 60 Sekunden überzeugend?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/pvs-{kontextname}.md`

```markdown
# Product Vision Statement: {Produktname}
**Datum:** {datum}
**Quelle:** Geoffrey Moore — Crossing the Chasm (1991)

---

## Vision Statement

> Für **{Zielkunde}**, der **{Bedürfnis}**, ist **{Produktname}** ein **{Kategorie}**, das **{Schlüsselvorteil}**. Im Gegensatz zu **{Alternative}** hat unser Produkt **{Differenzierung}**.

---

## Felder

| Feld | Inhalt |
|------|--------|
| Zielkunde | {spezifische Beschreibung} |
| Kundenbedürfnis | {Problem / Job to be done} |
| Produktname | {Name / Arbeitstitel} |
| Kategorie | {Produkttyp} |
| Schlüsselvorteil | {primärer Nutzen} |
| Alternative | {Konkurrent / Status quo} |
| Differenzierung | {Was macht es besser} |

## Elevator-Pitch-Test
{Kann das Statement in 60 Sekunden überzeugend erklärt werden? Anmerkungen.}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: das Vision Statement als Basis für den MVP nutzen (welche Features unterstützen die Vision, welche nicht?), oder das Statement direkt in das Product Vision Board überführen.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
