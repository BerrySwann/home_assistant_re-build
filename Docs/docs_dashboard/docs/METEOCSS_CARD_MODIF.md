# ⚠️ MODIFICATION MANUELLE — meteocss-card.js

---

## 🚨 WARNING — MISE À JOUR HACS

> **Si HACS met à jour `meteocss-card`, le fichier JS sera écrasé.**
> **Les couleurs personnalisées seront PERDUES.**
> **Refaire la manipulation ci-dessous immédiatement après toute mise à jour.**

---

## 📋 CONTEXTE

La carte `custom:meteo-card` (Pulpyyyy / meteocss-card) a ses palettes de couleurs
**codées en dur dans le fichier JS**, et non dans `meteo_settings.jinja`.

Les couleurs d'origine pour `sunset` et `sunrise` étaient très saturées / agressives
(rouge sang `#F30000`, bordeaux `#5D0000`, jaune fluo `#ECFF00`).

Elles ont été remplacées par une palette méditerranéenne douce (pêche, mauve, violet, bleu nuit).

---

## 📂 FICHIER CONCERNÉ

```
/config/www/community/meteocss-card/meteocss-card.js
(via Samba : H:\www\community\meteocss-card\meteocss-card.js)
```

Backup de l'original conservé :
```
H:\www\community\meteocss-card\meteocss-card.js.ORIGINAL
```

---

## 🎨 COULEURS MODIFIÉES

### sunset (coucher de soleil)

| Avant (original Pulpyyyy) | Après (custom) |
|:--------------------------|:---------------|
| `#FEFEFFCC 0%` | `#FFFAF2 0%` |
| `#ECFF00 10%` | `#FFE898 12%` |
| `#FD3229 25%` | `#FFBA72 26%` |
| `#F30000 45%` | `#FF9272 40%` |
| `#5D0000 75%` | `#D06880 56%` |
| `#001A33 100%` | `#5A2878 74%` |
| *(absent)* | `#0e1a4e 100%` |

**Résultat :** blanc crème → doré → pêche → saumoné → rose mauve → violet → bleu nuit

---

### sunrise (lever de soleil)

| Avant (original Pulpyyyy) | Après (custom) |
|:--------------------------|:---------------|
| `#FFF5C3 0%` | `#FFF8E0 0%` |
| `#FFD966 10%` | `#FFE080 15%` |
| `#FFA64D 30%` | `#FFB060 30%` |
| `#FF7F50 50%` | `#FF8060 48%` |
| `#5D0000 80%` | `#C85060 66%` |
| `#002340 100%` | `#502040 82%` |
| *(absent)* | `#100818 100%` |

**Résultat :** blanc chaud → doré → ambre → corail → rose foncé → bordeaux doux → nuit

---

## 🔧 PROCÉDURE DE RE-APPLICATION (après maj HACS)

```powershell
# 1. Ouvrir PowerShell sur Windows

# 2. Lire et modifier le fichier
$content = Get-Content "H:\www\community\meteocss-card\meteocss-card.js" -Raw -Encoding UTF8

# 3. Remplacer sunset (chercher la ligne sunset dans le JS et remplacer par :)
#    '#FFFAF2 0%, #FFE898 12%, #FFBA72 26%, #FF9272 40%, #D06880 56%, #5A2878 74%, #0e1a4e 100%'

# 4. Remplacer sunrise (chercher la ligne sunrise dans le JS et remplacer par :)
#    '#FFF8E0 0%, #FFE080 15%, #FFB060 30%, #FF8060 48%, #C85060 66%, #502040 82%, #100818 100%'

# 5. Supprimer le .gz
Remove-Item "H:\www\community\meteocss-card\meteocss-card.js.gz" -Force

# 6. Vider le cache navigateur HA (F5 ou Ctrl+Shift+R)
```

---

## ✅ VÉRIFICATION

Après modification, chercher dans le JS :
- `FFFAF2` → doit être présent (sunset)
- `FFF8E0` → doit être présent (sunrise)

---

*Modifié le : 2026-06-24*
*Par : Eric (via Cowork/Claude)*
