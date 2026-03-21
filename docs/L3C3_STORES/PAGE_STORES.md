<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-03a9f4?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord_2026-03-*.yaml → Vue: stores → section[0]` |
| 🔗 **Accès depuis** | Vignette L3C3 tap → `/dashboard-tablette/stores` |
| 🏗️ **Type carte** | `type: grid` (section unique, `max_columns: 1`) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3.x |

---

# 🪟 L3C3 — Page : Stores & Fenêtres

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Section STORE SALON](#section-store-salon)
4. [Section STORE BUREAU](#section-store-bureau)
5. [Logique de position des boutons](#logique-de-position-des-boutons)
6. [Entité DnD (light.store_*_dnd)](#entité-dnd-lightstore_dnd)
7. [Entités utilisées](#entités-utilisées)
8. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page secondaire dédiée à la commande complète des deux stores motorisés (Salon et Bureau). Chaque store dispose de sa propre section avec :

- **Conditions d'automatisation** affichées (T° balcon + règle logique)
- **État de la fenêtre** (contact Zigbee) en badge en-tête
- **enhanced-shutter-card** : visuel animé du store avec position en temps réel
- **Affichage textuel** de l'état (ex: "Salon : Ouvert")
- **5 boutons de position rapide** : 100% / 75% / 50% / 25% / 10%
- **Interrupteur DnD** (voyants de commande physique)

Retour vers la vue principale via tap sur le heading STORES.

### Intégrations requises

- ✅ **Zigbee2MQTT** — `cover.store_salon` / `cover.store_bureau`
- ✅ **SONOFF SNZB-04** (Zigbee) — contacts fenêtres
- ✅ **Templates** — `sensor.store_*_status`, `sensor.store_*_signal_strength`
- ✅ **SONOFF SNZB-02** — `sensor.th_balcon_nord_temperature`
- ✅ **Entité virtuelle** — `light.store_*_dnd` (helper)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:enhanced-shutter-card` | Visuel animé du store (position, lames) |
| `custom:button-card` | État textuel + boutons de position |
| `custom:mushroom-light-card` | Interrupteur DnD (voyants commandes physiques) |
| `custom:stack-in-card` | Groupement sections CONDITIONS et STORE * |
| `custom:mod-card` | Styles CSS inline sur `text-divider-row` |
| `custom:text-divider-row` | Séparateurs de sections textuels |
| `custom:streamline-card` | Navigation bar en bas de page |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌──────────────────────────────────────────────────────────┐
│  STORES (heading)                          tap → /0      │
├──────────────────────────────────────────────────────────┤
│  ── CONDITIONS ──────────────────────────────────────    │
│  Auto close at +34°  [T° balcon badge]                   │
├──────────────────────────────────────────────────────────┤
│  ── STORE SALON ─────────────────────────────────────    │
│  Fenêtre Salon  [état contact]  [batterie]               │  ← heading
│  ┌─ enhanced-shutter-card (cover.store_salon) ─────────┐ │
│  │  (visuel animé, position en temps réel)              │ │
│  └──────────────────────────────────────────────────────┘ │
│  "Salon : Ouvert"  (button-card état textuel)            │
│  [ 100% ]  [ 75% ]  [ 50% ]  [ 25% ]  [ 10% ]           │  ← 5 boutons
│  Store Salon (Voyants commandes)  [mushroom toggle DnD]  │
├──────────────────────────────────────────────────────────┤
│  STORES (heading)                          tap → /0      │
├──────────────────────────────────────────────────────────┤
│  ── CONDITIONS ──────────────────────────────────────    │
│  Auto open at +18° or auto close at +25°  [T° badge]    │
├──────────────────────────────────────────────────────────┤
│  ── STORE BUREAU ────────────────────────────────────    │
│  Fenêtre Bureau  [état contact]  [batterie]              │  ← heading
│  ┌─ enhanced-shutter-card (cover.store_bureau) ────────┐ │
│  │  (visuel animé, position en temps réel)              │ │
│  └──────────────────────────────────────────────────────┘ │
│  "Bureau : Ouvert"  (button-card état textuel)           │
│  [ 100% ]  [ 75% ]  [ 50% ]  [ 25% ]  [ 10% ]           │  ← 5 boutons
│  Store Bureau (Voyants commandes)  [mushroom toggle DnD] │
├──────────────────────────────────────────────────────────┤
│  [nav_bar streamline]                                    │
└──────────────────────────────────────────────────────────┘
```

> **Note** : Le heading `STORES` apparaît deux fois dans le YAML (une fois par section store). Cela permet à chaque section de fonctionner de façon autonome sur la page.

---

## 🎚️ SECTION STORE SALON

### Conditions d'automatisation

La condition affichée sur la page correspond à la règle d'automatisation réelle du volet Salon :

> **Auto close at +34°C** — le store se ferme automatiquement si la T° extérieure (balcon Nord) dépasse 34°C.

Badge : `sensor.th_balcon_nord_temperature` (température en temps réel).

### Fenêtre Salon

Heading avec deux badges :
- `binary_sensor.contact_fenetre_salon_sonoff_contact` — état de la fenêtre (`on` = ouvert / `off` = fermé)
- `sensor.contact_fenetre_salon_sonoff_battery` — niveau pile du capteur (tap → more-info)

### Enhanced-Shutter-Card

```yaml
type: custom:enhanced-shutter-card
entities:
  - entity: cover.store_salon
    name: Salon
    name_disabled: true
    opening_disabled: true
    passive_mode: false
    resize_height_pct: 100
    resize_width_pct: 130
    title_position: bottom
    opening_position: bottom
    inline_header: true
    view_image: " "
    buttons_position: left
    signal_entity: sensor.store_salon_signal_strength
    shutter_slat_image: esc-shutter-slat.png
    shutter_bottom_image: esc-shutter-bottom.png
```

- `opening_disabled: true` — bouton d'ouverture natif de la carte désactivé (remplacé par les boutons personnalisés)
- `signal_entity` — affiche la qualité du signal Zigbee du store
- `shutter_slat_image` / `shutter_bottom_image` — images personnalisées des lames et bord bas

### État textuel (button-card)

```yaml
state_display: |
  [[[
    return 'Salon : ' + entity.state;
  ]]]
```

Affiche l'état brut du `sensor.store_salon_status` préfixé par `"Salon : "`.

### Boutons de position rapide

5 boutons `cover.set_cover_position` avec mapping spécifique (voir [Logique de position](#logique-de-position-des-boutons)).

### Interrupteur DnD

```yaml
type: custom:mushroom-light-card
entity: light.store_salon_dnd
```

Toggle pour activer/désactiver les voyants LED de la télécommande physique du store (voir [Entité DnD](#entité-dnd-lightstore_dnd)).

---

## 🎚️ SECTION STORE BUREAU

### Conditions d'automatisation

> **Auto open at +18° or auto close at +25°C** — le store Bureau s'ouvre automatiquement si la T° ext est entre 18°C et 25°C, et se ferme au-delà de 25°C. (Logique inversée par rapport au Salon — fenêtre thermique optimale pour le bureau Nord.)

Badge : `sensor.th_balcon_nord_temperature`.

### Fenêtre Bureau

Heading avec deux badges :
- `binary_sensor.contact_fenetre_bureau_sonoff_contact` — état fenêtre (+ icône `mdi:door-open`)
- `sensor.contact_fenetre_bureau_sonoff_battery` — pile (tap → more-info)

### Enhanced-Shutter-Card

Identique au Salon avec `cover.store_bureau` et `sensor.store_bureau_signal_strength`.

### État textuel

```yaml
state_display: |
  [[[
    return 'Bureau : ' + entity.state;
  ]]]
```

### Boutons de position rapide

5 boutons avec mapping spécifique Bureau (voir ci-dessous).

### Interrupteur DnD

```yaml
entity: light.store_bureau_dnd
```

---

## 📐 LOGIQUE DE POSITION DES BOUTONS

Les boutons affichent un pourcentage "logique" (perception visuelle) mais envoient une position différente à HA car le store a une mécanique non linéaire.

### Store Salon (`cover.store_salon`)

| Label affiché | Position HA envoyée | Notes |
|:-------------|:--------------------|:------|
| `100%` | `100` | Ouvert complet |
| `75%` | `85` | Partiellement ouvert |
| `50%` | `70` | Mi-course |
| `25%` | `49` | Presque fermé |
| `10%` | `20` | Entrebâillé / occultant |

### Store Bureau (`cover.store_bureau`)

| Label affiché | Position HA envoyée | Notes |
|:-------------|:--------------------|:------|
| `100%` | `100` | Ouvert complet |
| `75%` | `90` | Partiellement ouvert |
| `50%` | `60` | Mi-course |
| `25%` | `45` | Presque fermé |
| `10%` | `25` | Entrebâillé / occultant |

> ⚠️ Les positions exactes ont été calibrées empiriquement pour correspondre à la perception visuelle. Les valeurs diffèrent entre Salon et Bureau en raison de mécaniques différentes.

---

## 💡 ENTITÉ DnD (`light.store_*_dnd`)

`light.store_salon_dnd` et `light.store_bureau_dnd` sont des entités **helper de type light** (ou input_boolean exposé comme light) utilisées pour contrôler les **voyants LED de la télécommande physique** du store (mode "Ne pas déranger").

- **ON** : les voyants de la télécommande s'allument (commandes physiques actives)
- **OFF** : les voyants sont éteints (télécommande silencieuse / DnD)

Affichées via `custom:mushroom-light-card` avec icône `phu:roller-shutter-switch`.

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Covers (stores motorisés)

| Entité | Store | Source |
|:-------|:------|:-------|
| `cover.store_salon` | Volet Salon | Zigbee2MQTT [NAT] |
| `cover.store_bureau` | Volet Bureau | Zigbee2MQTT [NAT] |

### Binary sensors (contacts fenêtres)

| Entité | Pièce | Matériel | Source |
|:-------|:------|:---------|:-------|
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | Salon | SONOFF SNZB-04 | Zigbee [NAT] |
| `binary_sensor.contact_fenetre_cuisine_sonoff_contact` | Cuisine | SONOFF SNZB-04 | Zigbee [NAT] |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | Bureau | SONOFF SNZB-04 | Zigbee [NAT] |
| `binary_sensor.contact_fenetre_chambre_sonoff_contact` | Chambre | SONOFF SNZB-04 | Zigbee [NAT] |

### Batteries contacts

| Entité | Pièce | Source |
|:-------|:------|:-------|
| `sensor.contact_fenetre_salon_sonoff_battery` | Salon | Zigbee [NAT] |
| `sensor.contact_fenetre_bureau_sonoff_battery` | Bureau | Zigbee [NAT] |

### Sensors templates (statut + signal)

| Entité | Rôle | Source |
|:-------|:-----|:-------|
| `sensor.store_salon_status` | Texte état store Salon | [TPL] à préciser |
| `sensor.store_bureau_status` | Texte état store Bureau | [TPL] à préciser |
| `sensor.store_salon_signal_strength` | Signal Zigbee Salon | Zigbee2MQTT [NAT] |
| `sensor.store_bureau_signal_strength` | Signal Zigbee Bureau | Zigbee2MQTT [NAT] |

### Température extérieure

| Entité | Rôle | Source |
|:-------|:-----|:-------|
| `sensor.th_balcon_nord_temperature` | T° ext balcon (condition affichée) | SONOFF SNZB-02 [NAT] |

### Helpers DnD

| Entité | Store | Type | Source |
|:-------|:------|:-----|:-------|
| `light.store_salon_dnd` | Salon | Helper light / virtual | [NAT UI] |
| `light.store_bureau_dnd` | Bureau | Helper light / virtual | [NAT UI] |

---

## 🐛 DÉPANNAGE

### Le store ne répond pas aux boutons de position
1. Vérifier que `cover.store_salon` / `cover.store_bureau` est disponible (Zigbee2MQTT actif)
2. Vérifier le signal : `sensor.store_*_signal_strength` — si faible, rapprocher le coordinateur Zigbee
3. Tester via Outils développeur → Services → `cover.set_cover_position`

### La enhanced-shutter-card n'affiche pas le visuel
→ Vérifier que les images `esc-shutter-slat.png` et `esc-shutter-bottom.png` sont bien dans `/config/www/` (ou le chemin configuré dans `enhanced-shutter-card`)

### L'état textuel affiche "undefined" ou une erreur
→ Vérifier que `sensor.store_*_status` existe et est disponible. C'est un template — vérifier dans Outils développeur → États.

### Le DnD ne bascule pas
→ `light.store_*_dnd` doit être un helper HA existant. Vérifier dans Paramètres → Appareils → Helpers.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:enhanced-shutter-card` | HACS | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |
| `custom:mushroom-light-card` | HACS | ✅ Essentiel |
| `custom:stack-in-card` | HACS | ✅ Structure |
| `custom:mod-card` | HACS | ✅ Style séparateurs |
| `custom:text-divider-row` | HACS | ✅ Séparateurs |
| `custom:streamline-card` | HACS | ✅ Nav bar |
| `cover.store_salon` / `cover.store_bureau` | Zigbee2MQTT | ✅ Essentiel |
| `binary_sensor.contact_fenetre_*` × 4 | SONOFF SNZB-04 | ✅ Essentiel |
| `sensor.store_*_status` × 2 | Templates | ✅ Requis |
| `light.store_*_dnd` × 2 | Helper HA | ✅ Requis |
| Images ESC (`esc-shutter-*.png`) | `/config/www/` | ✅ Requis |

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin |
|------|--------|
| Vignette L3C3 | `docs/L3C3_STORES/L3C3_VIGNETTE_STORES.md` |
| Page YAML | `dashbord/page_stores.yaml` |
| Automatisation volet Salon | `automations.yaml` (condition T° > 34°C) |
| Automatisation volet Bureau | `automations.yaml` (condition T° 18–25°C) |

---

← Retour : `docs/L3C3_STORES/L3C3_VIGNETTE_STORES.md` | → Suivant : `docs/L4C1_*/`
