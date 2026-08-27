#!/usr/bin/env python3
"""Erzeugt das Claude-Code-Plugin aus den Methodenquellen.

Aus `pdt-skills/{id}.md` werden Commands unter `pdt-claude-plugin/commands/{id}.md`.
Die Dialogfuehrung bleibt unveraendert, nur das Frontmatter wird umgestellt und
der Ausgabepfad zeigt ins Projekt des Nutzers statt in den Plugin-Ordner.

    python3 build-plugin.py
    python3 build-plugin.py --check

Handgepflegt im Plugin bleiben: Agents, Skills, Einstiegs- und Space-Commands,
Dokumentation. Erzeugt werden die Methoden-Commands, die uebrigen Dateien in commands/ bleiben handgepflegt.

Nur Standardbibliothek.
"""

import os, re, sys, argparse

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]
PLUGIN = "pdt-claude-plugin"


def frontmatter(path):
    s = open(path, encoding="utf-8").read()
    if not s.startswith("---"):
        return {}, s
    end = s.find("\n---", 3)
    fm = {}
    for line in s[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, s[end + 4:].lstrip("\n")


def method_index(gitbook):
    """{skill_id: (space, title, description)}"""
    out = {}
    for space in SPACES:
        d = os.path.join(gitbook, space)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            fm, _ = frontmatter(os.path.join(d, fn))
            if fm.get("skill"):
                out[fm["skill"]] = (space, fm.get("title", fn[:-3]), fm.get("description", ""))
    return out


def to_command(skill_src, mid, space, title, description):
    """Skill-Datei in eine Command-Datei umbauen."""
    fm, body = frontmatter_from_text(skill_src)
    desc = description or fm.get("description", "")
    hint = fm.get("argument-hint", '"[optional: Produkt, Unternehmen oder Kontext]"')
    head = (f"---\n"
            f"description: {desc}\n"
            f"argument-hint: {hint}\n"
            f"---\n\n")
    # Ausgabepfad zeigt ins Projekt des Nutzers, nicht in den Plugin-Ordner
    body = body.replace("`workspace/", "`pdt-workspace/")
    # Der Namensraum kommt vom Plugin, Verweise auf pdt: bleiben als Aufruf gueltig
    return head + body


def frontmatter_from_text(s):
    if not s.startswith("---"):
        return {}, s
    end = s.find("\n---", 3)
    fm = {}
    for line in s[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, s[end + 4:].lstrip("\n")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    gitbook = os.path.join(root, "gitbook-methods")
    skills = os.path.join(root, "pdt-skills")
    target = os.path.join(root, PLUGIN, "commands")
    if not os.path.isdir(os.path.join(root, PLUGIN)):
        print(f"Plugin-Ordner fehlt: {PLUGIN}")
        return 2

    idx = method_index(gitbook)
    os.makedirs(target, exist_ok=True)
    written, drift, problems = [], [], []

    for mid, (space, title, description) in sorted(idx.items()):
        src = os.path.join(skills, f"{mid}.md")
        if not os.path.isfile(src):
            problems.append(f"{mid}: Skill fehlt in pdt-skills")
            continue
        new = to_command(open(src, encoding="utf-8").read(), mid, space, title, description)
        dst = os.path.join(target, f"{mid}.md")
        old = open(dst, encoding="utf-8").read() if os.path.isfile(dst) else None
        if old == new:
            continue
        if args.check:
            drift.append(f"{mid}.md")
        else:
            open(dst, "w", encoding="utf-8").write(new)
            written.append(f"{mid}.md")

    # Verwaistes entfernen
    KEEP = {"start", "strategy", "problem", "solution", "product", "market"}
    for fn in sorted(os.listdir(target)):
        if fn.endswith(".md") and fn[:-3] not in idx and fn[:-3] not in KEEP:
            if args.check:
                drift.append(f"{fn} verwaist")
            else:
                os.remove(os.path.join(target, fn))
                written.append(f"{fn} entfernt")

    print(f"{len(idx)} Methoden mit Skill")
    if args.check:
        if drift or problems:
            for d in drift[:10]:
                print(f"  veraltet: {d}")
            if len(drift) > 10:
                print(f"  ... und {len(drift) - 10} weitere")
            for pr in problems:
                print(f"  PROBLEM: {pr}")
            return 1
        print("  Plugin-Commands aktuell.")
        return 0
    print(f"  geschrieben: {len(written)}")
    for pr in problems:
        print(f"  PROBLEM: {pr}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
