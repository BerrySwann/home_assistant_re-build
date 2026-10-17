---
name: "ha-push-yaml"
description: "Skill HA ReBuild - pousse des fichiers YAML config locaux vers la prod HA (H:\\), avec sauvegarde locale .bak_AAAA_MM_JJ_HHhMMmSSs avant toute modification (jamais de sauvegarde en prod). MD5-first : pousse uniquement si le fichier est different de la prod. Declencher sur : \"pousse le yaml en prod\", \"deploie le fichier YAML\", \"copie vers H:\\\", \"met a jour la prod avec ce YAML\", \"valide et pousse\", \"on met ca en prod\". OPERATION CRITIQUE."
---

# HA Push YAML - Local config_system_YAML -> Prod H:\

> OPERATION CRITIQUE : un YAML mal forme ou pousse au mauvais endroit peut casser HA.
> Logique MD5-first : si le fichier est identique en prod, le push est annule.

## CHEMINS DE REFERENCE

- **Source (Windows)** : `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\`

`config_system_YAML\` est l'IMAGE LOCALE de la prod (H:\) : chaque fichier y a le meme
nom et le meme chemin relatif que sur H:\ (jamais de suffixe dans le nom du fichier
courant), pour rester comparable 1:1 avec la prod a tout moment (voir ha-resync-docs
pour la tenir a jour depuis GitHub).

| Source locale | Prod HA |
|:---|:---|
| sensors/ | H:\sensors\ |
| templates/ | H:\templates\ |
| utility_meter/ | H:\utility_meter\ |
| command_line/ | H:\command_line\ |
| input_booleans/ | H:\input_booleans\ |
| groups/ | H:\groups\ |
| shell_command/ | H:\shell_command\ |
| themes/ | H:\themes\ |
| blueprints/ | H:\blueprints\ |
| Automations | INTERDIT - UI HA uniquement |

## REGLE DE SAUVEGARDE (depuis le 2026-10-08, remplace celle du 2026-10-04)

- On modifie TOUJOURS en local (`ReBuild\docs`), puis on pousse vers H:. Jamais de sauvegarde sur H: ni sur D: (ne pas remplir le SSD du mini PC).
- Avant CHAQUE modification, copier le fichier a cote de lui sous `fichier.yaml.bak_AAAA_MM_JJ_HHhMMmSSs` (ex : `P1_kWh_clim.yaml.bak_2026_10_08_08h54m30s`).
- Jour meme : 10 sauvegardes max par fichier. La 11e envoie la plus ancienne a la CORBEILLE WINDOWS.
- Le lendemain, `/histo` fait le menage : par fichier et par jour passe, il garde la sauvegarde la plus RECENTE, la renomme `fichier.yaml.bak_AAAA_MM_JJ` et envoie les autres a la corbeille Windows. Il ne touche jamais aux sauvegardes du jour.
- Jours precedents : 3 `.bak_AAAA_MM_JJ` max par fichier. La 4e (la plus ancienne) va a la corbeille Windows.
- "Poubelle" = corbeille Windows (jamais de suppression definitive). Pas de corbeille sur H:.
- Restauration : retirer le suffixe `.bak_...` du nom. La prod ne recoit JAMAIS de nom avec suffixe `.bak_...`.

## WORKFLOW

### 0 - AVANT TOUTE MODIFICATION D'UN FICHIER EXISTANT : sauvegarde locale

```powershell
$src = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\{sous-chemin}\{fichier}.yaml"

if (Test-Path $src) {
  $suffixe = Get-Date -Format "yyyy_MM_dd_HH'h'mm'm'ss's'"   # ex 2026_10_08_12h07m20s
  $backup = "$src.bak_$suffixe"
  Copy-Item $src $backup
  Write-Host "Sauvegarde creee : $backup"
}
```

Plafond du jour : 10 sauvegardes max par fichier. S'il y en a deja 10 pour AUJOURD'HUI,
la plus ancienne du jour va a la corbeille Windows avant d'en creer une nouvelle :

```powershell
Add-Type -AssemblyName Microsoft.VisualBasic
$today = Get-Date -Format "yyyy_MM_dd"
$base = Split-Path $src -Leaf
$dir = Split-Path $src
$jour = @(Get-ChildItem -Path $dir -File | Where-Object { $_.Name -like "$base.bak_${today}_*h*m*s" } | Sort-Object Name)
if ($jour.Count -ge 10) {
  $old = $jour[0].FullName
  [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($old,'OnlyErrorDialogs','SendToRecycleBin')
  Write-Host "Corbeille Windows (plus ancienne du jour) : $old"
}
```

(A executer avant le Copy-Item pour que le total du jour reste a 10 max.)

Le menage des jours precedents (renommage en `.bak_AAAA_MM_JJ`, 3 max) n'est PAS fait ici :
c'est le travail de `/histo`. Ne pas le faire a la main sans demande.

Modifier ensuite le fichier `{fichier}.yaml` (sans suffixe) : c'est lui qui sera
compare puis pousse vers la prod aux etapes suivantes.

### 1 - MD5 local du fichier cible
```powershell
$src = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\{sous-chemin}\{fichier}.yaml"
$localHash = (Get-FileHash $src -Algorithm MD5).Hash
Write-Host "Local : $localHash"
```

### 2 - MD5 prod (H:\)
```powershell
$dest = "H:\{sous-chemin}\{fichier}.yaml"
if (Test-Path $dest) {
  $prodHash = (Get-FileHash $dest -Algorithm MD5).Hash
  Write-Host "Prod  : $prodHash"
} else {
  $prodHash = $null
  Write-Host "Prod  : ABSENT (nouveau fichier)"
}
```

### 3 - Comparer
```powershell
if ($localHash -eq $prodHash) {
  Write-Host "MD5 identiques - fichier deja a jour en prod. Rien a pousser."
  exit
}
Write-Host "DIFF detecte - le fichier local est different de la prod."
```

Si MD5 identiques -> **arreter immediatement**.

### 4 - Checks pre-push (si DIFF)

- Extension `.yaml` + pas `secrets.yaml` + pas automation
- YAML valide : pas de tabulations, au moins 1 `unique_id:`

```powershell
$f = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\{sous-chemin}\{fichier}.yaml"
if (Select-String -Path $f -Pattern "`t" -Quiet) { "TABULATIONS DETECTEES" } else { "OK pas de tabulation" }
(Select-String -Path $f -Pattern "unique_id:").Count
```

### 5 - Confirmation explicite utilisateur
```
RESUME PRE-PUSH
--------------------------------------------------
Fichier    : {sous-chemin}/{fichier}.yaml
Sauvegarde : {fichier}.yaml.bak_AAAA_MM_JJ_HHhMMmSSs (creee avant modif, locale uniquement)
Local      : {hash_local}
Prod       : {hash_prod} (DIFF / NOUVEAU)
--------------------------------------------------
Confirmes-tu le push ? (oui / non)
```
Attendre la reponse avant de continuer.

### 6 - Push

**Regle absolue : la prod (H:\) ne recoit JAMAIS un nom de fichier avec un suffixe
`.bak_...`.** Meme si le fichier pousse est une sauvegarde (restauration d'une ancienne
version), le nom de destination est toujours reconstruit SANS le suffixe avant la copie.
Si aucun fichier precis n'est indique (ambiguite sur lequel pousser), **on prend par
defaut le plus recent** (le fichier courant sans suffixe s'il existe, sinon la
sauvegarde la plus recente) :

```powershell
# Si $src porte un suffixe .bak_... (restauration d'une sauvegarde), on le retire
# pour construire le nom de destination - la prod ne doit jamais voir de suffixe.
$nomSansBak = (Split-Path $src -Leaf) -replace '\.bak_\d{4}_\d{2}_\d{2}(_\d{2}h\d{2}m\d{2}s)?$', ''
$dest = Join-Path "H:\{sous-chemin}" $nomSansBak

$destDir = Split-Path $dest
New-Item -ItemType Directory -Path $destDir -Force | Out-Null
Copy-Item $src $dest -Force
Write-Host "Pousse : $nomSansBak (source : $(Split-Path $src -Leaf))"
```

La prod (H:\) ne recoit QUE le fichier courant, nom sans suffixe - jamais de `.bak_...`.
L'historique des versions reste uniquement en local.

### 7 - Verification MD5 finale
```powershell
$h1 = (Get-FileHash $src -Algorithm MD5).Hash
$h2 = (Get-FileHash $dest -Algorithm MD5).Hash
if ($h1 -eq $h2) { "OK MD5 identiques" } else { "DIFF - verifier !" }
```

### 8 - Rechargement HA
- Outils dev > YAML > **Verifier la configuration**
- Si OK -> **Recharger** le domaine concerne (sensors, templates, utility_meter...)
- Verifier logs HA (Settings > System > Logs)

## REGLES

1. **MD5 d'abord** - si identique en prod, ne pas pousser.
2. **Confirmation utilisateur obligatoire** avant tout push.
3. **secrets.yaml -> interdit absolu.**
4. **automations.yaml -> UI HA uniquement.**
5. **Jamais de sauvegarde en prod (H:\) ni sur D:** - toute sauvegarde se fait cote local,
   avant modification, au format `fichier.yaml.bak_AAAA_MM_JJ_HHhMMmSSs` (voir etape 0).
6. **10 sauvegardes max par fichier le jour meme** - la 11e envoie la plus ancienne du
   jour a la corbeille Windows.
7. **Jours precedents : 3 `.bak_AAAA_MM_JJ` max par fichier**, la plus ancienne en
   corbeille Windows. Le renommage et le menage sont faits par `/histo` le lendemain
   (la plus recente du jour est gardee). Ne jamais toucher aux sauvegardes du jour.
8. **La prod ne recoit jamais de nom de fichier avec suffixe `.bak_...`** - le suffixe est
   toujours retire au moment du push, meme si la source poussee en porte un.
9. **En cas d'ambiguite sur quel fichier pousser, prendre le plus recent** (le fichier
   courant sans suffixe s'il existe, sinon la sauvegarde la plus recente).
10. **Un souci (collision de nom, date illisible, sauvegarde douteuse) : le signaler a
    l'utilisateur et ne rien supprimer.**
