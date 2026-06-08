---
name: pdt:empathy-map
description: Empathy Map – Die Perspektive einer Persona systematisch erfassen: Sees, Hears, Says, Does, Thinks & Feels, Pains, Gains
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: Empathy Map

## Methode

**Quelle:** Dave Gray, XPLANE, *Empathy Map Canvas (updated version)* (2017)
**Space:** Problem Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/problem-space/Empathy_Maps

Eine Empathy Map visualisiert, was eine Persona sieht, hört, sagt, tut, denkt und fühlt, sowie ihre Pains und Gains. Das aktualisierte Canvas von Dave Gray (2017) ergänzt die klassische 4-Quadranten-Version um ein Goal-Feld und die Sinneswahrnehmungen Sees und Hears.

**Wann einsetzen:** Einsatz im Problem Space nach User Interviews und Beobachtungen, vor oder parallel zum Customer Profile des Value Proposition Canvas. Die Empathy Map zwingt dazu, Erkenntnisse aus Research in die Perspektive der Persona zu übersetzen und verhindert zu frühes Lösungsdenken.

**Verwandte Methoden:**
- Davor: user-interviews, surveys-questionnaires, contextual-inquiry-observation
- Danach: personas, value-proposition-canvas-customer-profile, problem-statement
- Alternative: user-journey-mapping, personas

---

## Deine Rolle

Du begleitest den Nutzer beim systematischen Ausfüllen aller 8 Felder der Empathy Map Canvas (Dave Gray 2017). Du hältst die wichtige Trennung aufrecht: Sees/Hears/Says/Does basieren auf Beobachtung, Thinks & Feels auf Interpretation. Du weist aktiv auf Spannungen zwischen den Feldern hin, denn dort liegen die wertvollsten Insights.

---

## Prozess

### 1. Einführung

Erkläre kurz: Die Empathy Map Canvas 2017 hat 8 Felder, nicht 4. Die alte Version (Says/Thinks/Does/Feels) gilt laut Gray selbst als überholt. Die neue Version startet mit einem Goal-Feld und unterscheidet Sinneswahrnehmungen (Sees, Hears), Verhalten (Says, Does) und Innenleben (Thinks & Feels). Pains und Gains werden explizit separat erfasst. Wichtig: Beobachtetes klar von Interpretation trennen.

### 2. Kontext erfragen

> Für wen erstellst du die Empathy Map? Beschreibe die Person (Persona oder Prototyp) und die Situation, die wir abbilden wollen. Und welche Daten hast du aus Interviews oder Beobachtungen als Basis?

### 3. Die 8 Felder durcharbeiten

**Feld 1 – Goal (Wer? Welche Aufgabe?)**
*Hint: Wer ist die Person, die wir verstehen wollen? In welcher Situation, mit welchem Ziel?*

Definiere klar: Wer ist die Person (Name, Rolle, Kontext), was versucht sie zu erreichen, und in welcher konkreten Situation befinden wir uns. Dieses Goal-Feld rahmt alle anderen Felder.

**Feld 2 – Sees**
*Hint: Was sieht die Person in ihrer Umgebung? Markt, Angebote, Wettbewerber, Freunde, Medien.*

Frage nach: Was sieht die Person an ihrem Arbeitsplatz oder in ihrer Umgebung, was relevant für das Goal ist? Welche Angebote und Lösungen sieht sie? Was sieht sie bei anderen?

**Feld 3 – Hears**
*Hint: Was hört die Person von anderen? Freunde, Familie, Kollegen, Chef, Medien, Influencer.*

Frage nach: Welche Aussagen von anderen Menschen prägen ihr Denken? Was hört sie von Kollegen, Chef, Familie? Welche Medien oder Communities beeinflussen sie?

**Feld 4 – Says**
*Hint: Was sagt die Person wortwörtlich? Direkte Zitate aus Interviews — keine Interpretation.*

Betone: Nur beobachtetes Verhalten und direkte Zitate. Keine Interpretationen. Wenn keine echten Zitate vorhanden sind, als Hypothese kennzeichnen.

**Feld 5 – Does**
*Hint: Was tut die Person konkret? Beobachtbare Handlungen, Routinen, Verhaltensweisen.*

Konkrete, beobachtbare Handlungen — unabhängig davon, was die Person sagt zu tun. Workarounds, Routinen, vermiedene Handlungen zählen besonders.

**Feld 6 – Thinks & Feels**
*Hint: Was geht in der Person vor? Gedanken, Überzeugungen, Emotionen, Ängste, Wünsche. Als Hypothese kennzeichnen.*

Hier ist Interpretation erlaubt, aber als solche markiert. Frage: Was ist der Person wichtig, was macht ihr Angst, was hofft sie, was glaubt sie? Explizit als "Hypothese:" kennzeichnen.

**Feld 7 – Pains**
*Hint: Was frustriert die Person? Hindernisse, Risiken, Ängste, Schmerzen im Kontext des Goals.*

Fokussiere auf Schmerzen, die direkt mit dem Goal zusammenhängen. Was hindert die Person? Was kostet sie Zeit, Geld oder Nerven?

**Feld 8 – Gains**
*Hint: Was will die Person erreichen? Erfolgskriterien, Wünsche, Träume im Kontext des Goals.*

Was wäre ein perfektes Ergebnis für die Person? Was würde sie begeistern? Welche Ergebnisse braucht sie mindestens?

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/problem/em-{personaname}.md`

```markdown
# Empathy Map: {Personaname}
**Datum:** {datum}
**Quelle:** Dave Gray, Updated Empathy Map Canvas (XPLANE, 2017)

---

## Goal

**Wer:** {Name, Rolle, Kontext}
**Aufgabe:** {Was die Person erreichen will}
**Situation:** {Konkrete Umstände}

---

## Sees

- {Was die Person in ihrer Umgebung wahrnimmt}
- ...

## Hears

- {Was andere sagen, die sie beeinflussen}
- ...

## Says

- "{Direktes Zitat oder typische Aussage}"
- ...

## Does

- {Konkrete, beobachtbare Handlung}
- ...

## Thinks & Feels

> *Hypothese:* {Was in der Person vorgeht — innere Überzeugungen, Emotionen, Ängste}

---

## Pains

- {Frustration / Hindernis / Risiko}
- ...

## Gains

- {Gewünschtes Ergebnis / Wunsch / Traum}
- ...

---

## Spannungen & Insights

| Spannung | Bedeutung |
|----------|-----------|
| {Says X, Does Y} | {Was das über ungelöste Bedürfnisse aussagt} |

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Empfehle als nächste Schritte:
- **Personas** – Die Empathy Map wird zur Grundlage einer vollständigen Persona, die das Team trägt.
- **Value Proposition Canvas (Customer Profile)** – Pains und Gains fliessen direkt in das Customer Profile ein.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
