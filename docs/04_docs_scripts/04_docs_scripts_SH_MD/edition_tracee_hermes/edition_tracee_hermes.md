# edition_tracee_hermes.py - modele d'edition tracee (.bak, MD5, journal MODIFS)

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
Modele d'edition tracee, a copier puis adapter (le docstring le dit : « A COPIER puis adapter ..., pas a importer »). Il fournit cinq fonctions :

- `md5(p)` : empreinte MD5 du fichier, tronquee aux 8 premiers caracteres hexadecimaux.
- `stamp()` : horodatage `%Y_%m_%d_%Hh%Mm%Ss` a l'heure reelle (un `.bak` date du futur se verrait a l'audit).
- `rec(action, path, av, ap, raison, bak="-")` : ajoute une ligne au journal MODIFS ; si le journal n'existe pas, il le cree d'abord avec l'entete `# MODIFS <date du jour> - hermes`.
- `edit(path, pairs, raison=RAISON)` : verifie que chaque motif `old` est present exactement une fois, copie le fichier en `<chemin>.bak_<stamp>`, applique les remplacements, recalcule le MD5, puis n'ecrit la ligne de journal que si le MD5 a change.
- `corbeille(path, dossier=False)` : suppression par la corbeille Windows (`SendToRecycleBin` via `Microsoft.VisualBasic.FileIO.FileSystem`, appele en PowerShell `-NoProfile`), avec recontrole d'absence apres l'appel.

Le bloc `__main__` parcourt la liste `EDITS` (triplets chemin / liste de paires / raison) et appelle `edit()` pour chacun. La constante `BS = chr(92)` sert a fabriquer des antislashs sans passer par un heredoc.

Le docstring explique pourquoi le fichier existe : construit dans un heredoc bash, un chemin Windows litteral perd ses antislashs (`historique\03_RAPPORTS` arrive comme l'octet 0x03, `\n` comme un saut de ligne), le resultat ecrit dans les fichiers et dans le journal est corrompu et ne se voit qu'a la relecture. D'ou la methode : ecrire le script avec `write_file`, chemins en chaine brute `r"..."` ou en `chr(92)`, puis relire le fichier ecrit.

## Emplacement
- Script (copie maitre) : `docs\04_docs_scripts\04_docs_scripts_SH\edition_tracee_hermes\edition_tracee_hermes.py`
- Original vivant : `D:\hermes\skills\journal-modifs\templates\edition_tracee.py` (contenu identique, 3383 octets)
- Journal vise par defaut (constante `J`, a adapter) : `C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\01_MODIFS_IA\MODIFS_2026-10-24_hermes.md`

## Lancement
`python edition_tracee_hermes.py`

Aucun argument, aucune option : tout se regle dans le fichier avant l'appel.
- `J` : chemin du journal du jour, sous le commentaire `# --- adapter : journal du jour`.
- `RAISON` : raison par defaut, chaine vide, annotee « raison par defaut, courte, sans secret ».
- `EDITS` : un triplet par fichier, `(chemin, [(ancien, nouveau), ...], "raison courte")`. La liste est vide par defaut (seule une ligne commentee en exemple) : tel quel, le script ne modifie rien.

## Sortie et codes de retour
Le script n'appelle jamais `sys.exit` : code de retour 0 quand tout s'est deroule, exception Python qui remonte sinon. Lignes imprimees :

- motif absent ou present plusieurs fois : `REFUS <chemin> : motif present <n> fois -> <70 premiers caracteres du motif>` ; rien n'est ecrit.
- ecriture sans changement reel : `AUCUN CHANGEMENT sur <chemin> (MD5 identique) : pas de ligne de journal`.
- edition reussie : `<chemin> : <md5 avant> -> <md5 apres> | <nom du .bak>`.
- corbeille : `corbeille <chemin> : parti=True|False`.

Ligne de journal ecrite par `rec()` :

`<AAAA-MM-JJ HH:MM:SS> | hermes | <action> | <chemin> | avant=<md5> apres=<md5> | <raison> ; bak : <nom du .bak>`

`edit()` y passe l'action `MODIFIE`. Journal et fichiers edites sont ouverts en UTF-8 avec `newline=""`, et la ligne se termine par un `\r\n` explicite.

## Limites
- Tout ou rien par fichier : un seul motif qui n'apparait pas exactement une fois annule l'edition de tout le fichier (ni `.bak`, ni ecriture), et `edit()` renvoie `None` sans autre signal que le message `REFUS`.
- Pas de mode simulation, pas de `--help`, pas d'argument : pour verifier, on relit le fichier ecrit ; pour changer de cible, on edite `J`, `RAISON` ou `EDITS`.
- `edit()` ne teste pas l'existence du chemin : un chemin faux leve `FileNotFoundError` des la lecture.
- Le `.bak` est copie et le fichier reecrit avant le controle `av == ap` : en cas de MD5 identique il reste un `.bak` horodate, seul le journal n'est pas touche.
- `corbeille()` interpole le chemin entre apostrophes dans une commande PowerShell : un chemin contenant une apostrophe casse la commande. Le seul controle est l'absence du chemin apres l'appel (`parti=`) ; le script ne verifie pas ou l'element est parti.
- `md5()` charge le fichier entier en memoire et tronque l'empreinte a 8 caracteres : pas adapte a de gros binaires.
- Le journal n'est cree qu'a la premiere ligne reellement ecrite : une edition refusee ne cree pas `J`.
