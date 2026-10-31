# audit_huissier_hermes.py - proces-verbal d'audit du projet HA ReBuild (lecture seule)

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

*Cree le 2026-10-31 : copie maitre du script Hermes rangee dans le depot (ordre d'Eric)*

## Role
Execute les 7 passes d'audit d'un bloc et produit un proces-verbal horodate. Constats uniquement : le script ne modifie aucun fichier du projet.

- Passe 1 TREE : arborescences LOCAL / PROD / GITHUB (`docs`), comptages par sous-arbre et ecarts de structure (seulement LOCAL, seulement PROD, seulement GITHUB).
- Passe 2 MD5 TRIGUL : deleguee a `md5_docs.py` (docs, LOCAL <-> PROD <-> GITHUB, LOCAL = verite) et `md5_prod.py` (hors docs, PROD et GITHUB doivent etre identiques), md5 brut et md5 normalise LF.
- Passe 3 DEPENDANCES : presence et en-tete de la matrice, headers CHAINE DE DEPENDANCES des YAML de config, references de fichiers cassees, vignettes `LxCx` introuvables.
- Passe 4 ENTITY INDEX : entites des YAML actifs contre la matrice (non referencees, fantomes), par domaine.
- Passe 5 FORMAT sur la PROD `H:` : deleguee a `check_box_ascii.py` (boites ASCII) et `check_slug_name_uid.py` (slug, name, unique_id), plus controles residuels (headers obligatoires, caracteres typographiques interdits, nommage de fichier, tabulations).
- Passe 6 AUTOMATIONS : `automations.yaml` PROD contre les fichiers locaux (`docs/03`), avec differences, orphelins et archives locales.
- Passe 7 SCRIPTS : `scripts.yaml` PROD contre les `04_docs_scripts_YAML` locaux, et scripts `.sh` de `04_docs_scripts_SH` LOCAL contre PROD (md5 + diff).

## Emplacement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\audit_huissier_hermes\audit_huissier_hermes.py` (md5 `7aaae06dc6c82a26fff54647676d7a0a`, identique a l'original vivant `D:\hermes\skills\smart-home\ha-audit-huissier\scripts\audit_huissier.py`).
- Perimetre lu : LOCAL `C:/Users/Berry Swann/Documents/ReBuild`, PROD `H:/`, GITHUB = depot git sur `H:/` (`git ls-files`, `git HEAD` / `origin/main`).
- Matrice : `docs\00_IA\00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire\DEPENDANCES_GLOBALES_CLAUDE_memoire.md` ; YAML de config : `docs\01_docs_config_system\01_config_system_SH_PY_YAML` ; dashboard (vignettes) : `docs\02_docs_dashboard\02_dashboard_docs_YAML`.
- Sorties : `%LOCALAPPDATA%\Temp\audit_huissier\` (hors projet).
- Sous-scripts importes depuis le dossier du script : `md5_docs.py` et `md5_prod.py` (passe 2), `check_box_ascii.py` et `check_slug_name_uid.py` (passe 5), `check_automations.py` (passe 6), `check_scripts.py` (passe 7). Seul le script principal est range dans ce dossier du depot.

## Lancement
`env -u PYTHONPATH python audit_huissier.py` (commande de l'en-tete du script)

Variante explicite du message d'erreur PyYAML, venv hermes-agent en Python 3.11 :
`env -u PYTHONPATH "C:/Users/Berry Swann/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe" audit_huissier.py`

## Sortie et codes de retour
- Console : ligne d'en-tete `AUDIT HUISSIER - AAAA-MM-JJ HH:MM - lecture seule`, puis une ligne `[OK]` ou `[ERREUR]` par passe, puis les deux chemins de rapports et un resume (TREE, MD5, DEPS, ENTITY, BOX, IDENT, RESIDU, AUTOM, SCRIPTS).
- PV : `%LOCALAPPDATA%\Temp\audit_huissier\PV_audit_AAAA-MM-JJ_HHMM.md` (markdown, sections par passe, details replies en blocs `<details>`).
- Details : `%LOCALAPPDATA%\Temp\audit_huissier\audit_details.json` (resultats des 7 passes, `indent=1`, `ensure_ascii=False`).
- Codes de retour : aucun `sys.exit` en fin de `main()` et aucune exception remontee par une passe (chaque passe est entouree d'un `try/except` qui enregistre `{"pass": ..., "error": ...}`) : sortie normale en code 0 meme si des passes echouent. Seul arret en erreur : `SystemExit("ERREUR: PyYAML absent de cet interpreteur ...")` si `import yaml` echoue.

## Limites
- Lecture seule sur le projet : les seules ecritures sont le PV et le JSON dans `%LOCALAPPDATA%\Temp\audit_huissier\`. Aucune correction, aucune mise a jour de fichiers.
- PyYAML obligatoire dans l'interpreteur ; le venv hermes-agent (Python 3.11) est celui indique par le script.
- L'en-tete annonce 5 passes, la liste `steps` de `main()` en execute 7 (PASSE 6 AUTOMATIONS et PASSE 7 SCRIPTS comprises).
- Les passes 2, 5, 6 et 7 dependent de 6 sous-scripts presents dans le meme dossier ; sans eux l'import leve une exception, la passe est notee `[ERREUR]` et le PV continue.
- Chemins en dur : LOCAL, PROD `H:/`, repo git `H:/`. Le disque `H:` doit etre monte ; les erreurs git sont renvoyees en texte (`<git error: ...>`) avec un timeout de 180 s.
- Perimetre filtre : extensions `.md`, `.yaml`, `.yml`, `.sh`, `.py`, `.txt`, `.json` ; dossiers exclus `__pycache__`, `.git`, `_old`, `backup`, `historique`, `CLAUDE_backup`, `_old_avant_staging` ; fichiers `.bak_` ecartes. Passe 5 : a la racine de `H:` seuls les dossiers `sensors`, `templates`, `utility_meter`, `command_line`, `groups`, `input_booleans`, `shell_command`, `input_number` sont lus.
- Listes tronquees dans le PV : 80 fichiers par ecart d'arborescence, 120 ecarts MD5, 150 entites non referencees, 80 fantomes, 150 fichiers par detail, 10 ecarts par fichier, 25 modifications git, 40 archives ou orphelins. Le JSON `audit_details.json` garde les structures completes des passes.
- Passe 4 : une seule version par (dossier, nom sans date) est retenue, la plus recente par date dans le nom ; les dossiers d'archive sont ignores.
- Si la passe 1 echoue, son resultat n'a pas de cle `sections` et le resume console leve un `KeyError` apres l'ecriture du PV et du JSON.
