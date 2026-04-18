# PALETTE COULEURS — PRISES CONNECTÉES PAR PIÈCE (Pôle 2)

> **Source de vérité** : `IA_CONTEXT_BASE.md` § Palette Officielle (Pôles 3 & 2)
> **Référence dashboard** : `apexcharts-card` (donuts + barres) et `--mdc-theme-primary` des `tabbed-card`.
> **Entités sources** : `dashbord/page_energie_mensuel.yaml` / `dashbord/page_energie_temps_reel.yaml`
> **Dernière mise à jour** : 2026-03-08 (Refonte complète — entités réelles + palette Gemini)

---

## 1. ENTRÉE — Gris clair

| Appareil       | Entité (`_quotidien_kwh_um`)                                  | Couleur              |
|----------------|---------------------------------------------------------------|----------------------|
| Box Internet   | `sensor.prise_box_internet_ikea_quotidien_kwh_um`             | `gainsboro`          |
| Horloge        | `sensor.prise_horloge_ikea_quotidien_kwh_um`                  | `rgb(183, 183, 183)` |

**`--mdc-theme-primary`** : `rgb(220, 220, 220)`

---

## 4. SALON — Rose (3 appareils)

| Appareil       | Entité (`_quotidien_kwh_um`)                                  | Couleur                  |
|----------------|---------------------------------------------------------------|--------------------------|
| PC Géraldine   | `sensor.prise_pc_s_gege_ikea_quotidien_kwh_um`                | `rgb(174, 68, 90)`       |
| Chargeur Salon | `sensor.prise_salon_chargeur_nous_quotidien_kwh_um`           | `rgb(196, 75, 97)`       |
| TV Salon       | `sensor.prise_tv_salon_ikea_quotidien_kwh_um`                 | `rgb(215, 95, 115)`      |

**`--mdc-theme-primary`** : `rgb(215, 95, 115)`

---

## 5. CUISINE — Violet (8 appareils)

### Cuisson / Électroménager chaud (6 appareils)

| Appareil         | Entité (`_quotidien_kwh_um`)                                  | Couleur                |
|------------------|---------------------------------------------------------------|------------------------|
| Four Micro-ondes | `sensor.prise_four_micro_ondes_nous_quotidien_kwh_um`         | `rgb(98, 78, 136)`     |
| Petit-déjeuner   | `sensor.prise_petit_dejeune_nous_quotidien_kwh_um`            | `rgb(118, 93, 160)`    |
| Lave-linge       | `sensor.prise_lave_linge_nous_quotidien_kwh_um`               | `rgb(137, 103, 179)`   |
| Lave-vaisselle   | `sensor.prise_lave_vaisselle_nous_quotidien_kwh_um`           | `rgb(129, 116, 180)`   |
| AirFryer Ninja   | `sensor.prise_airfryer_ninja_nous_quotidien_kwh_um`           | `rgb(142, 122, 181)`   |
| Four & Plaque    | `sensor.four_et_plaque_de_cuisson_quotidien_kwh_um`           | `rgb(162, 148, 249)`   |

### Froid (2 appareils)

| Appareil   | Entité (`_quotidien_kwh_um`)                                  | Couleur              |
|------------|---------------------------------------------------------------|----------------------|
| Frigo      | `sensor.prise_frigo_cuisine_nous_quotidien_kwh_um`            | `cyan`               |
| Congélateur| `sensor.prise_congelateur_cuisine_nous_quotidien_kwh_um`      | `rgb(19, 160, 255)`  |

**`--mdc-theme-primary`** : `rgb(118, 93, 160)`

---

## 7. BUREAU — Orange (2 appareils)

| Appareil       | Entité (`_quotidien_kwh_um`)                                  | Couleur                  |
|----------------|---------------------------------------------------------------|--------------------------|
| PC Bureau      | `sensor.prise_bureau_pc_ikea_quotidien_kwh_um`                | `rgb(255, 165, 0)`       |
| Fer à repasser | `sensor.prise_bureau_fer_a_repasser_nous_quotidien_kwh_um`    | `rgb(255, 183, 51)`      |

**`--mdc-theme-primary`** : `rgb(255, 165, 0)`

---

## 9. CHAMBRE — Vert (2 appareils)

| Appareil    | Entité (`_quotidien_kwh_um`)                                  | Couleur                  |
|-------------|---------------------------------------------------------------|--------------------------|
| Tête de lit | `sensor.prise_tete_de_lit_chambre_quotidien_kwh_um`           | `rgb(75, 130, 85)`       |
| TV Chambre  | `sensor.prise_tv_chambre_nous_quotidien_kwh_um`               | `rgb(105, 155, 110)`     |

**`--mdc-theme-primary`** : `rgb(88, 130, 70)`

---

## 10. AUTRE — Veilles / Standby

| Appareil    | Entité                                                        | Couleur |
|-------------|---------------------------------------------------------------|---------|
| All Standby | `sensor.all_standby_quotidien_kwh_um`                         | `grey`  |

**`--mdc-theme-primary`** : `grey`

---

## RÉCAPITULATIF RAPIDE

| #  | Pièce    | Famille    | `--mdc-theme-primary`  | Appareils   |
|----|----------|------------|------------------------|-------------|
|  1 | ENTRÉE   | Gris clair | `rgb(220, 220, 220)`   | 2           |
|  4 | SALON    | Rose       | `rgb(215, 95, 115)`    | 3           |
|  5 | CUISINE  | Violet     | `rgb(118, 93, 160)`    | 6 + 2 froid |
|  7 | BUREAU   | Orange     | `rgb(255, 165, 0)`     | 2           |
|  9 | CHAMBRE  | Vert       | `rgb(88, 130, 70)`     | 2           |
| 10 | AUTRE    | Gris       | `grey`                 | 1 (standby) |

---

## NOTE SUR LES ENTITÉS

Pattern général : `sensor.prise_{slug}_{marque}_{periode}_kwh_um`

- **`{marque}`** : `ikea` (IKEA TRÅDFRI / DIRIGERA) ou `nous` (NOUS Smart Plug)
- **`{periode}`** : `quotidien` / `hebdomadaire` / `mensuel` / `annuel`
- **Exceptions sans suffixe marque** :
  - `sensor.four_et_plaque_de_cuisson_*` (prise sans nom de marque)
  - `sensor.all_standby_*` (capteur virtuel agrégé)

> **Synchronisation** : Les couleurs de ce fichier sont synchronisées avec la section
> `### 🎨 PALETTE COULEURS OFFICIELLE` de `docs/IA/IA_CONTEXT_BASE.md`.


<!-- obsidian-wikilinks -->
---
*Liens : [[L2C1_VIGNETTE_ENERGIE]]  [[L3C2_VIGNETTE_PRISES]]*
