# (E) MINUTERIE SÈCHE-SERVIETTES SDB — TIMER 2H

> **Fichier :** `automations_corrige/P1_sdb/E_minuterie_seche_serviettes.yaml`
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
