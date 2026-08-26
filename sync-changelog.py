#!/usr/bin/env python3
"""Schreibt einen Eintrag in gitbook-methods/CHANGELOG.md.

    python3 sync-changelog.py --new product-market-fit
    python3 sync-changelog.py --bump patch --note "Quellenangabe korrigiert"
    python3 sync-changelog.py --check

Die Methodenzahl kommt aus data.js, die naechste Version aus dem obersten
Eintrag. Idempotent: Ist die Methode schon im Changelog genannt, passiert
nichts. Der erzeugte Text ist ein Geruest, das praezisiert werden darf.

Nur Standardbibliothek.
"""

import os, re, sys, json, argparse, datetime

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]


def frontmatter(path):
    s = open(path, encoding="utf-8").read()
    end = s.find("\n---", 3)
    fm = {}
    for line in s[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def find_method(gitbook, mid):
    for space in SPACES:
        d = os.path.join(gitbook, space)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            fm = frontmatter(os.path.join(d, fn))
            if fm.get("skill") == mid:
                return space, fm
    return None, None


def total_methods(explorer):
    src = open(os.path.join(explorer, "data.js"), encoding="utf-8").read()
    d = json.loads(src.split("const PDT_DATA = ", 1)[1].rstrip().rstrip(";\n").rstrip(";"))
    return sum(len(v) for v in d["methods"].values())


def next_version(clsrc, part):
    m = re.search(r"^## \[(\d+)\.(\d+)\.(\d+)\]", clsrc, re.M)
    if not m:
        return "1.0.0"
    ma, mi, pa = (int(x) for x in m.groups())
    if part == "major":
        return f"{ma + 1}.0.0"
    if part == "minor":
        return f"{ma}.{mi + 1}.0"
    return f"{ma}.{mi}.{pa + 1}"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--new", metavar="ID", help="Eintrag fuer eine neue Methode")
    ap.add_argument("--bump", choices=["major", "minor", "patch"])
    ap.add_argument("--note", default="")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    gitbook = os.path.join(root, "gitbook-methods")
    cl = os.path.join(gitbook, "CHANGELOG.md")
    clsrc = open(cl, encoding="utf-8").read()
    total = total_methods(here)

    if args.check:
        m = re.search(r"Methoden gesamt:\s*(\d+)", clsrc)
        if not m:
            print("oberster Eintrag nennt keine Methodenzahl")
            return 1
        if int(m.group(1)) != total:
            print(f"oberster Eintrag nennt {m.group(1)} Methoden, es sind {total}")
            return 1
        print("Changelog aktuell.")
        return 0

    if args.new:
        space, fm = find_method(gitbook, args.new)
        if not space:
            print(f"Methode mit skill '{args.new}' nicht gefunden")
            return 2
        title = fm.get("title", args.new)
        if title in clsrc:
            print(f"'{title}' steht bereits im Changelog, nichts zu tun.")
            return 0
        desc = fm.get("description", "").rstrip(".")
        label = space.replace("-space", "").capitalize() + " Space"
        body = (f"### Neu\n"
                f"- **{title}** ({label}): {desc}. "
                f"Skill `pdt:{args.new}`, YAML-Skeleton, Eintrag in `commands/{space.replace('-space','')}.md`.\n")
        ver = next_version(clsrc, "minor")
    elif args.bump:
        if not args.note:
            print("--bump braucht --note")
            return 2
        rub = {"major": "### Geändert", "minor": "### Neu", "patch": "### Behoben"}[args.bump]
        body = f"{rub}\n- {args.note}\n"
        ver = next_version(clsrc, args.bump)
    else:
        print("entweder --new, --bump oder --check")
        return 2

    today = datetime.date.today().isoformat()
    entry = f"## [{ver}] · {today}\n\nMethoden gesamt: {total}\n\n{body}\n"
    anchor = re.search(r"^## \[", clsrc, re.M)
    clsrc = clsrc[:anchor.start()] + entry + clsrc[anchor.start():]
    open(cl, "w", encoding="utf-8").write(clsrc)
    print(f"Changelog {ver} geschrieben, {total} Methoden.")
    print("Text pruefen und bei Bedarf praezisieren.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
