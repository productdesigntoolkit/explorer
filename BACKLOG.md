# Backlog

Vorhaben rund um den Explorer und die Methodenkette. Stand 2026-08-27.

Kontext: Eine Methode lebt in fünf Repos, die Checkliste dazu steht in `gitbook-methods/ADDING-A-METHOD.md`, die Prüfung in `check-methods.py`. Ziel der Arbeitspakete unten ist, die Zahl der Handgriffe pro Methode von zehn auf fünf zu senken.

## AP 1 · Product_Lifecycle reparieren

Priorität 1 · etwa 5 Minuten · kein Risiko

`gitbook-methods/strategy-space/Product_Lifecycle.md` ist die einzige der 84 Methoden, die ihre Überschriften mit HTML-Ankern aus einem alten GitBook-Export schreibt, und sie hat keine `description` im Frontmatter. Deshalb greift weder das Frontmatter noch der Fallback in `build.py`, und die Karte im Explorer bleibt ohne Beschreibungstext.

- [ ] `description` ins Frontmatter
- [ ] Überschriften auf das Format der übrigen Dateien bringen
- [ ] `build.py`, danach `check-methods.py`

## AP 2 · skill-Feld in die Quelle holen

Priorität 1 · etwa eine Stunde · geringes Risiko · Voraussetzung für AP 3

Heute steht `skill:` nur in der Explorer-Kopie und wird von `add-skill-mapping.py` aus einer Tabelle mit 80 Einträgen nachgetragen. Eine reine Namensregel ersetzt die Tabelle nicht: Sie trifft 68 von 80 Fällen, 12 Ausnahmen bleiben, darunter `Marktstrategie` zu `market-strategy` und `Mockups` zu `mockups-wireframes`.

Besserer Weg: das Feld direkt in `gitbook-methods` ins Frontmatter schreiben, einmalig für alle Methoden aus der bestehenden Tabelle generiert. GitBook rendert Frontmatter nicht, die Bücher ändern sich also nicht.

- [ ] Feld in allen Methodendateien in `gitbook-methods` setzen
- [ ] `SKILL_MAP` und `add-skill-mapping.py` entfernen
- [ ] `check-methods.py`: Vergleich Quelle gegen Kopie auf exakte Gleichheit umstellen, die Ausnahme für die skill-Zeile entfällt

Der eigentliche Gewinn ist nicht die gesparte Tabelle, sondern dass Quelle und Kopie danach byteweise identisch sind.

## AP 3 · sync-methods.sh statt Handkopie

Priorität 2 · etwa eine Stunde · geringes Risiko · nach AP 2

Ein Skript im Explorer, das Methodendateien aus `gitbook-methods` und Skills aus `pdt-skills` spiegelt, `build.py` aufruft und `check-methods.py` anhängt.

Bewusst lokal und nicht als GitHub Action: `gitbook-methods` ist privat, `explorer` ist öffentlich. Eine Action, die aus dem privaten ins öffentliche Repo zieht, bräuchte ein Token im öffentlichen Repo. Das Risiko steht in keinem Verhältnis zum gesparten Handgriff.

- [ ] `sync-methods.sh` schreiben
- [ ] Schritt 5 in `ADDING-A-METHOD.md` auf den einen Befehl kürzen

## AP 4 · Zähler generieren

Priorität 2 · etwa eine Stunde · geringes Risiko · unabhängig

`sync-counts.py` schreibt die Zahlen in den fünf Space-Commands von `pdt-claude_plugin` und im Explorer-README aus `data.js`. Die inhaltlichen Listen bleiben Handarbeit, nur die Zähler werden abgeleitet. Am 2026-08-26 standen vier von fünf Zählern falsch, das ist die Fehlerquelle, die damit wegfällt.

- [ ] `sync-counts.py` schreiben
- [ ] Schritte 6 und 7 in `ADDING-A-METHOD.md` anpassen

## AP 5 · Release-Aufgaben des Plugins

Priorität 3 · abhängig vom Releasetermin

Steht im BACKLOG des Plugin-Projekts unter `brain/LABS/030-IN_PROGRESS/pdt-claude_plugin/`: Methoden-Skills aus `pdt-skills` nachfüllen und die Suggested Paths der fünf Space-Commands kuratieren. Beides gehört an den Punkt, an dem das Plugin gepackt wird.

## Kleinere offene Punkte

- Vier Methoden haben bewusst keinen Skill (`Value_Proposition_Jobs_to_be_done`, `Value_Proposition_Pains_and_Gains`, `Hooked_Model`, `UAC_Tracker`). `check-methods.py` meldet sie als Hinweis. Entweder Skills nachziehen oder die Ausnahme im Skript hinterlegen.
- `uac-tracker.yaml` in `pdt-templates` gehört zu keiner Methode mit Skill, Kehrseite des Punkts oben.
- `mockup-method` und `mockups-wireframes` überschneiden sich funktional, steht schon im Plugin-BACKLOG.
