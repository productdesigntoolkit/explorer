#!/usr/bin/env python3
"""Erzeugt die Methodenlisten in gitbook-methods/SUMMARY.md.

Der Anzeigetext kommt aus dem Feld `title` im Frontmatter, nicht aus dem
Dateinamen. Sortiert wird nach einem Schluessel ohne Satzzeichen, sonst
schiebt sich "Product Vision Statement" vor "Product-Market Fit", weil das
Leerzeichen im Zeichensatz vor dem Bindestrich steht.

Alles ausserhalb der fuenf Space-Abschnitte bleibt unveraendert, ebenso die
Intro-Zeile je Space.

    python3 sync-summary.py
    python3 sync-summary.py --check

Nur Standardbibliothek.
"""

import os, re, sys, argparse

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]


def frontmatter(path):
    s = open(path, encoding="utf-8").read()
    if not s.startswith("---"):
        return {}
    end = s.find("\n---", 3)
    fm = {}
    for line in s[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def sortkey(title):
    """Kleinschreibung, Satzzeichen zu Leerzeichen, Mehrfachleerzeichen zusammen."""
    t = title.lower()
    t = re.sub(r"[^\w\s]", " ", t, flags=re.UNICODE)
    return re.sub(r"\s+", " ", t).strip()


def method_lines(gitbook, space):
    out = []
    d = os.path.join(gitbook, space)
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md") or fn == "README.md":
            continue
        fm = frontmatter(os.path.join(d, fn))
        title = fm.get("title") or fn[:-3].replace("_", " ")
        out.append((sortkey(title), f"* [{title}]({space}/{fn})"))
    return [line for _, line in sorted(out)]


def rebuild(gitbook):
    p = os.path.join(gitbook, "SUMMARY.md")
    lines = open(p, encoding="utf-8").read().split("\n")
    out, i = [], 0
    space_of_heading = {}
    for s in SPACES:
        label = "## " + s.replace("-space", "").capitalize() + " Space"
        space_of_heading[label] = s
    # Market/Problem/... Grossschreibung passt, Strategy ebenso

    while i < len(lines):
        line = lines[i]
        out.append(line)
        space = space_of_heading.get(line.strip())
        if not space:
            i += 1
            continue
        i += 1
        # Abschnitt bis zur naechsten Ueberschrift einsammeln
        block = []
        while i < len(lines) and not lines[i].startswith("## "):
            block.append(lines[i])
            i += 1
        intro = [b for b in block if f"{space}/README.md" in b]
        blank_before = [b for b in block[:1] if b.strip() == ""]
        out.extend(blank_before)
        out.extend(intro)
        out.extend(method_lines(gitbook, space))
        # eine Leerzeile vor der naechsten Ueberschrift
        out.append("")
    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    gitbook = os.path.join(os.path.abspath(args.root), "gitbook-methods")
    p = os.path.join(gitbook, "SUMMARY.md")

    old = open(p, encoding="utf-8").read()
    new = rebuild(gitbook)
    if old == new:
        print("SUMMARY.md aktuell.")
        return 0
    diff = [(a, b) for a, b in zip(old.split("\n"), new.split("\n")) if a != b]
    if args.check:
        print(f"SUMMARY.md weicht ab, {len(diff)} Zeilen. sync-summary.py laufen lassen.")
        for a, b in diff[:12]:
            print(f"  - {a}\n  + {b}")
        return 1
    open(p, "w", encoding="utf-8").write(new)
    print(f"SUMMARY.md geschrieben, {len(diff)} Zeilen geaendert.")
    for a, b in diff[:20]:
        print(f"  - {a}\n  + {b}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
