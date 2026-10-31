# renomme_chemins_trace_hermes.py - renommage trace de chemins dans un arbre

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
Remplace des chaines (ancien -> nouveau) dans les fichiers texte d'un arbre, en gardant la trace de chaque geste : un `.bak` horodate par fichier modifie, une ligne imprimee par fichier touche et un rapport texte depose dans le home. Les paires viennent d'un fichier JSON passe en argument ; elles sont appliquees de la chaine la plus longue a la plus courte, et un lookbehind negatif est pose automatiquement quand le nouveau nom finit par l'ancien (cas `prefixe + ancien`, type `04_docs_scripts_SH` vs `docs_scripts_SH`), pour ne pas re-prefixer.

## Emplacement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\renomme_chemins_trace_hermes\renomme_chemins_trace_hermes.py`
- Original vivant : `D:\hermes\skills\journal-modifs\scripts\renomme_chemins_trace.py`
- Paires : fichier JSON fourni par l'appelant, au format `[["ancien", "nouveau"], ...]` (chemin libre, passe en premier argument)
- Rapport : `~/rapport_renommage_<AAAA_MM_JJ_HHhMMmSS>.txt` (soit `C:\Users\Berry Swann\rapport_renommage_....txt` ici, chemin non parametrable)
- Sauvegardes : a cote de chaque fichier modifie, suffixe `.bak_<AAAA_MM_JJ_HHhMMmSS>` (meme horodatage pour toute la passe)

## Lancement
```
python renomme_chemins_trace_hermes.py paires.json --root D:\hermes --dry
python renomme_chemins_trace_hermes.py paires.json --root D:\hermes
```
- `--dry` : simulation, aucune ecriture et aucun `.bak` ; la colonne `apres=` vaut `-`.
- Sans `--root` : la racine est le dossier courant (`os.getcwd()`).
- Seules ces extensions sont lues : `.md`, `.py`, `.txt`, `.yaml`, `.yml`, `.json`, `.sh`, `.ps1`, `.vbs`, `.bat`.
- Dossiers ignores : `.git`, `.curator_backups`, `__pycache__`, `sessions`, `composer-pastes`, `cache`, `logs`, `node_modules`, `venv`, `.venv`, `.archive`, `cron`.
- Fichiers ignores : `.bak`, `.bak_*`, `.pyc`.
- Fichiers non decodables en UTF-8 ou illisibles : sautes sans message.
- Fin de ligne preservee telle quelle (lecture et ecriture en `newline=""`), la casse des extensions est ignoree au filtrage (`.MD` accepte).

## Sortie et codes de retour
Une ligne par fichier reellement modifie (rien pour les autres) :
```
<chemin> | avant=<8 premiers car de md5> apres=<8 premiers car de md5> | <ancien>=<n> <ancien>=<n> ...
```
- `avant=` : md5 du fichier avant reecriture ; `apres=` : md5 apres reecriture, ou `-` en `--dry`.
- Les comptes sont donnes par regle ayant produit au moins un remplacement.
- Resume final : `fichiers : <N>` (suivi de ` (dry)` en simulation) puis `rapport : <chemin>`.
- Le rapport contient en tete `# bak suffixe : .bak_<horodatage>` puis les memes lignes ; il est ecrit meme si aucun fichier n'a ete modifie (rapport vide).
- Code retour : `2` si aucun argument n'est fourni (le script imprime alors son propre docstring), `0` sinon.

## Limites
- Le nom parle de chemins, le script ne renomme rien : il reecrit le **contenu** des fichiers. Aucun dossier ni fichier n'est renomme ou deplace.
- Aucune validation des arguments : `--root` sans valeur leve une `IndexError` ; `paires.json` absent, illisible ou JSON invalide leve une exception Python non geree (traceback), sans message propre.
- Remplacement litteral sans limite de mot (`\b`) : une chaine incluse dans un mot plus long est remplacee aussi ; le lookbehind ne couvre que le cas ou le nouveau nom finit par l'ancien.
- Les regles s'enchainent sur le texte deja modifie : un nom produit par une regle peut etre re-touche par une regle plus courte appliquee ensuite.
- Aucun retour arriere : les `.bak_` s'accumulent a chaque passe (un par fichier modifie), pas de nettoyage ni de restauration automatique.
- Ecriture du fichier entier, pas de correctif ligne a ligne ; le codec est `utf-8` strict (ni `utf-8-sig`, ni repli latin-1).
- Le rapport est toujours depose dans le home, sans option pour changer son emplacement ni le desactiver.
- Pas de mode verbeux ni de filtre par extension en ligne de commande : le perimetre est fige dans le script.
