# CONGÉLATEUR - ALARME PANNE PROBABLE (PAS DE COURANT)

> **Fichier :** non versionné en YAML (automation = UI HA uniquement, cf. CLAUDE.md)
> **Config source :** `docs/03_docs_automations/docs_automations_YAML/P2_PRISES/congelateur_alarme_panne.yaml` (à coller manuellement dans l'UI HA)
> **ID HA :** N/A — automation pas encore créée dans HA (en attente de collage UI par Eric)
> **Mode HA :** `single`
> **MàJ :** 2026-09-01

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
| `binary_sensor.congelateur_compresseur_actif` | Template, cf. `templates/P2_prise/P2_congelateur_alarme/P2_congelateur_compresseur_actif.yaml` |

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
