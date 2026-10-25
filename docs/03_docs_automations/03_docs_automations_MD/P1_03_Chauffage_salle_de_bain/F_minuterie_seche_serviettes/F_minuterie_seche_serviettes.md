# (F) MINUTERIE SÈCHE-SERVIETTES SDB - TIMER 2H

> **Mise a jour 2026-10-11 :** fiche renommée F_MINUTERIE_SECHE_SERVIETTES.md (ancien nom E_), chemin du YAML et ID HA ajoutés, contenu relu contre le YAML, conforme.
>
> **Mise a jour 2026-10-07 :** cette automation s'appelle desormais **F** (elle etait E puis G, renommee par Eric ; lettres decalees le 2026-10-11). Doublee le meme jour par G et H (timers, voir `TIMERS_SDB_SOUFFLANT_ET_SECHE_SERVIETTES.md`). F reste active en doublon jusqu'au test de G.

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_03_Chauffage_Salle_de_Bain/f_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h/f_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h.yaml`
> **ID HA :** `1766776781417` (en prod dans automations.yaml)
> **Mode HA :** `single`

---

## 📝 Description

Démarrée automatiquement dès détection d'une consommation > 50W sur la prise
sèche-serviette. Attend 2h, vérifie que la prise est toujours ON, la coupe,
notifie, attend 1 min puis la remet en veille (réarmement).

---

## ⚡ Déclencheurs

| Type | Entité | Seuil |
|:---|:---|:---|
| `numeric_state` | `sensor.prise_seche_serviette_salle_de_bain_nous_power` | > 50W |

---

## ⚙️ Séquence

1. `delay: 02:00:00`
2. Condition : `switch.prise_seche_serviette_salle_de_bain_nous` est `on`
3. `switch.turn_off` → prise sèche-serv
4. Notification `Sèche-Serv. OFF` / `2h écoulees. Arret automatique.`
5. `delay: 00:01:00`
6. `switch.turn_on` → réarmement veille

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.prise_seche_serviette_salle_de_bain_nous_power` | Déclencheur (W) |
| `switch.prise_seche_serviette_salle_de_bain_nous` | Pilotage ON/OFF |

### Notifications

| Titre (15c max) | Message |
|:---|:---|
| `Sèche-Serv. OFF` | `2h écoulees. Arret automatique.` |

---

## ⚠️ Points d'attention

- Mode `single` : si la prise s'allume pendant le décompte, pas de relance. Intentionnel (anti-doublon).
- Le réarmement en veille (turn_on à la fin) est nécessaire car la prise NOUS doit rester alimentée pour le suivi conso.
