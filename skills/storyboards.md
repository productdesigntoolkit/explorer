---
name: pdt:storyboards
description: Storyboards – Die Lösung als Nutzergeschichte durcherzählen, bevor ein Prototyp gebaut wird, um Lücken in der UX-Logik früh zu entdecken
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Storyboards

## Methode

**Quelle:** Webb Smith, Walt Disney Studios; adaptiert für UX durch IDEO, *Storyboarding in Animation; Design Thinking Bootleg* (1933 / 2005)
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/Storyboards

Storyboards sind sequenzielle visuelle Darstellungen, die den Ablauf einer User Journey oder eines Nutzungsszenarios in Form von Bildsequenzen erzählen. Sie helfen dabei, komplexe Interaktionen und Erlebnisse zu visualisieren und emotionale Aspekte der Nutzererfahrung zu veranschaulichen.

**Wann einsetzen:** Storyboards werden eingesetzt, um User Journeys zu visualisieren, Designkonzepte zu kommunizieren und emotionale Reaktionen von Nutzern darzustellen. Sie eignen sich besonders gut zur Präsentation von Ideen vor Stakeholdern und zur Identifikation von Schwachstellen in der Nutzererfahrung.

**Verwandte Methoden:**
- Davor: Crazy 8s, How Might We Questions
- Danach: Wireframes / Mockups, Prototyping, Usability Testing
- Alternative: Crazy 8s, Wireframes / Mockups

---

## Deine Rolle

Du hilfst beim Durchdenken und Strukturieren des Storyboards als Textnarrative — da visuelle Skizzen hier nicht möglich sind, beschreibst du jeden Frame präzise mit Situation, Aktion und Emotion. Du prüfst ob die Geschichte eine kohärente User Journey ergibt: wenn das Storyboard keine klare Geschichte erzählt, ist die Lösung noch nicht bereit für einen Prototypen.

---

## Prozess

### 1. Einführung

Erkläre die PDT-Regel: wenn das Storyboard keine kohärente Geschichte ergibt, ist die Lösung noch nicht klar genug für einen Prototyp. Storyboards zwingen dazu, die Lösung als Nutzergeschichte zu durchdenken — nicht als Feature-Liste. Jeder Frame zeigt: was tut die Person, was fühlt sie, was passiert.

### 2. Kontext erfragen

> Welche Persona und welches Szenario soll das Storyboard zeigen — und welche Lösung oder welcher Lösungsansatz wird dabei durchgespielt?

### 3. Die 5 Felder durcharbeiten

**Feld 1 – Szenario & Hauptfigur**
*Hint: Welche Persona in welcher konkreten Situation? Hauptfigur, Kontext und Ausgangssituation klar definieren.*

Definiere Persona, konkreten Kontext (wann, wo, in welcher Situation) und das Ausgangsproblem das die Geschichte auslöst.

**Feld 2 – Frames (6–8 Panels)**
*Hint: Was passiert in jedem Panel? Zeige: Ausgangsproblem → Trigger → Lösung einsetzen → Ergebnis.*

Erarbeite gemeinsam 6–8 Frames. Für jeden Frame: Situation beschreiben, Aktion der Person, Emotion/Reaktion. Kein Text-Dump — ein Frame = ein Moment.

Typische Struktur:
- Frame 1–2: Ausgangssituation und Problem
- Frame 3: Trigger (Moment der Lösung)
- Frame 4–6: Lösung in Aktion (Kerninteraktionen)
- Frame 7–8: Ergebnis und emotionale Auflösung

**Feld 3 – Kerninteraktionen**
*Hint: Welche Interaktionen mit dem Produkt werden gezeigt? Was muss der Nutzer tun? Was bekommt er zurück?*

Extrahiere die 2–3 wichtigsten Produktinteraktionen aus dem Storyboard. Das sind die Prioritäten für den Prototypen.

**Feld 4 – Gezeigte Annahmen**
*Hint: Welche Annahmen über Nutzerverhalten werden im Storyboard gemacht? Diese müssen validiert werden.*

Liste alle Verhaltensannahmen die im Storyboard impliziert werden. Diese sind Input für das Testprotokoll.

**Feld 5 – Team-Feedback**
*Hint: Was hat das Team beim Review des Storyboards angemerkt? Welche Lücken oder Widersprüche wurden gefunden?*

Welche Momente in der Geschichte fühlen sich unlogisch an? Wo fehlen Frames? Was müsste anders verlaufen?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/sb-{kontextname}.md`

```markdown
# Storyboard: {Titel / Szenario}
**Datum:** {datum}
**Persona:** {Name}
**Quelle:** Disney / IDEO Design Thinking (1933/2005)

---

## Szenario
**Persona:** {Kurzprofil}
**Kontext:** {Wann, wo, in welcher Situation}
**Ausgangsproblem:** {Was löst die Geschichte aus}

---

## Frames

**Frame 1 — {Titel}**
{Situation / Bild-Beschreibung}
*Emotion: {Gefühlslage der Persona}*

**Frame 2 — {Titel}**
{Situation / Bild-Beschreibung}
*Emotion: {Gefühlslage}*

**Frame 3 — {Titel (Trigger)}**
{Moment der Lösung}
*Emotion: {Neugier / Erleichterung / ...}*

**Frame 4 — {Titel}**
{Kerninteraktion mit dem Produkt}
*Emotion: {Gefühlslage}*

**Frame 5 — {Titel}**
{Weiterer Schritt}
*Emotion: {Gefühlslage}*

**Frame 6 — {Titel}**
{Ergebnis / Auflösung}
*Emotion: {Zufriedenheit / Überraschung / ...}*

---

## Kerninteraktionen (Prioritäten für Prototyp)
1. {Interaktion}
2. {Interaktion}
3. {Interaktion}

## Annahmen (zu validieren)
- {Verhaltensannahme}
- {Verhaltensannahme}

## Team-Feedback
- {Lücken, Widersprüche, Anpassungen}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: die Kerninteraktionen aus dem Storyboard als Grundlage für Wireframes oder Mockups nutzen, oder direkt einen ersten Lo-Fi-Prototypen bauen und mit 5 Nutzern testen.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
