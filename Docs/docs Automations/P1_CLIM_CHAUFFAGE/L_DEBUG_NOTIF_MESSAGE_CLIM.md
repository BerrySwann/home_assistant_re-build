# (L) DEBUG — NOTIFIER CHANGEMENTS MESSAGE CLIM

> **Fichier :** `automations_corrige/P1_clim_chauffage/L_debug_notif_message_clim.yaml`
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

## ⚙️ Actions — Choose selon contenu du message

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
