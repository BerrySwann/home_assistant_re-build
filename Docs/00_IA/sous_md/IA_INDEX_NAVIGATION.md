# IA_INDEX_NAVIGATION.md — Contexte & Compétence INDEX NAVIGATION

*Créé le : 2026-05-30*

---

## Ce que c'est

Fichier local : `ReBuild/INDEX_NAVIGATION_FULL.md`
Fichier GitHub : `INDEX_NAVIGATION.md` (racine du repo `home_assistant_re-build`)
Taille : ~2655 lignes

Index de navigation complet des 18 vignettes du dashboard HA.
Structure en accordéon HTML (`<details>`/`<summary>`) à 3 niveaux, rendu natif sur GitHub.

---

## Structure par vignette (L*C*)

```
Niveau 1 : L*C* — LABEL | X page(s) | ~N entités        ← rétracté par défaut
  Niveau 2a : 🖼️ Vignette
    → Doc vignette (lien Docs/docs_dashboard/docs/L*C*_NOM/)
    → YAML vignette (lien Docs/Dashboard/L*C*_XX_Nom/)
    → Fichiers sources TREE_CORRIGE (par fichier, entités listées)
  Niveau 2b : 📄 Page(s)
    → Doc page + YAML page
    → Fichiers sources TREE_CORRIGE
    → 💬 Pop-up #hash — N entités
        chaque entité : "voir fichier" (lien TREE_CORRIGE) ou "Natif HA"
  Niveau 2c : 📎 Fichiers complémentaires (si présents)
```

---

## Chemins — relatifs racine GitHub

| Type | Chemin |
|:-----|:-------|
| YAMLs dashboard | `Docs/Dashboard/L*C*_XX_Nom/` |
| Docs vignettes | `Docs/docs_dashboard/docs/L*C*_NOM/` |
| Fichiers sources | `Docs/docs_dashboard/TREE_CORRIGE/templates\|sensors\|utility_meter/` |

---

## Comment régénérer le fichier

Le fichier est généré par script Python (session Cowork 2026-05-30).
Les données intermédiaires sont en `/tmp/` (fetched_yaml.pkl, entity_map.pkl) — perdues entre sessions.

**À régénérer après :**
- Ajout ou modification d'une vignette ou page YAML
- Ajout d'un nouveau fichier dans TREE_CORRIGE
- Correction d'un unique_id dans TREE_CORRIGE

**Procédure :**
1. Relancer le fetch des 40 YAMLs dashboard (18 vignettes + pages)
2. Relancer le fetch/scan TREE_CORRIGE local pour le mapping entity → fichier source
3. Régénérer avec le script de parsing (parse_page + render_sources_html + render_popup_html)
4. Sauvegarder dans `ReBuild/INDEX_NAVIGATION_FULL.md`
5. Pusher sur GitHub en remplacement de `INDEX_NAVIGATION.md`

---

## Limites connues

- Entités dans templates Jinja (`states('sensor.xxx')`) **non extraites** par le parser regex
- Entités dans `button-card` JS inline **non extraites**
- Réel nb d'entités ~30-40% supérieur sur pages complexes (L2C1, L1C1)
- **L4C1 Proxmox** : page non pushée sur GitHub, doc vignette à créer
- Le parser pop-up utilise une logique séquentielle (bubble-card flat) : les entités sont assignées au dernier pop-up défini avant elles dans le fichier

---

## Mapping entités → fichiers sources

736 `unique_id` mappés depuis TREE_CORRIGE local au 2026-05-30.
Fichier référence local : `ReBuild/docs_dashboard/TREE_CORRIGE/` (scan complet `.yaml`).
Cas particulier : Mini-PC supprimé — sensors proxmox_* via MQTT natif directement (pas de fichier YAML dans templates/).
