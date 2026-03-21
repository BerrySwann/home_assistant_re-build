<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/vigieau` |
| 🔗 **Accès depuis** | Vignette L6C3 (tap) |
| 🏗️ **Layout** | `type: grid` — section unique SÉCHERESSE |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 💧 L6C3 — Page Vigieau (Vigilance Eau — Restrictions Sécheresse)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Section Sécheresse](#section-sécheresse)
4. [Entités utilisées](#entités-utilisées--provenance-complète)
5. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page affichant le niveau d'alerte sécheresse et les restrictions en vigueur pour Vence, depuis l'intégration **Vigieau** (HACS). Structure en 3 blocs : carte état niveau (custom:button-card colorée), barre progression (custom:bar-card 0→4), liste dynamique des restrictions actives (custom:auto-entities filtrant `sensor.*_restrictions_vence`).

### Intégrations requises
- ✅ Vigieau (HACS — `custom_components/vigieau`) — commune Vence

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Carte état niveau sécheresse (couleur dynamique) |
| `custom:bar-card` | Barre progression niveau 0→4 |
| `custom:auto-entities` | Liste dynamique des restrictions actives |
| `custom:vertical-stack-in-card` | Groupement sans bordure |
| `card_mod` | Suppression bordures |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────────┐
│  HEADING — SECHERESSE                           │
├─────────────────────────────────────────────────┤
│  custom:button-card                             │
│  sensor.alert_level_in_vence                    │
│  (couleur fond dynamique par état)              │
├─────────────────────────────────────────────────┤
│  custom:bar-card                                │
│  sensor.alert_level_in_vence_numeric (0→4)      │
│  (barre couleur attribut 'Couleur')             │
├─────────────────────────────────────────────────┤
│  custom:auto-entities                           │
│  filter: entity_id sensor.*_restrictions_vence  │
│  (grid 4 colonnes — toutes restrictions)        │
└─────────────────────────────────────────────────┘
```

---

## 📍 SECTION SÉCHERESSE

### Carte état — `custom:button-card`

La couleur du fond est calculée dynamiquement selon l'état de `sensor.alert_level_in_vence` :

| État entité | Couleur fond | Signification |
|-------------|-------------|---------------|
| `null` / `unavailable` | `rgb(200, 200, 200)` | Données indisponibles |
| `vigilance` | `rgb(165, 207, 123)` | Vigilance (vert) |
| `alerte` | `rgb(254, 178, 76)` | Alerte (orange) |
| `alerte_renforcee` | `rgb(244, 67, 54)` | Alerte renforcée (rouge) |
| `crise` | `rgb(150, 0, 50)` | Crise (bordeaux) |

> ⚠️ **Typo dans le code source** : l'état `alerte` contient `rgb(254, 178, 7 un6)` → valeur incorrecte. La couleur correcte est `rgb(254, 178, 76)`.

```yaml
type: custom:button-card
entity: sensor.alert_level_in_vence
show_state: true
show_name: true
name: "Niveau d'alerte"
styles:
  card:
    - background: |
        [[[
          var state = entity.state;
          if (!state || state === 'unavailable' || state === 'null') return 'rgb(200, 200, 200)';
          if (state === 'vigilance')        return 'rgb(165, 207, 123)';
          if (state === 'alerte')           return 'rgb(254, 178, 76)';
          if (state === 'alerte_renforcee') return 'rgb(244, 67, 54)';
          if (state === 'crise')            return 'rgb(150, 0, 50)';
          return 'rgb(200, 200, 200)';
        ]]]
card_mod:
  style: |
    ha-card {
      border: none !important;
      box-shadow: none !important;
    }
```

### Barre progression — `custom:bar-card`

```yaml
type: custom:bar-card
entity: sensor.alert_level_in_vence_numeric
min: 0
max: 4
name: "Niveau alerte sécheresse"
color: "{{ state_attr('sensor.alert_level_in_vence_numeric', 'Couleur') }}"
card_mod:
  style: |
    ha-card {
      border: none !important;
      box-shadow: none !important;
      background: transparent;
    }
```

> L'attribut `Couleur` est exposé nativement par l'intégration Vigieau — même logique que les attributs AtmoFrance.

### Liste restrictions — `custom:auto-entities`

```yaml
type: custom:auto-entities
filter:
  include:
    - entity_id: sensor.*_restrictions_vence
card:
  type: grid
  columns: 4
  square: false
card_mod:
  style: |
    ha-card {
      border: none !important;
      box-shadow: none !important;
      background: transparent;
    }
```

États possibles des entités restrictions :
- `Aucune restriction`
- `Sensibilisation`
- `Interdiction sauf exception`
- `Interdiction`

### Tap action — `browser_mod.popup` (fonctionnel — v1)

La syntaxe `fire-dom-event` avec `browser_mod.popup` fonctionne avec **browser_mod v1.x** (HACS) correctement installé et enregistré dans le navigateur.

```yaml
tap_action:
  action: fire-dom-event
  browser_mod:
    service: browser_mod.popup
    data:
      title: |
        [[[ return entity.attributes.friendly_name; ]]]
      style: |
        --popup-min-width: 300px;
        --popup-max-width: 300px;
      content:
        type: custom:button-card
        entity: |
          [[[ return entity.entity_id; ]]]
        show_state: true
        show_name: true
        show_icon: false
        styles:
          card:
            - padding: 16px
          name:
            - font-size: 14px
          state:
            - font-size: 18px
            - font-weight: bold
        card_mod:
          style: |
            ha-card {
              border: none !important;
              box-shadow: none !important;
              background: transparent;
            }
```

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives Vigieau (HACS — aucun fichier YAML à créer)

| Entité | Attributs exposés | Rôle |
|--------|------------------|------|
| `sensor.alert_level_in_vence` | état textuel | Niveau d'alerte global (`null` / `vigilance` / `alerte` / `alerte_renforcee` / `crise`) |
| `sensor.alert_level_in_vence_numeric` | `Couleur`, `icon` | Niveau d'alerte numérique 0→4 |
| `sensor.*_restrictions_vence` | état textuel | Restrictions par usage (arrosage / piscine / lavage / ...) — liste variable |

> ✅ Toutes les entités sont natives Vigieau (HACS `custom_components/vigieau`) — aucun template YAML requis.

---

## 🐛 DÉPANNAGE

### Entité `sensor.alert_level_in_vence` unavailable
1. Vérifier que l'intégration Vigieau (HACS) est installée et configurée pour la commune **Vence** (06140).
2. L'API Vigieau (vigieau.gouv.fr) peut être indisponible ponctuellement — attendre la prochaine mise à jour.
3. Consulter les logs HA → chercher `vigieau`.

### `custom:auto-entities` n'affiche aucune restriction
- Si `sensor.*_restrictions_vence` ne retourne aucune entité, l'intégration n'a peut-être pas encore synchronisé les données de restriction.
- Vérifier les entités disponibles dans Outils Développeur > États → chercher `restrictions_vence`.

### Couleur fond toujours grise
- L'état `null` de Vigieau (aucune restriction active) est affiché en gris — comportement normal.
- Si l'état réel est `vigilance` ou supérieur mais la couleur reste grise, vérifier que `entity.state` correspond bien aux valeurs attendues (attention aux majuscules/underscores).

### Dépannage — `browser_mod.popup` ne se déclenche pas

**Cause la plus fréquente :** browser_mod n'est pas installé via HACS, ou installé mais pas encore enregistré dans le navigateur.

**Diagnostic en 3 étapes :**

1. Vérifier que browser_mod est installé → HACS → Intégrations → chercher "browser_mod"
2. Après installation, **recharger la page** dans le navigateur (F5 ou Ctrl+R) — l'enregistrement se fait au premier chargement
3. Vérifier que l'entité `sensor.browser_mod_*` apparaît dans Outils Développeur → États

**Prérequis :** browser_mod v1.x (HACS) installé et navigateur rechargé → `fire-dom-event` fonctionne normalement.

---

### Typo couleur état `alerte`
- Code source contient `rgb(254, 178, 7 un6)` → corriger en `rgb(254, 178, 76)`.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| Vigieau (HACS) — commune Vence | Intégration native | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |
| `custom:bar-card` | HACS | ✅ Essentiel |
| `custom:auto-entities` | HACS | ✅ Essentiel |
| `custom:vertical-stack-in-card` | HACS | Optionnel |
| `card_mod` | HACS | ✅ Essentiel |
| `browser_mod` | HACS | ✅ v1.x — installé, fonctionne |

---

## 🔗 FICHIERS LIÉS

### Documentation
- [`L6C3_VIGNETTE_VIGIEAU.md`](./L6C3_VIGNETTE_VIGIEAU.md) — vignette résumé
- [`../L6C2_POLLUTION_POLLEN/`](../L6C2_POLLUTION_POLLEN/) — qualité air extérieur (AtmoFrance)

---

← Retour : `L6C2_POLLUTION_POLLEN/` | → Fin Ligne 6
