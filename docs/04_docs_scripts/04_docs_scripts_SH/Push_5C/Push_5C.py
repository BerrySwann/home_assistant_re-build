# Push_5C.py - push general de l etape 5C de /histo (docs vers H:\docs). Modes : plan (lecture seule, defaut) | exec.
# Fiche : docs\04_docs_scripts\04_docs_scripts_SH_MD\Push_5C\Push_5C.md . Interpreteur : python -I -X utf8
import os, hashlib, glob, re, sys, shutil
L=r"C:\Users\Berry Swann\Documents\ReBuild\docs"; P=r"H:\docs"
import datetime
T=r"C:\Users\Berry Swann\Documents\ReBuild\TEMPO\miroir_5C_"+datetime.date.today().isoformat()
MODE=sys.argv[1] if len(sys.argv)>1 else "plan"
def skip(rel):
    parts=rel.split("\\")
    if rel=="99_docs_MD_system\\ENTITES_GLOBAL_INDEX\\ENTITES_GLOBAL_INDEX.md": return False  # exception Eric 2026-10-31 17h33
    if any(p.startswith("XX_") or p=="99_docs_MD_system" for p in parts[:-1]): return True
    n=parts[-1]
    if ".bak" in n or n=="secrets.yaml" or n.endswith(".pyc") or (n.startswith("#") and n.endswith("#")): return True
    if "__pycache__" in parts or "Dashboard_COMPLET" in parts: return True
    if any(("ARCHIVE" in p.upper() and p.upper().startswith(("_ARCHIVE","ARCHIVE"))) or "_archive_" in p.lower() for p in parts): return True
    return False
def walk(root):
    out={}
    for d,ds,fs in os.walk(root):
        for f in fs:
            full=os.path.join(d,f); out[os.path.relpath(full,root)]=full
    return out
def md5(p):
    h=hashlib.md5()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
def strip(p):
    t=open(p,"rb").read().decode("utf-8","replace").replace("\r\n","\n")
    t=re.sub(r'<div align="center">.*?</div>\n*','',t,count=1,flags=re.S)
    return hashlib.md5(t.encode()).hexdigest()
loc={r:p for r,p in walk(L).items() if not skip(r)}
prod={r:p for r,p in walk(P).items() if not skip(r)}
new=[];diff=[];same=0
for r,p in loc.items():
    if r not in prod: new.append(r)
    elif os.path.getsize(p)==os.path.getsize(prod[r]) and md5(p)==md5(prod[r]): same+=1
    else: diff.append(r)
only=[r for r in prod if r not in loc]
connu=[];inconnu=[]
for r in diff:
    if r.startswith("98_sauvegarde_hors_docs\\"): connu.append(r); continue  # copie derivee de Sync_98 : la source locale fait foi
    lp=loc[r]; h=strip(prod[r]); d,n=os.path.split(lp); stem,ext=os.path.splitext(n)
    cands=glob.glob(os.path.join(d,stem+".bak*"))+glob.glob(os.path.join(d,n+".bak*"))
    (connu if any(strip(b)==h for b in cands) else inconnu).append(r)
print("local=%d prod=%d identiques=%d NOUVEAU=%d DIFF=%d (connus %d, INCONNUS %d) SEUL_EN_PROD=%d"%(len(loc),len(prod),same,len(new),len(diff),len(connu),len(inconnu),len(only)))
print("-- SEUL_EN_PROD:"); [print("  ",r) for r in sorted(only)]
print("-- DIFF INCONNUS:"); [print("  ",r) for r in inconnu]
print("-- NOUVEAU (dossiers):")
g={}
for r in new: k="\\".join(r.split("\\")[:2]); g[k]=g.get(k,0)+1
[print("  %4d %s"%(v,k)) for k,v in sorted(g.items())]
if MODE!="exec": sys.exit(0)
# garde-fou : aucune suppression en prod sans ordre d Eric
if only: print("ABANDON : SEUL_EN_PROD non vide, a decider avec Eric (copie TEMPO + suppression a faire a part)"); sys.exit(3)
# 1) copie TEMPO + MD5 puis suppression
ok=0
for r in only:
    dst=os.path.join(T,r); os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copy2(prod[r],dst)
    assert md5(dst)==md5(prod[r]),r
for r in only:
    os.remove(prod[r]); ok+=1
for r in sorted({os.path.dirname(r) for r in only},key=len,reverse=True):
    d=os.path.join(P,r)
    while d!=P and os.path.isdir(d) and not os.listdir(d): os.rmdir(d); d=os.path.dirname(d)
print("supprimes en prod (copie TEMPO + MD5 OK):",ok)
# 2) push NOUVEAU + DIFF connus
n=0;bad=[]
for r in new+connu:
    src=loc[r]; dst=os.path.join(P,r); os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copyfile(src,dst)
    if md5(src)!=md5(dst): bad.append(r)
    n+=1
print("pousses:",n,"MD5 differents apres push:",len(bad)); [print("  KO",r) for r in bad]
print("non pousses (PROD DIFFERENTE INCONNUE):",len(inconnu))
