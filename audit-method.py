#!/usr/bin/env python3
"""Audit einer einzelnen Methode und Publikationsreport.

Laeuft am Ende von ADDING-A-METHOD.md, nach dem Committen. Geht die Checkliste
Schritt fuer Schritt durch, prueft Inhalt und Konsistenz der Methode ueber alle
fuenf Repos und schreibt einen Report.

    python3 audit-method.py product-market-fit
    python3 audit-method.py product-market-fit --online   # Quell-Links abrufen
    python3 audit-method.py product-market-fit --out PFAD

Exit 1, wenn ein Schritt offen ist. Nur Standardbibliothek.
"""

import os, re, sys, json, argparse, subprocess, datetime

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]
CMD_FOR_SPACE = {s: s.replace("-space", "") for s in SPACES}
YAML_KEYS = ["id", "name", "space", "phase", "activity", "priority", "aliases",
             "canonical_source", "fields", "pdt_notes", "related",
             "version", "pdt_version", "created_at", "updated_at"]
METHOD_SECTIONS = ["Kurzbeschreibung", "Einsatzzweck", "Kurzanleitung", "Beispielprompt", "Quellen"]
SKILL_SECTIONS = ["Methode", "Deine Rolle", "Prozess", "Output-Format", "Nach dem Output", "Sprache"]

OK, FAIL, INFO = "ok", "offen", "hinweis"


class Report:
    def __init__(self):
        self.steps = []      # (nr, titel, status, detail)
        self.audit = []      # (bereich, status, text)
        self.manual = []     # was nicht maschinell pruefbar ist

    def step(self, nr, titel, status, detail=""):
        self.steps.append((nr, titel, status, detail))

    def note(self, bereich, status, text):
        self.audit.append((bereich, status, text))

    def failed(self):
        return [s for s in self.steps if s[2] == FAIL] + [a for a in self.audit if a[1] == FAIL]


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
    return fm, s[end + 4:]


def sections(text):
    return re.findall(r"^##\s+(.+?)\s*$", text, re.M)


def find_method(gitbook, needle):
    """Findet die Methodendatei ueber Dateiname, Skill-ID oder Titel."""
    needle_l = needle.lower().replace(" ", "").replace("-", "").replace("_", "")
    for space in SPACES:
        d = os.path.join(gitbook, space)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            p = os.path.join(d, fn)
            fm, _ = frontmatter(p)
            cands = [fn[:-3], fm.get("skill", ""), fm.get("title", "")]
            for c in cands:
                if c and c.lower().replace(" ", "").replace("-", "").replace("_", "").replace("/", "") == needle_l:
                    return space, fn[:-3], p, fm
    return None, None, None, None


def parse_yaml_lite(path):
    """Reicht fuer die drei Formen, die in den Skeletons vorkommen."""
    txt = open(path, encoding="utf-8").read()
    top = set(re.findall(r"^([a-z_]+):", txt, re.M))
    fields = re.findall(r"^  - id:\s*(\S+)", txt, re.M)
    related = re.findall(r"^    - (\S+)", txt, re.M)
    def val(k):
        m = re.search(rf"^{k}:\s*(.+)$", txt, re.M)
        return m.group(1).strip().strip('"') if m else None
    return txt, top, fields, related, val


def git_state(repo):
    """Zustand eines Repos. reports/ bleibt aussen vor, das Audit schreibt dorthin selbst."""
    if not os.path.isdir(os.path.join(repo, ".git")):
        return "kein Repo"
    def g(*a):
        return subprocess.run(["git", "-C", repo] + list(a), capture_output=True, text=True).stdout.strip()
    dirty = bool(g("status", "--porcelain", "--", ".", ":(exclude)reports"))
    ahead = g("rev-list", "--count", "@{u}..HEAD") or "0"
    if dirty:
        return "nicht committet"
    if ahead != "0":
        return f"{ahead} Commit(s) nicht gepusht"
    return "committet und gepusht"


def check_url(url, timeout=8):
    import urllib.request, urllib.error
    req = urllib.request.Request(url, headers={"User-Agent": "pdt-audit"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return str(e)[:60]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("method", help="Dateiname, Skill-ID oder Titel der Methode")
    ap.add_argument("--root", default=os.path.dirname(here))
    ap.add_argument("--online", action="store_true", help="Quell-Links abrufen")
    ap.add_argument("--pre-publish", action="store_true",
                    help="vor der Veroeffentlichung: offene Repos sind erwartet, kein Fehler")
    ap.add_argument("--out", help="Zieldatei des Reports")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    explorer = here
    gitbook = os.path.join(root, "gitbook-methods")
    templates = os.path.join(root, "pdt-templates", "pdt-yaml_skeletons_v0.1.0")
    skills = os.path.join(root, "pdt-skills")
    plugin = os.path.join(root, "pdt-claude_plugin", "commands")

    space, stem, mpath, fm = find_method(gitbook, args.method)
    if not space:
        print(f"Methode nicht gefunden: {args.method}")
        return 2
    sid = fm.get("skill")
    title = fm.get("title", stem)
    r = Report()

    # ---- Schritt 1, YAML-Skeleton
    ypath = os.path.join(templates, f"{sid}.yaml") if sid else None
    if not sid:
        r.step(1, "YAML-Skeleton", INFO, "Methode hat bewusst keinen Skill, daher kein Skeleton")
    elif not ypath or not os.path.isfile(ypath):
        r.step(1, "YAML-Skeleton", FAIL, f"{sid}.yaml fehlt")
    else:
        txt, top, fields, related, val = parse_yaml_lite(ypath)
        missing = [k for k in YAML_KEYS if k not in top]
        problems = []
        if missing:
            problems.append("fehlende Schluessel: " + ", ".join(missing))
        if not 3 <= len(fields) <= 10:
            problems.append(f"{len(fields)} Felder, erlaubt sind 3 bis 10")
        if val("space") not in [s.replace("-space", "") for s in SPACES]:
            problems.append(f"space '{val('space')}' unbekannt")
        if val("phase") not in ["WHY", "WHAT", "HOW", "WHEN"]:
            problems.append(f"phase '{val('phase')}' unbekannt")
        if val("space") != CMD_FOR_SPACE[space]:
            problems.append(f"space im YAML ist '{val('space')}', Methode liegt in {space}")
        have_yaml = {f[:-5] for f in os.listdir(templates) if f.endswith(".yaml")}
        broken = [s for s in related if s not in have_yaml]
        if broken:
            problems.append("related zeigt ins Leere: " + ", ".join(broken))
        if re.search(r"\b(ae|oe|ue)\b|Stueck|fuer|koennen|waere", txt):
            problems.append("transliterierte Umlaute gefunden, echte Umlaute verwenden")
        todos = txt.count("TODO")
        if todos:
            problems.append(f"{todos} TODO-Marker offen")
        r.step(1, "YAML-Skeleton", FAIL if problems else OK,
               "; ".join(problems) or f"{len(fields)} Felder, Schema vollstaendig")

    # ---- Schritt 2, Methodentext
    body = open(mpath, encoding="utf-8").read()
    _, text = frontmatter(mpath)
    problems = []
    for k in ["title", "space", "description"]:
        if not fm.get(k):
            problems.append(f"Frontmatter ohne {k}")
    if not sid:
        problems.append("Frontmatter ohne skill (nur zulaessig, wenn bewusst kein Skill existiert)")
    secs = sections(text)
    for s in METHOD_SECTIONS:
        if s not in secs:
            problems.append(f"Abschnitt fehlt: {s}")
    if fm.get("space") != space:
        problems.append(f"space im Frontmatter ist '{fm.get('space')}', Datei liegt in {space}")
    todos = body.count("TODO")
    if todos:
        problems.append(f"{todos} TODO-Marker offen")
    steps_n = len(re.findall(r"^\d+\. \*\*", text, re.M))
    r.step(2, "Methodentext", FAIL if problems else OK,
           "; ".join(problems) or f"{len(secs)} Abschnitte, {steps_n} Schritte in der Kurzanleitung")

    # ---- Schritt 3, SUMMARY
    sm = open(os.path.join(gitbook, "SUMMARY.md"), encoding="utf-8").read()
    m = re.search(rf"\* \[(.+?)\]\({space}/{re.escape(stem)}\.md\)", sm)
    if not m:
        r.step(3, "SUMMARY.md", FAIL, "kein Eintrag")
    elif m.group(1) != title:
        r.step(3, "SUMMARY.md", INFO, f"Anzeigetext '{m.group(1)}' weicht vom title '{title}' ab")
    else:
        r.step(3, "SUMMARY.md", OK, f"Eintrag vorhanden, Text gleich dem title")

    # ---- Schritt 4, Skill
    spath = os.path.join(skills, f"{sid}.md") if sid else None
    if not sid:
        r.step(4, "Skill", INFO, "bewusst kein Skill")
    elif not os.path.isfile(spath):
        r.step(4, "Skill", FAIL, f"{sid}.md fehlt in pdt-skills")
    else:
        sfm, stext = frontmatter(spath)
        problems = []
        if sfm.get("name") != f"pdt:{sid}":
            problems.append(f"name ist '{sfm.get('name')}', erwartet 'pdt:{sid}'")
        desc = sfm.get("description", "")
        if not desc:
            problems.append("description fehlt")
        elif "–" in desc or "—" in desc:
            problems.append("description nutzt einen Gedankenstrich, Konvention ist der Doppelpunkt")
        for s in SKILL_SECTIONS:
            if s not in sections(stext):
                problems.append(f"Abschnitt fehlt: {s}")
        todos = open(spath, encoding="utf-8").read().count("TODO")
        if todos:
            problems.append(f"{todos} TODO-Marker offen")
        r.step(4, "Skill", FAIL if problems else OK,
               "; ".join(problems) or "Frontmatter und Abschnitte vollstaendig")

    # ---- Schritt 5, Spiegel
    problems = []
    ecopy = os.path.join(explorer, space, f"{stem}.md")
    if not os.path.isfile(ecopy):
        problems.append("Methodentext fehlt im Explorer")
    elif open(ecopy, encoding="utf-8").read() != body:
        problems.append("Methodentext weicht von der Quelle ab")
    if sid:
        scopy = os.path.join(explorer, "skills", f"{sid}.md")
        if not os.path.isfile(scopy):
            problems.append("Skill fehlt im Explorer")
        elif open(scopy, encoding="utf-8").read() != open(spath, encoding="utf-8").read():
            problems.append("Skill weicht von der Quelle ab")
    djs = os.path.join(explorer, "data.js")
    if os.path.isfile(djs):
        d = json.loads(open(djs, encoding="utf-8").read().split("const PDT_DATA = ", 1)[1].rstrip().rstrip(";\n").rstrip(";"))
        entry = [x for x in d["methods"].get(space, []) if x["file"] == f"{stem}.md"]
        if not entry:
            problems.append("fehlt in data.js, build.py laufen lassen")
        elif not entry[0].get("desc"):
            problems.append("data.js hat keine description fuer diese Methode")
    r.step(5, "Spiegel und data.js", FAIL if problems else OK,
           "; ".join(problems) or "Kopien byteweise identisch, Eintrag in data.js vorhanden")

    # ---- Schritt 6, Template-Liste
    cpath = os.path.join(plugin, CMD_FOR_SPACE[space] + ".md")
    if not os.path.isfile(cpath):
        r.step(6, "Template-Liste", INFO, "Command-Datei nicht gefunden")
    else:
        csrc = open(cpath, encoding="utf-8").read()
        r.step(6, "Template-Liste", OK if title in csrc else FAIL,
               f"Eintrag in commands/{CMD_FOR_SPACE[space]}.md" if title in csrc else "kein Eintrag")

    # ---- Schritt 7, Zaehler
    res = subprocess.run([sys.executable, os.path.join(explorer, "sync-counts.py"),
                          "--root", root, "--check"], capture_output=True, text=True)
    r.step(7, "Zaehler", OK if res.returncode == 0 else FAIL,
           "alle aktuell" if res.returncode == 0 else res.stdout.strip().splitlines()[-1])

    # ---- Schritt 8, Changelog
    cl = os.path.join(gitbook, "CHANGELOG.md")
    if not os.path.isfile(cl):
        r.step(8, "Changelog", FAIL, "CHANGELOG.md fehlt")
    else:
        clsrc = open(cl, encoding="utf-8").read()
        if title in clsrc:
            r.step(8, "Changelog", OK, "Methode im Changelog genannt")
        else:
            # Methoden, die seit Einfuehrung des Changelogs nicht angefasst wurden,
            # koennen dort nicht stehen. Das ist kein offener Punkt.
            dates = re.findall(r"^## \[[\d.]+\] · (\d{4}-\d{2}-\d{2})", clsrc, re.M)
            start = min(dates) if dates else None
            # Datum der Anlage, nicht der letzten Aenderung: strukturelle Sammel-
            # aenderungen fassen alle Dateien an, ohne jede Methode einzeln zu nennen.
            added = subprocess.run(["git", "-C", gitbook, "log", "--diff-filter=A",
                                    "--format=%ad", "--date=short", "--",
                                    os.path.relpath(mpath, gitbook)],
                                   capture_output=True, text=True).stdout.strip().splitlines()
            added = added[-1] if added else ""
            if start and added and added < start:
                r.step(8, "Changelog", INFO,
                       f"Methode am {added} angelegt, Changelog beginnt am {start}")
            else:
                r.step(8, "Changelog", FAIL, f"'{title}' kommt im Changelog nicht vor")

    # ---- Schritt 9, Kette
    res = subprocess.run([sys.executable, os.path.join(explorer, "check-methods.py"), "--root", root],
                         capture_output=True, text=True)
    r.step(9, "check-methods.py", OK if res.returncode == 0 else FAIL,
           "keine Fehler" if res.returncode == 0 else "Fehler, Ausgabe des Skripts pruefen")

    # ---- Schritt 10, Git
    states = {name: git_state(os.path.join(root, name)) for name in
              ["pdt-templates", "gitbook-methods", "pdt-skills", "explorer", "pdt-claude_plugin"]}
    offen = [f"{k}: {v}" for k, v in states.items() if v not in ("committet und gepusht", "kein Repo")]
    if args.pre_publish:
        r.step(10, "Repos", INFO,
               "vor der Veroeffentlichung, offen: " + ("; ".join(offen) or "nichts"))
    else:
        r.step(10, "Repos", FAIL if offen else OK, "; ".join(offen) or "alle fuenf committet und gepusht")

    # ---- Inhaltliches Audit
    q = text.split("## Quellen", 1)[-1] if "## Quellen" in text else ""
    for label, pat in [("Autor", r"\*\*Autor:\*\*"), ("Werk", r"\*\*Werk:\*\*"),
                       ("Jahr", r"\*\*Jahr:\*\*"), ("Link", r"\*\*Link:\*\*")]:
        r.note("Quellenblock", OK if re.search(pat, q) else FAIL,
               f"{label} {'vorhanden' if re.search(pat, q) else 'fehlt'}")
    years = re.findall(r"\*\*Jahr:\*\*\s*_?(\d{4})", q)
    if years:
        y = int(years[0])
        thisyear = datetime.date.today().year
        r.note("Quellenblock", OK if 1900 <= y <= thisyear else FAIL,
               f"Jahr {y} plausibel" if 1900 <= y <= thisyear else f"Jahr {y} unplausibel")

    urls = re.findall(r"https?://[^\s\)\]]+", q)
    if args.online and urls:
        for u in dict.fromkeys(urls):
            st = check_url(u)
            r.note("Quell-Link", OK if st == 200 else FAIL, f"{st}  {u}")
    elif urls:
        r.note("Quell-Link", INFO, f"{len(set(urls))} Links im Quellenblock, mit --online pruefbar")

    if sid and ypath and os.path.isfile(ypath):
        _, _, fields, _, _ = parse_yaml_lite(ypath)
        r.note("YAML gegen Text", INFO,
               f"{len(fields)} YAML-Felder, {steps_n} Schritte in der Kurzanleitung")
        if os.path.isfile(spath):
            sk = open(spath, encoding="utf-8").read()
            fehlend = [f for f in fields if f.replace("_", " ") not in sk.lower().replace("_", " ")]
            blocks = len(re.findall(r"^\*\*(Feld|Power|Schritt|Power)\s", sk, re.M))
            r.note("YAML gegen Skill", INFO,
                   f"{blocks} Prozessbloecke im Skill gegenueber {len(fields)} YAML-Feldern")

    r.manual = [
        "Fachliche Richtigkeit des Inhalts",
        "Uebereinstimmung der Quellenangabe mit dem Originalwerk, also Autor, Titel, Jahr, Seitenzahlen",
        "Ob die Hints im YAML fuer Studierende tatsaechlich weiterhelfen",
        "Ob die Methode im richtigen Space und in der richtigen Aktivitaet liegt",
    ]

    # ---- Ausgabe
    today = datetime.date.today().isoformat()
    lines = []
    lines.append(f"# Publikationsreport: {title}")
    lines.append("")
    lines.append(f"**Datum:** {today}  ")
    lines.append(f"**Space:** {space}  ")
    lines.append(f"**Datei:** `{space}/{stem}.md`  ")
    lines.append(f"**Skill:** `{sid or 'keiner'}`")
    lines.append("")
    lines.append("## Checkliste")
    lines.append("")
    lines.append("| Nr | Schritt | Status | Befund |")
    lines.append("|----|---------|--------|--------|")
    sym = {OK: "ok", FAIL: "OFFEN", INFO: "Hinweis"}
    for nr, t, st, det in r.steps:
        lines.append(f"| {nr} | {t} | {sym[st]} | {det} |")
    lines.append("")
    lines.append("## Audit")
    lines.append("")
    for bereich, st, txt in r.audit:
        lines.append(f"- **{bereich}** [{sym[st]}] {txt}")
    lines.append("")
    lines.append("## Nicht maschinell prüfbar")
    lines.append("")
    for m_ in r.manual:
        lines.append(f"- {m_}")
    lines.append("")
    fails = r.failed()
    lines.append(f"**Ergebnis:** {'publiziert, alle Schritte erledigt' if not fails else str(len(fails)) + ' Punkt(e) offen'}")
    out = "\n".join(lines) + "\n"

    print(out)
    target = args.out or os.path.join(explorer, "reports", f"{today}-{sid or stem}.md")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, "w", encoding="utf-8").write(out)
    print(f"Report: {os.path.relpath(target, root)}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
