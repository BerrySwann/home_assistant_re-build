# Sync_98_sauvegarde.py - copie Infra_Proxmox, TODO et historique (hors docs) vers docs\98_sauvegarde_hors_docs pour la prod/GitHub. Modes : plan (defaut) | exec
# Fiche : docs\04_docs_scripts\04_docs_scripts_SH_MD\Sync_98_sauvegarde\Sync_98_sauvegarde.md . Interpreteur : python -I -X utf8
import os,re,sys,hashlib
B=r"C:\Users\Berry Swann\Documents\ReBuild"
D=os.path.join(B,"docs","98_sauvegarde_hors_docs")
SRC=["Infra_Proxmox","TODO","historique"]
EXCLUS=set()  # SONOFF_STATUS_2026-05-23.md n est plus exclu : identifiant, mot de passe et cle reseau sont caviardes dans la copie (ordre d Eric 2026-10-31)
TXT=(".md",".html",".log",".txt",".csv",".tsv",".json",".js",".svg",".sh",".ps1",".py",".yaml",".yml")
MASK=re.compile(rb"ghp_[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]+")
def ignore(n, rel=""):
    if rel.startswith("Infra_Proxmox") and ".bak" in n: return False  # les .bak d Infra_Proxmox sont gardes (Eric 2026-10-31)
    return (".bak" in n or ".avant_" in n or ".racine_avant" in n or n=="secrets.yaml" or n.endswith(".pyc")
            or (n.startswith("#") and n.endswith("#")))
BANNER=("<div align=\"center\">\r\n\r\n"
"[![Statut](https://img.shields.io/badge/Statut-bak_d-ff9800?style=flat-square)](.)&nbsp;\r\n"
"[![MàJ](https://img.shields.io/badge/MàJ-@MAJ@-44739e?style=flat-square)](.)&nbsp;\r\n"
"[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;\r\n"
"[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;\r\n"
"[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;\r\n"
"[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;\r\n"
"[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;\r\n"
"[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)\r\n\r\n</div>\r\n")
mode=sys.argv[1] if len(sys.argv)>1 else "plan"
new=chg=same=0; excl=[]; masked=[]
for s in SRC:
    for dp,dn,fn in os.walk(os.path.join(B,s)):
        dn[:]=[d for d in dn if d!="__pycache__"]
        for f in fn:
            p=os.path.join(dp,f); rel=os.path.relpath(p,B)
            if ignore(f,rel): continue
            if rel in EXCLUS: excl.append(rel); continue
            data=open(p,"rb").read()
            if f.lower().endswith(TXT):
                if rel.startswith("Infra_Proxmox"):
                    data=re.sub(rb"(?im)^(\s*(?:password|user|network_key|pan_id|ext_pan_id|auth_token):).*",rb"\1 ***",data)
                    data=re.sub(rb"auth `[^`]*` / `[^`]*`",b"auth `***` / `***`",data)
                m=MASK.sub(b"ghp_***",data)
                if m!=data: masked.append(rel); data=m
            mb=re.search(r"\.bak_(\d{4})_(\d{2})_(\d{2})\.md$",f)
            if rel.startswith("Infra_Proxmox") and mb and b"img.shields.io" not in data:
                maj="%s--%s--%s"%mb.groups()
                ban=BANNER.replace("@MAJ@",maj).encode("utf-8")
                k=data.find(b"\n")+1
                data=data[:k]+b"\r\n"+ban+b"\r\n"+data[k:]
            dst=os.path.join(D,rel)
            if os.path.exists(dst):
                if hashlib.md5(open(dst,"rb").read()).digest()==hashlib.md5(data).digest(): same+=1; continue
                chg+=1
            else: new+=1
            if mode=="exec":
                os.makedirs(os.path.dirname(dst),exist_ok=True); open(dst,"wb").write(data)
print("mode=%s nouveaux=%d modifies=%d identiques=%d exclus=%d jetons_masques=%d"%(mode,new,chg,same,len(excl),len(masked)))
for e in excl: print("EXCLU",e)