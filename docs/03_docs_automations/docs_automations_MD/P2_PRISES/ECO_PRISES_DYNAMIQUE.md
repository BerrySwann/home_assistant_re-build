# [P2] ECO PRISES DYNAMIQUE — By Présence/Groupe

**Catégorie :** P2_prises
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
| `sensor.eco_prises_config` | Attribut `prises` (liste JSON) — cf. `templates/P2_prise/P2_eCO_prises/P2_eco_prises_config.yaml` |
| `notify.mobile_app_eric` | Notification de résumé |

## Fichier source

`P2_prises/eco_prises_dynamique_by_presence_groupe.yaml`

## ⚠️ Notes techniques

- Domaine-agnostique : `homeassistant.turn_on/off` fonctionne sur `switch.*` et `light.*`.
- `groupes: []` sans `absent_only` = toujours OFF (quel que soit le groupe).
- La config externe utilise `tojson` (HA exige une string template pour les attributs).
- Après modification de la config : Outils dev → YAML → **Recharger templates**.
- Référence : `sensor.eco_prises_config` (unique_id `eco_prises_config`).

---
*Doc unique du 2026-09-10 — fusion de ECO_PRISES.md et ECO_PRISES_DYNAMIQUE.md. L'ancienne fiche décrivait un montage disparu (5 prises en dur + créneaux HC + fenêtre de présence) ; le live a été refactorisé en liste externalisée déclenchée par le seul changement de groupe.*
