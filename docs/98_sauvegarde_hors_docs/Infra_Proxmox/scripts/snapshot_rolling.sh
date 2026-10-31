#!/bin/bash
# =============================================================
# snapshot_rolling.sh — Snapshots automatiques roulants (3j)
# Proxmox host — /usr/local/bin/snapshot_rolling.sh
# VMs : 100 (HomeAssistant)
# LXC : 200 (z2m), 201 (mariadb)
# =============================================================

DATE=$(date +%Y%m%d)
KEEP=3
SNAP_PREFIX="auto"

log() { echo "[$(date '+%H:%M:%S')] $1"; }

# --- Snapshot VM 100 (HomeAssistant) ---
log "Snapshot VM 100..."
qm snapshot 100 "${SNAP_PREFIX}${DATE}" --description "Auto ${DATE}" 2>&1
if [ $? -eq 0 ]; then
    log "VM 100 OK"
else
    log "VM 100 ERREUR"
fi

# --- Snapshot LXC 200 (z2m) ---
log "Snapshot LXC 200..."
pct snapshot 200 "${SNAP_PREFIX}${DATE}" --description "Auto ${DATE}" 2>&1
if [ $? -eq 0 ]; then
    log "LXC 200 OK"
else
    log "LXC 200 ERREUR"
fi

# --- Snapshot LXC 201 (mariadb) ---
log "Snapshot LXC 201..."
pct snapshot 201 "${SNAP_PREFIX}${DATE}" --description "Auto ${DATE}" 2>&1
if [ $? -eq 0 ]; then
    log "LXC 201 OK"
else
    log "LXC 201 ERREUR"
fi

# --- Nettoyage : garder seulement les ${KEEP} derniers ---

# VM 100
OLD=$(qm listsnapshot 100 2>/dev/null \
    | awk '{print $2}' \
    | grep "^${SNAP_PREFIX}[0-9]" \
    | sort \
    | head -n -${KEEP})
for SNAP in $OLD; do
    log "Suppression VM 100 -> $SNAP"
    qm delsnapshot 100 "$SNAP"
done

# LXC 200
OLD=$(pct listsnapshot 200 2>/dev/null \
    | awk '{print $2}' \
    | grep "^${SNAP_PREFIX}[0-9]" \
    | sort \
    | head -n -${KEEP})
for SNAP in $OLD; do
    log "Suppression LXC 200 -> $SNAP"
    pct delsnapshot 200 "$SNAP"
done

# LXC 201
OLD=$(pct listsnapshot 201 2>/dev/null \
    | awk '{print $2}' \
    | grep "^${SNAP_PREFIX}[0-9]" \
    | sort \
    | head -n -${KEEP})
for SNAP in $OLD; do
    log "Suppression LXC 201 -> $SNAP"
    pct delsnapshot 201 "$SNAP"
done

log "Terminé."
