---
name: "ha-push-docs"
description: "HA ReBuild skill - synchronizes the local documentation files (*.md + dashboard *.yaml) to the prod H:\\docs (HA Samba). Trigger on: \"pousse les docs en prod\", \"sync docs\", \"met a jour H:\\docs\", \"nettoie les anciens yaml Dashboard\", \"vire les vieux yaml\"."
---

# HA Push Docs - Local -> H:\docs (*.md + dashboard *.yaml)

> Files present in several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18).

Synchronizes the local documentation to `H:\docs\`: `*.md` files AND dashboard `*.yaml` files.
Pushes only the files whose MD5 differs from prod.

> For *.md only -> /ha_push_md. For HA config yaml -> /ha_push_yaml.

## REFERENCE PATHS

**Project base (Windows)**: `C:\Users\Berry Swann\Documents\ReBuild\`

| Local source | Prod destination | Type |
|:---|:---|:---|
| `docs\02_docs_dashboard\02_dashboard_docs_MD\` | `H:\docs\02_docs_dashboard\02_dashboard_docs_MD\` | *.md |
| `docs\03_docs_automations\03_docs_automations_MD\` | `H:\docs\03_docs_automations\03_docs_automations_MD\` | *.md |
| `docs\04_docs_scripts\04_docs_scripts_YAML_MD\` | `H:\docs\04_docs_scripts\04_docs_scripts_YAML_MD\` | *.md |
| `docs\04_docs_scripts\04_docs_scripts_SH_MD\` | `H:\docs\04_docs_scripts\04_docs_scripts_SH_MD\` | *.md |
| `docs\02_docs_dashboard\02_dashboard_docs_YAML\` | `H:\docs\02_docs_dashboard\02_dashboard_docs_YAML\` | dashboard *.yaml |

> Prod reproduces the tree of `docs`: prod path = `H:\docs\` + path relative to `docs\` (checked on 2026-10-31: no flat file in `H:\docs`, no `H:\docs\Dashboard` folder).

> Use `mcp__Windows-MCP__PowerShell` for H:\ (Samba). secrets.yaml is strictly forbidden.

## WORKFLOW

### BEFORE ANY PUSH - Check of the XX_ folders (decided by Eric on 2026-10-25 21:19, mandatory)

The `XX_` folders exist only locally and must never be lost. Before the first computation of this skill, AND a second time right after the push (before/after check), run:
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\Check_XX_presents.py"`
It also refuses any XX_ folder present in prod (ALERTE). It compares the XX_ folders and their files with the manifest `XX_manifest.json` (same folder). `RESULTAT : OK` = continue. An ALERTE (missing folder or file) = push NOTHING, warn Eric, restore from `TEMPO\XX_sauvegarde_2026-10-25` only on his order. XX_ folders are never pushed to prod. The manifest is updated (`--maj`) only on Eric's order.

### 1 - Local MD5 of all files (*.md + dashboard *.yaml)
```powershell
$base = "C:\Users\Berry Swann\Documents\ReBuild"
$localMd5 = @{}

# *.md
@("$base\docs\02_docs_dashboard\02_dashboard_docs_MD",
  "$base\docs\03_docs_automations\03_docs_automations_MD",
  "$base\docs\04_docs_scripts\04_docs_scripts_YAML_MD",
  "$base\docs\04_docs_scripts\04_docs_scripts_SH_MD") | ForEach-Object {
  $srcRoot = $_
  if (Test-Path $srcRoot) {
    Get-ChildItem $srcRoot -Recurse -Filter "*.md" | ForEach-Object {
      $rel = "md|" + $_.FullName.Replace("$base\docs\", "")
      $localMd5[$rel] = @{ Path=$_.FullName; Hash=(Get-FileHash $_.FullName -Algorithm MD5).Hash }
    }
  }
}

# dashboard *.yaml (latest per type only)
$yamlSrc = "$base\docs\02_docs_dashboard\02_dashboard_docs_YAML"
Get-ChildItem $yamlSrc -Directory | Where-Object { $_.Name -ne 'Dashboard_COMPLET' } | ForEach-Object {
  $subDir = $_.Name
  Get-ChildItem $_.FullName -Filter "*.yaml" |
    Group-Object { $_.Name -replace '_\d{4}[-_]\d{2}[-_]\d{2}\.yaml$', '' } |
    ForEach-Object {
      $latest = $_.Group | Sort-Object Name | Select-Object -Last 1
      $rel = "yaml|" + $latest.FullName.Replace("$base\docs\", "")
      $localMd5[$rel] = @{ Path=$latest.FullName; Hash=(Get-FileHash $latest.FullName -Algorithm MD5).Hash }
    }
}
Write-Host "Local : $($localMd5.Count) fichiers indexes"
```

### 2 - Prod MD5 (H:\docs)
```powershell
$prodMd5 = @{}
Get-ChildItem "H:\docs" -Recurse -Filter "*.md" | ForEach-Object {
  $rel = "md|" + $_.FullName.Replace("H:\docs\", "")
  $prodMd5[$rel] = (Get-FileHash $_.FullName -Algorithm MD5).Hash
}
Get-ChildItem "H:\docs\02_docs_dashboard\02_dashboard_docs_YAML" -Recurse -Filter "*.yaml" -ErrorAction SilentlyContinue | ForEach-Object {
  $rel = "yaml|" + $_.FullName.Replace("H:\docs\", "")
  $prodMd5[$rel] = (Get-FileHash $_.FullName -Algorithm MD5).Hash
}
Write-Host "Prod  : $($prodMd5.Count) fichiers indexes"
```

### 3 - Diff computation
```powershell
$toPush = @()
$localMd5.Keys | ForEach-Object {
  $raison = if (-not $prodMd5.ContainsKey($_)) { "NOUVEAU" }
             elseif ($localMd5[$_].Hash -ne $prodMd5[$_]) { "DIFF" }
             else { $null }
  if ($raison) {
    $toPush += [PSCustomObject]@{ Key=$_; Raison=$raison; Path=$localMd5[$_].Path }
  }
}
$toPush | Format-Table Key, Raison -AutoSize
Write-Host "$($toPush.Count) fichier(s) a pousser."
```

If `$toPush.Count -eq 0` -> "Tout est a jour - rien a pousser." and stop.

### 3B - Update of the .md of the modified dashboard yaml files (mandatory, CLAUDE.md rule of 2026-10-13)

For each dashboard `*.yaml` present in `$toPush` (tile, page, card): update its `.md` sheet LOCALLY, BEFORE pushing.

1. Find the sheet in `docs\02_docs_dashboard\GLOBAL_INDEX_VIGNETTES_PAGES.md` (columns Fiche vignette, Fiche page, Autres fichiers) from the code (L1C1...) or the yaml name. Sheet not found: report it, do not invent one.
2. Local backup of the sheet (rule 7), then modify only the lines concerned (date, entities, behavior). Never a full rewrite.
3. If the yaml changes the entities or dependencies of a tile: also update `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` (rule 6).
4. File added, renamed or deleted: update `GLOBAL_INDEX_REPO.md` (rule 10).
5. Re-run steps 1 to 3 for the `*.md` so that the updated sheets leave in the same push.
6. Nothing to modify: say so in the report with the reason (never silent).

### 4 - Push only the different files
```powershell
$toPush | ForEach-Object {
  $rel  = $_.Key.Substring($_.Key.IndexOf("|") + 1)
  $dest = "H:\docs\$rel"
  $destDir = Split-Path $dest
  New-Item -ItemType Directory -Path $destDir -Force | Out-Null
  Copy-Item $_.Path $dest -Force
  Write-Host "Pousse ($($_.Raison)) : $($_.Key)"
}
```

### 5 - Cleanup of Dashboard duplicates (if requested) - NEVER in Dashboard_COMPLET (rule 9)
Delete the old versions of dashboard yaml in prod. **Dry-run + confirmation mandatory before deletion.** Warning: the deletion happens on H:\docs, there is no recycle bin on H:, so never a direct deletion: each file to delete is first copied to `TEMPO\<operation>_AAAA-MM-JJ\` (same tree), the MD5 of the copy is verified, then it is deleted on H: ; report in the modifications journal (TEMPO rule of CLAUDE.md of 2026-10-18). Local backups are not concerned (see rule 7 below).

```powershell
# DRY-RUN
Get-ChildItem "H:\docs\02_docs_dashboard\02_dashboard_docs_YAML" -Recurse -Filter "*.yaml" |
  Where-Object { $_.FullName -notmatch '\\Dashboard_COMPLET\\' } |
  Group-Object { $_.DirectoryName + "\" + ($_.Name -replace '_\d{4}[-_]\d{2}[-_]\d{2}\.yaml$', '') } |
  Where-Object { $_.Count -gt 1 } |
  ForEach-Object {
    $_.Group | Sort-Object Name | Select-Object -SkipLast 1 |
      ForEach-Object { Write-Host "[DRY-RUN] A supprimer : $($_.FullName)" }
  }
```

### 6 - Final MD5 verification on the pushed files
```powershell
$toPush | ForEach-Object {
  $dest = "H:\docs\" + $_.Key.Substring($_.Key.IndexOf("|") + 1)
  $h1 = (Get-FileHash $_.Path -Algorithm MD5).Hash
  $h2 = (Get-FileHash $dest -Algorithm MD5).Hash
  if ($h1 -eq $h2) { Write-Host "OK   $($_.Key)" } else { Write-Host "DIFF $($_.Key)" }
}
```

### 5B - Special case: GLOBAL_INDEX_REPO.md and README.md (2 destinations, decided by Eric on 2026-10-13, locations updated on 2026-10-18)

A single source file, TWO destinations in prod:

| Local source | Destination 1 (docs mirror) | Destination 2 (root, clickable links on GitHub) |
|:---|:---|:---|
| `docs\01_docs_config_system\01_config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` | `H:\docs\01_docs_config_system\01_config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` | `H:\GLOBAL_INDEX_REPO.md` |
| `docs\01_docs_config_system\01_config_system_MD\README\README.md` | `H:\docs\01_docs_config_system\01_config_system_MD\README\README.md` | `H:\README.md` |

- The destinations are computed by hand: these files are NOT in the 5 sources of the table at the top (whose computation is described above), do not mix them with the computation of those sources.
- MD5 of the source compared to EACH destination separately. Push only those that differ. Show both lines in the diff (NOUVEAU / DIFF / identique).
- Final MD5 verification on both destinations (source = destination 1 = destination 2).
- The backups `GLOBAL_INDEX_REPO.bak_...` and `README.bak_...` stay local (rule 8).
- GitHub: never a direct push. The repository receives the files through the HA backup (script ha_git_backup.sh), not through this skill.
- `Github\README.md` is no longer the original since 2026-10-18 (Eric's decision): do not push it anymore.
- /histo updates the local working copy and, since 2026-10-30, also pushes all of `docs` to prod (step 5C, except `XX_` and `.bak`). Whatever /histo does, this skill remains the one that guarantees the TWO destinations of these two files (rule 10).

## RULES

1. **MD5 first, push only the different files** - never a mass overwrite.
2. **Show the diff before pushing.**
3. **secrets.yaml -> strictly forbidden.**
4. **Local = absolute truth**: in case of conflict, local wins.
5. **Dry-run mandatory** before any deletion of Dashboard duplicates.
6. **DEPENDANCES_GLOBALES_CLAUDE_memoire.md** (`docs\00_IA\00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire\`): since 2026-10-30 it goes to prod with the general push of /histo (step 5C, all of `docs` except `XX_` and `.bak`), which replaces the 2026-10-25 decision that kept it local only. It is not in the 5 sources of this skill: update its date and lines locally, /histo pushes it.
7. **Never create a backup on H: nor on D:** (rule of 2026-10-08). Before modifying a documentation file, modify it LOCALLY after making a copy next to it, `fichier.ext.bak_AAAA_MM_JJ_HHhMMmSSs` (10 max on the same day, 3 `.bak_AAAA_MM_JJ` max for previous days, cleanup done by /histo, deletions to the Windows recycle bin). See CLAUDE.md, section REGLE DE SAUVEGARDE.
8. **Local backups are never pushed**: the `*.bak_...` files are not picked by the `*.md` / `*.yaml` filters. If a `.md` file with a dated name (`_AAAA-MM-JJ_HHhmm.md` or `_AAAA-MM-JJ.md`) or an `_ARCHIVE` folder shows up in the diff, it is a local backup or archive: do not push it and report it.
9. **Dashboard_COMPLET: never touch it** (decided by Eric on 2026-10-11). This folder holds the running updates of the complete dashboard, it is never emptied. This skill excludes it from the MD5/push computation (step 1) and from the duplicate cleanup (step 5): no copy, no deletion, no rename, locally as in prod. Even if the request says "vire les vieux yaml" or "nettoie les anciens yaml Dashboard", this folder is ignored and reported. The only circuit that handles it is step 5B of /histo.
10. **GLOBAL_INDEX_REPO.md and README.md: always pushed to BOTH places** (mirror `H:\docs\01_docs_config_system\01_config_system_MD\...` AND root `H:\`), MD5 verified on each (see step 5B). Never only one of the two.
11. **Every push updates the `.md` of the pushed files** (CLAUDE.md rule of 2026-10-13): no push of a dashboard yaml without the update of its sheet (step 3B). Local is modified first, never prod.
12. **Check after push** (decided on 2026-10-18): run `Verif_emplacements.py` (read-only); GLOBAL_INDEX_REPO and README must come out SYNC or GITHUB EN ATTENTE DU BACKUP.

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_push_docs/ha_push_docs.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-push-docs/SKILL.md` must stay identical to this copy.
