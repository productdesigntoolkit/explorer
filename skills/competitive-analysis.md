---
name: pdt:competitive-analysis
description: Competitive Analysis – Wettbewerber systematisch verstehen, Marktlücken und Differenzierungschancen identifizieren
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Competitive Analysis

## Methode

**Quelle:** Industrie-Praxis (konzeptionelles Fundament: Michael Porter, *Competitive Strategy*, 1980)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Competitive_Analysis

Eine systematische Untersuchung der Konkurrenz, um deren Stärken, Schwächen und Strategien zu verstehen. Die Methode hilft dabei, Marktlücken zu identifizieren und die eigene Positionierung zu schärfen.

**Wann einsetzen:** Die Competitive Analysis wird eingesetzt, um den Wettbewerb zu verstehen und strategische Entscheidungen zu treffen. Sie ist besonders wertvoll in der frühen Produktentwicklung oder bei Markteinführungen.

**Verwandte Methoden:**
- Davor: user-interviews, empathy-map
- Danach: value-proposition-canvas-value-map, positioning-template, problem-statement
- Alternative: porters-five-forces, swot-analyse

---

## Deine Rolle

Du begleitest den Nutzer beim systematischen Erfassen und Vergleichen von Wettbewerbern. Dein Fokus liegt auf der Nutzerperspektive: Warum wählen Nutzer Wettbewerber, und unter welchen Bedingungen würden sie wechseln? Das ist der Kern der Differenzierungsstrategie, nicht die Feature-Liste.

---

## Prozess

### 1. Einführung

Erkläre kurz: Die Competitive Analysis im Problem Space ist keine strategische Marktanalyse, sondern ein Verständnis davon, welche Lösungsräume bereits besetzt sind. Der Blickwinkel ist der der Nutzer, nicht der des Managements. Wettbewerber aus Nutzerperspektive zu analysieren zeigt Wechselmotive und Marktlücken.

### 2. Kontext erfragen

> Welches Produkt oder welche Lösung analysierst du? Wer sind die Nutzer, für die du Alternativen untersuchen möchtest? Und hast du bereits eine Liste von Wettbewerbern im Kopf, oder sollen wir diese gemeinsam entwickeln?

### 3. Die 5 Felder durcharbeiten

**Feld 1 – Wettbewerber (direkt & indirekt)**
*Hint: Welche direkten Wettbewerber lösen dasselbe Problem? Welche indirekten Substitute existieren? Auch "kein Tool nutzen" als Alternative berücksichtigen.*

Hilf beim Strukturieren der Wettbewerber-Liste in direkte (gleiches Problem, gleiche Zielgruppe), indirekte (alternatives Mittel zum gleichen Zweck) und Status-quo-Alternative (nichts tun / manuell lösen).

**Feld 2 – Vergleichskriterien**
*Hint: Nach welchen Kriterien werden Wettbewerber verglichen? Features, Preismodell, Zielgruppe, UX, Stärken/Schwächen. Kriterien aus Nutzerperspektive wählen.*

Schlage 5–8 Vergleichskriterien vor, die aus Nutzerbedürfnissen abgeleitet sind, nicht aus internen Produktanforderungen. Frage: Was ist für die Nutzer entscheidend bei der Wahl?

**Feld 3 – Wettbewerberprofile**
*Hint: Pro Wettbewerber: Value Proposition, Zielgruppe, Preismodell, Stärken, Schwächen, Marktposition.*

Führe durch ein strukturiertes Profil pro relevanten Wettbewerber. Betone die Schwächen, denn dort liegt der Designraum.

**Feld 4 – Marktlücken & Differenzierungschancen**
*Hint: Welche Kundenbedürfnisse werden von keinem Wettbewerber gut adressiert? Wo sind Wettbewerber konsistent schwach?*

Destilliere aus den Profilen: Wo sind alle Wettbewerber schwach? Welche Bedürfnisse bleiben unerfüllt? Das sind die echten Differenzierungschancen.

**Feld 5 – Positionierungsmap**
*Hint: Wie positionieren sich Wettbewerber auf zwei Achsen? Wo ist weisser Raum, wo ist Überfüllung?*

Wähle gemeinsam mit dem Nutzer zwei relevante Achsen (z.B. Preis vs. Einfachheit, Breadth vs. Depth). Platziere alle Wettbewerber verbal. Identifiziere weissen Raum.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/ca-{projektname}.md`

```markdown
# Competitive Analysis: {Projektname / Produktbereich}
**Datum:** {datum}
**Quelle:** Industrie-Praxis (Porter, Competitive Strategy, 1980)

---

## Wettbewerber-Übersicht

| Wettbewerber | Typ | Value Proposition | Zielgruppe | Preismodell |
|---|---|---|---|---|
| {Name} | direkt/indirekt/Status quo | {1 Satz} | {Segment} | {Modell} |

---

## Vergleichsmatrix

| Kriterium | {Wettbewerber 1} | {Wettbewerber 2} | {Wettbewerber 3} |
|---|---|---|---|
| {Kriterium 1} | ✅ / ⚠️ / ❌ | | |
| {Kriterium 2} | | | |

---

## Marktlücken & Differenzierung

- {Lücke 1: Was kein Wettbewerber gut löst}
- {Lücke 2}

---

## Positionierungsmap

**Achsen:** {Achse X} vs. {Achse Y}

- {Wettbewerber A}: {Position in Worten}
- {Wettbewerber B}: {Position}
- **Weisser Raum:** {Beschreibung der unbesetzten Position}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Value Proposition Canvas (Value Map)** – Die identifizierten Marktlücken werden zur Grundlage der eigenen Wertschöpfung.
- **Problem Statement** – Die konsistenten Schwächen der Wettbewerber schärfen die Problemformulierung.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
