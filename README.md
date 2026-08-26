# PDT Method Explorer

Interactive dashboard for the Product Design Toolkit – 85 methods across 5 spaces, auto-built from Markdown files.

**Live:** https://productdesigntoolkit.github.io/explorer/

## How it works

- Method content lives in `*/space/*.md` files with YAML frontmatter
- `build.py` reads all files and generates `data.js`
- `index.html` renders the dashboard from `data.js`
- GitHub Actions rebuilds on every push to `main`

## Local development

```bash
python3 build.py   # regenerate data.js
open index.html    # preview in browser
```

## Method pipeline

All scripts live here. The full flow is documented in `gitbook-methods/ADDING-A-METHOD.md`.

```bash
python3 new-method.py <id> --space <space> --title "..." --group "..." --oneliner "..."
# write the content: YAML, method text, skill

./sync-methods.sh                       # navigation, mirror, build, lists, counters, check
python3 sync-changelog.py --new <id>    # changelog entry
python3 audit-method.py <id> --online --pre-publish
# ► checkpoint: read the report in reports/, then approve
./publish-method.sh <id>                # commit and push every touched repo
```

Dry runs: `./sync-methods.sh --check`, `./publish-method.sh <id> --dry-run`.
Single steps: `sync-summary.py`, `sync-commands.py`, `sync-counts.py`, `build.py`, `check-methods.py`.

## Data source

Method files are synced from [`productdesigntoolkit/gitbook-methods`](https://github.com/productdesigntoolkit/gitbook-methods).
