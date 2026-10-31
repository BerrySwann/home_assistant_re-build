#!/bin/bash
set -e
echo "=== SETUP Z2M - PASSTHROUGH + CONFIG + SERVICE ==="

echo "--- 1. Check USB ---"
ls -la /dev/ttyUSB* 2>/dev/null || { echo "ERREUR: Aucun ttyUSB! Verifier branchement ZBT-1."; exit 1; }

echo "--- 2. Passthrough USB LXC 200 ---"
pct stop 200 2>/dev/null || true
sleep 2
grep -q "ttyUSB0" /etc/pve/lxc/200.conf && echo "[SKIP] Deja configure" || {
  echo "lxc.cgroup2.devices.allow: c 188:0 rwm" >> /etc/pve/lxc/200.conf
  echo "lxc.mount.entry: /dev/ttyUSB0 dev/ttyUSB0 none bind,optional,create=file" >> /etc/pve/lxc/200.conf
  echo "[OK] Passthrough ajoute"
}
pct start 200
sleep 4
pct exec 200 -- ls -la /dev/ttyUSB0 && echo "[OK] Device visible dans LXC" || echo "[WARN] Device pas visible"

echo "--- 3. Fix config Z2M ---"
pct exec 200 -- python3 -c "
content='''homeassistant:
  enabled: true
  legacy_entity_attributes: false
mqtt:
  server: mqtt://localhost:1883
serial:
  port: /dev/ttyUSB0
frontend:
  enabled: true
  port: 8080
permit_join: false
'''
open('/opt/zigbee2mqtt/data/configuration.yaml','w').write(content)
print('[OK] Config Z2M ecrite')
"

echo "--- 4. Fix service systemd ---"
pct exec 200 -- bash -c "printf '[Unit]\nDescription=Zigbee2MQTT\nAfter=network.target mosquitto.service\nRequires=mosquitto.service\n\n[Service]\nType=simple\nExecStart=/usr/bin/node /opt/zigbee2mqtt/index.js\nWorkingDirectory=/opt/zigbee2mqtt\nEnvironment=NODE_ENV=production\nStandardOutput=journal\nStandardError=journal\nRestart=on-failure\nRestartSec=5s\nUser=root\n\n[Install]\nWantedBy=multi-user.target\n' > /etc/systemd/system/zigbee2mqtt.service"
pct exec 200 -- systemctl daemon-reload
echo "[OK] Service corrige"

echo "--- 5. Start services ---"
pct exec 200 -- systemctl restart mosquitto
sleep 2
pct exec 200 -- systemctl restart zigbee2mqtt
sleep 6

echo "--- 6. Status final ---"
pct exec 200 -- systemctl is-active mosquitto && echo "[OK] Mosquitto UP" || echo "[KO] Mosquitto DOWN"
pct exec 200 -- systemctl is-active zigbee2mqtt && echo "[OK] Z2M UP" || echo "[KO] Z2M DOWN"
pct exec 200 -- journalctl -u zigbee2mqtt -n 20 --no-pager
echo "=== FIN ==="
