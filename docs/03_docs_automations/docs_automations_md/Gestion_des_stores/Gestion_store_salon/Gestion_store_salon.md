# GESTION SIMPLE DU STORE SALON (MATIN / SOIR)

> **Fichier :** `docs/03_docs_automations/docs_automations_YAML/Gestion_des_Stores/gestion_simple_du_store_salon_matin_soir/gestion_simple_du_store_salon_matin_soir.yaml`
> **ID HA :** `1775244989013` (en prod dans automations.yaml)
> **Mode HA :** `single`
> **MàJ :** 2026-10-11 (fiche réécrite d'après le YAML actif, identique à H:\automations.yaml)

---

## Description

Ouvre le store du salon au lever du soleil (pas avant 6h30) et le ferme au coucher du soleil. Description HA : "Ouvre le store au lever du soleil (pas avant 6h30) et le ferme au coucher". Le store ne bouge jamais si la fenêtre du salon est ouverte.

---

## Déclencheurs

| ID | Type | Détail |
|:---|:---|:---|
| `ouverture` | `time` | 06:30:00 |
| `ouverture` | `sun` | `sunrise` (lever du soleil) |
| `fermeture` | `sun` | `sunset` (coucher du soleil) |

---

## Conditions globales

- `binary_sensor.contact_fenetre_salon_sonoff_contact` est `off` (fenêtre fermée). Alias dans le YAML : "SÉCURITÉ : La fenêtre doit être FERMÉE".

---

## Actions (choose)

| Alias | Conditions | Action |
|:---|:---|:---|
| Matin : Ouverture si > 6h30 ET Soleil levé | déclencheur `ouverture` + heure après 06:29 + `sun.sun` à `above_horizon` | `cover.open_cover` sur `cover.store_salon` |
| Soir : Fermeture au coucher du soleil | déclencheur `fermeture` | `cover.close_cover` sur `cover.store_salon` |

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `cover.store_salon` | Store motorisé du salon |
| `sun.sun` | Lever / coucher du soleil, état au-dessus de l'horizon |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | Sécurité fenêtre |

---

## Notes

- Cette fiche remplace l'ancienne, qui décrivait la version "Gestion optimisée du store salon (anti-reflet PC)" (scénarios canicule, anti-reflet PC, froid + absence, nuit). Cette version n'est plus dans HA (décision Eric du 2026-10-11 : la fiche suit la version active). L'ancienne fiche est conservée en `GESTION_STORE_SALON.bak_<date_heure>.md` dans le même dossier ; l'ancien YAML `gestion_store_salon.yaml` n'existe plus en local (corbeille Windows du 2026-10-10), copie restée sur H:\docs\03_docs_automations\docs_automations_YAML\_old_avant_staging\stores\ et sur GitHub.
- Le store du bureau a sa propre automation ("Gestion Optimisée du Store Bureau", id `1775244953345`).