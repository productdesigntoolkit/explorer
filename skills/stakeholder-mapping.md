---
name: pdt:stakeholder-mapping
description: Stakeholder Mapping – Alle relevanten Akteure identifizieren, nach Macht und Interesse einordnen und strategisch managen
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Stakeholder Mapping

## Methode

**Quelle:** Aubrey L. Mendelow, *Environmental Scanning, The Impact of the Stakeholder Concept (Power/Interest Grid)* (1981)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Stakeholder_Mapping

Eine visuelle Methode zur Identifikation und Kategorisierung aller relevanten Personen, Gruppen und Organisationen, die von einem Projekt betroffen sind oder Einfluss darauf haben. Hilft dabei, Beziehungen zu verstehen und strategische Entscheidungen für das Stakeholder-Management zu treffen.

**Wann einsetzen:** Wird zu Projektbeginn eingesetzt, um alle relevanten Akteure zu erfassen und deren Einfluss sowie Interesse am Projekt zu bewerten. Besonders wertvoll bei komplexen Projekten mit vielen beteiligten Parteien oder bei internen Produkten mit organisatorischer Komplexität.

**Verwandte Methoden:**
- Davor: user-journey-mapping, problem-statement
- Danach: mvp-minimal-viable-product, product-vision-board, go-to-market-strategy
- Alternative: user-journey-mapping

---

## Deine Rolle

Du begleitest den Nutzer beim vollständigen Erfassen aller Stakeholder und ihrer Einordnung in das Power-Interest-Grid. Du erinnerst aktiv daran, dass nicht nur End-User Stakeholder sind: Entscheider, Beeinflusser und typische Skeptiker werden häufig vergessen. Bei B2B- und Enterprise-Produkten ist diese Vollständigkeit entscheidend für den Erfolg der Lösung.

---

## Prozess

### 1. Einführung

Erkläre kurz: Stakeholder Mapping stellt sicher, dass die Lösung nicht nur technisch und nutzerseitig funktioniert, sondern auch organisatorisch und politisch. Das Power-Interest-Grid (Mendelow 1981) teilt Stakeholder in vier Gruppen: hohe Macht + hohes Interesse (aktiv einbinden), hohe Macht + niedriges Interesse (zufriedenstellen), niedrige Macht + hohes Interesse (informieren), niedrige Macht + niedriges Interesse (beobachten). Jede Gruppe braucht eine andere Strategie.

### 2. Kontext erfragen

> Für welches Projekt oder welche Lösung erstellst du das Stakeholder Mapping? Und in welchem organisatorischen Kontext bewegen wir uns — internes Tool, B2B-Produkt oder etwas anderes?

### 3. Die 5 Felder durcharbeiten

**Feld 1 – Stakeholder-Identifikation**
*Hint: Wer ist von der Lösung betroffen oder hat Einfluss darauf? Intern und extern, nicht nur End-User.*

Brainstorme systematisch: Wer nutzt die Lösung direkt (End-User)? Wer zahlt dafür (Budget-Owner)? Wer muss es genehmigen (Management)? Wer ist indirekt betroffen (andere Abteilungen)? Wer könnte es blockieren (Skeptiker, Compliance)?

**Feld 2 – Power-Interest-Mapping**
*Hint: Hohe Macht + Hohes Interesse → Aktiv einbinden. Hohe Macht + Niedriges Interesse → Zufriedenstellen. Niedrige Macht + Hohes Interesse → Informieren. Niedrige Macht + Niedriges Interesse → Beobachten.*

Ordne jeden Stakeholder im Grid ein. Diskutiere strittige Fälle: Wer hat tatsächlich Entscheidungsgewalt? Wer hat informellen Einfluss, der nicht im Organigramm sichtbar ist?

**Feld 3 – Bedürfnisse & Erwartungen**
*Hint: Was erwartet jeder wichtige Stakeholder? Welche Kriterien muss die Lösung für ihn erfüllen? Was wäre ein Show-Stopper?*

Fokussiere auf Stakeholder mit hoher Macht oder hohem Interesse. Frage: Was sind ihre Erfolgskriterien? Was würde sie begeistern? Was wäre ein Deal-Breaker?

**Feld 4 – Kommunikationsplan**
*Hint: Wie und wie oft wird mit welchem Stakeholder kommuniziert? Format: Stakeholder → Kanal → Frequenz → Inhalt.*

Nicht alle Stakeholder brauchen dieselbe Kommunikation. Entwickle differenzierte Ansätze: Executive Summary für Management, detailliertes Update für Champions, Statusbericht für Informierte.

**Feld 5 – Stakeholder-Risiken**
*Hint: Welche Stakeholder könnten die Lösung blockieren? Warum? Wie werden ihre Bedenken proaktiv adressiert?*

Identifiziere potenzielle Blocker und ihre Motivationen. Frage: Was müsste passieren, damit sie die Lösung unterstützen? Welche Bedenken können proaktiv adressiert werden?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/sm-{projektname}.md`

```markdown
# Stakeholder Mapping: {Projektname}
**Datum:** {datum}
**Quelle:** Mendelow, Power/Interest Grid (1981)

---

## Stakeholder-Register

| Name / Gruppe | Intern/Extern | Rolle | Macht | Interesse | Grid-Position |
|---------------|---------------|-------|-------|-----------|--------------|
| {Name} | intern/extern | {Rolle} | hoch/niedrig | hoch/niedrig | {Quadrant} |

---

## Power-Interest-Grid

**Aktiv einbinden (Hohe Macht + Hohes Interesse):**
- {Stakeholder}: {Warum + Strategie}

**Zufriedenstellen (Hohe Macht + Niedriges Interesse):**
- {Stakeholder}: {Warum + Strategie}

**Informieren (Niedrige Macht + Hohes Interesse):**
- {Stakeholder}: {Warum + Strategie}

**Beobachten (Niedrige Macht + Niedriges Interesse):**
- {Stakeholder}: {Warum}

---

## Bedürfnisse & Erwartungen (Prioritäre Stakeholder)

| Stakeholder | Erwartungen | Erfolgskriterien | Show-Stopper |
|-------------|-------------|-----------------|--------------|
| {Name} | {Was sie erwarten} | {Was sie zufriedenstellt} | {Was sie blockiert} |

---

## Kommunikationsplan

| Stakeholder | Kanal | Frequenz | Inhalt |
|-------------|-------|----------|--------|
| {Name} | {Email / Meeting / Report} | {wöchentlich / monatlich} | {Was kommuniziert wird} |

---

## Stakeholder-Risiken

| Stakeholder | Risiko | Massnahme |
|-------------|--------|-----------|
| {Name} | {Warum er/sie blockieren könnte} | {Wie Bedenken adressiert werden} |

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **MVP (Minimal Viable Product)** – Die Bedürfnisse und Erwartungen der wichtigsten Stakeholder beeinflussen den Scope des ersten Releases.
- **Go-to-Market Strategy** – Die Stakeholder im Buying Center werden Teil der GTM-Strategie.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
