# ALLUMAGE LUMIÈRE ENTRÉE

> **Fichier :** `automations_corrige/P3_eclairage/allumage_lumiere_entree.yaml`
> **Mode HA :** `queued`

---

## 📝 Description

Allume la lumière de l'entrée lors d'une arrivée. Gère deux cas :
1. Arrivée initiale (G1 → G2/G3/G4) en période diurne (soleil levé)
2. Retour de Mamour quand Eric est déjà là (G3 → G4)

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.groupe` |

---

## ⚙️ Actions — Choose

**CAS 1 — Arrivée initiale diurne :**
- Condition : `from == groupe_1` ET `to in [groupe_2, groupe_3, groupe_4]`
- Condition : `sun.sun == above_horizon`
- Action : `light.turn_on → light.entree`

**CAS 2 — Retour Mamour (G3→G4) :**
- Condition : `from == groupe_3` ET `to == groupe_4`
- Action : `light.turn_on → light.entree`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.groupe` | Déclencheur + logique de transition |
| `sun.sun` | Condition lever/coucher soleil |
| `light.entree` | Lumière entrée (Hue White) |
