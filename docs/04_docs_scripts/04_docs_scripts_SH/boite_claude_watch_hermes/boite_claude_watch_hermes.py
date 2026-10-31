#!/usr/bin/env python
# Surveille la boite aux lettres Claude (D:\Discussion_Claude_Hermes).
# Sort un message seulement quand un fichier *_claude.md change ou apparait.
# Le message dit QUEL fichier a change, COMBIEN de lignes sont nouvelles et QUELS
# identifiants de messages sont concernes, avec un apercu. Sortie vide = rien a signaler.
# DIR et STATE peuvent etre forces par variable d'environnement (test hors boite reelle).
import os
import re
import json
import hashlib

DIR = os.environ.get("BOITE_CLAUDE_DIR", r"D:\Discussion_Claude_Hermes")
STATE = os.environ.get("BOITE_CLAUDE_STATE", r"D:\hermes\scripts\.boite_claude_state")
MAX_FILES = 4
PREVIEW = 260

ID = re.compile(r"\|\s*([ch]\d{8}-\d{2})\s*\|")


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_lines(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return [l.rstrip("\r\n") for l in f]
    except OSError:
        return []


def scan():
    out = {}
    try:
        names = sorted(os.listdir(DIR))
    except OSError:
        return None
    for n in names:
        if not n.endswith("_claude.md"):
            continue
        p = os.path.join(DIR, n)
        if os.path.isfile(p):
            out[n] = {"md5": md5_file(p), "lines": len(read_lines(p))}
    return out


def clean(t, limit=PREVIEW):
    t = "".join(c for c in t if 31 < ord(c) < 127 or c in " ")
    t = " ".join(t.split())
    return t[:limit] + (" ..." if len(t) > limit else "")


cur = scan()
if cur is None:
    raise SystemExit(0)

try:
    with open(STATE, encoding="utf-8") as f:
        raw = f.read().strip()
except OSError:
    raw = ""

prev = {}
if raw:
    try:
        prev = json.loads(raw)
    except ValueError:
        prev = {}
    if not isinstance(prev, dict) or any(not isinstance(v, dict) for v in prev.values()):
        prev = {}

if cur == prev:
    raise SystemExit(0)

with open(STATE, "w", encoding="utf-8") as f:
    json.dump(cur, f, sort_keys=True)

if not prev:
    raise SystemExit(0)

parts = []
for name in sorted(cur):
    now = cur[name]
    old = prev.get(name)
    if old == now:
        continue
    lines = read_lines(os.path.join(DIR, name))
    if old is None:
        news = lines
        entete = "%s : nouveau fichier, %d ligne(s)" % (name, len(news))
    else:
        n = max(0, int(now["lines"]) - int(old.get("lines", 0)))
        news = lines[len(lines) - n:] if n else lines[-1:]
        entete = "%s : %d nouvelle(s) ligne(s)" % (name, n if n else 1)
    ids = []
    for l in news:
        m = ID.search(l)
        if m:
            ids.append(m.group(1))
    apercu = ""
    for l in reversed(news):
        if l.strip() and not l.startswith("#") and "|" in l:
            apercu = clean(l)
            break
    bloc = entete
    if ids:
        bloc += " | id : " + ", ".join(ids[-4:])
    if apercu:
        bloc += " | " + apercu
    parts.append(bloc)
    if len(parts) >= MAX_FILES:
        break

if not parts:
    raise SystemExit(0)

print("Boite aux lettres Claude, changement detecte.")
for p in parts:
    print("- " + p)
print("A lire dans la session (instruction de Claude = decision d'Eric depuis le 2026-10-24).")
