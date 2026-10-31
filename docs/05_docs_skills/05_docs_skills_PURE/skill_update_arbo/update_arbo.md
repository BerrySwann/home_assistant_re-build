---
name: "update-arbo"
description: "HA ReBuild skill - updates IA_ARBO_DETAIL.md (LOCAL + PROD + GitHub counts) after any session that adds, deletes or moves files. Trigger when the user types /update-arbo or after a resync, push or purge that changes the counts."
---

# Skill: /update-arbo - Update of IA_ARBO_DETAIL.md

> Files present in several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18).

## Goal

Refresh the counts and the version information in `IA_ARBO_DETAIL.md`
after every session that changes the number of files.

## Paths

| File | Path |
|:-----|:-----|
| Local | `C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` |
| Prod  | `H:\docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` |

## Execution protocol

### Step 1 - Real LOCAL counts (PowerShell)

```powershell
$base = "C:\Users\Berry Swann\Documents\ReBuild"

$docs_total  = (Get-ChildItem "$base\docs" -Recurse -File).Count
$histo_total = (Get-ChildItem "$base\historique" -File).Count
$docs_01     = (Get-ChildItem "$base\docs\01_docs_config_system" -Recurse -File).Count
$cfg_yaml    = (Get-ChildItem "$base\docs\01_docs_config_system\01_config_system_SH_PY_YAML" -Recurse -File).Count
$cfg_md      = (Get-ChildItem "$base\docs\01_docs_config_system\01_config_system_MD" -Recurse -File).Count
$docs_02     = (Get-ChildItem "$base\docs\02_docs_dashboard" -Recurse -File).Count
$docs_03     = (Get-ChildItem "$base\docs\03_docs_automations" -Recurse -File).Count
$docs_04     = (Get-ChildItem "$base\docs\04_docs_scripts" -Recurse -File).Count
$docs_05     = (Get-ChildItem "$base\docs\05_docs_skills" -Recurse -File).Count
$docs_xx     = (Get-ChildItem "$base\docs\99_docs_MD_system" -Recurse -File).Count
$dash_complet= (Get-ChildItem "$base\docs\02_docs_dashboard\02_dashboard_docs_YAML\Dashboard_COMPLET" -Filter "*.yaml").Count

Write-Host "LOCAL docs/ total   : $docs_total"
Write-Host "  historique/       : $histo_total"
Write-Host "  01_docs_config/   : $docs_01 (01_config_system_SH_PY_YAML : $cfg_yaml ; 01_config_system_MD : $cfg_md)"
Write-Host "  02_docs_dashboard : $docs_02 (Dashboard_COMPLET : $dash_complet yaml)"
Write-Host "  03_docs_automations: $docs_03"
Write-Host "  04_docs_scripts   : $docs_04"
Write-Host "  05_docs_skills    : $docs_05 (05_docs_skills_PURE + 05_docs_skills_MD + MOC_SKILLS.md, since 2026-10-31)"
Write-Host "  99_docs_MD_system : $docs_xx (local only)"
```

### Step 2 - Real PROD counts H:\docs (PowerShell)

```powershell
$prod_docs = (Get-ChildItem "H:\docs" -Recurse -File).Count
$prod_01   = (Get-ChildItem "H:\docs\01_docs_config_system" -Recurse -File -ErrorAction SilentlyContinue).Count
$prod_02   = (Get-ChildItem "H:\docs\02_docs_dashboard" -Recurse -File).Count
$prod_03   = (Get-ChildItem "H:\docs\03_docs_automations" -Recurse -File).Count
$prod_04   = (Get-ChildItem "H:\docs\04_docs_scripts" -Recurse -File).Count
$prod_05   = (Get-ChildItem "H:\docs\05_docs_skills" -Recurse -File -ErrorAction SilentlyContinue).Count
# XX_ folders never go to prod: no XX_ count in PROD (if one exists there, it is an ALERTE, see ha-push-md)

# Dashboard at the root of H:\
$dash_racine = Get-ChildItem "H:\" -Filter "Dashboard_*.yaml" | Sort-Object Name | Select-Object -Last 1 -ExpandProperty Name

Write-Host "PROD H:\docs/ total : $prod_docs"
Write-Host "  01_docs_config/   : $prod_01"
Write-Host "  02_docs_dashboard : $prod_02"
Write-Host "  03_docs_automations: $prod_03"
Write-Host "  04_docs_scripts   : $prod_04"
Write-Host "  05_docs_skills    : $prod_05"
Write-Host "Dashboard racine H:\ : $dash_racine"
```

### Step 3 - Last GitHub commit (PowerShell)

```powershell
$api = "https://api.github.com/repos/BerrySwann/home_assistant_re-build/commits/main"
$r   = Invoke-RestMethod $api -Headers @{"User-Agent"="PowerShell"}
$tree = Invoke-RestMethod "https://api.github.com/repos/BerrySwann/home_assistant_re-build/git/trees/main?recursive=1" -Headers @{"User-Agent"="PowerShell"}
$gh_total = $tree.tree.Count
$gh_docs  = ($tree.tree | Where-Object { $_.path -like "docs/*" }).Count

Write-Host "GitHub commit : $($r.sha.Substring(0,8)) - $($r.commit.author.date)"
Write-Host "GitHub tree   : $gh_total objets / docs/ : $gh_docs"
```

### Step 4 - Update IA_ARBO_DETAIL.md (PowerShell .Replace)

Read the file, make exact string replacements (do NOT use -replace regex
to avoid problems with special characters). Use:
```powershell
$c = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
$c = $c.Replace("old text", "new text")
[System.IO.File]::WriteAllText($path, $c, [System.Text.Encoding]::UTF8)
```

Do not give a helper function the name of a PowerShell alias (rd, h, ...), and remember that variable names are not case-sensitive ($E and $e are the same variable): both traps emptied files on 2026-10-31. Make a `.bak_AAAA_MM_JJ_HHhMMmSSs` first and check the file size after writing.

The trees are a two-column grid of fixed width: a replacement that changes the length of a line must remove or add as many spaces before the end border, to keep all the lines of the table at the same width (check after writing).

**Sections to update systematically:**

1. Header line `*Derniere mise a jour :` -> date + session summary
2. `releve YYYY-MM-DD)` in the LOCAL tree block -> today's date
3. `releve YYYY-MM-DD ; = H:\` in the PROD tree block -> today's date
4. `docs/ (NNN fichiers` -> new LOCAL count
5. `historique/ (NN` -> new count
6. `01_docs_config_system/ (NN` in LOCAL -> new count + note (sub-folders 01_config_system_MD and 01_config_system_SH_PY_YAML)
7. `02_docs_dashboard/ (NN` in LOCAL -> new count
8. `Dashboard_YYYY_MM-DD.yaml (export le plus recent)` -> name of the latest dashboard
9. `docs/ (NNN` in PROD -> new count
10. `Dernier releve arbre (API git trees)** : YYYY-MM-DD - **NNN` -> new
11. `dernier commit` hash and date -> new commit
12. `docs/` NNN in Repartition GitHub -> new count
13. `05_docs_skills/ (NN` in LOCAL and in PROD -> new counts (LOCAL block: PURE, MD and MOC_SKILLS.md rows; the PROD block keeps the old structure until the next push of /histo step 5C)

### Step 5 - Push to H:\docs

```powershell
$src  = "C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md"
$dest = "H:\docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md"
Copy-Item $src $dest -Force
$h1 = (Get-FileHash $src  -Algorithm MD5).Hash
$h2 = (Get-FileHash $dest -Algorithm MD5).Hash
if ($h1 -eq $h2) { Write-Host "OK LOCAL = PROD" } else { Write-Host "ERREUR MD5" }
```

### Step 6 - Summary

```
UPDATE_ARBO - [date]
LOCAL docs/ : NNN fichiers (02_dash: NN / 03_auto: NN / config_yaml: NN / skills: NN)
PROD H:\docs/ : NNN fichiers
GitHub : NNN objets / docs/ NNN / commit XXXXXXXX
Fichier LOCAL = PROD : OK
```

## Rules

1. **Real counts only** - never an estimated or remembered value.
2. **Re-edit only the lines that changed** - no full rewrite of the file.
3. **Use strict .Replace()** - no regex (problems with special characters).
4. **Push to H:\docs after every modification** - the two files must be identical.
5. **secrets.yaml -> strictly forbidden**.
6. **Do not modify the narrative sections** (REGLES DE CASSE, AUDIT, GITHUB URL patterns) unless explicitly asked.
7. **"resync tree" said by Eric = update of IA_ARBO_DETAIL.md by this skill** (observed on 2026-10-18), not a GitHub -> local copy.

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_update_arbo/update_arbo.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/update-arbo/SKILL.md` must stay identical to this copy.
