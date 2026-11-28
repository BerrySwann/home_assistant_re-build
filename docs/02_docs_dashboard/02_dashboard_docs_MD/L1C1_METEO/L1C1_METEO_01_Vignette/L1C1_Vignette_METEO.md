<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--11--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette%20Doc-4fc3f7?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📍 **Position** | Dashboard HOME - Ligne 1, Colonne 1 |
| 🔗 **Navigation** | `/dashboard-tablette/meteo` |
| 🃏 **Type de carte** | `custom:button-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-05-09 |
| 🏠 **Version HA** | 2025.2.x → 2.0 |

---

# 🌤️ VIGNETTE L1C1 : MÉTÉO

---

## 📋 VUE D'ENSEMBLE

Cette vignette est le point d'entrée principal vers toutes les informations météorologiques. Elle affiche simplement l'icône météo et le titre, sans données temps réel (contrairement aux autres vignettes qui affichent des custom_fields complexes).

### Design visuel
- Icône : `mdi:weather-partly-cloudy` (nuage partiellement couvert, rotation 350°, couleur gold)
- Aspect : Carré (1:1), bordure blanche double (3px), fond transparent
- Style : Minimaliste, pas de données affichées sur la vignette

---

## 🔧 CODE SOURCE COMPLET

```yaml
type: custom:button-card
show_icon: false
show_entity_picture: true
entity_picture: "[[[ return '/local/images/meteocons/' + states['weather.vence'].state + '.svg'; ]]]"
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/meteo
name: Météo
custom_fields:
  info: "[[[ return states['sensor.vence_original_condition'].state + ' - ' + Math.round(parseFloat(states['sensor.th_balcon_nord_temperature'].state)) + '°' ]]]"
styles:
  card:
    - aspect-ratio: 1/1
    - border-radius: 10px
    - background: transparent
    - border-width: 3px
    - border-color: white
    - border-style: double
    - color: white
    - font-size: 15px
  entity_picture:
    - width: 55%
    - height: auto
    - position: absolute
    - left: 24%
    - top: 19%
  name:
    - color: white
    - top: 12%
    - left: 10%
    - font-size: 80%
    - font-weight: bold
    - position: absolute
  custom_fields:
    info:
      - position: absolute
      - bottom: 10%
      - width: 100%
      - text-align: center
      - color: white
      - font-size: 80%
      - font-weight: bold
```

---

## 📊 ENTITÉS UTILISÉES

| Entité | Source | Rôle |
|--------|--------|------|
| `weather.vence` | Météo-France | Son état choisit l'image `/local/images/meteocons/<état>.svg` |
| `sensor.vence_original_condition` | Météo-France | Condition en texte, première partie de la ligne d'info |
| `sensor.th_balcon_nord_temperature` | Zigbee - UI (Sonoff SNZB-02) | Température extérieure arrondie, deuxième partie de la ligne d'info |

> Cette vignette est purement navigationnelle : elle sert uniquement de bouton d'accès vers la page météo détaillée. Toutes les entités météo sont présentes dans la page de destination.

---

## 🎨 ANATOMIE DE LA CARTE

### Structure `custom:button-card`

```
┌─────────────────────────────────┐
│  Météo          (name)          │ ← Position: top 12%, left 5%
│                                  │
│                                  │
│        🌤️                       │ ← Icône: rotated 350°, color gold
│      (icon)                      │    Position: left 20%, top 20%
│                                  │
│                                  │
└─────────────────────────────────┘
   ↑
   Bordure: 3px double white
   Background: transparent
   Border-radius: 10px
```

### Paramètres clés

| Paramètre | Valeur | Rôle |
|-----------|--------|------|
| `aspect-ratio` | `1/1` | Force un carré parfait |
| `icon.transform` | `rotate(350deg)` | Incline légèrement l'icône (-10°) |
| `icon.color` | `gold` | Couleur dorée pour le soleil |
| `name.position` | `absolute` | Positionnement manuel du texte |
| `size` | `60%` | Taille de l'icône à 60% de l'espace disponible |

---

## 🔄 LOGIQUE DE NAVIGATION

```
USER CLICK
    ↓
tap_action: navigate
    ↓
navigation_path: /dashboard-tablette/meteo
    ↓
OUVERTURE PAGE MÉTÉO DÉTAILLÉE
    ├─ Prévisions Météo France
    ├─ Cartes Windy interactives
    ├─ Rose des vents
    ├─ Baromètre
    ├─ UV / Pluie
    ├─ Pop-up #foudre (Blitzortung)
    ├─ Pop-up #alert (Alertes MétéoFrance)
    └─ Pop-up #sun (Lever/Coucher soleil)
```

> **IMPORTANT :** Le `navigation_path` doit correspondre exactement au `path` défini dans la configuration du dashboard cible (généralement dans `configuration.yaml` ou via l'UI).

---

## 🛠️ MODIFICATIONS COURANTES

### Changer l'icône

```yaml
icon: mdi:weather-sunny  # Soleil plein
icon: mdi:weather-cloudy # Nuageux complet
icon: mdi:weather-rainy  # Pluie
```

### Adapter la couleur de l'icône dynamiquement

```yaml
icon:
  - color: |
      [[[
        const temp = parseFloat(states['sensor.th_balcon_nord_temperature']?.state);
        if (temp < 10) return 'lightblue';
        if (temp < 20) return 'gold';
        return 'orange';
      ]]]
```

### Ajouter un badge de température

```yaml
# À ajouter après "size: 60%"
custom_fields:
  temp: |
    [[[
      const t = states['sensor.th_balcon_nord_temperature']?.state;
      return `<span style="position:absolute; bottom:10px; right:10px; font-size:12px; color:white;">${t}°C</span>`;
    ]]]
```

---

## 🎯 DIFFÉRENCES AVEC LES AUTRES VIGNETTES

| Aspect | Vignette Météo (L1C1) | Vignettes complexes (L1C2, L1C3...) |
|--------|----------------------|--------------------------------------|
| Données affichées | ❌ Aucune | ✅ Multiples custom_fields |
| Entités surveillées | ❌ Aucune | ✅ triggers_update avec 10-30 entités |
| Complexité JS | ⭐ Minimale | ⭐⭐⭐⭐⭐ JavaScript avancé |
| Rôle | 🚪 Navigation pure | 📊 Affichage + Navigation |

---

## 🐛 DÉPANNAGE

### La vignette ne navigue pas
1. Vérifier que le dashboard `/dashboard-tablette/meteo` existe
2. Vérifier les logs HA : `Paramètres > Système > Journaux`
3. Tester en remplaçant par un chemin connu : `navigation_path: /lovelace/0`

### L'icône ne s'affiche pas

```yaml
# Vérifier que button-card est installé via HACS
# Redémarrer HA si l'installation est récente
```

### La bordure ne s'affiche pas en blanc

```yaml
# Vérifier que le thème actif ne surcharge pas les couleurs
# Forcer avec !important si nécessaire :
border-color: white !important
```

---

## 📚 FICHIERS LIÉS

- Page destination : `PAGE_METEO.md` (documentation complète de la page)
- Templates météo : `/templates/meteo/M_01_*` à `M_04_*` (Série Météo)
- Sensors météo : `sensors/meteo/M_03_meteo_sensors_blitzortung.yaml`

---

## 📝 NOTES DE MAINTENANCE

| Champ | Valeur |
|-------|--------|
| Dernière modification | 2026-02-26 |
| Créé par | Eric (BerrySwann) |
| Version HA | 2025.1.x → 2.0 |

### Historique des changements
- `2024-XX-XX` : Création initiale de la vignette
- `2026-02-26` : Documentation complète pour migration HA 2.0
- `2026-05-09` : Mise à jour date - aucun changement YAML (vignette inchangée)

### Points d'attention
- Cette vignette est volontairement simple : ne pas ajouter de custom_fields complexes ici
- L'icône `mdi:weather-partly-cloudy` est statique : elle ne change pas selon la météo réelle
- Si besoin d'une icône dynamique, utiliser la carte météo native HA au lieu de button-card

---

→ **Prochaine étape :** Consulter `PAGE_METEO.md` pour la documentation complète de la page de destination.


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_METEO]]  [[TUTO_IMAGES_ALERTES_METEO_FRANCE]]  [[L1C2_Vignette_TEMPERATURES]]  [[L1C3_Vignette_CLIM]]*

---

## Modifications du 2026-11-28

Le bloc de code source est resynchronisé avec le YAML docs. Différences par rapport à l'ancienne version de la fiche :

- L'icône `mdi:weather-partly-cloudy` est remplacée par une image `entity_picture` (`/local/images/meteocons/<état de weather.vence>.svg`), avec `show_icon: false`.
- Un champ `info` affiche la condition de `sensor.vence_original_condition` suivie de la température arrondie de `sensor.th_balcon_nord_temperature`.
- La section ENTITÉS UTILISÉES est corrigée : la vignette lit bien trois entités, elle n'est plus purement navigationnelle.
<!-- annotations_log: [2026-11-28] L1C1 : lot 3 verif fiches: code resynchronise avec le YAML docs, entites utilisees corrigees (weather.vence, vence_original_condition, th_balcon_nord_temperature) -->
