---
name: "ha-push-yaml"
description: "HA ReBuild skill - pushes local config YAML files to the HA prod (root H:\\ AND docs mirror), local .bak backup before any change, MD5-first. Trigger on: pousse le yaml en prod, deploie le fichier YAML, on met ca en prod."
---

# HA Push YAML - Local 01_config_system_SH_PY_YAML -> Prod H:\

> CRITICAL OPERATION: a malformed YAML, or one pushed to the wrong place, can break HA.
> MD5-first logic: if the file is identical in prod, the push is cancelled.

## REFERENCE PATHS

- **Source (Windows)**: `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\`

`01_config_system_SH_PY_YAML\` is the LOCAL IMAGE of prod (H:\): each file has the same
name and the same relative path as on H:\ (never a suffix in the name of the current
file), so that it stays comparable 1:1 with prod at any time. LOCAL is the truth:
prod must never be ahead of local (Eric's rule of 2026-10-18).

EXCEPTION since 2026-10-29: under `.scripts\` and `command_line\`, local puts each file
in its own folder; prod root (PR) stays FLAT. See FLATTENING RULE.

**Map of locations (single source, read it when in doubt)**:
`docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md`.
Each config file exists in 5 locations: local (L), prod root `/config` (PR = H:\),
prod docs mirror (PM = `H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\`),
GitHub root (GR) and GitHub `docs/` (GD). This skill pushes to PR AND PM (never only one
of the two). GitHub follows at the HA backup launched by Eric (never a direct push).

| Local source (under 01_config_system_SH_PY_YAML\) | Prod root (PR) | Prod mirror (PM) |
|:---|:---|:---|
| sensors/, templates/, utility_meter/, groups/, input_booleans/, input_number/, shell_command/, timers/ | H:\<same path> | H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\<same path> |
| configuration.yaml, sql.yaml, input_button.yaml, input_datetime.yaml, input_select.yaml | H:\<file> | same as mirror |
| .scripts\01_scripts.sh\<nom>_sh\<nom>.sh and .scripts\02_scripts.py\<nom>_py\<nom>.py | H:\.scripts\<nom>.<ext> (FLAT) | same as local (full path with folders) |
| command_line\<categorie>\<nom>_yaml\<nom>.yaml | H:\command_line\<categorie>\<nom>.yaml (FLAT) | same as local (full path with folders) |
| scripts\*.sh | H:\scripts\<file> | same as mirror |
| themes/, blueprints/, notifs/, scenes.yaml, ip_bans.yaml | PROD ONLY - never push | - |
| Automations | FORBIDDEN - HA UI only | - |

`.sh` / `.py` scripts: push to `H:\.scripts\` or `H:\scripts\` only on Eric's explicit order.

## FLATTENING RULE (added 2026-10-29, Eric's order)

LOCAL puts `.scripts\` and `command_line\` ONE FOLDER PER FILE (folder = `<name without extension>_<extension>`):
- `.scripts\01_scripts.sh\<nom>_sh\<nom>.sh` and `.scripts\02_scripts.py\<nom>_py\<nom>.py`
- `command_line\<categorie>\<nom>_yaml\<nom>.yaml`

HOME ASSISTANT STAYS FLAT: in prod root (PR), `/config/.scripts/<nom>.<ext>` and
`/config/command_line/<categorie>/<nom>.yaml`. `configuration.yaml` loads `command_line/` with
`!include_dir_merge_list` (recursive): a file pushed one folder too deep would be read TWICE
(same unique_id, duplicated sensors). The `shell_command` entries call absolute flat paths
(`/config/.scripts/<nom>`): a misplaced file breaks the call. The mirror (PM) and GitHub `docs/` (GD)
keep the local structure; prod root (PR) and GitHub root (GR) are flat.

Computation of the prod root path (validated on 2026-10-29 on the 12 files concerned, all present flat in prod):

```powershell
function Get-RelProd([string]$rel) {   # $rel = relative path under 01_config_system_SH_PY_YAML\, separator \
  $p = @($rel -split '\\')
  if ($p[0] -notin '.scripts','command_line') { return $rel }          # other folders: unchanged
  if ($p[0] -eq '.scripts' -and $p.Count -ge 3 -and $p[1] -in '01_scripts.sh','02_scripts.py') { $p = @('.scripts') + @($p[2..($p.Count-1)]) }
  $cible = if ($p[0] -eq '.scripts') { 2 } else { 3 }                   # flat depth
  if ($p.Count -gt $cible) {
    $leaf = $p[-1]; $stem = [IO.Path]::GetFileNameWithoutExtension($leaf); $ext = [IO.Path]::GetExtension($leaf).TrimStart('.')
    if ($p[-2] -cne "${stem}_${ext}") { return $null }                  # folder that does not carry the file name
    $p = @($p[0..($p.Count-3)]) + $leaf                                 # remove the folder of the file
  }
  if ($p.Count -ne $cible) { return $null }                              # NON CONFORME: push nothing
  return ($p -join '\')
}
$rel     = 'command_line\Audit\audit_md5_yaml_yaml\audit_md5_yaml.yaml'   # example
$relProd = Get-RelProd $rel      # -> command_line\Audit\audit_md5_yaml.yaml ; $null = STOP
$dest    = "H:\$relProd"                                                   # PR (flat)
$destPM  = "H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\$rel"  # PM (local structure)
```

In steps 2 and 6, `{sous-chemin racine}` is the folder returned by `Get-RelProd`, `{sous-chemin}` is the local path.
If `Get-RelProd` returns `$null`: STOP, push nothing, warn Eric. Verif_emplacements.py applies the same
rule (section 4 STRUCTURE NON CONFORME of its report).

## BACKUP RULE (since 2026-10-08, replaces the one of 2026-10-04)

- ALWAYS modify in local (`ReBuild\docs`), then push to H:. Never a backup on H: nor on D: (do not fill the SSD of the mini PC).
- Before EACH modification, copy the file next to itself as `fichier.yaml.bak_AAAA_MM_JJ_HHhMMmSSs` (e.g. `P1_kWh_clim.yaml.bak_2026_10_08_08h54m30s`).
- Same day: 10 backups max per file. The 11th sends the oldest to the WINDOWS RECYCLE BIN.
- The next day, `/histo` does the cleanup: per file and per past day, it keeps the MOST RECENT backup, renames it `fichier.yaml.bak_AAAA_MM_JJ` and sends the others to the Windows recycle bin. It never touches the backups of the current day.
- Previous days: 3 `.bak_AAAA_MM_JJ` max per file. The 4th (the oldest) goes to the Windows recycle bin.
- "Trash" = Windows recycle bin (never a permanent deletion). There is no recycle bin on H: : any deletion in prod first goes through a copy in `TEMPO\<operation>_AAAA-MM-JJ\` (same tree, MD5 of the copy verified), then deletion on H: and a report in the modifications journal (TEMPO rule of CLAUDE.md of 2026-10-18).
- Restore: remove the `.bak_...` suffix from the name. Prod NEVER receives a name with a `.bak_...` suffix.

## WORKFLOW

### BEFORE ANY PUSH - Check of the XX_ folders (decided by Eric on 2026-10-25 21:19, mandatory)

The `XX_` folders exist only locally and must never be lost. Before the first computation of this skill, AND a second time right after the push (before/after check), run:
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\Check_XX_presents.py"`
It also refuses any XX_ folder present in prod (ALERTE). It compares the XX_ folders and their files with the manifest `XX_manifest.json` (same folder). `RESULTAT : OK` = continue. An ALERTE (missing folder or file) = push NOTHING, warn Eric, restore from `TEMPO\XX_sauvegarde_2026-10-25` only on his order. XX_ folders are never pushed to prod. The manifest is updated (`--maj`) only on Eric's order.

### 0 - BEFORE ANY MODIFICATION OF AN EXISTING FILE: local backup

```powershell
$src = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}\{fichier}.yaml"

if (Test-Path $src) {
  $suffixe = Get-Date -Format "yyyy_MM_dd_HH'h'mm'm'ss's'"   # e.g. 2026_10_08_12h07m20s
  $backup = "$src.bak_$suffixe"
  Copy-Item $src $backup
  Write-Host "Sauvegarde creee : $backup"
}
```

Daily cap: 10 backups max per file. If there are already 10 for TODAY,
the oldest of the day goes to the Windows recycle bin before a new one is created:

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

(Run it before the Copy-Item so that the total for the day stays at 10 max.)

The cleanup of previous days (renaming to `.bak_AAAA_MM_JJ`, 3 max) is NOT done here:
it is the job of `/histo`. Do not do it by hand unless asked.

Then modify the file `{fichier}.yaml` (without suffix): it is the one that will be
compared then pushed to prod in the next steps.

### 1 - Local MD5 of the target file
```powershell
$src = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}\{fichier}.yaml"
$localHash = (Get-FileHash $src -Algorithm MD5).Hash
Write-Host "Local : $localHash"
```

### 2 - Prod MD5 in the TWO locations (root PR and mirror PM)
```powershell
$dest   = "H:\{sous-chemin racine}\{fichier}.yaml"   # PR: {sous-chemin racine} = Get-RelProd of {sous-chemin} (FLATTENING RULE)
$destPM = "H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}\{fichier}.yaml"   # PM
$prodHash = if (Test-Path $dest)   { (Get-FileHash $dest   -Algorithm MD5).Hash } else { $null }
$pmHash   = if (Test-Path $destPM) { (Get-FileHash $destPM -Algorithm MD5).Hash } else { $null }
Write-Host "Prod racine : $(if($prodHash){$prodHash}else{'ABSENT'})"
Write-Host "Prod miroir : $(if($pmHash){$pmHash}else{'ABSENT'})"
```

### 3 - Compare
```powershell
if ($localHash -eq $prodHash -and $localHash -eq $pmHash) {
  Write-Host "MD5 identiques aux deux emplacements - rien a pousser."
  exit
}
Write-Host "DIFF detecte (racine et/ou miroir)."
```

If MD5 are identical in both locations -> **stop immediately**. If only one of the two
differs, push only that one.

If prod (root or mirror) differs from local AND also differs from the local version from before
the modification (the `.bak` backup of the day), someone wrote in prod: do not push, report it
to Eric (prod must not be ahead, but it is not overwritten without saying so).

### 4 - Pre-push checks (if DIFF)

- `.yaml` extension + not `secrets.yaml` + not an automation
- Valid YAML: no tabs, at least 1 `unique_id:`

```powershell
$f = "C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}\{fichier}.yaml"
if (Select-String -Path $f -Pattern "`t" -Quiet) { "TABULATIONS DETECTEES" } else { "OK pas de tabulation" }
(Select-String -Path $f -Pattern "unique_id:").Count
```

### 5 - Explicit user confirmation
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
Wait for the answer before continuing.

### 6 - Push

**Absolute rule: prod (H:\) NEVER receives a file name with a `.bak_...` suffix.**
Even if the pushed file is a backup (restoring an old version), the destination name
is always rebuilt WITHOUT the suffix before the copy. If no precise file is given
(ambiguity about which one to push), **the most recent is taken by default** (the
current file without suffix if it exists, otherwise the most recent backup):

```powershell
# If $src carries a .bak_... suffix (restoring a backup), remove it
# to build the destination name - prod must never see a suffix.
$nomSansBak = (Split-Path $src -Leaf) -replace '\.bak_\d{4}_\d{2}_\d{2}(_\d{2}h\d{2}m\d{2}s)?$', ''
$dest = Join-Path "H:\{sous-chemin racine}" $nomSansBak

$destPM = Join-Path "H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\{sous-chemin}" $nomSansBak

foreach ($d in $dest, $destPM) {
  New-Item -ItemType Directory -Path (Split-Path $d) -Force | Out-Null
  Copy-Item $src $d -Force
  Write-Host "Pousse : $d (source : $(Split-Path $src -Leaf))"
}
```

Prod (H:\) receives ONLY the current file, name without suffix - never a `.bak_...`.
The version history stays only in local.

### 7 - Final MD5 verification
```powershell
$h1 = (Get-FileHash $src -Algorithm MD5).Hash
foreach ($d in $dest, $destPM) {
  $h2 = (Get-FileHash $d -Algorithm MD5).Hash
  if ($h1 -eq $h2) { "OK MD5 identiques : $d" } else { "DIFF - verifier ! $d" }
}
```

Optional global check (read-only, 5 locations):
`$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py"`
(report in `historique\MD5\03_verif_emplacements\`). After the push, the file must come out
SYNC or GITHUB EN ATTENTE DU BACKUP.

### 8 - HA reload
- Developer tools > YAML > **Check configuration**
- If OK -> **Reload** the domain concerned (sensors, templates, utility_meter...)
- Check the HA logs (Settings > System > Logs)

## RULES

1. **MD5 first** - if identical in prod, do not push.
2. **User confirmation mandatory** before any push.
3. **secrets.yaml -> absolute prohibition.**
4. **automations.yaml -> HA UI only.**
5. **Never a backup in prod (H:\) nor on D:** - any backup is done on the local side,
   before modification, in the format `fichier.yaml.bak_AAAA_MM_JJ_HHhMMmSSs` (see step 0).
6. **10 backups max per file on the same day** - the 11th sends the oldest of the
   day to the Windows recycle bin.
7. **Previous days: 3 `.bak_AAAA_MM_JJ` max per file**, the oldest in the Windows
   recycle bin. The renaming and the cleanup are done by `/histo` the next day
   (the most recent of the day is kept). Never touch the backups of the current day.
8. **Prod never receives a file name with a `.bak_...` suffix** - the suffix is
   always removed at push time, even if the pushed source carries one.
9. **In case of ambiguity about which file to push, take the most recent** (the current
   file without suffix if it exists, otherwise the most recent backup).
10. **A problem (name collision, unreadable date, doubtful backup): report it to
    the user and delete nothing.**
11. **Two destinations in prod** (decided by Eric on 2026-10-18): root `H:\` (PR) AND
    mirror `H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\` (PM), MD5 verified on
    each. Never only one of the two. See `IA_CARTE_EMPLACEMENTS.md`.
12. **Prod only**: themes/, blueprints/, notifs/, scenes.yaml, ip_bans.yaml, secrets.yaml are
    never pushed (Eric's decisions of 2026-10-18).
13. **.sh / .py scripts**: flat in `H:\.scripts\` in prod (sub-folders 01_scripts.sh,
    02_scripts.py and the `<nom>_<ext>` folder of the file in local only); push only on
    Eric's explicit order.
14. **Flattening mandatory** (2026-10-29): the prod root path of `.scripts\` and of
    `command_line\` is ALWAYS computed with `Get-RelProd`. `$null` (non-conforming structure) = STOP.
    After a push in `command_line\`, check that no `<nom>_yaml` folder exists in prod
    (`Get-ChildItem H:\command_line -Directory -Recurse`: only category folders).

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_push_yaml/ha_push_yaml.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-push-yaml/SKILL.md` must stay identical to this copy.
