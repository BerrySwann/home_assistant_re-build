# (J) DEBUG - NOTIFIER CHANGEMENTS MESSAGE CLIM

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/j_debug_notifier_les_changements_de_message_clim_mobile/j_debug_notifier_les_changements_de_message_clim_mobile.yaml`
> **Mode HA :** `single` (implicite)

---

## 📝 Description

Automation de debug/monitoring. Surveille `sensor.message_clim_personnalise_7h30_21h00`
et décompose son contenu pour envoyer des notifications spécifiques selon
le type de changement détecté (présence, tendance T°, mode chauffage/refroidissement).

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.message_clim_personnalise_7h30_21h00` |

---

## ⚙️ Actions - Choose selon contenu du message

| Cas | Détection | Message envoyé |
|:---|:---|:---|
| CELLULAR | `CELLULAR` dans le state | Absence détectée |
| MAMOUR | `MAMOUR` dans le state | Mamour seul |
| ERIC | `ERIC` dans le state | Eric seul |
| LES DEUX | `Clim [2] en [WIFI]` | Duo |
| UP | `Up >>>` | T° en hausse |
| DOWN | `Down <<<` | T° en baisse |
| STABLE | `stable` | T° stable |
| HEAT | `Heat` | Mode chauffage |
| COOL | `Cool` | Mode refroidissement |
| FAN | `Fan` | Mode ventilation |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.message_clim_personnalise_7h30_21h00` | Source de vérité |

### Notifications

Toutes envoyées vers `notify.mobile_app_eric` avec messages texte ciblés.
