#!/usr/bin/env bash
# ╭──────────────────────────────────────────────────────────────────────────╮
# │ HERMES AUDIT MD5 DOCS — 3 NIVEAUX : PROD H: / LOCAL / GITHUB             │
# ╰──────────────────────────────────────────────────────────────────────────╯
# Compare chaque fichier .md (docs/ + README + INDEX_GLOBAL) entre :
#   PROD (H:) · LOCAL (ReBuild) · GITHUB (curl raw URL)
# Statuts : ✅ SYNC · ⚠️ CRLF (même contenu, fins de ligne) · ❌ DIFF · 🚫 ABSENT
# Rapport : <ReBuild>/historique/hermes_md5_audit_docs_YYYY-MM-DD.txt
#           + copie hermes_md5_audit_docs_latest.txt
#
# ## 📝 DESCRIPTION :
# Script HERMES — complément de audit_md5.sh (YAML prod vs GitHub) et de
# audit_md5_docs.ps1 (Claude). Périmètre : docs .md, 3 niveaux comparés,
# classification qui neutralise l'écart CRLF/LF (local Windows = CRLF,
# prod H: et GitHub = LF). Nom de rapport préfixé "hermes_" pour ne jamais
# entrer en collision avec le rapport de Claude (md5_audit_docs_*.txt).
#
# ## 🧮 CALCUL & SOURCES :
# - LOCAL  : $LOCAL_ROOT/docs/**/*.md + Github/README.md + Github/INDEX_GLOBAL.md
# - PROD   : $PROD_ROOT/docs/**/*.md + README.md + INDEX_GLOBAL.md
# - GITHUB : curl raw https://raw.githubusercontent.com/.../main/<relpath>
# - MD5 brut (octets exacts) + MD5 normalisé (CRLF->LF) pour la classification
# - README/INDEX_GLOBAL : mapping local Github/ -> racine prod & GitHub
#
# ## ⚠️ IMPORTANT (PIÈGES) :
# - curl Windows n'écrit PAS dans /tmp (chemin MSYS) → utiliser un chemin
#   Windows explicite (cygpath -m "$LOCALAPPDATA/Temp") pour le fichier tmp.
# - Fichiers locaux en CRLF (Windows) : le MD5 normalisé tranche entre
#   ⚠️ CRLF (sans action) et ❌ DIFF (action).
# - Chemins à espaces/accents (ex: "Carte Météo Vence.md") : encodage URL
#   via python urllib (disponible en git-bash Windows).
# - S'exécute LOCALEMENT (git-bash Windows), pas sur HA (besoin du montage H:).
# - set -euo pipefail : les find utilisent || true (répertoire absent OK).
#
# ## 🖥️ TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
# - Aucune vignette directe — outil de maintenance DOCS (workflow ReBuild)
# - Alimente : décision de /ha_push_docs avant chaque push GitHub

set -euo pipefail

# ── CONFIG ────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_ROOT="${LOCAL_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"   # ReBuild/
PROD_ROOT="${PROD_ROOT:-/h}"                                       # montage H:
GH_BASE="${GH_BASE:-https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main}"
LOG_DIR="${LOG_DIR:-$LOCAL_ROOT/historique}"

# Chemin Windows explicite pour curl (sinon write error sur /tmp MSYS)
TMP_DIR="$(cygpath -m "$LOCALAPPDATA/Temp" 2>/dev/null || echo "$LOCAL_ROOT")"
TMP_TREE="$TMP_DIR/hermes_audit_tree_$$.txt"
TMP_PROD="$TMP_DIR/hermes_audit_prod_$$.txt"
TMP_LOCAL="$TMP_DIR/hermes_audit_local_$$.txt"
TMP_GH="$TMP_DIR/hermes_audit_gh_$$.tmp"

mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/hermes_md5_audit_docs_$(date '+%Y-%m-%d').txt"

# ── PASS 1 : TREE (référentiel = local, source de vérité DOCS) ────────────
{
echo "╭──────────────────────────────────────────────────────────────────────────────╮"
echo "│ HERMES AUDIT MD5 DOCS — $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "╰──────────────────────────────────────────────────────────────────────────────╯"
echo ""
echo "── PASS 1 : TREE (local ReBuild) ─────────────────────────────────────────────"
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
    # Mapping racine : Github/README.md (local) -> README.md (prod)
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
echo "  → tmp Windows : $TMP_DIR (curl natif ne gère pas /tmp MSYS)" >> "$LOG"
echo "" >> "$LOG"

urlencode() {  # encodage URL (espaces, accents) via python
    python -c 'import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1], safe="/"))' "$1"
}

# ── COMPARAISON 3 NIVEAUX ─────────────────────────────────────────────────
echo "── COMPARAISON PROD / LOCAL / GITHUB ────────────────────────────────────────" >> "$LOG"
printf "%-70s | %-8s | %-8s | %-8s | %s\n" "FICHIER" "PROD" "LOCAL" "GITHUB" "STATUT" >> "$LOG"
printf '%.0s─' {1..115} >> "$LOG"; echo "" >> "$LOG"

# Charger les MD5 dans des tableaux associatifs (fiable, pas de grep en boucle)
declare -A PROD_MD5 LOCAL_MD5
while IFS='|' read -r f m; do [ -n "$f" ] && PROD_MD5["$f"]="$m"; done < "$TMP_PROD"
while IFS='|' read -r f m; do [ -n "$f" ] && LOCAL_MD5["$f"]="$m"; done < "$TMP_LOCAL"

OK=0; CRLF_COUNT=0; DIFF_COUNT=0; ABSENT_COUNT=0

while IFS= read -r rel; do
    # valeurs : "brut normalise" ou "- -"
    prod="${PROD_MD5[$rel]:-- -}"
    loca="${LOCAL_MD5[$rel]:-- -}"

    # GITHUB
    rm -f "$TMP_GH"
    enc=$(urlencode "$rel")
    HTTP_CODE=$(curl -sf --max-time 20 -o "$TMP_GH" -w '%{http_code}' "${GH_BASE}/${enc}" 2>/dev/null || echo "000")
    if [[ "$HTTP_CODE" == "200" ]] && [[ -s "$TMP_GH" ]]; then
        gh="$(md5sum "$TMP_GH" | cut -d' ' -f1) $(tr -d '\r' < "$TMP_GH" | md5sum | cut -d' ' -f1)"
    else
        gh="- -"
    fi

    # Classification
    present=0; raw_same=1; norm_same=1; first_raw=""; first_norm=""
    for v in "$prod" "$loca" "$gh"; do
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

    p1="${prod%% *}"; l1="${loca%% *}"; g1="${gh%% *}"
    [ "$p1" = "-" ] && p1="????"
    [ "$l1" = "-" ] && l1="????"
    [ "$g1" = "-" ] && g1="????"
    printf "%-70s | %.8s | %.8s | %.8s | %s\n" "$rel" "$p1" "$l1" "$g1" "$statut" >> "$LOG"
done < "$TMP_TREE"

# ── RÉSUMÉ ────────────────────────────────────────────────────────────────
{
echo ""
printf '%.0s─' {1..115}; echo ""
echo "RÉSULTAT : $TOTAL fichiers — ✅ $OK SYNC · ⚠️ $CRLF_COUNT CRLF · ❌ $DIFF_COUNT DIFF · 🚫 $ABSENT_COUNT ABSENT"
printf '%.0s─' {1..115}; echo ""
} >> "$LOG"

rm -f "$TMP_TREE" "$TMP_PROD" "$TMP_LOCAL" "$TMP_GH"

# Copie latest (préfixe hermes_ : jamais de collision avec Claude)
cp "$LOG" "$LOG_DIR/hermes_md5_audit_docs_latest.txt" 2>/dev/null || true

echo "$(date '+%Y-%m-%d %H:%M:%S %Z') ✅ HERMES Audit MD5 DOCS terminé : $TOTAL fichiers · $OK SYNC · $CRLF_COUNT CRLF · $DIFF_COUNT DIFF · $ABSENT_COUNT ABSENT → $LOG"

# annotations_log:
# [2026-08-07] Création — script HERMES, format rapport hermes_md5_audit_docs_*.txt
#              (distinct de Claude : md5_audit_docs.ps1 -> md5_audit_docs_*.txt)
#              FIX curl : chemin tmp Windows explicite (cygpath -m) — le curl
#              natif Windows échoue sur /tmp MSYS (write error, exit 23)
#              FIX grep : tableaux associatifs au lieu de grep en boucle
#              (le pattern |rel| ne matchait jamais, ligne = rel|md5)
