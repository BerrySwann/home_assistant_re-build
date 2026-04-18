<div align="center">

[![Statut](https://img.shields.io/badge/Statut-VERROUILLÉ-44739e?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-INTERDITES-f44336?style=flat-square)](.)&nbsp;

[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--18-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

> **🔒 DOC VERROUILLÉE — VERSION FINALE**
> Ce fichier est considéré comme terminé. Aucune modification ne doit être apportée sans décision explicite.
>
> ⚠️ **2 bugs esthétiques connus (à traiter ultérieurement) :**
> 1. Icône HA dans la vignette — positionnement à revoir (alignement vertical résiduel à peaufiner)
> 2. Page MAJ — mise en page des grilles à affiner sur petit écran (espacement entre Grille 1 et Grille 2)

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → vignette L4 Ligne 4 Col 3 |
| 🔗 **Accès depuis** | Vignette cliquable → `/dashboard-tablette/maj` |
| 🏗️ **Layout** | `custom:button-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-18 |
| 🏠 **Version HA** | 2026.3 |

---

# 🔄 L4C3 — MISES À JOUR HOME ASSISTANT

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Vignette L4C3](#-vignette-l4c3--button-card)
4. [Entités utilisées](#-entités-utilisées--provenance-complète)
5. [Dépannage](#-dépannage)

---

## 🎯 VUE D'ENSEMBLE

La vignette L4C3 affiche le **nombre total de mises à jour disponibles** dans Home Assistant (Core, Supervisor, HACS, add-ons, intégrations). Elle sert de point d'entrée vers la page dédiée `/dashboard-tablette/maj` qui détaille chaque mise à jour par catégorie.

- **État normal (0 MAJ)** : texte et bordure blancs, icône HA bleue (`lightblue`).
- **État alerte (≥1 MAJ)** : texte et icône orange.
- **Clic** : navigation vers la page `/dashboard-tablette/maj`.

### Intégrations requises

- ✅ Domaine `update` natif HA (Core ≥ 2021.12 — pas d'installation requise)
- ✅ HACS (pour les mises à jour HACS custom)
- ✅ Supervisor / Add-ons (si HA OS ou Supervised)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette L4C3 — affichage compteur + icône HA |
| `custom:mushroom-update-card` | Page MAJ — carte individuelle par composant |
| `custom:mushroom-template-card` | Page MAJ — chips CPU/RAM, versions texte |
| `custom:auto-entities` | Page MAJ — liste dynamique des mises à jour disponibles |
| `custom:mushroom-title-card` | Page MAJ — titres de sections |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────────────┐
│  VIGNETTE L4C3 (button-card)                        │
│  entity: sensor.available_updates                   │
│  → Navigation : /dashboard-tablette/maj             │
└─────────────────────────────────────────────────────┘
                        ↓ clic
         → voir PAGE_MAJ.md pour le YAML complet
```

---

## 📍 VIGNETTE L4C3 — button-card

### Code (version corrigée — bug margin-left résolu)

```yaml
type: custom:button-card
entity: sensor.available_updates
icon: mdi:home-assistant
aspect_ratio: 1/1
name: Software | modules
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/maj
styles:
  card:
    - border-radius: 10px
    - background: transparent
    - border-width: 3px
    - border-color: white
    - border-style: double
    - color: |
        [[[
          if (entity.state == '0') return 'white';
          else return 'orange';
        ]]]
    - font-size: 11px
    - line-height: 1.2
    - font-weight: bold
  grid:
    - grid-template-areas: "'icon n' 'updates updates'"
    - grid-template-columns: auto 1fr
    - grid-template-rows: 1fr min-content
  name:
    - font-weight: bold
    - color: white
    - align-self: start
    - justify-self: center
    - margin-right: 50px
  custom_fields:
    icon:
      - width: 40px
      - height: 40px
      - justify-self: center   # [FIX] margin-left: 250% supprimé (icône hors carte)
      - align-self: center     # [FIX] margin-top: 0% supprimé
      - color: |
          [[[
            if (entity.state == '0') return 'lightblue';
            else return 'orange';
          ]]]
    updates:
      - align-self: start
      - justify-self: center
custom_fields:
  icon: |
    [[[
      return '<ha-icon icon="mdi:home-assistant" style="width: 40px; height: 40px; color: ' +
        (entity.state == '0' ? 'lightblue' : 'orange') + ';"></ha-icon>';
    ]]]
  updates: |
    [[[
      if (entity.state == '0') return 'Tout est à jour';
      else if (entity.state == '1') return '1 mise à jour';
      else return entity.state + ' mises à jour';
    ]]]
```

### Rôle

Affiche sur une seule vignette carrée : l'icône HA (colorisée selon l'état), le nom `Software | modules`, et le résumé textuel du nombre de mises à jour en attente. La couleur passe en orange dès qu'au moins 1 MAJ est disponible.

### Entités

- `sensor.available_updates` [TPL] — compteur template calculé depuis `update.*` (state == 'on')

---

> 📄 **Page complète (YAML des 2 grilles) :** [`PAGE_MAJ.md`](./PAGE_MAJ.md)

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

> Chaque entité est listée avec son **fichier source exact** dans le repo ReBuild.

---

### 🌐 Intégrations natives HA (UI — aucun fichier YAML à créer)

| Entité | Intégration | Configuré via |
|--------|-------------|---------------|
| `update.home_assistant_core_update` | Natif HA | Automatique |
| `update.home_assistant_operating_system_update` | Natif HA | Automatique |
| `update.home_assistant_supervisor_update` | Natif HA | Automatique |
| `update.hacs_update` | HACS | Paramètres > Intégrations |
| `update.*` (add-ons, Z2M, etc.) | Natif HA / intégrations | Automatique |
| `sensor.current_version` | Natif HA | Automatique |
| `sensor.processor_use` | System Monitor | Paramètres > Intégrations |
| `sensor.memory_use_percent` | System Monitor | Paramètres > Intégrations |

---

### 📁 `templates/utilitaires/Mise_a_jour_home_assistant.yaml`
> Calcule le nombre total de mises à jour disponibles (domaine `update`, state == 'on').

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.available_updates` | `available_updates` | Compteur — alimente la vignette L4C3 |

---

## 🐛 DÉPANNAGE

### Icône HA bleue invisible dans la vignette

**Cause :** `margin-left: 250%` dans `styles.custom_fields.icon` pousse l'icône hors de la zone visible de la carte.

**Fix :**
1. Dans le dashboard, éditer la vignette L4C3.
2. Dans `styles → custom_fields → icon`, supprimer les lignes `margin-left: 250%` et `margin-top: 0%`.
3. Vérifier que `justify-self: center` et `align-self: center` sont présents.
4. Sauvegarder — l'icône HA bleue doit apparaître en haut à gauche de la vignette.

### sensor.available_updates indisponible

**Cause :** Le fichier `Mise_a_jour_home_assistant.yaml` absent ou non référencé dans `configuration.yaml`.

**Fix :**
1. Vérifier que `templates/utilitaires/Mise_a_jour_home_assistant.yaml` est présent dans `/config/`.
2. Vérifier que `configuration.yaml` inclut bien `!include_dir_merge_list templates/`.
3. Recharger les templates via HA : Outils développeur > YAML > Recharger les modèles.

### auto-entities ne liste rien

**Cause :** Aucune entité `update.*` en état `on` = tout est à jour. Comportement normal.
Vérifier dans Outils développeur > États : filtrer `update.` et regarder si `state == on`.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.available_updates` | Template | ✅ Essentiel |
| Domaine `update.*` natif HA | Natif | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |
| `custom:mushroom-update-card` | HACS | ✅ Essentiel (page MAJ) |
| `custom:auto-entities` | HACS | ✅ Essentiel (page MAJ) |
| `custom:mushroom-template-card` | HACS | ⚠️ Optionnel (chips CPU/RAM) |
| HACS | HACS | ⚠️ Optionnel (MAJ HACS uniquement) |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA — ReBuild)

- `TREE_CORRIGE/templates/utilitaires/Mise_a_jour_home_assistant.yaml`

### Documentation

- [`PAGE_MAJ.md`](./PAGE_MAJ.md) — YAML complet de la page `/dashboard-tablette/maj` (2 grilles)
- [`docs/WIFI_PRESENCE (Home Page)/PAGE_HOME.md`](../WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md) — vue d'ensemble des 18 vignettes
- [`docs/DEPENDANCES_GLOBALES.md`](../DEPENDANCES_GLOBALES.md) — chaîne de dépendances L4C3

---

← Retour : [`PAGE_HOME.md`](../WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md) | → Suite : [`PAGE_MAJ.md`](./PAGE_MAJ.md)


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_MAJ]]  [[L4C1_VIGNETTE_empty]]  [[L4C2_VIGNETTE_MINI_PC]]*
