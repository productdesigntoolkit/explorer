# Backlog

Vorhaben rund um den Explorer und die Methodenkette. Stand 2026-08-27.

Kontext: Eine Methode lebt in fünf Repos, die Checkliste dazu steht in `gitbook-methods/ADDING-A-METHOD.md`, die Prüfung in `check-methods.py`. Ziel der Arbeitspakete unten ist, die Zahl der Handgriffe pro Methode von zehn auf fünf zu senken.

## AP 1 · Product_Lifecycle reparieren · erledigt 2026-08-27

- [x] `description` ins Frontmatter
- [x] Überschriften auf das Format der übrigen Dateien gebracht, doppelte Anker-ID entfernt
- [x] Kurzanleitung und Beispielprompt ergänzt, beide fehlten als einzige der 85 Methoden
- [x] `build.py` und `check-methods.py` sauber

Die Figure, die Phasentabelle und der PDF-Download sind unverändert erhalten.

## AP 2 · skill-Feld in die Quelle holen · erledigt 2026-08-27

- [x] Feld in allen 81 Methodendateien mit Skill in `gitbook-methods` gesetzt, aus der bisherigen Tabelle generiert
- [x] `SKILL_MAP` und `add-skill-mapping.py` entfernt
- [x] `check-methods.py` liest die Skill-ID aus dem Frontmatter und vergleicht Quelle gegen Kopie auf exakte Gleichheit

Vier Methoden haben bewusst keinen Skill und damit kein Feld, sie erscheinen als Hinweis: `Value_Proposition_Jobs_to_be_done`, `Value_Proposition_Pains_and_Gains`, `Hooked_Model`, `UAC_Tracker`.

## AP 3 · sync-methods.sh statt Handkopie · erledigt 2026-08-27

- [x] `sync-methods.sh` schreibt den Spiegel, ruft `build.py`, `sync-counts.py` und `check-methods.py`
- [x] Entfernt im Explorer auch, was in der Quelle nicht mehr existiert
- [x] `--check` als Trockenlauf, Exit 1 bei Abweichung
- [x] Schritte 5, 7 und 9 in `ADDING-A-METHOD.md` darauf umgestellt

Bewusst lokal und nicht als GitHub Action: `gitbook-methods` ist privat, `explorer` ist öffentlich. Ein Token dafür im öffentlichen Repo wäre ein zu hoher Preis für einen gesparten Handgriff.

## AP 4 · Zähler generieren · erledigt 2026-08-27

`sync-counts.py` schreibt elf Zahlen in acht Dateien aus `data.js`: Gesamtzahl im Explorer-README, Gesamtzahl und fünf Space-Zahlen in `gitbook-methods/GITHUB_README.md`, Gesamtzahl in der GitBook-Landing-Page, dazu je zwei Zähler in den fünf Space-Commands. Die inhaltlichen Listen bleiben Handarbeit.

- [x] `sync-counts.py` schreiben, mit `--check` für den Trockenlauf
- [x] Schritte 6 und 7 in `ADDING-A-METHOD.md` angepasst
- [x] `check-methods.py` ruft `sync-counts.py --check` auf, statt die Muster ein zweites Mal zu führen

## AP 5 · Release-Aufgaben des Plugins

Priorität 3 · abhängig vom Releasetermin

Steht im BACKLOG des Plugin-Projekts unter `brain/LABS/030-IN_PROGRESS/pdt-claude_plugin/`: Methoden-Skills aus `pdt-skills` nachfüllen und die Suggested Paths der fünf Space-Commands kuratieren. Beides gehört an den Punkt, an dem das Plugin gepackt wird.

## AP 6 · SUMMARY.md generieren · erledigt 2026-08-27

- [x] `sync-summary.py` erzeugt die Methodenlisten aus Dateiliste und `title`, Teil von `sync-methods.sh`
- [x] Sortierung über einen Schlüssel ohne Satzzeichen
- [x] Elf Zeilen korrigiert, darunter acht Anzeigenamen und drei Sortierfehler
- [x] `title` von `Impact Mapping (Strategy)` korrigiert, dort fehlte die Klammer

Alles ausserhalb der fünf Space-Abschnitte bleibt unverändert, ebenso die Intro-Zeile je Space. Gegengeprüft: 102 Linkziele vorher wie nachher, keines verloren, keines neu.

## AP 7 · Template-Listen generieren

Priorität 3 · halber Tag · mittleres Risiko

Die Listen in `pdt-claude_plugin/commands/*.md` sind halb mechanisch. Nummerierung und Gruppenzuordnung wären ableitbar, sobald jede Methode zwei zusätzliche Frontmatter-Felder trägt: die thematische Gruppe und den englischen Einzeiler. Danach bleibt pro Methode nur dieser eine Satz Autorenarbeit.

- [ ] Felder `group` und `oneliner` in 85 Methoden ergänzen
- [ ] Generator schreiben, Teil von `sync-methods.sh`

## Kleinere offene Punkte

- Vier Methoden haben bewusst keinen Skill (`Value_Proposition_Jobs_to_be_done`, `Value_Proposition_Pains_and_Gains`, `Hooked_Model`, `UAC_Tracker`). `check-methods.py` meldet sie als Hinweis. Entweder Skills nachziehen oder die Ausnahme im Skript hinterlegen.
- `uac-tracker.yaml` in `pdt-templates` gehört zu keiner Methode mit Skill, Kehrseite des Punkts oben.
- `mockup-method` und `mockups-wireframes` überschneiden sich funktional, steht schon im Plugin-BACKLOG.
