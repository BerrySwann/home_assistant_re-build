# 🌐 PLAN RÉSEAU — 10.32.154.x
*Dernière mise à jour : 2026-09-24*

---

## 📋 RÉSUMÉ DES PLAGES

| Plage | Catégorie | Nb |
|:------|:----------|:--:|
| `10.32.154.11x` | PCs fixes | 3 |
| `10.32.154.20x` | IoT / Média / Domotique | 6 |
| `10.32.154.22x` | Smartphones / Portables | 4 |
| `10.32.154.23x` | Clim / Chauffage RM4-Mini | 4 |
| `10.32.154.24x` | Proxmox HOST + Infra | 7 |

---

## 🖥️ 10.32.154.11x — PCs FIXES

| IP | MAC | Description |
|:---|:----|:------------|
| `10.32.154.110` | `B4:2E:99:44:44:A1` | PC ERIC |
| `10.32.154.111` | `B4:2E:99:44:44:72` | PC Mamour |
| `10.32.154.112` | `C8:60:00:74:84:E2` | PC LINUXMINT |

---

## 📺 10.32.154.20x — IoT / MÉDIA / DOMOTIQUE

| IP | MAC | Description |
|:---|:----|:------------|
| `10.32.154.201` | `10:09:F9:5A:54:BF` | Amazon Fire TV |
| `10.32.154.202` | `68:07:0A:96:B6:4B` | TV Chambre |
| `10.32.154.203` | `48:E1:E9:DC:64:01` | Store Salon |
| `10.32.154.204` | `48:E1:E9:DC:5A:17` | Store Bureau |
| `10.32.154.205` | `74:38:B7:2D:A7:FA` | Imprimante Canon |
| `10.32.154.206` | `EC:B5:FA:2C:B3:BC` | Hue Bridge |

---

## 📱 10.32.154.22x — SMARTPHONES / PORTABLES

| IP | MAC | Description |
|:---|:----|:------------|
| `10.32.154.221` | `32:89:FE:15:C6:B9` | POCO-X7-Pro [E] — MAC 1 (Wi-Fi) |
| `10.32.154.222` | `A2:6E:FE:6A:93:2D` | POCO-X7-Pro [E] — MAC 2 (aléatoire) |
| `10.32.154.223` | `AE:42:65:CF:38:29` | OnePlus-10-Pro-5G — MAC 1 |
| `10.32.154.224` | `B2:67:82:8E:4B:74` | OnePlus-10-Pro-5G — MAC 2 |

> **Note :** Les doubles MAC par appareil sont dues aux adresses MAC aléatoires (privacy MAC).
> Fixer l'adresse MAC sur chaque téléphone si les deux entrées DHCP posent problème.

---

## ❄️ 10.32.154.23x — CLIM / CHAUFFAGE RM4-Mini (Broadlink)

| IP | MAC | Description |
|:---|:----|:------------|
| `10.32.154.231` | `E8:70:72:DE:91:B8` | Clim Salon RM4-Mini |
| `10.32.154.232` | `E8:70:72:AB:B9:C9` | Clim Bureau RM4-Mini |
| `10.32.154.233` | `E8:70:72:BA:65:56` | Clim Chambre RM4-Mini |
| `10.32.154.234` | `E8:70:72:AB:B9:B3` | Soufflant SdB RM4-Mini |

> **Intégration HA :** SmartIR via Broadlink. Entités : `climate.clim_salon`, `climate.clim_bureau`, `climate.clim_chambre`, `switch.soufflant_sdb`.

---

## 🖧 10.32.154.24x — PROXMOX HOST + INFRASTRUCTURE

| IP | VMID | Description | Type | Status |
|:---|:-----|:------------|:-----|:-------|
| `10.32.154.240` | HOST | Proxmox HOST (hyperviseur) + cloudflared | Physique | running |
| `10.32.154.241` | -    | Raspberry Pi (rebuild — éteint) | Physique | off |
| `10.32.154.242` | CT 201 | mariadb | CT (LXC) | running |
| `10.32.154.243` | VM 100 | homeassistant | VM (KVM) | running |
| `10.32.154.244` | CT 200 | z2m (Zigbee2MQTT + Mosquitto) | CT (LXC) | running |
| `10.32.154.245` | CT 202 | myelectricaldata | CT (LXC) | running |
| `10.32.154.246` | CT 501 | searxng | CT (LXC) | running |

> **Note RPi (.241) :** Raspberry Pi 4 utilisé pour la phase proto "aide a la personne". Actuellement éteint. Conserver la réservation DHCP.
> **Note Cloudflared :** Tourne en **service systemd** directement sur le HOST Proxmox (.240). CT dédié non créé - architecture simplifiée retenue.
> **Note 2026-09-20 — Add-on HA = vestige :** l'add-on *Cloudflared* de Home Assistant avait perdu son certificat → boucle de relance (watchdog toutes les ~9 min, ne servait aucun trafic). **Arrêté proprement (stop + watchdog off)** le 2026-09-20. **Ne pas le relancer** : le tunnel actif est celui du host (.240) ; un second tunnel créerait un conflit de routes DNS. (Il retentera une fois à chaque gros redémarrage tant qu'il reste en « démarrer au boot ».)
> **Note CT 501 (.246) :** SearXNG installé 2026-08-20. IP réelle : `10.32.154.246` (vérifiée le 2026-09-24 : config net0 PVE + port 8888 ouvert) - l'IP .251 précédemment documentée n'est plus active. Nesting=1 active (requis Debian 12 + systemd 252).

---

## 🔐 STRATÉGIE SSL — Cloudflare Tunnel (Cloudflared)

### Objectif
Accès HTTPS sans avertissement à tous les services locaux — sans ouvrir de port sur le routeur, sans gérer de certificat.

### Architecture cible

```
Internet
     │
     ▼
Cloudflare Edge  ←── Certificat géré automatiquement par Cloudflare
     │
     ▼
cloudflared (systemd sur pve host 10.32.154.240)  ←── Tunnel chiffré sortant
     │
     └──▶ erodi-ha.com → 10.32.154.243:8123  (HA VM)  ✅ OPÉRATIONNEL
```

> **Avantages vs NPM+DuckDNS :** zéro port ouvert, zéro cert à gérer, zéro renouvellement, fonctionne même sans IP publique fixe.
> **État :** Tunnel actif depuis 2026-05-08. Testé et confirmé depuis 4G. cloudflared installé sur le host (pas de CT dédié). Re-vérifié le 2026-09-20 (HA + z2m servis, après redémarrage du host).

### Étapes de mise en place

#### 1. Prérequis — Domaine sur Cloudflare
- Domaine : **`erodi-ha.com`** (ou autre domaine géré dans Cloudflare)
- DNS du domaine doit être délégué à Cloudflare (nameservers Cloudflare)

#### 2. Installation cloudflared sur le host Proxmox ✅ FAIT
```bash
# Installé directement sur pve host (pas de CT dédié)
# Service systemd actif : cloudflared.service
# Tunnel nommé : proxmox-home (ou similaire)
```

#### 3. Cloudflare Dashboard — Route configurée ✅ FAIT
| Subdomain | Domain | Service | État |
|:----------|:-------|:--------|:-----|
| *(root)* | `erodi-ha.com` | `http://10.32.154.243:8123` | ✅ Actif |

#### 4. HA — configuration.yaml ✅ FAIT
```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
    - 172.30.33.0/24   # Tailscale add-on
    - 172.30.0.0/16    # HA add-ons
    - 10.32.154.0/24   # Réseau local Proxmox (couvre cloudflared sur .240)
  ip_ban_enabled: true
  login_attempts_threshold: 3
```

## 🗑️ ANCIENNES IPs — À SUPPRIMER DU DHCP

| Ancienne IP | MAC | Était | Remplacée par |
|:------------|:----|:------|:--------------|
| `10.32.154.106` | `D8:3A:DD:FB:F3:22` | HA_RE-BUILD (RPi) | `.241` |
| `10.32.154.113` | `C8:60:00:74:84:E2` | PC LINUXMINT | `.112` |
| `10.32.154.166` | `BC:24:11:63:6A:92` | z2m | `.244` |
| `10.32.154.196` | `68:1D:EF:4D:BD:6C` | Proxmox HOST | `.240` |
| `10.32.154.211` | `EC:B5:FA:2C:B3:BC` | Hue Bridge | `.206` |
| `10.32.154.225` | `BC:24:11:93:5D:02` | homeassistant | `.243` |
| `10.32.154.201` | `BC:24:11:52:B2:59` | mariadb (ancienne IP Proxmox config) | `.242` ✅ |
| `10.32.154.245` | *(CT supprimé)* | NPM — Nginx Proxy Manager | **SUPPRIMÉ** ✅ |

> **Procédure :** Modifier chaque réservation DHCP dans l'interface routeur, puis redémarrer l'appareil concerné pour qu'il prenne la nouvelle IP.

---

## ⚠️ IMPACTS SUR HOME ASSISTANT

Après migration des IPs Proxmox, mettre à jour dans HA :

| Fichier / Entrée | Ancienne valeur | Nouvelle valeur |
|:-----------------|:----------------|:----------------|
| `configuration.yaml` → `trusted_proxies` | *(aucun)* | *(obsolète : le CT Cloudflared n'a jamais été créé - `.246` est aujourd'hui le CT 501 searxng)* |
| MyElectricalData `config.yaml` → `ha_url` | `http://10.32.154.225:8123` | `http://10.32.154.243:8123` |
| Z2M `configuration.yaml` → `mqtt.server` | `mqtt://10.32.154.225` | `mqtt://10.32.154.243` |
| Tout fichier YAML référençant `.225` | `.225` | `.243` |
> **Note 2026-09-24 :** section historique (migration terminée de longue date). Le CT Cloudflared n'a jamais été créé (cloudflared tourne sur le host), et `.246` est aujourd'hui l'IP du CT 501 searxng (cf. section 24x).

---

*Généré avec Cowork — HA ReBuild 2026-05-06*
