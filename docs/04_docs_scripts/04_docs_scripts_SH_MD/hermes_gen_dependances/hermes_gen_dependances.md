# hermes_gen_dependances.py - generateur de DEPENDANCES_GLOBALES_HERMES_V1.md

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

*Cree le 2026-10-31 : copie maitre du script rangee dans le depot (ordre d'Eric)*

## Role
Genere le document de dependances du tableau de bord HA a partir de l'arbre local ReBuild. Lecture des quatre sous-arbres de `ReBuild/docs` cites en Emplacement, plus `scripts\annotations_v1.json` et, en lecture seule, `H:\` ; ecriture limitee au seul fichier de sortie, en local.

Le script reconstruit six blocs :
- `MATRICE DES VIGNETTES` : une ligne par dossier `L0C0_...` a `L6C3_...` avec nombre d'entites et de cartes.
- `1. VIGNETTES DASHBOARD` : par vignette, la chaine de dependances (NAT/TPL/SEN/UM -> fichiers de definition -> vignette), la liste des entites consommees, les fichiers de config deployables avec leur statut prod, puis les YAML du dossier dashboard.
- `2. SCRIPTS .SH` : chaque `.sh` avec les entites HA qu'il cite.
- `3. AUTOMATIONS` : par pole, nombre de fichiers YAML, d'automations (`alias:`) et d'entites.
- `4. SCRIPTS NON-SH` : chaque `.py` avec son nombre d'entites.
- `5. ENTITES ORPHELINES` : entites definies dans la config mais presentes dans aucun dashboard, aucune automation, aucun script, avec type et fichier source.

Les types sont deduits de l'emplacement du fichier de definition dans `01_config_system_SH_PY_YAML` : `templates/` -> `TPL`, `sensors/` -> `SEN`, `utility_meter/` -> `UM`, `command_line/` et tout le reste -> `NAT`.

Regle de detection des entites : expression `domaine.objet` sur la liste `DOMAINES` du script (binary_sensor, sensor, switch, light, ... zone, scene). Les commentaires sont retires avant la recherche (`nettoie`) : un commentaire qui cite une entite supprimee (cas `binary_sensor.meteoalarm`, c20261025-01) ne doit pas la faire revivre dans le document. Les cartes sont comptees par les lignes `type: ...`. Les `.bak` et les `__pycache__` sont ignores.

Exception `L0C0` : les fichiers `Page_*.yaml` de la vignette `L0C0` ne sont pas comptes, sinon les 18 autres vignettes sont absorbees dans `L0C0`.

Si `scripts/annotations_v1.json` existe, ses annotations par code de vignette sont reinjectees sous le titre de chaque vignette ; fichier absent ou illisible = aucune annotation, sans erreur.

## Emplacement
- Script (copie maitre decrite ici) : `docs\04_docs_scripts\04_docs_scripts_SH\hermes_gen_dependances\hermes_gen_dependances.py`
- Original vivant, identique au bit pres : `ReBuild\scripts\hermes_gen_dependances.py`
- Sortie par defaut : `docs\99_docs_MD_system\DEPENDANCES_GLOBALES_HERMES\DEPENDANCES_GLOBALES_HERMES_V1.md`
- Entrees lues : `docs\02_docs_dashboard\02_dashboard_docs_YAML` (vignettes), `docs\01_docs_config_system\01_config_system_SH_PY_YAML` (definitions), `docs\03_docs_automations\03_docs_automations_YAML` (poles, dossiers `XX_` ignores), `docs\04_docs_scripts\04_docs_scripts_SH` (`.sh` et `.py`), `scripts\annotations_v1.json` (optionnel)
- Lecture seule sur la prod : `H:\` sert uniquement a comparer le md5 de chaque fichier de config (statut `identique`, `different`, `absent en prod`, `prod inaccessible`, `illisible`). Rien n'est ecrit en prod, rien sur GitHub.

## Lancement
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\hermes_gen_dependances\hermes_gen_dependances.py"`

Variante avec sortie ailleurs : `... hermes_gen_dependances.py --out "C:\chemin\fichier.md"` (`--out` prend l'argument suivant dans `sys.argv` ; le dossier de destination est cree si besoin).

Le script affiche trois lignes : le chemin ecrit, le nombre de lignes et d'octets, puis le resume `vignettes N | entites definies N | referencees N | orphelines N`.

## Sortie et codes de retour
- Fichier ecrit en UTF-8, fins de ligne `\n` (LF), dossier cree par `os.makedirs(..., exist_ok=True)`.
- Structure du fichier : titre `# DEPENDANCES GLOBALES HERMES - TABLEAU DE BORD HA`, deux lignes d'italique (origine de la reconstruction, date de generation et regles), `## LEGENDE`, `## MATRICE DES VIGNETTES`, `## SOMMAIRE`, sections 1 a 5, puis `## STATISTIQUES` (vignettes, entites definies, referencees, orphelines, scripts .sh, scripts non-sh, poles d'automations, cartes au total).
- Code 0 : generation terminee, `ecrit : <chemin>` affiche. Le script ne fait aucun `sys.exit` : un fichier de sortie ecrit signifie succes.
- Code non nul : exception Python non rattrapee (par exemple `--out` sans argument -> `IndexError`, ou dossier de sortie non inscriptible). Aucune generation partielle n'est annoncee : le fichier n'est ecrit qu'a la fin, en une seule passe.
- Les erreurs de lecture d'un fichier source sont silencieuses (`lire` rend une chaine vide sur `OSError`) : un YAML illisible est compte comme vide, pas comme erreur.

## Limites
- Ne jamais ecraser l'en-tete de 8 badges du fichier genere : le script ouvre la sortie en mode `w` et n'ecrit que son propre titre, sa legende et ses sections. Le bloc de badges ajoute au document n'est pas reproduit ; s'il est present, il faut le remettre apres chaque generation.
- Le document est entierement reecrit a chaque passage : aucune fusion, aucune conservation de retouche manuelle hors `annotations_v1.json`.
- Reconstruction assumee, pas une copie de l'ancien generateur : le script produit la meme structure de sections avec ses propres regles explicites, il ne pretend pas reproduire l'ancien a l'identique.
- Les entites ne sont vues qu'en texte : une entite construite dynamiquement (template, concat, secret) echappe a l'expression reguliere et peut ressortir fausse orpheline.
- Les types dependent du premier segment de dossier sous `01_config_system_SH_PY_YAML` : un fichier range ailleurs tombe en `NAT`.
- Le statut prod ne vaut que si `H:\` est monte au moment du lancement ; sinon tout est marque `prod inaccessible`.
- 365 lignes, aucune dependance externe (stdlib : os, re, sys, json, datetime, collections, hashlib).
