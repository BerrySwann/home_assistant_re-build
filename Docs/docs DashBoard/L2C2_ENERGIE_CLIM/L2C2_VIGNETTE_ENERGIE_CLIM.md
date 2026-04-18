# L2C2 — VIGNETTE : Énergie Clim / Radiateur / Soufflant
*Dernière mise à jour : 2026-03-24*

---

## 📋 TABLE DES MATIÈRES

- [Description](#description)
- [Rendu visuel](#rendu-visuel)
- [Code source](#code-source)
- [Entités utilisées](#entités-utilisées--provenance-complète)
- [Logique JavaScript](#logique-javascript)
- [Paramètres clés](#paramètres-clés)
- [Dépannage](#dépannage)

---

## Description

**Type de carte :** `custom:button-card`
**Position dashboard :** L2C2 (Ligne 2, Colonne 2)
**tap_action :** Navigue vers `/dashboard-tablette/energie-clim`

Vignette carrée affichant la consommation énergétique des 6 appareils de chauffage/clim en 3 colonnes :

| Colonne | Contenu | Alignement |
|---------|---------|------------|
| `piece` | Nom de pièce colorisé selon état ON/OFF/mode | Gauche |
| `quotidien` | kWh du jour (reset minuit) | Droite |
| `mensuel` | kWh du mois (reset 1er du mois) | Droite |

**7 lignes affichées :** Salon / Cuisine / Bureau / SdB Sft / SdB SèS / Chambre / **TOTAL** (lightgreen, bold)

---

## Rendu visuel

```
╔══════════════════════════════╗
║     Consommation CLIM        ║
╠══════════╦══════════╦════════╣
║ Salon    ║  0.25kWh ║ 3.10kWh║  ← skyblue (cool ON)
║ Cuisine  ║   85 Wh  ║ 0.95kWh║  ← rgb(168,136,181) (heat ON)
║ Bureau   ║    0 Wh  ║    0kWh║  ← rouge (off_off : éteint)
║ SdB Sft  ║    0 Wh  ║    0kWh║  ← blanc (off)
║ SdB SèS  ║    0 Wh  ║   50 Wh║  ← blanc (off)
║ Chambre  ║ 1.20 kWh ║ 8.40kWh║  ← orange (heat ON)
╠══════════╬══════════╬════════╣
║ TOTAL    ║ 1.55 kWh ║12.95kWh║  ← lightgreen bold
╚══════════╩══════════╩════════╝
```

**Note :** Valeurs < 1 kWh affichées en Wh (×1000). Unité en `font-size: 5px` (discrète).

---

## Code source

```yaml
type: custom:button-card
entities:
  - climate.clim_salon_rm4_mini
  - climate.radiateur_cuisine
  - climate.clim_bureau_rm4_mini
  - climate.soufflant_salle_de_bain
  - climate.clim_chambre_rm4_mini
  - sensor.salon_power_status
  - sensor.cuisine_power_status
  - sensor.bureau_power_status
  - sensor.sdb_soufflant_etat
  - sensor.sdb_seche_serviette_etat
  - sensor.chambre_power_status
  - sensor.clim_salon_quotidien_kwh_um
  - sensor.radiateur_elec_cuisine_quotidien_kwh_um
  - sensor.clim_bureau_quotidien_kwh_um
  - sensor.soufflant_sdb_quotidien_kwh_um
  - sensor.seche_serviette_sdb_quotidien_kwh_um
  - sensor.clim_chambre_quotidien_kwh_um
  - sensor.conso_clim_rad_total_quotidien
  - sensor.clim_salon_mensuel_kwh_um
  - sensor.radiateur_elec_cuisine_mensuel_kwh_um
  - sensor.clim_bureau_mensuel_kwh_um
  - sensor.soufflant_sdb_mensuel_kwh_um
  - sensor.seche_serviette_sdb_mensuel_kwh_um
  - sensor.clim_chambre_mensuel_kwh_um
  - sensor.conso_clim_rad_total_mensuel
triggers_update:
  - climate.clim_salon_rm4_mini
  - climate.radiateur_cuisine
  - climate.clim_bureau_rm4_mini
  - climate.soufflant_salle_de_bain
  - climate.clim_chambre_rm4_mini
  - sensor.salon_power_status
  - sensor.cuisine_power_status
  - sensor.bureau_power_status
  - sensor.sdb_soufflant_etat
  - sensor.sdb_seche_serviette_etat
  - sensor.chambre_power_status
  - sensor.clim_salon_quotidien_kwh_um
  - sensor.radiateur_elec_cuisine_quotidien_kwh_um
  - sensor.clim_bureau_quotidien_kwh_um
  - sensor.soufflant_sdb_quotidien_kwh_um
  - sensor.seche_serviette_sdb_quotidien_kwh_um
  - sensor.clim_chambre_quotidien_kwh_um
  - sensor.conso_clim_rad_total_quotidien
  - sensor.clim_salon_mensuel_kwh_um
  - sensor.radiateur_elec_cuisine_mensuel_kwh_um
  - sensor.clim_bureau_mensuel_kwh_um
  - sensor.soufflant_sdb_mensuel_kwh_um
  - sensor.seche_serviette_sdb_mensuel_kwh_um
  - sensor.clim_chambre_mensuel_kwh_um
  - sensor.conso_clim_rad_total_mensuel
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/energie-clim
styles:
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
  grid:
    - grid-template-areas: |
        "titre titre titre"
        "piece quotidien mensuel"
    - grid-template-columns: 1fr 1fr 1fr
    - grid-template-rows: auto
    - margin-top: 4.5px
  custom_fields:
    titre:
      - grid-area: titre
      - justify-self: center
      - text-align: center
      - font-weight: bold
    piece:
      - justify-self: start
      - margin-left: 8px
      - text-align: left
    quotidien:
      - justify-self: start
      - margin-left: 8px
      - text-align: left
    mensuel:
      - justify-self: end
      - margin-right: 5px
      - text-align: right
custom_fields:
  titre: Consommation CLIM
  piece: |
    [[[
      const colorMap = {
        'off_off': 'rgb(244,67,54)',
        'on_cool': 'skyblue',
        'on_heat': '#FFA500',
        'on_fan': 'turquoise',
        'off': 'white',
        'on_off': '#aaaaaa'
      };
      function getColorForStatus(powerStatus, mode) {
        if (powerStatus === 'off') {
          return mode === 'off' ? colorMap['off_off'] : colorMap['off'];
        } else {
          return colorMap[`on_${mode}`] || colorMap['off'];
        }
      }
      function safeState(entityId) {
        return states[entityId]?.state?.toLowerCase() || 'off';
      }
      const pieces = [
        { name: 'Salon',   power: safeState('sensor.salon_power_status'),   mode: safeState('sensor.clim_salon_etat') },
        { name: 'Cuisine', power: safeState('sensor.cuisine_power_status'), mode: safeState('sensor.radiateur_cuisine_etat') },
        { name: 'Bureau',  power: safeState('sensor.bureau_power_status'),  mode: safeState('sensor.clim_bureau_etat') },
        { name: 'SdB Sft', power: safeState('sensor.sdb_soufflant_power_status'),       mode: safeState('sensor.sdb_soufflant_etat') },
        { name: 'SdB SèS', power: safeState('sensor.sdb_seche_serviette_power_status'), mode: safeState('sensor.sdb_seche_serviette_etat') },
        { name: 'Chambre', power: safeState('sensor.chambre_power_status'), mode: safeState('sensor.clim_chambre_etat') },
        { name: 'TOTAL', color: 'lightgreen', bold: true }
      ];
      return pieces.map(piece =>
        `<span style="display: block; text-align: left; line-height: 1.2; color: ${piece.color || getColorForStatus(piece.power, piece.mode)}; ${piece.bold ? 'font-weight: bold;' : ''}">${piece.name}</span>`
      ).join('');
    ]]]
  quotidien: |
    [[[
      const list = [
        'sensor.clim_salon_quotidien_kwh_um',
        'sensor.radiateur_elec_cuisine_quotidien_kwh_um',
        'sensor.clim_bureau_quotidien_kwh_um',
        'sensor.soufflant_sdb_quotidien_kwh_um',
        'sensor.seche_serviette_sdb_quotidien_kwh_um',
        'sensor.clim_chambre_quotidien_kwh_um',
        'sensor.conso_clim_rad_total_quotidien'
      ];
      return list.map((sensor, i) => {
        const s = states[sensor]?.state;
        const val = parseFloat(s);
        const isTotal = i === list.length - 1;
        if (s === 'unavailable' || s === 'unknown' || isNaN(val)) {
          let style = isTotal ? 'color: #aaaaaa; font-weight: bold;' : 'color: #aaaaaa;';
          return `<span style="display: block; text-align: right; line-height: 1.2; ${style}">N/A</span>`;
        }
        let unit = val < 1 ? 'Wh' : 'kWh';
        let displayVal = val < 1 ? (val * 1000).toFixed(0) : val.toFixed(2);
        let style = isTotal ? 'color: lightgreen; font-weight: bold;' : '';
        return `<span style="display: block; text-align: right; line-height: 1.2; ${style}">${displayVal} <span style="font-size: 5px;">${unit}</span></span>`;
      }).join('');
    ]]]
  mensuel: |
    [[[
      const list = [
        'sensor.clim_salon_mensuel_kwh_um',
        'sensor.radiateur_elec_cuisine_mensuel_kwh_um',
        'sensor.clim_bureau_mensuel_kwh_um',
        'sensor.soufflant_sdb_mensuel_kwh_um',
        'sensor.seche_serviette_sdb_mensuel_kwh_um',
        'sensor.clim_chambre_mensuel_kwh_um',
        'sensor.conso_clim_rad_total_mensuel'
      ];
      return list.map((sensor, i) => {
        const s = states[sensor]?.state;
        const val = parseFloat(s);
        const isTotal = i === list.length - 1;
        if (s === 'unavailable' || s === 'unknown' || isNaN(val)) {
          let style = isTotal ? 'color: #aaaaaa; font-weight: bold;' : 'color: #aaaaaa;';
          return `<span style="display: block; text-align: right; line-height: 1.2; ${style}">N/A</span>`;
        }
        let unit = val < 1 ? 'Wh' : 'kWh';
        let displayVal = val < 1 ? (val * 1000).toFixed(0) : val.toFixed(2);
        let style = isTotal ? 'color: lightgreen; font-weight: bold;' : '';
        return `<span style="display: block; text-align: right; line-height: 1.2; ${style}">${displayVal} <span style="font-size: 5px;">${unit}</span></span>`;
      }).join('');
    ]]]
```

---

## Entités utilisées — Provenance complète

### Entités `entities:` et `triggers_update:` (25 total)

| # | Entité | Type | Rôle | Fichier source |
|---|--------|------|------|----------------|
| 1 | `climate.clim_salon_rm4_mini` | NAT | Thermostat Salon | SmartIR |
| 2 | `climate.radiateur_cuisine` | NAT | Thermostat Cuisine | Meross |
| 3 | `climate.clim_bureau_rm4_mini` | NAT | Thermostat Bureau | SmartIR |
| 4 | `climate.soufflant_salle_de_bain` | NAT | Thermostat SdB Soufflant | Meross |
| 5 | `climate.clim_chambre_rm4_mini` | NAT | Thermostat Chambre | SmartIR |
| 6 | `sensor.salon_power_status` | TPL | ON/OFF Salon | `P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` |
| 7 | `sensor.cuisine_power_status` | TPL | ON/OFF Cuisine | idem |
| 8 | `sensor.bureau_power_status` | TPL | ON/OFF Bureau | idem |
| 9 | `sensor.sdb_soufflant_etat` | TPL | Mode Soufflant SdB | idem |
| 10 | `sensor.sdb_seche_serviette_etat` | TPL | Mode Sèche-Serv SdB | idem |
| 11 | `sensor.chambre_power_status` | TPL | ON/OFF Chambre | idem |
| 12 | `sensor.clim_salon_quotidien_kwh_um` | UM | kWh jour Salon | `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` |
| 13 | `sensor.radiateur_elec_cuisine_quotidien_kwh_um` | UM | kWh jour Cuisine | idem |
| 14 | `sensor.clim_bureau_quotidien_kwh_um` | UM | kWh jour Bureau | idem |
| 15 | `sensor.soufflant_sdb_quotidien_kwh_um` | UM | kWh jour SdB Sft | idem |
| 16 | `sensor.seche_serviette_sdb_quotidien_kwh_um` | UM | kWh jour SdB SèS | idem |
| 17 | `sensor.clim_chambre_quotidien_kwh_um` | UM | kWh jour Chambre | idem |
| 18 | `sensor.conso_clim_rad_total_quotidien` | TPL | TOTAL kWh jour | `P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| 19 | `sensor.clim_salon_mensuel_kwh_um` | UM | kWh mois Salon | `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` |
| 20 | `sensor.radiateur_elec_cuisine_mensuel_kwh_um` | UM | kWh mois Cuisine | idem |
| 21 | `sensor.clim_bureau_mensuel_kwh_um` | UM | kWh mois Bureau | idem |
| 22 | `sensor.soufflant_sdb_mensuel_kwh_um` | UM | kWh mois SdB Sft | idem |
| 23 | `sensor.seche_serviette_sdb_mensuel_kwh_um` | UM | kWh mois SdB SèS | idem |
| 24 | `sensor.clim_chambre_mensuel_kwh_um` | UM | kWh mois Chambre | idem |
| 25 | `sensor.conso_clim_rad_total_mensuel` | TPL | TOTAL kWh mois | `P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` |

### Entités accédées uniquement via JS `states[]` (NON dans `entities:`)

> ⚠️ Ces entités sont lues dynamiquement dans le JS du champ `piece` mais ne sont **pas déclarées** dans `entities:` ni `triggers_update:`. La mise à jour de la couleur dépend donc du refresh des autres entités listées.

| Entité | Rôle |
|--------|------|
| `sensor.clim_salon_etat` | Mode Salon (cool/heat/fan/off) |
| `sensor.radiateur_cuisine_etat` | Mode Cuisine (heat/off) |
| `sensor.clim_bureau_etat` | Mode Bureau (cool/heat/fan/off) |
| `sensor.sdb_soufflant_power_status` | ON/OFF SdB Soufflant |
| `sensor.sdb_seche_serviette_power_status` | ON/OFF SdB Sèche-Serv |
| `sensor.clim_chambre_etat` | Mode Chambre (cool/heat/fan/off) |

**Source :** `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml`

---

## Logique JavaScript

### 1. Colonne `piece` — ColorMap 5 états

```
powerStatus = 'off' + mode = 'off'  → rgb(244,67,54)  [ROUGE]    Éteint = hors tension
powerStatus = 'off' + mode ≠ 'off'  → 'white'          [BLANC]    Éteint = programmé/inactif
powerStatus = 'on'  + mode = 'cool' → 'skyblue'        [BLEU]     Climatisation froid
powerStatus = 'on'  + mode = 'heat' → '#FFA500'        [ORANGE]   Chauffage
powerStatus = 'on'  + mode = 'fan'  → 'turquoise'      [TURQUOISE] Ventilation
```

La ligne **TOTAL** ignore le colorMap : toujours `lightgreen` + `font-weight: bold`.

Fonction `safeState()` : renvoie `'off'` si l'entité est indisponible (protection NaN/crash).

### 2. Colonnes `quotidien` / `mensuel` — Basculement Wh ↔ kWh

```javascript
val < 1  → affiche en Wh  : (val × 1000).toFixed(0) + " Wh"
val ≥ 1  → affiche en kWh : val.toFixed(2) + " kWh"
unité : font-size: 5px (discrète, ne prend pas de place)
```

Si état = `'unavailable'`, `'unknown'` ou `NaN` → affiche `N/A` en `#aaaaaa`.

La ligne TOTAL (index 6 dans la liste) : `color: lightgreen; font-weight: bold`.

---

## Paramètres clés

| Paramètre | Valeur |
|-----------|--------|
| Type | `custom:button-card` |
| Aspect ratio | `1/1` (carré) |
| Border | `3px double white` |
| Font size | `11px` |
| Grid | 3 colonnes : `1fr 1fr 1fr` |
| Grid areas | `"titre titre titre" / "piece quotidien mensuel"` |
| tap_action | navigate → `/dashboard-tablette/energie-clim` |

---

## Dépannage

**Toutes les couleurs restent blanches :**
Vérifier que `sensor.*_power_status` et `sensor.*_etat` sont bien générés par `ui_dashboard.yaml`. Ces entités doivent retourner `'off'`, `'cool'`, `'heat'` ou `'fan'` (casse lowercase dans le JS).

**Valeurs N/A dans quotidien/mensuel :**
Les UM de `P1_UM_AMHQ.yaml` ne sont pas encore alimentés. Vérifier que les sensors `*_energie_totale_kwh` (Riemann) dans `sensors/P1_clim_chauffage/P1_DUT_clim_chauffage.yaml` sont actifs.

**SdB Sft/SèS ne changent pas de couleur malgré l'appel :**
`sensor.sdb_soufflant_power_status` et `sensor.sdb_seche_serviette_power_status` ne sont **pas dans `entities:`**. Si ces sensors changent d'état sans qu'une autre entité listed déclenche un refresh, la vignette ne se mettra pas à jour. Solution : les ajouter à `entities:` et `triggers_update:`.

**TOTAL reste à 0 :**
Vérifier `sensor.conso_clim_rad_total_quotidien` et `sensor.conso_clim_rad_total_mensuel` dans `P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml`. Ces entités agrègent les 6 UM.

---

## Fichiers liés

| Fichier | Rôle |
|---------|------|
| `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` | Compteurs UM Q/H/M/A (source kWh) |
| `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Templates power_status + etat |
| `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` | TOTAL quotidien + mensuel kWh |
| `sensors/P1_clim_chauffage/P1_DUT_clim_chauffage.yaml` | Intégration Riemann (kWh source UM) |


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_ENERGIE_CLIM]]  [[L1C3_VIGNETTE_CLIM]]  [[L2C1_VIGNETTE_ENERGIE]]  [[L2C3_VIGNETTE_ECLAIRAGE]]*
