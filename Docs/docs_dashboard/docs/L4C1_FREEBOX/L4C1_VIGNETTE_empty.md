<div align="center">

[![Statut](https://img.shields.io/badge/Statut-%E2%9B%94%20SUPPRIM%C3%89-f44336?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--17-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → Ligne 4, Colonne 1 |
| 🔗 **Tap** | `/dashboard-tablette/systeme-freebox` |
| 🏗️ **Layout** | `custom:button-card` — aspect-ratio 1/1 |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-17 |
| 🏠 **Version HA** | 2026.3 |

> ⛔ **SUPPRIMÉ 2026-04-17** : Routeur Beryl en coupure entre la Freebox et HA → impossible d'accéder aux données Freebox. Intégration Freebox et SpeedTest abandonnées. La vignette L4C1 est remplacée par un placeholder **Empty** (`mdi:flask-empty`).

---

# 🌐 L4C1 — Vignette Placeholder (Empty)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Code](#code)
3. [Dépendances](#dépendances-critiques)

---

## 🎯 VUE D'ENSEMBLE

Vignette placeholder statique — remplace l'ancienne vignette FreeBox Pop. Aucune entité affichée. La page cible (`/dashboard-tablette/systeme-freebox`) est marquée ⛔ OBSOLÈTE.

### Motif de suppression
- Routeur **Beryl** positionné en coupure entre la Freebox et HA → intégration Freebox inaccessible
- **SpeedTest CLI** abandonné (binaire manquant au démarrage, erreurs log au boot)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette carrée placeholder |

---

## 📍 CODE — VIGNETTE

```yaml
type: custom:button-card
icon: mdi:flask-empty
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/systeme-freebox
name: Empty
size: 60%
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
    - line-height: 1.2
  icon:
    - transform: rotate(340deg)
    - left: 20%
    - top: 20%
    - color: white
    - opacity: 1
  name:
    - color: white
    - top: 12%
    - left: 5%
    - font-size: 80%
    - font-weight: bold
    - position: absolute
```

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Documentation
- [`PAGE_FREEBOX.md`](./PAGE_FREEBOX.md) — page ⛔ OBSOLÈTE

---

← Retour : `L3C3_STORES/` | → Suivant : `L4C2_MINI_PC/`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_empty]]  [[L4C2_VIGNETTE_MINI_PC]]  [[L4C3_VIGNETTE_MAJ]]*
