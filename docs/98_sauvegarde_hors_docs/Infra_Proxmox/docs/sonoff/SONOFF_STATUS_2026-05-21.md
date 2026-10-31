# SONOFF Z2M Migration — Status & Next Steps
**Date:** 2026-05-21  
**Mini-PC:** Proxmox 7.0.0-3  
**LXC 200:** Z2M (accessible http://10.32.154.244:8099)

---

## 🔴 Current Issue: SONOFF Not Mapped to /dev/ttyUSB*

### Hardware Status
✅ SONOFF **physically detected** in lsusb:
```
Bus 001 Device 003: ID 1a86:55d4 QinHeng Electronics SONOFF Zigbee 3.0 USB Dongle Plus V2
```

❌ SONOFF **NOT visible** as `/dev/ttyUSB*` or `/dev/ttyACM*` on host or in LXC 200:
```bash
ls -la /dev/ttyUSB*  # No such file or directory
ls -la /dev/ttyACM*  # No such file or directory
```

### Root Cause
**Proxmox kernel 7.0.0-3 missing CH340 driver** (SONOFF uses QinHeng CH340 chipset):
```bash
modprobe ch340  # Module ch340 not found in directory /lib/modules/7.0.0-3-pve
```

### What's Ready
✅ Snapshots fixed & automated (2h daily)  
✅ LXC 200 created & Z2M running  
✅ Script `setup_z2m.sh` ready (in C:\Users\Berry Swann\Documents\HA\ReBuild\Promox\)  
❌ USB passthrough not configured yet (depends on device visibility)

---

## 📋 Tomorrow's Action Plan

### Step 1: Verify Physical Connection
- [ ] Physically reseat SONOFF USB cable on Mini-PC
- [ ] Ensure it's fully plugged in and lit (if has LED)
- [ ] Wait 5 seconds
- [ ] Run: `lsusb | grep QinHeng`
- **If seen:** Continue to Step 2
- **If NOT seen:** Check cable/USB port health

### Step 2: Identify Device Port
```bash
# Check which /dev/ttyUSB* or /dev/ttyACM* appears
ls -la /dev/ttyUSB*
ls -la /dev/ttyACM*

# Or check kernel messages
dmesg | tail -20
```

**Note:** If still not visible, may need to:
- Compile CH340 driver for kernel 7.0.0-3
- OR reboot Proxmox (drastic but may load drivers)
- OR use different USB port on Mini-PC

### Step 3: Adapt setup_z2m.sh
**Current script hardcoded to `/dev/ttyUSB0`**
- If SONOFF is `/dev/ttyUSB1`, edit lines in script:
  - Line 6: Change `ttyUSB0` → `ttyUSB1`
  - Line 13: Change `/dev/ttyUSB0` → `/dev/ttyUSB1`
  - Line 28: In config.yaml, change port accordingly

### Step 4: Execute Setup
```bash
cd /usr/local/bin
# Review adapted script first
cat setup_z2m.sh | head -30

# Execute
./setup_z2m.sh
```

Expected output:
```
[OK] Passthrough added
[OK] Config Z2M ecrite
[OK] Service corrige
[OK] Mosquitto UP
[OK] Z2M UP
```

### Step 5: Re-pair Devices
1. Start with **IKEA TRADFRI button** (OTA test target)
2. Log into Z2M UI (http://10.32.154.244:8080)
3. Enable pairing mode
4. Press TRADFRI button pairing combo
5. Verify in Z2M
6. Test OTA update

---

## 🛠️ Troubleshooting Checklist

| Issue | Check |
|-------|-------|
| `/dev/ttyUSB*` still missing | Check kernel modules: `lsmod \| grep ch340` |
| Z2M can't connect to device | Verify passthrough with: `pct exec 200 -- ls -la /dev/ttyUSB0` |
| Mosquitto won't start | Check logs: `journalctl -u mosquitto -n 20` |
| Z2M service won't start | Check logs: `journalctl -u zigbee2mqtt -n 20` |
| OTA still fails on device | May need to restart Z2M or reload device in UI |

---

## 📌 Key Files

| File | Location | Purpose |
|------|----------|---------|
| setup_z2m.sh | `/usr/local/bin/` (on Proxmox) | Automated Z2M+Mosquitto setup |
| setup_z2m.sh | `C:\Users\Berry Swann\Documents\HA\ReBuild\Promox\` | Local backup/reference copy |
| Z2M config | `/opt/zigbee2mqtt/data/configuration.yaml` | Z2M settings (auto-generated) |
| Snapshot log | `/var/log/snapshot_rolling.log` | Daily backup activity |
| Z2M logs | `journalctl -u zigbee2mqtt` | Z2M runtime logs |

---

## 🎯 Success Criteria

- [ ] SONOFF mapped to `/dev/ttyUSB*` or `/dev/ttyACM*`
- [ ] Passthrough configured (device visible inside LXC 200)
- [ ] Mosquitto running inside LXC 200
- [ ] Z2M service running and accessible
- [ ] At least one device (TRADFRI) re-paired
- [ ] OTA update test successful

