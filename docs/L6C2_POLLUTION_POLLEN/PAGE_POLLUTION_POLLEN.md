<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/pollen-pollution` |
| 🔗 **Accès depuis** | Vignette L6C2 (tap) |
| 🏗️ **Layout** | `type: grid` — `column_span: 10` — 2 sections distinctes |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 🌿 L6C2 — Page Pollens & Pollution (Atmo France — Vence)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Section Pollens](#section-pollens)
4. [Section Qualité de l'Air](#section-qualité-de-lair)
5. [Palette de couleurs AtmoFrance](#palette-de-couleurs-atmofrance)
6. [Entités utilisées](#entités-utilisées--provenance-complète)
7. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page en 2 sections verticales : **Pollens** (6 espèces — grid 3 colonnes) et **Qualité de l'air** (5 polluants — grid 5 colonnes). Toutes les entités proviennent de l'intégration **AtmoFrance** (HACS) — les entités `sensor.qualite_globale_*` exposent des attributs `Libellé` et `Couleur` directement exploitables dans les cartes sans template intermédiaire.

### Intégrations requises
- ✅ AtmoFrance (HACS — `custom_components/atmofrance`) — station Vence

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:entity-progress-card-template` | Barre de progression globale Pollens / Air |
| `custom:ring-tile` | Jauge circulaire par espèce/polluant (0-7) |
| `custom:text-divider-row` | Séparateurs de sections |
| `custom:vertical-stack-in-card` | Groupement sans bordure |
| `custom:stack-in-card` | Bloc section sans bordure |
| `custom:mod-card` | CSS variables text-divider |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────────┐
│  HEADING — POLLENS - POLUTION                   │
├─────────────────────────────────────────────────┤
│  ── POLLENS [ Atmo France - Vence ] ──          │
│  entity-progress-card — qualite_globale_pollen  │
│  (barre 0→7, libellé + couleur dynamiques)      │
│  Grid 3 colonnes — 6 ring-tile espèces          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │Graminées│ │Ambroisie│ │ Armoise │           │
│  └─────────┘ └─────────┘ └─────────┘           │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │  Aulne  │ │ Bouleau │ │ Olivier │           │
│  └─────────┘ └─────────┘ └─────────┘           │
├─────────────────────────────────────────────────┤
│  ── QUALITE DE L'AIR [ Atmo France - Vence ] ── │
│  entity-progress-card — qualite_globale_vence   │
│  (barre 0→7, libellé + couleur dynamiques)      │
│  Grid 5 colonnes — 5 ring-tile polluants        │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐           │
│  │ O₃ │ │NO₂ │ │SO₂ │ │PM10│ │PM25│           │
│  └────┘ └────┘ └────┘ └────┘ └────┘           │
└─────────────────────────────────────────────────┘
```

---

## 📍 SECTION POLLENS

### Barre globale (`entity-progress-card-template`)

```yaml
entity: sensor.qualite_globale_pollen_vence
name: Qualité Pollens
icon: mdi:flower-pollen
secondary: "{{ state_attr(entity, 'Libellé') }} ({{ states(entity) }})"
bar_color: "{{ state_attr(entity, 'Couleur') }}"
color: "{{ state_attr(entity, 'Couleur') }}"
bar_size: large
bar_effect: radius
percent: |
  {% set current = states(entity) | int(0) %}
  {% set max_value = 7 %}
  {{ (current / max_value * 100) | round(0) }}
```

> Les attributs `Libellé` et `Couleur` sont fournis **nativement** par l'intégration AtmoFrance — pas de template YAML requis.

### Ring-tiles par espèce (grid 3 colonnes, scale 0.96)

Chaque ring-tile utilise **deux entités** :
- `entity` → concentration brute (valeur affichée au centre)
- `ring_entity` → niveau d'indice 0-7 (pilote l'anneau coloré)

| Espèce | entity (concentration) | ring_entity (niveau) |
|--------|----------------------|----------------------|
| Graminées | `sensor.concentration_gramine_vence` | `sensor.niveau_gramine_vence` |
| Ambroisie | `sensor.concentration_ambroisie_vence` | `sensor.niveau_ambroisie_vence` |
| Armoise | `sensor.concentration_armoise_vence` | `sensor.niveau_armoise_vence` |
| Aulne | `sensor.concentration_aulne_vence` | `sensor.niveau_aulne_vence` |
| Bouleau | `sensor.concentration_bouleau_vence` | `sensor.niveau_bouleau_vence` |
| Olivier | `sensor.concentration_olivier_vence` | `sensor.niveau_olivier_vence` |

---

## 📍 SECTION QUALITÉ DE L'AIR

### Barre globale

```yaml
entity: sensor.qualite_globale_vence
name: Qualité Air
secondary: "{{ state_attr(entity, 'Libellé') }} ({{ states(entity) }})"
bar_color: "{{ state_attr(entity, 'Couleur') }}"
color: "{{ state_attr(entity, 'Couleur') }}"
```

### Ring-tiles par polluant (grid 5 colonnes, scale 0.57)

> ⚠️ Les polluants utilisent `ring_entity: sensor.*_vence` (même entité que `entity`) — l'anneau et la valeur sont pilotés par la même entité, contrairement aux pollens qui dissocient concentration/niveau.

> ⚠️ **Typo** : O₃ a `ring_type: opn` au lieu de `ring_type: open` — à corriger si l'anneau ne s'affiche pas.

| Polluant | entity / ring_entity |
|----------|---------------------|
| O₃ (Ozone) | `sensor.ozone_vence` |
| NO₂ (Dioxyde d'azote) | `sensor.dioxyde_d_azote_vence` |
| SO₂ (Dioxyde de soufre) | `sensor.dioxyde_de_soufre_vence` |
| PM10 | `sensor.pm10_vence` |
| PM25 | `sensor.pm25_vence` |

---

## 🎨 PALETTE DE COULEURS ATMOFRANCE (0→7)

Commune à tous les ring-tiles pollens et polluants :

| Indice | Couleur HEX | Rendu |
|--------|-------------|-------|
| 0 | `#ddd` | Gris clair (données absentes) |
| 1 | `#50f0e6` | Cyan (Très bon) |
| 2 | `#50ccaa` | Vert (Bon) |
| 3 | `#f0e641` | Jaune (Moyen) |
| 4 | `#ff5050` | Rouge clair (Médiocre) |
| 5 | `#960032` | Rouge foncé (Mauvais) |
| 6 | `#872181` | Violet (Très mauvais) |
| 7 | `#888` | Gris (Extrêmement mauvais) |

> Note : la palette AtmoFrance officielle est légèrement différente de la palette CLAUDE.md — elle est conservée telle quelle pour cohérence avec les données officielles.

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives AtmoFrance (HACS — aucun fichier YAML à créer)

**Indices globaux :**

| Entité | Attributs exposés | Rôle |
|--------|------------------|------|
| `sensor.qualite_globale_vence` | `Libellé`, `Couleur` | Indice qualité air global 0-7 |
| `sensor.qualite_globale_pollen_vence` | `Libellé`, `Couleur` | Indice pollen global 0-7 |

**Pollens (× 6 espèces) :**

| Concentration | Niveau |
|--------------|--------|
| `sensor.concentration_gramine_vence` | `sensor.niveau_gramine_vence` |
| `sensor.concentration_ambroisie_vence` | `sensor.niveau_ambroisie_vence` |
| `sensor.concentration_armoise_vence` | `sensor.niveau_armoise_vence` |
| `sensor.concentration_aulne_vence` | `sensor.niveau_aulne_vence` |
| `sensor.concentration_bouleau_vence` | `sensor.niveau_bouleau_vence` |
| `sensor.concentration_olivier_vence` | `sensor.niveau_olivier_vence` |

**Polluants atmosphériques (× 5) :**

| Entité | Polluant |
|--------|---------|
| `sensor.ozone_vence` | O₃ |
| `sensor.dioxyde_d_azote_vence` | NO₂ |
| `sensor.dioxyde_de_soufre_vence` | SO₂ |
| `sensor.pm10_vence` | PM10 |
| `sensor.pm25_vence` | PM25 (extérieur AtmoFrance — ≠ `sensor.qualite_air_salon_ikea_pm25` intérieur IKEA) |

> ⚠️ `sensor.pm25_vence` est la mesure **extérieure** AtmoFrance — ne pas confondre avec les capteurs IKEA Vindstyrka intérieurs documentés en L6C1.

---

## 🐛 DÉPANNAGE

### Anneau O₃ ne s'affiche pas
Typo dans le code : `ring_type: opn` → corriger en `ring_type: open`.

### Entités `sensor.*_vence` indisponibles
1. Vérifier que l'intégration AtmoFrance (HACS) est installée et configurée pour la station **Vence** (06).
2. L'API AtmoFrance peut avoir des délais de mise à jour (toutes les heures environ).
3. Consulter les logs HA → chercher `atmofrance`.

### `entity-progress-card-template` affiche barre vide
Vérifier que l'attribut `Couleur` de l'entité AtmoFrance est bien une couleur CSS valide (ex: `#50ccaa`). Si l'entité est `unavailable`, la barre sera vide.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| AtmoFrance (HACS) — station Vence | Intégration native | ✅ Essentiel |
| `custom:entity-progress-card-template` | HACS | ✅ Essentiel |
| `custom:ring-tile` | HACS | ✅ Essentiel |
| `custom:text-divider-row` | HACS | ✅ Essentiel |
| `custom:vertical-stack-in-card` | HACS | ✅ Essentiel |
| `custom:stack-in-card` | HACS | ✅ Essentiel |
| `custom:mod-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Documentation
- [`L6C2_VIGNETTE_POLLUTION_POLLEN.md`](./L6C2_VIGNETTE_POLLUTION_POLLEN.md) — vignette résumé
- [`../L6C1_AIR_QUALITE/`](../L6C1_AIR_QUALITE/) — qualité air intérieur (IKEA Vindstyrka)

---

← Retour : `L6C1_AIR_QUALITE/` | → Suivant : `L6C3_VIGIEAU/`
