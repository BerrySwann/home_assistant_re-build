# IA_INDEX_NAVIGATION.md — Contexte & Competence INDEX NAVIGATION (dashboard)

*Refait le : 2026-07-21 (ancien fichier 2026-05-30 obsolete — TREE_CORRIGE + INDEX_NAVIGATION_FULL.md supprimes)*

---

## Ce que c'est

La navigation dashboard est indexee dans la section `02-DASHBOARD` de :
- **Index principal** : `H:\Docs\INDEX_GLOBAL.md` (source de verite, rendu GitHub)
- **Copie locale** : `ReBuild/Github/INDEX_GLOBAL.md`

Il n'y a plus de fichier `INDEX_NAVIGATION_FULL.md` ni `INDEX_NAVIGATION.md` distinct —
fusionnes dans INDEX_GLOBAL.md (2026-07-16).

---

## Arborescence locale dashboard

```
DOCS/02_docs_dashboard/
- dashboard_docs_YAML/       <- YAMLs dashboard (vignettes, pages, cartes isolees)
    L1C1_01_Meteo/
    L1C2_02_Temperatures/
    ... (L*C* pour les 18 vignettes)
    Dashboard_COMPLET/       <- Exports complets dashboard (Dashboard_YYYY_MM_DD.yaml)
- dashboard_docs_MD/         <- Docs texte par vignette/page
    DEPENDANCES_GLOBALES.md  <- Chaînes de dependances toutes vignettes
    L1C1_*/  L1C2_*/  ...
```

Chemin prod config YAML : `DOCS/01_docs_config_system/config_system_YAML/` (sensors/, templates/, utility_meter/)
Chemin prod dashboard : `H:\Docs\` (push depuis local)

---

## Structure de l'index (section 02-DASHBOARD dans INDEX_GLOBAL.md)

```
Niveau 1 : L*C* — LABEL | X page(s) | ~N entites       <- retracte par defaut
  Niveau 2a : Vignette
    - Doc vignette (lien docs/02_docs_dashboard/dashboard_docs_MD/L*C*_*)
    - YAML vignette (lien docs/02_docs_dashboard/dashboard_docs_YAML/L*C*_*)
    - Fichiers sources (par fichier, entites listees)
  Niveau 2b : Page(s)
    - Doc page + YAML page
    - Fichiers sources (sensors/ templates/ utility_meter/)
    - Pop-up #hash — N entites
        chaque entite : "voir fichier" (lien config_system_YAML/) ou "Natif HA"
  Niveau 2c : Fichiers complementaires (si presents)
```

> Structure accordeon HTML (`<details>`/`<summary>`) a 3 niveaux, rendu natif sur GitHub.
> Balance globale verifiee apres chaque modif : `<details>` 358/358, `<blockquote>` 376/376.

---

## Chemins GitHub (relatifs racine repo `home_assistant_re-build`)

| Type | Chemin GitHub |
|:-----|:-------------|
| YAMLs dashboard | `docs/02_docs_dashboard/dashboard_docs_YAML/L*C*_*/` |
| Docs vignettes | `docs/02_docs_dashboard/dashboard_docs_MD/L*C*_*/` |
| Fichiers sources YAML | `docs/01_docs_config_system/config_system_YAML/sensors/\|templates/\|utility_meter/` |

> ⚠️ Casse minuscule `docs/` depuis 2026-07-19 (renommage H:\Docs -> H:\docs + push GitHub).
> Tous les liens INDEX_GLOBAL.md utilisent `docs/` minuscule (385 liens corriges).

---

## Etat de l'index (audit 2026-07-19)

- **18 vignettes** L1C1 a L6C3 auditees et corrigees integralement (entites verifiees contre YAML reel).
- **Homepage** corrigee (sensor.etat_wifi_maison, temperature_delta_affichage).
- Bugs corriges : balises `<details>` non fermees sur L1C2 et L1C3 (tout apres L1C2 etait imbrique).
- Blocs "Fichiers sources" repositionnes sur les bonnes pages (L2C1, L3C1, L4C3, L5C2).

---

## Limites toujours valides

- Entites dans templates Jinja (`states('sensor.xxx')`) non extraites par un parser automatique.
- Entites dans `button-card` JS inline non extractibles automatiquement.
- Reel nb d'entites ~30-40% superieur sur pages complexes (L2C1, L1C1).
- L3C1 : incoherence structurelle HTML "Page Gauche"/"Page Droite" deconnectees de leurs blocs
  entites — signalee, non corrigee (hors perimetre exactitude entites).

---

## Comment mettre a jour l'index

Apres ajout/modification d'une vignette, page ou fichier source :

1. Lire le YAML reel concerne (`DOCS/02_docs_dashboard/dashboard_docs_YAML/L*C*/`)
2. Verifier chaque entite citee contre le YAML prod (`DOCS/01_docs_config_system/config_system_YAML/`)
3. Mettre a jour la section 02-DASHBOARD de `INDEX_GLOBAL.md` (local puis H:\Docs\)
4. Verifier la balance `<details>`/`</details>` et `<blockquote>`/`</blockquote>` avant push
5. Mettre a jour `DEPENDANCES_GLOBALES.md` si necessaire (/sync_index)
