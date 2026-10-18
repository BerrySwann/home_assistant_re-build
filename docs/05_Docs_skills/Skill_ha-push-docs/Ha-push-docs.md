---
name: "ha-push-docs"
description: "Skill HA ReBuild - synchronise les fichiers de documentation locaux (*.md + *.yaml dashboard) vers la prod H:\\Docs (Samba HA). Declencher sur : \"pousse les docs en prod\", \"sync docs\", \"met a jour H:\\Docs\", \"nettoie les anciens yaml Dashboard\", \"vire les vieux yaml\"."
---

# HA Push Docs - Local -> H:\Docs (*.md + *.yaml dashboard)

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18).

Synchronise la documentation locale vers `H:\Docs\` : fichiers `*.md` ET `*.yaml` dashboard.
Pousse uniquement les fichiers dont le MD5 differe de la prod.

> Pour les *.md seuls -> /ha_push_md. Pour les yaml config HA -> /ha_push_yaml.

## CHEMINS DE REFERENCE

**Base projet (Windows)** : `C:\Users\Berry Swann\Documents\ReBuild\`

| Source locale | Destination prod | Type |
|:---|:---|:---|
| `docs\02_docs_dashboard\dashboard_docs_MD\` | `H:\Docs\` | *.md |
| `docs\03_docs_automations\docs_automations_MD\` | `H:\Docs\` | *.md |
| `docs\04_docs_scripts\docs_scripts_YAML_MD\` | `H:\Docs\` | *.md |
| `docs\04_docs_scripts\docs_scripts_SH_MD\` | `H:\Docs\` | *.md |
| `docs\02_docs_dashboard\dashboard_docs_YAML\` | `H:\Docs\Dashboard\` | *.yaml dashboard |

> Utiliser `mcp__Windows-MCP__PowerShell` pour H:\ (Samba). secrets.yaml interdit absolu.

## WORKFLOW

### 1 - MD5 local de tous les fichiers (*.md + *.yaml dashboard)
```powershell
$base = "C:\Users\Berry Swann\Documents\ReBuild"
$localMd5 = @{}

# *.md
@("$base\docs\02_docs_dashboard\dashboard_docs_MD",
  "$base\docs\03_docs_automations\docs_automations_MD",
  "$base\docs\04_docs_scripts\docs_scripts_YAML_MD",
  "$base\docs\04_docs_scripts\docs_scripts_SH_MD") | ForEach-Object {
  $srcRoot = $_
  if (Test-Path $srcRoot) {
    Get-ChildItem $srcRoot -Recurse -Filter "*.md" | ForEach-Object {
      $rel = "md|" + $_.FullName.Replace($srcRoot + "\", "")
      $localMd5[$rel] = @{ Path=$_.FullName; Hash=(Get-FileHash $_.FullName -Algorithm MD5).Hash }
    }
  }
}

# *.yaml dashboard (plus recent par type uniquement)
$yamlSrc = "$base\docs\02_docs_dashboard\dashboard_docs_YAML"
Get-ChildItem $yamlSrc -Directory | Where-Object { $_.Name -ne 'Dashboard_COMPLET' } | ForEach-Object {
  $subDir = $_.Name
  Get-ChildItem $_.FullName -Filter "*.yaml" |
    Group-Object { $_.Name -replace '_\d{4}[-_]\d{2}[-_]\d{2}\.yaml$', '' } |
    ForEach-Object {
      $latest = $_.Group | Sort-Object Name | Select-Object -Last 1
      $rel = "yaml|$subDir\$($latest.Name)"
      $localMd5[$rel] = @{ Path=$latest.FullName; Hash=(Get-FileHash $latest.FullName -Algorithm MD5).Hash }
    }
}
Write-Host "Local : $($localMd5.Count) fichiers indexes"
```

### 2 - MD5 prod (H:\Docs)
```powershell
$prodMd5 = @{}
Get-ChildItem "H:\Docs" -Recurse -Filter "*.md" | ForEach-Object {
  $rel = "md|" + $_.FullName.Replace("H:\Docs\", "")
  $prodMd5[$rel] = (Get-FileHash $_.FullName -Algorithm MD5).Hash
}
Get-ChildItem "H:\Docs\Dashboard" -Recurse -Filter "*.yaml" -ErrorAction SilentlyContinue | ForEach-Object {
  $rel = "yaml|" + $_.FullName.Replace("H:\Docs\Dashboard\", "")
  $prodMd5[$rel] = (Get-FileHash $_.FullName -Algorithm MD5).Hash
}
Write-Host "Prod  : $($prodMd5.Count) fichiers indexes"
```

### 3 - Calcul du diff
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

Si `$toPush.Count -eq 0` -> "Tout est a jour - rien a pousser." et arreter.

### 3B - Mise a jour des .md des yaml dashboard modifies (obligatoire, regle CLAUDE.md du 2026-10-13)

Pour chaque `*.yaml` dashboard present dans `$toPush` (vignette, page, carte) : mettre a jour sa fiche `.md` en LOCAL, AVANT de pousser.

1. Trouver la fiche dans `docs\02_docs_dashboard\GLOBAL_INDEX_VIGNETTES_PAGES.md` (colonnes Fiche vignette, Fiche page, Autres fichiers) a partir du code (L1C1...) ou du nom du yaml. Fiche introuvable : le signaler, ne pas en inventer.
2. Sauvegarde locale de la fiche (regle 7), puis ne modifier que les lignes concernees (date, entites, comportement). Jamais de reecriture complete.
3. Si le yaml change les entites ou dependances d'une vignette : mettre aussi a jour `DEPENDANCES_GLOBALES.md` (regle 6).
4. Fichier ajoute, renomme ou supprime : mettre a jour `GLOBAL_INDEX_REPO.md` (regle 10).
5. Relancer les etapes 1 a 3 pour les `*.md` afin que les fiches mises a jour partent dans le meme push.
6. Rien a modifier : le dire dans le rapport avec la raison (jamais silencieux).
### 4 - Push uniquement les fichiers differents
```powershell
$toPush | ForEach-Object {
  if ($_.Key.StartsWith("md|")) {
    $rel  = $_.Key.Replace("md|", "")
    $dest = "H:\Docs\$rel"
  } else {
    $rel  = $_.Key.Replace("yaml|", "")
    $dest = "H:\Docs\Dashboard\$rel"
  }
  $destDir = Split-Path $dest
  New-Item -ItemType Directory -Path $destDir -Force | Out-Null
  Copy-Item $_.Path $dest -Force
  Write-Host "Pousse ($($_.Raison)) : $($_.Key)"
}
```

### 5 - Nettoyage doublons Dashboard (si demande) - JAMAIS dans Dashboard_COMPLET (regle 9)
Supprimer les anciennes versions de yaml dashboard en prod. **Dry-run + confirmation obligatoire avant suppression.** Attention : la suppression se fait sur H:\Docs, il n'y a pas de corbeille sur H: (suppression definitive). Les sauvegardes locales ne sont pas concernees (voir regle 7 ci-dessous).

```powershell
# DRY-RUN
Get-ChildItem "H:\Docs\Dashboard" -Recurse -Filter "*.yaml" |
  Where-Object { $_.FullName -notmatch '\\Dashboard_COMPLET\\' } |
  Group-Object { $_.DirectoryName + "\" + ($_.Name -replace '_\d{4}[-_]\d{2}[-_]\d{2}\.yaml$', '') } |
  Where-Object { $_.Count -gt 1 } |
  ForEach-Object {
    $_.Group | Sort-Object Name | Select-Object -SkipLast 1 |
      ForEach-Object { Write-Host "[DRY-RUN] A supprimer : $($_.FullName)" }
  }
```

### 6 - Verification MD5 finale sur les fichiers pousses
```powershell
$toPush | ForEach-Object {
  $dest = if ($_.Key.StartsWith("md|")) { "H:\Docs\" + $_.Key.Replace("md|","") }
          else { "H:\Docs\Dashboard\" + $_.Key.Replace("yaml|","") }
  $h1 = (Get-FileHash $_.Path -Algorithm MD5).Hash
  $h2 = (Get-FileHash $dest -Algorithm MD5).Hash
  if ($h1 -eq $h2) { Write-Host "OK   $($_.Key)" } else { Write-Host "DIFF $($_.Key)" }
}
```

### 5B - Cas particulier : GLOBAL_INDEX_REPO.md et README.md (2 destinations, decide par Eric le 2026-10-13, emplacements mis a jour le 2026-10-18)

Un seul fichier source, DEUX destinations en prod :

| Source locale | Destination 1 (miroir docs) | Destination 2 (racine, liens cliquables sur GitHub) |
|:---|:---|:---|
| `docs\01_docs_config_system\config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` | `H:\docs\01_docs_config_system\config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` | `H:\GLOBAL_INDEX_REPO.md` |
| `docs\01_docs_config_system\config_system_MD\README\README.md` | `H:\docs\01_docs_config_system\config_system_MD\README\README.md` | `H:\README.md` |

- Les destinations sont calculees a la main : ces fichiers ne sont PAS dans les 5 sources du tableau du haut (qui ecrivent dans H:\Docs\ a plat), ne pas les melanger au calcul de ces sources.
- MD5 de la source comparee a CHAQUE destination separement. Pousser seulement celles qui different. Afficher les deux lignes dans le diff (NOUVEAU / DIFF / identique).
- Verification MD5 finale sur les deux destinations (source = destination 1 = destination 2).
- Les sauvegardes `GLOBAL_INDEX_REPO.bak_...` et `README.bak_...` restent locales (regle 8).
- GitHub : jamais de push direct. Le depot recoit les fichiers via la sauvegarde HA (script ha_git_backup.sh), pas via ce skill.
- `Github\README.md` n'est plus l'original depuis le 2026-10-18 (decision d'Eric) : ne plus le pousser.
- /histo met a jour la copie de travail locale mais ne la pousse pas : c'est ce skill qui pousse.

## REGLES

1. **MD5 d'abord, push uniquement les fichiers differents** - jamais d'ecrasement en masse.
2. **Afficher le diff avant de pousser.**
3. **secrets.yaml -> interdit absolu.**
4. **Local = verite absolue** : en cas de conflit, le local l'emporte.
5. **Dry-run obligatoire** avant toute suppression de doublons Dashboard.
6. **DEPENDANCES_GLOBALES.md** toujours inclus s'il figure dans le diff.
7. **Jamais de sauvegarde creee sur H: ni sur D:** (regle du 2026-10-08). Avant de modifier un fichier de documentation, on le modifie en LOCAL apres en avoir fait une copie a cote de lui, `fichier.ext.bak_AAAA_MM_JJ_HHhMMmSSs` (10 max le jour meme, 3 `.bak_AAAA_MM_JJ` max pour les jours precedents, menage fait par /histo, suppressions vers la corbeille Windows). Voir CLAUDE.md, section REGLE DE SAUVEGARDE.
8. **Les sauvegardes locales ne sont jamais poussees** : les fichiers `*.bak_...` ne sont pas pris par les filtres `*.md` / `*.yaml`. Si un fichier `.md` au nom date (`_AAAA-MM-JJ_HHhmm.md` ou `_AAAA-MM-JJ.md`) ou un dossier `_ARCHIVE` apparait dans le diff, c'est une sauvegarde ou une archive locale : ne pas le pousser et le signaler.
9. **Dashboard_COMPLET : ne jamais y toucher** (decide par Eric le 2026-10-11). Ce dossier contient les mises a jour au fil de l'eau du dashboard complet, il ne se vide jamais. Ce skill l'exclut du calcul MD5/push (etape 1) et du nettoyage de doublons (etape 5) : aucune copie, aucune suppression, aucun renommage, en local comme en prod. Meme si la demande dit "vire les vieux yaml" ou "nettoie les anciens yaml Dashboard", ce dossier est ignore et signale. Le seul circuit qui s'en occupe est l'etape 5B de /histo.
10. **GLOBAL_INDEX_REPO.md et README.md : toujours pousses aux DEUX endroits** (miroir `H:\docs\01_docs_config_system\config_system_MD\...` ET racine `H:\`), MD5 verifie sur chacun (voir etape 5B). Jamais un seul des deux.
11. **Chaque push met a jour le `.md` des fichiers pousses** (regle CLAUDE.md du 2026-10-13) : pas de push de yaml dashboard sans la mise a jour de sa fiche (etape 3B). Le local est modifie en premier, jamais la prod.
12. **Controle apres push** (decide le 2026-10-18) : lancer `Verif_emplacements.py` (lecture seule) ; GLOBAL_INDEX_REPO et README doivent sortir SYNC ou GITHUB EN ATTENTE DU BACKUP.