# PDT Method Explorer

Interactive dashboard for the Product Design Toolkit – 85 methods across 5 spaces, auto-built from Markdown files.

**Live:** https://productdesigntoolkit.github.io/explorer/
**HWZ edition:** https://productdesigntoolkit.github.io/explorer/hwz/

## How it works

- Method content lives in `*/space/*.md` files with YAML frontmatter
- `build.py` reads all files and generates `data.js`
- `src/*.html` holds the single source of every page, with `{{PLACEHOLDER}}` slots
- `build-brands.py` renders `src/` once per brand in `brands/`
- GitHub Actions rebuilds on every push to `main`

## Two brands, one source

The pages in the repo root and in `hwz/` are **generated**. Edit `src/`, never
the output. A change made once reaches both editions.

```
src/index.html  +  brands/pdt/  ->  ./index.html          (Product Design Toolkit)
                +  brands/hwz/  ->  ./hwz/index.html      (HWZ corporate design)
```

A brand is four files plus its own assets:

| File | Fills |
|------|-------|
| `brands/<id>/brand.json` | output folder, path prefix, page titles, short strings |
| `brands/<id>/tokens.css` | `{{TOKENS}}`, the `:root` block with every colour |
| `brands/<id>/brand.css` | `{{BRAND_CSS}}`, extra rules appended to each page |
| `brands/<id>/parts.html` | multi-line HTML and JS blocks, one per `<!-- part: NAME -->` |
| `brands/<id>/assets/` | files copied next to the rendered pages (logo, favicon) |

The HWZ edition drops the dark mode, because the HWZ corporate design has a
single light palette. That is a brand decision, not a code path: `THEME_INIT`,
`THEME_SWITCH` and `THEME_JS` are simply empty in `brands/hwz/parts.html`.

## Local development

```bash
python3 build.py            # regenerate data.js
python3 build-brands.py     # render both brand editions from src/
python3 build-brands.py --check   # report drift, write nothing
open index.html             # preview in browser
```

## Method pipeline

All scripts live here. The full flow is documented in `gitbook-methods/ADDING-A-METHOD.md`.

```bash
python3 new-method.py <id> --space <space> --title "..." --group "..." --oneliner "..."
# write the content: YAML, method text, skill

./sync-methods.sh                       # navigation, mirror, build, lists, counters, brands, check
python3 sync-changelog.py --new <id>    # changelog entry
python3 audit-method.py <id> --online --pre-publish
# ► checkpoint: read the report in reports/, then approve
./publish-method.sh <id>                # commit and push every touched repo
```

Dry runs: `./sync-methods.sh --check`, `./publish-method.sh <id> --dry-run`.
Single steps: `sync-summary.py`, `sync-commands.py`, `sync-counts.py`, `build.py`, `build-brands.py`, `check-methods.py`.

## Data source

Method files are synced from [`productdesigntoolkit/gitbook-methods`](https://github.com/productdesigntoolkit/gitbook-methods).
