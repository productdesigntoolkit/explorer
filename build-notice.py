#!/usr/bin/env python3
"""Erzeugt die NOTICE-Datei aus den Quellenblöcken der Methoden.

Die Herkunft kommt aus `## Quellen` jeder Methode, die Sonderfälle aus der von
Hand gepflegten `gitbook-methods/rights-exceptions.json`. Geschrieben wird nach
`pdt-claude-plugin/NOTICE` und `pdt-skills/NOTICE`, also in die beiden Ablagen,
die veroeffentlicht werden.

    python3 build-notice.py
    python3 build-notice.py --check

Luecken werden benannt, nicht verschwiegen. Nur Standardbibliothek.
"""

import os, re, sys, json, argparse, datetime

SPACES = [
    ("strategy-space", "Strategy Space"),
    ("problem-space", "Problem Space"),
    ("solution-space", "Solution Space"),
    ("product-space", "Product Space"),
    ("market-space", "Market Space"),
]
TARGETS = ["pdt-claude-plugin", "pdt-skills"]


def frontmatter(path):
    s = open(path, encoding="utf-8").read()
    end = s.find("\n---", 3)
    fm = {}
    for line in s[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, s[end + 4:]


def field(block, name):
    m = re.search(rf"\*\*{name}:\*\*\s*(.+?)\s*$", block, re.M)
    if not m:
        return None
    v = m.group(1).strip()
    # Markdown-Link zuerst aufloesen, sonst frisst die Kursiv-Bereinigung
    # Unterstriche in der URL
    v = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\2", v)
    if not v.startswith("http"):
        v = re.sub(r"_([^_]+)_", r"\1", v)
        v = re.sub(r"\*\*([^*]+)\*\*", r"\1", v)
    return v.strip() or None


def collect(gitbook):
    out, gaps = {}, []
    for space, label in SPACES:
        rows = []
        d = os.path.join(gitbook, space)
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            fm, body = frontmatter(os.path.join(d, fn))
            q = body.split("## Quellen", 1)[-1] if "## Quellen" in body else ""
            row = {
                "id": fm.get("skill"),
                "titel": fm.get("title", fn[:-3]),
                "autor": field(q, "Autor"),
                "werk": field(q, "Werk"),
                "jahr": field(q, "Jahr"),
                "link": field(q, "Link"),
            }
            fehlt = [k for k in ("autor", "werk", "jahr", "link") if not row[k]]
            if fehlt:
                gaps.append(f"{space}/{fn}: {', '.join(fehlt)}")
            rows.append(row)
        rows.sort(key=lambda r: re.sub(r"[^\w\s]", " ", r["titel"].lower()))
        out[space] = rows
    return out, gaps


def render(rows, exc, gaps):
    total = sum(len(v) for v in rows.values())
    L = []
    L.append("NOTICE")
    L.append("======")
    L.append("")
    L.append("Product Design Toolkit")
    L.append("Copyright (c) 2026 Ralph Hutter  ·  https://productdesigntoolkit.net")
    L.append("")
    L.append(f"Diese Sammlung bündelt {total} Methoden der digitalen Produktentwicklung.")
    L.append("Die redaktionelle Aufbereitung, also Struktur, Kurzanleitungen, Prompts und")
    L.append("Dialogführung, steht unter CC BY-NC-SA 4.0 und stammt von Ralph Hutter.")
    L.append("")
    L.append("Die Methoden selbst stammen von ihren jeweiligen Urhebern und sind nicht")
    L.append("durch diese Lizenz abgedeckt. Es gelten die Bedingungen der Rechteinhaber.")
    L.append("Diese Datei listet die Herkunft je Methode.")
    L.append("")
    if exc:
        L.append("")
        L.append("METHODEN MIT AUSDRÜCKLICHEN NUTZUNGSBEDINGUNGEN")
        L.append("-----------------------------------------------")
        L.append("")
        L.append("Für die folgenden Methoden haben die Rechteinhaber eigene Bedingungen")
        L.append("veröffentlicht, die über das allgemeine Urheberrecht hinausgehen.")
        L.append("")
        for mid, e in sorted(exc.items()):
            titel = e.get("titel") or next((r["titel"] for rs in rows.values() for r in rs if r["id"] == mid), mid)
            L.append(f"  {titel}")
            L.append(f"    Rechteinhaber: {e['rechteinhaber']}")
            for line in re.findall(r".{1,68}(?:\s|$)", e["bedingung"]):
                if line.strip():
                    L.append(f"    {line.strip()}")
            L.append(f"    Quelle: {e['quelle']}  (geprüft {e['geprueft']})")
            if e.get("status"):
                for line in re.findall(r".{1,68}(?:\s|$)", e["status"]):
                    if line.strip():
                        L.append(f"    {line.strip()}")
            L.append("")
    L.append("")
    L.append("HERKUNFT DER METHODEN")
    L.append("---------------------")
    L.append("")
    for space, label in SPACES:
        L.append(label)
        L.append("-" * len(label))
        L.append("")
        for r in rows[space]:
            L.append(f"  {r['titel']}")
            teile = []
            if r["autor"]:
                teile.append(r["autor"])
            if r["werk"]:
                teile.append(r["werk"])
            if r["jahr"]:
                teile.append(str(r["jahr"]))
            L.append("    " + (" · ".join(teile) if teile else "Urheber nicht erfasst"))
            if r["link"]:
                L.append(f"    {r['link']}")
            if r["id"] in exc:
                L.append("    Siehe Abschnitt zu den Nutzungsbedingungen oben.")
            L.append("")
    L.append("")
    L.append("LÜCKEN")
    L.append("------")
    L.append("")
    if gaps:
        L.append(f"Bei {len(gaps)} von {total} Methoden ist die Quellenangabe unvollständig.")
        L.append("Häufigster Fall ist ein fehlendes Jahr bei Methoden ohne einzelne")
        L.append("Urheberschaft, etwa Problem Statement oder Marktstrategie. Die Angaben")
        L.append("werden nachgetragen, sobald sie am Original geprüft sind.")
        L.append("")
        for g in gaps:
            L.append(f"  {g}")
    else:
        L.append("Keine. Alle Methoden tragen Autor, Werk, Jahr und Link.")
    L.append("")
    L.append("")
    L.append("Diese Datei wird erzeugt: explorer/build-notice.py")
    L.append("Sonderfälle von Hand: gitbook-methods/rights-exceptions.json")
    L.append("")
    return "\n".join(L)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    gitbook = os.path.join(root, "gitbook-methods")

    excp = os.path.join(gitbook, "rights-exceptions.json")
    exc = {}
    if os.path.isfile(excp):
        exc = {k: v for k, v in json.load(open(excp, encoding="utf-8")).items() if not k.startswith("_")}
    else:
        print("Hinweis: rights-exceptions.json fehlt, Sonderfälle werden nicht ausgewiesen")

    rows, gaps = collect(gitbook)
    text = render(rows, exc, gaps)

    stale = []
    for t in TARGETS:
        p = os.path.join(root, t, "NOTICE")
        if not os.path.isdir(os.path.dirname(p)):
            continue
        old = open(p, encoding="utf-8").read() if os.path.isfile(p) else None
        if old == text:
            continue
        if args.check:
            stale.append(f"{t}/NOTICE")
        else:
            open(p, "w", encoding="utf-8").write(text)
            stale.append(f"{t}/NOTICE geschrieben")

    total = sum(len(v) for v in rows.values())
    print(f"{total} Methoden, {len(exc)} mit ausdrücklichen Bedingungen, {len(gaps)} unvollständige Quellenangaben")
    if args.check:
        if stale:
            for s in stale:
                print(f"  veraltet: {s}")
            return 1
        print("  NOTICE aktuell.")
        return 0
    for s in stale:
        print(f"  {s}")
    if not stale:
        print("  NOTICE war aktuell")
    return 0


if __name__ == "__main__":
    sys.exit(main())
