# Mf_vigilance_images.sh - cartes de vigilance Meteo France (J0 et J1)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Mf_vigilance_images/Mf_vigilance_images.sh` |
| Prod | `/config/scripts/mf_vigilance_images.sh` (`H:\scripts\mf_vigilance_images.sh`) |
| Langage | Shell (sh, curl) |
| Appele par | capteurs `command_line` de `command_line/Meteo/carte_meteo_france.yaml` (J0 et J1) |
| Ecrit | `/config/www/weather/meteo_france_alerte_today.png` et `meteo_france_alerte_tomorrow.png` |

## Role

Telecharge les cartes de vigilance Meteo France d'aujourd'hui (J0) et de demain (J1) vers un dossier. Il remplace l'ancienne methode a token fixe (code 900908). Aucun token a maintenir : le script pose d'abord le cookie de session du site de vigilance, derive le jeton attendu par l'API a partir de ce cookie, puis telecharge les cartes. Le cookie ne vit qu'une heure, d'ou la rederivation a chaque execution.

Il refuse toute reponse qui n'est pas un vrai PNG (code de sortie 1 et message), et affiche en derniere ligne une date `... maj ok` : un capteur `command_line` qui n'ecrit qu'un fichier resterait `unavailable` a vie.

## Utilisation

```
sh /config/scripts/mf_vigilance_images.sh [dossier_de_sortie] [both|J0|J1]
```

- Sans 2e argument : les deux cartes. Dossier par defaut : `/config/www/weather`.
- Utilise dans `carte_meteo_france.yaml` avec `J0` puis `J1`.
- Les cameras `camera.mf_alerte_today` et `camera.mf_alerte_tomorrow` (local_file) affichent les PNG dans le pop-up `#alert` de la page meteo.

## Etat

- Prod, local et copie de config identiques (MD5 3E20109D au 2026-10-31).
- Fait partie du palier 1 du controle `Check_prod_fonctionnelle` (script cite par chemin dans un fichier YAML de la prod).
- Image de secours `www/weather/meteo_france_alerte_nodata.png` (carte de France grise) quand les cartes manquent.

## Origine de cette fiche

Creee le 2026-10-31 par Claude (ordre d'Eric 22:30), a la lecture du script en prod.