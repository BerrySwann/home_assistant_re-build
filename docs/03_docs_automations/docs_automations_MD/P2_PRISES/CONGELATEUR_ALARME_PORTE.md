# CONGÉLATEUR - ALARME PORTE MAL FERMÉE (PROBABLE)

> **Fichier :** non versionné en YAML (automation = UI HA uniquement, cf. CLAUDE.md)
> **Config source :** `docs/03_docs_automations/docs_automations_YAML/P2_PRISES/congelateur_alarme_porte.yaml` (à coller manuellement dans l'UI HA)
> **ID HA :** N/A — automation pas encore créée dans HA (en attente de collage UI par Eric)
> **Mode HA :** `single`
> **MàJ :** 2026-09-01

---

## 📝 Description

Détecte une probable porte de congélateur mal fermée : la température monte
au-dessus d'un seuil pendant que le compresseur tourne activement (donc il
n'arrive pas à compenser une perte de froid). Distingue ce cas d'une panne
(voir `CONGELATEUR_ALARME_PANNE.md`) en croisant température et courant de
la prise de mesure du congélateur.

Design discuté et validé avec Eric le 2026-09-01, seuils dérivés de
l'historique réel de `sensor.prise_congelateur_cuisine_nous_current`
(cycles compresseur observés : ~40-55 min actif, ~5 min coupure normale).

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| — | `numeric_state` | `sensor.tongel_temperature` > -15°C pendant 5 min |

---

## ⚙️ Conditions

| Condition | Détail |
|:---|:---|
| `state` | `binary_sensor.congelateur_compresseur_actif` == `on` (compresseur actif) |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.tongel_temperature` | Capteur Zigbee2MQTT (Tongel), température congélateur, installé 2026-09-01 |
| `binary_sensor.congelateur_compresseur_actif` | Template, cf. `templates/P2_prise/P2_congelateur_alarme/P2_congelateur_compresseur_actif.yaml` |

### Notifications

| Titre | Cible |
|:---|:---|
| `Congélateur : porte mal fermée ?` | `notify.mobile_app_eric`, `notify.mobile_app_mamour` + `persistent_notification` (id `congelateur_alarme_porte`) |

---

## ⚠️ Notes techniques

- `notify.eric` / `notify.mamour` (entités du registre) ne sont **pas** des
  services appelables dans cette instance HA — services réels vérifiés :
  `notify.mobile_app_eric` / `notify.mobile_app_mamour`.
- Eric et Mamour ont chacun 2 téléphones enregistrés dans HA (Xiaomi +
  OnePlus NE2213) ; seul le téléphone Xiaomi de chacun est notifié
  (décision Eric du 2026-09-01).
- Design non testé sur un vrai cycle porte ouverte / panne réelle au
  moment de la création — seuils à valider en conditions réelles.
- Pré-requis : `binary_sensor.congelateur_compresseur_actif` doit être
  poussé en prod et HA rechargé avant de créer cette automation.
