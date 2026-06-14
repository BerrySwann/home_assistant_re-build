#!/usr/bin/env bash
# ╭──────────────────────────────────────────────────────────────────────────╮
# │ AUDIT MD5 — 3 PASSES : TREE → MD5 PROD → MD5 GITHUB → RAPPORT          │
# ╰──────────────────────────────────────────────────────────────────────────╯
# Compare chaque fichier YAML entre la prod HA et GitHub (origin/main)
# Statuts : ✅ SYNC · ❌ DIFF · ⚠️ PUSH MANQUANT
# Log : /config/.logs/md5_audit_YYYY-MM-DD.txt

set -euo pipefail

LOG_DIR="/config/.logs"
LOG="$LOG_DIR/md5_audit_$(date '+%Y-%m-%d').txt"
TMP_TREE="/tmp/audit_tree_$$.txt"
TMP_PROD="/tmp/audit_prod_$$.txt"
mkdir -p "$LOG_DIR"

cd /config

DIRS="sensors templates utility_meter command_line"
EXTRA_FILES="automations.yaml"

# ── PASS 1 : TREE ─────────────────────────────────────────────────────────
{
echo "╭──────────────────────────────────────────────────────────────────────────────╮"
echo "│ AUDIT MD5 — $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "╰──────────────────────────────────────────────────────────────────────────────╯"
echo ""
echo "── PASS 1 : TREE LOCAL ──────────────────────────────────────────────────────"
} > "$LOG"

find $DIRS -name "*.yaml" 2>/dev/null | sort > "$TMP_TREE"

# Ajouter les fichiers extra s'ils existent
for f in $EXTRA_FILES; do
    [ -f "$f" ] && echo "$f" >> "$TMP_TREE"
done

TOTAL=$(wc -l < "$TMP_TREE")
cat "$TMP_TREE" | while read -r f; do echo "  $f"; done >> "$LOG"
echo "" >> "$LOG"
echo "  → $TOTAL fichiers" >> "$LOG"
echo "" >> "$LOG"

# ── PASS 2 : MD5 PROD ─────────────────────────────────────────────────────
echo "── PASS 2 : MD5 PROD ───────────────────────────────────────────────────────" >> "$LOG"
> "$TMP_PROD"
while IFS= read -r file; do
    md5=$(md5sum "$file" 2>/dev/null | cut -d' ' -f1)
    echo "$file|$md5" >> "$TMP_PROD"
done < "$TMP_TREE"
echo "  → $TOTAL MD5 calculés" >> "$LOG"
echo "" >> "$LOG"

# ── PASS 3 : MD5 GITHUB + COMPARAISON ────────────────────────────────────
echo "── PASS 3 : MD5 GITHUB (git fetch) ─────────────────────────────────────────" >> "$LOG"
git fetch origin >/dev/null 2>&1
echo "  → fetch OK" >> "$LOG"
echo "" >> "$LOG"

echo "── COMPARAISON PROD vs GITHUB ───────────────────────────────────────────────" >> "$LOG"
printf "%-68s | %-8s | %-8s | %s\n" "FICHIER" "PROD" "GITHUB" "STATUT" >> "$LOG"
printf '%.0s─' {1..105} >> "$LOG"; echo "" >> "$LOG"

OK=0; DIFF_COUNT=0; PUSH_MANQUANT=0

while IFS='|' read -r file prod_md5; do
    github_raw=$(git show "origin/main:${file}" 2>/dev/null)
    if [[ -z "$github_raw" ]]; then
        github_md5=""
        statut="⚠️  PUSH MANQUANT"
        PUSH_MANQUANT=$((PUSH_MANQUANT+1))
    else
        github_md5=$(echo "$github_raw" | md5sum | cut -d' ' -f1)
        if [[ "$prod_md5" == "$github_md5" ]]; then
            statut="✅ SYNC"
            OK=$((OK+1))
        else
            statut="❌ DIFF"
            DIFF_COUNT=$((DIFF_COUNT+1))
        fi
    fi

    printf "%-68s | %.8s | %.8s | %s\n" \
        "$file" \
        "${prod_md5:-??????}" \
        "${github_md5:-??????}" \
        "$statut" >> "$LOG"
done < "$TMP_PROD"

# ── RÉSUMÉ ────────────────────────────────────────────────────────────────
{
echo ""
printf '%.0s─' {1..105}; echo ""
echo "RÉSULTAT : $TOTAL fichiers — ✅ $OK SYNC · ❌ $DIFF_COUNT DIFF · ⚠️ $PUSH_MANQUANT PUSH MANQUANT"
printf '%.0s─' {1..105}; echo ""
} >> "$LOG"

# Nettoyage /tmp
rm -f "$TMP_TREE" "$TMP_PROD"

# Résumé vers stdout pour le log shell_command
echo "$(date '+%Y-%m-%d %H:%M:%S %Z') ✅ Audit MD5 terminé : $TOTAL fichiers · $OK SYNC · $DIFF_COUNT DIFF · $PUSH_MANQUANT PUSH MANQUANT → $LOG"
# [2026-06-14] FIX : git fetch origin main → git fetch origin
# (git fetch origin main ne met pas à jour refs/remotes/origin/main → git show stale)
