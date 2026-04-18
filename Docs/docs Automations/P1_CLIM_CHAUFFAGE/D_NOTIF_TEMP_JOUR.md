# (D) NOTIFICATION TEMPÉRATURE — JOUR (07H30 → 21H00)

> **Fichier :** `automations_corrige/P1_clim_chauffage/D_notif_temp_jour.yaml`
> **Mode HA :** `queued`

---

## 📝 Description

Envoie le message personnalisé de clim (tendance T°, mode, présence) à chaque
changement de température extérieure, en période diurne. Inclut une vérification
de disponibilité des capteurs avant envoi.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.th_balcon_nord_temperature` |
| `time` | 07:30:00 (envoi forcé au réveil) |

---

## 🔒 Conditions

- Plage horaire inline : `after 07:30 before 21:00`

---

## ⚙️ Actions

1. Pause 2s (stabilisation)
2. **Si** capteurs KO → notification d'erreur `[ANJ] Erreur Capteurs`
3. **Sinon** → notification `[Automa. Notif. Jrs]` avec `sensor.message_clim_personnalise_7h30_21h00`

---

## 🔌 DÉPENDANCES

### Entités lues

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_temperature` | Déclencheur + vérification dispo |
| `sensor.message_clim_personnalise_7h30_21h00` | Contenu du message à envoyer |
| `sensor.mamour_wi_fi_connection` | Vérification dispo |
| `sensor.eric_wi_fi_connection` | Vérification dispo |

### Notifications

| Titre | Condition |
|:---|:---|
| `[ANJ] Erreur Capteurs` | Capteur indisponible |
| `[Automa. Notif. Jrs]` | Normal — contenu du sensor message |
