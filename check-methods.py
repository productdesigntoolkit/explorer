#!/usr/bin/env python3
"""Konsistenzpruefung der PDT-Methodenkette ueber alle Repos.

Prueft, ob eine Methode auf allen Ebenen vorhanden und stimmig ist:
YAML-Skeleton, Methodentext, SUMMARY, Explorer-Kopie, Skill, Skill-Mapping,
data.js, Template-Listen der Space-Commands und die Zaehler.

Reiner Report, aendert nichts. Exit 1 bei FEHLER, 0 bei nur HINWEIS.
Nur Standardbibliothek, kein pyyaml.
"""

import os, re, sys, json, argparse, subprocess

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]
CMD_FOR_SPACE = {s: s.replace("-space", "") for s in SPACES}

ERROR, WARN = "FEHLER", "HINWEIS"
findings = []


def add(level, check, msg):
    findings.append((level, check, msg))


# ---------- Einlesen ----------

def frontmatter(path):
    """Minimaler Frontmatter-Parser, gleiche Logik wie build.py."""
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    fm = {}
    for line in content[4:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, content[end + 4:].lstrip("\n")


def method_files(base):
    """{space: {dateiname_ohne_endung: pfad}}"""
    out = {}
    for space in SPACES:
        d = os.path.join(base, space)
        out[space] = {}
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".md") and fn != "README.md":
                out[space][fn[:-3]] = os.path.join(d, fn)
    return out


def load_data_js(explorer):
    p = os.path.join(explorer, "data.js")
    if not os.path.isfile(p):
        add(ERROR, "data.js", "data.js nicht gefunden")
        return None
    src = open(p, encoding="utf-8").read()
    try:
        return json.loads(src.split("const PDT_DATA = ", 1)[1].rstrip().rstrip(";\n").rstrip(";"))
    except Exception as e:
        add(ERROR, "data.js", f"data.js nicht parsebar: {e}")
        return None


# ---------- Pruefungen ----------

def check_gitbook_vs_explorer(gitbook, explorer):
    """Gibt (gitbook_dateien, explorer_dateien) zurueck."""
    g, e = method_files(gitbook), method_files(explorer)
    for space in SPACES:
        for name in sorted(set(g[space]) - set(e[space])):
            add(ERROR, "explorer-kopie", f"{space}/{name}.md fehlt im Explorer")
        for name in sorted(set(e[space]) - set(g[space])):
            add(ERROR, "explorer-kopie", f"{space}/{name}.md nur im Explorer, nicht in gitbook-methods")
        for name in sorted(set(g[space]) & set(e[space])):
            a = open(g[space][name], encoding="utf-8").read()
            b = open(e[space][name], encoding="utf-8").read()
            if a != b:
                add(ERROR, "explorer-kopie", f"{space}/{name}.md weicht von der Quelle ab")
    return g, e


def check_summary(gitbook, g):
    p = os.path.join(gitbook, "SUMMARY.md")
    if not os.path.isfile(p):
        add(ERROR, "summary", "SUMMARY.md nicht gefunden")
        return
    src = open(p, encoding="utf-8").read()
    for space in SPACES:
        for name in sorted(g[space]):
            if f"{space}/{name}.md" not in src:
                add(ERROR, "summary", f"{space}/{name}.md fehlt in SUMMARY.md")


def skill_ids(g):
    """{(space, name): skill_id} aus dem Frontmatter der Methodentexte."""
    out = {}
    for space in SPACES:
        for name, path in g[space].items():
            fm, _ = frontmatter(path)
            out[(space, name)] = fm.get("skill")
    return out


def check_yaml(templates, g, sids):
    if not os.path.isdir(templates):
        add(WARN, "yaml", f"{templates} nicht gefunden, Pruefung uebersprungen")
        return
    have = {fn[:-5] for fn in os.listdir(templates) if fn.endswith(".yaml")}
    used = set()
    for space in SPACES:
        for name in sorted(g[space]):
            sid = sids.get((space, name))
            if not sid:
                continue
            used.add(sid)
            if sid not in have:
                add(ERROR, "yaml", f"{sid}.yaml fehlt (Methode {space}/{name}.md)")
    for orphan in sorted(have - used):
        add(WARN, "yaml", f"{orphan}.yaml gehoert zu keiner Methode")


def check_skills(explorer, master, g, e, sids):
    edir = os.path.join(explorer, "skills")
    if not os.path.isdir(edir):
        add(ERROR, "skills", "explorer/skills/ nicht gefunden")
        return
    have_e = {fn[:-3] for fn in os.listdir(edir) if fn.endswith(".md") and fn != "README.md"}

    for space in SPACES:
        for name in sorted(g[space]):
            sid = sids.get((space, name))
            if not sid:
                add(WARN, "skill", f"{space}/{name}.md hat kein skill-Feld im Frontmatter")
                continue
            if sid not in have_e:
                add(ERROR, "skills", f"skills/{sid}.md fehlt (Methode {space}/{name}.md)")

    if os.path.isdir(master):
        have_m = {fn[:-3] for fn in os.listdir(master) if fn.endswith(".md") and fn != "README.md"}
        for sid in sorted(have_m - have_e):
            add(ERROR, "skill-ablagen", f"{sid}.md nur in pdt-skills, nicht im Explorer")
        for sid in sorted(have_e - have_m):
            add(ERROR, "skill-ablagen", f"{sid}.md nur im Explorer, nicht in pdt-skills")
        for sid in sorted(have_e & have_m):
            a = open(os.path.join(master, sid + ".md"), encoding="utf-8").read()
            b = open(os.path.join(edir, sid + ".md"), encoding="utf-8").read()
            if a != b:
                add(ERROR, "skill-ablagen", f"{sid}.md weicht zwischen pdt-skills und Explorer ab")
    else:
        add(WARN, "skill-ablagen", f"{master} nicht gefunden, Abgleich uebersprungen")


def check_data_js(data, g):
    if not data:
        return
    for space in SPACES:
        in_js = {m["file"][:-3] for m in data["methods"].get(space, [])}
        for name in sorted(set(g[space]) - in_js):
            add(ERROR, "data.js", f"{space}/{name}.md fehlt in data.js (build.py laufen lassen)")
        for name in sorted(in_js - set(g[space])):
            add(ERROR, "data.js", f"{name} steht in data.js, hat aber keine Methodendatei")
        for m in data["methods"].get(space, []):
            if not m.get("desc"):
                add(WARN, "data.js", f"{space}/{m['file']}: keine description im Frontmatter")


def check_counts(explorer, root):
    """Zaehler pruefen. Die Muster stehen in sync-counts.py, damit es nur eine Quelle gibt."""
    script = os.path.join(explorer, "sync-counts.py")
    if not os.path.isfile(script):
        add(WARN, "zaehler", "sync-counts.py nicht gefunden, Zaehler nicht geprueft")
        return
    r = subprocess.run([sys.executable, script, "--root", root, "--check"],
                       capture_output=True, text=True)
    if r.returncode == 0:
        return
    for line in r.stdout.splitlines():
        line = line.strip()
        if line and not line.startswith("Abweichungen") and "Methoden:" not in line:
            add(ERROR, "zaehler", line + "  (sync-counts.py laufen lassen)")
    if r.stderr.strip():
        add(ERROR, "zaehler", r.stderr.strip().splitlines()[-1])


def check_changelog(gitbook, data):
    """CHANGELOG.md muss existieren und im obersten Eintrag die aktuelle Methodenzahl nennen."""
    if not data:
        return
    p = os.path.join(gitbook, "CHANGELOG.md")
    if not os.path.isfile(p):
        add(ERROR, "changelog", "CHANGELOG.md in gitbook-methods fehlt")
        return
    src = open(p, encoding="utf-8").read()
    ver = re.search(r"^## \[([\d.]+)\]", src, re.M)
    cnt = re.search(r"Methoden gesamt:\s*(\d+)", src)
    soll = sum(len(v) for v in data["methods"].values())
    if not ver:
        add(ERROR, "changelog", "kein Versionseintrag im Format ## [x.y.z] gefunden")
    if not cnt:
        add(ERROR, "changelog", "oberster Eintrag nennt keine Zeile 'Methoden gesamt: N'")
    elif int(cnt.group(1)) != soll:
        add(ERROR, "changelog",
            f"oberster Eintrag{' ' + ver.group(1) if ver else ''} nennt {cnt.group(1)} Methoden,"
            f" es sind {soll}. Changelog nachtragen.")


def check_readme(explorer, data):
    if not data:
        return
    p = os.path.join(explorer, "README.md")
    if not os.path.isfile(p):
        return
    soll = sum(len(v) for v in data["methods"].values())
    src = open(p, encoding="utf-8").read()
    m = re.search(r"(\d+) methods across 5 spaces", src)
    if not m:
        add(WARN, "readme", "Methodenzahl im README nicht gefunden")
    elif int(m.group(1)) != soll:
        add(ERROR, "readme", f"README sagt {m.group(1)} Methoden, es sind {soll}")


# ---------- Ablauf ----------

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here),
                    help="Ordner mit den PDT-Repos (Default: Elternordner des Explorers)")
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    explorer = here
    gitbook = os.path.join(root, "gitbook-methods")
    templates = os.path.join(root, "pdt-templates", "pdt-yaml_skeletons_v0.1.0")
    master = os.path.join(root, "pdt-skills")

    print(f"PDT Methodenkette, Pruefung")
    print(f"Wurzel: {root}\n")

    if not os.path.isdir(gitbook):
        print(f"gitbook-methods nicht gefunden unter {gitbook}")
        return 1

    data = load_data_js(explorer)

    g, e = check_gitbook_vs_explorer(gitbook, explorer)
    sids = skill_ids(g)
    check_summary(gitbook, g)
    check_yaml(templates, g, sids)
    check_skills(explorer, master, g, e, sids)
    check_data_js(data, g)
    check_counts(explorer, root)
    check_changelog(gitbook, data)

    total = sum(len(v) for v in g.values())
    print(f"{total} Methoden in gitbook-methods")
    if data:
        print("Pro Space: " + ", ".join(f"{s.replace('-space','')} {len(data['methods'].get(s, []))}" for s in SPACES))
    print()

    errs = [f for f in findings if f[0] == ERROR]
    warns = [f for f in findings if f[0] == WARN]
    for level, group in ((ERROR, errs), (WARN, warns)):
        if not group:
            continue
        print(f"{level} ({len(group)})")
        for _, check, msg in group:
            print(f"  [{check}] {msg}")
        print()
    if not findings:
        print("Alles stimmig.")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
