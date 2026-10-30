<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Technique-607d8b?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Sujet** | Pont Philips Hue - blocage de Hue Sync (Ambilight) |
| 🖥️ **Pont** | `10.32.154.206` (Hue Bridge, modèle BSB002) |
| 🔧 **Firmware** | `1978418030` |
| 🔑 **API user** | `hermes#pc` = `<HUE_BRIDGE_KEY>` (valeur : variable d'environnement utilisateur Windows `HUE_BRIDGE_KEY`, jamais dans ce fichier ; PowerShell `$env:HUE_BRIDGE_KEY`, bash `$HUE_BRIDGE_KEY`) |
| 📅 **Modifié le** | 2026-10-11 |

---

# 🌉 PONT HUE - BLOCAGE DE HUE SYNC (AMBILIGHT)

> **Problème** : Hue Sync (Ambilight sur les 3 Hue Play du bureau) pilote le groupe Entertainment "Moniteur PC" et entre en conflit avec Home Assistant. Quand Sync est actif, il prend l'exclusivité des lampes.
>
> **Solution** : désactiver le stream du groupe 4 (`active: false`). Les lampes restent pilotables par HA. Pour bloquer définitivement, supprimer les entrées Hue Sync de la whitelist.

---

## 🔌 INFORMATIONS DU PONT

| Champ | Valeur |
|:------|:-------|
| IP | `10.32.154.206` |
| Modèle | BSB002 (Hue Bridge v2, rond) |
| MAC | `ec:b5:fa:2c:b3:bc` |
| Firmware | `1978418030` |
| Nom | Hue Bridge |
| Lumières | 22 |
| Groupes | 15 |

### Création d'un accès API (une seule fois)

> Bouton physique requis : appuyer sur le bouton rond du pont, puis exécuter dans les 30 secondes.

```bash
curl -X POST http://10.32.154.206/api \
  -H "Content-Type: application/json" \
  -d '{"devicetype":"hermes#pc"}'
```

Réponse : `{"success":{"username":"<HUE_BRIDGE_KEY>"}}`

---

## 🎮 GROUPE ENTERTAINMENT "MONITEUR PC"

| Champ | Valeur |
|:------|:-------|
| Group ID | `4` |
| Nom | Moniteur PC |
| Type | Entertainment |
| Lumières | `26` (Hue Play 3 PC Bureau), `23` (Hue Play 2 PC Bureau), `10` (Hue Play 1 PC Bureau) |
| Modèle lampes | Extended color light (Hue Play) |

> Le groupe 13 "Moniteur PC" (type Zone) contient les mêmes lampes mais n'a pas de stream.

---

## 🔧 COMMANDES

### Couper Hue Sync (libérer les lampes pour HA)

```bash
curl -X PUT "http://10.32.154.206/api/<HUE_BRIDGE_KEY>/groups/4" \
  -H "Content-Type: application/json" \
  -d '{"stream":{"active":false}}'
```

Vérification :

```bash
curl "http://10.32.154.206/api/<HUE_BRIDGE_KEY>/groups/4" \
  | python -c "import sys,json; d=json.load(sys.stdin); print(d['stream'])"
```

Résultat attendu : `{'proxymode': 'auto', 'proxynode': '/bridge', 'active': False, 'owner': None}`

### Réactiver Hue Sync (remettre l'Ambilight)

```bash
curl -X PUT "http://10.32.154.206/api/<HUE_BRIDGE_KEY>/groups/4" \
  -H "Content-Type: application/json" \
  -d '{"stream":{"active":true}}'
```

Vérification :

```bash
curl "http://10.32.154.206/api/<HUE_BRIDGE_KEY>/groups/4" \
  | python -c "import sys,json; d=json.load(sys.stdin); print(d['stream'])"
```

Résultat attendu : `{'proxymode': 'auto', 'proxynode': '/bridge', 'active': True, 'owner': '055359f7-...'}`

---

## 📋 RÉSUMÉ

| Action | Commande |
|:-------|:---------|
| Couper Sync | `PUT /api/{user}/groups/4` + `{"stream":{"active":false}}` |
| Remettre Sync | `PUT /api/{user}/groups/4` + `{"stream":{"active":true}}` |

**Effet** : les lampes restent allumables/éteignables par HA, mais Hue Sync ne peut plus les piloter en Ambilight tant que `active=false`.

---

## 🚫 BLOCAGE DÉFINITIF DE HUE SYNC

> ⚠️ **Attention** : si Hue Sync tourne et que quelqu'un clique "Démarrer la synchro", il remet `active=true` tout seul. Pour bloquer définitivement, il faut supprimer ses entrées de la whitelist.

### Whitelist actuelle (45 entrées, 2026-10-11)

| Type | Nombre | Exemples |
|:-----|:-------|:---------|
| Hue Sync | 14 | `Hue Sync#BERRY-SWANN-SYS` (actif, owner du stream), `Hue Sync#BERRY-SWANN-WIN`, `Hue Sync#ERODIWIN11SYSTE`, `Hue Sync#DESKTOP-*`, `Hue Sync#ERODI-WIN10-SYS` |
| home-assistant | 4 | `home-assistant#maison` |
| Hue (app mobile) | 8 | `Hue#NE2213`, `Hue#GM1900`, `Hue#GM1901`, `Hue#2412DPC0AG` |
| stream_deck | 7 | `stream_deck` |
| Alexa | 1 | `hue-alexa-smarthome-skill-v1` |
| Google | 1 | `hue-hca-actions-on-google` |
| Her practice | 1 | `hermes#pc` |
| Usine | 1 | `starterkit-setup#factory` |

### Supprimer une entrée whitelist

```bash
curl -X DELETE "http://10.32.154.206/api/<HUE_BRIDGE_KEY>/config/whitelist/055359f7-..."
```

> L'ID `055359f7-...` est l'owner actuel du stream (Hue Sync#BERRY-SWANN-SYS). Les autres entrées Hue Sync ont des IDs différents, à relever via `GET /api/{user}` (section `config.whitelist`).

### Conséquence

Après suppression, Hue Sync ne pourra plus s'authentifier ni reprendre le stream. Il faudra recréer un accès API (bouton physique) pour le réactiver.

---

## 📝 NOTES

- Le stream actif appartient à `Hue Sync#BERRY-SWANN-SYS` (dernière utilisation : 2026-10-11 15:51).
- L'entrée `hermes#pc` a été créée le 2026-10-11 (bouton physique).
- Les entrées `Hue Sync#ERODI-WIN10-SYS` et `Hue Sync#DESKTOP-*` datent de 2021-2024 : nettoyage possible.
