#!/usr/bin/env python3
"""Erzeugt die Template-Listen in pdt-claude_plugin/commands/{space}.md.

Quelle sind die Felder `title`, `group` und `oneliner` im Frontmatter der
Methoden. Gruppen erscheinen in der Reihenfolge, die in GROUP_ORDER steht,
innerhalb einer Gruppe wird alphabetisch sortiert. Alles ausserhalb des
Templates-Blocks bleibt unveraendert.

    python3 sync-commands.py
    python3 sync-commands.py --check

Nur Standardbibliothek.
"""

import os, re, sys, argparse

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]
CMD_FOR_SPACE = {s: s.replace("-space", "") for s in SPACES}

# Reihenfolge der Gruppen je Space. Strategy fuehrt bewusst eine flache Liste.
GROUP_ORDER = {
    "strategy-space": [],
    "problem-space": ["Research & Discovery", "Synthesis & Analysis", "Problem Definition", "Value Discovery"],
    "solution-space": ["Ideation", "Definition", "Prototyping", "Validation"],
    "product-space": ["Vision & Strategy", "Requirements & Features", "Planning & Prioritization", "Architecture & Technology"],
    "market-space": ["Go-to-Market", "Brand & Content", "Growth & Acquisition", "Segmentation & Targeting", "Measurement & Optimization"],
}


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


def sortkey(t):
    t = re.sub(r"[^\w\s]", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def methods(gitbook, space):
    out = []
    d = os.path.join(gitbook, space)
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md") or fn == "README.md":
            continue
        fm = frontmatter(os.path.join(d, fn))
        out.append({"title": fm.get("title", fn[:-3]),
                    "group": fm.get("group"),
                    "oneliner": fm.get("oneliner", "")})
    return out


def render(space, ms, problems):
    lines, n = [], 0
    order = GROUP_ORDER.get(space) or []
    if order:
        seen = set()
        for g in order:
            grp = sorted([m for m in ms if m["group"] == g], key=lambda m: sortkey(m["title"]))
            if not grp:
                continue
            lines.append("")
            lines.append(f"### {g}")
            for m in grp:
                n += 1
                lines.append(f"{n}. **{m['title']}** – {m['oneliner']}")
                seen.add(m["title"])
        rest = [m for m in ms if m["title"] not in seen]
        if rest:
            for m in rest:
                problems.append(f"{space}: '{m['title']}' hat die Gruppe '{m['group']}', die nicht in GROUP_ORDER steht")
    else:
        lines.append("")
        for m in sorted(ms, key=lambda m: sortkey(m["title"])):
            n += 1
            lines.append(f"{n}. **{m['title']}** – {m['oneliner']}")
    lines.append("")
    return "\n".join(lines), n


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    gitbook = os.path.join(root, "gitbook-methods")
    plugin = os.path.join(root, "pdt-claude_plugin", "commands")

    problems, changed = [], []
    for space in SPACES:
        p = os.path.join(plugin, CMD_FOR_SPACE[space] + ".md")
        if not os.path.isfile(p):
            problems.append(f"{os.path.basename(p)} nicht gefunden")
            continue
        ms = methods(gitbook, space)
        for m in ms:
            if not m["oneliner"]:
                problems.append(f"{space}: '{m['title']}' hat kein Feld oneliner")
        block, n = render(space, ms, problems)
        src = open(p, encoding="utf-8").read()
        m = re.search(r"(## Templates \(\d+\)\n)(.*?)(\n## Suggested Paths)", src, re.S)
        if not m:
            problems.append(f"{os.path.basename(p)}: Templates-Block nicht gefunden")
            continue
        new = src[:m.start(1)] + f"## Templates ({n})\n" + block + src[m.start(3):]
        new = re.sub(r"\(\d+ templates\)", f"({n} templates)", new, count=1)
        if new != src:
            changed.append(os.path.relpath(p, root))
            if not args.check:
                open(p, "w", encoding="utf-8").write(new)

    if args.check:
        if changed or problems:
            for c in changed:
                print(f"  veraltet: {c}")
            for pr in problems:
                print(f"  PROBLEM: {pr}")
            return 1
        print("Template-Listen aktuell.")
        return 0
    for c in changed:
        print(f"  aktualisiert: {c}")
    for pr in problems:
        print(f"  PROBLEM: {pr}")
    if not changed and not problems:
        print("  Template-Listen waren aktuell")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
