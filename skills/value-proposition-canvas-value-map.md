---
name: pdt:value-proposition-canvas-value-map
description: Value Proposition Canvas — Value Map – Die Lösungsseite des VPC: wie Products & Services, Pain Relievers und Gain Creators explizit auf das Customer Profile antworten
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Value Proposition Canvas — Value Map

## Methode

**Quelle:** Alexander Osterwalder, Yves Pigneur, Greg Bernarda, Alan Smith, *Value Proposition Design* (2014)
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/Value_Proposition_Canvas_Value_Map

Die Value Map ist die rechte Hälfte des Value Proposition Canvas und beschreibt, wie das Angebot auf die Kundenbedürfnisse antwortet. Sie umfasst Products & Services, Pain Relievers und Gain Creators. Zusammen mit dem Customer Profile ergibt sich der Problem-Solution-Fit.

**Wann einsetzen:** Einsatz im Solution Space, nachdem das Customer Profile vollständig ausgefüllt wurde. Die Value Map zwingt zur expliziten Verbindung zwischen Kundenbedürfnissen und Angebotselementen: jeder Pain Reliever adressiert einen konkreten Pain, jeder Gain Creator erzeugt einen konkreten Gain.

**Verwandte Methoden:**
- Davor: Value Proposition Canvas Customer Profile, Problem Statement, How Might We Questions
- Danach: Positioning Template, MVP — Minimal Viable Product, Product Vision Board, Prototyping
- Alternative: Product Vision Statement

---

## Deine Rolle

Du begleitest das Ausfüllen der Value Map mit expliziten 1-zu-1-Verbindungen zum Customer Profile. Du verhindere generische Antworten und bestehst auf konkreten Zuordnungen: Pain Reliever X adressiert Pain Y aus dem Customer Profile. Du hilfst, den Fit-Check ehrlich durchzuführen: was ist validiert, was ist Hypothese?

---

## Prozess

### 1. Einführung

Erkläre Osterwalders Grundprinzip: "Fit is when customers get excited about your value proposition." Das passiert nur durch explizite Verbindungen — nicht durch generische Versprechen. Die Value Map antwortet direkt auf das Customer Profile: kein Element der Value Map existiert im Vakuum.

### 2. Kontext erfragen

> Liegt ein Customer Profile (Jobs, Pains, Gains) vor, das als Basis für die Value Map dienen kann — und was ist das Produkt oder der Service, den du beschreiben möchtest?

### 3. Die 4 Felder durcharbeiten

**Feld 1 – Products & Services**
*Hint: Welche konkreten Produkte und Services bietest du dem Kunden an? Liste alle Angebotskomponenten auf: physisch, digital, Services, finanziell, immateriell. Dies ist das Angebot, noch nicht der Nutzen.*

Liste alle Angebotskomponenten. Für jede: physisch, digital, Service, immateriell? Das ist das "Was" — nicht das "Warum".

**Feld 2 – Pain Relievers**
*Hint: Wie lindern deine Produkte und Services die konkreten Pains aus dem Customer Profile? Explizite 1-zu-1-Zuordnung: Pain X wird durch Pain Reliever Y adressiert. Fokussiere auf die extremen Pains.*

Für jeden Pain Reliever: welcher konkrete Pain aus dem Customer Profile wird adressiert? Formuliere die Verbindung explizit. Nicht alle Pains müssen gelöst werden — fokussiere auf die extremen.

**Feld 3 – Gain Creators**
*Hint: Wie erzeugen deine Produkte und Services die konkreten Gains? Zuordnung zu required, expected, desired und unexpected Gains. Differenzierung entsteht oft über unexpected Gains.*

Für jeden Gain Creator: welchen Gain aus dem Customer Profile erzeugt er? Klassifiziere: required, expected, desired oder unexpected? Unexpected Gains schaffen oft den entscheidenden Unterschied.

**Feld 4 – Fit-Check (Problem-Solution Fit)**
*Hint: Welche Pains und Gains werden bewusst NICHT adressiert? Wo ist der Fit stark, wo schwach? Ist der Fit Hypothese oder bereits validiert?*

Bewerte jeden Fit: stark / mittel / schwach. Markiere: validiert durch Nutzer-Feedback, oder Hypothese? Out-of-Scope-Liste erstellen: was wird bewusst nicht adressiert?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/vpc-valuemap-{kontextname}.md`

```markdown
# Value Map: {Produktname}
**Datum:** {datum}
**Quelle:** Osterwalder et al. — Value Proposition Design (2014)

---

## Products & Services
| Komponente | Typ | Beschreibung |
|-----------|-----|-------------|
| {name} | {physisch/digital/service/immateriell} | {was es ist} |

---

## Pain Relievers

| Pain Reliever | Adressiert Pain (aus Customer Profile) | Stärke des Fits |
|--------------|--------------------------------------|----------------|
| {name} | {konkreter Pain} | Stark / Mittel / Schwach |

---

## Gain Creators

| Gain Creator | Erzeugt Gain (aus Customer Profile) | Typ | Stärke des Fits |
|-------------|-------------------------------------|-----|----------------|
| {name} | {konkreter Gain} | required / expected / desired / unexpected | Stark / Mittel / Schwach |

---

## Fit-Check

**Starker Fit:**
- {Verbindung die bereits validiert ist}

**Schwacher Fit / Hypothesen:**
- {Verbindung die noch validiert werden muss}

**Bewusst nicht adressiert (Out of Scope):**
- {Pains / Gains die ausgeschlossen wurden, mit Begründung}

**Gesamtbewertung:** {Fit stark / teilweise / schwach — Grundlage für Entscheidung}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: Hypothesen im Fit-Check durch Nutzerfeedback validieren (z.B. durch Interviews oder Usability Tests), oder den validierten Fit als Basis für das Positioning Template und das MVP nutzen.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
