<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--10b-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/` *(vignette inline dashboard Home)* |
| 🔗 **Accès depuis** | Vue Home — Ligne 5, Colonne 3 |
| 🔗 **tap →** | `/dashboard-tablette/reserve` |
| 🏗️ **Layout** | `custom:button-card` → `custom:flex-horseshoe-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-10 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

---

# 🗄️ L5C3 — VIGNETTE TAILLE DB MARIADB

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Code](#code)
4. [Logique couleurs — seuils](#logique-couleurs--seuils)
5. [Entités — provenance complète](#entités--provenance-complète)
6. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Vignette compacte affichant la taille de la base de données MariaDB sous forme de jauge en fer à cheval (`flex-horseshoe-card`). La couleur de la jauge évolue du vert au rouge selon le remplissage (0 → 4000 MiB). Un tap navigue vers la page de réserve/stats.

### Intégrations requises

- ✅ **sql** (natif HA) — interroge MariaDB via `!secret mariadb_url`
- ✅ **MariaDB** (addon HA) — base `homeassistant`

### Cartes HACS

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Wrapper vignette — cadre, ratio 1/1, border double |
| `custom:flex-horseshoe-card` | Jauge en fer à cheval avec dégradé par seuils |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────┐
│  custom:button-card (wrapper)           │
│  aspect-ratio 1/1 — border double white │
│  ┌───────────────────────────────────┐  │
│  │  custom_fields: graph             │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │ custom:flex-horseshoe-card  │  │  │
│  │  │  icône  mdi:database        │  │  │
│  │  │  valeur  XXXX.X MiB         │  │  │
│  │  │  label   MARIADB            │  │  │
│  │  │  hline   séparateur         │  │  │
│  │  │  jauge   0 → 4000 MiB       │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
│  tap → /dashboard-tablette/reserve      │
└─────────────────────────────────────────┘
```

---

## 📍 CODE

> ⚠️ **Points de vigilance importants :**
> - `horseshoe_style: colorstopgradient` doit être **dans** le bloc `show:`, pas à la racine.
> - `tap_action` doit être **dans** le tableau `entities`, pas à la racine de `flex-horseshoe-card`.
> - Le `button-card` wrapper intercepte les taps → ne pas mettre de `tap_action` dessus.

```yaml
type: custom:button-card
show_icon: false
show_name: false
styles:
  grid:
    - grid-template-areas: '"graph"'
    - grid-template-columns: 1fr
    - grid-template-rows: 1fr
  card:
    - aspect-ratio: 1/1
    - border-radius: 10px
    - background: transparent
    - border-width: 3px
    - border-color: white
    - border-style: double
    - color: white
    - font-size: 11px
    - line-height: 1.2
  custom_fields:
    graph:
      - width: 115%
      - height: 120%
      - margin-top: 20px
      - margin-left: 10px
      - margin-right: 10px
      - margin-bottom: 0px
      - align-self: center
      - justify-self: center
custom_fields:
  graph:
    card:
      type: custom:flex-horseshoe-card
      entities:
        - entity: sensor.taille_db_home_assistant
          tap_action:
            action: navigate
            navigation_path: /dashboard-tablette/reserve
          decimals: 1
          name: MARIADB
          icon: mdi:database
      show:
        horseshoe: true
        icons: true
        states: true
        names: true
        hlines: true
        horseshoe_style: colorstopgradient
      layout:
        icons:
          - id: 0
            entity_index: 0
            xpos: 50
            ypos: 25
            size: 5
        states:
          - id: 0
            entity_index: 0
            xpos: 50
            ypos: 60
            styles:
              - font-weight: bold;
              - font-size: 30px;
              - opacity: 0.95;
        names:
          - id: 0
            entity_index: 0
            xpos: 50
            ypos: 77
            styles:
              - font-weight: 700;
              - font-size: 15px;
              - opacity: 0.9;
        hlines:
          - id: 0
            xpos: 50
            ypos: 37
            length: 50
            styles:
              - stroke: var(--primary-text-color);
              - stroke-width: 2;
              - stroke-linecap: round;
              - opacity: 1;
      horseshoe_scale:
        min: 0
        max: 4000
        width: 3
      color_stops:
        "0": green
        "1800": gold
        "2500": rgb(231,180,57)
        "3000": rgb(225,156,24)
        "3500": darkorange
        "4000": red
      card_mod:
        style: |
          ha-card {
            background: none !important;
            box-shadow: none !important;
            border: none !important;
          }
```

---

## 🎨 LOGIQUE COULEURS — SEUILS

| Seuil (MiB) | Couleur | Signification |
|:-----------:|---------|---------------|
| 0 | `green` | Base saine, ample marge |
| 1 800 | `gold` | 45 % — attention à surveiller |
| 2 500 | `rgb(231,180,57)` | 62.5 % — nettoyage recommandé |
| 3 000 | `rgb(225,156,24)` | 75 % — action requise |
| 3 500 | `darkorange` | 87.5 % — critique |
| 4 000 | `red` | 100 % — saturation |

> **Rappel :** `max: 4000` MiB = 4 GiB. Ajuster si la base dépasse cette limite.

---

## 📊 ENTITÉS — PROVENANCE COMPLÈTE

### 📁 `sql.yaml`
> Intégration `sql` native HA — interroge `information_schema` via `!secret mariadb_url`.
> Aucun credentials en clair dans le YAML. Requête : `SUM(data_length + index_length) / POWER(1024,2)`.

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.taille_db_home_assistant` | `taille_db_home_assistant` | Taille DB en MiB (1 décimale) |

```yaml
# Entrée dans sql.yaml
- name: "Taille Db Home Assistant"
  unique_id: taille_db_home_assistant
  db_url: !secret mariadb_url
  query: >
    SELECT Round(Sum(data_length + index_length) / POWER(1024,2), 1) AS value
    FROM information_schema.tables
    WHERE table_schema = "homeassistant";
  column: "value"
  unit_of_measurement: "MiB"
  device_class: data_size
```

### 🔐 `secrets.yaml` (référence)

| Clé | Usage |
|-----|-------|
| `mariadb_url` | URL complète `mysql://user:pass@host/homeassistant` utilisée par `sql.yaml` |

---

## 🐛 DÉPANNAGE

### Capteur affiche `0.0` ou `unavailable`
1. Vérifier que `mariadb_url` dans `secrets.yaml` est au format `mysql://user:password@localhost/homeassistant?charset=utf8mb4`
2. Tester la connexion depuis le terminal HA : `mysql -u USER -p'PASS' -e 'SHOW DATABASES;'`
3. Vérifier que l'intégration `sql` est bien chargée : **Paramètres → Journaux → Filtrer "sql"**
4. Forcer le rechargement via **Outils développeur → YAML → Recharger sql**

### Horseshoe ne s'affiche pas / couleur bleue au lieu du dégradé
- Vérifier que `horseshoe_style: colorstopgradient` est bien **dans** `show:` (pas à la racine)
- Vérifier que tous les flags `show:` sont présents (`horseshoe`, `icons`, `states`, `names`, `hlines`)

### tap_action ne fonctionne pas
- Le `tap_action` doit être **dans** le tableau `entities`, pas à la racine de `flex-horseshoe-card`
- Ne pas mettre de `tap_action` sur le `button-card` wrapper — il intercepte les taps et bloque la navigation

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.taille_db_home_assistant` | `sql.yaml` | ✅ Essentiel |
| `mariadb_url` dans `secrets.yaml` | Secret HA | ✅ Essentiel |
| `custom:flex-horseshoe-card` | HACS | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |
| MariaDB addon HA | Addon | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA v2.0)
- `sql.yaml` — définition du capteur `sensor.taille_db_home_assistant`
- `secrets.yaml` — `mariadb_url` (credentials hors repo)

### Documentation
- `docs/L5C1_PILES_BATTERIES/L5C1_VIGNETTE_BATTERIES.md` — vignette L5 adjacente

---

← Retour : `L5C2_BATTERIE_PORTAIL` | → Suivant : `L6C1_QUALITE_AIR`
