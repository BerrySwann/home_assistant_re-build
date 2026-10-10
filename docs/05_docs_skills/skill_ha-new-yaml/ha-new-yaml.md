---
name: ha-new-yaml
description: >
  Skill HA ReBuild - genere un squelette YAML conforme aux conventions du projet
  (bordures ASCII, headers obligatoires, slug tertiaire, name/unique_id).
  Declencher sur : "cree un nouveau fichier YAML", "nouveau sensor/template/utility_meter",
  "squelette YAML", "nouveau fichier P0/P1/P2/P3", "cree le fichier [nom]".
---

# HA New YAML - Generation de Squelette Conforme

Genere un fichier YAML vide mais entierement conforme aux conventions du projet HA ReBuild :
bordures ASCII, headers obligatoires, slug tertiaire, name/unique_id coherents.

> Scope : sensors/, templates/, utility_meter/, command_line/. Jamais les automations.

---

## QUESTIONS A POSER AVANT DE GENERER

1. **Pole** : P0 Energie / P1 Chauffage / P2 Prises / P3 Eclairage / P4 Presence / M Meteo / A Air / S Stores / MP Mini-PC ?
2. **Type de fichier** : sensor / template / utility_meter / command_line ?
3. **Piece** (si applicable) : Entree / Cellier / Toilette / Salon / Cuisine / Couloir / Bureau / SDB / Chambre ?
4. **Nom fonctionnel** : que fait ce fichier en une phrase ?
5. **Entite(s) source(s)** : quel capteur brut ou entite HA alimente ce fichier ?
6. **Aval** : quel fichier ou vignette consomme les entites produites ?

---

## REGLES DE CONFORMITE

### Bordure titre principal - coins arrondis, 78 caracteres
Utiliser les vrais caracteres Unicode : coins arrondis (U+256D/256E/256F/2570), barres (U+2500/2502).
- Si titre > 74 car. -> elargir la boite, ne pas tronquer.
- Toujours en MAJUSCULES.

### Bordure titre secondaire - coins carres, 37 caracteres
Utiliser les vrais caracteres Unicode : coins carres (U+250C/2510/2514/2518), barres (U+2500/2502).
- Un par groupe logique d'entites. Numerotation 1 a 9.

### Headers en-tete obligatoires (juste sous la boite principale)
```yaml
# ## DESCRIPTION :
# ## CALCUL & SOURCES :
# ## CHAINE DE DEPENDANCES :
#   | MATERIEL | CAPTEUR BRUT (source) | CE FICHIER (unique_id) | AVAL |
# ## IMPORTANT (PIEGES) :
# ## TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
```

### Slug tertiaire
```yaml
# --- unique_id_exact_de_l_entite ---
```

### name / unique_id
- `name` : majuscules initiales + prefixe pole. Ex: `"Radiateur Cuisine Energie Quotidien"`
- `unique_id` : minuscules + underscores. Ex: `radiateur_cuisine_energie_quotidien`
- Coherence croisee obligatoire.

---

## EMPLACEMENT DU FICHIER GENERE

| Type | Chemin Windows |
|:-----|:---------------|
| sensor | `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\sensors\P{N}_{domaine}\` |
| template | `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\templates\P{N}_{domaine}\` |
| utility_meter | `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\utility_meter\P{N}_{domaine}\` |
| command_line | `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\command_line\` |

Nommage : `P{N}_TYPE_NOM_AMHQ.yaml` si multi-cycles, sinon `P{N}_TYPE_NOM.yaml`.

Apres generation, proposer `/sync_index`.
