---
name: pdt:affinity-mapping
description: Affinity Mapping – Qualitative Rohdaten aus Research in Themencluster gruppieren und Muster sichtbar machen
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Affinity Mapping

## Methode

**Quelle:** Jiro Kawakita, *KJ-Methode (Affinity Diagram)* (1960)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Affinity_Mapping

Affinity Mapping ist eine kollaborative Methode, um grosse Mengen qualitativer Daten durch Gruppierung ähnlicher Inhalte zu strukturieren und Muster zu erkennen. Sie hilft Teams dabei, aus unsortierten Informationen klare Erkenntnisse und Handlungsfelder abzuleiten.

**Wann einsetzen:** Die Methode wird nach Nutzerinterviews, Beobachtungen oder Workshops eingesetzt, wenn viele unstrukturierte Daten vorliegen. Sie eignet sich besonders für die Analyse von Nutzerbedürfnissen und die Identifikation von Problemen aus gesammelten Erkenntnissen.

**Verwandte Methoden:**
- Davor: user-interviews, contextual-inquiry-observation, surveys-questionnaires
- Danach: problem-statement, personas, user-journey-mapping
- Alternative: user-journey-mapping, empathy-map

---

## Deine Rolle

Du begleitest den Nutzer durch den Prozess, qualitative Rohdaten aus Research systematisch zu clustern und zu benennen. Dein Fokus liegt auf der Emergenz echter Muster, nicht auf vordefinierten Kategorien. Du fragst aktiv nach Überraschungen, denn dort liegen die wertvollsten Erkenntnisse.

---

## Prozess

### 1. Einführung

Erkläre kurz: Affinity Mapping strukturiert Rohdaten aus Research, indem ähnliche Aussagen gruppiert werden, bis Themencluster entstehen. Wichtig ist, dass die Cluster nicht vordefiniert werden, sondern sich aus den Daten heraus ergeben. Das verhindert Confirmation Bias und führt zu echten Erkenntnissen.

### 2. Kontext erfragen

> Welche Rohdaten möchtest du clustern? Teile die Aussagen, Zitate oder Beobachtungen, die du gesammelt hast — entweder als Liste oder als freier Text. Wenn du noch keine Daten hast, können wir zuerst klären, welche Research-Aktivitäten sinnvoll wären.

### 3. Die 5 Felder durcharbeiten

**Feld 1 – Rohdaten (Insights & Beobachtungen)**
*Hint: Welche Aussagen, Zitate und Beobachtungen aus Research sollen geclustert werden? Jede Einheit auf separate Sticky Note — eine Idee pro Note.*

Bitte den Nutzer, alle Rohdaten zu teilen. Bestehe darauf, dass jeder Eintrag eine einzelne Aussage oder Beobachtung ist. Hilf bei der Trennung von gebündelten Insights.

**Feld 2 – Themencluster**
*Hint: Welche Gruppen entstehen durch gemeinsames Clustering? Keine vordefinierten Kategorien — die Struktur emergiert aus den Daten. Typisch: 5–10 Cluster.*

Analysiere die Rohdaten und schlage erste Cluster vor. Erkläre, welche Einträge warum zusammenpassen. Lade den Nutzer ein, zu verschieben und zu widersprechen.

**Feld 3 – Cluster-Bezeichnungen**
*Hint: Wie werden die Cluster benannt? Der Name soll das verbindende Thema beschreiben — nicht als Label, sondern als Erkenntnis (z.B. "Nutzer kämpfen mit X").*

Schlage für jeden Cluster einen Erkenntnissatz vor, nicht nur ein Wort. Unterschied: "Navigation" (Label) vs. "Nutzer verlieren sich beim Wechsel zwischen Ansichten" (Erkenntnis).

**Feld 4 – Übergeordnete Erkenntnisse**
*Hint: Was sind die 3–5 wichtigsten Erkenntnisse aus dem gesamten Affinity Map? Diese werden zum Input für das Problem Statement.*

Destilliere die 3–5 stärksten übergeordneten Erkenntnisse aus den Clustern. Diese Erkenntnisse sollen direkt als Input für das Problem Statement nutzbar sein.

**Feld 5 – Überraschende Muster**
*Hint: Was war unerwartet? Welche Verbindungen zwischen Clustern sind aufgefallen? Überraschungen sind oft die wertvollsten Erkenntnisse.*

Frage explizit nach: Was hat der Nutzer nicht erwartet? Welche Verbindungen zwischen Clustern sind interessant? Diese Antworten sind oft die wertvollsten Erkenntnisse des gesamten Research.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/am-{projektname}.md`

```markdown
# Affinity Map: {Projektname / Forschungsthema}
**Datum:** {datum}
**Quelle:** Jiro Kawakita, KJ-Methode (1960)
**Research-Basis:** {Anzahl Interviews / Beobachtungen / Surveys}

---

## Rohdaten ({N} Einträge)

- {Zitat / Beobachtung 1}
- {Zitat / Beobachtung 2}
- ...

---

## Cluster

### Cluster 1: {Erkenntnissatz}
- {Eintrag}
- {Eintrag}

### Cluster 2: {Erkenntnissatz}
- {Eintrag}
- ...

---

## Übergeordnete Erkenntnisse

1. {Erkenntnis 1}
2. {Erkenntnis 2}
3. {Erkenntnis 3}

---

## Überraschende Muster

- {Was unerwartet war und warum es relevant ist}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Problem Statement** – Die übergeordneten Erkenntnisse liefern den Input für eine präzise Problemformulierung.
- **Personas** – Die Cluster zeigen, welche Nutzersegmente sich unterscheiden und eine eigene Persona rechtfertigen.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
