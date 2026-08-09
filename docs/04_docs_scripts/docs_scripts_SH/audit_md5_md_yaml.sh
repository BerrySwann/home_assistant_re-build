#!/usr/bin/env bash
# ╭──────────────────────────────────────────────────────────────────────────╮
# │ AUDIT MD5 DOCS — TRIANGULATION LOCAL → PROD → GITHUB                      │
# ╰──────────────────────────────────────────────────────────────────────────╯
# Compare TOUS les fichiers docs/ (.md + .yaml + .sh) entre :
#   LOCAL (ReBuild, source de vérité) · PROD (H:) · GITHUB (curl raw URL)
# Statuts : ✅ SYNC · ⚠️ CRLF (même contenu, fins de ligne) · ❌ DIFF · 🚫 ABSENT
# Log : <ReBuild>/historique/md5_audit_md_yaml_YYYY-MM-DD.txt
#       + copie md5_audit_md_yaml_latest.txt (compatibilité carte dashboard)
#
# ## 📝 DESCRIPTION :
# Périmètre complet : tout le dossier docs/ sans exclusion (.md + .yaml + .sh).
# LOCAL = source de vérité absolue (cascade : local → H:\Docs → GitHub, cf. CLAUDE.md).
# Ce script s'exécute LOCALEMENT (git-bash Windows), pas sur HA.
#
# ## 🧮 CALCUL & SOURCES :
# - LOCAL  : $LOCAL_ROOT/docs/**/*.{md,yaml,sh}
# - PROD   : $PROD_ROOT/docs/**/*.{md,yaml,sh}
# - GITHUB : curl raw https://raw.githubusercontent.com/.../main/docs/<relpath>
# - MD5 brut (octets exacts) + MD5 normalisé (CRLF->LF) pour la classification
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
#
# ## 🖥️ TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
# - L5C3 Système — carte "Journal Audit MD5 Docs" (même log md5_audit_md_yaml_*)

set -euo pipefail

# ── CONFIG ────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_ROOT="${LOCAL_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"   # ReBuild/
PROD_ROOT="${PROD_ROOT:-/h}"                                       # montage H:
GH_BASE="${GH_BASE:-https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main}"
LOG_DIR="${LOG_DIR:-$LOCAL_ROOT/historique}"

# Chemin Windows explicite pour curl (sinon write error sur /tmp MSYS)
TMP_DIR="$(cygpath -m "$LOCALAPPDATA/Temp" 2>/dev/null || echo "$LOCAL_ROOT")"
TMP_TREE="$TMP_DIR/audit_md_tree_$$.txt"
TMP_PROD="$TMP_DIR/audit_md_prod_$$.txt"
TMP_LOCAL="$TMP_DIR/audit_md_local_$$.txt"
TMP_GH="$TMP_DIR/audit_md_gh_$$.tmp"

mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/md5_audit_md_yaml_$(date '+%Y-%m-%d').txt"

# ── PASS 1 : TREE (référentiel = local, source de vérité DOCS) ────────────
{
echo "╭──────────────────────────────────────────────────────────────────────────────╮"
echo "│ AUDIT MD5 DOCS (triangulation) — $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "╰──────────────────────────────────────────────────────────────────────────────╯"
echo ""
echo "── PASS 1 : TREE (local ReBuild = SOURCE DE VÉRITÉ) ──────────────────────────"
} > "$LOG"

find "$LOCAL_ROOT/docs" \( -name "*.md" -o -name "*.yaml" -o -name "*.sh" \) 2>/dev/null \
  | sed "s|^$LOCAL_ROOT/||" | sort > "$TMP_TREE" || true

TOTAL=$(wc -l < "$TMP_TREE")
TOTAL_MD=$(grep -c '\.md$' "$TMP_TREE" 2>/dev/null || echo 0)
TOTAL_YAML=$(grep -c '\.yaml$' "$TMP_TREE" 2>/dev/null || echo 0)
TOTAL_SH=$(grep -c '\.sh$' "$TMP_TREE" 2>/dev/null || echo 0)
while IFS= read -r f; do echo "  $f"; done < "$TMP_TREE" >> "$LOG"
echo "" >> "$LOG"
echo "  → $TOTAL fichiers ($TOTAL_MD .md · $TOTAL_YAML .yaml · $TOTAL_SH .sh)" >> "$LOG"
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
    lf="$LOCAL_ROOT/$rel"
    pf="$PROD_ROOT/$rel"
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

# ── COMPARAISON 3 NIVEAUX ─────────────────────────────────────────────────
echo "── COMPARAISON LOCAL / PROD / GITHUB ────────────────────────────────────────" >> "$LOG"
printf "%-70s | %-8s | %-8s | %-8s | %s\n" "FICHIER" "LOCAL" "PROD" "GITHUB" "STATUT" >> "$LOG"
printf '%.0s─' {1..115} >> "$LOG"; echo "" >> "$LOG"

declare -A PROD_MD5 LOCAL_MD5
while IFS='|' read -r f m; do [ -n "$f" ] && PROD_MD5["$f"]="$m"; done < "$TMP_PROD"
while IFS='|' read -r f m; do [ -n "$f" ] && LOCAL_MD5["$f"]="$m"; done < "$TMP_LOCAL"

OK=0; CRLF_COUNT=0; DIFF_COUNT=0; ABSENT_COUNT=0

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

    # Classification (LOCAL = source de vérité)
    present=0; raw_same=1; norm_same=1; first_raw=""; first_norm=""
    for v in "$loca" "$prod" "$gh"; do
        [ "$v" != "- -" ] || continue
        present=$((present+1))
        r="${v%% *}"; n="${v##* }"
        [ -n "$first_raw" ]   || first_raw="$r"
        [ -n "$first_norm" ]  || first_norm="$n"
        [ "$r" = "$first_raw" ]  || raw_same=0
        [ "$n" = "$first_norm" ] || norm_same=0
    done

    if [ "$present" -lt 3 ]; then
        statut="🚫 ABSENT"
        ABSENT_COUNT=$((ABSENT_COUNT+1))
    elif [ "$raw_same" -eq 1 ]; then
        statut="✅ SYNC"
        OK=$((OK+1))
    elif [ "$norm_same" -eq 1 ]; then
        statut="⚠️ CRLF"
        CRLF_COUNT=$((CRLF_COUNT+1))
    else
        statut="❌ DIFF"
        DIFF_COUNT=$((DIFF_COUNT+1))
    fi

    l1="${loca%% *}"; p1="${prod%% *}"; g1="${gh%% *}"
    [ "$l1" = "-" ] && l1="????"
    [ "$p1" = "-" ] && p1="????"
    [ "$g1" = "-" ] && g1="????"
    printf "%-70s | %.8s | %.8s | %.8s | %s\n" "$rel" "$l1" "$p1" "$g1" "$statut" >> "$LOG"
done < "$TMP_TREE"

# ── RÉSUMÉ ────────────────────────────────────────────────────────────────
{
echo ""
printf '%.0s─' {1..115}; echo ""
echo "RÉSULTAT : $TOTAL fichiers ($TOTAL_MD .md · $TOTAL_YAML .yaml · $TOTAL_SH .sh) — ✅ $OK SYNC · ⚠️ $CRLF_COUNT CRLF · ❌ $DIFF_COUNT DIFF · 🚫 $ABSENT_COUNT ABSENT"
echo "Source de vérité : LOCAL (ReBuild). Écart local→prod = prod EN RETARD."
printf '%.0s─' {1..115}; echo ""
} >> "$LOG"

rm -f "$TMP_TREE" "$TMP_PROD" "$TMP_LOCAL" "$TMP_GH"

# Copie latest (compatibilité carte dashboard L5C3)
cp "$LOG" "$LOG_DIR/md5_audit_md_yaml_latest.txt" 2>/dev/null || true

echo "$(date '+%Y-%m-%d %H:%M:%S %Z') ✅ Audit MD5 docs terminé : $TOTAL fichiers ($TOTAL_MD .md · $TOTAL_YAML .yaml · $TOTAL_SH .sh) · $OK SYNC · $CRLF_COUNT CRLF · $DIFF_COUNT DIFF · $ABSENT_COUNT ABSENT → $LOG"

# annotations_log:
# [2026-08-08] Version enrichie (même nom que le script HA de Claude) :
#              ajout du maillon LOCAL→PROD — triangulation 3 niveaux.
#              Le local ReBuild est la SOURCE DE VÉRITÉ des docs .md.
#              S'exécute sur Windows (git-bash), pas sur HA.
#              Garde le nom + le log md5_audit_md_yaml_* (compatibilité carte L5C3).
# [2026-08-09] Extension périmètre : tout docs/ sans exclusion (.md + .yaml + .sh)
#              PASS 1 : find unique sur docs/ avec 3 extensions. Suppression case README/INDEX_GLOBAL.
#              Résumé distingue les 3 types (TOTAL_MD / TOTAL_YAML / TOTAL_SH).
