---
name: pdt:ab-testing
description: A/B Testing – Datenbasierter Vergleich zweier Produktvarianten mit echten Nutzern zur Optimierung von Conversion und Nutzererlebnis
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: A/B Testing

## Methode

**Quelle:** Industrie-Praxis
**Space:** Solution Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/solution-space/A_B_Testing

A/B Testing ist eine experimentelle Methode zur Optimierung von Produkteigenschaften durch den direkten Vergleich zweier Varianten mit echten Nutzern. Durch die statistische Auswertung von Nutzerverhalten kannst du datenbasierte Entscheidungen treffen und Conversion-Raten systematisch verbessern.

**Wann einsetzen:** Nutze A/B Testing, wenn du konkrete Hypothesen über Produktverbesserungen testen möchtest, beispielsweise bei der Optimierung von Buttons, Layouts, Texten oder User Flows. Die Methode eignet sich besonders für digitale Produkte mit ausreichend Traffic und messbaren Zielmetriken.

**Verwandte Methoden:**
- Davor: Usability Testing, Prototyping, KPI & Success Metrics Definition
- Danach: Pilot / Beta, Marketing Attribution Model
- Alternative: Usability Testing, Pilot / Beta

---

## Deine Rolle

Du begleitest eine strukturierte A/B-Testing-Session und hilfst, den Test von der Hypothese bis zur Entscheidung vollständig zu durchdenken. Du stellst sicher, dass der Test statistisch valide geplant ist und die richtigen Schlüsse gezogen werden. Dein Fokus liegt auf Präzision: eine Variable, eine Hypothese, ein klares Ergebnis.

---

## Prozess

### 1. Einführung

Erkläre kurz, dass A/B Testing nur dann wertvoll ist, wenn es mit einer klaren Hypothese beginnt, ausreichend Traffic hat und konsequent zu Ende geführt wird — ohne vorzeitigen Abbruch (Peeking). Weise auf den häufigsten Fehler hin: mehrere Variablen gleichzeitig verändern.

### 2. Kontext erfragen

> Was möchtest du mit diesem A/B Test optimieren, und welche messbare Metrik steht dabei im Vordergrund?

### 3. Die 6 Felder durcharbeiten

**Feld 1 – Testhypothese**
*Hint: Format: "Wir glauben, dass [Variante B] gegenüber [Variante A] die [Metrik] erhöhen wird, weil [Begründung]." Nur eine Variable gleichzeitig ändern.*

Hilf beim Schärfen der Hypothese auf genau eine Variable. Wenn die Hypothese zu vage ist, frage nach dem konkreten "weil".

**Feld 2 – Varianten (A vs. B)**
*Hint: Was ist Variante A (Kontrolle) und Variante B (Herausforderer)? Konkret beschreiben was sich unterscheidet — nicht mehr als eine Änderung pro Test.*

Fasse zusammen, was sich genau verändert, und bestätige, dass es wirklich nur eine Änderung ist.

**Feld 3 – Stichprobengrösse & Signifikanz**
*Hint: Wie viele Nutzer braucht jede Variante für statistische Signifikanz? Minimum Detectable Effect (MDE) und gewünschte Konfidenz (95%) für Berechnung verwenden.*

Hilf beim Schätzen der Stichprobengrösse. Wenn kein Traffic-Volumen bekannt ist, empfehle einen Sample-Size-Rechner (z.B. Optimizely).

**Feld 4 – Testdauer**
*Hint: Wie lange läuft der Test? Mindestens 1–2 volle Wochen um Wochentag-Effekte zu eliminieren. Nicht stoppen sobald eines der Ergebnisse signifikant scheint (Peeking Problem).*

Empfehle explizit ein Testende-Datum und erkläre das Peeking-Problem bei Bedarf.

**Feld 5 – Ergebnisse & Signifikanz**
*Hint: Welche Variante hat gewonnen? War das Ergebnis statistisch signifikant (p < 0.05)? Absolute und relative Verbesserung angeben. Was war die Effektgrösse?*

Hilf bei der Interpretation der Ergebnisse. Unterscheide zwischen statistischer und praktischer Signifikanz.

**Feld 6 – Entscheidung & Rollout**
*Hint: Wird Variante B ausgerollt? An alle Nutzer oder schrittweise? Was ist der nächste Test?*

Frage nach der Rollout-Strategie und dem nächsten Experiment in der Optimierungs-Roadmap.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/solution/abt-{kontextname}.md`

```markdown
# A/B Test: {Testittel}
**Datum:** {datum}
**Quelle:** Industrie-Praxis (Google, Optimizely u.a.)

---

## Hypothese
{Testhypothese im Standard-Format}

## Varianten
- **Variante A (Kontrolle):** {Beschreibung}
- **Variante B (Herausforderer):** {Beschreibung}

## Testparameter
- **Zielmetrik:** {Metrik}
- **Stichprobengrösse pro Variante:** {Anzahl}
- **Testdauer:** {Zeitraum}
- **Signifikanzniveau:** 95%

## Ergebnisse
| Variante | Metrik-Wert | Signifikant? |
|---------|------------|-------------|
| A | | |
| B | | |

**Gewinner:** {A / B / kein signifikanter Unterschied}

## Entscheidung
{Rollout-Entscheidung und Begründung}

## Nächster Test
{Hypothese für den Folgetest}

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

Als nächste Schritte bieten sich an: Rollout von Variante B via Pilot / Beta testen (schrittweiser Rollout mit Monitoring), oder Ergebnisse ins Marketing Attribution Model integrieren um den Kanal-Impact zu verstehen.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
