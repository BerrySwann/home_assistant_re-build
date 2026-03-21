<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → Ligne 4, Colonne 1 |
| 🔗 **Tap** | `/dashboard-tablette/systeme-freebox` |
| 🏗️ **Layout** | `custom:button-card` — aspect-ratio 1/1 |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 🌐 L4C1 — Vignette FreeBox Pop

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Code](#code)
3. [Entités utilisées](#entités-utilisées--provenance-complète)
4. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Vignette de navigation carrée 1/1 vers la page Freebox/Réseau. Aucune entité affichée — rôle purement navigationnel. L'icône engrenage tourne à 340° et est colorée en rouge (couleur Error palette CLAUDE.md) pour indiquer que cette section est critique/infra.

### Intégrations requises
- ✅ Aucune (vignette statique — pas d'entité live)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette carrée avec icône et navigation |

---

## 📍 CODE — VIGNETTE

```yaml
type: custom:button-card
icon: mdi:cog-outline
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/systeme-freebox
name: FreeBox Pop
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
    - color: rgb(244,67,54)
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

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives HA (UI — aucun fichier YAML à créer)

| Entité | Intégration | Configuré via |
|--------|-------------|---------------|
| *(aucune)* | — | Vignette statique |

---

## 🐛 DÉPANNAGE

### Icône non visible / vignette blanche
1. Vérifier que `custom:button-card` est installé via HACS.
2. Recharger le cache navigateur (Ctrl+Shift+R).

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Documentation
- [`PAGE_FREEBOX.md`](./PAGE_FREEBOX.md) — page complète `/dashboard-tablette/systeme-freebox`

---

← Retour : `L3C3_STORES/` | → Suivant : `L4C2_MINI_PC/`
