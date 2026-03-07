# PALETTE COULEURS — PRISES CONNECTÉES PAR PIÈCE (L2C2)

> Référence officielle pour `apexcharts-card` (donuts + barres) et `--mdc-theme-primary` des tabbed-cards.
> Chaque pièce a une famille chromatique distincte des lampes (L2C3).

---

## 1. ENTRÉE — Teal / Cyan (réseau)

| Appareil               | Entité (`_quotidien_kwh_um`)                     | Couleur            | HEX / RGB                  |
|------------------------|--------------------------------------------------|--------------------|----------------------------|
| Box Internet           | `sensor.box_internet_entree_quotidien_kwh_um`    | Teal 600           | `rgb(0, 172, 193)`         |
| Horloge                | `sensor.horloge_entree_quotidien_kwh_um`         | Teal 300           | `rgb(77, 208, 225)`        |

**`--mdc-theme-primary`** : `rgb(0, 172, 193)`

---

## 4. SALON — Ambre / Or (multimédia)

| Appareil               | Entité (`_quotidien_kwh_um`)                     | Couleur            | HEX / RGB                  |
|------------------------|--------------------------------------------------|--------------------|----------------------------|
| PC Géraldine           | `sensor.pc_s_gege_salon_quotidien_kwh_um`        | Amber 600          | `rgb(255, 193, 7)`         |
| Chargeur Salon         | `sensor.salon_chargeur_salon_quotidien_kwh_um`   | Amber 800          | `rgb(255, 160, 0)`         |

**`--mdc-theme-primary`** : `rgb(255, 193, 7)`

---

## 5. CUISINE — Rouge / Rose (électroménager — 8 appareils)

| Appareil               | Entité (`_quotidien_kwh_um`)                     | Couleur            | HEX / RGB                  |
|------------------------|--------------------------------------------------|--------------------|----------------------------|
| Frigo                  | `sensor.frigo_cuisine_quotidien_kwh_um`          | Red 900            | `rgb(183, 28, 28)`         |
| Congélateur            | `sensor.congel_cuisine_quotidien_kwh_um`         | Red 700            | `rgb(211, 47, 47)`         |
| Lave-Linge             | `sensor.lave_linge_cuisine_quotidien_kwh_um`     | Red 400            | `rgb(239, 83, 80)`         |
| Lave-Vaisselle         | `sensor.lave_vaisselle_cuisine_quotidien_kwh_um` | Pink 400           | `rgb(240, 98, 146)`        |
| Four / Plaque          | `sensor.four_plaque_cuisine_quotidien_kwh_um`    | Red 600            | `rgb(229, 57, 53)`         |
| Micro-ondes            | `sensor.micro_ondes_cuisine_quotidien_kwh_um`    | Deep Orange 400    | `rgb(255, 112, 67)`        |
| AirFryer               | `sensor.airfryer_cuisine_quotidien_kwh_um`       | Deep Orange 200    | `rgb(255, 171, 145)`       |
| Petit-Déj              | `sensor.petit_dejeune_cuisine_quotidien_kwh_um`  | Orange 200         | `rgb(255, 204, 128)`       |

**`--mdc-theme-primary`** : `rgb(229, 57, 53)`

---

## 7. BUREAU — Bleu ardoise (informatique)

| Appareil               | Entité (`_quotidien_kwh_um`)                     | Couleur            | HEX / RGB                  |
|------------------------|--------------------------------------------------|--------------------|----------------------------|
| PC Bureau              | `sensor.bureau_pc_quotidien_kwh_um`              | Blue 700           | `rgb(25, 118, 210)`        |
| Fer à repasser         | `sensor.fer_a_repasser_bureau_quotidien_kwh_um`  | Blue 300           | `rgb(100, 181, 246)`       |

**`--mdc-theme-primary`** : `rgb(25, 118, 210)`

---

## 9. CHAMBRE — Indigo / Bleu nuit (repos)

| Appareil               | Entité (`_quotidien_kwh_um`)                     | Couleur            | HEX / RGB                  |
|------------------------|--------------------------------------------------|--------------------|----------------------------|
| Tête de lit            | `sensor.tete_de_lit_chambre_quotidien_kwh_um`    | Indigo 600         | `rgb(57, 73, 171)`         |
| TV Chambre             | `sensor.tv_chambre_quotidien_kwh_um`             | Indigo 300         | `rgb(121, 134, 203)`       |

**`--mdc-theme-primary`** : `rgb(57, 73, 171)`

---

## 10. AUTRE — Gris neutre (standby)

| Appareil               | Entité                                           | Couleur            | HEX / RGB                  |
|------------------------|--------------------------------------------------|--------------------|----------------------------|
| All Standby            | `sensor.all_standby_quotidien_kwh_um`            | Grey 600           | `rgb(117, 117, 117)`       |

**`--mdc-theme-primary`** : `rgb(117, 117, 117)`

---

## RÉCAPITULATIF RAPIDE

| Pièce     | Famille         | `--mdc-theme-primary`    |
|-----------|-----------------|--------------------------|
| Entrée    | Teal            | `rgb(0, 172, 193)`       |
| Salon     | Ambre           | `rgb(255, 193, 7)`       |
| Cuisine   | Rouge/Rose      | `rgb(229, 57, 53)`       |
| Bureau    | Bleu ardoise    | `rgb(25, 118, 210)`      |
| Chambre   | Indigo          | `rgb(57, 73, 171)`       |
| Autre     | Gris            | `rgb(117, 117, 117)`     |

---

## NOTE SUR LES ENTITÉS

Les entités `_quotidien_kwh_um` ci-dessus suivent le pattern :
`sensor.{slug_appareil}_{piece}_{periode}_kwh_um`

Périodes disponibles : `quotidien` / `hebdomadaire` / `mensuel` / `annuel`

Source sensors : `sensors/p2_sensors_ prises.yaml`
