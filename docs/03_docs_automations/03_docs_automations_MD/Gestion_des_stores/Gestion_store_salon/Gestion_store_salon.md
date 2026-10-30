# GESTION SIMPLE DU STORE SALON (MATIN / SOIR)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-ff9800?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Gestion_des_Stores/gestion_simple_du_store_salon_matin_soir/gestion_simple_du_store_salon_matin_soir.yaml`
> **ID HA :** `1775244989013` (en prod dans automations.yaml)
> **Mode HA :** `single`
> **MàJ :** 2026-10-29 (refonte sur le modèle du store bureau, voir Notes ; automation en HA alignée sur ce YAML et testée par Eric le 2026-10-29)

---

## Description

Ouvre le store du salon à partir de 6h30 tant que le soleil n'est pas couché, et le ferme au coucher du soleil, sur le modèle de l'automation du store du bureau, sans les températures. Le store ne bouge jamais si la fenêtre du salon est ouverte. Il ne s'ouvre que depuis une position fermée (position inférieure à 1).

---

## Déclencheurs

| ID | Type | Détail |
|:---|:---|:---|
| `reveil` | `time` | 06:30:00 (entre guillemets dans le YAML) |
| (aucun) | `sun` | `sunset` (coucher du soleil) |
| `fenetre` | `state` | `binary_sensor.contact_fenetre_salon_sonoff_contact` passe à `off` (fenêtre refermée) |

---

## Conditions globales

- `binary_sensor.contact_fenetre_salon_sonoff_contact` est `off` (fenêtre fermée). Alias dans le YAML : "SÉCURITÉ : La fenêtre doit être FERMÉE pour bouger le store".

---

## Actions (choose)

| Alias | Conditions | Action |
|:---|:---|:---|
| MATIN : Ouverture | heure après 06:30:00 + soleil avant le coucher (`sun`, `before: sunset`) + `cover.store_salon` attribut `current_position` inférieur à 1 | `cover.open_cover` sur `cover.store_salon` |
| SOIR : Fermeture | soleil après le coucher (`sun`, `after: sunset`) | `cover.close_cover` sur `cover.store_salon` |

Les conditions ne dépendent pas du déclencheur : un lancement manuel (Exécuter) évalue les mêmes conditions.

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `cover.store_salon` | Store motorisé du salon (attribut `current_position`) |
| condition et déclencheur `sun` | Coucher du soleil |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | Sécurité fenêtre et déclencheur de réouverture |

---

## Notes

- Cette fiche remplace l'ancienne, qui décrivait la version "Gestion optimisée du store salon (anti-reflet PC)" (scénarios canicule, anti-reflet PC, froid + absence, nuit). Cette version n'est plus dans HA (décision Eric du 2026-10-11 : la fiche suit la version active). L'ancienne fiche est conservée en `GESTION_STORE_SALON.bak_<date_heure>.md` dans le même dossier ; l'ancien YAML `gestion_store_salon.yaml` n'existe plus en local (corbeille Windows du 2026-10-10), copie restée sur H:\docs\03_docs_automations\03_docs_automations_YAML\_old_avant_staging\stores\ et sur GitHub.
- Le store du bureau a sa propre automation ("Gestion Optimisée du Store Bureau", id `1775244953345`).
- 2026-10-29 : le store ne s'ouvrait pas au lever du soleil. Trace HA du 2026-10-29 : le déclencheur `sunrise` est parti à 07:02:00 alors que `sun.sun` valait encore `below_horizon` (passé à `above_horizon` à 07:03:00), donc la condition du matin échouait. La condition accepte maintenant directement un déclencheur de type `sun` et ne vérifie `sun.sun` que pour le déclencheur de 06:30. Dans le YAML, les heures 06:30:00 et 06:29:00 sont désormais entre guillemets : sans guillemets, HA les lit comme un nombre (erreur "Invalid time specified: 23340"). Lu dans HA le 2026-10-29 à 07:25 : l'automation a encore l'ancienne condition `sun.sun` et un décalage de +1 minute sur `sunrise`, absent du YAML local.
- 2026-10-29 (2e version) : refonte sur le modèle de "Gestion Optimisée du Store Bureau", sans les températures et avec 06:30 à la place de 07:00. Raison : les lancements manuels de 07:27 et 07:30 n'ont rien fait, car les deux branches du `choose` exigeaient un déclencheur d'id `ouverture` ou `fermeture`, absent d'un lancement manuel (traces HA : déclencheur vide). Conséquence connue : à 06:30 l'ouverture a lieu même si le soleil n'est pas encore levé (lever du jour de la trace : 07:02).

<!-- annotations_log:
[2026-10-29] L3C3 - fiche alignee sur le YAML local (condition matin en template, heures entre guillemets, note du 2026-10-29) ; bak : Gestion_store_salon.bak_2026_10_29_07h28m54s.md
[2026-10-29] L3C3 - fiche refaite sur le nouveau YAML (modele store bureau, 06:30, sans temperatures) ; bak : Gestion_store_salon.bak_2026_10_29_07h32m27s.md
[2026-10-29] L3C3 - ligne MaJ corrigee : automation HA alignee sur le YAML local, ouverture constatee par Eric ; bak : Gestion_store_salon.bak_2026_10_29_07h34m37s.md -->
