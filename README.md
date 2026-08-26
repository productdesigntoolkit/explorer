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

## Consistency check

```bash
python3 check-methods.py   # checks all four PDT repos, exit 1 on findings
```

Verifies that every method exists on all levels: YAML skeleton, method text, SUMMARY,
explorer copy, skill, skill mapping, data.js, the space command lists and all counters.
Checklist for adding a method: `gitbook-methods/ADDING-A-METHOD.md`.

## Data source

Method files are synced from [`productdesigntoolkit/gitbook-methods`](https://github.com/productdesigntoolkit/gitbook-methods).
