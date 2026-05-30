# 👥 RÉFÉRENTIEL P4 — PRÉSENCE COMPLÈTE
*Lire ce fichier si : automation clim, message notify avec présence, logique sensor.groupe ou sensor.presence.*

---

## sensor.groupe — Logique d'automatisation

> Source : `templates/P4_groupe_presence/02_logique_wifi_cellular.yaml`
> Réseau cible : `'Module B.E.R.Y.L. [GG-5.0]'` ou `'Module B.E.R.Y.L. [GG-2.4]'`

Utilisé par les automations (clim, volets, mode éco).

| Valeur | Signification | Condition |
|:-------|:--------------|:----------|
| `groupe_1` | **Absent** — personne sur le réseau cible | ni Mamour ni Eric en WiFi cible |
| `groupe_2` | **Mamour seule** — Eric absent | Mamour en WiFi cible, Eric hors réseau |
| `groupe_3` | **Eric seul** — Mamour absente | Eric en WiFi cible, Mamour hors réseau |
| `groupe_4` | **Tous les deux** — présence simultanée | Mamour ET Eric en WiFi cible |

---

## sensor.presence — Affichage dashboard / en-tête notifications

Utilisé dans les messages : `{{ states('sensor.presence') }}`
Format : `[X: statut_X/statut_Y]` où statut = `WIFI` | `CELL` | `WIFI_!?`

| Valeur affichée | Situation |
|:----------------|:----------|
| `[2] en [WIFI]` | Les deux sur le réseau domestique |
| `[2] en [CELL]` | Les deux en cellulaire |
| `[2] en [WIFI_!?]` | Les deux en WiFi, mais sur un autre réseau |
| `[Mamour: WIFI/CELL]` | Mamour présente (domestique), Eric en cellulaire |
| `[Mamour: WIFI/WIFI_!?]` | Mamour présente (domestique), Eric sur autre WiFi |
| `[Eric: WIFI/CELL]` | Eric présent (domestique), Mamour en cellulaire |
| `[Eric: WIFI/WIFI_!?]` | Eric présent (domestique), Mamour sur autre WiFi |
| `[CELL / WIFI_!?]` | Aucun sur le domestique — Mamour=CELL, Eric=autre WiFi |
| `[WIFI_!? / CELL]` | Aucun sur le domestique — Mamour=autre WiFi, Eric=CELL |

> **Ordre d'affichage :** `[Eric: e_stat/m_stat]` → Eric en premier, Mamour en second.

---

## Légende des codes réseau

| Code | Signification |
|:-----|:--------------|
| `WIFI` | Connecté au réseau domestique (Beryl GG-5.0 ou GG-2.4) |
| `WIFI_!?` | Connecté à un autre WiFi (bureau, voisin, hotspot…) |
| `CELL` | Connexion cellulaire (4G/5G) — hors WiFi |
