---
name: ha-status
description: >
  Skill HA ReBuild - genere un resume ultra-compact de l'avancement du projet en 3 points.
  Declencher OBLIGATOIREMENT quand l'utilisateur tape /status, demande "ou en est le projet",
  "quel est l'avancement", "resume la situation", "c'est quoi l'etat actuel", "on en est ou",
  ou demande un bilan rapide de ce qui a ete fait / ce qui reste a faire dans le projet HA ReBuild.
  Economie de tokens : evite de relire tout l'historique de la conversation.
---

# Skill : /ha_status - Avancement du projet HA ReBuild

## Objectif

Resumer l'etat du projet en **3 points maximum**, de facon ultra-compacte.
Zero discours, zero repetition de code deja valide.

## Protocole d'execution

### 1. Lire les sources disponibles

Dans l'ordre de priorite :
1. L'historique de la conversation en cours (fichiers mentionnes, validations, erreurs)
2. `docs\02_docs_dashboard\dashboard_docs_MD\DEPENDANCES_GLOBALES.md` (etat des chaines)
3. Fichiers recents dans `docs\01_docs_config_system\config_system_YAML\` (dates de modification)

### 2. Format de reponse obligatoire

```
STATUS - [date du jour]

[1] FAIT    : [liste courte des fichiers/entites valides recemment]
[2] EN COURS : [tache ou fichier actuellement en traitement]
[3] SUIVANT  : [prochaine action prioritaire identifiee]

Blocages : [aucun | description courte si bloquant]
```

### Regles de sobriete

- Maximum 2 lignes par point
- Utiliser les IDs de la matrice (L1C1, P2, etc.) pour referencer vignettes et poles
- Utiliser les noms de fichiers courts (ex: `P1_kWh_clim_chauffage.yaml`)
- Si rien n'a ete fait dans la session : `[1] FAIT : aucune modification validee dans cette session`
- Ne jamais repeter le contenu YAML deja poste dans la conversation
