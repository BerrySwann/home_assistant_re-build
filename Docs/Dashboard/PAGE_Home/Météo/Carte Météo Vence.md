# Carte Météo Vence Corrigée — YAML

**Dernière mise à jour :** 2026-06-26
**Carte HACS :** MeteoCSS Card (`Pulpyyyy/meteocss-card`)
**Version au moment de la rédaction :** v3.1.0

---

## ⚠️ À FAIRE À CHAQUE MISE À JOUR DE LA CARTE (HACS)

> **CRITIQUE :** Quand la carte `meteocss-card` est mise à jour via HACS, les valeurs par défaut de couleurs (`sunrise` / `sunset`) du fichier JS sont **réinitialisées** aux couleurs d'origine (hard saturation, peu esthétiques). Le bloc `colors:` personnalisé ci-dessous N'EST PAS affecté par la mise à jour HACS lui-même (il vit dans le YAML, pas dans le JS) — mais il faut **vérifier après chaque MAJ HACS** que :
> 1. La structure de configuration (`colors.sunrise`, `colors.sunset`) est toujours supportée par la nouvelle version
> 2. Aucun nouveau défaut ou breaking change n'écrase silencieusement le bloc `colors:` personnalisé
> 3. Recoller le bloc `colors:` ci-dessous si la carte semble être revenue aux couleurs d'origine après une MAJ

**Bloc à recoller systématiquement après vérification post-MAJ :**

```yaml
colors:
  sunrise: '#FFF2BD 0%, #F4D797 20%, #EBB58A 40%, #DA7F7D 60%, #B5728E 80%, #776E99 100%'
  sunset: '#FFE58A 0%, #FFCE61 20%, #EE6C45 40%, #BF3475 60%, #50366F 80%, #1F214D 100%'
```

À insérer dans l'instance `custom:meteo-card` qui gère le layer `sky` (voir structure complète plus bas).

---

## 📌 Contexte du projet

Carte météo composite pour le dashboard tablette de Vence, basée sur **MeteoCSS Card** (composant JS chargé via HACS), affichant :
- Ciel dynamique (couleurs selon condition météo + heure)
- Soleil et lune positionnés par calcul astronomique réel (`sun.sun`)
- Rose des vents décorative (SVG en perspective 3D)
- Alertes météo (vigilance Météo France) avec animation de clignotement
- Température et condition actuelle, heure et nom de ville

---

## 🗂️ Où vit quoi

| Élément | Emplacement |
|---|---|
| Logique de rendu (sky/sun/moon/background/foreground), calcul position soleil, couleurs par défaut | **Fichier JS de la carte HACS** (`meteocss-card.js`) — jamais modifié directement |
| Configuration (entités, angle, layers, couleurs personnalisées) | **YAML de la carte** (ce document) |
| Anciens fichiers Jinja (`meteo_settings.jinja`, `rotation.jinja`, `meteo.jinja`) | **Obsolètes** — appartenaient à l'ancien système "100% CSS/Jinja", non utilisés par MeteoCSS Card |
| `demometeo.yaml`, `cssmeteo.yaml` | Probablement **obsolètes** également (à confirmer/nettoyer) |

---

## ⚙️ Paramètre `house_angle` — rappel important

`house_angle` **n'est pas** l'orientation géographique de la façade (Sud = 180° n'est qu'une coïncidence pratique). C'est l'**azimut auquel le soleil est centré visuellement** sur la carte.

- Formule (dans `MeteoCoordsCalculator._calculatePosition`) : le soleil est centré quand `azimuth_réel == house_angle`
- **Valeur actuelle retenue : `180`** → centre le soleil sur l'écran au midi solaire réel (~13h30 à Vence en été)
- Ancienne valeur testée : `212` (orientation réelle de la façade, Sud-Sud-Ouest) → centrage décalé vers 14h45-15h00

---

## 🧩 Structure YAML complète (référence)

```yaml
type: picture-elements
image: /local/meteo/empty.png
elements:
  - type: custom:meteo-card
    weather: weather.vence
    sun_entity: sun.sun
    house_angle: 180
    singleton_id: vence_meteo
    colors:
      sunrise: '#FFF2BD 0%, #F4D797 20%, #EBB58A 40%, #DA7F7D 60%, #B5728E 80%, #776E99 100%'
      sunset: '#FFE58A 0%, #FFCE61 20%, #EE6C45 40%, #BF3475 60%, #50366F 80%, #1F214D 100%'
    layers:
      - sky
      - background
    style:
      top: 50%
      left: 50%
      width: 100%
      height: 100%

  - type: custom:html-template-card
    title: ""
    ignore_line_breaks: true
    picture_elements_mode: true
    content: |-
      <div style="position:absolute;top:52%;left:50%;
        transform:translate(-50%,-50%) perspective(180px) rotateX(58deg);
        width:160px;height:160px;opacity:0.6;pointer-events:none;">
        <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
          <circle cx="100" cy="100" r="78" fill="none" stroke="rgba(150,170,200,0.5)" stroke-width="1.5"/>
          <polygon points="146,54 108,100 146,146 100,108 54,146 92,100 54,54 100,92"
            fill="rgba(120,150,190,0.7)"/>
          <polygon points="100,38 106,94 162,100 106,106 100,162 94,106 38,100 94,94"
            fill="rgba(200,210,225,0.95)"/>
          <circle cx="100" cy="100" r="9" fill="rgba(10,20,40,0.9)" stroke="rgba(200,210,225,0.8)" stroke-width="2"/>
          <text x="100" y="34" text-anchor="middle" font-size="20" font-weight="bold" fill="rgba(220,230,245,1)" font-family="Arial,sans-serif">S</text>
          <text x="100" y="174" text-anchor="middle" font-size="20" font-weight="bold" fill="rgba(150,170,200,0.9)" font-family="Arial,sans-serif">N</text>
          <text x="22" y="106" text-anchor="middle" font-size="20" font-weight="bold" fill="rgba(150,170,200,0.9)" font-family="Arial,sans-serif">E</text>
          <text x="180" y="106" text-anchor="middle" font-size="20" font-weight="bold" fill="rgba(220,230,245,1)" font-family="Arial,sans-serif">W</text>
        </svg>
      </div>
    style:
      top: 58%
      left: 50%
      width: 100%
      height: 100%

  - type: custom:html-template-card
    title: ""
    ignore_line_breaks: true
    picture_elements_mode: true
    content: |-
      {% if is_state('sensor.alerte_meteo', 'Jaune') or
            is_state('sensor.alerte_meteo', 'Orange') or
            is_state('sensor.alerte_meteo', 'Rouge') %}
      <style>
        @keyframes alerte-pulse {
          0%,100% { opacity:1; }
          50%      { opacity:0.3; }
        }
      </style>
      <div style="
        position:absolute;top:70%;left:50%;
        transform:translateX(-50%);
        font-size:14px;font-weight:bold;letter-spacing:4px;
        font-variant:small-caps;
        color:{% if is_state('sensor.alerte_meteo','Jaune') %}rgba(255,185,0,1)
              {% elif is_state('sensor.alerte_meteo','Orange') %}rgba(210,65,0,1)
              {% else %}rgba(150,10,10,1){% endif %};
        text-shadow:0px 1px 4px rgba(0,0,0,0.8);
        white-space:nowrap;pointer-events:none;
        {% if is_state('sensor.alerte_meteo','Rouge') %}animation:alerte-pulse 0.9s ease-in-out infinite;{% endif %}
      ">
        {% if is_state('sensor.alerte_meteo','Jaune') %}⚠️ Vigilance Jaune ⚠️
        {% elif is_state('sensor.alerte_meteo','Orange') %}⚠️ Vigilance Orange ⚠️
        {% else %}⚠️ Vigilance Rouge ⚠️
        {% endif %}
      </div>
      {% endif %}
    style:
      top: "-5%"
      left: 50%
      width: 100%
      height: 100%

  - type: custom:html-template-card
    title: ""
    ignore_line_breaks: true
    picture_elements_mode: true
    content: |-
      <div style="
        position:absolute;bottom:8px;left:50%;
        transform:translateX(-50%);
        font-size:16px;font-weight:bold;letter-spacing:4px;
        font-variant:small-caps;color:rgba(255,255,255,0.85);
        text-shadow:0px 1px 4px rgba(0,0,0,0.8);
        white-space:nowrap;pointer-events:none;">
        {{ states('sensor.vence_original_condition') }} — {{ states('sensor.th_balcon_nord_temperature') | round(1) }}°C
      </div>
    style:
      top: 47%
      left: 50%
      width: 100%
      height: 100%

  - type: custom:html-template-card
    title: ""
    ignore_line_breaks: true
    picture_elements_mode: true
    content: |-
      <div style="
        position:absolute;top:8px;left:50%;
        transform:translateX(-50%);
        font-size:19px;font-weight:bold;letter-spacing:4px;
        font-variant:small-caps;color:rgba(255,255,255,0.85);
        text-shadow:0px 1px 4px rgba(0,0,0,0.8);
        white-space:nowrap;pointer-events:none;">
        VENCE — {{ now().strftime('%H:%M') }}
      </div>
    style:
      top: 50%
      left: 50%
      width: 100%
      height: 100%

  - type: custom:meteo-card
    weather: weather.vence
    sun_entity: sun.sun
    house_angle: 180
    singleton_id: vence_meteo
    layers:
      - sun
      - moon
      - foreground
    style:
      top: 50%
      left: 50%
      width: 100%
      height: 100%

card_mod:
  style: |
    :host {
      display: block;
      height: 270px !important;
      overflow: hidden;
      border-radius: var(--ha-card-border-radius, 12px);
    }
```

---

## 🔑 Points clés à retenir

| Règle | Détail |
|---|---|
| **2 instances `meteo-card` maximum** | Une pour `sky`+`background`, une pour `sun`+`moon`+`foreground`. Ne jamais dupliquer au-delà — cause directe d'`Unknown type` / conflits de rendu observés le 2026-06-26 |
| **`singleton_id: vence_meteo`** | Obligatoire sur les deux instances pour qu'elles partagent le même état météo/soleil/lune (sinon désynchronisation visuelle) |
| **Couleurs personnalisées** | Définies une seule fois, sur l'instance qui gère `sky` (pas besoin de répéter sur la seconde instance) |
| **`card_mod`** | Toujours au niveau racine du `picture-elements`, jamais imbriqué dans un élément de la liste `elements` |
| **Fichiers `.jinja` (meteo_settings, rotation, meteo)** | Orphelins de l'ancien système, sans effet sur MeteoCSS Card — à nettoyer si confirmé inutilisés ailleurs |

---

## 📜 Historique des changements

- **2026-06-26** : Diagnostic complet du problème "Unknown type" (cause : 6 instances `meteo-card` dupliquées sans `singleton_id`). Correction → 2 instances synchronisées. Recherche et intégration de dégradés sunrise/sunset moins saturés que les défauts d'origine.
