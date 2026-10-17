---
name: histo
description: "Skill HA ReBuild - genere un journal de bord ultra-compact et le sauvegarde, puis enchaine automatiquement le sync_index (DEPENDANCES_GLOBALES.md, docs impactees, GLOBAL_INDEX_REPO.md), le journal fusionne et la copie Obsidian et le menage des sauvegardes .bak puis la mise a jour du tree (IA_ARBO_DETAIL.md). Declencher OBLIGATOIREMENT quand l'utilisateur tape /histo, demande un journal de bord, genere l'histo, fais un resume a sauvegarder, cree un log de session, exporte l'historique. Usage typique : fin de session, avant de fermer Cowork."
---

# Skill : /histo - Journal de bord + sync_index (dont GLOBAL_INDEX_REPO) + journal fusionne + copie Obsidian + menage .bak + tree

## Objectif

Six actions, plus l'etape 5B, enchainees sans interruption :
1. Generer et sauvegarder le journal de bord de session
2. Executer le sync_index (DEPENDANCES_GLOBALES.md, docs impactees, GLOBAL_INDEX_REPO.md, GLOBAL_INDEX_AUTOMATIONS.md, GLOBAL_INDEX_VIGNETTES_PAGES.md, GLOBAL_INDEX_SCRIPTS_SH.md, GLOBAL_INDEX_SCRIPTS_YAML.md, GLOBAL_INDEX_IA.md)

3. Mettre a jour le JOURNAL FUSIONNE (historique/) avec la session qui vient d'etre ecrite
4. Copier le journal de session et le journal fusionne dans le coffre Obsidian
5. Faire le menage des sauvegardes (.bak) du perimetre docs, selon la REGLE DE SAUVEGARDE (etape 5)
5B. Verifier l'export Dashboard depose a la racine de la prod et ne garder qu'un export en prod (etape 5B)
6. Mettre a jour les tree : IA_ARBO_DETAIL.md (comptages local, prod, GitHub), avec le skill update-arbo (etape 6)
6B. Controler les 9 fichiers de SOUS_CONTEXT_IA (lecture seule, rapport d'ecarts, etape 6 point 7)
6C. Controler tous les index globaux (lecture seule, rapport d'ecarts, etape 6 point 8)

Ne jamais demander confirmation entre les etapes. Les faire dans la foulee. Seule exception : le DRY-RUN du menage (etape 5) a la premiere execution sur un dossier, qui s'arrete pour presenter la liste et attendre le go de l'utilisateur (voir les garde-fous de l'etape 5).

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
- Cette mise en forme s'applique uniquement aux NOUVEAUX journaux `histo_*.md`. Les anciens journaux, GLOBAL_INDEX_REPO.md et les autres fichiers restent inchanges et sans emoji (exception d'emojis accordee par Eric le 2026-10-08, limitee aux nouveaux journaux histo). Les nouveaux blocs de session du journal fusionne ont seulement le gras, sans emoji (etape 3).

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
| Config YAML (sensors, templates, utility_meter...) | `DEPENDANCES_GLOBALES.md` + `GLOBAL_INDEX_REPO.md` |
| Automation | `docs/03_docs_automations/docs_automations_MD/{nom}.md` + `GLOBAL_INDEX_REPO.md` |
| Script | `docs/04_docs_scripts/docs_scripts_YAML_MD/{nom}.md` + `GLOBAL_INDEX_REPO.md` |
| Tout type impactant une vignette | `DEPENDANCES_GLOBALES.md` |
| Fichier ajoute, renomme ou supprime (helper, export, fiche) | `GLOBAL_INDEX_REPO.md` |
| Skill du projet modifie (`.claude/skills/<skill>/SKILL.md`) | copie `docs/05_docs_skills/skill_<nom>/<nom>.md` |

**Chemins Windows :**
- `C:\Users\Berry Swann\Documents\ReBuild\docs\05_docs_MD_system\DEPENDANCES_GLOBALES\DEPENDANCES_GLOBALES.md`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\03_docs_automations\docs_automations_MD\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_YAML_MD\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\05_docs_MD_system\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md`

**Chemin bash sandbox :** detecter via `ls /sessions/` si necessaire (prefixe de session variable).

### Protocole

1. Identifier les fichiers modifies pendant la session (depuis le journal de bord qui vient d'etre genere)
2. Pour chaque fichier impactant DEPENDANCES_GLOBALES.md : mettre a jour la date en tete de fichier, puis pousser le fichier en prod (decide par Eric le 2026-10-14) : comparer le MD5 de la copie locale a `H:\docs\05_docs_MD_system\DEPENDANCES_GLOBALES\DEPENDANCES_GLOBALES.md`, copier seulement si different (sans sauvegarde sur H: : le `.bak` reste local), verifier le MD5 apres, y compris quand la ligne de date est la seule modification. Si la prod differe de la version locale d'avant la modification (quelqu'un d'autre a ecrit en prod) : ne pas pousser et le signaler. Si H: est inaccessible : le noter sans bloquer.
3. Pour chaque automation validee : verifier/mettre a jour son `.md` dans `docs_automations_MD/`
4. Pour chaque script valide : verifier/mettre a jour son `.md` dans `docs_scripts_YAML_MD/`
5. Mettre a jour `GLOBAL_INDEX_REPO.md` (voir ci-dessous)
6. Si un `.md` de doc est absent : le signaler (ne pas bloquer)
7. Pour chaque skill du projet modifie pendant la session : copier d'abord le fichier existant `docs/05_docs_skills/skill_<nom>/<nom>.md` en `docs/05_docs_skills/skill_<nom>/<nom>.bak_AAAA_MM_JJ_HHhMMmSSs.md` (sauvegarde avant ecrasement, jusqu'a 10 par jour ; le menage de l'etape 5 range les jours passes en `<nom>.bak_AAAA_MM_JJ.md`, 3 au plus), puis recopier le `SKILL.md` modifie vers `docs/05_docs_skills/skill_<nom>/<nom>.md`. Pas de copie dans `.claude/ARCHIVE`. Pas de push des skills vers `H:` tant qu'Eric ne le demande pas (decision du 2026-10-11).
8. Regenerer GLOBAL_INDEX_AUTOMATIONS.md (decide le 2026-10-13) : lancer `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\gen_global_index_automations\gen_global_index_automations.py"`. Le script lit H:\automations.yaml et le registre HA (lecture seule), croise avec docs_automations_YAML et docs_automations_MD, et ecrit `docs\03_docs_automations\GLOBAL_INDEX_AUTOMATIONS.md` (sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs.md` automatique si le contenu change ; rien d'ecrit si identique). Ne jamais modifier ce fichier a la main. VERIFIER la sortie du script : la ligne liens=N casses=M doit avoir casses=0 (sinon signaler chaque LIEN_CASSE en tete du rapport final) ; mettre dans le rapport final les lignes de resume du script et chaque ecart cite (sans_yaml, sans_fiche, sans_entity, id_different, erreurs_yaml). Un ecart nouveau par rapport a la session precedente doit etre signale a Eric, pas corrige sans demande. Si H: est inaccessible (code retour 2) : le noter sans bloquer. Pas de push automatique (poussable avec /ha-push-docs sur demande).
9. Regenerer GLOBAL_INDEX_VIGNETTES_PAGES.md (decide le 2026-10-13), meme principe que le point 8 : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\gen_global_index_vignettes_pages\gen_global_index_vignettes_pages.py"`. Le script lit l'arbre local docs\02_docs_dashboard (dashboard_docs_MD et dashboard_docs_YAML, sauvegardes exclues, Dashboard_COMPLET jamais lu) et ecrit `docs\02_docs_dashboard\GLOBAL_INDEX_VIGNETTES_PAGES.md` (sauvegarde `.bak_...md` automatique si le contenu change). Ne jamais modifier ce fichier a la main. VERIFIER la sortie du script : la ligne liens=N casses=M doit avoir casses=0 (sinon signaler chaque LIEN_CASSE en tete du rapport final) ; mettre dans le rapport final les lignes de resume du script (vignettes sans fiche ou sans YAML, dossiers d un seul cote, sans_dependances). Pas de push automatique.
10. Regenerer GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md (decide le 2026-10-13), meme principe : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\gen_global_index_scripts\gen_global_index_scripts.py"`. Le script lit l'arbre local docs\04_docs_scripts et la prod en lecture seule (H:\scripts.yaml, H:\automations.yaml, H:\shell_command, H:\.scripts, registre HA) et ecrit les deux fichiers a la racine de docs\04_docs_scripts (sauvegarde `.bak_...md` automatique si le contenu change). Chaque fichier explique la difference entre scripts SH (programmes bash/python) et scripts YAML (scripts Home Assistant). VERIFIER la sortie : les deux lignes `liens=N casses=M` doivent avoir casses=0 ; signaler dans le rapport final les lignes de resume SH et YAML et chaque ecart (script sans fiche, copie de H:\.scripts DIFFERENT du local, script YAML different de la prod ou sans YAML local, fichiers .py ranges dans docs_scripts_YAML). Si H: est inaccessible (code retour 2) : le noter sans bloquer. Ne jamais pousser un script de H:\.scripts sans ordre d'Eric. Ne jamais modifier ces fichiers a la main.
11. Regenerer GLOBAL_INDEX_IA.md (decide le 2026-10-13) : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\gen_global_index_ia\gen_global_index_ia.py"`. Le script liste tous les fichiers de docs\00_IA (IA_CONTEXT_BASE et SOUS_CONTEXT_IA) avec qui s'en sert, leur but, quand les lire, leur MD5 prod et un lien, et resume les `.bak` par dossier. Il ecrit docs\00_IA\GLOBAL_INDEX_IA.md (sauvegarde `.bak_...md` automatique si le contenu change). VERIFIER la sortie : la ligne `liens=N casses=M sans_description=K` doit avoir casses=0 et sans_description=0. Si un fichier est nouveau dans docs\00_IA (sans_description > 0) : le lire, ajouter son entree (qui, but, quand) dans le dictionnaire DESC du script apres sauvegarde du script, puis relancer ; ne jamais inventer une description sans avoir lu le fichier. Ne jamais modifier GLOBAL_INDEX_IA.md a la main.

### Mise a jour de GLOBAL_INDEX_REPO.md

Fichier : `C:\Users\Berry Swann\Documents\ReBuild\docs\05_docs_MD_system\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` (copie de travail locale, ses liens sont relatifs a la racine du depot : elle ne se clique pas ici ; poussee en prod a chaque /histo aux deux endroits (miroir H:\docs\05_docs_MD_system\GLOBAL_INDEX_REPO\ et racine H:\GLOBAL_INDEX_REPO.md, lue sur GitHub), voir le point 8 ci-dessous ; GitHub est alimente par le backup HA depuis H:, jamais en push direct).

1. Si aucun fichier de la session n'est ajoute, renomme, supprime ou deplace, et qu'aucune entite citee n'a change : noter "GLOBAL_INDEX_REPO deja a jour" et passer au point 8 (le push compare quand meme les MD5).
2. Sinon, faire d'abord une sauvegarde dans le meme dossier : `GLOBAL_INDEX_REPO.bak_AAAA_MM_JJ_HHhMMmSSs.md` (format PowerShell `Get-Date -Format "yyyy_MM_dd_HH'h'mm'm'ss's'"` ; le dossier INDEX_GLOBAL est dans le perimetre du menage de l'etape 5).
3. Ne reecrire que les lignes concernees, jamais le fichier entier :
   - ajouter une entree pour chaque nouveau fichier (automation, script, helper YAML, fiche), dans la section de son type, a cote des entrees voisines, avec le meme format que celles-ci
   - mettre a jour les entrees renommees ou supprimees
   - mettre a jour les compteurs de section concernes (par exemple le nombre d'automations ou de fichiers de scripts) en les recomptant, sans les deduire de l'ancien nombre
   - mettre a jour la ligne d'en-tete de date
4. Garder le format existant du fichier : UTF-8 sans BOM, fins de ligne LF (verifie le 2026-10-11 : le fichier est en LF, ne pas le convertir en CRLF). Controler le format avant d'ecrire.
5. Controles apres ecriture : le fichier se relit en UTF-8, les compteurs modifies correspondent au nombre d'entrees, les liens ajoutes pointent vers des fichiers qui existent. Les entites ajoutees doivent avoir ete verifiees en live ou lues dans un fichier de la session, jamais recopiees de memoire.
6. Les ecarts deja presents avant la session (entites citees qui ne repondent plus, desequilibres de compteurs) ne sont pas corriges ici : les mentionner dans le rapport s'ils concernent la session.
7. Note pour ha-trigul : depuis le push de /histo (decide par Eric le 2026-10-14), `GLOBAL_INDEX_REPO.md` est present en prod sous docs/05_docs_MD_system/GLOBAL_INDEX_REPO/ (miroir) ; il reste ABSENT sur le depot tant que le backup HA ne l'a pas repris ; son exemplaire a la racine de H: (GLOBAL_INDEX_REPO.md) n'est pas compare par le script.
8. Push en prod (decide par Eric le 2026-10-14, il remplace l'ancienne regle "pas de push automatique" : Eric avait pris ce fichier pour un autre) : apres les controles du point 5, que le fichier ait ete modifie ou non, comparer le MD5 de la copie de travail a chacune des DEUX destinations, comme l'etape 5B de ha-push-docs : `H:\docs\05_docs_MD_system\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` (miroir) et `H:\GLOBAL_INDEX_REPO.md` (racine). Copier seulement celles qui different, sans sauvegarde sur H: (les `.bak` restent locaux), puis verifier le MD5 : source = miroir = racine. Jamais un seul des deux. Ne pas pousser si les controles du point 5 ont echoue. Si H: est inaccessible : le noter sans bloquer. GitHub : jamais de push direct (le depot est alimente par le backup HA depuis H:).

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

- Ne jamais ecraser un fusionne existant : un nouveau nom par nouvelle date de fin. Si le fichier cible existe deja (meme date de fin, nouvelle session du meme jour), le sauvegarder d'abord en `JOURNAL_FUSIONNE_..._[DATE_FIN].bak_AAAA_MM_JJ_HHhMMmSSs.md` puis le mettre a jour.
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

- Ne jamais ecraser un fichier existant du dossier Obsidian : s'il existe deja, ne pas le copier et le signaler. Seule exception : un fusionne de meme nom (mise a jour du meme jour), qui est ecrase SANS sauvegarde sur D: (regle : jamais de sauvegarde sur D:). La version precedente reste dans `historique\` (sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs.{ext}` faite a l'etape 3).
- L'ancien fusionne reste dans le dossier Obsidian.
- Apres chaque copie, comparer le MD5 source / destination et le noter dans le rapport (`identique` ou `DIFFERENT`).
- Si `D:\` ou le dossier est inaccessible : le signaler dans le rapport, ne pas bloquer et ne pas creer d'autre dossier a la place.

---

## ETAPE 5 - MENAGE DES SAUVEGARDES (enchaine automatiquement, apres la copie Obsidian)

Applique la REGLE DE SAUVEGARDE du 2026-10-08 (definie dans CLAUDE.md). Tout se passe en LOCAL, jamais sur H: ni sur D:.

**Perimetre :** `C:\Users\Berry Swann\Documents\ReBuild\docs\00_*` a `05_*` (recursif) + `C:\Users\Berry Swann\Documents\ReBuild\Claude md SAVE\`.
**Hors perimetre (ne pas toucher) :** TODO, Github, historique, Infra_Proxmox, `_old_avant_staging` (racine et sous-dossiers `docs\`), le reste de `.claude` (skills et commands actifs). Le dossier `.claude\ARCHIVE\` est HORS perimetre (decision d'Eric le 2026-10-11 : conserve pour un eventuel retour en arriere, a supprimer quand il ne servira plus ; il ne vit plus avec histo). Les sauvegardes d'un skill vivent dans `docs\05_docs_skills\skill_<nom>\` et suivent la meme regle que le reste (jusqu'a 10 `.bak_AAAA_MM_JJ_HHhMMmSSs` pour le jour, 3 `.bak_AAAA_MM_JJ` pour les jours passes). Les exports `docs\02_docs_dashboard\dashboard_docs_YAML\Dashboard_COMPLET\` sont conserves tels quels : jamais renommes en `.bak`, jamais mis a la corbeille par ce menage (voir etape 5B). Ignorer tout dossier `_ARCHIVE` / `ARCHIVE` et tout fichier dont le nom contient `_archive_` (ex : `_ARCHIVE\DEPENDANCES_GLOBALES_archive_2026-10-07_18h13.md`).

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
- une version ou une sauvegarde -> `{nom_de_travail}.bak_AAAA_MM_JJ.{ext}` (le nom de travail ne contient pas de date) ;
- la version courante d'un fichier de travail -> le nom sans date (`{nom}.ext`).

Un nom de fichier ne porte JAMAIS de date dans sa partie courante. En cas de doute (nom qui pourrait
etre un vrai document et non une sauvegarde), on signale et on ne touche pas.

### Formats reconnus (dans le perimetre uniquement)

| Famille | Exemple | Traitement |
|:---|:---|:---|
| A - sauvegarde horodatee | `fichier.bak_2026_10_07_21h14m05s.yaml` | voir protocole |
| B - sauvegarde finale | `fichier.bak_2026_10_07.yaml` | gardee, soumise au plafond de 3 |
| C - anciens `.bak` | `.bak_2026-09-28`, `.bak_20260929`, `.bak2_...`, `.bak-...` | renommes `fichier.bak_AAAA_MM_JJ.yaml` |
| D - versions datees d'un fichier de travail | `page_L4C2_proxmox_2026-06-18.yaml`, `fichier_2026-10-07_22h00.ext` | seulement si le fichier de travail non date `{nom}.ext` existe dans le meme dossier : chaque version datee devient `{nom}.bak_AAAA_MM_JJ.{ext}` (plafond 3). Sans fichier de travail non date : nom douteux, signaler, ne pas toucher |
| E - sauvegardes nommees | `CLAUDE_backup_2026-07-31.md`, `CLAUDE_2026-10-04.md`, `fichier_old.md` | renommees `{nom_de_travail}.bak_AAAA_MM_JJ.{ext}`, ou `{nom_de_travail}` est le nom du fichier de travail courant, extension comprise : `CLAUDE_backup_2026-07-31.md` -> `CLAUDE.bak_2026_07_31.md`, `CLAUDE_2026-10-04.md` -> `CLAUDE.bak_2026_10_04.md`, `fichier_old.md` -> `fichier.bak_<date>.md`. Le nom de travail est le nom complet du fichier non date voisin, jamais tronque (`04_backup_git_push_manuel_2026-05-31.yaml` -> `04_backup_git_push_manuel.bak_2026_05_31.yaml`, pas `04.bak_...`). Date lue dans le nom, a defaut date de modification. Un fichier non date, sans version de travail correspondante, dont le nom contient `backup`, `save` ou `old` (ex : `ha_git_backup.sh`, `HA_GIT_BACKUP.md`) est un vrai fichier : ne pas le traiter |

> Aucune famille n'est une liste fermee. Tout nom portant une date (`AAAA-MM-JJ`, `AAAA_MM_JJ`,
> `AAAAMMJJ`) ou un marqueur `backup`, `save`, `old`, `ancien`, `avant`, `orig`, et qui n'est pas le
> fichier de travail courant, entre dans la conformite (famille E). Restent exclus les dossiers
> `_ARCHIVE` / `ARCHIVE` (dont `.claude\ARCHIVE\`), les fichiers `*_archive_*` et `Dashboard_COMPLET\` restent exclus. Un marqueur seul ne suffit pas : sans date et sans version de travail voisine, le fichier est un vrai fichier.

### Protocole

1. Date du jour = `Get-Date -Format "yyyy_MM_dd"`. **Les sauvegardes du jour ne sont jamais touchees** (famille A du jour, et famille D du jour).
2. Regrouper par fichier d'origine (meme dossier, meme nom de base, meme famille) puis, dans chaque groupe, par jour passe.
3. Pour chaque jour passe d'un groupe :
   - garder la sauvegarde la plus RECENTE : d'abord par l'horodatage lu dans le nom (jour + heure) ; a egalite (noms sans heure, ex `.bak_2026-09-20`, `.bak_2026-09-20b`, `.bak2_...`), par la date de modification du fichier ; si l'egalite persiste et que les contenus different (MD5), ne rien supprimer et signaler le groupe ; si les contenus sont identiques, garder n'importe lequel ;
   - la renommer en `fichier.bak_AAAA_MM_JJ.yaml` (famille A), les autres de ce jour vont a la corbeille Windows ;
   - famille C : renommer en `.bak_AAAA_MM_JJ.{ext}` (la date est lue dans le nom) ;
   - famille D : seulement si le fichier de travail non date `{nom}.ext` existe dans le dossier ; chaque version datee devient `{nom}.bak_AAAA_MM_JJ.{ext}` (nom de travail complet, jamais tronque ; plusieurs versions du meme jour : la plus recente est gardee, les autres vont a la corbeille ; plafond 3) ; sans fichier de travail non date, signaler et ne pas toucher ;
   - famille E : renommer en `{nom_de_travail}.bak_AAAA_MM_JJ.{ext}`, ou `{nom_de_travail}` est le nom du fichier de travail courant, extension comprise (ex : `CLAUDE_backup_2026-07-31.md` -> `CLAUDE.bak_2026_07_31.md`, `CLAUDE_2026-10-04.md` -> `CLAUDE.bak_2026_10_04.md`) ; date lue dans le nom, a defaut date de modification.
4. Plafond : si un fichier a plus de 3 `.bak_AAAA_MM_JJ.{ext}` (apres les renommages ci-dessus, famille A, B et C), la plus ancienne va a la corbeille Windows, et ainsi de suite jusqu'a 3. Le plafond de 3 s'applique a toutes les familles (A, B, C, D, E).
5. Si la date change pendant l'execution (minuit passe), garder la date relevee au lancement de l'etape.

### Garde-fous (ne rien supprimer, remonter le souci)

- Collision : le nom cible existe deja (ex : un `.bak_2026_10_07` est deja present pour ce fichier) -> ne pas renommer, ne pas supprimer, signaler le groupe.
- Date illisible ou impossible (mois 13, jour 32) -> ne pas traiter, signaler.
- Nom douteux (pourrait etre un vrai fichier et non une sauvegarde) -> ne pas traiter, signaler.
- Famille D sans fichier de travail non date dans le dossier -> ne pas traiter, signaler.
- Fichier non date contenant `backup`, `save` ou `old`, sans version de travail voisine (ex : `ha_git_backup.sh`) -> vrai fichier, ne pas traiter.
- Exports `Dashboard_COMPLET` -> jamais traites.
- Erreur de la corbeille (fichier verrouille, acces refuse) -> ne pas retenter par une autre methode, signaler.
- Avant de lancer l'etape pour la premiere fois sur un dossier : produire d'abord la liste (DRY-RUN : renommages et envois en corbeille prevus) et la presenter, sans rien modifier, puis attendre le go de l'utilisateur (seul arret autorise de /histo). Dans tous les autres cas, quel que soit le nombre de fichiers (decision d'Eric le 2026-10-15) : aucun go a attendre ; ecrire la liste dans historique\menage_dry_run_AAAA-MM-JJ.txt, la citer dans le rapport final, puis executer. Relire le plan avant de le presenter ou de l'executer : aucune cible ne doit etre tronquee, aucun export Dashboard ni vrai fichier ne doit y figurer, et le plafond de 3 doit etre calcule apres les renommages de la famille D. Executer ensuite sans re-demander ; le tree (etape 6) est fait apres l'execution du menage, ou le rapport precise que ses comptages sont d'avant menage.

### Rapport (a mettre dans le rapport final)

- nombre de fichiers renommes, envoyes a la corbeille, ignores (archives / jour courant)
- liste des soucis signales (collision, date illisible, nom douteux, erreur) avec le chemin complet
- pour chaque envoi en corbeille : le chemin d'origine (restaurable depuis la corbeille Windows)

---

## ETAPE 5B - EXPORT DASHBOARD (enchaine automatiquement, apres le menage, sans demander)

Eric depose de temps en temps un export du dashboard a la racine de la prod (`H:\Dashboard_*.yaml`). Cette etape le recupere en local, puis ne garde qu'un seul export en prod. Elle compare par MD5, jamais par le nom (le 2026-10-11, `H:\Dashboard_2026_10_04.yaml` avait le contenu de l'export du 11/10).

Dossiers : local `C:\Users\Berry Swann\Documents\ReBuild\docs\02_docs_dashboard\dashboard_docs_YAML\Dashboard_COMPLET\` ; prod `H:\docs\02_docs_dashboard\dashboard_docs_YAML\Dashboard_COMPLET\`.

1. Pour chaque `H:\Dashboard_*.yaml` a la racine : calculer le MD5 et le comparer a celui de chaque export du dossier local. Si un export local a le meme MD5 : rien a copier. Sinon l'export est nouveau : le copier dans le dossier local en gardant le meme nom. Si ce nom existe deja en local avec un autre contenu (erreur de nommage), le copier sous `Dashboard_AAAA_MM_JJ.yaml`, date = date de derniere modification du fichier de la racine ; si ce nom existe aussi avec un autre contenu : ne rien copier, signaler. Le fichier de la racine n'est jamais modifie ni supprime.
2. Les exports locaux sont tous conserves tels quels, sans `.bak` (le menage de l'etape 5 ne les traite pas).
3. Prod : prendre l'export local le plus recent (date dans le nom `Dashboard_AAAA_MM_JJ`, a defaut date de modification). Si le dossier prod ne contient pas un fichier de meme MD5 : le copier dans le dossier prod, verifier le MD5 apres copie, puis supprimer les autres exports du dossier prod (suppression definitive : pas de corbeille sur H:). Il ne doit rester qu'un seul export en prod, le plus recent. Jamais de sauvegarde sur H:.
4. Si le dossier prod contient deja le plus recent et lui seul : noter "Dashboard deja a jour".

---

## ETAPE 6 - TREE (enchaine automatiquement, apres le menage)

Met a jour l'arborescence documentee : `C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` (comptages LOCAL, PROD et GitHub). Cette etape vient en dernier pour que les comptages refletent l'etat final apres le menage de l'etape 5.

1. Appliquer le protocole du skill `update-arbo` : comptages reels local et prod `H:\docs`, dernier commit et arbre GitHub, remplacements `.Replace()` stricts sur les seules lignes qui changent. Aucune valeur estimee ou memorisee.
2. Si les comptages sont identiques a ceux du fichier : ne rien modifier, noter "tree deja a jour".
3. Avant de modifier `IA_ARBO_DETAIL.md` : sauvegarde locale `IA_ARBO_DETAIL.bak_AAAA_MM_JJ_HHhMMmSSs.md` a cote du fichier (REGLE DE SAUVEGARDE, 10 max le jour meme).
4. Pousser ensuite vers `H:\docs\00_IA\SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` (MD5 local contre prod avant et apres). Jamais de sauvegarde sur H:.
5. Si l'API GitHub est injoignable : ne pas inventer de valeur, garder les anciennes valeurs GitHub du fichier et le signaler dans le rapport.
6. Ne pas modifier les sections narratives du fichier.
7. Controle des 9 fichiers de `docs\00_IA\SOUS_CONTEXT_IA\` (decide le 2026-10-13, apres le push de IA_ARBO_DETAIL pour que le MD5 prod soit definitif) : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\check_sous_context_ia\check_sous_context_ia.py"`. Script en LECTURE SEULE : il ne corrige rien. Il verifie par fichier la structure (un dossier par fichier, baks bien nommes, plafonds 10 le jour meme / 3 par jour passe), le MD5 prod (IA_SKILLS_INVENTAIRE absent de la prod = attendu), la date declaree en en-tete (ecart au-dela de 60 jours), les chemins `docs/NN_...` cites qui n'existent plus, les nombres "N automations" / "N vignettes" contre la prod et les dossiers, et les entites citees absentes du registre HA et des etats. Mettre dans le rapport final la derniere ligne `controle sous_context_ia: dossiers=N baks=N ecarts=N casses=N` et chaque ecart cite. Le script controle aussi (depuis le 2026-10-17) que chaque chemin `docs/00_IA/...md` cite dans `Claude md SAVE\CLAUDE.md` existe en local avec la casse exacte : mettre dans le rapport la ligne `CLAUDE.md : chemins docs/00_IA cites=N morts=N` ; un chemin mort est un ecart signale a Eric, a corriger dans CLAUDE.md et ses 3 fichiers apparentes seulement sur sa demande. Un ecart nouveau par rapport a la session precedente est signale a Eric, jamais corrige sans demande. Si H: est inaccessible : le noter sans bloquer. Fichiers figes : ceux listes dans la constante FIGES du script (nom -> date du gel) ne subissent plus de controle de contenu, seulement structure, baks et MD5 prod, plus un ecart "fige mais modifie depuis" ; seul Eric decide de figer un fichier, ne jamais en figer de soi-meme.
8. Controle de tous les index globaux (decide le 2026-10-13, apres les regenerations de l'etape 2 et les pushs) : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\check_global_index\check_global_index.py"`. Script en LECTURE SEULE. Il verifie, pour GLOBAL_INDEX_REPO, GLOBAL_INDEX_AUTOMATIONS, GLOBAL_INDEX_VIGNETTES_PAGES, GLOBAL_INDEX_SCRIPTS_SH, GLOBAL_INDEX_SCRIPTS_YAML, ENTITES_GLOBAL_INDEX et GLOBAL_INDEX_IA : l'existence, les liens casses (ceux de GLOBAL_INDEX_REPO sont relatifs a la racine du depot : resolus dans ReBuild puis en prod), l'equilibre des balises details et blockquote du REPO, la presence et le MD5 en prod (GLOBAL_INDEX_REPO aux 2 emplacements), les entites citees absentes du registre HA et des etats (REPO et ENTITES). Mettre dans le rapport final la derniere ligne `controle global_index: index=N liens=N casses=N ecarts=N` et chaque ecart cite. Ne rien corriger sans demande : les liens casses deja connus de la section 03 de GLOBAL_INDEX_REPO sont signales a Eric, jamais reecrits en masse. Pour un index genere, un lien casse ou un ecart de contenu = relancer d'abord le generateur (etape 2) puis ce script ; si l'ecart reste, le signaler. Si H: est inaccessible : le noter sans bloquer.

---
## ORDRE D'EXECUTION STRICT

1. Bash : determiner date + numero session
2. Generer le bloc journal
3. Ecrire `historique/histo_[date]_s[N].md`
4. Presenter le fichier
5. Enchainer sync_index (dont GLOBAL_INDEX_REPO.md) sans pause ni question
6. Mettre a jour le journal fusionne (etape 3)
7. Copier dans Obsidian (etape 4)
8. Menage des sauvegardes (etape 5)
9. Export Dashboard (etape 5B)
10. Mettre a jour le tree (etape 6)
11. Afficher le rapport final

### Format de rapport final (apres toutes les etapes)

```
SYNC_INDEX - [date]

Fichiers mis a jour :
- DEPENDANCES_GLOBALES.md : date en tete -> [date session] | push prod : [MD5 identique | non pousse (raison)]
- GLOBAL_INDEX_REPO.md : [entrees ajoutees / compteurs modifies] | deja a jour (sauvegarde : [nom du .bak]) | push prod : [miroir docs et racine H: MD5 identiques | non pousse (raison)]
- GLOBAL_INDEX_AUTOMATIONS.md : [regenere | inchange] | resume du script : [prod / local_yaml / fiches / sans_yaml / sans_fiche / sans_entity / id_different]
- GLOBAL_INDEX_VIGNETTES_PAGES.md : [regenere | inchange] | resume du script : [vignettes / dossiers / manques / seul_md / seul_yaml / sans_dependances]
- GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md : [regenere | inchange] | resume du script : [SH scripts / sans_fiche / prod_different ; YAML scripts / sans_yaml / different / sans_fiche / py_dans_yaml]
- GLOBAL_INDEX_IA.md : [regenere | inchange] | resume du script : [liens / casses / sans_description]
- [autres fichiers si applicable]

JOURNAL FUSIONNE :
- [nom du fichier] : [n] lignes, sessions ajoutees : [liste]

OBSIDIAN :
- [fichier] : copie, MD5 identique | non copie (deja present) | DIFFERENT

MENAGE .bak :
- renommes : [n] | corbeille Windows : [n] | ignores : [n]
- soucis a traiter : [liste avec chemin complet] | aucun

DASHBOARD :
- racine H: : [fichier] : nouveau, copie en local | deja present (MD5) | aucun export
- prod Dashboard_COMPLET : [export unique] ; supprimes : [liste] | deja a jour

TREE :
- IA_ARBO_DETAIL.md : [comptages modifies] | deja a jour (sauvegarde : [nom du .bak]) ; MD5 local = prod : OK | ECART

SOUS_CONTEXT_IA :
- controle sous_context_ia: dossiers=[n] baks=[n] ecarts=[n] casses=[n] ; ecarts : [liste fichier : ecart] | aucun
- CLAUDE.md : chemins docs/00_IA cites=[n] morts=[n]
- entites introuvables a verifier : [liste] | aucune

INDEX GLOBAUX :
- controle global_index: index=[n] liens=[n] casses=[n] ecarts=[n] ; detail : [liste index : ecart] | aucun

>> [fichier introuvable ou incomplet si applicable]
```

---
## NOTE HISTORIQUE - limite de 30 fichiers du menage, supprimee le 2026-10-15

Trace gardee a la demande d'Eric (2026-10-15 20h11), pour retrouver ce qui a change si un menage touche un fichier par erreur. Cette note ne s'applique pas : c'est un historique.

- Avant le 2026-10-15, l'etape 5 s'arretait apres le dry-run et attendait le go d'Eric si c'etait la premiere execution sur un dossier OU si plus de 30 fichiers etaient concernes. /histo-final (ligne 15) reprenait cette regle : pas d'extinction tant que le menage attendait le go.
- Le 2026-10-15 (ordres d'Eric a 19h27, 19h35 et 20h08), le go au-dela de 30 fichiers a ete supprime. Le plan est ecrit dans historique\menage_dry_run_AAAA-MM-JJ.txt, cite dans le rapport final, puis execute sans attente. Seule pause restante : la premiere execution du menage sur un dossier.
- Contexte de la decision : le 2026-10-14, un /histo-final est reste 2h20 en attente du go (77 actions) et n'a pas pu eteindre les lumieres ni le PC. Ce soir-la, mon premier calcul du dry-run annoncait 362 envois en corbeille a cause d'un bug de ma part (plage PowerShell 1..0 sur un groupe d'un seul fichier) ; il avait ete rattrape avant execution justement grace a la relecture du plan. Sans la pause, ce plan faux aurait ete execute.
- Si un fichier a ete envoye a tort a la corbeille : il est dans la corbeille Windows (jamais de suppression definitive) tant qu'elle n'est pas videe. Plans et rapports : historique\menage_dry_run_*.txt et historique\menage_execute_*.txt (chemins d'origine). Journal des modifs : historique\modifs\MODIFS_AAAA-MM-JJ_claude.md.
- Texte exact de l'ancienne ligne (supprimee de l'etape 5) :

```text
- Avant de lancer l'etape pour la premiere fois sur un dossier, ou si plus de 30 fichiers sont concernes : produire d'abord la liste (DRY-RUN : renommages et envois en corbeille prevus) et la presenter, sans rien modifier, puis attendre le go de l'utilisateur (seul arret autorise de /histo). Relire le plan avant de le presenter : aucune cible ne doit etre tronquee, aucun export Dashboard ni vrai fichier ne doit y figurer, et le plafond de 3 doit etre calcule apres les renommages de la famille D. Executer ensuite sans re-demander ; le tree (etape 6) est fait apres l'execution du menage, ou le rapport precise que ses comptages sont d'avant menage.
```
