---
name: journal-modifs
description: Skill HA ReBuild - note au fil de l'eau chaque modification de fichier (creation, modification, renommage, suppression, push) dans un journal par auteur, lisible par Claude et Hermes. A appliquer apres chaque ecriture et a lire au debut de session.
---

# Skill : journal-modifs

## Objectif

Eviter les modifications sans trace ni auteur (constate le 2026-10-10 : CLAUDE.md, DEPENDANCES_GLOBALES.md, cartes de presence modifies sans journal). Chaque agent (Claude, Hermes) note une ligne par fichier modifie, au moment de la modification, dans son propre fichier du jour. L'autre agent le lit au debut de sa session.

## Emplacements

- Maitre (local) : `C:\Users\Berry Swann\Documents\ReBuild\historique\modifs\MODIFS_AAAA-MM-JJ_<auteur>.md`
- Copie prod : `H:\docs\modifs\MODIFS_AAAA-MM-JJ_<auteur>.md`
- `<auteur>` : `claude` ou `hermes` (minuscules). Un autre agent prend son propre nom.
- Chaque agent n'ecrit QUE dans son fichier, jamais dans celui de l'autre (evite les ecritures simultanees).
- Hermes, qui n'a pas forcement acces au dossier local, ecrit directement son fichier dans `H:\docs\modifs\`.
- Ces fichiers ne sont pas des sauvegardes : pas de .bak, hors perimetre du menage /histo.

## Quand noter

Apres chaque ecriture REUSSIE dans le perimetre du projet : creation, modification, renommage, deplacement, suppression (corbeille), copie vers H: ou D:, push.

Perimetre : ReBuild (docs, scripts, historique, Github, TODO, MOC, Claude md SAVE, .claude), H: (docs, .scripts, YAML de config), copies D:\Cerveau-Obsidian et D:\hermes.

Ne pas noter : les lectures, les fichiers temporaires dans %TEMP%, le journal lui-meme.

La ligne est ecrite apres l'ecriture, jamais avant. Si l'ecriture echoue : ne rien noter, ou noter ECHEC avec la cause.

## Format d'une ligne

Une ligne par fichier, ajoutee en fin de fichier (jamais de reecriture du fichier) :

`AAAA-MM-JJ HH:MM:SS | auteur | ACTION | chemin complet | avant=XXXXXXXX apres=XXXXXXXX | raison courte`

- ACTION : CREE, MODIFIE, RENOMME, DEPLACE, SUPPRIME, COPIE, POUSSE, ECHEC, LOT
- MD5 : 8 premiers caracteres en minuscules ; `-` si non applicable (fichier cree : avant=- ; fichier supprime : apres=-)
- RENOMME, DEPLACE, COPIE, POUSSE : le chemin est la destination, la source va dans la raison (`depuis ...`)
- Sauvegarde faite avant modification : citer son nom dans la raison (`bak : nom`)
- Raison : quelques mots, sans secret (jamais de mot de passe, token ni contenu de fichier)
- Pas de retour a la ligne dans une ligne. ASCII simple de preference.
- Premiere ligne d'un fichier neuf : `# MODIFS AAAA-MM-JJ - <auteur>`

## Operations en masse

Au-dela de 10 fichiers dans une meme operation (menage .bak, push d'un dossier, resync) : une seule ligne LOT, avec le nombre de fichiers et le chemin d'un rapport qui liste chaque fichier (dry-run, execution, log). Ce rapport doit exister.

`AAAA-MM-JJ HH:MM:SS | auteur | LOT | <dossier ou operation> | n=<nombre> | rapport : <chemin>`

## Ecriture (PowerShell, a adapter a l'agent)

```powershell
$a='claude'   # ou 'hermes'
$d=Get-Date -Format 'yyyy-MM-dd'
$enc=New-Object Text.UTF8Encoding($false)
$f="C:\Users\Berry Swann\Documents\ReBuild\historique\modifs\MODIFS_${d}_$a.md"
New-Item -ItemType Directory -Force (Split-Path $f) | Out-Null
if(-not (Test-Path $f)){ [IO.File]::WriteAllText($f,"# MODIFS $d - $a`r`n",$enc) }
$ligne='{0} | {1} | MODIFIE | {2} | avant={3} apres={4} | {5}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'),$a,$chemin,$avant,$apres,$raison
[IO.File]::AppendAllText($f,$ligne+"`r`n",$enc)
New-Item -ItemType Directory -Force 'H:\docs\modifs' | Out-Null
Copy-Item $f 'H:\docs\modifs\' -Force
```

Format du fichier : CRLF, UTF-8 sans BOM. Copie vers H: apres chaque lot de modifications, et en tout cas avant de rendre la main a l'utilisateur.

## Debut de session (obligatoire)

1. Lire les dernieres lignes des journaux du jour et de la veille dans `H:\docs\modifs\` : les siens et ceux de l'autre agent.
2. Chercher les modifications non journalisees : lister les fichiers du perimetre dont la date de modification est posterieure a la derniere ligne des journaux et qui n'ont aucune ligne. Les presenter a l'utilisateur AVANT de commencer ("modifications sans journal : ..."), sans deviner l'auteur : il est inconnu tant qu'aucune ligne ne le dit.
3. Ne pas supposer qu'une modification absente du journal est de soi-meme.

## Fin de session et /histo

Les journaux du jour des deux auteurs servent de source a l'etape 1 du /histo : chaque fichier cite dans le journal de bord doit retrouver sa ligne. Un ecart est signale dans le journal de bord ("modifications non journalisees : ...").

## Limites (a connaitre)

- Ne couvre pas les modifications faites a la main par l'utilisateur ni par HA (backup git automatique) : d'ou le controle du debut de session.
- Le journal est declaratif : une ligne absente ne prouve rien, et une ligne presente ne prouve pas que le fichier est reste tel quel (comparer le MD5 en cas de doute).
- Si la copie vers H: est impossible : le signaler, ne pas bloquer le travail.
