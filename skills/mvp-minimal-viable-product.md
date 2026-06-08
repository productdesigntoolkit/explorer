---
name: pdt:mvp-minimal-viable-product
description: MVP — Minimal Viable Product – Das kleinste Produkt definieren, das eine vollständige Hypothese testet, ohne Zeit und Ressourcen zu verschwenden
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: MVP — Minimal Viable Product

## Methode

**Quelle:** Eric Ries, *The Lean Startup, How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses* (2011)
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/MVP_-_Minimal_Viable_Product

Das Minimal Viable Product (MVP) ist eine frühe Version eines Produkts mit nur den grundlegendsten Funktionen, die ausreichen, um erste Nutzerfeedbacks zu sammeln und die Kernhypothesen zu validieren. Es ermöglicht schnelles Lernen mit minimalem Aufwand.

**Wann einsetzen:** Das MVP wird in der frühen Entwicklungsphase eingesetzt, um Produktideen kostengünstig zu testen, bevor grössere Investitionen getätigt werden. Es eignet sich besonders gut für neue Produkte, Startups oder wenn Unsicherheit über Marktbedürfnisse besteht.

**Verwandte Methoden:**
- Davor: How Might We Questions, Crazy 8s, Value Proposition Canvas Value Map
- Danach: Usability Testing, Pilot / Beta, KPI & Success Metrics Definition
- Alternative: Prototyping, Pilot / Beta

---

## Deine Rolle

Du hilfst beim Definieren eines fokussierten MVPs — nicht als Entschuldigung für schlechte Qualität, sondern als strategisches Instrument um die riskanteste Annahme zuerst zu testen. Du verhindere Feature-Creep und stellst konsequent die Frage: "Brauchen wir das wirklich für den Kernwert?" Du strukturierst den Build-Measure-Learn-Zyklus konkret.

---

## Prozess

### 1. Einführung

Erkläre den PDT-Grundsatz: Ein MVP ist kein halbes Produkt. Es ist das kleinste Produkt, das eine vollständige Hypothese testet — nicht perfekt, aber vollständig in seiner Kernfunktion. Der grösste Fehler: MVP als Entschuldigung für Schludrigkeit. Der zweitgrösste: zu viele Features die alle "minimal wichtig" sind.

### 2. Kontext erfragen

> Was ist die Produktidee oder das Problem, für das du ein MVP definieren möchtest — und was ist die eine Kernhypothese, die du damit testen willst?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – MVP-Hypothese**
*Hint: Format: "Wir glauben, dass [Zielgruppe] [Lösung] nutzen werden, weil [Annahme]. Wir messen das durch [Metrik]."*

Schärfe die Hypothese bis sie in diesem Format steht. Eine Hypothese pro MVP.

**Feld 2 – Kernwert (was das MVP MUSS)**
*Hint: Welche minimale Funktionalität ist nötig um den Kernwert zu liefern? Der MVP muss einen vollständigen Job erledigen können.*

Definiere 2–3 Must-Have-Features. Für jedes: warum ist es zwingend für den Kernwert?

**Feld 3 – Bewusst ausgeschlossen**
*Hint: Was gehört explizit NICHT in den MVP? Diese Liste ist genauso wichtig wie die In-Scope-Liste.*

Erstelle eine bewusste Out-of-Scope-Liste. Für jedes Feature: warum ist es für die Hypothese nicht nötig?

**Feld 4 – Validierungskriterien**
*Hint: Woran erkennen wir, ob der MVP die Hypothese bestätigt oder widerlegt? Was muss eintreten damit wir skalieren, pivotieren oder stoppen?*

Definiere konkrete Go/Pivot/Stop-Kriterien mit Zahlen. Was ist der Schwellenwert?

**Feld 5 – Build-Measure-Learn Zyklus**
*Hint: Was wird gebaut, wie wird gemessen, was soll gelernt werden? Zeitrahmen für den ersten Zyklus.*

Strukturiere den ersten Zyklus: Wer baut was bis wann? Wie wird gemessen? Wann wird ausgewertet?

**Feld 6 – Riskanteste Annahme**
*Hint: Was ist die eine Annahme, die wenn falsch, das gesamte Geschäftsmodell infrage stellt?*

Identifiziere die eine riskanteste Annahme. Ist der MVP darauf fokussiert? Falls nicht: adjustieren.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/mvp-{kontextname}.md`

```markdown
# MVP Definition: {Produktname}
**Datum:** {datum}
**Quelle:** Eric Ries — The Lean Startup (2011)

---

## MVP-Hypothese
Wir glauben, dass {Zielgruppe} {Lösung} nutzen werden, weil {Annahme}. Wir messen das durch {Metrik}.

## Riskanteste Annahme
{Die eine kritische Annahme}

## In Scope (Must-Have)
1. **{Feature}** — {Begründung: warum für Kernwert nötig}
2. **{Feature}** — {Begründung}

## Out of Scope (bewusst ausgeschlossen)
- **{Feature}:** {Begründung: warum nicht nötig}
- **{Feature}:** {Begründung}

## Validierungskriterien
| Szenario | Kriterium | Entscheidung |
|---------|---------|------------|
| Go (skalieren) | {Metrik} > {Wert} | Weiterbauen |
| Pivot | {Bedingung} | Richtung ändern |
| Stop | {Bedingung} | Projekt einstellen |

## Build-Measure-Learn Zyklus
- **Build:** {Was bis wann}
- **Measure:** {Wie und womit}
- **Learn:** {Auswertung wann, mit wem}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: das MVP mit einem Usability Test prüfen bevor es an echte Nutzer geht, oder direkt den Pilot / Beta-Plan entwickeln um den Build-Measure-Learn-Zyklus zu operationalisieren.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
