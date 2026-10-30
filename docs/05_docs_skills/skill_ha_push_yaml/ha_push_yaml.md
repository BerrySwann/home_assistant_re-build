---
name: "ha-push-yaml"
description: "Skill HA ReBuild - pousse des YAML config locaux vers la prod HA (racine H:\\ ET miroir docs), sauvegarde locale .bak avant modification, MD5-first. Declencher sur : pousse le yaml en prod, deploie le fichier YAML, on met ca en prod."
---

# HA Push YAML - Local 01_config_system_SH_PY_YAML -> Prod H:\

> OPERATION CRITIQUE : un YAML mal forme ou pousse au mauvais endroit peut casser HA.
> Logique MD5-first : si le fichier est identique en prod, le push est annule.

## CHEMINS DE REFERENCE

- **Source (Windows)** : `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\`

`01_config_system_SH_PY_YAML\` est l'IMAGE LOCALE de la prod (H:\) : chaque fichier y a le meme
nom et le meme chemin relatif que sur H:\ (jamais de suffixe dans le nom du fichier
courant), pour rester comparable 1:1 avec la prod a tout moment. Le LOCAL fait foi :
la prod ne doit jamais etre en avance sur le local (regle d'Eric du 2026-10-18).

EXCEPTION depuis le 2026-10-29 : sous `.scripts\` et `command_line\`, le local range chaque
fichier dans son propre dossier ; la prod racine (PR) reste A PLAT. Voir REGLE D'APLATISSEMENT.

**Carte des emplacements (source unique, a lire en cas de doute)** :
`docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md`.
Chaque fichier de config existe a 5 emplacements : local (L), prod racine `/config` (PR = H:\),
prod miroir docs (PM = `H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\`),
GitHub racine (GR) et GitHub `docs/` (GD). Ce skill pousse vers PR ET PM (jamais un seul
des deux). GitHub suit au backup HA lance par Eric (jamais de push direct).

| Source locale (sous 01_config_system_SH_PY_YAML\) | Prod racine (PR) | Prod miroir (PM) |
|:---|:---|:---|
| sensors/, templates/, utility_meter/, groups/, input_booleans/, input_number/, shell_command/, timers/ | H:\<meme chemin> | H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\<meme chemin> |
| configuration.yaml, sql.yaml, input_button.yaml, input_datetime.yaml, input_select.yaml | H:\<fichier> | idem miroir |
| .scripts\01_scripts.sh\<nom>_sh\<nom>.sh et .scripts\02_scripts.py\<nom>_py\<nom>.py | H:\.scripts\<nom>.<ext> (A PLAT) | idem local (chemin complet avec dossiers) |
| command_line\<categorie>\<nom>_yaml\<nom>.yaml | H:\command_line\<categorie>\<nom>.yaml (A PLAT) | idem local (chemin complet avec dossiers) |
| scripts\*.sh | H:\scripts\<fichier> | idem miroir |
| themes/, blueprints/, notifs/, scenes.yaml, ip_bans.yaml | PROD SEULE - ne jamais pousser | - |
| Automations | INTERDIT - UI HA uniquement | - |

Scripts `.sh` / `.py` : push vers `H:\.scripts\` ou `H:\scripts\` uniquement sur ordre explicite d'Eric.

## REGLE D'APLATISSEMENT (ajoutee le 2026-10-29, ordre d'Eric)

Le LOCAL range `.scripts\` et `command_line\` UN DOSSIER PAR FICHIER (dossier = `<nom sans extension>_<extension>`) :
- `.scripts\01_scripts.sh\<nom>_sh\<nom>.sh` et `.scripts\02_scripts.py\<nom>_py\<nom>.py`
- `command_line\<categorie>\<nom>_yaml\<nom>.yaml`

HOME ASSISTANT RESTE A PLAT : en prod racine (PR), `/config/.scripts/<nom>.<ext>` et
`/config/command_line/<categorie>/<nom>.yaml`. `configuration.yaml` charge `command_line/` par
`!include_dir_merge_list` (recursif) : un fichier pousse un dossier trop bas serait lu EN DOUBLE
(meme unique_id, capteurs dupliques). Les `shell_command` appellent des chemins plats absolus
(`/config/.scripts/<nom>`) : un fichier mal place casse l'appel. Le miroir (PM) et GitHub `docs/` (GD)
gardent la structure locale ; la prod racine (PR) et GitHub racine (GR) sont a plat.

Calcul du chemin prod racine (valide le 2026-10-29 sur les 12 fichiers concernes, tous presents a plat en prod) :

```powershell
function Get-RelProd([string]$rel) {   # $rel = chemin relatif sous 01_config_system_SH_PY_YAML\, separateur \
  $p = @($rel -split '\\')
  if ($p[0] -notin '.scripts','command_line') { return $rel }          # autres dossiers : inchange
  if ($p[0] -eq '.scripts' -and $p.Count -ge 3 -and $p[1] -in '01_scripts.sh','02_scripts.py') { $p = @('.scripts') + @($p[2..($p.Count-1)]) }
  $cible = if ($p[0] -eq '.scripts') { 2 } else { 3 }                   # profondeur a plat
  if ($p.Count -gt $cible) {
    $leaf = $p[-1]; $stem = [IO.Path]::GetFileNameWithoutExtension($leaf); $ext = [IO.Path]::GetExtension($leaf).TrimStart('.')
    if ($p[-2] -cne "${stem}_${ext}") { return $null }                  # dossier qui ne porte pas le nom du fichier
    $p = @($p[0..($p.Count-3)]) + $leaf                                 # retire le dossier du fichier
  }
  if ($p.Count -ne $cible) { return $null }                              # NON CONFORME : ne rien pousser
  return ($p -join '\')
}
$rel     = 'command_line\Audit\audit_md5_yaml_yaml\audit_md5_yaml.yaml'   # exemple
$relProd = Get-RelProd $rel      # -> command_line\Audit\audit_md5_yaml.yaml ; $null = ARRET
$dest    = "H:\$relProd"                                                   # PR (a plat)
$destPM  = "H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\$rel"  # PM (structure locale)
```

Dans les etapes 2 et 6, `{sous-chemin racine}` est le dossier de `Get-RelProd`, `{sous-chemin}` le chemin local.
Si `Get-RelProd` renvoie `$null` : ARRET, ne rien pousser, prevenir Eric. Verif_emplacements.py applique la meme
regle (section 4 STRUCTURE NON CONFORME de son rapport).

## REGLE DE SAUVEGARDE (depuis le 2026-10-08, remplace celle du 2026-10-04)

- On modifie TOUJOURS en local (`ReBuild\docs`), puis on pousse vers H:. Jamais de sauvegarde sur H: ni sur D: (ne pas remplir le SSD du mini PC).
- Avant CHAQUE modification, copier le fichier a cote de lui sous `fichier.yaml.bak_AAAA_MM_JJ_HHhMMmSSs` (ex : `P1_kWh_clim.yaml.bak_2026_10_08_08h54m30s`).
- Jour meme : 10 sauvegardes max par fichier. La 11e envoie la plus ancienne a la CORBEILLE WINDOWS.
- Le lendemain, `/histo` fait le menage : par fichier et par jour passe, il garde la sauvegarde la plus RECENTE, la renomme `fichier.yaml.bak_AAAA_MM_JJ` et envoie les autres a la corbeille Windows. Il ne touche jamais aux sauvegardes du jour.
- Jours precedents : 3 `.bak_AAAA_MM_JJ` max par fichier. La 4e (la plus ancienne) va a la corbeille Windows.
- "Poubelle" = corbeille Windows (jamais de suppression definitive). Pas de corbeille sur H: : toute suppression en prod passe d'abord par une copie dans `TEMPO\<operation>_AAAA-MM-JJ\` (meme arborescence, MD5 de la copie verifie), puis suppression sur H: et rapport dans le journal des modifs (regle TEMPO de CLAUDE.md du 2026-10-18).
- Restauration : retirer le suffixe `.bak_...` du nom. La prod ne recoit JAMAIS de nom avec suffixe `.bak_...`.

## WORKFLOW

### AVANT TOUT PUSH - Controle des dossiers XX_ (decide par Eric le 2026-10-25 21:19, obligatoire)

Les dossiers `XX_` n'existent qu'en local et ne doivent jamais se perdre. Avant le premier calcul de ce skill, ET une seconde fois juste apres le push (controle avant/apres), lancer :
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\Check_XX_presents.py"`
Il refuse aussi tout dossier XX_ present en prod (ALERTE). Il compare les dossiers XX_ et leurs fichiers au manifeste `XX_manifest.json` (meme dossier). `RESULTAT : OK` = on continue. Une ALERTE (dossier ou fichier manquant) = ne RIEN pousser, prevenir Eric, restaurer depuis `TEMPO\XX_sauvegarde_2026-10-25` seulement sur son ordre. Les XX_ ne se poussent jamais en prod. Le manifeste ne se met a jour (`--maj`) que sur ordre d'Eric.

### 0 - AVANT TOUTE MODIFICATION D'UN FICHIER EXISTANT : sauvegarde locale

```powershell
$src = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}\{fichier}.yaml"

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
$src = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}\{fichier}.yaml"
$localHash = (Get-FileHash $src -Algorithm MD5).Hash
Write-Host "Local : $localHash"
```

### 2 - MD5 prod aux DEUX emplacements (racine PR et miroir PM)
```powershell
$dest   = "H:\{sous-chemin racine}\{fichier}.yaml"   # PR : {sous-chemin racine} = Get-RelProd de {sous-chemin} (REGLE D'APLATISSEMENT)
$destPM = "H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}\{fichier}.yaml"   # PM
$prodHash = if (Test-Path $dest)   { (Get-FileHash $dest   -Algorithm MD5).Hash } else { $null }
$pmHash   = if (Test-Path $destPM) { (Get-FileHash $destPM -Algorithm MD5).Hash } else { $null }
Write-Host "Prod racine : $(if($prodHash){$prodHash}else{'ABSENT'})"
Write-Host "Prod miroir : $(if($pmHash){$pmHash}else{'ABSENT'})"
```

### 3 - Comparer
```powershell
if ($localHash -eq $prodHash -and $localHash -eq $pmHash) {
  Write-Host "MD5 identiques aux deux emplacements - rien a pousser."
  exit
}
Write-Host "DIFF detecte (racine et/ou miroir)."
```

Si MD5 identiques aux deux emplacements -> **arreter immediatement**. Si un seul des deux
differe, ne pousser que celui-la.

Si la prod (racine ou miroir) differe du local ET differe aussi de la version locale d'avant
la modification (sauvegarde `.bak` du jour), quelqu'un a ecrit en prod : ne pas pousser, le
signaler a Eric (la prod ne doit pas etre en avance, mais on ne l'ecrase pas sans le dire).

### 4 - Checks pre-push (si DIFF)

- Extension `.yaml` + pas `secrets.yaml` + pas automation
- YAML valide : pas de tabulations, au moins 1 `unique_id:`

```powershell
$f = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}\{fichier}.yaml"
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
Prod racine: {hash_prod} (DIFF / NOUVEAU / identique)
Prod miroir: {hash_pm} (DIFF / NOUVEAU / identique)
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
$dest = Join-Path "H:\{sous-chemin racine}" $nomSansBak

$destPM = Join-Path "H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}" $nomSansBak

foreach ($d in $dest, $destPM) {
  New-Item -ItemType Directory -Path (Split-Path $d) -Force | Out-Null
  Copy-Item $src $d -Force
  Write-Host "Pousse : $d (source : $(Split-Path $src -Leaf))"
}
```

La prod (H:\) ne recoit QUE le fichier courant, nom sans suffixe - jamais de `.bak_...`.
L'historique des versions reste uniquement en local.

### 7 - Verification MD5 finale
```powershell
$h1 = (Get-FileHash $src -Algorithm MD5).Hash
foreach ($d in $dest, $destPM) {
  $h2 = (Get-FileHash $d -Algorithm MD5).Hash
  if ($h1 -eq $h2) { "OK MD5 identiques : $d" } else { "DIFF - verifier ! $d" }
}
```

Controle global facultatif (lecture seule, 5 emplacements) :
`$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py"`
(rapport dans `historique\MD5\03_verif_emplacements\`). Apres le push, le fichier doit
sortir SYNC ou GITHUB EN ATTENTE DU BACKUP.

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
11. **Deux destinations en prod** (decide par Eric le 2026-10-18) : racine `H:\` (PR) ET
    miroir `H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\` (PM), MD5 verifie sur
    chacune. Jamais un seul des deux. Voir `IA_CARTE_EMPLACEMENTS.md`.
12. **Prod seule** : themes/, blueprints/, notifs/, scenes.yaml, ip_bans.yaml, secrets.yaml ne
    sont jamais pousses (decisions d'Eric du 2026-10-18).
13. **Scripts .sh / .py** : a plat dans `H:\.scripts\` en prod (sous-dossiers 01_scripts.sh,
    02_scripts.py et dossier `<nom>_<ext>` du fichier en local seulement) ; push uniquement sur
    ordre explicite d'Eric.
14. **Aplatissement obligatoire** (2026-10-29) : le chemin prod racine de `.scripts\` et de
    `command_line\` se calcule TOUJOURS avec `Get-RelProd`. `$null` (structure non conforme) = ARRET.
    Apres un push dans `command_line\`, verifier qu'aucun dossier `<nom>_yaml` n'existe en prod
    (`Get-ChildItem H:\command_line -Directory -Recurse` : seuls les dossiers de categorie).