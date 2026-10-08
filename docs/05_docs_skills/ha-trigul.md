---
name: ha-trigul
description: "Skill HA ReBuild - triangulation MD5 des docs .md entre local (ReBuild), prod (H:) et GitHub, rapport range dans historique\\MD5. Declencher sur /trigul, trigul, triangulation, audit md5 des docs, les docs sont-ils a jour en prod et sur GitHub."
---

# Skill : /ha-trigul - triangulation MD5 des docs (local / prod / GitHub)

## Objectif

Comparer chaque fichier .md de documentation entre les 3 niveaux et ecrire un rapport dans `historique\MD5\`. Lecture seule : le skill ne modifie, ne pousse et ne corrige aucun fichier de documentation. Il n'ecrit que le rapport.

Perimetre : `docs/**/*.md` + `Github/README.md` + `Github/INDEX_GLOBAL.md` (compares a `README.md` et `INDEX_GLOBAL.md` a la racine de la prod et du depot). Les YAML de config sont hors perimetre (voir ha-resync-tree et ha-push-yaml).

Source de verite = LOCAL (ReBuild). Un ecart local/prod veut dire prod EN RETARD ; un ecart prod/depot veut dire depot EN RETARD.

## Fichiers et chemins

- Script (ne pas le modifier) : `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md.sh`
- Interpreteur : `C:\Program Files\Git\bin\bash.exe` (git-bash ; la prod H: y apparait en /h)
- Dossier des rapports : `C:\Users\Berry Swann\Documents\ReBuild\historique\MD5\`
- Rapport du jour : `hermes_md5_audit_md_[YYYY-MM-DD].txt` ; copie automatique `hermes_md5_audit_md_latest.txt`

Le script ecrit par defaut dans `historique\` (racine). Pour ranger le rapport dans `historique\MD5\`, passer la variable `LOG_DIR` au lancement (la commande ci-dessous le fait). Ne pas toucher au script pour ca.

## Protocole

1. Lister `historique\MD5\` : si `hermes_md5_audit_md_[date du jour].txt` existe deja, le sauvegarder d'abord dans le meme dossier sous `hermes_md5_audit_md_[date].bak_AAAA_MM_JJ_HHhMMmSSs` (le script ecrase le rapport du jour). Format en PowerShell : `Get-Date -Format "yyyy_MM_dd_HH'h'mm'm'ss's'"`. Le dossier historique\MD5 est hors perimetre du menage de /histo.
2. Verifier qu'aucun `bash` ne tourne deja (Get-Process bash).
3. Lancer le script avec cette commande PowerShell (Windows-MCP), telle quelle :

```
if(Get-Process bash -ErrorAction SilentlyContinue){ 'deja en cours, pas de relance' } else {
$cmd='cmd.exe /c "set LOG_DIR=C:/Users/Berry Swann/Documents/ReBuild/historique/MD5&& "C:\Program Files\Git\bin\bash.exe" "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md.sh" > "%TEMP%\trigul_out.txt" 2> "%TEMP%\trigul_err.txt""'
$r=Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine=$cmd}; 'lance, ReturnValue='+$r.ReturnValue+' PID '+$r.ProcessId+' a '+(Get-Date -Format HH:mm:ss) }
```

   Pourquoi cette forme : la liaison avec le PC renvoie l'appel quand il depasse 60 s. Avec `Start-Process -PassThru`, l'appel restait bloque, la liaison le renvoyait, et le script demarrait deux fois, ce qui entrelace le rapport. Ici le lancement est detache (retour immediat) et la garde `Get-Process bash` empeche un second lancement si l'appel est renvoye.
4. Attendre la fin avec des appels courts (moins de 60 s chacun, par exemple `Start-Sleep 40` puis un controle) : `Get-Process bash` (nombre de processus), taille et date du rapport du jour, derniere ligne de `%TEMP%\trigul_out.txt`. Duree constatee le 2026-10-08 : environ 1 min 30 pour 162 fichiers. Le script est termine quand plus aucun `bash` ne tourne et que la derniere ligne de `trigul_out.txt` commence par une date puis "HERMES audit MD5 termine". Ne jamais relancer pendant qu'un `bash` tourne.
5. Si un double lancement a quand meme eu lieu (plus de 2 processus `bash` demarres a une minute d'ecart) : arreter les `bash` (Stop-Process), supprimer le rapport du jour et les fichiers `%TEMP%\hermes_md_*`, puis relancer une seule fois avec la commande de l'etape 3.
6. Lire le rapport (UTF-8) : les lignes `RESULTAT` et `PAR PAIRE` en fin de fichier, puis les lignes de la table dont le statut n'est pas SYNC.
7. Verifier que `hermes_md5_audit_md_latest.txt` est identique au rapport du jour (MD5).
8. Supprimer les fichiers temporaires `trigul_out.txt` et `trigul_err.txt` dans `%TEMP%`, et verifier qu'aucun `bash` ne tourne plus.

## Lecture du rapport

Colonnes : FICHIER | L<->P | P<->R | L<->R | DETAIL (L = local, P = prod, R = repo GitHub).
Statuts globaux : SYNC (les 3 identiques), CRLF (seule la fin de ligne differe, sans action), DIFF (contenu different, action reelle), ABSENT (manque sur au moins un niveau).

Si presque tout est ABSENT cote prod, la prod H: n'etait pas visible depuis le processus lance : verifier l'acces a H: avant de conclure.

Faux positifs connus, constates le 2026-10-08 (162 fichiers, 147 SYNC, 1 DIFF, 14 ABSENT, resultat identique sur deux passages) :
- Les sauvegardes et archives locales (anciens noms `_YYYY-MM-DD_HHhMM.md` ou `_YYYY-MM-DD.md`, par exemple `AUTOMATIONS_2026-10-07_22h00.md`, ou fichiers sous `_ARCHIVE/`) sont ABSENT en prod et sur GitHub : c'est normal, elles restent locales (regle du 2026-10-08 : jamais de sauvegarde en prod). Les sauvegardes au nouveau format `.md.bak_AAAA_MM_JJ...` ne sont pas vues par le script (il ne lit que les `*.md`).
- `INDEX_GLOBAL.md` en DIFF local contre prod = repo : attendu tant qu'il n'existe pas de circuit de push pour ce fichier.
- Juste apres un push GitHub, un "1 DIFF" peut venir du cache CDN de raw.githubusercontent.com (environ 5 min) : attendre ou verifier par l'API contents avant de conclure.

Tout autre ecart est un vrai ecart a traiter.

## Compte rendu a l'utilisateur

- Donner les lignes `RESULTAT` et `PAR PAIRE` telles quelles.
- Lister les ecarts hors faux positifs (fichier, niveau en retard). S'il n'y en a pas, le dire.
- Donner le chemin du rapport dans `historique\MD5\`.
- Ne rien pousser ni corriger sans demande. Pour une prod en retard, proposer ha-push-md ou ha-push-docs.
- Repondre en francais, concis, sans emojis ni tableaux.