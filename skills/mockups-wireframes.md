---
name: pdt:mockups-wireframes
description: Wireframes / Mockups – Strukturierte UI-Darstellungen in der richtigen Fidelität planen, dokumentieren und für Usability Tests vorbereiten
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Wireframes / Mockups

## Methode

**Quelle:** Industrie-Praxis
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/Mockups

Mockups sind statische, visuelle Darstellungen eines Produkts oder einer Benutzeroberfläche, die das Design und Layout zeigen. Sie helfen dabei, Designentscheidungen zu validieren und Stakeholdern eine konkrete Vorstellung des Produkts zu vermitteln.

**Wann einsetzen:** Mockups werden eingesetzt, wenn das grundlegende Konzept und die Informationsarchitektur definiert sind und nun das visuelle Design entwickelt werden soll. Sie eignen sich besonders für die Kommunikation mit Stakeholdern, Entwicklern und zur Vorbereitung von Usability-Tests.

**Verwandte Methoden:**
- Davor: Storyboards, Crazy 8s
- Danach: Prototyping, Usability Testing
- Alternative: Storyboards, Prototyping

---

## Deine Rolle

Du begleitest die Planung und Dokumentation von Wireframes und Mockups. Da du keine visuellen Designs erstellen kannst, fokussierst du dich auf: Fidelitätsstrategie, Screen-Inventar, Navigationsflows, Designentscheide und deren Begründung. Du hilfst, das Mockup konzeptionell durchzudenken, bevor es im Tool (Figma, Balsamiq etc.) erstellt wird.

---

## Prozess

### 1. Einführung

Erkläre die PDT-Faustregel: so wenig Fidelität wie nötig um das zu testen was getestet werden soll. Zu hohe Fidelität zu früh lenkt ab — Tester sprechen dann über Farben statt über Funktionalität. Fidelität ist eine Entscheidung, keine Selbstverständlichkeit.

### 2. Kontext erfragen

> Was soll mit diesem Mockup getestet oder kommuniziert werden, und für welches Produkt oder Feature wird es erstellt?

### 3. Die 5 Felder durcharbeiten

**Feld 1 – Fidelitätsstufe**
*Hint: Lo-Fi (grobe Struktur, kein Styling) für frühe Ideation; Mid-Fi (klare Struktur, Platzhalter) für Nutzertests; Hi-Fi (visuell fertig) für finale Validierung.*

Hilf beim Entscheid der richtigen Fidelitätsstufe basierend auf dem Ziel. Empfehle explizit eine Stufe und begründe sie.

**Feld 2 – Screens & Flows**
*Hint: Welche Screens werden erstellt? Welche Navigation zwischen Screens? Der Flow muss die Kern-User-Story abdecken — nicht alle Features.*

Erstelle ein Screen-Inventar und einen Navigation-Flow als Textdiagramm. Fokus auf Happy Path.

**Feld 3 – Wichtige Designentscheide**
*Hint: Welche Layouts, Informationshierarchien oder Interaktionsmuster wurden gewählt? Warum? Explizit machen was Annahme ist und was validiert wurde.*

Dokumentiere 3–5 bewusste Designentscheide mit Begründung. Markiere, was Annahme ist.

**Feld 4 – Content & Daten (Platzhalter)**
*Hint: Welche echten Inhalte oder Daten würden hier erscheinen? Realistische Platzhalter statt "Lorem ipsum".*

Definiere für jeden Screen: was sind realistische Beispiel-Inhalte? Das hilft Layoutprobleme früh zu erkennen.

**Feld 5 – Feedback aus Review**
*Hint: Welches Feedback haben Stakeholder oder Nutzer zum Mockup gegeben? Was wird angepasst, was bleibt?*

Dokumentiere Review-Feedback und Entscheidungen: was wird geändert (mit Begründung), was bleibt bewusst so.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/ux-{kontextname}.md`

```markdown
# Wireframes / Mockups: {Produkt / Feature}
**Datum:** {datum}
**Fidelität:** {Lo-Fi / Mid-Fi / Hi-Fi}
**Quelle:** Industrie-Praxis (UI/UX-Community)

---

## Ziel des Mockups
{Was wird getestet oder kommuniziert?}

## Screen-Inventar

| Screen | Beschreibung | Kerninteraktion |
|--------|-------------|----------------|
| {name} | {inhalt} | {aktion} |

## Navigation Flow
{Textdiagramm: Screen A → [Aktion] → Screen B}

## Designentscheide
1. **{Entscheid}:** {Begründung} — *Validiert / Hypothese*
2. **{Entscheid}:** {Begründung} — *Validiert / Hypothese*

## Content-Platzhalter
{Screen X: Beispiel-Inhalte}

## Review-Feedback
- **Behalten:** {Begründung}
- **Anpassen:** {Was und warum}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: das Mockup in einen interaktiven Prototyp überführen (z.B. in Figma verlinkte Screens), oder direkt einen Usability Test planen um die dokumentierten Designentscheide zu validieren.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
