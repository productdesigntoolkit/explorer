#!/usr/bin/env python3
"""Erzeugt die Methodenuebersicht des Plugins aus data.js.

Schreibt `pdt-claude-plugin/docs/methodenuebersicht.md`: fuenf Spaces, je
Methode Aufruf, Titel, Zweck und Link auf die Methodenbibliothek.

    python3 build-plugin-docs.py
    python3 build-plugin-docs.py --check

Register: sachlich und unpersoenlich, nach dem Audience Profile
fachexperte-fuehrungskraft. Keine persoenliche Ansprache, keine Analogien.

Nur Standardbibliothek.
"""

import os, re, sys, json, argparse, datetime

PLUGIN = "pdt-claude-plugin"
SPACES = [
    ("strategy-space", "Strategy Space", "Warum und für wen?"),
    ("problem-space", "Problem Space", "Welches Problem wird gelöst?"),
    ("solution-space", "Solution Space", "Wie wird es gelöst?"),
    ("product-space", "Product Space", "Was wird gebaut und wie?"),
    ("market-space", "Market Space", "Wie kommt es an den Markt?"),
]


def frontmatter(path):
    s = open(path, encoding="utf-8").read()
    end = s.find("\n---", 3)
    fm = {}
    for line in s[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def first_sentence(text, limit=150):
    t = text.strip()
    m = re.search(r"^(.{20,}?[.!?])(\s|$)", t)
    s = m.group(1) if m else t
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + " …"


def build(root):
    gitbook = os.path.join(root, "gitbook-methods")
    rows = {}
    for space, _, _ in SPACES:
        d = os.path.join(gitbook, space)
        items = []
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            fm = frontmatter(os.path.join(d, fn))
            if not fm.get("skill"):
                continue
            items.append((fm.get("title", fn[:-3]), fm["skill"],
                          first_sentence(fm.get("description", "")),
                          f"{space}/{fn[:-3].lower()}"))
        items.sort(key=lambda x: re.sub(r"[^\w\s]", " ", x[0].lower()))
        rows[space] = items

    total = sum(len(v) for v in rows.values())
    out = []
    out.append("# Methodenübersicht")
    out.append("")
    out.append(f"{total} Methoden in fünf Spaces. Jede Methode wird über den angegebenen Befehl aufgerufen "
               "und führt durch die Anwendung bis zu einem Ergebnis in `pdt-workspace/`.")
    out.append("")
    out.append("Der Aufbau der Methode selbst, also Herkunft, Quellen und ausführliche Anleitung, steht in der "
               "Methodenbibliothek. Die Spalte Beschreibung nennt den Zweck in einem Satz.")
    out.append("")
    out.append("Ist die passende Methode unklar, genügt eine Beschreibung der Situation in eigenen Worten. "
               "Der Method Finder meldet sich ohne Befehl. Für einen Einstieg ohne Vorgabe: `/pdt:start`.")
    out.append("")
    out.append("---")
    out.append("")
    for space, label, frage in SPACES:
        out.append(f"## {label}")
        out.append("")
        out.append(f"*{frage}* · {len(rows[space])} Methoden · Wegweiser: `/pdt:{space.replace('-space','')}`")
        out.append("")
        out.append("| Aufruf | Methode | Beschreibung |")
        out.append("|--------|---------|--------------|")
        for title, sid, desc, slug in rows[space]:
            out.append(f"| `/pdt:{sid}` | [{title}](https://productdesigntoolkit.gitbook.io/"
                       f"productdesigntoolkit-docs/{slug}) | {desc} |")
        out.append("")
    out.append("---")
    out.append("")
    out.append("Diese Seite wird aus den Methodenquellen erzeugt und nicht von Hand gepflegt. "
               "Generator: `explorer/build-plugin-docs.py`.")
    out.append("")
    return "\n".join(out), total


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    target = os.path.join(root, PLUGIN, "docs", "methodenuebersicht.md")
    if not os.path.isdir(os.path.dirname(target)):
        os.makedirs(os.path.dirname(target), exist_ok=True)
    new, total = build(root)
    old = open(target, encoding="utf-8").read() if os.path.isfile(target) else None
    if old == new:
        print(f"Methodenübersicht aktuell, {total} Methoden.")
        return 0
    if args.check:
        print(f"Methodenübersicht veraltet. build-plugin-docs.py laufen lassen.")
        return 1
    open(target, "w", encoding="utf-8").write(new)
    print(f"Methodenübersicht geschrieben, {total} Methoden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
