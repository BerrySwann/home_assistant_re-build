<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--24-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `docs/02_docs_dashboard/02_dashboard_docs_yaml/L5C1_PILES_BATTERIES/L5C1_PILES_BATTERIES_02_Page/L5C1_Page_PILES_BATTERIES.yaml` |
| 🔗 **Accès depuis** | Tap vignette L5C1 → `/dashboard-tablette/battery-bp` |
| 🔗 **Retour vers** | Tap header → `/dashboard-tablette/0` |
| 🏗️ **Layout** | `type: grid` - 4 cartes `battery-state-card` (une par type, chacune precedee d'un en-tete) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-24 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

---

# 🔋 PAGE BATTERIES - DÉTAIL PAR TYPE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Structure commune](#structure-commune)
4. [Section 1 - Boutons HUE](#section-1--boutons-hue)
5. [Section 2 - Boutons & détecteurs IKEA](#section-2--boutons--détecteurs-ikea)
6. [Section 3 - Contacts fenêtres SONOFF](#section-3--contacts-fenêtres-sonoff)
7. [Section 4 - Thermostats SONOFF](#section-4--thermostats-sonoff)
8. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page complète listant tous les équipements à batterie, découpée en 4 sections par type/marque. Chaque section affiche un collapse avec le niveau minimum et la plage, triée par niveau croissant. Dégradé rouge → jaune → vert.

### Cartes HACS

| Carte | Usage |
|-------|-------|
| `custom:battery-state-card` | 4 sections indépendantes |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────────────┐
│  HEADER - "BATTERIES (Boutons / Thermostats…)"      │
│  tap → /dashboard-tablette/0                        │
├─────────────────────────────────────────────────────┤
│  [1] Boutons HUE              11 entités            │
│      collapse · mdi:light-switch                    │
├─────────────────────────────────────────────────────┤
│  [2] Boutons & détect. IKEA    9 entités            │
│      collapse · mdi:hammer-screwdriver              │
├─────────────────────────────────────────────────────┤
│  [3] Contacts fenêtres SONOFF  4 entités            │
│      collapse · mdi:window-closed-variant           │
├─────────────────────────────────────────────────────┤
│  [4] Thermostats SONOFF        9 entités            │
│      collapse · mdi:thermometer                     │
└─────────────────────────────────────────────────────┘
```

---

## 📍 STRUCTURE COMMUNE

Chaque section suit le même schéma - seuls le `heading`, l'icône du collapse et la liste d'entités varient.

### Blocs identiques dans les 4 sections

```yaml
secondary_info: "{last_changed}"
colors:
  steps:
    - "#ff0000"
    - "#ffff00"
    - "#00ff00"
  gradient: true
filter:
  exclude:
    - name: entity_id
      value: sensor.ne2213_*
    - name: entity_id
      value: sensor.gm1901_battery_level
    - name: entity_id
      value: sensor.sm_a530f_battery_level
    - name: entity_id
      value: sensor.tablette_battery_level
sort:
  by: state
bulk_rename:
  - from: " Batterie"
  - from: " Battery"
  - from: " level"
  - from: " (HUE)"
  - from: Hue Smart
  - from: button
    to: Bouton
  - from: Th
    to: Thermostat
card_mod:
  style: |
    ha-card {
      background: none !important;
      box-shadow: none !important;
      border: none !important;
    }
style: '.groupItems { max-height: 2000px !important; }'
```

> Cle `style` ajoutee le 2026-10-24 (R80) sur les 4 cartes : contournement du bug de battery-state-card 4.2.0 qui tronque la derniere ligne du groupe deplie (hauteur max = nombre de batteries x 50 px). A retirer quand une release corrige le bug (R107). Voir Depannage.

---

## 📍 SECTION 1 - Boutons HUE

### Collapse
`"Boutons HUE (Total : {count} / Mini. : {min} %)"` · `mdi:light-switch`

### Entités (11) · Philips Hue [bridge natif]

| Entité | Pièce |
|--------|-------|
| `sensor.hue_smart_button_entree_1_batterie` | Entrée 1 |
| `sensor.hue_smart_button_entree_2_batterie` | Entrée 2 |
| `sensor.hue_smart_button_eco_batterie` | Eco |
| `sensor.hue_smart_button_table_batterie` | Table salon |
| `sensor.hue_smart_button_cuisine_batterie` | Cuisine |
| `sensor.hue_smart_button_couloir_batterie` | Couloir |
| `sensor.hue_smart_button_bureau_batterie` | Bureau |
| `sensor.hue_smart_button_salle_de_bain_batterie` | SDB |
| `sensor.hue_smart_button_chambre_batterie` | Chambre |
| `sensor.hue_smart_button_chambre_gege_batterie` | Chambre Gege |
| `sensor.hue_smart_button_chambre_eric_batterie` | Chambre Eric |

---

## 📍 SECTION 2 - Boutons & détecteurs IKEA

### Collapse
`"Capteurs IKEA (Total : {count} / Mini. : {min} %)"` · `mdi:hammer-screwdriver`

### Entités (9) · Zigbee2MQTT [Z2M]

| Entité | Type |
|--------|------|
| `sensor.poussoir_tv_ikea_tradfri_battery` | Poussoir TV chambre |
| `sensor.inter_bureau_rodret_battery` | Inter RODRET bureau |
| `sensor.inter_somrig_battery` | Inter SOMRIG |
| `sensor.inter_salon_4_ikea_battery` | Inter salon |
| `sensor.detecteur_de_fuite_ikea_battery` | Détecteur de fuite |
| `sensor.detecteur_ikea_vallhorn_battery` | Détecteur VALLHORN |
| `sensor.poussoir_pc_ikea_tradfri_battery` | Poussoir PC bureau |
| `sensor.inter_soufflant_salle_de_bain_ikea_rodret_battery` | Inter soufflant SDB |
| `sensor.inter_reserve_ikea_rodret_battery` | Inter RODRET reserve (deduit du nom de l'entite) |

---

## 📍 SECTION 3 - Contacts fenêtres SONOFF

### Collapse
`"Contacts de fenêtres SONOFF (Total : {count} / Mini. : {min} %)"` · `mdi:window-closed-variant`

### Entités (4) · Zigbee2MQTT [Z2M]

| Entité | Pièce |
|--------|-------|
| `sensor.contact_fenetre_salon_sonoff_battery` | Salon |
| `sensor.contact_fenetre_cuisine_sonoff_battery` | Cuisine |
| `sensor.contact_fenetre_bureau_sonoff_battery` | Bureau |
| `sensor.contact_fenetre_chambre_sonoff_battery` | Chambre |

---

## 📍 SECTION 4 - Thermostats SONOFF

### Collapse
`"Thermostats SONOFF (Total : {count} / Mini. : {min} %)"` · `mdi:thermometer`

### Entités (9) · Zigbee2MQTT [Z2M]

| Entité | Pièce |
|--------|-------|
| `sensor.th_balcon_nord_battery` | Balcon Nord (T° ext) |
| `sensor.th_salon_battery` | Salon |
| `sensor.th_cellier_battery` | Cellier |
| `sensor.th_cuisine_battery` | Cuisine |
| `sensor.th_bureau_battery` | Bureau |
| `sensor.th_salle_de_bain_battery` | SDB |
| `sensor.th_chambre_battery` | Chambre |
| `sensor.tongel_battery` | Congélateur (sonde Tongel) *(ajout 2026-09-24)* |
| `sensor.porte_congel_battery` | Congélateur (contact porte) *(ajout 2026-09-24)* |

> Renommages en place (2026-09-24) : `Tongel` → `Thermostat Congél.`, `Porte Congel` → `Porte Congél.`

---

## 🐛 DÉPANNAGE

### "Custom element doesn't exist: battery-state-card"
Nom HACS exact : `battery-state-card` (pas `batterie-state-card`). Vider le cache navigateur après installation.

### Une section affiche des appareils d'une autre section
Les `filter/exclude` ne filtrent que les entités exclues - les entités d'une section peuvent apparaître dans une autre si elles ne sont pas dans le collapse. Vérifier que chaque entité est bien listée dans **une seule** section.

### Le groupe deplie est tronque (derniere ligne coupee)
Bug de battery-state-card 4.2.0 : la hauteur du groupe deplie est figee a (nombre de batteries x 50 px), alors qu'une ligne avec `secondary_info` fait environ 52 px. Contournement en place (R80) : cle `style: '.groupItems { max-height: 2000px !important; }'` sur chaque carte. Le correctif amont (PR #934 de battery-state-card) est fusionne sur master depuis le 2026-10-12 mais pas encore publie. Quand une release le contient : mettre la carte a jour puis retirer la cle (R107). Si un groupe parait bizarre apres la mise a jour, c'est ce contournement qui n'est plus utile, pas un nouveau bug.

---

## 📝 DÉPENDANCES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:battery-state-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

- `docs/02_docs_dashboard/02_dashboard_docs_yaml/L5C1_PILES_BATTERIES/L5C1_PILES_BATTERIES_02_Page/L5C1_Page_PILES_BATTERIES.yaml`
- `docs/02_docs_dashboard/02_dashboard_docs_yaml/L5C1_PILES_BATTERIES/L5C1_PILES_BATTERIES_01_Vignette/L5C1_Vignette_PILES_BATTERIES.yaml` (vignette - inchangée)
- `docs/02_docs_dashboard/02_dashboard_docs_md/L5C1_PILES_BATTERIES/L5C1_PILES_BATTERIES_01_Vignette/L5C1_Vignette_PILES_BATTERIES.md`

---

← Retour : `L5C1_Vignette_PILES_BATTERIES.md` | → Suivant : -


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L5C1_Vignette_PILES_BATTERIES]]*

<!-- annotations_log:
[2026-10-24] Alignement sur le yaml prod synchronise (L5C1_Page_PILES_BATTERIES.yaml, md5 ac255846) : 5 sections -> 4 cartes ; section 3 Contacts fenetres IKEA retiree (absente du yaml prod) et sections suivantes renumerotees ; section 2 IKEA 8 -> 9 entites (ajout sensor.inter_reserve_ikea_rodret_battery) ; cle style R80 documentee (bloc commun + depannage, voir R107) ; dates mises a jour, demande d'Eric 15:19. Non corrige : ligne Path du tableau d'en-tete (ancien nom de fichier 2026-09-24).
[2026-10-24] Chemins corriges (ligne Path du tableau d'en-tete + 3 lignes de FICHIERS LIES : anciens noms de fichiers remplaces par les chemins reels sous docs/02_docs_dashboard), accord d'Eric 15:24 
[2026-10-24] R83 / L5C1 : entity_id Hue d'entree renommes entee -> entree (Hue Smart button Entree 1 et 2), apres renommage dans HA, accord d'Eric 15:42 -->
