# L4C2 — VIGNETTE : Mini PC
*Dernière mise à jour : 2026-05-03*

> ✅ **STATUT : DÉPLOYÉE — Mini PC Intel NUC en production.**
> Entité principale : `sensor.temperature_cpu_package` (commande linux `sensors`).
> Navigation : `/dashboard-tablette/systeme-mini-pc` (page Mini PC définitive).

---

## 📋 TABLE DES MATIÈRES

- [Description](#description)
- [Rendu visuel](#rendu-visuel)
- [Code source](#code-source)
- [Entités utilisées](#entités-utilisées--provenance-complète)
- [Logique JavaScript — seuils couleur](#logique-javascript--seuils-couleur)
- [Paramètres clés](#paramètres-clés)
- [Dépannage](#dépannage)

---

## Description

**Type de carte :** `custom:button-card`
**Position dashboard :** L4C2 (Ligne 4, Colonne 2)
**tap_action :** Navigue vers `/dashboard-tablette/systeme-mini-pc`

Vignette carrée affichant 5 métriques système du Mini PC (via intégration `system_monitor` + `sensors` Linux) + consommation de la prise IKEA :

| Zone grille | Contenu |
|-------------|---------|
| `i` | Icône NUC (`phu:intel-nuc`) — couleur selon T° CPU |
| `temp` | T° CPU avec icône thermomètre — couleur selon seuils |
| `n` | Nom : `_____ Mini - P.C. _____` (bold) |
| `cpu` | CPU % — icône server vert fixe |
| `conso` | Power W (prise IKEA) — icône lightning vert fixe |
| `ram` | RAM % — icône memory vert fixe |
| `sd` | Disk % — icône harddisk vert fixe |

---

## Rendu visuel

```
╔══════════════════════════════╗
║  [NUC]🟢      🌡️ 48°C 🟢    ║
║     _____ Mini - P.C. _____  ║
║  🖥️ CPU:  23%                ║
║  ⚡ Power: 11W               ║
║  💾 RAM:  58%                ║
║  💿 SD:   41%                ║
╚══════════════════════════════╝

États couleur (icône NUC + temp):
  < 65°C → 🟢 rgb(70,175,75)
  65–74°C → 🟠 orange
  ≥ 75°C → 🔴 rgb(244,67,54)
```

---

## Code source

```yaml
type: custom:button-card
entity: sensor.temperature_cpu_package
icon: phu:intel-nuc
aspect_ratio: 1/1
name: _____ Mini - P.C. _____
entities:
  - sensor.temperature_cpu_package
  - sensor.system_monitor_utilisation_du_processeur
  - sensor.system_monitor_utilisation_de_la_memoire
  - sensor.system_monitor_utilisation_du_disque
  - sensor.prise_mini_pc_ikea_power
triggers_update:
  - sensor.temperature_cpu_package
  - sensor.system_monitor_utilisation_du_processeur
  - sensor.system_monitor_utilisation_de_la_memoire
  - sensor.system_monitor_utilisation_du_disque
  - sensor.prise_mini_pc_ikea_power
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/systeme-mini-pc
styles:
  card:
    - border-radius: 10px
    - background: transparent
    - border-width: 3px
    - border-color: white
    - border-style: double
    - color: white
    - font-size: 11px
    - line-height: 1.2
    - padding: 3%
  grid:
    - grid-template-areas: |
        "i temp"
        "n n"
        "cpu cpu"
        "conso conso"
        "ram ram"
        "sd sd"
  name:
    - font-weight: bold
    - font-size: 13px
    - color: white
    - align-self: middle
    - justify-self: center
    - padding-bottom: 7px
  icon:
    - color: |
        [[[
          if (!entity || entity.state === 'unavailable' || entity.state === 'unknown') return '#aaaaaa';
          const t = parseFloat(entity.state);
          if (t < 65) return 'rgb(70, 175, 75)';
          if (t < 75) return 'orange';
          return 'rgb(244,67,54)';
        ]]]
    - width: 100%
  custom_fields:
    temp:
      - align-self: start
      - margin-top: 18px
      - margin-right: 10px
      - "--text-icon-sensor": |
          [[[
            if (entity.state < 65) return 'rgb(70, 175, 75)';
            if (entity.state >= 65 && entity.state < 75) return 'orange';
            else return 'rgb(244,67,54)';
          ]]]
      - "--text-color-sensor": |
          [[[
            if (entity.state < 65) return 'rgb(255,255,255)';
            if (entity.state >= 65 && entity.state < 75) return 'orange';
            else return 'rgb(244,67,54)';
          ]]]
    cpu:
      - padding-bottom: 1px
      - align-self: middle
      - justify-self: start
      - "--text-color-sensor": |
          [[[
            const stateObj = states["sensor.system_monitor_utilisation_du_processeur"];
            if (!stateObj || stateObj.state === 'unavailable' || stateObj.state === 'unknown') return '#aaaaaa';
            let val = parseFloat(stateObj.state);
            if (val < 75) return 'white';
            if (val >= 75 && val < 90) return 'orange';
            else return 'rgb(244,67,54)';
          ]]]
    conso:
      - padding-bottom: 1px
      - align-self: middle
      - justify-self: start
      - "--text-color-sensor": |
          [[[
            const stateObj = states["sensor.prise_mini_pc_ikea_power"];
            if (!stateObj || stateObj.state === 'unavailable' || stateObj.state === 'unknown') return '#aaaaaa';
            let val = parseFloat(stateObj.state);
            if (val < 15) return 'white';
            if (val >= 15 && val < 19) return 'orange';
            else return 'rgb(244,67,54)';
          ]]]
    ram:
      - padding-bottom: 1px
      - align-self: middle
      - justify-self: start
      - "--text-color-sensor": |
          [[[
            const stateObj = states["sensor.system_monitor_utilisation_de_la_memoire"];
            if (!stateObj || stateObj.state === 'unavailable' || stateObj.state === 'unknown') return '#aaaaaa';
            let val = parseFloat(stateObj.state);
            if (val < 75) return 'white';
            if (val >= 75 && val < 90) return 'orange';
            else return 'rgb(244,67,54)';
          ]]]
    sd:
      - padding-bottom: 0px
      - align-self: middle
      - justify-self: start
      - "--text-color-sensor": |
          [[[
            const stateObj = states["sensor.system_monitor_utilisation_du_disque"];
            if (!stateObj || stateObj.state === 'unavailable' || stateObj.state === 'unknown') return '#aaaaaa';
            let val = parseFloat(stateObj.state);
            if (val < 75) return 'white';
            if (val >= 75 && val < 90) return 'orange';
            else return 'rgb(244,67,54)';
          ]]]
custom_fields:
  temp: |
    [[[
      return `<ha-icon icon="mdi:thermometer" style="width: 15px; height: 15px; color: var(--text-icon-sensor);"></ha-icon> <span style="color: var(--text-color-sensor);">${entity.state}°C</span>`
    ]]]
  cpu: |
    [[[
      const stateObj = states['sensor.system_monitor_utilisation_du_processeur'];
      const val = (stateObj && stateObj.state !== 'unavailable' && stateObj.state !== 'unknown') ? stateObj.state + '%' : 'N/A';
      return `<ha-icon icon="mdi:server" style="width: 15px; height: 15px; color: rgb(70, 175, 75);"></ha-icon><span>CPU: <span style="color: var(--text-color-sensor);">${val}</span></span>`
    ]]]
  conso: |
    [[[
      const stateObj = states['sensor.prise_mini_pc_ikea_power'];
      const val = (stateObj && stateObj.state !== 'unavailable' && stateObj.state !== 'unknown') ? stateObj.state + 'W' : 'N/A';
      return `<ha-icon icon="mdi:lightning-bolt-outline" style="width: 15px; height: 15px; color: rgb(70, 175, 75);"></ha-icon><span>Power: <span style="color: var(--text-color-sensor);">${val}</span></span>`
    ]]]
  ram: |
    [[[
      const stateObj = states['sensor.system_monitor_utilisation_de_la_memoire'];
      const val = (stateObj && stateObj.state !== 'unavailable' && stateObj.state !== 'unknown') ? stateObj.state + '%' : 'N/A';
      return `<ha-icon icon="mdi:memory" style="width: 15px; height: 15px; color: rgb(70, 175, 75);"></ha-icon><span>RAM: <span style="color: var(--text-color-sensor);">${val}</span></span>`
    ]]]
  sd: |
    [[[
      const stateObj = states['sensor.system_monitor_utilisation_du_disque'];
      const val = (stateObj && stateObj.state !== 'unavailable' && stateObj.state !== 'unknown') ? stateObj.state + '%' : 'N/A';
      return `<ha-icon icon="mdi:harddisk" style="width: 15px; height: 15px; color: rgb(70, 175, 75);"></ha-icon><span>SD: <span style="color: var(--text-color-sensor);">${val}</span></span>`
    ]]]
```

---

## Entités utilisées — Provenance complète

| Entité | Type | Rôle | Source |
|--------|------|------|--------|
| `sensor.temperature_cpu_package` | MQTT | T° CPU Package (°C) — entité principale | Script `lm-sensors` (VM) → MQTT |
| `sensor.system_monitor_utilisation_du_processeur` | NAT | CPU % | Intégration `system_monitor` (HA) |
| `sensor.system_monitor_utilisation_de_la_memoire` | NAT | RAM % | Intégration `system_monitor` |
| `sensor.system_monitor_utilisation_du_disque` | NAT | Disk % (VM ~30 GiB) | Intégration `system_monitor` |
| `sensor.prise_mini_pc_ikea_power` | NAT | Puissance W (prise IKEA Inspelning) | Intégration Zigbee2MQTT / IKEA |

> **Note T° :** `sensor.temperature_cpu_package` est publié via MQTT par un script `lm-sensors` tournant dans la VM. `system_monitor` ne remonte aucune T° en contexte VM Proxmox.

---

## Logique JavaScript — Seuils couleur

### Icône NUC + champ `temp` (basé sur `entity.state` = T° CPU)

```
< 65°C  → rgb(70,175,75)   [VERT]    Normal
65–74°C → orange            [ORANGE]  Attention
≥ 75°C  → rgb(244,67,54)   [ROUGE]   Critique
```

La couleur `--text-icon-sensor` (icône thermomètre) et `--text-color-sensor` (valeur °C) suivent les mêmes seuils. En dessous de 65°C, la couleur du texte est `rgb(255,255,255)` (blanc) et non vert — distinction visuelle subtile.

### Champ `cpu` (CPU %)

```
< 75%  → white
75–89% → orange
≥ 90%  → rgb(244,67,54)
```

### Champ `conso` (puissance W prise IKEA)

```
< 15W  → white    (veille / idle)
15–18W → orange   (charge modérée)
≥ 19W  → rouge    (charge élevée)
```

### Champs `ram` et `sd` (RAM % et Disk %)

```
< 75%  → white
75–89% → orange
≥ 90%  → rgb(244,67,54)
```

**Protection N/A :** tous les champs vérifient `unavailable` / `unknown` et renvoient `#aaaaaa` + `N/A`.
Les icônes (server, lightning, memory, harddisk) restent en `rgb(70,175,75)` fixe — seule la valeur change de couleur.

---

## Paramètres clés

| Paramètre | Valeur |
|-----------|--------|
| Type | `custom:button-card` |
| Icône | `phu:intel-nuc` |
| Aspect ratio | `1/1` (carré) |
| Border | `3px double white` |
| Font size | `11px` (valeurs) / `13px` (nom) |
| Grid areas | `"i temp" / "n n" / "cpu cpu" / "conso conso" / "ram ram" / "sd sd"` |
| tap_action | navigate → `/dashboard-tablette/systeme-mini-pc` |
| Entité principale | `sensor.temperature_cpu_package` (MP_01 — sensors Linux) |

---

## Dépannage

**Icône NUC manquante (`phu:intel-nuc`) :**
Cette icône vient de la collection `phu` (Phlex Home Icons ou Hue Icons HACS). Vérifier que le pack est installé. Alternative : `mdi:desktop-tower`.

**Toutes les valeurs à N/A :**
L'intégration `system_monitor` n'est pas configurée ou le service est arrêté. Vérifier `configuration.yaml` — entrée `system_monitor:` et redémarrer HA.

**`sensor.prise_mini_pc_ikea_power` unavailable :**
La prise IKEA Inspelning est hors réseau Zigbee. Vérifier la connexion Zigbee2MQTT.

**Couleurs jamais en rouge (CPU très chaud non détecté) :**
Le seuil `entity.state` dans `styles.icon` utilise la comparaison `< 65` sans `parseFloat()`. Si HA renvoie la T° en string, la comparaison peut échouer. Ajouter `parseFloat(entity.state)` si nécessaire.

---

## Fichiers liés

| Fichier | Rôle |
|---------|------|
| `configuration.yaml` | Déclaration intégration `system_monitor` |
| `sensors/sensors_mini_pc.yaml` *(archive TREE_ORIGINE)* | Anciens sensors RPi — à vérifier si migré |
| *(futur)* `docs/L4C2_MINI_PC/PAGE_MINI_PC.md` | Page dédiée Mini PC — à créer après migration |


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_MINI_PC]]  [[PAGE_RASPI]]  [[L4C1_VIGNETTE_empty]]  [[L4C3_VIGNETTE_MAJ]]*
