#!/usr/bin/env python
"""Renommage trace de chemins/noms dans un arbre, avec lookbehind et rapport.

Usage :
    python renomme_chemins_trace.py paires.json --root D:\\hermes --dry
    python renomme_chemins_trace.py paires.json --root D:\\hermes

paires.json : [["ancien", "nouveau"], ...] . Les paires sont triees par longueur
DE SCROISSANTE de l'ancien (variantes longues d'abord). Si le nouveau nom
commence par un prefixe + l'ancien (04_docs_scripts_SH vs docs_scripts_SH), un
lookbehind negatif est pose automatiquement pour ne pas re-prefixer.

Ecrit un .bak horodate par fichier modifie, imprime une ligne par fichier
(chemin | avant= | apres= | comptes) et depose le meme contenu dans un rapport.
Ne touche pas aux .bak, .pyc, ni aux dossiers de cache/sessions.
"""
import os, re, sys, json, hashlib, shutil, datetime

SKIP_DIRS = {".git", ".curator_backups", "__pycache__", "sessions", "composer-pastes",
             "cache", "logs", "node_modules", "venv", ".venv", ".archive", "cron"}
SKIP_FILE = re.compile(r"\.bak_|\.bak$|\.pyc$")
EXTS = {".md", ".py", ".txt", ".yaml", ".yml", ".json", ".sh", ".ps1", ".vbs", ".bat"}


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build(pairs):
    rules = []
    for old, new in sorted(pairs, key=lambda p: -len(p[0])):
        prefix = new[: len(new) - len(old)] if new.endswith(old) else ""
        pat = r"(?<!%s)%s" % (re.escape(prefix), re.escape(old)) if prefix else re.escape(old)
        rules.append((re.compile(pat), new, old))
    return rules


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    pairs = json.load(open(sys.argv[1], encoding="utf-8"))
    root = sys.argv[sys.argv.index("--root") + 1] if "--root" in sys.argv else os.getcwd()
    dry = "--dry" in sys.argv
    stamp = datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss")
    rules = build(pairs)
    rows = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if SKIP_FILE.search(fn) or os.path.splitext(fn)[1].lower() not in EXTS:
                continue
            p = os.path.join(base, fn)
            try:
                with open(p, encoding="utf-8", newline="") as f:
                    src = f.read()
            except (UnicodeDecodeError, OSError):
                continue
            text, counts = src, {}
            for rx, new, old in rules:
                text, n = rx.subn(new, text)
                if n:
                    counts[old] = n
            if not counts or text == src:
                continue
            before = md5(p)
            if not dry:
                shutil.copy2(p, p + ".bak_" + stamp)
                with open(p, "w", encoding="utf-8", newline="") as f:
                    f.write(text)
                after = md5(p)[:8]
            else:
                after = "-"
            rows.append("%s | avant=%s apres=%s | %s" % (
                p, before[:8], after, " ".join("%s=%d" % kv for kv in counts.items())))
    out = os.path.join(os.path.expanduser("~"), "rapport_renommage_%s.txt" % stamp)
    with open(out, "w", encoding="utf-8") as f:
        f.write("# bak suffixe : .bak_%s\n" % stamp)
        f.write("\n".join(rows) + "\n")
    for r in rows:
        print(r)
    print("fichiers : %d%s\nrapport : %s" % (len(rows), " (dry)" if dry else "", out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
