# CONGÉLATEUR - ALARME PERTE DE SUPERVISION (CAPTEUR TONGEL MUET)

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P2_Alarme_Congélateur/congelateur_alarme_capteur/congelateur_alarme_capteur.yaml`
> **ID HA :** `1788279749343` (en prod dans automations.yaml, active dans HA)
> **Mode HA :** `single`
> **MàJ :** 2026-10-11 (en-tête corrigé : chemin, ID HA ; contenu relu contre le YAML)

---

## 📝 Description

Détecte que `sensor.tongel_temperature` ne remonte plus rien (état
`unavailable` ou `unknown`) depuis 2h — perte de supervision du congélateur,
indépendante de son état réel (compresseur en panne ou non). Cause possible :
pile morte, perte de portée Zigbee, capteur défectueux.

Délai de 2h choisi par Eric le 2026-09-01, sans historique de reporting
disponible pour ce capteur (appairé le jour même) — pas de valeur dérivée
empiriquement, à ajuster si trop de faux positifs ou trop lent à détecter
une vraie perte.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| — | `state` | `sensor.tongel_temperature` → `unavailable` pendant 2h |
| — | `state` | `sensor.tongel_temperature` → `unknown` pendant 2h |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.tongel_temperature` | Capteur Zigbee2MQTT (Tongel), température congélateur, installé 2026-09-01 |

### Notifications

| Titre | Cible |
|:---|:---|
| `Congélateur : capteur muet` | `notify.mobile_app_eric`, `notify.mobile_app_mamour` + `persistent_notification` (id `congelateur_alarme_capteur`) |

---

## ⚠️ Notes techniques

- `notify.eric` / `notify.mamour` (entités du registre) ne sont **pas** des
  services appelables — services réels vérifiés :
  `notify.mobile_app_eric` / `notify.mobile_app_mamour`.
- Ne dépend pas de `binary_sensor.congelateur_compresseur_actif` — se
  déclenche même si la prise de courant fonctionne normalement.
