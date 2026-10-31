# boite_claude_watch_hermes.py - veille de la boite aux lettres Claude

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
Surveille la boite aux lettres Claude (`D:\Discussion_Claude_Hermes`) et ne sort un message que si un fichier `*_claude.md` change ou apparait. Le message dit QUEL fichier a change, COMBIEN de lignes sont nouvelles et QUELS identifiants de messages sont concernes, avec un apercu. Sortie vide = rien a signaler.

Mecanique, telle qu'ecrite dans le script (quatre fonctions, aucune dependance hors bibliotheque standard) :

- `scan()` : `os.listdir(DIR)` trie, ne retient que les noms finissant par `_claude.md` qui sont des fichiers ; pour chacun, empreinte MD5 (`md5_file`, blocs de 65536 octets) et nombre de lignes (`read_lines`, UTF-8, `errors="replace"`). Dossier illisible = `None`.
- Etat courant compare a l'etat precedent lu dans `STATE` (JSON). JSON illisible, objet vide, ou valeur non-dict : l'etat precedent est ignore.
- Fichier nouveau : toutes ses lignes sont "nouvelles" et l'entete dit `nouveau fichier`. Fichier modifie : lignes nouvelles = difference entre le nombre de lignes actuel et l'ancien, bornee a zero ; si la difference est nulle, seule la derniere ligne est examinee et l'entete annonce `1 nouvelle(s) ligne(s)`.
- Identifiants : expression reguliere `\|\s*([ch]\d{8}-\d{2})\s*\|` cherchee dans les lignes nouvelles ; les 4 derniers sont affiches (`id : ...`).
- Apercu : derniere ligne nouvelle non vide, ne commencant pas par `#` et contenant un `|`, nettoyee par `clean()` (seuls les caracteres de code 32 a 126 et les espaces sont gardes, espaces compresses), tronquee a 260 caracteres avec ` ...` en suffixe si depassement.
- Au plus 4 fichiers par message (`MAX_FILES = 4`), parcourus par ordre alphabetique.

## Emplacement
- Copie maitre (ce depot) : `docs\04_docs_scripts\04_docs_scripts_SH\boite_claude_watch_hermes\boite_claude_watch_hermes.py`
- Original vivant : `D:\hermes\scripts\boite_claude_watch.py` (3319 octets, md5 `e5c51f080d96304ab3cd1c669e039052`, identique a la copie ci-dessus)
- Boite surveillee : `D:\Discussion_Claude_Hermes`, surchargeable par la variable d'environnement `BOITE_CLAUDE_DIR`
- Fichier d'etat : `D:\hermes\scripts\.boite_claude_state`, surchargeable par la variable d'environnement `BOITE_CLAUDE_STATE`

## Lancement
`python -I -X utf8 "D:\hermes\scripts\boite_claude_watch.py"`

- Aucun argument n'est lu : tout se regle par `BOITE_CLAUDE_DIR` et `BOITE_CLAUDE_STATE`.
- Test hors boite reelle : forcer ces deux variables vers un dossier et un fichier d'etat jetables.
- Le script ne fait que constater : une sortie vide laisse la main, un message se termine par l'invitation a lire dans la session.

## Sortie et codes de retour
Les quatre sorties explicites du script sont des `SystemExit(0)` : cette veille ne signale jamais d'anomalie par un code non nul.

- Code 0, aucune sortie : dossier absent ou illisible, aucun `*_claude.md`, etat identique au precedent, premier passage (aucun etat enregistre), ou aucune difference exploitable. Silence = rien a signaler.
- Code 0, message en trois parties, sur stdout :
  - `Boite aux lettres Claude, changement detecte.`
  - une ligne `- ` par fichier retenu, au format `nom : N nouvelle(s) ligne(s) | id : c20261031-01, ... | apercu` (la partie `id` n'apparait que si un identifiant est trouve, l'apercu que s'il en existe un) ; pour un fichier inconnu de l'etat : `nom : nouveau fichier, N ligne(s)`.
  - `A lire dans la session (instruction de Claude = decision d'Eric depuis le 2026-10-24).`
- Le fichier d'etat est reecrit (JSON, `sort_keys=True`) des qu'une difference est constatee, avant l'emission du message.
- Cas non interceptes : l'ecriture de l'etat et le calcul MD5 ne sont pas proteges par `try`, une erreur disque a cet endroit remonterait en traceback (code non nul), sans message formate.

## Limites
- Filtre par nom uniquement : seuls les `*_claude.md` sont vus ; les `*_hermes.md` et tout fichier d'un autre nom ne sont jamais surveilles, meme modifies.
- Un seul niveau : `os.listdir(DIR)` ne descend pas dans les sous-dossiers ; un fichier `*_claude.md` range plus profond n'est jamais vu.
- Detection par MD5 et nombre de lignes, sans memorisation du contenu : une modification a nombre de lignes constant est bien detectee, mais le message annonce alors `1 nouvelle(s) ligne(s)` et n'affiche que la derniere ligne, les identifiants eventuels des autres lignes modifiees sont perdus.
- Etat ecrit avant le message : si la sortie n'est pas lue, le changement est deja consomme et ne sera plus signale au tour suivant.
- Plafond de 4 fichiers par message : les fichiers au-dela du quatrieme ne sont pas decrits dans ce passage, alors que l'etat les a deja enregistres.
- Identifiants et apercu sont des extraits : 4 identifiants au maximum, 260 caracteres d'apercu, et `clean()` supprime tout caractere hors ASCII imprimable (accents compris) — l'apercu n'est pas le texte d'origine.
- Aucun verrou sur le fichier d'etat : deux instances simultanees peuvent s'ecraser mutuellement l'etat.
- Le message ne porte ni horodatage ni heure de modification ; il ne dit pas quand le changement a eu lieu.
