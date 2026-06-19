# METEOCONS — Récupération des SVG animés (basmilius)

*Dernière mise à jour : 2026-05-16*

---

## Contexte

Les icônes proviennent du package npm `@meteocons/svg` (basmilius/weather-icons).  
Ce sont des SVG animés via SMIL (`animateTransform`) — pas de JS requis, natif navigateur.

- Repo GitHub : https://github.com/basmilius/weather-icons
- Package npm  : https://www.npmjs.com/package/@meteocons/svg
- Version utilisée : **0.1.0**
- Style utilisé : **fill** (4 styles dispo : fill / flat / line / monochrome)

---

## Méthode : téléchargement via npm tarball

Le repo GitHub ne contient PAS les SVG directement dans les dossiers `packages/svg/fill/` etc.  
Les fichiers sont uniquement disponibles via le tarball npm publié.

### 1. Récupérer le tarball

```bash
# Trouver l'URL du tarball (dernière version)
curl -sL "https://registry.npmjs.org/@meteocons/svg/latest" | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print(d['version'], d['dist']['tarball'])"

# Télécharger
curl -sL "https://registry.npmjs.org/@meteocons/svg/-/svg-0.1.0.tgz" -o meteocons.tgz
```

### 2. Lister le contenu

```bash
tar -tzf meteocons.tgz | grep "^package/fill/" | head -20
```

Structure interne du tarball :
```
package/fill/clear-day.svg
package/fill/cloudy.svg
package/flat/clear-day.svg
package/line/clear-day.svg
package/monochrome/clear-day.svg
...
```

### 3. Extraire le style fill

```bash
mkdir -p meteocons_fill
tar -xzf meteocons.tgz --wildcards 'package/fill/*.svg' -C /tmp/extract/
cp /tmp/extract/package/fill/*.svg ./meteocons_fill/
```

---

## Mapping états HA → noms de fichiers

Les états de `weather.vence` (Météo France) ne correspondent pas directement aux noms basmilius.  
Il faut renommer (ou créer des copies) :

| État HA (`weather.vence`) | Fichier basmilius source       | Copié en             |
|:--------------------------|:-------------------------------|:---------------------|
| `sunny`                   | `clear-day.svg`                | `sunny.svg`          |
| `clear-night`             | `clear-night.svg`              | `clear-night.svg`    |
| `partlycloudy`            | `partly-cloudy-day.svg`        | `partlycloudy.svg`   |
| `partlycloudy-night`      | `partly-cloudy-night.svg`      | `partlycloudy-night.svg` |
| `cloudy`                  | `cloudy.svg`                   | `cloudy.svg`         |
| `fog`                     | `fog-day.svg`                  | `fog.svg`            |
| `rainy`                   | `overcast-day-rain.svg`        | `rainy.svg`          |
| `pouring`                 | `extreme-day-rain.svg`         | `pouring.svg`        |
| `snowy`                   | `snow.svg`                     | `snowy.svg`          |
| `snowy-rainy`             | `sleet.svg`                    | `snowy-rainy.svg`    |
| `windy`                   | `wind.svg`                     | `windy.svg`          |
| `windy-variant`           | `partly-cloudy-day.svg`        | `windy-variant.svg`  |
| `lightning`               | `thunderstorms-day.svg`        | `lightning.svg`      |
| `lightning-rainy`         | `thunderstorms-day-rain.svg`   | `lightning-rainy.svg`|
| `hail`                    | `hail.svg`                     | `hail.svg`           |
| `exceptional`             | `not-available.svg`            | `exceptional.svg`    |

Script de renommage bash :

```bash
declare -A MAP=(
  ["sunny"]="clear-day"
  ["partlycloudy"]="partly-cloudy-day"
  ["cloudy"]="cloudy"
  ["fog"]="fog-day"
  ["rainy"]="overcast-day-rain"
  ["pouring"]="extreme-day-rain"
  ["snowy"]="snow"
  ["snowy-rainy"]="sleet"
  ["windy"]="wind"
  ["windy-variant"]="partly-cloudy-day"
  ["lightning"]="thunderstorms-day"
  ["lightning-rainy"]="thunderstorms-day-rain"
  ["hail"]="hail"
  ["exceptional"]="not-available"
  ["clear-night"]="clear-night"
  ["partlycloudy-night"]="partly-cloudy-night"
)

for HA_STATE in "${!MAP[@]}"; do
  cp "${MAP[$HA_STATE]}.svg" "${HA_STATE}.svg"
done
```

---

## Installation dans Home Assistant

```bash
# Sur le serveur HA (SSH ou terminal VSCode add-on)
mkdir -p /config/www/images/meteocons

# Copier les 16 fichiers renommés depuis ce dossier
# (via SCP, Samba, File Editor, ou GitHub)
```

URL d'accès dans HA : `/local/images/meteocons/{état}.svg`

---

## Utilisation dans button-card (vignette L1C1)

```yaml
type: custom:button-card
show_icon: false
show_entity_picture: true
entity_picture: "[[[ return '/local/images/meteocons/' + states['weather.vence'].state + '.svg'; ]]]"
```

### Fallback si état inconnu

```yaml
entity_picture: "[[[ const s = states['weather.vence'].state; const known = ['sunny','partlycloudy','cloudy','fog','rainy','pouring','snowy','snowy-rainy','windy','windy-variant','lightning','lightning-rainy','hail','exceptional','clear-night','partlycloudy-night']; return '/local/images/meteocons/' + (known.includes(s) ? s : 'exceptional') + '.svg'; ]]]"
```

---

## Notes

- Le CDN `cdn.meteocons.com` n'est **pas** utilisable (retourne 404 sur les chemins testés).
- Le repo GitHub ne publie **pas** les SVG en raw — uniquement via le tarball npm.
- Les 475 SVG du package couvrent alertes, boussoles, UV, phases lunaires, etc. — utiles pour d'autres vignettes.
- Les animations sont du SMIL natif SVG (`animateTransform`) — aucune dépendance JS.
