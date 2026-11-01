# Check_prod_fonctionnelle.py - controle des fichiers qui font tourner la prod

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Check_prod_fonctionnelle/Check_prod_fonctionnelle.py` |
| Langage | Python 3 |
| Lance par | etape D de `trigul_run.py` (apres le trigul profond) et /histo etape 6 point 13 |
| Ecrit | uniquement son rapport dans `historique/03_RAPPORTS/06_MD5/06_PROD_FONCTIONNELLE/` |

## Role

Decide par Eric le 2026-10-31 : la priorite absolue, ce sont les fichiers qui font tourner la prod. Le script verifie les 98 fichiers du palier 1 (7 YAML racine + dossiers sensors, templates, utility_meter, command_line, shell_command, groups, input_booleans, input_number, timers, scripts, .scripts) sur 4 colonnes : P prod racine, R GitHub, L local, M prod miroir docs. Un fichier est vert seulement si les 4 sont identiques. Il controle aussi que les 17 `!include` de configuration.yaml et les scripts cites par chemin existent.

automations.yaml et scripts.yaml : le trigul profond les copie d'abord dans leur dossier ORIGINAL, extrait les 63 automations et 9 scripts et les compare au local ; le script lit cette copie du jour (jamais H: directement), exige qu'elle soit egale a H: et reprend le resultat unite par unite du rapport profond.

Verifie en fin de controle, entre la prod et GitHub seulement (jamais en local) : les historiques `notifs/*.txt` et les 18 images du dashboard. Signale tout element inconnu a la racine de H: (derive).

Hors manifeste (decide par Eric) : scenes.yaml, blueprints, themes, custom_components et www/community (reinstallables par HACS), .storage, images non citees, .bak et fichiers locaux seuls.

## Utilisation

```
python -I -X utf8 Check_prod_fonctionnelle.py
```

Lecture seule. Code de retour 0 palier 1 conforme, 1 ecart au palier 1, 2 H: injoignable. Le rapport contient le verdict du palier 1, un tree special prod (fichiers par dossier), les ecarts et le tableau P | R | L | M.

## Etat

- Cree le 2026-10-31. Premier controle complet : 98 fichiers verts, 17 !include sur 17, 4 scripts cites sur 4, 6 notifs et 18 images presents, derive 0.
- Branche dans `trigul_run.py` (etape D). Branchement dans /histo et /histo-final : un palier 1 en ecart bloque le push 5C et l'extinction.

## Origine de cette fiche

Creee le 2026-10-31 par Claude (ordre d'Eric 22:26).

## Mise a jour 2026-11-01

La copie ORIGINAL du jour de automations.yaml et scripts.yaml est aussi reconnue sous son nom date (base.bak_AAAA_MM_JJ.yaml), nom pris par le menage definitif de /histo-final ; la copie horodatee reste prioritaire si elle existe.
