# CONGÉLATEUR - ALARME PANNE PROBABLE (PAS DE COURANT)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P2_Alarme_Congélateur/congelateur_alarme_panne/congelateur_alarme_panne.yaml`
> **ID HA :** `1788279708180` (en prod dans automations.yaml, active dans HA)
> **Mode HA :** `single`
> **MàJ :** 2026-10-11 (en-tête corrigé : chemin, ID HA ; contenu relu contre le YAML)

---

## 📝 Description

Détecte une probable panne électrique ou mécanique du congélateur : la
température monte au-dessus du seuil ET le compresseur ne tire plus aucun
courant depuis 1h (il ne redémarre plus), contrairement au cas "porte mal
fermée" où le compresseur reste actif (cf. `CONGELATEUR_ALARME_PORTE.md`).

Seuil "1h sans consommation" choisi par Eric le 2026-09-01 (valeur initiale
proposée : 25 min, dérivée de l'historique réel montrant des coupures
normales de compresseur ~5 min max) — plus conservateur, donc détection
plus lente en cas de vraie panne mais risque de faux positif très faible.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| — | `numeric_state` | `sensor.tongel_temperature` > -15°C pendant 5 min |

---

## ⚙️ Conditions

| Condition | Détail |
|:---|:---|
| `state` | `binary_sensor.congelateur_compresseur_actif` == `off` pendant 1h (aucun appel de courant) |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.tongel_temperature` | Capteur Zigbee2MQTT (Tongel), température congélateur, installé 2026-09-01 |
| `binary_sensor.congelateur_compresseur_actif` | Template, cf. `docs/01_docs_config_system/01_config_system_SH_PY_YAML/templates/P2_prise/P2_congelateur/P2_congelateur_compresseur_actif.yaml` |

### Notifications

| Titre | Cible |
|:---|:---|
| `Congélateur : panne probable` | `notify.mobile_app_eric`, `notify.mobile_app_mamour` + `persistent_notification` (id `congelateur_alarme_panne`) |

---

## ⚠️ Notes techniques

- Peut aussi se déclencher si c'est la **prise de mesure** NOUS qui est
  hors ligne (Wi-Fi coupé, pas branchée), pas forcément le congélateur —
  limite documentée dans le fichier `binary_sensor` source.
- `notify.eric` / `notify.mamour` (entités du registre) ne sont **pas** des
  services appelables — services réels vérifiés :
  `notify.mobile_app_eric` / `notify.mobile_app_mamour`.
- Pré-requis : `binary_sensor.congelateur_compresseur_actif` doit être
  poussé en prod et HA rechargé avant de créer cette automation.
