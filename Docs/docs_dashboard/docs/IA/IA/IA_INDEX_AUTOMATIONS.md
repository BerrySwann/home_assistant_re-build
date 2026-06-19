# IA_INDEX_AUTOMATIONS.md — Contexte & Compétence INDEX AUTOMATIONS

*Créé le : 2026-05-30*

---

## Ce que c'est

Fichier : `docs_automations/docs/INDEX_AUTOMATIONS.md`
Taille : ~980 lignes

Index de navigation complet des 48 automations HA, organisées en 10 catégories.
Structure en accordéon HTML (`<details>`/`<summary>`) à 2 niveaux, rendu natif sur GitHub.

---

## Structure

```
Niveau 1 : Catégorie (nb automations | description)
  Niveau 2 : ✅/⚠️ Alias automation
    → Doc + YAML TREE_CORRIGE
    → Déclencheurs (trigger types)
    → Entités (accordéon)
    → Notifications (accordéon)
```

---

## Catégories (10)

| Catégorie | Nb | Dossier TREE_CORRIGE |
|:----------|:---|:---------------------|
| 🔧 Backup Git | 7 | `backup/` |
| 🌤️ Météo | 5 | `meteo/` |
| 🌡️ P1 Clim & Chauffage | 11 | `P1_clim_chauffage/` |
| 🍳 P1 Cuisine | 2 | `P1_cuisine/` |
| 🚿 P1 Salle de Bain | 3 | `P1_sdb/` |
| 🔌 P2 Prises | 3 | `P2_prises/` |
| 💡 P3 Éclairage | 8 | `P3_eclairage/` |
| 🏠 Stores | 2 | `stores/` |
| ⚡ Énergie | 2 | `energie/` |
| 🖥️ Système | 6 | `systeme/` |
| 🍓 Raspberry Pi4 (archivé) | 1 | `raspi/` |

---

## Anomalies connues (2026-05-30)

- `P2_prises/eco_prises.yaml` → ancienne version — à archiver `old/`
- `P2_prises/bureau_allumage_pc.yaml` → supprimée de HA — à archiver
- `P2_prises/rodret_soufflant_sdb.yaml` → supprimée de HA — à archiver
- `P2_prises/rodret_tv_chambre.yaml` → supprimée de HA — à archiver
- `P2_bouton_rodret_soufflant_sdb.yaml` → mal placé à la racine
- `systeme/diag_enregistrement_journalier.yaml` → **absent de GitHub — vérifier dans HA live**

---

## Comment régénérer

1. Fetcher `automations.yaml` depuis GitHub raw
2. Parser les 48 automations top-level par `alias:`
3. Reconstruire le mapping CATEGORIES (catégorie → liste alias + doc + tree_rel)
4. Régénérer avec `render_automation_html()`
5. Sauvegarder dans `docs_automations/docs/INDEX_AUTOMATIONS.md`

**À régénérer après :**
- Ajout / suppression / renommage d'une automation dans HA
- Création d'un nouveau fichier dans TREE_CORRIGE
- Modification d'une catégorie

---

## Docs automations

14 docs créées le 2026-05-30 (nouvelles automations non documentées).
Toutes les docs sont dans `docs_automations/docs/[CATEGORIE]/NOM.md`.
Contenu minimal généré — descriptions à compléter manuellement.
