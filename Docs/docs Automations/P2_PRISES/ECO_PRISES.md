# AUTOMATION ÉCO PRISES — PILOTAGE DYNAMIQUE

> **Fichier :** `automations_corrige/P2_prises/eco_prises.yaml`
> **Mode HA :** `queued`

---

## 📝 Description

Pilotage de 5 prises selon le groupe de présence (G1–G4), les Heures Creuses
et la fenêtre de présence 07h30–21h.
Recalcule à chaque changement de groupe et à chaque transition HC/HP (01h, 07h30, 13h, 14h30, 21h).

---

## ⚡ Déclencheurs

| Type | Entité / Horaire |
|:---|:---|
| `state` | `sensor.groupe` |
| `time` | 01:00 / 07:30 / 13:00 / 14:30 / 21:00 |

---

## ⚙️ Variables calculées

| Variable | Logique |
|:---|:---|
| `is_hc` | 01:00–07:30 ou 13:00–14:30 |
| `is_pres_win` | 07:30–21:00 |
| `g` | `sensor.groupe` |
| `pres_active` | G2 ou G4 |
| `target_horloge` | ON si présent ET fenêtre présence |
| `target_vapote` | ON si présent+fenêtre OU HC |

---

## ⚙️ Logique par groupe

| Groupe | Horloge | Vapote | 3 Play | PC bureau | Tête de lit |
|:---:|:---:|:---:|:---:|:---:|:---:|
| G1 | OFF | HC seulement | OFF | OFF | OFF |
| G2 | target | target | ON | OFF | ON |
| G3 | OFF | HC seulement | ON | — | OFF |
| G4 | target | target | ON | — | ON |

---

## 🔌 DÉPENDANCES

### Entités lues

| Entité | Rôle |
|:---|:---|
| `sensor.groupe` | Groupe de présence |
| `sensor.presence` | Texte présence (notif titre) |

### Entités pilotées

| Entité | Rôle |
|:---|:---|
| `switch.prise_horloge_ikea` | Horloge entrée |
| `light.hue_smart_salon` | Vapote / prise Hue salon |
| `switch.ecran_p_c_3_play_hue` | Écran 3 Play (bureau) |
| `switch.hue_smart_eco_pc_bureau` | Alim PC bureau |
| `switch.prise_tete_de_lit_chambre` | Tête de lit chambre |

### Notifications

| Titre | Message |
|:---|:---|
| `sensor.presence` | Comptage prises ON |
