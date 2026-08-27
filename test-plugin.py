#!/usr/bin/env python3
"""Testsuite fuer das PDT Claude Plugin.

    python3 test-plugin.py              alle Gruppen
    python3 test-plugin.py --group B    nur eine Gruppe

Gruppen:
  A  Struktur und Manifest
  B  Commands, 85 Methoden plus Einstieg plus 5 Spaces
  C  Agents
  D  Skills
  E  Konsistenz zur Quelle
  F  Paketierung

Exit 1, sobald ein Test fehlschlaegt. Nur Standardbibliothek.
"""

import os, re, sys, json, argparse, subprocess, zipfile, tempfile, shutil

PLUGIN = "pdt-claude-plugin"
SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]
CMD_SECTIONS = ["Methode", "Deine Rolle", "Prozess", "Output-Format", "Sprache"]

results = []


def check(group, name, ok, detail=""):
    results.append((group, name, bool(ok), detail))


def frontmatter(path):
    s = open(path, encoding="utf-8").read()
    if not s.startswith("---"):
        return {}, s
    end = s.find("\n---", 3)
    if end == -1:
        return {}, s
    fm = {}
    for line in s[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, s[end + 4:]


TOP = {"start", "strategy", "problem", "solution", "product", "market"}


def all_commands(root):
    d = os.path.join(root, PLUGIN, "commands")
    return {fn[:-3]: os.path.join(d, fn) for fn in sorted(os.listdir(d)) if fn.endswith(".md")}


def method_commands(root):
    return {k: v for k, v in all_commands(root).items() if k not in TOP}


def top_commands(root):
    return {k: v for k, v in all_commands(root).items() if k in TOP}


# ---------- A, Struktur und Manifest ----------

def group_a(root):
    p = os.path.join(root, PLUGIN)
    mani = os.path.join(p, ".claude-plugin", "plugin.json")
    check("A", "A1 plugin.json am richtigen Ort", os.path.isfile(mani))
    if os.path.isfile(mani):
        d = json.load(open(mani, encoding="utf-8"))
        check("A", "A2 Pflichtfeld name in kebab-case",
              bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", d.get("name", ""))), d.get("name", ""))
        for f in ["version", "description", "author", "license"]:
            check("A", f"A3 Metadatum {f}", f in d)
        check("A", "A4 version nach SemVer",
              bool(re.fullmatch(r"\d+\.\d+\.\d+", str(d.get("version", "")))), str(d.get("version")))
    mk = os.path.join(p, ".claude-plugin", "marketplace.json")
    check("A", "A5 marketplace.json vorhanden", os.path.isfile(mk))
    if os.path.isfile(mk) and os.path.isfile(mani):
        m = json.load(open(mk, encoding="utf-8"))
        names = [x.get("name") for x in m.get("plugins", [])]
        check("A", "A6 Marketplace nennt das Plugin", json.load(open(mani, encoding="utf-8"))["name"] in names, str(names))
    for d_ in ["commands", "agents", "skills"]:
        check("A", f"A7 {d_}/ auf Plugin-Ebene", os.path.isdir(os.path.join(p, d_)))
    check("A", "A8 keine Komponenten in .claude-plugin/",
          not any(os.path.isdir(os.path.join(p, ".claude-plugin", x)) for x in ["commands", "agents", "skills"]))
    r = subprocess.run(["claude", "plugin", "validate", "--strict", p], capture_output=True, text=True)
    check("A", "A9 claude plugin validate --strict", r.returncode == 0, r.stdout.strip().splitlines()[-1] if r.stdout else "")


# ---------- B, Commands ----------

def group_b(root):
    meths = method_commands(root)
    tops = top_commands(root)
    check("B", "B1 85 Methoden-Commands", len(meths) == 85, f"{len(meths)}")
    check("B", "B2 Einstieg und 5 Spaces", set(tops) == {"start", "strategy", "problem", "solution", "product", "market"},
          ", ".join(sorted(tops)))
    check("B", "B3 keine Namenskollision", not (set(meths) & set(tops)), ", ".join(sorted(set(meths) & set(tops))))
    sub = [x for x in os.listdir(os.path.join(root, PLUGIN, "commands"))
           if os.path.isdir(os.path.join(root, PLUGIN, "commands", x))]
    check("B", "B3b keine Unterordner in commands/, die werden nicht gefunden", not sub, ", ".join(sub))

    no_desc, has_name, no_hint, ws, todo, secs, nolink = [], [], [], [], [], [], []
    for mid, p in {**meths, **tops}.items():
        fm, body = frontmatter(p)
        if not fm.get("description"):
            no_desc.append(mid)
        if "name" in fm:
            has_name.append(mid)
        if mid in meths:
            if "argument-hint" not in fm:
                no_hint.append(mid)
            missing = [s for s in CMD_SECTIONS if not re.search(rf"^## {re.escape(s)}\s*$", body, re.M)]
            if missing:
                secs.append(f"{mid}: {', '.join(missing)}")
            if "productdesigntoolkit.gitbook.io" not in body:
                nolink.append(mid)
        if re.search(r"`workspace/", body):
            ws.append(mid)
        if "TODO" in body:
            todo.append(mid)
    check("B", "B4 jede Datei hat description", not no_desc, ", ".join(no_desc[:5]))
    check("B", "B5 kein name-Feld, Namensraum kommt vom Plugin", not has_name, ", ".join(has_name[:5]))
    check("B", "B6 Methoden haben argument-hint", not no_hint, ", ".join(no_hint[:5]))
    check("B", "B7 Ausgabepfad zeigt nicht in den Plugin-Ordner", not ws, ", ".join(ws[:5]))
    check("B", "B8 keine TODO-Marker", not todo, ", ".join(todo[:5]))
    check("B", "B9 Pflichtabschnitte vorhanden", not secs, "; ".join(secs[:3]))
    check("B", "B10 Verweis auf die Methodenbibliothek", not nolink, ", ".join(nolink[:5]))


# ---------- C, Agents ----------

def group_c(root):
    d = os.path.join(root, PLUGIN, "agents")
    files = {fn[:-3]: os.path.join(d, fn) for fn in sorted(os.listdir(d)) if fn.endswith(".md")}
    check("C", "C1 11 Agents", len(files) == 11, f"{len(files)}")
    spaces = {f"space-{s.replace('-space','')}" for s in SPACES}
    check("C", "C2 fuenf Space-Agents", spaces <= set(files), ", ".join(sorted(spaces - set(files))))
    check("C", "C3 sechs Spezialisten", len([f for f in files if f.startswith("specialist-")]) == 6)
    no_desc, short, refs = [], [], []
    for name, p in files.items():
        fm, body = frontmatter(p)
        if not fm.get("description"):
            no_desc.append(name)
        elif len(fm["description"]) < 80:
            short.append(name)
        for ref in re.findall(r"`(space-[a-z]+|specialist-[a-z]+)`", body):
            if ref not in files:
                refs.append(f"{name} -> {ref}")
    check("C", "C4 jeder Agent hat description", not no_desc, ", ".join(no_desc))
    check("C", "C5 description aussagekraeftig", not short, ", ".join(short))
    check("C", "C6 verwiesene Agents existieren", not refs, "; ".join(sorted(set(refs))[:5]))


# ---------- D, Skills ----------

def group_d(root):
    d = os.path.join(root, PLUGIN, "skills")
    dirs = [x for x in sorted(os.listdir(d)) if os.path.isdir(os.path.join(d, x))]
    check("D", "D1 Skills als Ordner", len(dirs) >= 2, ", ".join(dirs))
    flat = [x for x in os.listdir(d) if x.endswith(".md")]
    check("D", "D2 keine flachen Skill-Dateien", not flat, ", ".join(flat))
    meths = set(method_commands(root))
    tops = set(top_commands(root))
    for name in dirs:
        sp = os.path.join(d, name, "SKILL.md")
        check("D", f"D3 {name}/SKILL.md vorhanden", os.path.isfile(sp))
        if not os.path.isfile(sp):
            continue
        fm, body = frontmatter(sp)
        check("D", f"D4 {name} name stimmt mit Ordner", fm.get("name") == name, fm.get("name", ""))
        desc = fm.get("description", "")
        check("D", f"D5 {name} description mit Auslösern", len(desc) > 120 and ("when" in desc.lower() or "Use" in desc))
        broken = [c for c in re.findall(r"/pdt:([a-z0-9-]+)", body) if c not in meths and c not in tops]
        check("D", f"D6 {name} verweist nur auf vorhandene Commands", not broken, ", ".join(sorted(set(broken))))


# ---------- E, Konsistenz zur Quelle ----------

def group_e(root, here):
    r = subprocess.run([sys.executable, os.path.join(here, "build-plugin.py"), "--root", root, "--check"],
                       capture_output=True, text=True)
    check("E", "E1 Commands entsprechen den Quellen", r.returncode == 0, r.stdout.strip().splitlines()[-1] if r.stdout else "")
    r = subprocess.run([sys.executable, os.path.join(here, "check-methods.py"), "--root", root],
                       capture_output=True, text=True)
    check("E", "E2 Methodenkette fehlerfrei", r.returncode == 0)
    data = json.loads(open(os.path.join(here, "data.js"), encoding="utf-8").read()
                      .split("const PDT_DATA = ", 1)[1].rstrip().rstrip(";\n").rstrip(";"))
    total = sum(len(v) for v in data["methods"].values())
    check("E", "E3 Anzahl Commands gleich Anzahl Methoden", len(method_commands(root)) == total, f"{total}")
    gitbook = os.path.join(root, "gitbook-methods")
    ids = set()
    for space in SPACES:
        for fn in os.listdir(os.path.join(gitbook, space)):
            if fn.endswith(".md") and fn != "README.md":
                fm, _ = frontmatter(os.path.join(gitbook, space, fn))
                if fm.get("skill"):
                    ids.add(fm["skill"])
    r = subprocess.run([sys.executable, os.path.join(here, "build-plugin-docs.py"), "--root", root, "--check"],
                       capture_output=True, text=True)
    check("E", "E5 Methodenuebersicht aktuell", r.returncode == 0, r.stdout.strip())
    ov = os.path.join(root, PLUGIN, "docs", "methodenuebersicht.md")
    if os.path.isfile(ov):
        txt = open(ov, encoding="utf-8").read()
        calls = set(re.findall(r"`/pdt:([a-z0-9-]+)`", txt))
        known = set(all_commands(root))
        check("E", "E6 Uebersicht verweist nur auf vorhandene Commands",
              calls <= known, ", ".join(sorted(calls - known)[:5]))
        check("E", "E7 Uebersicht ohne persoenliche Ansprache",
              not re.search(r"\b(du|dir|dich|dein\w*)\b|\b(Sie|Ihre\w*|Ihrem|Ihren)\b", txt),
              "Register laut Audience Profile: unpersoenlich")
    check("E", "E4 IDs stimmen mit den Methoden ueberein", ids == set(method_commands(root)),
          ", ".join(sorted(ids ^ set(method_commands(root)))[:5]))


# ---------- F, Paketierung ----------

def group_f(root):
    p = os.path.join(root, PLUGIN)
    tmp = tempfile.mkdtemp(prefix="pdt-zip-")
    zpath = os.path.join(tmp, "pdt-claude-plugin.zip")
    n = 0
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for base, dirs, files in os.walk(p):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
            for f in files:
                if f == ".DS_Store":
                    continue
                full = os.path.join(base, f)
                z.write(full, os.path.join("pdt-claude-plugin", os.path.relpath(full, p)))
                n += 1
    size = os.path.getsize(zpath) / 1024
    check("F", "F1 ZIP laesst sich packen", n > 100, f"{n} Dateien, {size:.0f} KB")
    out = os.path.join(tmp, "entpackt")
    with zipfile.ZipFile(zpath) as z:
        z.extractall(out)
    unpacked = os.path.join(out, "pdt-claude-plugin")
    check("F", "F2 Manifest im entpackten ZIP",
          os.path.isfile(os.path.join(unpacked, ".claude-plugin", "plugin.json")))
    check("F", "F3 Methoden im entpackten ZIP",
          len([f for f in os.listdir(os.path.join(unpacked, "commands")) if f.endswith(".md")]) == 91)
    r = subprocess.run(["claude", "plugin", "validate", "--strict", unpacked], capture_output=True, text=True)
    check("F", "F4 entpacktes ZIP validiert", r.returncode == 0)
    shutil.rmtree(tmp)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--group", choices=list("ABCDEF"))
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    groups = {"A": lambda: group_a(root), "B": lambda: group_b(root), "C": lambda: group_c(root),
              "D": lambda: group_d(root), "E": lambda: group_e(root, here), "F": lambda: group_f(root)}
    for g in ([args.group] if args.group else list("ABCDEF")):
        groups[g]()

    print(f"PDT Plugin, Testlauf\nPfad: {os.path.join(root, PLUGIN)}\n")
    cur = None
    for g, name, ok, detail in results:
        if g != cur:
            print(f"--- Gruppe {g}")
            cur = g
        print(f"  {'ok   ' if ok else 'FEHLT'} {name}" + (f"   [{detail}]" if detail else ""))
    fails = [r for r in results if not r[2]]
    print(f"\n{len(results) - len(fails)} von {len(results)} bestanden")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
