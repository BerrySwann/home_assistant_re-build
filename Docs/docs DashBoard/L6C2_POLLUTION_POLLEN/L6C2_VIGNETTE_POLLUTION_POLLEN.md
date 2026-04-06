<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → Ligne 6, Colonne 2 |
| 🔗 **Tap** | `/dashboard-tablette/pollen-pollution` |
| 🏗️ **Layout** | `custom:button-card` — name dynamique JavaScript |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 🌿 L6C2 — Vignette Pollulèn ©

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Logique d'affichage](#logique-daffichage)
3. [Code](#code)
4. [Entités utilisées](#entités-utilisées--provenance-complète)
5. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Vignette "Pollulèn ©" affichant simultanément le **niveau de qualité de l'air** et le **niveau pollen** pour Vence, avec code couleur dynamique sur une échelle 0-7. Le `name` est entièrement généré en JavaScript — pas de texte statique. Navigation vers la page `/dashboard-tablette/pollen-pollution`.

### Intégrations requises
- ✅ AtmoFrance (HACS — `custom_components/atmofrance`) ou équivalent fournissant `sensor.qualite_globale_vence` et `sensor.qualite_globale_pollen_vence`

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette avec `name` JavaScript dynamique bi-couleur |

---

## 🎨 LOGIQUE D'AFFICHAGE

### Échelle de couleur (commune air + pollen)

| Niveau | Couleur | Signification indicative |
|--------|---------|--------------------------|
| 0 | `grey` | Données indisponibles |
| 1 | `green` | Très bon |
| 2 | `lightgreen` | Bon |
| 3 | `gold` | Moyen |
| 4 | `orange` | Médiocre |
| 5 | `red` | Mauvais |
| 6 | `darkred` | Très mauvais |
| 7 | `purple` | Extrêmement mauvais |

### Rendu affiché

```
Pollulèn ©
Niveau X  /  Niveau Y
  ^air          ^pollen
  (coloré)      (coloré)
```

---

## 📍 CODE — VIGNETTE

```yaml
type: custom:button-card
icon: mdi:face-mask-outline
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/pollen-pollution
name: |-
  [[[
    var airQuality = states['sensor.qualite_globale_vence'].state;
    var pollenAlert = states['sensor.qualite_globale_pollen_vence'].state;
    function getColor(value) {
      var severity = [
        { color: 'grey',    from: 0, to: 0 },
        { color: 'green',   from: 1, to: 1 },
        { color: 'lightgreen', from: 2, to: 2 },
        { color: 'gold',    from: 3, to: 3 },
        { color: 'orange',  from: 4, to: 4 },
        { color: 'red',     from: 5, to: 5 },
        { color: 'darkred', from: 6, to: 6 },
        { color: 'purple',  from: 7, to: 7 }
      ];
      var color = severity.find(function(range) {
        return value >= range.from && value <= range.to;
      });
      return color ? color.color : 'black';
    }
    var airColor    = getColor(airQuality);
    var pollenColor = getColor(pollenAlert);
    return `<div style="text-align: left; color: white; font-size: 13px; margin-bottom: 4px;">Pollulèn ©</div>
            <div>
              <span style="color: ${airColor}; font-weight: bold;">Niveau ${airQuality}</span> /
              <span style="color: ${pollenColor}; font-weight: bold;">Niveau ${pollenAlert}</span>
            </div>`;
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
    - color: white
    - opacity: 1
  name:
    - color: white
    - top: 10px
    - left: 10px
    - font-size: 80%
    - font-weight: bold
    - position: absolute
```

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives HA

| Entité | Source probable | Rôle |
|--------|----------------|------|
| `sensor.qualite_globale_vence` [NAT] | AtmoFrance (HACS) | Indice qualité de l'air 0-7 — attributs `Libellé` + `Couleur` natifs |
| `sensor.qualite_globale_pollen_vence` [NAT] | AtmoFrance (HACS) | Indice pollen 0-7 — attributs `Libellé` + `Couleur` natifs |

> ✅ **Confirmé** : entités natives AtmoFrance (HACS — `custom_components/atmofrance`). Les attributs `Libellé` et `Couleur` sont exposés directement par l'intégration — aucun template YAML intermédiaire requis.

---

## 🐛 DÉPANNAGE

### Vignette affiche "Niveau unavailable"
1. Vérifier que l'intégration AtmoFrance (ou équivalente) est active et mise à jour.
2. L'API AtmoFrance peut être lente ou indisponible → attendre la prochaine mise à jour automatique.
3. Contrôler l'état des entités dans Outils Développeur > États → chercher `qualite_globale`.

### Couleur toujours `black`
La fonction `getColor()` retourne `'black'` si la valeur est hors de la plage 0-7. Vérifier que `sensor.qualite_globale_vence` retourne bien un entier (pas une chaîne textuelle).

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.qualite_globale_vence` | Intégration / Template | ✅ Essentiel |
| `sensor.qualite_globale_pollen_vence` | Intégration / Template | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Documentation
- `PAGE_POLLUTION_POLLEN.md` — *(à créer — page non encore fournie)*

---

← Retour : `L6C1_AIR_QUALITE/` | → Suivant : `L6C3_VIGIEAU/`
