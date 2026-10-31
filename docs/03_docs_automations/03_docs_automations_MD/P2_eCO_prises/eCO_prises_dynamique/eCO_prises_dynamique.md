# [P2] ECO PRISES DYNAMIQUE — By Présence/Groupe

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

**Catégorie HA :** P2_éCO. Prises
**Alias HA :** `ECO. PRISES DYNAMIQUE -> By-Présence/Groupe`
**ID HA :** `1775245530054`
**Mode HA :** `queued`

## Description

Pilote une liste de prises et d'éclairages selon le **groupe de présence courant**
(G1 à G4). La liste des entités et leurs groupes est **externalisée** : l'automation
ne contient aucune prise en dur, elle lit la configuration à chaque exécution.

Ajouter ou retirer une prise = **1 ligne** dans la config externe + recharger les
templates. L'automation ne change jamais.

## Déclencheur

- `state` sur `sensor.groupe` (id : `groupe_change`) — un changement de groupe suffit.

## Condition

- Filtre anti-démarrage : ignore les transitions depuis `unavailable`, `unknown` ou vide.
  Évite de purger les prises quand HA redémarre et que `sensor.groupe` se réinitialise.

## Logique (pour chaque prise de la config)

- **groupe courant ∈ `groupes` de l'entrée** → `homeassistant.turn_on`
- **sinon** → `homeassistant.turn_off`, **sauf** si l'entrée est marquée `absent_only`
  et que le groupe courant n'est pas `groupe_1` : dans ce cas la prise est laissée
  dans son état (elle est pilotée par ailleurs — PC bureau, TV salon, TV chambre).

En clair :
- `groupes: [...]` = allumée pour ces groupes, éteinte sinon.
- `groupes: []` + `absent_only: true` = **coupée uniquement en mode Absent (G1)**,
  jamais allumée par cette automation.

## Prises pilotées (config `sensor.eco_prises_config`)

| Entité | Rôle | Groupes d'allumage |
|:---|:---|:---|
| `switch.prise_horloge_ikea` | Horloge entrée | G2, G4 |
| `light.hue_smart_eco_salon` | Éclairage salon | G2, G4 |
| `switch.ecran_p_c_3_play_hue` | Écran 3 Play (bureau) | G2, G3, G4 |
| `switch.prise_tete_de_lit_chambre` | Tête de lit chambre | G2, G4 |
| `light.hue_smart_eco_tv_salon` | TV salon | absent_only → OFF en G1 |
| `light.hue_smart_eco_pc_bureau` | PC bureau | absent_only → OFF en G1 |
| `light.hue_smart_eco_tv_chambre` | TV chambre | absent_only → OFF en G1 |

Rappel des groupes : G1 = Absent · G2 = Mamour seule · G3 = Eric seul · G4 = Tous les deux.

## Après la bascule

Délai de 5 secondes (le temps que les états se propagent), puis notification mobile
à Eric : titre `ECO PRISES: <GROUPE>`, message `[X/Y] prises ON` (comptage des prises
effectivement allumées).

## DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.groupe` | Groupe de présence courant |
| `sensor.eco_prises_config` | Attribut `prises` (liste JSON) — cf. `templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml` |
| `notify.mobile_app_eric` | Notification de résumé |
| `sensor.eco_prises_spy` | Spy de contrôle : groupe + état des 7 prises + écarts |

## Fichier source

`docs/03_docs_automations/03_docs_automations_YAML/P2_eCO_prises/eCO_prises_dynamique_by_presence_groupe/eCO_prises_dynamique_by_presence_groupe.yaml` (la liste des prises est dans `docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml`)

## ⚠️ Notes techniques

- Domaine-agnostique : `homeassistant.turn_on/off` fonctionne sur `switch.*` et `light.*`.
- `groupes: []` sans `absent_only` = toujours OFF (quel que soit le groupe).
- La config externe utilise `tojson` (HA exige une string template pour les attributs).
- Après modification de la config : Outils dev → YAML → **Recharger templates**.
- Référence : `sensor.eco_prises_config` (unique_id `eco_prises_config`).
- **Correctif 2026-09-23** : la liste `prises` est convertie via `| from_json` avant le
  `repeat.for_each` (il exige une liste native ; l'ancien texte JSON provoquait
  "Repeat 'for_each' must be a list of items" - 5 exécutions aborted en ~1,5 ms,
  tête de lit jamais coupée en absence). Spy de contrôle : `sensor.eco_prises_spy`.

---
*Relue le 2026-10-11 contre le YAML et contre la config externe : contenu conforme, seuls la catégorie et le chemin source ont été corrigés. Doc unique du 2026-09-10 — fusion de ECO_PRISES.md et ECO_PRISES_DYNAMIQUE.md. L'ancienne fiche décrivait un montage disparu (5 prises en dur + créneaux HC + fenêtre de présence) ; le live a été refactorisé en liste externalisée déclenchée par le seul changement de groupe.*
