#!/usr/bin/env python3
"""Legt die drei Inhaltsdateien einer neuen Methode als Geruest an.

    python3 new-method.py product-market-fit \
        --space solution --title "Product-Market Fit" \
        --group Validation --oneliner "Does the market pull the product"

Erzeugt YAML-Skeleton, Methodentext und Skill mit vollstaendigem Schema und
TODO-Markern. Ueberschreibt nichts. Was danach zu tun ist, steht im Ablauf
gitbook-methods/ADDING-A-METHOD.md.

Nur Standardbibliothek.
"""

import os, re, sys, argparse, datetime

PHASE = {"strategy": "WHY", "problem": "WHAT", "solution": "WHAT", "product": "HOW", "market": "WHEN"}
ACTIVITY = {
    "strategy": "Strategy Definition", "problem": "Problem Discovery",
    "solution": "Solution Validation", "product": "Solution Development",
    "market": "Solution Availability",
}
TODO = "TODO"


def filename_from_title(title):
    t = title.replace("/", " ").replace("—", " ").replace("–", " ")
    t = re.sub(r"[^\w\s\-()]", "", t)
    t = re.sub(r"\s+", "_", t.strip())
    return t


def yaml_stub(mid, name, space, activity, priority):
    return f"""id: {mid}
name: {name}
space: {space}
phase: {PHASE[space]}
activity: {activity}
priority: {priority}

aliases:
  - {TODO} bekannte Kurzform
  - {TODO} alternativer deutscher Name

canonical_source:
  author: {TODO}
  work: {TODO}
  year: {TODO}
  url: {TODO}

fields:
  - id: {TODO}_snake_case
    label: {TODO} deutsches Label
    hint: "{TODO} konkrete Anleitung, handlungsorientiert, kein triviales Was ist dein Ziel."
  - id: {TODO}_zweites_feld
    label: {TODO}
    hint: "{TODO}"
  - id: {TODO}_drittes_feld
    label: {TODO}
    hint: "{TODO}"

pdt_notes: |
  {TODO} PDT-spezifischer Kontext in zwei bis vier Saetzen. Bezug auf den Space,
  auf Problem-First, und ein typischer Fehler.

related:
  before:
    - {TODO}-slug
  after:
    - {TODO}-slug
  alternative:
    - {TODO}-slug

version: "0.9.2"
pdt_version: "0.9.2"
created_at: "{datetime.date.today().isoformat()}"
updated_at: "{datetime.date.today().isoformat()}"
"""


def method_stub(mid, title, space, group, oneliner):
    grp = f'group: "{group}"\n' if group else ""
    return f"""---
title: "{title}"
space: {space}-space
description: "{TODO} ein Satz, der sagt was die Methode ist und was sie leistet."
skill: {mid}
{grp}oneliner: "{oneliner}"
---

# {title}

## Kurzbeschreibung

{TODO} Was ist die Methode, in zwei bis drei Saetzen.

## Einsatzzweck

{TODO} Wann einsetzen, wofuer sie taugt, wofuer nicht.

## Kurzanleitung

1. **{TODO} Schritt:** {TODO} Anleitung → {TODO} Beispiel.
2. **{TODO} Schritt:** {TODO} → {TODO}.
3. **{TODO} Schritt:** {TODO} → {TODO}.

## Beispielprompt

{{% code overflow="wrap" %}}
```
{TODO} Prompt, der durch die Felder des YAML fuehrt und Belege statt Behauptungen verlangt.
```
{{% endcode %}}

## Quellen

**Autor:** {TODO}
**Werk:** _{TODO}_
**Jahr:** {TODO}
**Link:** [{TODO}]({TODO})
**Typ:** kanonisch

**Ergaenzende Quellen:**

* {TODO}
"""


def skill_stub(mid, title, space):
    return f"""---
name: pdt:{mid}
description: {title} nach {TODO}: {TODO} was die Methode leistet
argument-hint: "[optional: Produkt, Unternehmen oder Kontext]"
---

# PDT: {title}

## Methode

**Quelle:** {TODO}
**Space:** {space.capitalize()} Space
**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs/{space}-space/{mid.replace('-', '_')}

{TODO} Was die Methode ist und wie sie sich im PDT einordnet.

**Wann einsetzen:** {TODO} Anlass, plus ein typischer Fehler.

**Verwandte Methoden:**
- Davor: {TODO}
- Danach: {TODO}
- Alternative: {TODO}

---

## Deine Rolle

{TODO} Haltung des Agenten, worauf er besteht, was er nicht durchgehen laesst.

---

## Prozess

### 1. Einfuehrung

{TODO} Logik der Methode in zwei Saetzen.

### 2. Kontext erfragen

> "{TODO} Einstiegsfrage"

### 3. Die Felder durcharbeiten

**Feld 1 – {TODO}**
*Hint: {TODO} aus dem YAML uebernehmen.*

{TODO} Worauf der Agent hier achtet.

---

## Output-Format

Schlage den Dateinamen vor:
`workspace/{space}/{mid}-{{kontextname}}.md`

```markdown
# {title}
**{TODO}:** {{name}}
**Datum:** {{datum}}
**Quelle:** {TODO}

---

{TODO} Tabellen und Abschnitte des Ergebnisses

---

*Erstellt mit PDT Claude Plugin · productdesigntoolkit.net*
```

---

## Nach dem Output

{TODO} Empfehlung fuer den naechsten Schritt.

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
"""


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("id", help="Skill-ID in kebab-case, zugleich Name des YAML")
    ap.add_argument("--space", required=True, choices=list(PHASE))
    ap.add_argument("--title", required=True)
    ap.add_argument("--group", default="", help="thematische Gruppe, im Strategy Space leer lassen")
    ap.add_argument("--oneliner", default=TODO + " englische Kurzzeile")
    ap.add_argument("--activity", default=None)
    ap.add_argument("--priority", type=int, default=2, choices=[1, 2, 3])
    ap.add_argument("--root", default=os.path.dirname(here))
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    mid, space, title = args.id, args.space, args.title
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", mid):
        print(f"id muss kebab-case sein: {mid}")
        return 2
    activity = args.activity or ACTIVITY[space]
    fn = filename_from_title(title)

    targets = [
        (os.path.join(root, "pdt-templates", "pdt-yaml_skeletons_v0.1.0", f"{mid}.yaml"),
         yaml_stub(mid, title, space, activity, args.priority)),
        (os.path.join(root, "gitbook-methods", f"{space}-space", f"{fn}.md"),
         method_stub(mid, title, space, args.group, args.oneliner)),
        (os.path.join(root, "pdt-skills", f"{mid}.md"),
         skill_stub(mid, title, space)),
    ]
    exists = [p for p, _ in targets if os.path.exists(p)]
    if exists:
        for p in exists:
            print(f"existiert bereits: {os.path.relpath(p, root)}")
        return 1
    for p, content in targets:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", encoding="utf-8").write(content)
        print(f"angelegt: {os.path.relpath(p, root)}")

    n = sum(content.count(TODO) for _, content in targets)
    print(f"\n{n} TODO-Marker. Reihenfolge: erst das YAML, dann Methodentext, dann Skill.")
    print("Danach: ./sync-methods.sh, python3 sync-changelog.py --new " + mid + ",")
    print(f"        python3 audit-method.py {mid} --online --pre-publish")
    return 0


if __name__ == "__main__":
    sys.exit(main())
