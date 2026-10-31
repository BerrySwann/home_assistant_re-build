# SONOFF Z2M Migration — Status & Next Steps
**Date:** 2026-05-23  
**Mini-PC:** Proxmox 7.0.0-3  
**LXC 200:** Z2M (accessible http://10.32.154.244:8099)

---

## ⚙️ Détail du Matériel (Clés Zigbee)

| Matériel | Acquisition | Statut | Rôle |
|:---------|:------------|:-------|:-----|
| **Clé Sonoff V2 (Nouvelle)** | **22/05/2026** | **PROD** | Connectée au LXC 200 (Zigbee2MQTT) |
| Clé Sonoff (Ancienne) | 2024 | Archivée | Historique — début de l'aventure HA |

---

## ✅ RÉSOLU — Z2M Opérationnel & Stable (2026-05-23)

### Ce qui a été fait
| Étape | Statut | Détail |
|-------|--------|--------|
| SONOFF détecté (`lsusb`) | ✅ | ID `1a86:55d4` QinHeng SONOFF V2 (Modèle 2026) |
| Firmware vérifié | ✅ | EZSP 7.4.4 [GA] — EmberZNet (Dongle-E) |
| `/dev/ttyUSB0` visible sur host | ✅ | `crw-rw---- 188, 0` |
| Passthrough USB → LXC 200 | ✅ | Via `dev0:` + `lxc.mount.entry` + `lxc.cgroup2.devices.allow: c 188:* rwm` |
| `/dev/ttyUSB0` visible dans LXC | ✅ | `crw-rw---- 1 root root 188, 0` |
| Mosquitto installé & configuré | ✅ | Port 1883, auth `***` / `***` |
| Z2M `configuration.yaml` corrigé | ✅ | `onboarding: false`, `frontend.enabled: true` |
| **Instabilité Z2M résolue** | ✅ | **Correctifs appliqués avec Claude AI (Stabilité OK)** |
| Z2M démarré et stable | ✅ | `Zigbee2MQTT started!` sur port 8099 |
| Discovery MQTT vers HA | ✅ | Entités bridge publiées sur `homeassistant/#` |

---

## 🧪 Test d'appairage en cours

- [x] **Premier appareil Zigbee appairé** (Essai réussi avec nouvelle clé)
- [ ] **Tests de stabilité** (Ouin-ouin sous surveillance)
- [ ] **Re-appairage massif** de tous les anciens équipements

---

## 🔧 Configuration finale

### `/etc/pve/lxc/200.conf` (Proxmox host)
```ini
dev0: /dev/ttyUSB0
lxc.cgroup2.devices.allow: c 188:* rwm
lxc.mount.entry: /dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_V2_940fc42bf9c2ef11be72e6b08048b910-if00-port0 dev/ttyUSB0 none bind,optional,create=file
```

### `/opt/z2m/data/configuration.yaml` (LXC 200)
```yaml
version: 5
mqtt:
  base_topic: zigbee2mqtt
  server: mqtt://10.32.154.244:1883
  user: ***
  password: ***
serial:
  adapter: ember
  baudrate: 115200
  rtscts: false
  port: /dev/ttyUSB0
advanced:
  log_level: info
  channel: 25
  network_key: ***
  pan_id: ***
  ext_pan_id: ***
frontend:
  enabled: true
  port: 8099
homeassistant:
  enabled: true
onboarding: false
```

### `/etc/mosquitto/conf.d/z2m.conf` (LXC 200)
```
listener 1883
allow_anonymous false
password_file /etc/mosquitto/passwd
```

---

## 📋 Prochaines étapes

- [ ] **Continuer l'appairage** — UI Z2M : http://10.32.154.244:8099 → Permit join
- [ ] **Vérifier les entités dans HA** — S'assurer que les noms correspondent aux slugs canoniques (P3, etc.)
- [ ] **Valider la stabilité réseau** après 24h de fonctionnement

---

## 🛠️ Commandes utiles (LXC 200)

```bash
# Statut services
systemctl status zigbee2mqtt
systemctl status mosquitto

# Logs Z2M temps réel
journalctl -u zigbee2mqtt -f

# Redémarrage propre
systemctl restart mosquitto && systemctl restart zigbee2mqtt

# Vérifier dongle
ls -la /dev/ttyUSB0
```

---

## 📌 Key Files

| Fichier | Emplacement | Rôle |
|---------|-------------|------|
| Z2M config | `/opt/z2m/data/configuration.yaml` | Config principale Z2M |
| Mosquitto conf | `/etc/mosquitto/conf.d/z2m.conf` | Auth + port broker MQTT |
| Mosquitto passwd | `/etc/mosquitto/passwd` | Credentials MQTT |
| LXC config | `/etc/pve/lxc/200.conf` | Passthrough USB Proxmox |
| Z2M logs | `journalctl -u zigbee2mqtt` | Logs runtime |

---

## 🎯 Critères de succès — EN COURS 🟡

- [x] Discovery MQTT vers HA opérationnelle
- [x] Premier appareil Zigbee appairé (Nouvelle clé 2026)
- [ ] Tous les anciens appareils re-appairés
- [ ] Stabilité confirmée (aucun crash Z2M)
