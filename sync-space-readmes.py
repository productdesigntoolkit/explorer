#!/usr/bin/env python3
"""Erzeugt die Methodenlisten in den fuenf Space-READMEs von gitbook-methods.

Die READMEs waren bisher das einzige handgepflegte Navigationsartefakt der
Kette und entsprechend abgedriftet: zwoelf Methoden fehlten in den Listen,
drei Eintraege zeigten auf geloeschte GitBook-Seiten (/broken/pages/...), und
ein Platzhalter im urspruenglichen Generator war mit dem letzten Methodennamen
statt mit dem Space-Namen gefuellt worden ("Die Methoden im SWOT Analyse ...").

Ersetzt wird ausschliesslich:
  - der Listenblock unter "## Alle Methoden in diesem Space"
  - die Willkommenszeile
  - die Einleitungszeile unter "## Wann diese Methoden nutzen?"
  - die Aufzaehlungszeile "Systematischer {slug}-Arbeit"

Alles andere bleibt unveraendert, insbesondere "## Tipps fuer diesen Space".
Dort wachsen die handgeschriebenen Teile weiter, ohne Marker.

Der Anzeigetext kommt aus dem Feld `title` im Frontmatter, nicht aus dem
Dateinamen, und wird wie in sync-summary.py sortiert.

    python3 sync-space-readmes.py
    python3 sync-space-readmes.py --check

Nur Standardbibliothek.
"""

import os, re, sys, argparse

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]

LIST_HEADING = "## Alle Methoden in diesem Space"
USE_HEADING = "## Wann diese Methoden nutzen?"


def label(space):
    """strategy-space -> Strategy Space"""
    return space.replace("-space", "").capitalize() + " Space"


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
        out.append((sortkey(title), f"* [{title}]({fn})"))
    return [line for _, line in sorted(out)]


def rebuild(gitbook, space):
    p = os.path.join(gitbook, space, "README.md")
    lines = open(p, encoding="utf-8").read().split("\n")
    lab = label(space)
    slug = space.replace("-space", "")
    out, i = [], 0

    while i < len(lines):
        line = lines[i]

        if line.strip() == LIST_HEADING:
            out.append(line)
            i += 1
            # Block bis zur naechsten Ueberschrift verwerfen und neu schreiben
            while i < len(lines) and not lines[i].startswith("## "):
                i += 1
            out.append("")
            out.extend(method_lines(gitbook, space))
            out.append("")
            continue

        if line.startswith("Willkommen im"):
            out.append(
                f"Willkommen im **{lab}**! Hier findest du alle Methoden "
                f"dieser Phase deiner Produktentwicklung."
            )
            i += 1
            continue

        if line.startswith("Die Methoden im ") and line.rstrip().endswith("helfen dir bei:"):
            out.append(f"Die Methoden im {lab} helfen dir bei:")
            i += 1
            continue

        m = re.match(rf"^([*-]) Systematischer {slug}-Arbeit\s*$", line)
        if m:
            # Aufzaehlungszeichen der Umgebung uebernehmen, die Listen sind
            # je nach Space mit * oder - gesetzt
            out.append(f"{m.group(1)} Systematischer Arbeit im {lab}")
            i += 1
            continue

        out.append(line)
        i += 1

    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    gitbook = os.path.join(os.path.abspath(args.root), "gitbook-methods")

    changed, total = [], 0
    for space in SPACES:
        p = os.path.join(gitbook, space, "README.md")
        old = open(p, encoding="utf-8").read()
        new = rebuild(gitbook, space)
        if old == new:
            continue
        diff = [(a, b) for a, b in zip(old.split("\n"), new.split("\n")) if a != b]
        total += len(diff)
        changed.append((space, p, new, diff))

    if not changed:
        print("Space-READMEs aktuell.")
        return 0

    if args.check:
        print(f"Space-READMEs weichen ab, {len(changed)} Dateien, {total} Zeilen. "
              f"sync-space-readmes.py laufen lassen.")
        for space, _, _, diff in changed:
            print(f"  {space}: {len(diff)} Zeilen")
        return 1

    for space, p, new, diff in changed:
        open(p, "w", encoding="utf-8").write(new)
        print(f"{space}/README.md geschrieben, {len(diff)} Zeilen geaendert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
