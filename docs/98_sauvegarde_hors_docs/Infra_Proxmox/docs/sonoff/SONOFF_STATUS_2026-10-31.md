# SONOFF / Z2M - Etat et configuration (mise a jour 2026-10-31)

**Date de mise a jour :** 2026-10-31
**Remplace pour la lecture :** `SONOFF_STATUS_2026-05-23.md` (mise a la corbeille le 2026-10-31 : trop ancienne, elle contenait identifiant, mot de passe MQTT et cle reseau Zigbee en clair).
**Secrets :** identifiant MQTT, mot de passe, `network_key`, `pan_id`, `ext_pan_id` et `auth_token` sont caviardes (`***`) dans ce fichier. Les valeurs reelles sont dans la configuration de Z2M, jamais ici.

---

## Provenance des informations
- **Etabli le 2026-10-31 (releve live)** : applications HA, integration MQTT, entites du bridge Z2M, ports ouverts depuis le PC.
- **Source sauvegarde Z2M du 2026-06-14** (version 2.10.1, fichier `z2m-backup.2.10.1...zip` a la racine de ReBuild) : contenu de `configuration.yaml`. Meme version que la version actuelle, donc la config est probablement inchangee, mais ce n'est pas verifie : le fichier vivant dans le LXC n'a pas ete lu.
- **Releve du 2026-05-23** (ancienne fiche) : materiel, passthrough USB, commandes. Non reverifie.

## Architecture actuelle
| Element | Etat | Source |
|:--|:--|:--|
| Z2M | version **2.10.1**, bridge connecte depuis le 2026-10-29 08:06, log level info, permit join off | HA, releve 2026-10-31 |
| Interface Z2M | `http://10.32.154.244:8099` repond (HTTP 200) | releve 2026-10-31 |
| Hote Z2M | LXC 200 sur Proxmox (10.32.154.240, interface 8006 joignable) | CLAUDE.md + releve 2026-10-31 |
| Broker MQTT utilise par HA | application **Mosquitto broker** (`core_mosquitto` 7.1.3, demarree), integration MQTT chargee, 10.32.154.243:1883 ouvert | HA, releve 2026-10-31 |
| Ancien Mosquitto du LXC 200 | le port 1883 de 10.32.154.244 repond encore ; usage actuel **inconnu** | releve 2026-10-31 |
| Cle Zigbee | Sonoff V2 (EFR32MG21, recue le 22/05/2026), adaptateur `ember` | CLAUDE.md, ancienne fiche |
| Appareils declares dans Z2M | **52** (au 2026-06-14) | sauvegarde 2026-06-14 |

## Ecarts par rapport a la fiche du 2026-05-23
- Le broker MQTT n'est plus le Mosquitto du LXC 200 : HA utilise l'application Mosquitto (10.32.154.243). La sauvegarde du 2026-06-14 pointe deja vers 10.32.154.243.
- `base_topic` : `zigbee2mqtt2` dans la sauvegarde (au lieu de `zigbee2mqtt`).
- `frontend.auth_token` present dans la sauvegarde (absent de la fiche de mai).
- Dans HA, deux jeux d'entites bridge : ceux avec suffixe `_2` sont actifs, ceux sans suffixe sont `unavailable` (anciens, a nettoyer si Eric confirme).

## Configuration Z2M (sauvegarde du 2026-06-14, secrets caviardes)
```yaml
version: 5
mqtt:
  base_topic: zigbee2mqtt2
  server: mqtt://10.32.154.243:1883
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
  auth_token: ***
homeassistant:
  enabled: true
onboarding: false
```

## Passthrough USB (`/etc/pve/lxc/200.conf`, releve du 2026-05-23, non reverifie)
```ini
dev0: /dev/ttyUSB0
lxc.cgroup2.devices.allow: c 188:* rwm
lxc.mount.entry: /dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_V2_940fc42bf9c2ef11be72e6b08048b910-if00-port0 dev/ttyUSB0 none bind,optional,create=file
```

## Commandes utiles (LXC 200)
```bash
systemctl status zigbee2mqtt
journalctl -u zigbee2mqtt -f
systemctl restart zigbee2mqtt
ls -la /dev/ttyUSB0
```

## Fichiers cles
| Fichier | Emplacement | Role |
|:--|:--|:--|
| Config Z2M | `/opt/z2m/data/configuration.yaml` (LXC 200) | Config principale Z2M |
| Sauvegarde Z2M | `z2m-backup.2.10.1.1781449845310.zip` (racine ReBuild, local seul, contient les secrets) | Config, base d'appareils, cle reseau |
| Application Mosquitto | HA, `core_mosquitto` | Broker MQTT actuel |
| Config LXC | `/etc/pve/lxc/200.conf` (Proxmox) | Passthrough USB |

## A verifier (non fait le 2026-10-31)
- Lire la `configuration.yaml` vivante du LXC 200 (acces SSH non utilise) pour confirmer broker, base_topic et canal.
- Dire si le Mosquitto du LXC 200 est encore utilise ou peut etre arrete.
- Nettoyer les entites bridge sans suffixe `_2` (unavailable).
- Firmware du dongle (EZSP 7.4.4 releve le 2026-05-23) : non reverifie.
