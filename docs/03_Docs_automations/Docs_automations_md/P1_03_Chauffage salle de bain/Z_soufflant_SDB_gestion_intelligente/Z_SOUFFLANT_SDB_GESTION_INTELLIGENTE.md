# (Z) SOUFFLANT SDB - GESTION INTELLIGENTE (ancienne logique, désactivée)

> **Fichier :** `docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage Salle de Bain/z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant/z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant.yaml`
> **ID HA :** `1774803407558` (`automation.a_2026_02_01_salle_de_bain_gestion_intelligente_soufflant`)
> **Alias HA :** `Z - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT`
> **Mode HA :** `queued` (`max: 3`)
> **État dans HA (relevé le 2026-10-11) :** désactivée (`off`), dernier déclenchement le 2026-05-27
> **MàJ :** 2026-10-11 (fiche écrite d'après le YAML, identique à H:\automations.yaml)

---

## Description

Ancienne automation tout-en-un du soufflant de la salle de bain. Description HA : "Cycle complet : Démarrage, Régulation, et Auto-off 60 min avec refroidissement". Dans HA elle est désactivée ; les fiches A / B (bouton et routage), E / F (timers) et D (watchdog) décrivent la chaîne actuelle du soufflant.

---

## Déclencheurs

| ID | Type | Entité | Condition |
|:---|:---|:---|:---|
| `inter_change` | `state` | `switch.inter_soufflant_salle_de_bain` | tout changement |
| `temp_high` | `numeric_state` | `sensor.th_salle_de_bain_temperature` | au-dessus de 22,9 pendant 1 min |
| `temp_low` | `numeric_state` | `sensor.th_salle_de_bain_temperature` | en dessous de 21,9 |
| `auto_off` | `state` | `switch.inter_soufflant_salle_de_bain` | passe à `on` pendant 1 h |

---

## Actions (choose, selon le déclencheur)

1. Allumage de l'interrupteur (`inter_change`, interrupteur `on`, température sous 25) :
   - `switch.turn_on` sur `switch.prise_soufflant_salle_de_bain_nous`, 1 s, IR `on_off` sur `remote.soufflant_sdb` (appareil `radiateur_sdb`), 0,8 s ;
   - si température sous 21 : IR `1000w` ×2 (0,8 s entre les deux) et `input_select.etat_resistance_soufflant_sdb` = `2000W` ; sinon IR `1000w` ×1 et l'état = `1000W` ;
   - 0,8 s, IR `swing`, `climate.soufflant_salle_de_bain` en `heat`.
2. Température haute (`temp_high`, interrupteur `on`, état résistance différent de `0W`) : IR `1000w` (×2 si l'état est `1000W`, sinon ×1), état résistance = `0W`.
3. Température basse (`temp_low`, interrupteur `on`, état résistance = `0W`) : IR `1000w`, état résistance = `1000W`.
4. Extinction (interrupteur passé à `off`, ou `auto_off`) : pour `auto_off`, `switch.turn_off` sur l'interrupteur ; puis IR `on_off`, 1 min, `climate.soufflant_salle_de_bain` en `off`, coupure de la prise, état résistance = `0W`.

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `switch.inter_soufflant_salle_de_bain` | Interrupteur (déclencheur, condition, coupure auto) |
| `sensor.th_salle_de_bain_temperature` | Température salle de bain |
| `switch.prise_soufflant_salle_de_bain_nous` | Prise du soufflant |
| `remote.soufflant_sdb` | Télécommande IR (appareil `radiateur_sdb`) |
| `input_select.etat_resistance_soufflant_sdb` | État mémorisé de la résistance (`0W`, `1000W`, `2000W`) |
| `climate.soufflant_salle_de_bain` | Entité climate du soufflant |

---

## Notes

- Elle remplace l'ancienne fiche `Z_SOUFFLANT_SDB_old_2024-2025` (un modèle sans description, avec l'alias "A - 2026/02/01 ..."), gardée en `.bak_date_heure` dans le même dossier.
- Dans le YAML, l'alias du cas de démarrage dit "DÉMARRAGE 2000W (< 21°C)" et envoie bien 2 commandes `1000w` ; le nom `2000W` correspond à l'état mémorisé.
- Le contexte actuel du chauffage SDB est décrit dans `SDB_SOUFFLANT_SPECIFICATION_2026.md` (spécification) et `TIMERS_SDB_SOUFFLANT_ET_SECHE_SERVIETTES.md`.