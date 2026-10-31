# verif_ecriture_hermes.py - controle d'une ecriture (MD5, taille, lignes, octets de controle)

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
Controle une ecriture fichier par fichier, en lecture seule : MD5 tronque a 8 caracteres hexadecimaux, taille en octets, nombre de lignes physiques (`splitlines`), octets de controle presents et nombre de caracteres non-ASCII distincts.

Le script porte son propre mode d'emploi : un fichier de journal ou de message doit sortir avec `lignes=2` (entete + 1 ligne) et `controle=aucun`. Tout `0x01`, `0x03` ou saut de ligne supplementaire signale un antislash mange par une sequence d'echappement : restaurer le `.bak` et reecrire.

## Emplacement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\verif_ecriture_hermes\verif_ecriture_hermes.py` (51 lignes)
- Original vivant : `D:\hermes\skills\autonomous-ai-agents\hermes-aligne\scripts\verif_ecriture.py` (identique a la copie, md5 `9ae4b73589adddf8b528038e64263268`)
- Aucun fichier annexe : ni manifeste, ni configuration, ni dependance externe (seulement `hashlib`, `io`, `sys`).

## Lancement
`python "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\verif_ecriture_hermes\verif_ecriture_hermes.py" FICHIER [FICHIER ...]`

- Un ou plusieurs fichiers en arguments ; ils sont traites dans l'ordre.
- Sans argument : le script affiche son propre document (`__doc__`) et retourne 2.
- Une erreur sur un fichier n'arrete pas la boucle : les fichiers suivants sont quand meme traites.

## Sortie et codes de retour
Une ligne par fichier, au format `%-64s md5=%s taille=%d lignes=%d controle=%s nonascii=%d` :
- nom du fichier sur 64 colonnes, puis `md5=` (8 caracteres), `taille=` (octets bruts), `lignes=` (lignes physiques), `controle=` (`aucun` si la liste est vide, sinon les codes en hexadecimal), `nonascii=` (nombre de caracteres distincts de code superieur a 126).
- Fichier illisible : la ligne porte `ERREUR <message>` a la place du rapport.

Codes de retour :
- `0` : tous les fichiers ont ete lus et aucun ne contient d'octet de controle.
- `1` : au moins un fichier contient un octet de controle.
- `2` : au moins un fichier est illisible, ou aucun argument n'a ete fourni.

Le `2` prime sur le `1` : le code n'est eleve a 1 que s'il vaut encore 0, alors qu'une erreur de lecture force 2.

## Limites
- Le controle ne porte que sur les caracteres de code inferieur a 9 ou compris entre 14 et 31 : tabulation (`0x09`) et fins de ligne (`0x0A` a `0x0D`) passent sans alerte.
- La lecture se fait en `utf-8` avec `errors='replace'` : un fichier d'un autre encodage n'est pas denonce comme tel, il ressort en non-ASCII (le remplacement produit des caracteres hors ASCII).
- `nonascii` compte des caracteres distincts, pas des occurrences : 10 000 accents identiques donnent `nonascii=1`.
- Le MD5 est tronque a 8 caracteres : suffisant pour comparer deux etats, pas pour certifier un fichier.
- Aucune option : ni recursivite, ni filtre d'extension, ni mode `--quiet`, ni sortie JSON.
- Le script ne repare rien : il constate. La remise en etat passe par la restauration du `.bak` et la reecriture, hors de son perimetre.
