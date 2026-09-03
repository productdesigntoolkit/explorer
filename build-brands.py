#!/usr/bin/env python3
"""Rendert die Seiten aus src/ fuer jede Marke unter brands/.

Eine Quelle, zwei Ausgaben. Wer eine Seite aendert, aendert sie in src/ und
laesst dieses Skript laufen; danach sind beide Fassungen auf demselben Stand.
Genau darum sind die Dateien im Repo-Root und in hwz/ generiert und nicht
von Hand gepflegt.

    python3 build-brands.py            bauen
    python3 build-brands.py --check    nichts schreiben, nur melden was abweicht

Eine Marke besteht aus vier Teilen:

    brands/<id>/brand.json   Ausgabeort, Pfadpraefix, kurze Strings, Titel
    brands/<id>/tokens.css   der :root-Block, fuellt {{TOKENS}}
    brands/<id>/brand.css    Zusatzregeln, fuellt {{BRAND_CSS}}
    brands/<id>/parts.html   mehrzeilige HTML- und JS-Bausteine
    brands/<id>/assets/      Dateien, die neben die Seiten kopiert werden

Platzhalter sind {{GROSSBUCHSTABEN}}, Ziffern erlaubt. Bleibt einer uebrig,
bricht der Lauf ab; lieber ein Fehler als eine Seite, die ihn anzeigt.

Nur Standardbibliothek.
"""

import os, re, sys, json, shutil, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")
BRANDS = os.path.join(HERE, "brands")

BANNER = ("<!-- Generiert von build-brands.py aus src/{page} und brands/{brand}/. "
          "Nicht direkt bearbeiten, Aenderungen gehen beim naechsten Lauf verloren. -->")

PART_RE = re.compile(r"^<!-- part: ([A-Z][A-Z0-9_]*) -->$", re.M)
PLACEHOLDER_RE = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_parts(path):
    """parts.html in {NAME: text} zerlegen. Alles vor dem ersten Marker ist
    Kommentar und faellt weg."""
    raw = read(path)
    marks = list(PART_RE.finditer(raw))
    if not marks:
        sys.exit(f"FEHLER: keine Bausteine in {path}")
    parts = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(raw)
        parts[m.group(1)] = raw[m.end():end].strip("\n")
    return parts


def load_brand(brand_id):
    d = os.path.join(BRANDS, brand_id)
    cfg = json.loads(read(os.path.join(d, "brand.json")))
    vars_ = dict(cfg.get("vars", {}))
    vars_["TOKENS"] = strip_leading_comment(read(os.path.join(d, "tokens.css")))
    vars_["BRAND_CSS"] = strip_leading_comment(read(os.path.join(d, "brand.css")))
    vars_.update(load_parts(os.path.join(d, "parts.html")))
    vars_["ROOT"] = cfg.get("root", "")
    cfg["vars"] = vars_
    cfg["dir"] = d
    return cfg


def strip_leading_comment(css):
    """Der erklaerende Kopfkommentar der Marken-CSS gehoert ins Repo, nicht in
    die ausgelieferte Seite."""
    css = css.strip("\n")
    if css.startswith("/*"):
        end = css.find("*/")
        if end != -1:
            css = css[end + 2:].lstrip("\n")
    return css.rstrip("\n")


def render(page, template, brand):
    vars_ = dict(brand["vars"])
    titles = brand.get("titles", {})
    if page not in titles:
        sys.exit(f"FEHLER: brands/{brand['id']}/brand.json kennt keinen Titel fuer {page}")
    vars_["TITLE"] = titles[page]

    def repl(m):
        key = m.group(1)
        if key not in vars_:
            sys.exit(f"FEHLER: {page}, Marke {brand['id']}: kein Wert fuer {{{{{key}}}}}")
        return vars_[key]

    # Mehrfach, damit ein Markenwert selbst einen Platzhalter enthalten darf,
    # etwa {{ROOT}} in einem Bildpfad. Die Schranke faengt einen Ringschluss ab.
    out = template
    for _ in range(5):
        new = PLACEHOLDER_RE.sub(repl, out)
        if new == out:
            break
        out = new
    left = PLACEHOLDER_RE.search(out)
    if left:
        sys.exit(f"FEHLER: {page}, Marke {brand['id']}: Platzhalter blieb stehen, "
                 f"{left.group(0)}. Verweist ein Markenwert im Kreis auf sich selbst?")

    # Banner direkt nach dem Doctype
    banner = BANNER.format(page=page, brand=brand["id"])
    out = out.replace("<!DOCTYPE html>\n", f"<!DOCTYPE html>\n{banner}\n", 1)

    # Leergeraeumte Bausteine hinterlassen leere Zeilen. Drei und mehr auf eins.
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nur melden, nichts schreiben")
    ap.add_argument("--brand", action="append", help="nur diese Marke bauen, mehrfach moeglich")
    args = ap.parse_args()

    if not os.path.isdir(SRC):
        sys.exit(f"FEHLER: {SRC} fehlt")
    pages = sorted(f for f in os.listdir(SRC) if f.endswith(".html"))
    if not pages:
        sys.exit(f"FEHLER: keine Seiten in {SRC}")

    brand_ids = args.brand or sorted(
        d for d in os.listdir(BRANDS) if os.path.isdir(os.path.join(BRANDS, d)))

    drift, written = [], []
    for brand_id in brand_ids:
        brand = load_brand(brand_id)
        outdir = os.path.normpath(os.path.join(HERE, brand.get("out", ".")))
        if not args.check:
            os.makedirs(outdir, exist_ok=True)

        for page in pages:
            new = render(page, read(os.path.join(SRC, page)), brand)
            target = os.path.join(outdir, page)
            old = read(target) if os.path.isfile(target) else None
            rel = os.path.relpath(target, HERE)
            if old == new:
                continue
            if args.check:
                drift.append(f"{rel}: nicht auf dem Stand von src/{page}")
            else:
                with open(target, "w", encoding="utf-8") as f:
                    f.write(new)
                written.append(rel)

        # Markeneigene Dateien neben die Seiten legen
        assets = os.path.join(brand["dir"], "assets")
        if os.path.isdir(assets):
            for name in sorted(os.listdir(assets)):
                if name.startswith("."):
                    continue
                s, t = os.path.join(assets, name), os.path.join(outdir, name)
                rel = os.path.relpath(t, HERE)
                same = (os.path.isfile(t)
                        and open(s, "rb").read() == open(t, "rb").read())
                if same:
                    continue
                if args.check:
                    drift.append(f"{rel}: weicht von brands/{brand_id}/assets ab")
                else:
                    shutil.copy2(s, t)
                    written.append(rel)

        print(f"{brand_id}: {len(pages)} Seiten nach {brand.get('out', '.')}/")

    if args.check:
        if drift:
            print("\nAbweichungen:")
            for d in drift:
                print(f"  {d}")
            return 1
        print("Alle Markenausgaben aktuell.")
        return 0
    for w in written:
        print(f"  geschrieben: {w}")
    if not written:
        print("  nichts zu tun, alle Ausgaben waren aktuell")
    return 0


if __name__ == "__main__":
    sys.exit(main())
