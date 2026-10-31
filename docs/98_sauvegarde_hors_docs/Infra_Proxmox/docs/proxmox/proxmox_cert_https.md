# Proxmox - Certificat HTTPS Let's Encrypt (Cloudflare DNS)

**Date** : 2026-08-08  
**Probleme resolu** : Brave/Chrome affichait "Non securise" / `NET::ERR_CERT_AUTHORITY_INVALID` sur `https://10.32.154.240:8006`  
**Cause** : Le cert auto-signe Proxmox n'a pas de SAN (Subject Alternative Name) - requis par tous les navigateurs modernes depuis 2017.

---

## Solution retenue : ACME / Let's Encrypt via Cloudflare DNS challenge

Proxmox obtient un vrai cert Let's Encrypt pour `pve.erodi-ha.com` en prouvant la propriete du domaine via l'API Cloudflare (challenge DNS, pas HTTP - aucun port a ouvrir vers l'exterieur).

Acces Proxmox apres setup : `https://pve.erodi-ha.com:8006`

---

## Etape 1 - Token API Cloudflare

1. https://dash.cloudflare.com/profile/api-tokens
2. "Create Token" -> template "Edit zone DNS"
3. Zone resources : `Include > Specific zone > erodi-ha.com`
4. Generer et copier le token (affiche une seule fois)

---

## Etape 2 - Record DNS Cloudflare

DNS > Records > Add record :
- Type : `A`
- Name : `pve`
- IPv4 : `10.32.154.240`
- Proxy : **OFF** (nuage gris, DNS only)

Note : Cloudflare affiche "reserved IP" - c'est normal pour une IP privee, ca fonctionne.

---

## Etape 3 - Plugin ACME dans Proxmox

> Datacenter > ACME > onglet "Challenge Plugins" > Add

- Plugin ID : `cloudflare`
- DNS API : `Cloudflare Managed DNS`
- API Data : `CF_Token=TON_TOKEN`

---

## Etape 4 - Compte ACME dans Proxmox

> Datacenter > ACME > onglet "Accounts" > Add

- Name : `letsencrypt`
- Email : `erodi@free.fr`
- Directory : `Let's Encrypt V2` (production)
- Cliquer "Register"

---

## Etape 5 - Domaine sur le node

> pve (node) > System > Certificates > section ACME > Add

- Domain : `pve.erodi-ha.com`
- Challenge type : `DNS`
- Plugin : `cloudflare`

Puis cliquer le crayon a cote de "Using Account: None" et selectionner `letsencrypt`.

Enfin : **"Order Certificates Now"** - le processus prend ~1 minute, doit se terminer par `TASK OK`.

---

## Etape 6 - Fichier hosts Windows (requis a chaque reinstall Windows)

Cloudflare filtre les A records vers IP privees sur son resolver public (1.1.1.1) - le navigateur ne peut donc pas resoudre `pve.erodi-ha.com`.

Contournement : entree manuelle dans le fichier hosts local.

**PowerShell en administrateur :**
```powershell
Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "10.32.154.240    pve.erodi-ha.com"
```

Verifier :
```powershell
nslookup pve.erodi-ha.com
```
Doit retourner `10.32.154.240`.

---

## Renouvellement automatique

Let's Encrypt expire tous les 90 jours. Proxmox gere le renouvellement automatiquement via la tache ACME - rien a faire manuellement.

---

## Recap acces

| Avant | Apres |
|:------|:------|
| `https://10.32.154.240:8006` (Non securise) | `https://pve.erodi-ha.com:8006` (cadenas vert) |
