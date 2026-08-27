#!/usr/bin/env python3
"""Schreibt alle Methodenzaehler aus data.js in die Dokumente, die sie nennen.

Eine Methode zu ergaenzen heisst heute, an mehreren Stellen Zahlen nachzuziehen.
Dieses Skript ist die einzige Stelle, die das tut. `--check` schreibt nicht,
sondern meldet nur Abweichungen und liefert Exit 1.

Nur Standardbibliothek.
"""

import os, re, sys, json, argparse

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]
CMD_FOR_SPACE = {s: s.replace("-space", "") for s in SPACES}
LABEL_FOR_SPACE = {
    "strategy-space": "Strategy Space",
    "problem-space": "Problem Space",
    "solution-space": "Solution Space",
    "product-space": "Product Space",
    "market-space": "Market Space",
}


def load_counts(explorer):
    p = os.path.join(explorer, "data.js")
    src = open(p, encoding="utf-8").read()
    data = json.loads(src.split("const PDT_DATA = ", 1)[1].rstrip().rstrip(";\n").rstrip(";"))
    per = {s: len(data["methods"].get(s, [])) for s in SPACES}
    return per, sum(per.values())


def targets(root, explorer, per, total):
    """Liste von (pfad, [(regex, ersetzung), ...]). Ersetzung darf \\g<1> nutzen."""
    gitbook = os.path.join(root, "gitbook-methods")
    plugin = os.path.join(root, "pdt-claude-plugin", "commands")
    t = []

    # Explorer README, Gesamtzahl
    t.append((os.path.join(explorer, "README.md"), [
        (r"\d+ methods across 5 spaces", f"{total} methods across 5 spaces"),
    ]))

    # GitHub README der Methodenbibliothek: Gesamtzahl, Aufzaehlung, Strukturbaum
    rules = [(r"\*\*[\d+]+ Methoden, Tools und Templates\*\*", f"**{total} Methoden, Tools und Templates**")]
    for s in SPACES:
        rules.append((rf"(\*\*{LABEL_FOR_SPACE[s]}\*\* \()\d+( Methoden\))", rf"\g<1>{per[s]}\g<2>"))
        rules.append((rf"(├── {s}/\s+# )\d+( Methoden)", rf"\g<1>{per[s]}\g<2>"))
    t.append((os.path.join(gitbook, "GITHUB_README.md"), rules))

    # GitBook Landing Page, Gesamtzahl
    t.append((os.path.join(gitbook, "README.md"), [
        (r"\*\*[\d+]+ Methoden, Tools und Templates\*\*", f"**{total} Methoden, Tools und Templates**"),
    ]))

    # Seiten des Explorers, Gesamtzahl und die Space-Zahlen auf der Plugin-Seite
    for page in ["about.html", "infografik.html", "plugin.html"]:
        t.append((os.path.join(explorer, page), [(r"\b\d+ Methoden\b", f"{total} Methoden")]))
    plugin_rules = [(r'(<div class="fact-n">)\d+(</div><div class="fact-l">Methoden als Befehle)', rf"\g<1>{total}\g<2>")]
    for s_ in SPACES:
        plugin_rules.append(
            (rf'(<span class="space-name">{LABEL_FOR_SPACE[s_]}</span>.*?<span class="space-n">)\d+(</span>)',
             rf"\g<1>{per[s_]}\g<2>"))
    t.append((os.path.join(explorer, "plugin.html"), plugin_rules))

    # Space-Commands des Plugins, zwei Zaehler je Datei
    for s in SPACES:
        t.append((os.path.join(plugin, CMD_FOR_SPACE[s] + ".md"), [
            (r"\(\d+ templates\)", f"({per[s]} templates)"),
            (r"## Templates \(\d+\)", f"## Templates ({per[s]})"),
        ]))
    return t


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--check", action="store_true", help="nur melden, nichts schreiben")
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    per, total = load_counts(here)
    drift, written = [], []

    for path, rules in targets(root, here, per, total):
        if not os.path.isfile(path):
            drift.append(f"{os.path.relpath(path, root)}: Datei nicht gefunden")
            continue
        src = open(path, encoding="utf-8").read()
        new = src
        for pat, rep in rules:
            if not re.search(pat, new):
                drift.append(f"{os.path.relpath(path, root)}: Muster nicht gefunden, {pat}")
                continue
            new = re.sub(pat, rep, new)
        if new != src:
            rel = os.path.relpath(path, root)
            if args.check:
                drift.append(f"{rel}: Zaehler veraltet")
            else:
                open(path, "w", encoding="utf-8").write(new)
                written.append(rel)

    print(f"{total} Methoden: " + ", ".join(f"{CMD_FOR_SPACE[s]} {per[s]}" for s in SPACES))
    if args.check:
        if drift:
            print("\nAbweichungen:")
            for d in drift:
                print(f"  {d}")
            return 1
        print("Alle Zaehler aktuell.")
        return 0
    for w in written:
        print(f"  aktualisiert: {w}")
    for d in drift:
        print(f"  PROBLEM: {d}")
    if not written and not drift:
        print("  nichts zu tun, alle Zaehler waren aktuell")
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main())
