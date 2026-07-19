#!/usr/bin/env bash
# =============================================================================
# prod_tree.sh — Arborescence complète de la prod HA (yaml / sh / txt)
# Dépôt   : docs_scripts/TREE_CORRIGE/.scripts/prod_tree.sh
# Prod     : /homeassistant/.scripts/prod_tree.sh
# Usage    : bash /homeassistant/.scripts/prod_tree.sh
# Sortie   : /homeassistant/prod_tree_YYYY-MM-DD.txt
# =============================================================================

DATE=$(date +%Y-%m-%d)
OUTPUT="/homeassistant/prod_tree_${DATE}.txt"

# --- YAML (hors dossiers système) ---
find /homeassistant \
  -name "*.yaml" \
  -not -path "*/custom_components/*" \
  -not -path "*/.git/*" \
  -not -path "*/blueprints/*" \
  -not -path "*/.storage/*" \
  -not -path "*/www/*" \
  -not -path "*/deps/*" \
  -print > "${OUTPUT}"

# --- Scripts bash ---
find /homeassistant \
  -name "*.sh" \
  -not -path "*/.git/*" \
  -print >> "${OUTPUT}"

# --- Fichiers texte (hors fichiers prod_tree eux-mêmes) ---
find /homeassistant \
  -name "*.txt" \
  -not -path "*/.git/*" \
  -not -name "prod_tree_*.txt" \
  -print >> "${OUTPUT}"

sort -o "${OUTPUT}" "${OUTPUT}"
echo "✅ $(wc -l < "${OUTPUT}") fichiers listés → ${OUTPUT}"
