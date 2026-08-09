#!/usr/bin/env bash
# ╭──────────────────────────────────────────────────────────────────────────╮
# │ HERMES AUDIT MD5 — TRIANGULATION LOCAL <-> PROD <-> REPO (docs .md)      │
# ╰──────────────────────────────────────────────────────────────────────────╯
# Compare chaque fichier .md entre les 3 niveaux :
#   LOCAL (ReBuild, source de vérité) · PROD (H:) · GITHUB (curl raw URL)
#
# ## 📝 DESCRIPTION :
# Script complémentaire de audit_md5_md.sh (prod, qui vérifie prod<->repo).
# Ici : triangulation COMPLÈTE local<->prod<->repo, exécutée sur le PC
# Windows (git-bash) — nécessaire car le maillon LOCAL n'est visible que
# depuis le PC (quand il est allumé).
#
# ## 🧮 CALCUL & SOURCES :
# - LOCAL  : $LOCAL_ROOT/docs/**/*.md + Github/README.md + Github/INDEX_GLOBAL.md
# - PROD   : $PROD_ROOT/docs/**/*.md + README.md + INDEX_GLOBAL.md
# - GITHUB : curl raw https://raw.githubusercontent.com/.../main/docs/<relpath>
# - MD5 brut (octets exacts) + MD5 normalisé (CRLF->LF)
# - README/INDEX_GLOBAL : mapping local Github/ -> racine prod & repo
#
# ## 📊 FORMAT LISIBLE (1er coup d'œil) :
#   FICHIER | L↔P | P↔R | L↔R | DÉTAIL
#   ✅/❌ par paire : L↔P ❌ = prod EN RETARD (source de vérité = local)
#                     P↔R ❌ = repo EN RETARD
#                     L↔R ❌ = local et repo divergent
#   Résumé final : compteurs par paire (L↔P / P↔R / L↔R)
#
# ## ⚠️ IMPORTANT (PIÈGES) :
# - curl Windows n'écrit PAS dans /tmp (chemin MSYS) → chemin Windows explicite
#   via cygpath -m "$LOCALAPPDATA/Temp" pour le fichier tmp.
# - Fichiers locaux en CRLF (Windows) : le MD5 normalisé tranche entre
#   ⚠️ CRLF (sans action) et ❌ DIFF (action réelle).
# - SOURCE DE VÉRITÉ = LOCAL : un écart local→prod signifie que la prod est
#   EN RETARD (à synchroniser depuis le local), pas l'inverse.
# - Chemins à espaces/accents : encodage URL via python urllib.
# - set -euo pipefail : les find utilisent || true (répertoire absent OK).
# - Ne PAS toucher aux archives (historique/JOURNAL*, CLAUDE_backup*).
#
# ## 🖥️ TABLEAU DE BORD :
# - Carte "Audit MD5 Docs" (L5C3 Système) — lue via sensor command_line HA
#   (version prod) ; ce script PC produit son propre rapport pour analyse.

set -euo pipefail

# ── CONFIG ────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_ROOT="${LOCAL_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"   # ReBuild/
PROD_ROOT="${PROD_ROOT:-/h}"                                       # montage H:
GH_BASE="${GH_BASE:-https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main}"
LOG_DIR="${LOG_DIR:-$LOCAL_ROOT/historique}"

# Chemin Windows explicite pour curl (sinon write error sur /tmp MSYS)
TMP_DIR="$(cygpath -m "$LOCALAPPDATA/Temp" 2>/dev/null || echo "$LOCAL_ROOT")"
TMP_TREE="$TMP_DIR/hermes_md_tree_$$.txt"
TMP_PROD="$TMP_DIR/hermes_md_prod_$$.txt"
TMP_LOCAL="$TMP_DIR/hermes_md_local_$$.txt"
TMP_GH="$TMP_DIR/hermes_md_gh_$$.tmp"

mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/hermes_md5_audit_md_$(date '+%Y-%m-%d').txt"

# ── PASS 1 : TREE (référentiel = local, source de vérité DOCS) ────────────
{
echo "╭──────────────────────────────────────────────────────────────────────────────╮"
echo "│ HERMES AUDIT MD5 (triangulation) — $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "╰──────────────────────────────────────────────────────────────────────────────╯"
echo ""
echo "── PASS 1 : TREE (local ReBuild = SOURCE DE VÉRITÉ) ──────────────────────────"
} > "$LOG"

find "$LOCAL_ROOT/docs" -name "*.md" 2>/dev/null | sed "s|^$LOCAL_ROOT/||" | sort > "$TMP_TREE" || true
# Fichiers racine : mapping local Github/ -> chemin repo
[ -f "$LOCAL_ROOT/Github/README.md" ]      && echo "README.md" >> "$TMP_TREE"
[ -f "$LOCAL_ROOT/Github/INDEX_GLOBAL.md" ] && echo "INDEX_GLOBAL.md" >> "$TMP_TREE"

TOTAL=$(wc -l < "$TMP_TREE")
while IFS= read -r f; do echo "  $f"; done < "$TMP_TREE" >> "$LOG"
echo "" >> "$LOG"
echo "  → $TOTAL fichiers .md" >> "$LOG"
echo "" >> "$LOG"

# ── PASS 2 : MD5 LOCAL + MD5 PROD (brut + normalisé) ─────────────────────
echo "── PASS 2 : MD5 LOCAL + PROD ─────────────────────────────────────────────────" >> "$LOG"

md5_both() {  # $1=fichier -> "brut normalise"
    local raw norm
    raw=$(md5sum "$1" 2>/dev/null | cut -d' ' -f1)
    norm=$(tr -d '\r' < "$1" | md5sum | cut -d' ' -f1)
    echo "$raw $norm"
}

while IFS= read -r rel; do
    case "$rel" in
        README.md|INDEX_GLOBAL.md)
            lf="$LOCAL_ROOT/Github/$rel"
            pf="$PROD_ROOT/$rel"
            ;;
        *)
            lf="$LOCAL_ROOT/$rel"
            pf="$PROD_ROOT/$rel"
            ;;
    esac
    if [ -f "$lf" ]; then
        echo "$rel|$(md5_both "$lf")" >> "$TMP_LOCAL"
    else
        echo "$rel|- -" >> "$TMP_LOCAL"
    fi
    if [ -f "$pf" ]; then
        echo "$rel|$(md5_both "$pf")" >> "$TMP_PROD"
    else
        echo "$rel|- -" >> "$TMP_PROD"
    fi
done < "$TMP_TREE"
echo "  → $TOTAL MD5 locaux + $TOTAL MD5 prod calculés" >> "$LOG"
echo "" >> "$LOG"

# ── PASS 3 : MD5 GITHUB (curl raw → md5sum direct) ───────────────────────
echo "── PASS 3 : MD5 GITHUB (curl raw → md5sum direct) ────────────────────────────" >> "$LOG"
echo "  → base : $GH_BASE" >> "$LOG"
echo "" >> "$LOG"

urlencode() {  # encodage URL (espaces, accents) via python
    python -c 'import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1], safe="/"))' "$1"
}

# ── COMPARAISON PAR PAIRES (L↔P / P↔R / L↔R) ──────────────────────────────
echo "── COMPARAISON PAR PAIRES (1er coup d'œil) ──────────────────────────────────" >> "$LOG"
printf "%-70s | %-4s | %-4s | %-4s | %s\n" "FICHIER" "L↔P" "P↔R" "L↔R" "DÉTAIL" >> "$LOG"
printf '%.0s─' {1..115} >> "$LOG"; echo "" >> "$LOG"

declare -A PROD_MD5 LOCAL_MD5
while IFS='|' read -r f m; do [ -n "$f" ] && PROD_MD5["$f"]="$m"; done < "$TMP_PROD"
while IFS='|' read -r f m; do [ -n "$f" ] && LOCAL_MD5["$f"]="$m"; done < "$TMP_LOCAL"

OK=0; CRLF_COUNT=0; DIFF_COUNT=0; ABSENT_COUNT=0
LP_OK=0; LP_DIFF=0; PR_OK=0; PR_DIFF=0; LR_OK=0; LR_DIFF=0

while IFS= read -r rel; do
    loca="${LOCAL_MD5[$rel]:-- -}"
    prod="${PROD_MD5[$rel]:-- -}"

    # GITHUB
    rm -f "$TMP_GH"
    enc=$(urlencode "$rel")
    HTTP_CODE=$(curl -sf --max-time 20 -o "$TMP_GH" -w '%{http_code}' "${GH_BASE}/${enc}" 2>/dev/null || echo "000")
    if [[ "$HTTP_CODE" == "200" ]] && [[ -s "$TMP_GH" ]]; then
        gh="$(md5sum "$TMP_GH" | cut -d' ' -f1) $(tr -d '\r' < "$TMP_GH" | md5sum | cut -d' ' -f1)"
    else
        gh="- -"
    fi

    # Extraction brut/normalisé
    lr="${loca%% *}"; ln="${loca##* }"
    pr="${prod%% *}"; pn="${prod##* }"
    gr="${gh%% *}";   gn="${gh##* }"

    # Comparaison par paire (normalisée : CRLF toléré)
    lp="✅"; prs="✅"; lrs="✅"
    if [ "$lr" = "-" ] || [ "$pr" = "-" ]; then lp="🚫"
    elif [ "$lr" != "$pr" ] && [ "$ln" = "$pn" ]; then lp="⚠️"
    elif [ "$lr" != "$pr" ]; then lp="❌"; LP_DIFF=$((LP_DIFF+1)); else LP_OK=$((LP_OK+1)); fi
    if [ "$pr" = "-" ] || [ "$gr" = "-" ]; then prs="🚫"
    elif [ "$pr" != "$gr" ] && [ "$pn" = "$gn" ]; then prs="⚠️"
    elif [ "$pr" != "$gr" ]; then prs="❌"; PR_DIFF=$((PR_DIFF+1)); else PR_OK=$((PR_OK+1)); fi
    if [ "$lr" = "-" ] || [ "$gr" = "-" ]; then lrs="🚫"
    elif [ "$lr" != "$gr" ] && [ "$ln" = "$gn" ]; then lrs="⚠️"
    elif [ "$lr" != "$gr" ]; then lrs="❌"; LR_DIFF=$((LR_DIFF+1)); else LR_OK=$((LR_OK+1)); fi

    # Statut global
    if [ "$lr" = "-" ] || [ "$pr" = "-" ] || [ "$gr" = "-" ]; then
        statut="🚫 ABSENT"
        ABSENT_COUNT=$((ABSENT_COUNT+1))
    elif [ "$lr" = "$pr" ] && [ "$pr" = "$gr" ]; then
        statut="✅ SYNC"
        OK=$((OK+1))
    elif [ "$ln" = "$pn" ] && [ "$pn" = "$gn" ]; then
        statut="⚠️ CRLF"
        CRLF_COUNT=$((CRLF_COUNT+1))
    else
        statut="❌ DIFF"
        DIFF_COUNT=$((DIFF_COUNT+1))
    fi

    # Détail : ne montrer les md5 que si écart
    detail=""
    if [ "$statut" != "✅ SYNC" ] && [ "$statut" != "⚠️ CRLF" ]; then
        d1="${lr:0:8}"; d2="${pr:0:8}"; d3="${gr:0:8}"
        [ "$d1" = "-" ] && d1="absent"
        [ "$d2" = "-" ] && d2="absent"
        [ "$d3" = "-" ] && d3="absent"
        detail="L=$d1 P=$d2 R=$d3"
    fi
    printf "%-70s | %-4s | %-4s | %-4s | %s\n" "$rel" "$lp" "$prs" "$lrs" "$detail" >> "$LOG"
done < "$TMP_TREE"

# ── RÉSUMÉ ────────────────────────────────────────────────────────────────
{
echo ""
printf '%.0s─' {1..115}; echo ""
echo "RÉSULTAT : $TOTAL fichiers — ✅ $OK SYNC · ⚠️ $CRLF_COUNT CRLF · ❌ $DIFF_COUNT DIFF · 🚫 $ABSENT_COUNT ABSENT"
echo "PAR PAIRE : L↔P ✅ $LP_OK / ❌ $LP_DIFF   P↔R ✅ $PR_OK / ❌ $PR_DIFF   L↔R ✅ $LR_OK / ❌ $LR_DIFF"
echo "Source de vérité : LOCAL (ReBuild). Écart L↔P = prod EN RETARD. Écart P↔R = repo EN RETARD."
printf '%.0s─' {1..115}; echo ""
} >> "$LOG"

rm -f "$TMP_TREE" "$TMP_PROD" "$TMP_LOCAL" "$TMP_GH"

# Copie latest
cp "$LOG" "$LOG_DIR/hermes_md5_audit_md_latest.txt" 2>/dev/null || true

echo "$(date '+%Y-%m-%d %H:%M:%S %Z') ✅ HERMES audit MD5 terminé : $TOTAL fichiers · $OK SYNC · $DIFF_COUNT DIFF · $ABSENT_COUNT ABSENT → $LOG"

# annotations_log:
# [2026-08-08] Création — script hermes de triangulation local<->prod<->repo
#              (complémentaire de audit_md5_md.sh sur HA qui vérifie prod<->repo)
#              Format lisible par paires L↔P / P↔R / L↔R. Exécution PC Windows.
