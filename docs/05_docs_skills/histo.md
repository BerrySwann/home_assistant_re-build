---
name: histo
description: "Skill HA ReBuild - genere un journal de bord ultra-compact et le sauvegarde, puis enchaine automatiquement le sync_index (DEPENDANCES_GLOBALES.md, docs impactees, INDEX_GLOBAL.md), le journal fusionne et la copie Obsidian et le menage des sauvegardes .bak puis la mise a jour du tree (IA_ARBO_DETAIL.md). Declencher OBLIGATOIREMENT quand l'utilisateur tape /histo, demande un journal de bord, genere l'histo, fais un resume a sauvegarder, cree un log de session, exporte l'historique. Usage typique : fin de session, avant de fermer Cowork."
---

# Skill : /histo - Journal de bord + sync_index (dont INDEX_GLOBAL) + journal fusionne + copie Obsidian + menage .bak + tree

## Objectif

Six actions enchainees sans interruption :
1. Generer et sauvegarder le journal de bord de session
2. Executer le sync_index (DEPENDANCES_GLOBALES.md, docs impactees, INDEX_GLOBAL.md)
3. Mettre a jour le JOURNAL FUSIONNE (historique/) avec la session qui vient d'etre ecrite
4. Copier le journal de session et le journal fusionne dans le coffre Obsidian
5. Faire le menage des sauvegardes (.bak) du perimetre docs, selon la REGLE DE SAUVEGARDE (etape 5)
6. Mettre a jour les tree : IA_ARBO_DETAIL.md (comptages local, prod, GitHub), avec le skill update-arbo (etape 6)

Ne jamais demander confirmation entre les etapes. Les faire dans la foulee.

---

## ETAPE 1 - JOURNAL DE BORD

### Collecter depuis l'historique de la conversation

- Date du jour (depuis env ou bash)
- Numero de session du jour (S1, S2, S3... selon les histo deja presents dans `historique/`)
- Fichiers YAML modifies/crees/valides (chemin court sous `docs/`)
- Entites creees ou corrigees (unique_id ou alias)
- Erreurs rencontrees et leur resolution
- Tache en cours ou terminee
- Backlog TODO.md si mentionne en session
- Prochaine action prioritaire

### Format de sortie obligatoire (Markdown mis en forme, depuis le 2026-10-08)

Le journal est du vrai Markdown (titres, gras, pastilles de couleur, icones), pas un bloc de code. Gabarit :

```
# 📓 Journal HA ReBuild - **[DATE]** (Session **S[N]**)

- ⏱️ **Session** : [duree estimee ou "N/A"]
- 🌿 **Branche active** : `docs/`

## ✅ Fichiers valides
- 🟢 `chemin/court/fichier.yaml` - [entite(s) concernee(s)] **[v]**
- ...

## 🟠 En cours
- 🟠 `fichier ou tache` - **[draft]** ou **[a tester]** ou **[a deployer]**
- (aucun si session terminee proprement)

## 🔴 Erreurs resolues
- 🔴 `fichier` : [type erreur] -> [correction appliquee] **[resolu]**
- (aucune si session propre)

## 📋 Taches backlog (TODO.md)
- 📌 [items identifies en session, si applicable]

## 🎯 Prochaine action
- [action prioritaire identifiee]

*Fin du journal*
```

Regles de mise en forme :
- Toute date est en gras (`**2026-10-08**`), dans le titre comme dans le texte.
- Tout commentaire ou etat entre crochets est en gras : `**[v]**`, `**[a tester]**`, `**[draft]**`, `**[a deployer]**`, `**[resolu]**`, `**[EN COURS]**`.
- Pastilles de couleur : 🟢 valide ou termine, 🟠 en cours ou a tester, 🔴 erreur, 🔵 information. Une icone par titre de rubrique comme dans le gabarit.
- Chemins, IDs d'entites et commandes en code inline (accents graves).
- Cette mise en forme s'applique uniquement aux NOUVEAUX journaux `histo_*.md`. Les anciens journaux, INDEX_GLOBAL.md et les autres fichiers restent inchanges et sans emoji (exception d'emojis accordee par Eric le 2026-10-08, limitee aux nouveaux journaux histo). Les nouveaux blocs de session du journal fusionne ont seulement le gras, sans emoji (etape 3).

### Sauvegarde obligatoire

- Determiner le numero de session : lister `historique/` (fichiers `.md` ET anciens `.txt`) et choisir le suffixe suivant (ex : si `histo_2026-08-08_s2.txt` ou `histo_2026-08-08_s2.md` existe -> creer `histo_2026-08-08_s3.md`)
- Sauvegarder dans `C:\Users\Berry Swann\Documents\ReBuild\historique\histo_[YYYY-MM-DD]_s[N].md` : le journal est ecrit en Markdown mis en forme, tel que defini ci-dessus, sans le placer dans un bloc de code (sinon gras et icones ne s'affichent pas). Les anciens `histo_*.txt` restent tels quels (pas de conversion).
- Presenter le fichier avec `mcp__cowork__present_files` (si l'outil n'est pas disponible, le dire dans le rapport final, ne pas bloquer)

### Regles

- Chemins courts (ex : `docs/01_docs_config_system/config_system_YAML/sensors/P1_kWh_clim.yaml`)
- IDs matrice pour les vignettes (L2C1, L1C3, etc.)
- Si session vide : indiquer `SESSION VIDE - aucune modification`
- Bloc autonome : lisible sans contexte par quelqu'un qui reprend le projet plus tard

---
## ETAPE 2 - SYNC_INDEX (enchaine automatiquement, sans demander)

Immediatement apres la sauvegarde du journal, executer le sync_index complet.

### Perimetre

| Type de fichier modifie | Index a mettre a jour |
|:---|:---|
| Config YAML (sensors, templates, utility_meter...) | `DEPENDANCES_GLOBALES.md` + `INDEX_GLOBAL.md` |
| Automation | `docs/03_docs_automations/docs_automations_MD/{nom}.md` + `INDEX_GLOBAL.md` |
| Script | `docs/04_docs_scripts/docs_scripts_YAML_MD/{nom}.md` + `INDEX_GLOBAL.md` |
| Tout type impactant une vignette | `DEPENDANCES_GLOBALES.md` |
| Fichier ajoute, renomme ou supprime (helper, export, fiche) | `INDEX_GLOBAL.md` |
| Skill du projet modifie (`.claude/skills/<skill>/SKILL.md`) | copie `docs/05_docs_skills/<skill>.md` |

**Chemins Windows :**
- `C:\Users\Berry Swann\Documents\ReBuild\docs\02_docs_dashboard\dashboard_docs_MD\DEPENDANCES_GLOBALES.md`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\03_docs_automations\docs_automations_MD\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_YAML_MD\`
- `C:\Users\Berry Swann\Documents\ReBuild\Github\INDEX_GLOBAL.md`

**Chemin bash sandbox :** detecter via `ls /sessions/` si necessaire (prefixe de session variable).

### Protocole

1. Identifier les fichiers modifies pendant la session (depuis le journal de bord qui vient d'etre genere)
2. Pour chaque fichier impactant DEPENDANCES_GLOBALES.md : mettre a jour la date en tete de fichier
3. Pour chaque automation validee : verifier/mettre a jour son `.md` dans `docs_automations_MD/`
4. Pour chaque script valide : verifier/mettre a jour son `.md` dans `docs_scripts_YAML_MD/`
5. Mettre a jour `INDEX_GLOBAL.md` (voir ci-dessous)
6. Si un `.md` de doc est absent : le signaler (ne pas bloquer)
7. Pour chaque skill du projet modifie pendant la session : recopier son `SKILL.md` vers `docs/05_docs_skills/<skill>.md` (sauvegarde locale `.bak_AAAA_MM_JJ_HHhMMmSSs` du fichier existant avant ecrasement), puis pousser vers `H:\docs\05_docs_skills\` apres comparaison MD5. Seul le fichier courant est pousse, jamais un `.bak`.

### Mise a jour de INDEX_GLOBAL.md

Fichier : `C:\Users\Berry Swann\Documents\ReBuild\Github\INDEX_GLOBAL.md` (copie locale uniquement, il n'existe pas de circuit de push pour lui ; ne pas le pousser).

1. Si aucun fichier de la session n'est ajoute, renomme, supprime ou deplace, et qu'aucune entite citee n'a change : noter "INDEX_GLOBAL deja a jour" et passer a l'etape suivante.
2. Sinon, faire d'abord une sauvegarde dans le meme dossier : `INDEX_GLOBAL.md.bak_AAAA_MM_JJ_HHhMMmSSs` (format PowerShell `Get-Date -Format "yyyy_MM_dd_HH'h'mm'm'ss's'"` ; le dossier Github est hors perimetre du menage de l'etape 5).
3. Ne reecrire que les lignes concernees, jamais le fichier entier :
   - ajouter une entree pour chaque nouveau fichier (automation, script, helper YAML, fiche), dans la section de son type, a cote des entrees voisines, avec le meme format que celles-ci
   - mettre a jour les entrees renommees ou supprimees
   - mettre a jour les compteurs de section concernes (par exemple le nombre d'automations ou de fichiers de scripts) en les recomptant, sans les deduire de l'ancien nombre
   - mettre a jour la ligne d'en-tete de date
4. Garder le format du fichier : CRLF, UTF-8 sans BOM.
5. Controles apres ecriture : le fichier se relit en UTF-8, les compteurs modifies correspondent au nombre d'entrees, les liens ajoutes pointent vers des fichiers qui existent. Les entites ajoutees doivent avoir ete verifiees en live ou lues dans un fichier de la session, jamais recopiees de memoire.
6. Les ecarts deja presents avant la session (entites citees qui ne repondent plus, desequilibres de compteurs) ne sont pas corriges ici : les mentionner dans le rapport s'ils concernent la session.
7. Note pour ha-trigul : `INDEX_GLOBAL.md` apparait en DIFF local contre prod et repo, c'est attendu tant qu'il reste local seulement.

### Regles sync_index

- Ne reecrire que les lignes concernees - pas le fichier complet (economie tokens)
- Si aucune dependance impactee : noter "Index deja a jour" dans le rapport final
- Chemin bash sandbox : toujours verifier avec `ls /sessions/` si le prefixe est incertain

---
## ETAPE 3 - JOURNAL FUSIONNE (enchaine automatiquement, sans demander)

Le journal fusionne est un seul fichier Markdown qui regroupe tous les journaux de session depuis le 2026-07-15. Il se lit en premier quand on reprend le projet : le FAIT en haut (par date), le RESTE A FAIRE en bas (par date).

**Dossier :** `C:\Users\Berry Swann\Documents\ReBuild\historique\`
**Nom :** `JOURNAL_FUSIONNE_2026-07-15_[DATE_FIN].md`, ou `[DATE_FIN]` = date de la derniere session incluse (format YYYY-MM-DD).

### Protocole

1. Reperer le fusionne le plus recent : `JOURNAL_FUSIONNE_*.md` (sans suffixe `.bak`), trie par date de fin dans le nom. Il sert de base.
2. Reperer les journaux `histo_*.md` et anciens `histo_*.txt` pas encore integres : comparer les dates et suffixes aux lignes `SESSION 2026-...` du fusionne. Y inclure celui qui vient d'etre ecrit a l'etape 1. Ne pas dependre de la seule date de modification des fichiers.
3. Lire chaque journal manquant en entier avant de l'integrer. Ne rien ajouter qui ne soit pas dans ces journaux (ni chiffre, ni etat, ni decision deduits). Un journal au format Markdown mis en forme (titres `##`, gras, icones) est integre au fusionne en ASCII : retirer les icones et pastilles, garder le fond (le gras du fusionne vient du format de bloc ci-dessous).
4. Construire le nouveau fichier a partir de la base, sans toucher au contenu existant :
   - ligne 2 d'en-tete : remplacer la date de fin dans `Periode : 2026-07-15 -> [DATE_FIN]` (la base utilise une fleche, ne changer que la date)
   - partie `PAR DATE - CE QUI A ETE FAIT` : ajouter un bloc par session, dans l'ordre chronologique, juste avant la ligne de titre `## **PAR DATE - CE QUI RESTE A FAIRE**` (le bandeau est un titre Markdown, hors bloc de code). Les blocs de session sont en vrai Markdown, hors bloc de code, pour que le gras s'affiche. Format du bloc (rubriques utiles seulement) :

         ### **SESSION [date] ([Sn]) - [duree] - [titre court]**

         **[FICHIERS VALIDES]**
         - ...

         **[ERREURS RESOLUES]**
         - ...

         **[DECISIONS]** / **[CONSTATS]**
         - ...

     Titre de session entier en gras, dates en gras, crochets en gras ; pas d'icone ni d'emoji dans le fusionne ; ASCII sauf les `**` du gras. Chemins en code inline. Session vide : une seule ligne `**SESSION [date] ([Sn], [heure]) : session vide - aucune modification depuis ...**`. Laisser une ligne vide avant et apres chaque bloc. Les anciennes sessions (titres et rubriques en gras, corps dans des blocs de code) ne sont pas modifiees.
   - partie `PAR DATE - CE QUI RESTE A FAIRE` : le bandeau est le titre `## **PAR DATE - CE QUI RESTE A FAIRE**`. Ajouter a la FIN du fichier, apres la derniere ligne ```, une entree par date en Markdown, le texte de chaque rubrique restant dans un bloc de code :

         ### **[date]**

         **[EN COURS]**

         (bloc de code ```text, contenu indente de 4 espaces, puis ```)

         **[PROCHAINE ACTION]**

         (bloc de code ```text, contenu indente de 4 espaces, puis ```)

         ### **ETAT ACTUEL AU [date] (soir, curated)**

         (bloc de code ```text : resume de l'etat courant et de ce qui reste ouvert, puis ```)

     Quand un item d'une entree plus ancienne a ete ferme depuis, le noter dans la nouvelle entree (par exemple `(ferme le 07/10)`), sans modifier l'ancienne. Le fichier se termine ainsi par une ligne ``` de fin de bloc de code.
5. Ecrire le nouveau fichier. Les blocs ajoutes sont en ASCII (pas de tiret long, pas de fleche, pas de caracteres speciaux, pas d'emoji ; seul le gras `**` est ajoute dans les nouveaux blocs de session) ; le contenu existant est repris tel quel, y compris ses caracteres speciaux.

### Regles

- Ne jamais ecraser un fusionne existant : un nouveau nom par nouvelle date de fin. Si le fichier cible existe deja (meme date de fin, nouvelle session du meme jour), le sauvegarder d'abord en `JOURNAL_FUSIONNE_..._[DATE_FIN].md.bak_AAAA_MM_JJ_HHhMMmSSs` puis le mettre a jour.
- L'ancien fusionne reste en place. Ne pas le supprimer sans demande.
- Format du fichier : CRLF, UTF-8 sans BOM, comme la base.
- Verifier apres ecriture : pas de BOM, aucun LF isole, un seul bandeau `RESTE A FAIRE`, le fichier se termine par la ligne ``` suivie d'une fin de ligne, nombre pair de lignes ``` (clotures equilibrees), nombre de lignes coherent avec base + ajouts.
- Ecrire par script (Python ou PowerShell) en passant les blocs par fichiers temporaires dans `%TEMP%` : une commande trop longue echoue (WinError 206). Ne jamais reconstituer le contenu existant a partir d'un affichage tronque : lire le fichier.
- Si la base est introuvable ou illisible : le signaler et s'arreter a cette etape, sans recreer tout le fusionne de memoire.

---

## ETAPE 4 - COPIE OBSIDIAN (enchainee automatiquement, sans demander)

**Dossier de destination :** `D:\Cerveau-Obsidian\14 Boulot\Journal\`

### A copier

- le fusionne qui vient d'etre ecrit a l'etape 3
- le journal `histo_[date]_s[N].md` de l'etape 1
- tous les `histo_*.md` / `histo_*.txt` plus recents que ceux deja presents dans le dossier Obsidian (cas d'un rattrapage)

### Regles

- Ne jamais ecraser un fichier existant du dossier Obsidian : s'il existe deja, ne pas le copier et le signaler. Seule exception : un fusionne de meme nom (mise a jour du meme jour), qui est ecrase SANS sauvegarde sur D: (regle : jamais de sauvegarde sur D:). La version precedente reste dans `historique\` (sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs` faite a l'etape 3).
- L'ancien fusionne reste dans le dossier Obsidian.
- Apres chaque copie, comparer le MD5 source / destination et le noter dans le rapport (`identique` ou `DIFFERENT`).
- Si `D:\` ou le dossier est inaccessible : le signaler dans le rapport, ne pas bloquer et ne pas creer d'autre dossier a la place.

---

## ETAPE 5 - MENAGE DES SAUVEGARDES (enchaine automatiquement, apres la copie Obsidian)

Applique la REGLE DE SAUVEGARDE du 2026-10-08 (definie dans CLAUDE.md). Tout se passe en LOCAL, jamais sur H: ni sur D:.

**Perimetre :** `C:\Users\Berry Swann\Documents\ReBuild\docs\00_*` a `05_*` (recursif) + `C:\Users\Berry Swann\Documents\ReBuild\Claude md SAVE\`.
**Hors perimetre (ne pas toucher) :** TODO, Github, historique, .claude, Infra_Proxmox. Ignorer aussi tout dossier `_ARCHIVE` / `ARCHIVE` et tout fichier dont le nom contient `_archive_` : ce sont des archives, pas des sauvegardes (ex : `_ARCHIVE\DEPENDANCES_GLOBALES_archive_2026-10-07_18h13.md`).

**"Poubelle" = corbeille Windows**, jamais de suppression definitive :
```powershell
Add-Type -AssemblyName Microsoft.VisualBasic
[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($f,'OnlyErrorDialogs','SendToRecycleBin')
```

### Principe de conformite (aucune exception)

Tout fichier du perimetre dont le nom porte une date ou un marqueur de sauvegarde, et qui ne suit pas
la REGLE DE SAUVEGARDE courante, est ramene aux regles. Aucun cas n'est laisse de cote sous pretexte
qu'il n'entre dans aucune famille : s'il porte une date ou un marqueur de sauvegarde, il est traite.

Deux cibles seulement :
- une version ou une sauvegarde -> `{nom_de_travail}.bak_AAAA_MM_JJ` (le nom de travail ne contient pas de date) ;
- la version courante d'un fichier de travail -> le nom sans date (`{nom}.ext`).

Un nom de fichier ne porte JAMAIS de date dans sa partie courante. En cas de doute (nom qui pourrait
etre un vrai document et non une sauvegarde), on signale et on ne touche pas.

### Formats reconnus (dans le perimetre uniquement)

| Famille | Exemple | Traitement |
|:---|:---|:---|
| A - sauvegarde horodatee | `fichier.yaml.bak_2026_10_07_21h14m05s` | voir protocole |
| B - sauvegarde finale | `fichier.yaml.bak_2026_10_07` | gardee, soumise au plafond de 3 |
| C - anciens `.bak` | `.bak_2026-09-28`, `.bak_20260929`, `.bak2_...`, `.bak-...` | renommes `fichier.yaml.bak_AAAA_MM_JJ` |
| D - fichiers de travail dates | `page_L4C2_proxmox_2026-06-18.yaml`, `fichier_2026-10-07_22h00.ext` | la plus recente devient le nom sans date `{nom}.ext` ; les autres deviennent `.bak_AAAA_MM_JJ` (plafond 3) |
| E - sauvegardes nommees | `CLAUDE_backup_2026-07-31.md`, `CLAUDE_2026-10-04.md`, `fichier_old.md` | renommees `{nom_de_travail}.bak_AAAA_MM_JJ`, ou `{nom_de_travail}` est le nom du fichier de travail courant, extension comprise : `CLAUDE_backup_2026-07-31.md` -> `CLAUDE.md.bak_2026_07_31`, `CLAUDE_2026-10-04.md` -> `CLAUDE.md.bak_2026_10_04`, `fichier_old.md` -> `fichier.md.bak_<date>`. Date lue dans le nom, a defaut date de modification |

> Aucune famille n'est une liste fermee. Tout nom portant une date (`AAAA-MM-JJ`, `AAAA_MM_JJ`,
> `AAAAMMJJ`) ou un marqueur `backup`, `save`, `old`, `ancien`, `avant`, `orig`, et qui n'est pas le
> fichier de travail courant, entre dans la conformite (famille E). Restent exclus les dossiers
> `_ARCHIVE` / `ARCHIVE` et les fichiers `*_archive_*`.

### Protocole

1. Date du jour = `Get-Date -Format "yyyy_MM_dd"`. **Les sauvegardes du jour ne sont jamais touchees** (famille A du jour, et famille D du jour).
2. Regrouper par fichier d'origine (meme dossier, meme nom de base, meme famille) puis, dans chaque groupe, par jour passe.
3. Pour chaque jour passe d'un groupe :
   - garder la sauvegarde la plus RECENTE : d'abord par l'horodatage lu dans le nom (jour + heure) ; a egalite (noms sans heure, ex `.bak_2026-09-20`, `.bak_2026-09-20b`, `.bak2_...`), par la date de modification du fichier ; si l'egalite persiste et que les contenus different (MD5), ne rien supprimer et signaler le groupe ; si les contenus sont identiques, garder n'importe lequel ;
   - la renommer en `fichier.yaml.bak_AAAA_MM_JJ` (famille A), les autres de ce jour vont a la corbeille Windows ;
   - famille C : renommer en `.bak_AAAA_MM_JJ` (la date est lue dans le nom) ;
   - famille D : la version la plus recente devient le nom sans date `{nom}.ext`, les autres deviennent des `.bak_AAAA_MM_JJ` (plafond 3) ;
   - famille E : renommer en `{nom_de_travail}.bak_AAAA_MM_JJ`, ou `{nom_de_travail}` est le nom du fichier de travail courant, extension comprise (ex : `CLAUDE_backup_2026-07-31.md` -> `CLAUDE.md.bak_2026_07_31`, `CLAUDE_2026-10-04.md` -> `CLAUDE.md.bak_2026_10_04`) ; date lue dans le nom, a defaut date de modification.
4. Plafond : si un fichier a plus de 3 `.bak_AAAA_MM_JJ` (apres les renommages ci-dessus, famille A, B et C), la plus ancienne va a la corbeille Windows, et ainsi de suite jusqu'a 3. Le plafond de 3 s'applique a toutes les familles (A, B, C, D, E).
5. Si la date change pendant l'execution (minuit passe), garder la date relevee au lancement de l'etape.

### Garde-fous (ne rien supprimer, remonter le souci)

- Collision : le nom cible existe deja (ex : un `.bak_2026_10_07` est deja present pour ce fichier) -> ne pas renommer, ne pas supprimer, signaler le groupe.
- Date illisible ou impossible (mois 13, jour 32) -> ne pas traiter, signaler.
- Nom douteux (pourrait etre un vrai fichier et non une sauvegarde) -> ne pas traiter, signaler.
- Erreur de la corbeille (fichier verrouille, acces refuse) -> ne pas retenter par une autre methode, signaler.
- Avant de lancer l'etape pour la premiere fois sur un dossier, ou si plus de 30 fichiers sont concernes : produire d'abord la liste (DRY-RUN : renommages et envois en corbeille prevus) et la presenter, sans rien modifier.

### Rapport (a mettre dans le rapport final)

- nombre de fichiers renommes, envoyes a la corbeille, ignores (archives / jour courant)
- liste des soucis signales (collision, date illisible, nom douteux, erreur) avec le chemin complet
- pour chaque envoi en corbeille : le chemin d'origine (restaurable depuis la corbeille Windows)

---

## ETAPE 6 - TREE (enchaine automatiquement, apres le menage)

Met a jour l'arborescence documentee : `C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\sous_context_ia\IA_ARBO_DETAIL.md` (comptages LOCAL, PROD et GitHub). Cette etape vient en dernier pour que les comptages refletent l'etat final apres le menage de l'etape 5.

1. Appliquer le protocole du skill `update-arbo` : comptages reels local et prod `H:\docs`, dernier commit et arbre GitHub, remplacements `.Replace()` stricts sur les seules lignes qui changent. Aucune valeur estimee ou memorisee.
2. Si les comptages sont identiques a ceux du fichier : ne rien modifier, noter "tree deja a jour".
3. Avant de modifier `IA_ARBO_DETAIL.md` : sauvegarde locale `IA_ARBO_DETAIL.md.bak_AAAA_MM_JJ_HHhMMmSSs` a cote du fichier (REGLE DE SAUVEGARDE, 10 max le jour meme).
4. Pousser ensuite vers `H:\docs\00_IA\sous_context_ia\IA_ARBO_DETAIL.md` (MD5 local contre prod avant et apres). Jamais de sauvegarde sur H:.
5. Si l'API GitHub est injoignable : ne pas inventer de valeur, garder les anciennes valeurs GitHub du fichier et le signaler dans le rapport.
6. Ne pas modifier les sections narratives du fichier.

---
## ORDRE D'EXECUTION STRICT

1. Bash : determiner date + numero session
2. Generer le bloc journal
3. Ecrire `historique/histo_[date]_s[N].md`
4. Presenter le fichier
5. Enchainer sync_index (dont INDEX_GLOBAL.md) sans pause ni question
6. Mettre a jour le journal fusionne (etape 3)
7. Copier dans Obsidian (etape 4)
8. Menage des sauvegardes (etape 5)
9. Mettre a jour le tree (etape 6)
10. Afficher le rapport final

### Format de rapport final (apres les six etapes)

```
SYNC_INDEX - [date]

Fichiers mis a jour :
- DEPENDANCES_GLOBALES.md : date en tete -> [date session]
- INDEX_GLOBAL.md : [entrees ajoutees / compteurs modifies] | deja a jour (sauvegarde : [nom du .bak])
- [autres fichiers si applicable]

JOURNAL FUSIONNE :
- [nom du fichier] : [n] lignes, sessions ajoutees : [liste]

OBSIDIAN :
- [fichier] : copie, MD5 identique | non copie (deja present) | DIFFERENT

MENAGE .bak :
- renommes : [n] | corbeille Windows : [n] | ignores : [n]
- soucis a traiter : [liste avec chemin complet] | aucun

TREE :
- IA_ARBO_DETAIL.md : [comptages modifies] | deja a jour (sauvegarde : [nom du .bak]) ; MD5 local = prod : OK | ECART

>> [fichier introuvable ou incomplet si applicable]
```