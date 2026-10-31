# check_xx_repertoires_hermes.py - controle des dossiers XX_ et 99_ locaux (lecture seule)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

*Cree le 2026-10-31 : copie maitre du script Hermes rangee dans le depot (ordre d'Eric, nommage <nom>_hermes)*

## Role
Verifie que chaque dossier attendu de `ReBuild\docs` existe encore, qu'il n'a pas maigri (nombre de fichiers hors `.bak` inferieur au minimum constate) et qu'aucun dossier `XX_` ne s'est retrouve en prod (`H:\docs`). Lecture seule : n'ecrit rien. Sortie 0 = tout est la ; sortie 1 = un dossier manque, a maigri ou est present en prod.

## Emplacement
- Script dans le depot : `docs\04_docs_scripts\04_docs_scripts_SH\check_xx_repertoires_hermes\check_xx_repertoires_hermes.py`
- Original vivant : `D:\hermes\scripts\check_xx_repertoires.py` (identique a la copie du depot, 3217 octets, verification par `diff` le 2026-10-31)
- Racine controlee (codee en dur) : `C:\Users\Berry Swann\Documents\ReBuild\docs`
- Racine prod surveillee (codee en dur) : `H:\docs`

Dossiers attendus, avec leur minimum de fichiers hors `.bak` :

| Dossier (relatif a docs) | Minimum |
|---|---|
| `99_docs_MD_system` | 2 |
| `02_docs_dashboard\02_dashboard_docs_MD\L4C1_MINI_PC\XX_L4C1_MINI_PC_03_Page_RASPI` | 1 |
| `02_docs_dashboard\02_dashboard_docs_YAML\L6C3_VIGIEAU\XX_L6C3_VIGIEAU_03_Correctif_upstream` | 1 |
| `02_docs_dashboard\02_dashboard_docs_YAML\XX_RASPI` | 2 |
| `03_docs_automations\03_docs_automations_YAML\XX_RASPI` | 2 |
| `04_docs_scripts\04_docs_scripts_SH\XX_MP_01_monitor_temp_sh_save_pour_RASPI` | 1 |
| `04_docs_scripts\04_docs_scripts_SH\XX_MPC_01_monitor_temp_sh_save_pour_RASPI` | 1 |

`99_docs_MD_system` est declare dans `LOCAL_SEUL` (renommage du 2026-10-31) : `99_` ne va jamais en prod, le controle d'existence est donc local seulement et la presence en prod n'est pas verifiee pour cette entree.

## Lancement
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\check_xx_repertoires_hermes\check_xx_repertoires_hermes.py"`

Variantes prevues par le script :
- `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\check_xx_repertoires_hermes\check_xx_repertoires_hermes.py" --quiet` : une seule ligne, et seulement si aucun probleme (`XX_ : N dossiers presents, aucun en prod`).
- `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\check_xx_repertoires_hermes\check_xx_repertoires_hermes.py" --json` : sortie JSON (`ok`, `problemes`, `dossiers`) avec, par dossier, `dossier`, `existe`, `fichiers`, `minimum`, `en_prod`, `etat`.

Le script se lance AVANT et APRES chaque push, et a chaque tour de travail qui touche `docs/` (decision d'Eric du 2026-10-25).

## Sortie et codes de retour
Sortie par defaut : une ligne par dossier (`etat` tronque a 9 caracteres, `fichiers/minimum`, chemin, puis `[EN PROD]` si applicable), suivie de `bilan : N problemes sur 7 dossiers XX_ attendus`.

Etats possibles par dossier : `OK`, `MANQUANT`, `MAIGRI (n < mini)`, `PRESENT EN PROD, interdit`.

- Code 0 : aucun probleme (`ok: true` en JSON) ; en `--quiet`, la ligne unique est imprimee.
- Code 1 : au moins un probleme (dossier manquant, dossier maigri, ou dossier present en prod) - ne rien pousser, prevenir Eric.

## Limites
- Lecture seule : le script n'ecrit rien, ne cree, ne restaure ni ne supprime aucun dossier ou fichier ; il ne pousse rien.
- Les chemins `docs` et `H:\docs` sont codes en dur : aucun argument ne permet de controler une autre racine.
- La liste des dossiers attendus et leurs minimums sont codes en dur dans `ATTENDUS` : ajouter un `XX_` demande de modifier le script (pas de fichier manifeste, pas d'option `--maj`).
- Le comptage est recursif (`os.walk`) mais exclut tout fichier dont le nom contient `.bak` ; il compte des fichiers, pas leur contenu ni leur md5.
- Pour l'entree `99_docs_MD_system` (dans `LOCAL_SEUL`), la prod n'est jamais consultee : un `99_` en prod ne serait pas signale par ce script.
- En mode `--quiet`, rien n'est imprime quand un probleme existe : seul le code de retour 1 le signale.
- Il ne verifie pas GitHub, seulement le local et `H:\docs`.
