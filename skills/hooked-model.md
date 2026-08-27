---
name: pdt:hooked-model
description: Hooked Model nach Nir Eyal: Den Vier-Phasen-Zyklus aus Trigger, Aktion, variabler Belohnung und Investment gestalten und ethisch prüfen
argument-hint: "[optional: Produkt, Zielgruppe oder Kontext]"
---

# PDT: Hooked Model

## Methode

**Quelle:** Nir Eyal, *Hooked, How to Build Habit-Forming Products* (2014)
**Space:** Market Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/market-space/Hooked_Model

Das Hooked Model beschreibt, wie Produkte Gewohnheiten aufbauen: ein Trigger führt zu einer Aktion, die Aktion zu einer variablen Belohnung, die Belohnung zu einem Investment, das den nächsten Trigger vorbereitet. Im PDT steht es im Market Space und gestaltet Bindung, nachdem ein Produkt am Markt ist.

**Wann einsetzen:** Wenn Nutzer zwar gewonnen, aber nicht gehalten werden, und wenn bestehende Funktionen auf ihre Bindungswirkung geprüft werden sollen. Es setzt einen belegten Nutzen voraus. Häufiger Fehler: den Zyklus als Wachstumstrick behandeln und die Ethikprüfung überspringen.

**Verwandte Methoden:**
- Davor: aarrr-framework, product-market-fit
- Danach: loyalty-builder, marketing-kpi-dashboard
- Alternative: flywheel-model

---

## Deine Rolle

Du gestaltest den Zyklus und prüfst ihn zugleich. Du verlangst für jede Phase eine konkrete Ausgestaltung und fragst am Ende die Manipulation Matrix ab, ohne sie als Formalie zu behandeln. Wenn der Nutzen des Produkts für den Nutzer unklar bleibt, sagst du das deutlich und empfiehlst, den Zyklus nicht zu bauen.

---

## Prozess

### 1. Einführung

Erkläre den Unterschied zwischen externem und internem Trigger: Solange nur externe Trigger wirken, hängt Nutzung an Werbebudget. Gewohnheit beginnt beim internen Trigger.

### 2. Kontext erfragen

> "Um welches Produkt geht es, und wie oft nutzen Menschen es heute, gemessen und nicht geschätzt?"

### 3. Die Felder durcharbeiten

**Feld 1 – Externe Trigger**
*Hint: Wie kommen Nutzer erstmals in Berührung?*

Unterscheide gekaufte von verdienten Triggern. Beide haben einen Preis, der eine in Geld, der andere in Zeit.

**Feld 2 – Interne Trigger**
*Hint: Welche Emotion oder Situation löst die Nutzung von selbst aus?*

Frage nach dem Moment vor der Nutzung. Ohne internen Trigger bleibt das Produkt dauerhaft auf Werbung angewiesen.

**Feld 3 – Aktion**
*Hint: Was ist die einfachste Handlung, die zur Belohnung führt?*

Nach dem Fogg Behavior Model braucht es Motivation, Fähigkeit und Auslöser gleichzeitig. Frage, welcher der drei heute fehlt.

**Feld 4 – Variable Belohnung**
*Hint: Was ist unvorhersehbar an der Belohnung?*

Getrennt nach Tribe, also soziale Anerkennung, Hunt, also Suchen und Finden, und Self, also Kompetenz und Fortschritt. Eine feste Belohnung erzeugt keine Gewohnheit.

**Feld 5 – Investment**
*Hint: Was investiert der Nutzer, das die künftige Nutzung wertvoller macht?*

Prüfe, ob das Investment den nächsten Trigger vorbereitet. Sonst ist es ein Aufwand ohne Gegenwert.

**Feld 6 – Ethikprüfung**
*Hint: Würdest du das Produkt selbst nutzen, und verbessert es das Leben der Nutzer?*

Beide Fragen einzeln beantworten lassen. Wer beides verneint, baut Ausbeutung. Halte das im Ergebnis fest, statt es zu übergehen.

**Feld 7 – Messgrössen des Zyklus**
*Hint: Wie oft durchlaufen Nutzer den vollen Zyklus?*

Zeit zwischen Sessions, Retention an Tag 1, 7 und 30, Tiefe der Investition. Dazu die Phase, in der Nutzer aussteigen.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/market/hooked-model-{kontextname}.md`

```markdown
# Hooked Model
**Produkt:** {name}
**Datum:** {datum}
**Quelle:** Nir Eyal, Hooked (2014)

---

## Der Zyklus

| Phase | Ausgestaltung | Heute vorhanden | Lücke |
|-------|---------------|-----------------|-------|
| Externer Trigger | {Ausgestaltung} | ja / nein / teilweise | {Lücke} |
| Interner Trigger | {Emotion oder Situation} | ja / nein / teilweise | {Lücke} |
| Aktion | {Handlung, Reibung} | ja / nein / teilweise | {Lücke} |
| Variable Belohnung | Tribe: {…} · Hunt: {…} · Self: {…} | ja / nein / teilweise | {Lücke} |
| Investment | {was investiert wird} | ja / nein / teilweise | {Lücke} |

## Ethikprüfung
**Würde ich es selbst nutzen:** ja / nein, {Begründung}
**Verbessert es das Leben der Nutzer:** ja / nein, {Begründung}
**Einordnung:** Facilitator / Peddler / Entertainer / Dealer

## Messgrössen
| Messgrösse | Wert heute | Ziel |
|-----------|-----------|------|
| Zeit zwischen Sessions | {Wert} | {Ziel} |
| Retention Tag 1 / 7 / 30 | {Werte} | {Ziel} |
| Tiefe der Investition | {Wert} | {Ziel} |

## Abbruchstelle und nächster Schritt
{In welcher Phase Nutzer aussteigen und was zuerst geändert wird}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle das **Marketing KPI Dashboard** (marketing-kpi-dashboard), um die Messgrössen dauerhaft zu verfolgen, und den **Loyalty Builder** (loyalty-builder) für die Bindung jenseits des Zyklus. Fällt die Ethikprüfung negativ aus, gehört der Schritt zurück ins Produkt, nicht ins Marketing.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
