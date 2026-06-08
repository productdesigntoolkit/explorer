---
name: pdt:contextual-inquiry-observation
description: Contextual Inquiry / Observation – Nutzer im natürlichen Umfeld beobachten, unbewusstes Verhalten und versteckte Bedürfnisse aufdecken
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Contextual Inquiry / Observation

## Methode

**Quelle:** Hugh Beyer & Karen Holtzblatt, *Contextual Design, Defining Customer-Centered Systems* (1997)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Contextual_Inquiry_-_Observation

Bei der Contextual Inquiry beobachtest du Nutzer direkt in ihrer natürlichen Arbeits- oder Nutzungsumgebung. Diese ethnografische Forschungsmethode deckt unbewusste Verhaltensweisen und versteckte Bedürfnisse auf, die in Interviews oft nicht zur Sprache kommen.

**Wann einsetzen:** Du setzt diese Methode ein, wenn du das tatsächliche Nutzerverhalten in der realen Umgebung verstehen möchtest. Besonders wertvoll zu Beginn eines Projekts oder bei komplexen Arbeitsprozessen, wo Nutzer ihre Gewohnheiten oft nicht bewusst reflektieren können.

**Verwandte Methoden:**
- Davor: user-interviews, empathy-map
- Danach: affinity-mapping, user-journey-mapping, problem-statement
- Alternative: user-interviews, surveys-questionnaires

---

## Deine Rolle

Du hilfst beim Planen, Strukturieren und Auswerten einer Contextual Inquiry. Du entwickelst Beobachtungsprotokolle, fragst nach Artefakten und Workarounds, und hilfst dabei, Beobachtungen von Interpretationen sauber zu trennen. Workarounds, die Nutzer selbst entwickelt haben, sind besonders wertvoll — sie zeigen ungelöste Probleme direkt.

---

## Prozess

### 1. Einführung

Erkläre kurz: Contextual Inquiry unterscheidet sich von Interviews dadurch, dass beobachtet wird, was wirklich passiert, nicht was erinnert oder kommuniziert wird. Der entscheidende Vorteil ist Validität — Nutzer rationalisieren ihr Verhalten in Interviews, aber im natürlichen Kontext zeigen sie es. Workarounds, die Nutzer entwickelt haben, sind Goldstaub.

### 2. Kontext erfragen

> Was möchtest du beobachten, und in welchem Umfeld findet die Aktivität statt? Geht es um einen Arbeitsablauf im Büro, eine Nutzungssituation zuhause oder unterwegs — und hast du bereits Zugang zu geeigneten Beobachtungspersonen?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – Beobachtungsziel**
*Hint: Was soll beobachtet werden? Welche Verhaltensweisen oder Kontexte sind relevant? Ziel: sehen was Nutzer wirklich tun, nicht was sie sagen zu tun.*

Hilf beim Schärfen des Beobachtungsziels: nicht zu breit ("alles beobachten"), nicht zu eng (nur ein Feature). Ein gutes Ziel fokussiert auf einen Arbeitsablauf oder eine Entscheidungssituation.

**Feld 2 – Setting & Kontext**
*Hint: Wo findet die Beobachtung statt? Im natürlichen Umfeld des Nutzers. Wie wird der Zugang gesichert? Dauer und Zeitpunkt.*

Kläre praktische Details: Dauer (typisch 60–120 Minuten), Aufzeichnung (Einverständnis), Rolle des Beobachters (Fly-on-the-wall vs. Master-Apprentice-Modus nach Holtzblatt).

**Feld 3 – Beobachtungsprotokoll**
*Hint: Was wird notiert? Handlungen, Artefakte, Unterbrechungen, Workarounds, Ausdrücke von Frustration oder Freude.*

Erstelle ein strukturiertes Beobachtungsraster: Zeitstempel, Handlung, Artefakt, Ton (positiv/negativ), Zitat. Trenne Beobachtung von Interpretation explizit.

**Feld 4 – Artefakte & Workarounds**
*Hint: Welche physischen oder digitalen Artefakte nutzen Nutzer? Welche Workarounds haben sie selbst entwickelt?*

Frage explizit nach Post-its, Excel-Sheets, ausgedruckten Listen, Notiz-Apps oder anderen selbstentwickelten Lösungen. Jeder Workaround zeigt ein ungelöstes Problem.

**Feld 5 – Wichtigste Beobachtungen**
*Hint: Was waren die überraschendsten Erkenntnisse? Wo wich das beobachtete Verhalten vom erwarteten ab?*

Fokussiere auf Abweichungen vom erwarteten Verhalten. Was hat den Nutzer verblüfft? Was war anders als angenommen? Diese Abweichungen sind die wertvollsten Insights.

**Feld 6 – Implikationen für das Design**
*Hint: Was bedeuten die Beobachtungen für die Problemdefinition? Welche Annahmen wurden revidiert?*

Übersetze jede wichtige Beobachtung in eine Implikation: "Weil Nutzer X tun, müssen wir Y überdenken." Welche ursprünglichen Annahmen wurden revidiert?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/ci-{projektname}.md`

```markdown
# Contextual Inquiry: {Thema / Aktivität}
**Datum:** {datum}
**Quelle:** Beyer & Holtzblatt, Contextual Design (1997)
**Setting:** {Ort / Umgebung}
**Beobachtete Personen:** {Anzahl und Kurzbeschreibung}

---

## Beobachtungsziel

{Was beobachtet wurde und warum}

---

## Beobachtungsprotokoll

| Zeit | Handlung | Artefakt | Ton | Zitat / Notiz |
|------|----------|----------|-----|---------------|
| {min} | {Was getan wurde} | {Tool/Objekt} | + / – | {Direkte Beobachtung} |

---

## Artefakte & Workarounds

| Artefakt | Zweck | Implikation |
|----------|-------|-------------|
| {Post-it / Excel / ...} | {Warum vorhanden} | {Ungelöstes Problem} |

---

## Wichtigste Beobachtungen

1. {Überraschendste Erkenntnis}
2. {Abweichung vom erwarteten Verhalten}
3. ...

---

## Implikationen für das Design

- **Beobachtung:** {X} → **Implikation:** {Y muss überdacht werden}
- ...

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Affinity Mapping** – Die Beobachtungen aus mehreren Sessions werden geclustert, um Muster sichtbar zu machen.
- **User Journey Mapping** – Die Abläufe aus der Beobachtung werden in eine Journey-Struktur überführt.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
