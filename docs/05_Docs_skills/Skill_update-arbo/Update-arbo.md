---
name: "update-arbo"
description: "Skill HA ReBuild - met a jour IA_ARBO_DETAIL.md (comptages LOCAL + PROD + GitHub) apres toute session qui ajoute, supprime ou deplace des fichiers. Declencher quand l'utilisateur tape /update-arbo ou apres un resync, push ou purge qui change les comptages."
---

# Skill : /update-arbo - Mise a jour IA_ARBO_DETAIL.md

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18).

## Objectif

Rafraichir les comptages et les informations de version dans `IA_ARBO_DETAIL.md`
apres chaque session qui modifie le nombre de fichiers.

## Chemins

| Fichier | Chemin |
|:--------|:-------|
| Local   | `C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` |
| Prod    | `H:\docs\00_IA\SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` |

## Protocole d'execution

### Etape 1 - Comptages reels LOCAL (PowerShell)

```powershell
$base = "C:\Users\Berry Swann\Documents\ReBuild"

$docs_total  = (Get-ChildItem "$base\docs" -Recurse -File).Count
$histo_total = (Get-ChildItem "$base\historique" -File).Count
$docs_01     = (Get-ChildItem "$base\docs\01_docs_config_system" -Recurse -File).Count
$cfg_yaml    = (Get-ChildItem "$base\docs\01_docs_config_system\config_system_SH_PY_YAML" -Recurse -File).Count
$cfg_md      = (Get-ChildItem "$base\docs\01_docs_config_system\config_system_MD" -Recurse -File).Count
$docs_02     = (Get-ChildItem "$base\docs\02_docs_dashboard" -Recurse -File).Count
$docs_03     = (Get-ChildItem "$base\docs\03_docs_automations" -Recurse -File).Count
$docs_04     = (Get-ChildItem "$base\docs\04_docs_scripts" -Recurse -File).Count
$docs_05     = (Get-ChildItem "$base\docs\XX_docs_MD_system" -Recurse -File).Count
$dash_complet= (Get-ChildItem "$base\docs\02_docs_dashboard\dashboard_docs_YAML\Dashboard_COMPLET" -Filter "*.yaml").Count

Write-Host "LOCAL docs/ total   : $docs_total"
Write-Host "  historique/       : $histo_total"
Write-Host "  01_docs_config/   : $docs_01 (config_system_SH_PY_YAML : $cfg_yaml ; config_system_MD : $cfg_md)"
Write-Host "  02_docs_dashboard : $docs_02 (Dashboard_COMPLET : $dash_complet yaml)"
Write-Host "  03_docs_automations: $docs_03"
Write-Host "  04_docs_scripts   : $docs_04"
Write-Host "  XX_docs_MD_system : $docs_05"
```

### Etape 2 - Comptages reels PROD H:\docs (PowerShell)

```powershell
$prod_docs = (Get-ChildItem "H:\docs" -Recurse -File).Count
$prod_01   = (Get-ChildItem "H:\docs\01_docs_config_system" -Recurse -File -ErrorAction SilentlyContinue).Count
$prod_02   = (Get-ChildItem "H:\docs\02_docs_dashboard" -Recurse -File).Count
$prod_03   = (Get-ChildItem "H:\docs\03_docs_automations" -Recurse -File).Count
$prod_04   = (Get-ChildItem "H:\docs\04_docs_scripts" -Recurse -File).Count
$prod_05   = (Get-ChildItem "H:\docs\XX_docs_MD_system" -Recurse -File).Count

# Dashboard racine H:\
$dash_racine = Get-ChildItem "H:\" -Filter "Dashboard_*.yaml" | Sort-Object Name | Select-Object -Last 1 -ExpandProperty Name

Write-Host "PROD H:\docs/ total : $prod_docs"
Write-Host "  01_docs_config/   : $prod_01"
Write-Host "  02_docs_dashboard : $prod_02"
Write-Host "  03_docs_automations: $prod_03"
Write-Host "  04_docs_scripts   : $prod_04"
Write-Host "  XX_docs_MD_system : $prod_05"
Write-Host "Dashboard racine H:\ : $dash_racine"
```

### Etape 3 - Dernier commit GitHub (PowerShell)

```powershell
$api = "https://api.github.com/repos/BerrySwann/home_assistant_re-build/commits/main"
$r   = Invoke-RestMethod $api -Headers @{"User-Agent"="PowerShell"}
$tree = Invoke-RestMethod "https://api.github.com/repos/BerrySwann/home_assistant_re-build/git/trees/main?recursive=1" -Headers @{"User-Agent"="PowerShell"}
$gh_total = $tree.tree.Count
$gh_docs  = ($tree.tree | Where-Object { $_.path -like "docs/*" }).Count

Write-Host "GitHub commit : $($r.sha.Substring(0,8)) - $($r.commit.author.date)"
Write-Host "GitHub tree   : $gh_total objets / docs/ : $gh_docs"
```

### Etape 4 - Mettre a jour IA_ARBO_DETAIL.md (PowerShell .Replace)

Lire le fichier, faire les remplacements de chaines exactes (NE PAS utiliser -replace regex
pour eviter les problemes avec les caracteres speciaux). Utiliser :
```powershell
$c = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
$c = $c.Replace("ancien texte", "nouveau texte")
[System.IO.File]::WriteAllText($path, $c, [System.Text.Encoding]::UTF8)
```

Les arbres sont une grille a deux colonnes de largeur fixe : un remplacement qui change la longueur d'une ligne doit retirer ou ajouter autant d'espaces avant la bordure de fin, pour garder toutes les lignes du tableau a la meme largeur (a verifier apres ecriture).

**Sections a mettre a jour systematiquement :**

1. Ligne d'entete `*Derniere mise a jour :` -> date + resume de la session
2. `releve YYYY-MM-DD)` dans le bloc arbo LOCAL -> date du jour
3. `releve YYYY-MM-DD ; = H:\` dans le bloc arbo PROD -> date du jour
4. `docs/ (NNN fichiers` -> nouveau comptage LOCAL
5. `historique/ (NN` -> nouveau comptage
6. `01_docs_config_system/ (NN` dans LOCAL -> nouveau comptage + note (sous-dossiers config_system_MD et config_system_SH_PY_YAML)
7. `02_docs_dashboard/ (NN` dans LOCAL -> nouveau comptage
8. `Dashboard_YYYY_MM-DD.yaml (export le plus recent)` -> nom du dernier dashboard
9. `docs/ (NNN` dans PROD -> nouveau comptage
10. `Dernier releve arbre (API git trees)** : YYYY-MM-DD - **NNN` -> nouveau
11. `dernier commit` hash et date -> nouveau commit
12. `docs/` NNN dans Repartition GitHub -> nouveau comptage

### Etape 5 - Pousser vers H:\docs

```powershell
$src  = "C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md"
$dest = "H:\docs\00_IA\SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md"
Copy-Item $src $dest -Force
$h1 = (Get-FileHash $src  -Algorithm MD5).Hash
$h2 = (Get-FileHash $dest -Algorithm MD5).Hash
if ($h1 -eq $h2) { Write-Host "OK LOCAL = PROD" } else { Write-Host "ERREUR MD5" }
```

### Etape 6 - Resume

```
UPDATE_ARBO - [date]
LOCAL docs/ : NNN fichiers (02_dash: NN / 03_auto: NN / config_yaml: NN)
PROD H:\docs/ : NNN fichiers
GitHub : NNN objets / docs/ NNN / commit XXXXXXXX
Fichier LOCAL = PROD : OK
```

## Regles

1. **Comptages reels uniquement** - jamais de valeur estimee ou memorisee.
2. **Ne reediter que les lignes qui ont change** - pas de reecriture complete du fichier.
3. **Utiliser .Replace() strict** - pas de regex (problemes avec les caracteres speciaux).
4. **Pousser vers H:\docs apres chaque modification** - les deux fichiers doivent etre identiques.
5. **secrets.yaml -> interdit absolu**.
6. **Ne pas modifier les sections narratives** (REGLES DE CASSE, AUDIT, GITHUB patterns URLs) sauf si explicitement demande.
7. **"resync tree" dit par Eric = mise a jour de IA_ARBO_DETAIL.md par ce skill** (constate le 2026-10-18), pas une copie GitHub -> local.