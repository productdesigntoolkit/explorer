#!/usr/bin/env bash
# Veroeffentlicht eine Methode: committet und pusht alle beruehrten Repos.
# Laeuft nach dem Checkpoint, also nachdem der Report gelesen und freigegeben ist.
#
#   ./publish-method.sh product-market-fit
#   ./publish-method.sh product-market-fit --dry-run
#
# Bricht ab, wenn der Trockenlauf der Kette nicht sauber ist.

set -euo pipefail

EXPLORER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$EXPLORER")"
REPOS=(pdt-templates gitbook-methods pdt-skills explorer pdt-claude_plugin)

ID="${1:-}"
[[ -z "$ID" ]] && { echo "Aufruf: ./publish-method.sh {skill-id} [--dry-run]" >&2; exit 2; }
DRY=0
[[ "${2:-}" == "--dry-run" ]] && DRY=1

TITLE="$(cd "$ROOT/gitbook-methods" && grep -rl "^skill: $ID$" ./*-space/*.md 2>/dev/null | head -1 | xargs -I{} grep -m1 '^title:' {} | sed 's/^title: *//;s/"//g' || true)"
[[ -z "$TITLE" ]] && { echo "Methode mit skill '$ID' nicht gefunden" >&2; exit 2; }

echo "Methode: $TITLE  ($ID)"
echo
echo "Trockenlauf der Kette"
if ! "$EXPLORER/sync-methods.sh" --check > /tmp/pdt-publish-check.txt 2>&1; then
  echo "  Kette nicht sauber, Veroeffentlichung abgebrochen:" >&2
  sed 's/^/    /' /tmp/pdt-publish-check.txt >&2
  exit 1
fi
echo "  sauber"
echo

MSG="feat: add $TITLE"
CHANGED=0
for repo in "${REPOS[@]}"; do
  d="$ROOT/$repo"
  [[ -d "$d/.git" ]] || { echo "  $repo: kein Repo, uebersprungen"; continue; }
  if [[ -z "$(git -C "$d" status --porcelain -- . ':(exclude)reports')" ]]; then
    ahead="$(git -C "$d" rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)"
    if [[ "$ahead" != "0" ]]; then
      echo "  $repo: $ahead Commit(s) offen"
      [[ $DRY -eq 0 ]] && git -C "$d" push -q origin HEAD && echo "    gepusht"
      CHANGED=1
    else
      echo "  $repo: nichts zu tun"
    fi
    continue
  fi
  echo "  $repo: committen"
  git -C "$d" status --porcelain -- . ':(exclude)reports' | sed 's/^/      /'
  if [[ $DRY -eq 0 ]]; then
    git -C "$d" add -A -- . ':(exclude)reports'
    git -C "$d" commit -q -m "$MSG

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
    git -C "$d" push -q origin HEAD
    echo "    committet und gepusht"
  fi
  CHANGED=1
done

echo
if [[ $DRY -eq 1 ]]; then
  echo "Trockenlauf, nichts veroeffentlicht."
  exit 0
fi
[[ $CHANGED -eq 0 ]] && { echo "Nichts zu veroeffentlichen."; exit 0; }

echo "Abschliessendes Audit"
python3 "$EXPLORER/audit-method.py" "$ID" --online
