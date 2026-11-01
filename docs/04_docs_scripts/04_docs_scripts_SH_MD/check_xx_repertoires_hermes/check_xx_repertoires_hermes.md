# check_xx_repertoires_hermes.py - controle des dossiers XX_ et 99_ locaux (lecture seule)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--01-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

*Cree le 2026-10-31 : copie maitre du script Hermes rangee dans le depot (ordre d'Eric, nommage <nom>_hermes)*

## Role
Verifie, pour chaque entree du manifeste `XX_manifest.json`, que le dossier de `ReBuild\docs` existe encore, que ses fichiers listes sont la et qu'il n'a pas maigri (nombre de fichiers hors `.bak` inferieur au minimum), et qu'aucun dossier `XX_` ne s'est retrouve en prod (`H:\docs`). Lecture seule : n'ecrit rien. Sortie 0 = tout est la ; sortie 1 = un dossier manque, a maigri ou est present en prod.

## Emplacement
- Script dans le depot : `docs\04_docs_scripts\04_docs_scripts_SH\check_xx_repertoires_hermes\check_xx_repertoires_hermes.py`
- Original vivant : `D:\hermes\scripts\check_xx_repertoires.py` (identique a la copie du depot : 4593 octets, md5 `c67a0c21` des deux cotes, verifie le 2026-11-01 apres le passage a la lecture du manifeste)
- Racine controlee (codee en dur) : `C:\Users\Berry Swann\Documents\ReBuild\docs`
- Racine prod surveillee (codee en dur) : `H:\docs`

Dossiers attendus : **lus dans le manifeste**, plus codes en dur.

- Source : `docs\04_docs_scripts\04_docs_scripts_JSON\Check_XX_presents\XX_manifest.json` (propriete de Claude, mis a jour par son `--maj` seulement ; ce script ne l'ecrit jamais).
- Une entree du manifeste = un dossier a surveiller. Minimum attendu = nombre de fichiers listes pour cette entree dans le manifeste.
- Le script signale en plus : un fichier du manifeste absent du disque, et un dossier `XX_` present sur le disque mais absent du manifeste (`NON DECLARE`).
- `99_docs_MD_system` est declare dans `LOCAL_SEUL` : `99_` ne va jamais en prod, seule l'existence locale est exigee et la presence en prod n'est pas verifiee pour cette entree.

Historique : la liste a d'abord ete codee en dur (8 dossiers). Deux renommages en deux jours l'ont cassee - `XX_docs_MD_system` devenu `99_docs_MD_system` le 31/10, puis les suffixes ` (a ne pas jeter)` et les miroirs MD le 01/11. Depuis le 2026-11-01 le script lit le manifeste (idee 8 de Hermes, acceptee par Eric) : un seul proprietaire de la liste.
## Lancement
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\check_xx_repertoires_hermes\check_xx_repertoires_hermes.py"`

Variantes prevues par le script :
- `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\check_xx_repertoires_hermes\check_xx_repertoires_hermes.py" --quiet` : une seule ligne, et seulement si aucun probleme (`XX_ : N dossiers presents, aucun en prod`).
- `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\check_xx_repertoires_hermes\check_xx_repertoires_hermes.py" --json` : sortie JSON (`ok`, `problemes`, `dossiers`) avec, par dossier, `dossier`, `existe`, `fichiers`, `minimum`, `en_prod`, `etat`.

Le script se lance AVANT et APRES chaque push, et a chaque tour de travail qui touche `docs/` (decision d'Eric du 2026-10-25).

## Sortie et codes de retour
Sortie par defaut : une ligne par dossier (`etat` tronque a 9 caracteres, `fichiers/minimum`, chemin, puis `[EN PROD]` si applicable), suivie de `bilan : N problemes sur N dossiers du manifeste`.

Etats possibles par dossier : `OK`, `MANQUANT`, `MAIGRI (n < mini)`, `FICHIER ABSENT (...)`, `PRESENT EN PROD, interdit`. S'ajoute la liste des dossiers `NON DECLARE dans le manifeste`.

- Code 0 : aucun probleme (`ok: true` en JSON) ; en `--quiet`, la ligne unique est imprimee.
- Code 1 : au moins un probleme (dossier manquant, dossier maigri, ou dossier present en prod) - ne rien pousser, prevenir Eric.

## Limites
- Lecture seule : le script n'ecrit rien, ne cree, ne restaure ni ne supprime aucun dossier ou fichier ; il ne pousse rien.
- Les chemins `docs` et `H:\docs` sont codes en dur : aucun argument ne permet de controler une autre racine.
- La liste vient du manifeste de Claude : ce script le lit, ne l'ecrit jamais et n'a pas de `--maj` (cette option appartient a `Check_XX_presents.py`, sur ordre d'Eric). Un manifeste absent ou illisible donne `MANIFESTE ABSENT` et le code 1.
- Le comptage est recursif (`os.walk`) mais exclut tout fichier dont le nom contient `.bak` ; il compte des fichiers, pas leur contenu ni leur md5.
- Pour l'entree `99_docs_MD_system` (dans `LOCAL_SEUL`), la prod n'est jamais consultee : un `99_` en prod ne serait pas signale par ce script.
- En mode `--quiet`, rien n'est imprime quand un probleme existe : seul le code de retour 1 le signale.
- Il ne verifie pas GitHub, seulement le local et `H:\docs`.
