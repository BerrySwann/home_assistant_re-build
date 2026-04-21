<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → Ligne 6, Colonne 3 |
| 🔗 **Tap** | `/dashboard-tablette/vigieau` |
| 🏗️ **Layout** | `custom:button-card` — icône + nom dynamiques |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 💧 L6C3 — Vignette Vigieau (Vigilance Eau)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Code](#code--vignette)
3. [Bug corrigé](#bug-corrigé--switch-sans-break)
4. [Entités utilisées](#entités-utilisées--provenance-complète)

---

## 🎯 VUE D'ENSEMBLE

Vignette affichant l'état de vigilance sécheresse pour Vence depuis l'intégration **Vigieau** (HACS). Icône et couleur dynamiques selon le niveau d'alerte. Navigation vers la page `/dashboard-tablette/vigieau` au tap.

### Intégrations requises
- ✅ Vigieau (HACS — `custom_components/vigieau`) — commune Vence

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette carrée — icône + texte couleur dynamiques |

---

## 📍 CODE — VIGNETTE

```yaml
type: custom:button-card
icon: |
  [[[
    var sensor = states['sensor.alert_level_in_vence'];
    var iconName = sensor && sensor.attributes && sensor.attributes.icon
      ? sensor.attributes.icon
      : 'mdi:water-outline';
    return iconName;
  ]]]
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/vigieau
name: |
  [[[
    var sensor = states['sensor.alert_level_in_vence'];
    var alertLevel = sensor.state;
    var alertColor = (sensor.attributes && sensor.attributes.Couleur)
      ? sensor.attributes.Couleur
      : 'grey';
    switch(alertLevel) {
      case 'vigilance (pas de restriction)':
        alertLevel = 'Aucune restriction';
        break;                                    # [L1] break ajouté — fallthrough corrigé
      case 'alerte_renforcee':
        alertLevel = 'Alerte renforcée';
        break;
      case 'crise':
        alertLevel = 'Crise';
        break;
      case 'alerte':
        alertLevel = 'Alerte';
        break;
    }
    return `<div style="text-align: left; color: white; font-size: 13px; margin-bottom: 4px;">Vigieau / Vigi-Eau</div>
            <div><span style="color: ${alertColor}; font-weight: bold;">${alertLevel}</span></div>`;
  ]]]
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
    - transform: rotate(350deg)
    - left: 15%
    - top: 15%
    - color: |
        [[[
          var sensor = states['sensor.alert_level_in_vence'];
          return (sensor && sensor.attributes && sensor.attributes.Couleur)
            ? sensor.attributes.Couleur
            : 'white';
        ]]]
  name:
    - color: white
    - top: 10px
    - left: 10px
    - font-size: 80%
    - font-weight: bold
    - position: absolute
```

---

## 🐛 BUG CORRIGÉ — Switch sans `break`

**Code original :**
```javascript
case 'vigilance (pas de restriction)':
  alertLevel = 'Aucune restriction';
  // ← pas de break → fallthrough vers alerte_renforcee
case 'alerte_renforcee':
  alertLevel = 'Alerte renforcée';
  break;
```

**Effet :** quand l'état est `vigilance`, `alertLevel` est d'abord mis à `'Aucune restriction'` puis immédiatement écrasé par `'Alerte renforcée'` — affichage incorrect.

**Fix [L1] :** `break;` ajouté après `alertLevel = 'Aucune restriction';`

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives Vigieau (HACS)

| Entité | Attributs utilisés | Rôle |
|--------|-------------------|------|
| `sensor.alert_level_in_vence` [NAT] | `.state` — `.attributes.Couleur` — `.attributes.icon` | Niveau alerte, couleur et icône dynamiques |

**États possibles de `sensor.alert_level_in_vence` :**

| État (`.state`) | Affiché | Couleur attendue |
|-----------------|---------|-----------------|
| `null` | *(non géré — state brut)* | grey |
| `vigilance (pas de restriction)` | `Aucune restriction` | *(défini par Vigieau)* |
| `alerte` | `Alerte` | *(défini par Vigieau)* |
| `alerte_renforcee` | `Alerte renforcée` | *(défini par Vigieau)* |
| `crise` | `Crise` | *(défini par Vigieau)* |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.alert_level_in_vence` | Intégration Vigieau (HACS) | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

- [`PAGE_VIGIEAU.md`](./PAGE_VIGIEAU.md) — page détaillée sécheresse / restrictions

---

# annotations_log:
# [L1] break ajouté — case 'vigilance (pas de restriction)' — fallthrough vers alerte_renforcee corrigé

← Retour : `L6C2_POLLUTION_POLLEN/` | → Fin Ligne 6


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_VIGIEAU]]  [[L6C1_VIGNETTE_AIR_QUALITE]]  [[L6C2_VIGNETTE_POLLUTION_POLLEN]]*
