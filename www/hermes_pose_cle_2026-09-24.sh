#!/bin/bash
# hermes_pose_cle_2026-09-24.sh
# Pose la cle SSH du PC Windows (Hermes) sur le CT 200 (Z2M).
# But : retirer la modif auth_token du 21/09 dans /opt/z2m/data/configuration.yaml.
# Lancable soit sur l'hote Proxmox (root), soit directement dans le CT 200 (root).
set -e

KEY='ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINqDgVPHYemLBU+bEiZ2W9mQXnX/eFq39lXig8BjmWnr Berry Swann@Berry-Swann-System'
MARK='Berry Swann@Berry-Swann-System'

do_pose() {
  local P="$1"
  $P bash -c "mkdir -p /root/.ssh; touch /root/.ssh/authorized_keys; grep -qF '$MARK' /root/.ssh/authorized_keys || echo '$KEY' >> /root/.ssh/authorized_keys; chmod 700 /root/.ssh; chmod 600 /root/.ssh/authorized_keys; echo POSE_OK; echo -n 'cles presentes: '; grep -c . /root/.ssh/authorized_keys"
}

if command -v pct >/dev/null 2>&1; then
  echo "[hote PVE detecte] pose via pct exec 200"
  do_pose "pct exec 200 --"
else
  echo "[pas de pct ici] execution locale (CT 200 ?)"
  do_pose ""
fi
echo "FINI"
