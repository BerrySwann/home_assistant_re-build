#!/usr/bin/env python3
"""
correct_linky.py - Rattrapage TOUTES lignes MANQUANT dans linky_histo.txt

Appele par shell_command.correct_linky_log (automation rattrapage_linky_ecart).
Argument : JSON string contenant les jours Linky disponibles
  Format : '[{"date": "28/08", "val": 14.37}, {"date": "27/08", "val": 12.5}]'
  - Seuls les jours avec val > 0 sont passes (filtres dans l'automation).
  - Couvre day_1 a day_7 de l'entite Linky.

Actions pour chaque entree du JSON :
  1. Cherche la ligne "(MANQUANT)" pour cette date dans linky_histo.txt.
     - Si trouvee : remplace par la valeur reelle avec "(RATTRAPÉ)".
     - Si absente : passe au suivant (cas normal - Linky etait deja disponible).
  2. Lit nodon_histo.txt pour la valeur Nodon du meme jour.
  3. Calcule l'ecart et l'ajoute dans ecart_histo.txt avec "(RATTRAPÉ)".

Fichiers :
  - /config/notifs/linky_histo.txt  (lecture + ecriture)
  - /config/notifs/nodon_histo.txt  (lecture seule)
  - /config/notifs/ecart_histo.txt  (append)
"""

import sys
import json

LINKY_HISTO = "/config/notifs/linky_histo.txt"
NODON_HISTO = "/config/notifs/nodon_histo.txt"
ECART_HISTO = "/config/notifs/ecart_histo.txt"


def load_nodon_values() -> dict:
    """Charge toutes les valeurs Nodon depuis nodon_histo.txt.
    Retourne un dict {date_fr: kwh} ex: {"28/08": 13.45}."""
    result = {}
    try:
        with open(NODON_HISTO, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or "| Nodon :" not in line:
                    continue
                try:
                    date_fr = line.split(" | ")[0].strip()
                    nodon_str = line.split("Nodon : ")[1].split(" kWh")[0].strip()
                    result[date_fr] = float(nodon_str)
                except (IndexError, ValueError):
                    pass
    except FileNotFoundError:
        print(f"[WARN] {NODON_HISTO} introuvable - ecarts non calcules")
    return result


def correct_all(data: list) -> None:
    if not data:
        print("[INFO] Aucune donnee Linky recue - rien a faire")
        return

    # Lire linky_histo.txt une seule fois
    try:
        with open(LINKY_HISTO, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[ERREUR] {LINKY_HISTO} introuvable")
        sys.exit(1)

    # Construire index des jours a corriger : {date_fr: kwh}
    corrections = {str(entry["date"]): float(entry["val"]) for entry in data}

    # Charger les valeurs Nodon une seule fois
    nodon_map = load_nodon_values()

    # Scanner et corriger linky_histo.txt
    new_lines = []
    corrected = []  # liste des dates effectivement corrigees

    for line in lines:
        matched = False
        for date_fr, linky_kwh in corrections.items():
            pattern = f"{date_fr} | Linky : 0.00 kWh (MANQUANT)"
            if pattern in line:
                replacement = f"{date_fr} | Linky : {linky_kwh:.2f} kWh (RATTRAPÉ)"
                new_lines.append(line.replace(pattern, replacement))
                corrected.append((date_fr, linky_kwh))
                matched = True
                break
        if not matched:
            new_lines.append(line)

    if not corrected:
        print("[INFO] Aucune ligne MANQUANT trouvee - rien a corriger")
        return

    # Ecrire linky_histo.txt corrige
    with open(LINKY_HISTO, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    # Appender les ecarts dans ecart_histo.txt
    ecart_lines = []
    for date_fr, linky_kwh in corrected:
        print(f"[OK] Corrige {date_fr} : {linky_kwh:.2f} kWh (RATTRAPÉ)")
        nodon_kwh = nodon_map.get(date_fr)
        if nodon_kwh is None:
            print(f"[WARN] Nodon introuvable pour {date_fr} - ecart non calcule")
            continue
        ecart_kwh = round(linky_kwh - nodon_kwh, 2)
        ecart_pct = round((ecart_kwh / linky_kwh) * 100, 1) if linky_kwh > 0 else 0.0
        ecart_line = (
            f"{date_fr} | Linky: {linky_kwh:.2f} kWh | Nodon: {nodon_kwh:.2f} kWh"
            f" | Ecart: {ecart_kwh} ({ecart_pct}%) (RATTRAPÉ)\n"
        )
        ecart_lines.append(ecart_line)
        print(f"[OK] Ecart loggue : {ecart_line.strip()}")

    if ecart_lines:
        with open(ECART_HISTO, "a", encoding="utf-8") as f:
            f.writelines(ecart_lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: correct_linky.py '<json>'")
        print('Ex:    correct_linky.py \'[{"date": "28/08", "val": 14.37}]\'')
        sys.exit(1)

    try:
        data = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"[ERREUR] JSON invalide : {e}")
        print(f"Recu : {sys.argv[1]}")
        sys.exit(1)

    if not isinstance(data, list):
        print(f"[ERREUR] JSON attendu : liste, recu : {type(data)}")
        sys.exit(1)

    correct_all(data)
