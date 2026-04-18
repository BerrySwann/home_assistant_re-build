# (E) NOTIFICATION TEMPÉRATURE — NUIT (21H00 → 07H30)

> **Fichier :** `automations_corrige/P1_clim_chauffage/E_notif_temp_nuit.yaml`
> **Mode HA :** `queued`

---

## 📝 Description

Miroir nocturne de D. Même logique mais sur la plage 21h00–07h30 et
avec `sensor.message_clim_personnalise_21h00_7h30`.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.th_balcon_nord_temperature` |
| `time` | 21:00:00 |

---

## ⚙️ Actions

1. Pause 2s
2. Si capteurs KO → `[ANN] Erreur Capteurs`
3. Sinon → `[Automa. Notif. Nuit]` avec contenu du sensor nuit

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_temperature` | Déclencheur |
| `sensor.message_clim_personnalise_21h00_7h30` | Message nuit |
| `sensor.mamour_wi_fi_connection` | Vérification |
| `sensor.eric_wi_fi_connection` | Vérification |
