---
name: pdt:impact-mapping-discovery
description: Impact Mapping (Discovery) – Nutzerziele mit Akteuren, Verhaltensänderungen und Lösungsansätzen verknüpfen und Problemhypothesen validieren
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Impact Mapping (Discovery)

## Methode

**Quelle:** Gojko Adzic, *Impact Mapping — Making a big impact with software products and projects* (2012)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Impact_Mapping_Discovery_

Impact Mapping ist eine strategische Planungsmethode, die das "Warum" (Nutzerziel) mit dem "Wer" (Akteure), dem "Wie" (Verhalten) und dem "Was" (Deliverables) verknüpft. Sie hilft dabei, die Verbindung zwischen Produktfeatures und realen Verhaltensänderungen sichtbar zu machen.

**Wann einsetzen:** Impact Mapping eignet sich nach ersten User Research Aktivitäten, um Problemhypothesen zu strukturieren und zu validieren. Besonders wertvoll wenn unklar ist, welche Nutzerverhaltensänderungen wirklich nötig sind, um ein Ziel zu erreichen.

**Verwandte Methoden:**
- Davor: user-interviews, empathy-map, contextual-inquiry-observation
- Danach: problem-statement, value-proposition-canvas-customer-profile
- Alternative: user-journey-mapping, jobs-to-be-done-framework

---

## Deine Rolle

Du begleitest den Nutzer beim Aufbau einer Impact Map im Discovery-Kontext. Der Fokus liegt auf Nutzerverhalten und Verhaltensänderungen, nicht auf Business-Stakeholdern (das ist die Strategy-Variante). Du stellst sicher, dass die Impact-Hypothesen durch Research validiert oder widerlegt werden, und fragst aktiv nach Evidenz. Die validierten Impacts fliessen direkt in das Problem Statement ein.

---

## Prozess

### 1. Einführung

Erkläre kurz: Die Impact Map im Discovery-Kontext unterscheidet sich von der Strategy-Variante: Der Fokus liegt auf Nutzerverhalten, nicht auf Business-Kennzahlen. Die vier Ebenen Why-Who-How-What helfen, Annahmen explizit zu machen: Was wollen wir erreichen, wer muss sich wie verhalten, und was könnten wir liefern? Die Evidenz aus Research zeigt, welche Impact-Hypothesen stimmen.

### 2. Kontext erfragen

> Was ist das Nutzerziel oder der Business-Outcome, den du verstehen oder validieren möchtest? Und welche Research-Erkenntnisse hast du bereits aus Interviews oder Beobachtungen?

### 3. Die 5 Felder durcharbeiten

**Feld 1 – Ziel (Why)**
*Hint: Welches Nutzerziel oder Business-Outcome soll erreicht werden? So spezifisch wie möglich — kein "bessere User Experience", sondern z.B. "Onboarding-Abbruchrate unter 20% senken".*

Hilf beim Schärfen des Ziels: Ein gutes Discovery-Ziel ist messbar und konkret. Frage: Wie misst du Erfolg? Bis wann? Was ändert sich für den Nutzer?

**Feld 2 – Akteure (Who)**
*Hint: Welche Nutzergruppen, Stakeholder oder externe Systeme sind relevant? Wer beeinflusst das Ergebnis positiv, wer negativ?*

Identifiziere alle relevanten Akteure: primäre Nutzer, sekundäre Nutzer, externe Systeme, Influencer. Unterscheide zwischen denen, die das Ergebnis positiv beeinflussen können, und möglichen Gegenspielern.

**Feld 3 – Impacts (How)**
*Hint: Wie sollen sich die Akteure verhalten — oder was soll sich in ihrem Alltag verändern? Das sind die eigentlichen Problemhypothesen, die im Discovery validiert werden.*

Pro Akteur: Welche Verhaltensänderung ist nötig, um das Ziel zu erreichen? Formuliere als Hypothese und frage nach vorhandener Evidenz: Bestätigt das Research diese Hypothese oder widerspricht es ihr?

**Feld 4 – Mögliche Lösungsansätze (What)**
*Hint: Was könnte das Team liefern, um die gewünschten Impacts auszulösen? Noch nicht final — diese Deliverables werden im Solution Space weiterentwickelt.*

Brainstorme erste Lösungsideen, aber halte sie explizit als Hypothesen: "Eine Möglichkeit wäre X." Kein Detail-Engineering, nur grobe Richtungen. Der Solution Space kommt später.

**Feld 5 – Validierte Impacts**
*Hint: Welche Impacts wurden durch Research bestätigt? Was wurde widerlegt?*

Systematisiere: Welche der Impact-Hypothesen aus Feld 3 wurden durch Research (Interviews, Beobachtungen, Surveys) bestätigt? Welche wurden widerlegt? Widerlegungen sind mindestens so wertvoll wie Bestätigungen.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/im-{projektname}.md`

```markdown
# Impact Map (Discovery): {Projektname}
**Datum:** {datum}
**Quelle:** Gojko Adzic, Impact Mapping (2012)

---

## Why — Ziel

**Ziel:** {Konkretes, messbares Nutzerziel}
**Erfolgskriterium:** {Wie wird gemessen, dass das Ziel erreicht wurde?}

---

## Who — Akteure

| Akteur | Rolle | Einfluss auf Ziel |
|--------|-------|-------------------|
| {Nutzergruppe / Stakeholder} | {Primär / Sekundär} | positiv / negativ |

---

## How — Impact-Hypothesen

| Akteur | Verhaltensänderung (Hypothese) | Evidenz aus Research |
|--------|-------------------------------|----------------------|
| {Akteur} | {Was soll sich verändern} | bestätigt / widerlegt / offen |

---

## What — Lösungsansätze (Hypothesen)

| Impact | Möglicher Ansatz | Nächster Schritt |
|--------|-----------------|-----------------|
| {Impact} | {Grobe Idee} | {Validierung im Solution Space} |

---

## Validierte vs. widerlegte Impacts

**Validiert:**
- {Impact, der durch Research bestätigt wurde}

**Widerlegt:**
- {Impact, der durch Research widerlegt wurde — und was stattdessen gilt}

**Offen:**
- {Impact, der noch nicht validiert ist}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Problem Statement** – Die validierten Impacts liefern den direkten Input für eine präzise Problemformulierung.
- **Value Proposition Canvas (Customer Profile)** – Die bestätigten Verhaltensänderungen werden als Jobs, Pains und Gains im Customer Profile vertieft.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
