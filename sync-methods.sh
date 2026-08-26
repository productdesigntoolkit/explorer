#!/usr/bin/env bash
# Spiegelt Methodentexte und Skills aus den Quell-Repos in den Explorer,
# baut data.js, schreibt alle Zaehler und prueft die Kette.
#
#   ./sync-methods.sh          spiegeln, bauen, pruefen
#   ./sync-methods.sh --check  nichts schreiben, nur melden was abweicht
#
# Bewusst lokal und nicht als GitHub Action: gitbook-methods ist privat,
# explorer ist oeffentlich. Ein Token dafuer im oeffentlichen Repo waere
# ein zu hoher Preis fuer einen gesparten Handgriff.

set -euo pipefail

EXPLORER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$EXPLORER")"
GITBOOK="$ROOT/gitbook-methods"
SKILLS="$ROOT/pdt-skills"
SPACES=(strategy-space problem-space solution-space product-space market-space)

CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

for d in "$GITBOOK" "$SKILLS"; do
  [[ -d "$d" ]] || { echo "fehlt: $d" >&2; exit 1; }
done

if [[ $CHECK -eq 1 ]]; then
  echo "Trockenlauf, es wird nichts geschrieben."
  drift=0
  for space in "${SPACES[@]}"; do
    if ! diff -rq "$GITBOOK/$space" "$EXPLORER/$space" >/dev/null 2>&1; then
      echo "  abweichend: $space"
      diff -rq "$GITBOOK/$space" "$EXPLORER/$space" 2>&1 | sed 's/^/    /'
      drift=1
    fi
  done
  if ! diff -rq --exclude=README.md --exclude='.*' "$SKILLS" "$EXPLORER/skills" >/dev/null 2>&1; then
    echo "  abweichend: skills"
    diff -rq --exclude=README.md --exclude='.*' "$SKILLS" "$EXPLORER/skills" 2>&1 | sed 's/^/    /'
    drift=1
  fi
  [[ $drift -eq 0 ]] && echo "  Spiegel aktuell."
  python3 "$EXPLORER/sync-summary.py" --root "$ROOT" --check || drift=1
  python3 "$EXPLORER/sync-commands.py" --root "$ROOT" --check || drift=1
  python3 "$EXPLORER/sync-counts.py" --check || drift=1
  python3 "$EXPLORER/check-methods.py" || drift=1
  exit $drift
fi

echo "SUMMARY"
python3 "$EXPLORER/sync-summary.py" --root "$ROOT" | head -1

echo
echo "Spiegeln"
for space in "${SPACES[@]}"; do
  mkdir -p "$EXPLORER/$space"
  # Loeschen, was in der Quelle nicht mehr existiert
  for f in "$EXPLORER/$space"/*.md; do
    [[ -e "$f" ]] || continue
    base="$(basename "$f")"
    [[ -e "$GITBOOK/$space/$base" ]] || { rm "$f"; echo "  entfernt: $space/$base"; }
  done
  cp "$GITBOOK/$space"/*.md "$EXPLORER/$space/"
  n=$(ls "$GITBOOK/$space"/*.md | grep -v '/README.md$' | wc -l | tr -d ' ')
  echo "  $space: $n Methoden"
done

mkdir -p "$EXPLORER/skills"
for f in "$EXPLORER/skills"/*.md; do
  [[ -e "$f" ]] || continue
  base="$(basename "$f")"
  [[ "$base" == "README.md" ]] && continue
  [[ -e "$SKILLS/$base" ]] || { rm "$f"; echo "  entfernt: skills/$base"; }
done
for f in "$SKILLS"/*.md; do
  [[ "$(basename "$f")" == "README.md" ]] && continue
  cp "$f" "$EXPLORER/skills/"
done
echo "  skills: $(ls "$SKILLS"/*.md | grep -v '/README.md$' | wc -l | tr -d ' ') Skills"

echo
echo "Bauen"
python3 "$EXPLORER/build.py" | tail -1

echo
echo "Template-Listen"
python3 "$EXPLORER/sync-commands.py" --root "$ROOT"

echo
echo "Zaehler"
python3 "$EXPLORER/sync-counts.py" | tail -n +2

echo
echo "Pruefen"
python3 "$EXPLORER/check-methods.py"
