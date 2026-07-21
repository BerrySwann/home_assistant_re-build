# IA_INDEX_AUTOMATIONS.md — Contexte & Competence INDEX AUTOMATIONS

*Refait le : 2026-07-21 (ancien fichier 2026-05-30 obsolete — TREE_CORRIGE + INDEX_AUTOMATIONS.md supprimes)*

---

## Ce que c'est

Les automations sont indexees dans la section `03-AUTOMATIONS` de :
- **Index principal** : `H:\Docs\INDEX_GLOBAL.md` (source de verite, rendu GitHub)
- **Copie locale** : `ReBuild/Github/INDEX_GLOBAL.md`

Il n'y a plus de fichier `INDEX_AUTOMATIONS.md` distinct — fusionne dans INDEX_GLOBAL.md (2026-07-16).

---

## Arborescence locale des automations

```
DOCS/03_docs_automations/
- docs_automations_YAML/     <- YAML individuels par automation (reference locale)
    P1_clim_chauffage/
    P1_cuisine/
    P1_sdb/
    P2_prises/
    P3_eclairage/
    backup/
    meteo/
    stores/
    energie/
    systeme/
    raspi/
- docs_automations_MD/       <- Docs texte par automation
```

> ⚠️ Ne jamais modifier `automations.yaml` directement.
> Tout changement passe par l'UI HA, en s'appuyant sur les fichiers `docs_automations_YAML/`.

---

## Comptage (verifie 2026-07-19)

**48 automations** dans `automations.yaml` prod.

| Categories | Nb reel |
|:-----------|:--------|
| Backup Git | 2 |
| Meteo | 5 |
| P1 Clim & Chauffage | 10 |
| P1 Cuisine | 2 |
| P1 Salle de Bain | 3 |
| P2 Prises | 3 |
| P3 Eclairage | 7 |
| Stores | 2 |
| Energie | 2 |
| Systeme | 6 |
| Raspberry Pi4 (archive) | 1 |

> Comptages verifies programmatiquement (audit 2026-07-19).
> "P1 Clim & Chauffage (11)" et "P3 Eclairage (8)" etaient faux dans INDEX_GLOBAL.md — corriges.

---

## Structure de l'index (section 03-AUTOMATIONS dans INDEX_GLOBAL.md)

```
Niveau 1 : Categorie (nb automations | description)
  Niveau 2 : Alias automation
    - Lien doc .md
    - Lien YAML docs_automations_YAML/
    - Declencheurs (trigger types)
    - Entites
    - Notifications
```

Structure accordeon HTML (`<details>`/`<summary>`) a 2 niveaux, rendu natif sur GitHub.

---

## Anomalies connues / ouvertes

- `P1-CUISINE-B` : correctif deploye en local (`b_chauffage_cuisine_vacances.yaml`),
  **PAS encore applique dans HA** — Eric doit le faire via UI HA (voir TODO.txt P1-CUISINE-B).

---

## Comment mettre a jour l'index

Apres ajout/suppression/renommage d'une automation dans HA :

1. Fetcher `automations.yaml` depuis GitHub (raw) ou lire `H:\automations.yaml`
2. Identifier l'alias concerne
3. Mettre a jour la section 03-AUTOMATIONS de `INDEX_GLOBAL.md`
4. Mettre a jour le compteur de la categorie dans le TOC
5. Creer/archiver le fichier YAML correspondant dans `docs_automations_YAML/`
6. Push `H:\Docs\INDEX_GLOBAL.md`
