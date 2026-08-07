#!/usr/bin/env bash
# ╭──────────────────────────────────────────────────────────────────────────╮
# │ AUDIT MD5 DOCS — 3 PASSES : TREE → MD5 PROD → MD5 GITHUB → RAPPORT     │
# ╰──────────────────────────────────────────────────────────────────────────╯
# Compare chaque fichier .md entre la prod HA (/config/docs/) et GitHub
# Statuts : ✅ SYNC · ❌ DIFF · ⚠️ ABSENT GITHUB
# Log : /config/.logs/hermes_md5_audit_docs_YYYY-MM-DD.txt

set -euo pipefail

LOG_DIR="/config/.logs"
LOG="$LOG_DIR/hermes_md5_audit_docs_$(date '+%Y-%m-%d').txt"
TMP_TREE="/tmp/audit_docs_tree_$$.txt"
TMP_PROD="/tmp/audit_docs_prod_$$.txt"
TMP_GH="/tmp/audit_docs_gh_$$.tmp"
mkdir -p "$LOG_DIR"

GH_BASE="https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/docs"
DOCS_ROOT="/config/docs"

# ── PASS 1 : TREE ─────────────────────────────────────────────────────────
{
echo "╭──────────────────────────────────────────────────────────────────────────────╮"
echo "│ AUDIT MD5 DOCS — $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "╰──────────────────────────────────────────────────────────────────────────────╯"
echo ""
echo "── PASS 1 : TREE LOCAL (/config/docs/) ─────────────────────────────────────"
} > "$LOG"

find "$DOCS_ROOT" -type f -name "*.md" | sort > "$TMP_TREE" || true

TOTAL=$(wc -l < "$TMP_TREE")
while IFS= read -r f; do
    echo "  ${f#$DOCS_ROOT/}" >> "$LOG"
done < "$TMP_TREE"
echo "" >> "$LOG"
echo "  → $TOTAL fichiers .md" >> "$LOG"
echo "" >> "$LOG"

# ── PASS 2 : MD5 PROD ─────────────────────────────────────────────────────
echo "── PASS 2 : MD5 PROD ───────────────────────────────────────────────────────" >> "$LOG"
> "$TMP_PROD"
while IFS= read -r file; do
    rel="${file#$DOCS_ROOT/}"
    md5=$(md5sum "$file" 2>/dev/null | cut -d' ' -f1)
    echo "$rel|$md5" >> "$TMP_PROD"
done < "$TMP_TREE"
echo "  → $TOTAL MD5 calculés" >> "$LOG"
echo "" >> "$LOG"

# ── PASS 3 : MD5 GITHUB (curl raw → md5sum direct) ────────────────────────
echo "── PASS 3 : MD5 GITHUB (curl raw → md5sum direct) ──────────────────────────" >> "$LOG"
echo "  → base : $GH_BASE" >> "$LOG"
echo "  → URL encoding via python3 urllib.parse.quote" >> "$LOG"
echo "" >> "$LOG"

echo "── COMPARAISON PROD vs GITHUB ───────────────────────────────────────────────" >> "$LOG"
printf "%-70s | %-8s | %-8s | %s\n" "FICHIER" "PROD" "GITHUB" "STATUT" >> "$LOG"
printf '%.0s─' {1..107} >> "$LOG"; echo "" >> "$LOG"

OK=0; DIFF_COUNT=0; ABSENT=0
github_md5=""

while IFS='|' read -r rel prod_md5; do
    rm -f "$TMP_GH"
    encoded=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$rel" 2>/dev/null || echo "$rel")
    HTTP_CODE=$(curl -sf --max-time 15 -o "$TMP_GH" \
        -w '%{http_code}' "${GH_BASE}/${encoded}" 2>/dev/null || echo "000")

    if [[ "$HTTP_CODE" != "200" ]] || [[ ! -s "$TMP_GH" ]]; then
        github_md5=""
        statut="⚠️  ABSENT GITHUB"
        ABSENT=$((ABSENT+1))
    else
        github_md5=$(md5sum "$TMP_GH" | cut -d' ' -f1)
        if [[ "$prod_md5" == "$github_md5" ]]; then
            statut="✅ SYNC"
            OK=$((OK+1))
        else
            statut="❌ DIFF"
            DIFF_COUNT=$((DIFF_COUNT+1))
        fi
    fi

    printf "%-70s | %.8s | %.8s | %s\n" \
        "$rel" "${prod_md5:-??????}" "${github_md5:-??????}" "$statut" >> "$LOG"
done < "$TMP_PROD"

# ── RÉSUMÉ ────────────────────────────────────────────────────────────────
{
echo ""
printf '%.0s─' {1..107}; echo ""
echo "RÉSULTAT : $TOTAL fichiers — ✅ $OK SYNC · ❌ $DIFF_COUNT DIFF · ⚠️ $ABSENT ABSENT GITHUB"
printf '%.0s─' {1..107}; echo ""
} >> "$LOG"

rm -f "$TMP_TREE" "$TMP_PROD" "$TMP_GH"

cp "$LOG" /config/.logs/hermes_md5_audit_docs_latest.txt 2>/dev/null || true

echo "$(date '+%Y-%m-%d %H:%M:%S %Z') ✅ Audit MD5 docs terminé : $TOTAL fichiers · $OK SYNC · $DIFF_COUNT DIFF · $ABSENT ABSENT GITHUB → $LOG"

# annotations_log:
# [2026-08-07] Création — miroir de audit_md5.sh pour les fichiers .md de /config/docs/
#              3 passes : tree → md5 prod → md5 github (curl raw + python3 url-encode)
#              Statuts : SYNC / DIFF / ABSENT GITHUB
#              Log prefix : hermes_md5_audit_docs_ (coexistence avec audit_md5.sh)
