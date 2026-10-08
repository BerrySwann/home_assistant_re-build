---
name: sync-index
description: >
  Skill HA ReBuild - met a jour DEPENDANCES_GLOBALES.md et l'index du projet apres validation
  d'un fichier YAML. Declencher OBLIGATOIREMENT quand l'utilisateur tape /sync_index, dit
  "met a jour l'index", "synchronise les dependances", "update DEPENDANCES_GLOBALES",
  apres avoir valide ou corrige un fichier YAML config, automation ou script, ou quand une
  entite modifiee impacte une vignette du dashboard. S'active aussi sur : "le fichier est
  valide", "c'est bon pour ce fichier", ou toute confirmation qu'un YAML vient d'etre
  corrige/approuve.
---

# Skill : /sync_index - Mise a jour de l'index et des dependances

## Objectif

Apres validation d'un fichier YAML (config, automation ou script), mettre a jour la
documentation de dependances pour maintenir la coherence du projet.

## Perimetre

| Type de fichier valide | Dossier source |
|:---|:---|
| Config HA (sensors, templates, utility_meter...) | `docs/` |
| Automation | `docs/03_docs_automations/docs_automations_YAML/` |
| Script | `docs/04_docs_scripts/docs_scripts_YAML/` |

## Fichiers a mettre a jour selon le type

| Type valide | Fichier index a mettre a jour |
|:---|:---|
| Config YAML | `docs/02_docs_dashboard/dashboard_docs_MD/DEPENDANCES_GLOBALES.md` |
| Automation | `docs/03_docs_automations/docs_automations_MD/{nom_automation}.md` + index automations si existant |
| Script | `docs/04_docs_scripts/docs_scripts_YAML_MD/{nom_script}.md` |
| Tout type impactant une vignette | `DEPENDANCES_GLOBALES.md` |

**Chemins Windows :**
- `C:\Users\Berry Swann\Documents\ReBuild\docs\02_docs_dashboard\dashboard_docs_MD\DEPENDANCES_GLOBALES.md`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\03_docs_automations\docs_automations_MD\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_YAML_MD\`

## Protocole d'execution

### 1. Identifier le type et les entites impactees

Determiner :
- **Type** : config YAML / automation / script
- **unique_id** ou alias de l'entite/automation/script
- **Fichier source** (chemin dans le bon dossier)
- **Vignette(s) concernee(s)** (L1C1 a L6C3) si applicable

### 2. Mettre a jour DEPENDANCES_GLOBALES.md (si config ou vignette impactee)

Lire le fichier, reperer les lignes concernees, passer les statuts non-valide -> OK.
Completer les colonnes "Fichier source" et "Entite" si vides.
Mettre a jour la date en haut du fichier.

### 3. Mettre a jour la doc automation (si automation validee)

Verifier si un fichier `.md` existe dans `docs/03_docs_automations/docs_automations_MD/` pour cette automation.
- Si oui : mettre a jour la section "Etat" ou "Derniere validation".
- Si non : signaler qu'il manque une doc et proposer de la creer.

### 4. Mettre a jour la doc script (si script valide)

Verifier si un fichier `.md` existe dans `docs/04_docs_scripts/docs_scripts_YAML_MD/` pour ce script.
- Si oui : mettre a jour la section "Etat".
- Si non : signaler qu'il manque une doc et proposer de la creer.

### 5. Format de reponse

```
SYNC_INDEX - [date du jour]

Type valide : [config YAML / automation / script]
Fichier     : [chemin court]
Entite/alias: [unique_id ou alias]
Vignette    : [L*C* ou N/A]

Mises a jour :
- DEPENDANCES_GLOBALES.md : [ligne] -> OK  (si applicable)
- docs_automations_MD/{nom}.md : [section mise a jour]  (si automation)
- docs_scripts_YAML_MD/{nom}.md : [section mise a jour]  (si script)
```

### 6. Si un fichier index est absent ou incomplet

Signaler : `>> {fichier} introuvable ou incomplet - verifier le chemin`
Proposer de creer/completer la section manquante.

## Regles

- **Ne reecrire que les lignes concernees** - pas le fichier complet (economie tokens).
- Si aucune dependance n'est impactee : repondre "Index deja a jour - aucune action" (1 ligne).
