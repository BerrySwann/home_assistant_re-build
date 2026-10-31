# MF_VIGILANCE_IMAGES - Cartes de vigilance Météo France (J0 et J1)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

> **Script :** `mf_vigilance_images.sh` (bash)
> **Emplacement prod :** `/config/scripts/mf_vigilance_images.sh` (dossier `scripts`, sans point : différent de `.scripts`)
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/scripts/mf_vigilance_images.sh` (copie identique dans `docs/04_docs_scripts/04_docs_scripts_SH/Mf_vigilance_images/Mf_vigilance_images.sh`)
> **Empreinte relevée le 2026-10-18 :** MD5 `3e20109d`, 1831 octets, copies identiques à la prod
> **Appelé par :** les deux capteurs `command_line` de `command_line/Meteo/carte_meteo_france.yaml`
> **Dernière modification :** 2026-10-01 (date du fichier)

---

## Description

Télécharge les cartes de vigilance Météo France d'aujourd'hui (J0) et de demain (J1) et les enregistre en PNG dans un dossier. Remplace l'ancienne source (API officielle DPVigilance), qui répondait HTTP 403 le 2026-10-01 (information du YAML appelant).

## Utilisation

`mf_vigilance_images.sh [dossier_de_sortie] [both|J0|J1]`

- Dossier de sortie par défaut : `/config/www/weather`.
- Sans deuxième argument ou avec `both` : les deux cartes. `J0` : `meteo_france_alerte_today.png`. `J1` : `meteo_france_alerte_tomorrow.png`.

## Fonctionnement

- Pose un cookie de session en appelant `https://vigilance.meteofrance.fr/fr` (cookie `mfsession`). Sans ce cookie, le script s'arrête avec le code 1.
- Le jeton est ce cookie passé au ROT13, envoyé dans `Authorization: Bearer`. Le cookie ne vit qu'une heure, le jeton est donc recalculé à chaque exécution. Aucun jeton ni clé n'est écrit dans le script.
- Télécharge `https://rwg.meteofrance.com/wsft/v3/warning/thumbnail?domain=FRA&resolution=large&warning_type=vigilance&echeance=J0` (ou `J1`), délai de 30 s.
- Refuse toute réponse dont les 8 premiers octets ne contiennent pas `PNG` (code de sortie 1).
- Se termine par une ligne horodatée `AAAA-MM-JJTHH:MM:SS maj ok`, qui sert de valeur au capteur.

## Appelé par (carte_meteo_france.yaml)

- `sensor.meteo_france_alertes_image_today` : `sh /config/scripts/mf_vigilance_images.sh /config/www/weather J0 2>&1 | tail -1`.
- `sensor.meteo_france_alertes_image_tomorrow` : même commande avec `J1`.
- Intervalle de 14400 s (4 h), délai de commande de 15 s. `automations.yaml` fait référence à ces deux capteurs (lignes 34 à 76).

## Points d'attention

- La source est l'API interne du site de vigilance, pas une API publique documentée : elle peut changer sans préavis (déduit).
- Un capteur `command_line` qui ne rend aucune valeur reste `unavailable`. D'où la dernière ligne obligatoire du script.
- D'après le YAML appelant : une carte fausse ne se voit pas dans Home Assistant. Vérifier l'empreinte et la taille des PNG (environ 55 ko), pas seulement leur présence.
- D'après le YAML appelant : les entités `camera.mf_alerte_today` et `camera.mf_alerte_tomorrow` (intégration `local_file`) affichent ces PNG dans le pop-up d'alerte du dashboard.
- Ne pas confondre `scripts/` (ce dossier) avec `.scripts/` (scripts de maintenance : sauvegarde GitHub, audits, rattrapage Linky) ni avec `scripts.yaml` (scripts HA).