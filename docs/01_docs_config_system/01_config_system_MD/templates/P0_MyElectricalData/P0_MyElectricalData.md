# P0_MyElectricalData - Capteurs Linky J0 à J7 (avec repli Nodon)

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `P0_MyElectricalData.yaml`
> **Emplacement prod :** `/config/templates/P0_energie_total_diag/P0_Linky/P0_MyElectricalData.yaml` (et miroir `/config/docs/01_docs_config_system/01_config_system_SH_PY_YAML/...`)
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/templates/P0_energie_total_diag/P0_Linky/P0_MyElectricalData.yaml`
> **Empreinte relevée le 2026-10-23 :** MD5 `60ce6de6`, 96575 octets, copie locale identique à la prod après le push du 2026-10-23
> **Inclus par :** `configuration.yaml` (`template: !include_dir_merge_list templates/`)
> **Dernière modification :** 2026-10-23 (repli Nodon J1 à J7 + coût de J0 aux tarifs HPHC)

---

## Description

Huit capteurs template `linky_jour_0` à `linky_jour_7` : consommation journalière sur 8 jours, avec les attributs `jour`, `hp`, `hc`, `total`, `cout`. Ils alimentent le tableau de l'onglet hebdomadaire de L2C1 (Énergie Générale).

- **J0 (Aujourd'hui)** : `sensor.genelec_appart_quotidien_um` (total) et `sensor.genelec_appart_hphc_quotidien_um_hp` / `_hc` (split). Coût = HP x `sensor.tarif_heures_pleines_ttc` + HC x `sensor.tarif_heures_creuses_ttc` (tarifs EDF HPHC 6kVA TTC lus en direct, plus de prix en dur).
- **J1 à J7** : attributs `day_N_HP`, `day_N_HC`, `dailyweek`, `dailyweek_cost` de `sensor.linky_25481620821301_consumption` (MyElectricalData / Enedis).

## Repli sur Nodon quand le Linky vaut 0 (depuis le 2026-10-23)

Enedis publie avec un ou deux jours de retard : quand `day_N_HP + day_N_HC` vaut 0 pour une date, le capteur prend la valeur Nodon de la même date et ajoute une `*` au nom du jour (exemple : `Mercredi*`). Total, HP, HC et coût suivent la valeur Nodon. L'étoile n'apparaît jamais sur une valeur Linky réelle.

Ordre de recherche de la valeur de remplacement (le premier qui répond gagne) :

1. `sensor.histo_energie_nodon_complet`, attribut `data[JJ/MM]` : total, HP, HC, coût (fichier `nodon_complet_histo.txt`).
2. Si la date est celle d'hier : `last_period` des trois compteurs Nodon (`genelec_appart_quotidien_um`, `..._hp`, `..._hc`), coût aux tarifs HPHC TTC. Ce cas couvre J1 sans attendre le fichier.
3. Sinon : le total de `sensor.histo_energie_nodon` (fichier `nodon_histo.txt`) ; HP, HC et coût restent à 0 faute de source.

Si aucune valeur Nodon n'est trouvée, le capteur affiche le Linky tel quel (0) sans étoile.

## Automations rattachées

Le repli lit des fichiers écrits par des automations P0 (Pôle Énergie) :

- **E - [P0] Histo Nodon complet quotidien** (id `1792780906393`, 23:59:10) : écrit `nodon_complet_histo.txt` (Total, HP, HC, Coût de la veille). C'est la source n°1 du repli.
- **B - [P0] Histo Nodon quotidien** (id `1788118227600`, 23:59:00) : écrit `nodon_histo.txt` (total seul). C'est la source n°3 (secours).

Les automations Linky A (id `1788118118362`), C (id `1788118327851`) et D (id `1788237916871`) journalisent et corrigent `linky_histo.txt` / `ecart_histo.txt`. Elles ne nourrissent pas ces capteurs, qui lisent directement les attributs `day_N` du capteur MyElectricalData.

## Points d'attention

- Chaque champ (état, jour, hp, hc, total, cout) répète le calcul de repli : le fichier fait environ 1500 lignes. Une modification du repli doit être faite dans les 7 capteurs.
- Le fichier `nodon_complet_histo.txt` n'existe qu'à partir du 23/10/2026 (première ligne : 22/10). Avant, les jours à 0 n'ont que le total Nodon (HP, HC et coût à 0).
- La valeur Nodon peut s'écarter du Linky (exemple relevé le 2026-10-23 : 20/10, Linky 5.7 kWh contre Nodon 3.8 kWh). Une valeur à `*` est une estimation.
- Les noms de jour viennent de `dailyweek` (index 0 pour J1 ... index 6 pour J7). Les corrections forcées des index de J6 et J7 sont conservées dans le fichier.
- Aval : vignette L2C1 04 Énergie Générale (tableau J0 à J7).