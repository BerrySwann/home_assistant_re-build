# IA_INDEX_NAVIGATION.md - Contexte & Competence INDEX NAVIGATION (dashboard)

*Mis a jour le : 2026-10-13 (arborescence, index generes et procedure remis a jour ; version precedente du 2026-07-21)*

---

## Ce que c'est

La navigation dashboard est indexee a deux endroits :
- **Index genere** : `docs/02_docs_dashboard/GLOBAL_INDEX_VIGNETTES_PAGES.md` (vignettes et pages : fiche, YAML, dependances). Regenere a chaque `/histo` par `docs/04_docs_scripts/04_docs_scripts_sh/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.py`. Ne jamais le modifier a la main.
- **Index detaille en accordeon** : section `02 - DASHBOARD (18 vignettes)` de `GLOBAL_INDEX_REPO.md` (racine de `H:\` + copie locale `docs/01_docs_config_system/config_system_MD/GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md`). Maintenue a la main.

Il n'y a plus de fichier `INDEX_NAVIGATION_FULL.md` ni `INDEX_NAVIGATION.md` distinct (fusionnes dans GLOBAL_INDEX_REPO.md le 2026-07-16). `INDEX_PAGES.md` a ete retire du local le 2026-10-13 : remplace par l'index genere.

---

## Arborescence locale dashboard (verifiee 2026-10-13)

```
docs/02_docs_dashboard/
- GLOBAL_INDEX_VIGNETTES_PAGES.md   <- index genere (ne pas modifier)
- 02_dashboard_docs_yaml/              <- YAMLs dashboard (vignettes, pages, cartes isolees)
    L0C0_PAGE_Home/  L1C1_METEO/  L1C2_TEMPERATURES/  ...  L6C3_VIGIEAU/  (18 vignettes)
    PAGE_RASPI/
    Dashboard_COMPLET/              <- Exports complets dashboard (Dashboard_YYYY_MM_DD.yaml)
- 02_dashboard_docs_md/                <- Fiches texte par vignette/page
    L0C0_PAGE_Home/  L1C1_METEO/  L1C2_TEMPERATURES/  ...  L6C3_VIGIEAU/
    (chaque dossier L*C* : 01_Vignette/ et 02_Page/, 02_page_nom si plusieurs pages)
```

La chaine de dependances (`DEPENDANCES_GLOBALES.md`) est dans `docs/XX_docs_MD_system/DEPENDANCES_GLOBALES/`, plus dans `02_dashboard_docs_md`.
Prod : `H:\docs\` = miroir de `docs\` local ; un seul export `H:\Dashboard_AAAA_MM_JJ.yaml` a la racine de `H:\` (verifie par `/histo`, etape 5B). Config YAML prod : `sensors/`, `templates/`, `utility_meter/` a la racine de `H:\`.

---

## Structure de l'index accordeon (section 02-DASHBOARD dans GLOBAL_INDEX_REPO.md)

```
Niveau 1 : L*C* - LABEL | X page(s) | ~N entites       <- retracte par defaut
  Niveau 2a : Vignette
    - Doc vignette (lien docs/02_docs_dashboard/02_dashboard_docs_md/L*C*_*/01_Vignette/...)
    - YAML vignette (lien docs/02_docs_dashboard/02_dashboard_docs_yaml/L*C*_*/...)
    - Fichiers sources (par fichier, entites listees)
  Niveau 2b : Page(s)
    - Doc page + YAML page
    - Fichiers sources (sensors/ templates/ utility_meter/)
    - Pop-up #hash - N entites
        chaque entite : "voir fichier" (lien config_system_SH_PY_YAML/) ou "Natif HA"
  Niveau 2c : Fichiers complementaires (si presents)
```

> Structure accordeon HTML (`<details>`/`<summary>`) a 3 niveaux, rendu natif sur GitHub.
> Balance globale verifiee le 2026-10-13 sur GLOBAL_INDEX_REPO.md : `<details>` 411/411, `<blockquote>` 430/430 (a reverifier apres chaque modif).

---

## Chemins GitHub (relatifs racine repo `home_assistant_re-build`)

| Type | Chemin GitHub |
|:-----|:-------------|
| YAMLs dashboard | `docs/02_docs_dashboard/02_dashboard_docs_yaml/L*C*_*/` |
| Docs vignettes | `docs/02_docs_dashboard/02_dashboard_docs_md/L*C*_*/01_Vignette/` |
| Fichiers sources YAML | `docs/01_docs_config_system/config_system_SH_PY_YAML/` |

> ⚠️ Casse minuscule `docs/` depuis 2026-07-19 (renommage H:\Docs -> H:\docs + push GitHub).

---

## Etat de l'index

- **Index genere (controle du 2026-10-13)** : 18 vignettes L1C1 a L6C3, 20 dossiers au total, 0 vignette sans fiche ou sans YAML ; 141 liens, 0 casse. Seul cas particulier : `PAGE_RASPI` (YAML sans fiche propre, sa fiche est rangee sous L4C1).
- Historique : audit du 2026-07-19 (18 vignettes verifiees contre le YAML reel ; homepage corrigee ; balises `<details>` non fermees corrigees sur L1C2 et L1C3 ; blocs "Fichiers sources" repositionnes).

---

## Limites toujours valides

- Entites dans templates Jinja (`states('sensor.xxx')`) non extraites par un parser automatique.
- Entites dans `button-card` JS inline non extractibles automatiquement.
- Reel nb d'entites ~30-40% superieur sur pages complexes (L2C1, L1C1) (estimation du 2026-07-19).
- L3C1 : incoherence structurelle HTML "Page Gauche"/"Page Droite" deconnectees de leurs blocs entites - constat du 2026-07-19, non revalide depuis.

---

## Comment mettre a jour l'index

Apres ajout/modification d'une vignette, page ou fichier source :

1. Lire le YAML reel concerne (`docs/02_docs_dashboard/02_dashboard_docs_yaml/L*C*/`).
2. Verifier chaque entite citee contre le YAML prod.
3. Lancer `/histo` (regenere `GLOBAL_INDEX_VIGNETTES_PAGES.md`) ou a la main : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\Gen_GLOBAL_INDEX_vignettes_pages\Gen_GLOBAL_INDEX_vignettes_pages.py"` ; verifier `liens=N casses=M` avec casses=0.
4. Mettre a jour a la main la section 02-DASHBOARD de `GLOBAL_INDEX_REPO.md` si besoin (local puis racine de H:), verifier la balance `<details>`/`</details>` et `<blockquote>`/`</blockquote>` avant push.
5. Mettre a jour `DEPENDANCES_GLOBALES.md` si necessaire (/sync-index).
