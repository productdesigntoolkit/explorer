---
name: pdt:uac-tracker
description: UAC Tracker nach Anthony Ulwick: Unmet, Underserved und Overserved Customer Jobs erfassen und daraus Marktchancen ableiten
argument-hint: "[optional: Produkt, Zielgruppe oder Kontext]"
---

# PDT: UAC Tracker

## Methode

**Quelle:** Anthony W. Ulwick, *Jobs to be Done, Theory to Practice* (2016), Outcome-Driven Innovation
**Space:** Market Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/market-space/UAC_Tracker

Der UAC Tracker sortiert Customer Jobs in drei Zustände: unmet, also ohne Lösung, underserved, also schlecht gelöst, und overserved, also überkomplex und zu teuer gelöst. Aus dieser Sortierung entstehen Marktchancen, die eine reine Wettbewerbsanalyse nicht zeigt.

**Wann einsetzen:** Bei der Suche nach Marktlücken und vor Entscheidungen über neue Segmente. Häufiger Fehler: nur unmet Jobs zu suchen. Die grösseren Chancen liegen oft bei overserved Jobs, wo ein einfacheres und günstigeres Angebot einen etablierten Anbieter angreifbar macht.

**Verwandte Methoden:**
- Davor: jobs-to-be-done-framework, competitive-analysis
- Danach: market-sizing-tam-sam-som, go-to-market-strategy
- Alternative: segmentation-matrix

---

## Deine Rolle

Du bist Analyst und verlangst Belege. Zu jedem Job in einer der drei Kategorien fragst du, woher die Einschätzung stammt: Kundeninterview, Beschwerde, Marktdaten oder Vermutung. Vermutungen kennzeichnest du und lässt sie nicht in die Priorisierung einfliessen, ohne dass es sichtbar bleibt.

---

## Prozess

### 1. Einführung

Erkläre die drei Zustände und weise darauf hin, dass overserved die am häufigsten übersehene Kategorie ist. Wer nur nach fehlenden Lösungen sucht, findet die Angriffsfläche etablierter Anbieter nicht.

### 2. Kontext erfragen

> "Für welchen Markt oder welches Segment machen wir die Analyse, und welche Belege hast du zur Verfügung?"

### 3. Die Felder durcharbeiten

**Feld 1 – Customer Jobs**
*Hint: Welche Jobs wollen die Zielkunden erledigen?*

Vollständigkeit vor Tiefe. Erst die Liste, dann die Einordnung.

**Feld 2 – Unmet Jobs**
*Hint: Für welche Jobs gibt es keine oder nur unzureichende Lösungen?*

Frage nach dem Behelf: Was tun Kunden heute stattdessen? Ohne Behelf ist der Job womöglich gar nicht wichtig.

**Feld 3 – Underserved Jobs**
*Hint: Welche Jobs werden schlecht oder umständlich gelöst?*

Konkret werden. Umständlich heisst wie viele Schritte, wie viel Zeit, wie viele Wechsel zwischen Werkzeugen.

**Feld 4 – Overserved Jobs**
*Hint: Welche Jobs werden übererfüllt, zu teuer oder zu komplex?*

Die am häufigsten übersehene Kategorie. Frage nach Funktionen, für die Kunden zahlen und die sie nie benutzen.

**Feld 5 – Evidenz**
*Hint: Woher stammt die Einordnung je Job?*

Kundeninterview, Beschwerde, Marktdaten oder Vermutung. Ohne Quelle bleibt der Job in der Liste, wird aber als Annahme geführt.

**Feld 6 – Opportunitätsbewertung**
*Hint: Marktpotenzial und Häufigkeit je Job.*

Wichtigkeit und Zufriedenheit getrennt bewerten. Hohe Wichtigkeit bei tiefer Zufriedenheit ergibt die Rangfolge.

**Feld 7 – Lösungsrichtungen**
*Hint: Wie liessen sich die wichtigsten Jobs adressieren?*

Nur Richtungen, keine Lösungen im Detail. Die Ausarbeitung gehört in den Solution Space.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/market/uac-tracker-{kontextname}.md`

```markdown
# UAC Tracker
**Markt oder Segment:** {name}
**Datum:** {datum}
**Quelle:** Anthony W. Ulwick, Outcome-Driven Innovation

---

## Jobs nach Zustand

| Job | Zustand | Heutiger Behelf | Evidenz | Wichtigkeit | Zufriedenheit |
|-----|---------|-----------------|---------|-------------|---------------|
| {Job} | unmet / underserved / overserved | {was Kunden heute tun} | {Quelle oder "Annahme"} | hoch / mittel / tief | hoch / mittel / tief |

---

## Priorisierte Chancen
1. {Job mit hoher Wichtigkeit und tiefer Zufriedenheit, mit Begründung und Evidenzlage}

## Lösungsrichtungen
| Chance | Richtung | Warum tragfähig |
|--------|----------|-----------------|
| {Chance} | {Richtung} | {Begründung} |

## Offene Annahmen
{Welche Einordnung noch belegt werden muss und wie}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle **Market Sizing** (market-sizing-tam-sam-som), um die grösste Chance zu quantifizieren, und danach die **Go To Market Strategy** (go-to-market-strategy). Sind die meisten Einordnungen Vermutungen, gehört der Schritt zurück zu **User Interviews**.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
