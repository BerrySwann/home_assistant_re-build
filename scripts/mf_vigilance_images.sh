#!/bin/bash
# Cartes de vigilance Meteo France (aujourd'hui J0 / demain J1) vers un dossier local.
# Usage : mf_vigilance_images.sh [dossier_de_sortie] [both|J0|J1]
#   sans 2e argument : les deux cartes (comportement d'origine, inchange)
#
# Aucun token a maintenir : le cookie de session est rederivE a chaque execution.
# Le token attendu par l'API est le cookie mfsession passe au ROT13, envoye en
# Authorization: Bearer. Le cookie ne vit qu'une heure, d'ou la rederivation.
set -u

DEST="${1:-/config/www/weather}"
ECHEANCE="${2:-both}"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140.0 Safari/537.36"
API="https://rwg.meteofrance.com/wsft/v3/warning/thumbnail?domain=FRA&resolution=large&warning_type=vigilance"
JAR="$(mktemp)"
trap 'rm -f "$JAR"' EXIT
mkdir -p "$DEST"

# 1) poser le cookie de session
curl -s -c "$JAR" -A "$UA" -m 20 "https://vigilance.meteofrance.fr/fr" -o /dev/null || exit 1
SESS=$(awk '$6=="mfsession"{print $7}' "$JAR")
[ -n "$SESS" ] || { echo "cookie mfsession absent"; exit 1; }

# 2) le token est ce cookie passe au ROT13
TOKEN=$(printf '%s' "$SESS" | tr 'A-Za-z' 'N-ZA-Mn-za-m')

# 3) telecharger les deux cartes et refuser tout ce qui n'est pas un vrai PNG
case "$ECHEANCE" in
  J0|j0) PAIRS="J0:today" ;;
  J1|j1) PAIRS="J1:tomorrow" ;;
  *)     PAIRS="J0:today J1:tomorrow" ;;
esac
for PAIR in $PAIRS; do
  ECH="${PAIR%%:*}"; NOM="${PAIR##*:}"
  F="$DEST/meteo_france_alerte_${NOM}.png"
  curl -s -A "$UA" -m 30 -H "Authorization: Bearer $TOKEN" -o "$F" "$API&echeance=$ECH" || exit 1
  head -c 8 "$F" | grep -q "PNG" || { echo "reponse non PNG pour $ECH"; exit 1; }
done

# Valeur de retour pour un capteur command_line : un capteur qui n'ecrit qu'un fichier
# reste unavailable a vie, et l'automation de rattrapage boucle alors pour rien.
date +"%Y-%m-%dT%H:%M:%S maj ok"
