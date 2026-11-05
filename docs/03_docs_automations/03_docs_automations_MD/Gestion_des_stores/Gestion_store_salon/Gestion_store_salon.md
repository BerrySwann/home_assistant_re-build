# GESTION OPTIMISEE DU STORE SALON (PRESENCE, SOLEIL, TEMPERATURES)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--05-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Gestion_des_stores/Gestion_simple_du_store_salon_matin_soir/Gestion_simple_du_store_salon_matin_soir.yaml` (le nom du fichier garde l'ancien intitule)
> **ID HA :** `1775244989013`
> **Alias HA :** `Gestion Optimisée du Store Salon`
> **Mode HA :** `single`
> **MàJ :** 2026-11-05 (copie du modèle du store bureau, seuils 12 et 32, groupes de présence ; appliqué dans HA le 2026-11-05 à 07:32 : HA = ce YAML, point de retour de l'ancien automations.yaml dans Automations_yaml_original\automations.bak_2026_11_05_07h30m30.yaml)

---

## Description

Gère le store du salon selon la présence (`sensor.groupe`), le lever et le coucher du soleil et la température extérieure (`sensor.th_balcon_nord_temperature`).

- **Groupe 1 (personne à la maison)** : le store se ferme, sans aucune autre condition (ni soleil, ni température, ni fenêtre). Branche prioritaire.
- **Groupe 2 (Mamour) ou groupe 4 (Mamour et Eric)** : le store s'ouvre (scénario A) s'il est fermé, après 07:00, entre le lever et le coucher du soleil, avec une température extérieure comprise entre 12 et 32 °C, et fenêtre fermée.
- **Groupe 3 (Eric seul)** : aucune ouverture automatique.
- **Chaleur** (scénario B, au-dessus de 32 °C avant le coucher) et **nuit** (scénario C, après le coucher) : fermeture, quel que soit le groupe, uniquement si la fenêtre est fermée.

Le store ne bouge jamais si la fenêtre du salon est ouverte, sauf en groupe 1 (décision d'Eric du 2026-11-05 : le groupe 1 ne tient compte d'aucune autre condition).

---

## Déclencheurs

| ID | Type | Détail |
|:---|:---|:---|
| `reveil` | `time` | 07:00:00 (entre guillemets dans le YAML) |
| `lever` | `sun` | `sunrise` (lever du soleil) |
| (aucun) | `state` | `sensor.th_balcon_nord_temperature` (tout changement) |
| (aucun) | `sun` | `sunset` (coucher du soleil) |
| `fenetre` | `state` | `binary_sensor.contact_fenetre_salon_sonoff_contact` passe à `off` (fenêtre refermée) |
| `groupe_1` | `state` | `sensor.groupe` passe à `groupe_1`, pendant 5 minutes |
| `groupe_2_4` | `state` | `sensor.groupe` passe à `groupe_2` ou `groupe_4`, immédiatement (sans délai) |

Le délai de 5 minutes sur le passage à `groupe_1` (fermeture) évite les bascules fugaces quand un téléphone change de réseau (piège noté dans `P4_groupe_presence.yaml`).

---

## Conditions globales

Aucune (`conditions: []`). La sécurité fenêtre est portée par chaque scénario A, B et C, ce qui permet au groupe 1 de la contourner.

---

## Actions (choose)

| Alias | Conditions | Action |
|:---|:---|:---|
| GROUPE 1 : Personne, fermeture | `sensor.groupe` = `groupe_1` (aucune autre condition) | `cover.close_cover` sur `cover.store_salon` |
| SCÉNARIO A : Ouverture Travail (Groupe 2 ou 4) | fenêtre fermée + `sensor.groupe` = `groupe_2` ou `groupe_4` + heure après 07:00:00 + soleil après le lever + soleil avant le coucher + température extérieure au-dessus de 12 et en dessous de 32 + `cover.store_salon` attribut `current_position` inférieur à 1 | `cover.open_cover` sur `cover.store_salon` |
| SCÉNARIO B : Fermeture Chaleur (Été) | fenêtre fermée + température extérieure au-dessus de 32 + soleil avant le coucher | `cover.close_cover` sur `cover.store_salon` |
| SCÉNARIO C : Fermeture Nuit | fenêtre fermée + soleil après le coucher | `cover.close_cover` sur `cover.store_salon` |

Les conditions ne dépendent pas du déclencheur : un lancement manuel (Exécuter) évalue les mêmes conditions. La branche du groupe 1 est évaluée en premier. À exactement 32 °C, ni le scénario A ni le B ne s'applique (comparaisons strictes). En groupe 1, chaque changement de température relance l'ordre de fermeture, même sur un store déjà fermé (sans conséquence).

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `cover.store_salon` | Store motorisé du salon (attribut `current_position`) |
| `sensor.groupe` | Groupe de présence : `groupe_1` personne, `groupe_2` Mamour, `groupe_3` Eric, `groupe_4` tous (template P4, `P4_groupe_presence.yaml`) |
| `sensor.th_balcon_nord_temperature` | Température extérieure (même capteur que l'automation du bureau) |
| condition et déclencheurs `sun` | Lever et coucher du soleil |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | Sécurité fenêtre et déclencheur de réouverture |

---

## Notes

- 2026-11-05 : l'automation du salon est remplacée par la copie de "Gestion Optimisée du Store Bureau" (id `1775244953345`), avec les entités du salon. Le capteur de température du bureau (`sensor.th_balcon_nord_temperature`) est repris tel quel, le salon n'en ayant pas. Heure 07:00 du bureau au lieu de 06:30. Seuils de température du salon : scénario A entre 12 et 32 (le bureau garde 18 et 25), scénario B au-dessus de 32. Puis ajout des groupes de présence.
- 2026-11-05 (décision d'Eric) : exceptionnellement, deux versions sont gardées. La version définitive est ce fichier. L'ancienne automation simple (matin/soir 06:30, sans température ni présence) est conservée dans `Gestion_simple_du_store_salon_matin_soir.bak_2026_11_05_07h06m31s.yaml` (même dossier, hors ménage). Une copie de la version juste avant l'ajout de la présence est dans le sous-dossier `COPIE_avant_presence_2026_11_05_archive` (local seulement, jamais poussée).
- Le store du bureau a sa propre automation (id `1775244953345`) et garde ses seuils 18 et 25.
- Historique, version du 2026-10-29 (06:30, sans température ni présence, remplacée le 2026-11-05) : cette fiche remplaçait l'ancienne, qui décrivait la version "Gestion optimisée du store salon (anti-reflet PC)" (scénarios canicule, anti-reflet PC, froid + absence, nuit). Cette version n'est plus dans HA (décision Eric du 2026-10-11 : la fiche suit la version active). L'ancienne fiche est conservée en `GESTION_STORE_SALON.bak_<date_heure>.md` dans le même dossier ; l'ancien YAML `gestion_store_salon.yaml` n'existe plus en local (corbeille Windows du 2026-10-10), copie restée sur H:\docs\03_docs_automations\03_docs_automations_YAML\_old_avant_staging\stores\ et sur GitHub.
- Le store du bureau a sa propre automation ("Gestion Optimisée du Store Bureau", id `1775244953345`).
- 2026-10-29 : le store ne s'ouvrait pas au lever du soleil. Trace HA du 2026-10-29 : le déclencheur `sunrise` est parti à 07:02:00 alors que `sun.sun` valait encore `below_horizon` (passé à `above_horizon` à 07:03:00), donc la condition du matin échouait. La condition accepte maintenant directement un déclencheur de type `sun` et ne vérifie `sun.sun` que pour le déclencheur de 06:30. Dans le YAML, les heures 06:30:00 et 06:29:00 sont désormais entre guillemets : sans guillemets, HA les lit comme un nombre (erreur "Invalid time specified: 23340"). Lu dans HA le 2026-10-29 à 07:25 : l'automation a encore l'ancienne condition `sun.sun` et un décalage de +1 minute sur `sunrise`, absent du YAML local.
- 2026-10-29 (2e version) : refonte sur le modèle de "Gestion Optimisée du Store Bureau", sans les températures et avec 06:30 à la place de 07:00. Raison : les lancements manuels de 07:27 et 07:30 n'ont rien fait, car les deux branches du `choose` exigeaient un déclencheur d'id `ouverture` ou `fermeture`, absent d'un lancement manuel (traces HA : déclencheur vide). Conséquence connue : à 06:30 l'ouverture a lieu même si le soleil n'est pas encore levé (lever du jour de la trace : 07:02).

<!-- annotations_log:
[2026-10-29] L3C3 - fiche alignee sur le YAML local (condition matin en template, heures entre guillemets, note du 2026-10-29) ; bak : Gestion_store_salon.bak_2026_10_29_07h28m54s.md
[2026-10-29] L3C3 - fiche refaite sur le nouveau YAML (modele store bureau, 06:30, sans temperatures) ; bak : Gestion_store_salon.bak_2026_10_29_07h32m27s.md
[2026-10-29] L3C3 - ligne MaJ corrigee : automation HA alignee sur le YAML local, ouverture constatee par Eric ; bak : Gestion_store_salon.bak_2026_10_29_07h34m37s.md
[2026-11-05] L3C3 - fiche refaite sur le YAML copie du bureau (seuils 12 et 32, groupes de presence, ordre d Eric 07:25) ; bak : Gestion_store_salon.bak_2026_11_05_07h26m47s.md
[2026-11-05] L3C3 - ligne MaJ corrigee : l'etat HA etait annonce aligne par erreur (test trop large) ; verifie dans automations.yaml : HA garde l'ancienne version ; bak : Gestion_store_salon.bak_2026_11_05_07h27m04s.md
[2026-11-05] L3C3 - ligne MaJ corrigee : automation appliquee dans HA a 07:32 (relue : identique au YAML local, entite on) ; bak : Gestion_store_salon.bak_2026_11_05_07h32m56s.md
[2026-11-05] L3C3 - groupe_2/groupe_4 : declencheur immediat, delai de 5 min retire (ordre d Eric 07:35) ; groupe_1 garde 5 min ; bak : Gestion_store_salon.bak_2026_11_05_07h35m05s.md -->
