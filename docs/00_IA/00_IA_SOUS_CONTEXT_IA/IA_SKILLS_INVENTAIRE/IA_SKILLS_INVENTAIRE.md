# Skills Hermes - inventaire vertical

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

Date : 2026-10-17 (v3) | 185 skills actives (hors `.archive` : 46 archivees)

Changements depuis la v2 (2026-10-11) : 4 skills supprimees le 16/10 (clim-smartir-daikin, ha-kiosk-visio, html-scroll-animations, suno-web-app-workflow), ha-maj renommee (source Claude : ha-update-check-cli).

Mise a jour 2026-10-24 : ha-resync-docs retire (supprime cote projet le 2026-10-20, dossier Hermes envoye a la corbeille le 2026-10-24) : communes 15 -> 14, total 186 -> 185. Les autres comptages datent du 2026-10-17 et ne sont pas recalcules (le doublon skill-library-mirroring a aussi ete supprime cote Hermes le 2026-10-24).

Les 14 skills communes avec Claude sont en face a face (corps identique, alignement du 2026-10-17 16h05).
Les skills propres a Hermes sont regroupees par sujet : les skills d'un meme theme sont les unes sous les autres.

---

## 1. Skills communes Claude = Hermes (14)

| # | Skill | Claude (`.claude/skills/`) | Hermes (`D:/hermes/skills/`) |
|---:|---|---|---|
| 1 | `fix-file` | `.claude/skills/fix-file/SKILL.md` | `smart-home/fix-file/SKILL.md` |
| 2 | `ha-new-yaml` | `.claude/skills/ha-new-yaml/SKILL.md` | `smart-home/ha-new-yaml/SKILL.md` |
| 3 | `ha-push-docs` | `.claude/skills/ha-push-docs/SKILL.md` | `smart-home/ha-push-docs/SKILL.md` |
| 4 | `ha-push-md` | `.claude/skills/ha-push-md/SKILL.md` | `smart-home/ha-push-md/SKILL.md` |
| 5 | `ha-push-yaml` | `.claude/skills/ha-push-yaml/SKILL.md` | `smart-home/ha-push-yaml/SKILL.md` |
| 6 | `ha-resync-tree` | `.claude/skills/ha-resync-tree/SKILL.md` | `smart-home/ha-resync-tree/SKILL.md` |
| 7 | `ha-status` | `.claude/skills/ha-status/SKILL.md` | `smart-home/ha-status/SKILL.md` |
| 8 | `ha-trigul` | `.claude/skills/ha-trigul/SKILL.md` | `smart-home/ha-trigul/SKILL.md` |
| 9 | `histo` | `.claude/skills/histo/SKILL.md` | `note-taking/histo/SKILL.md` |
| 10 | `histo-final` | `.claude/skills/histo-final/SKILL.md` | `note-taking/histo-final/SKILL.md` |
| 11 | `journal-modifs` | `.claude/skills/journal-modifs/SKILL.md` | `journal-modifs/SKILL.md` |
| 12 | `sync-index` | `.claude/skills/sync-index/SKILL.md` | `smart-home/sync-index/SKILL.md` |
| 13 | `update-arbo` | `.claude/skills/update-arbo/SKILL.md` | `smart-home/update-arbo/SKILL.md` |
| 14 | `ha-maj (source: ha-update-check-cli)` | `.claude/skills/ha-maj/SKILL.md` | `smart-home/ha-maj/SKILL.md` |

---

## 2. Skills propres a Hermes (171), par sujet

### Home Assistant - prod & exploitation (8)

- `home-assistant-config` - Config Home Assistant: valider, éditer, auditer YAML.
- `home-assistant-config-workflow` - Config HA repo re-build: analyse, correctifs, audits.
- `home-assistant-mcp` - Branche Claude/Hermes a Home Assistant via MCP (ha-mcp).
- `hermes-ha-gateway` - Query/control Home Assistant from Hermes via gateway/REST.
- `ha-audit-huissier` - Audit complet HA type PV huissier: 7 passes lecture seule.
- `ha-vie-et-cascades` - Etudier la vie de HA : rythmes, entites bavardes, cascades.
- `ha-energy-thermal-analysis` - Analyse conso/thermique HA: methode eprouvee (diag log).
- `ha-projet-documentation` - Docs projet HA : fiches modules, cascade C: -> 243 -> repo.

### Home Assistant - dashboards & pages (3)

- `ha-lovelace-dashboards` - Dashboards Lovelace YAML HA : structure, pièges, templates.
- `ha-www-pages` - Pages /local HA perso (Z:) : patch, déploiement, vérif.
- `ha-aidant-pages` - Use when édition pages Videsio/Musique (HA aidant .241).

### Home Assistant - clim & chauffage (1)

- `ha-ir-climate-control` - Clim HA: SmartIR/Broadlink, plages reelles, piste filaire.

### Home Assistant - materiel zigbee/thread (3)

- `ha-matter-thread` - Matter/Thread HA : ZBT-1, USB Proxmox, IKEA Zigbee caché.
- `z2m-ct200-ops` - Z2M CT200 : SSH, config yaml, options device, Shelly.
- `myelectricaldata-admin` - Admin MyElectricalData/Linky : dates, config, pièges.

### Pont Hue (10.32.154.206) (3)

- `hue-bridge-admin` - Use when managing Hue bridge scenes/buttons via local API.
- `hue-bridge-local-api` - Pont Hue local : API v1/v2, scènes, boutons, ménage.
- `openhue` - Control Philips Hue lights, scenes, rooms via OpenHue CLI.

### Proxmox (.240-.246) (2)

- `proxmox-admin` - Admin Proxmox via API REST (token, inventaire, backups).
- `proxmox-api` - Proxmox VE via API: token, inventaire, modifs (avec accord).

### LLM local - stack llama.cpp / LM Studio (8)

- `llm-local-serving` - LM Studio/llama.cpp : configs serveur, pièges API, CPU/VRAM
- `llm-local-stack` - Stack LLM local validé : llama-server + OpenFox, config.
- `llm-local-testing` - Test LLM local : GGUF, llama-server, LM Studio, bench.
- `local-llm-model-catalog` - Catalogue LLM local : familles, tailles, VRAM 16 Go, HF.
- `local-llm-stack` - Stack LLM local Windows : llama-server, OpenFox, CUDA, RAM.
- `llama-cpp` - llama.cpp local GGUF inference + HF Hub model discovery.
- `serving-llms-vllm` - vLLM: high-throughput LLM serving, OpenAI API, quantization.
- `huggingface-hub` - HuggingFace hf CLI: search/download/upload models, datasets.

### LLM local - OpenFox (8080) (4)

- `openfox-local-setup` - OpenFox + LLM local : install Windows, providers, X-High.
- `openfox-operations` - OpenFox : config, maxTokens, ctx, débug EventStore.
- `openfox-session-ops` - OpenFox local : config modèle, API, sessions coincées.
- `openfox` - OpenFox : install, wizard, serveur, providers, workflows.

### LLM - bench, couts & fact checking (8)

- `llm-bench-recap` - Bench LLM local : mesures tok/s, TTFT, VRAM, récap comparo.
- `llm-factuality-bench` - Banc SimpleQA: invention/abstention, A/B de consignes.
- `simpleqa-bench` - Mesurer invention et abstention d'un LLM (banc SimpleQA).
- `llm-api-cost-analysis` - Analyse conso/coûts API LLM (exports, projections).
- `deepseek-usage-analysis` - Analyse exports usage DeepSeek : coûts, cache, projection.
- `deepseek-usage-billing` - Facture DeepSeek : exports CSV, grilles, projection.
- `weights-and-biases` - W&B: log ML experiments, sweeps, model registry, dashboards.
- `evaluating-llms-harness` - lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.).

### Dev - code, debug & qualite (11)

- `systematic-debugging` - 4-phase root cause debugging: understand bugs before fixing.
- `test-driven-development` - TDD: enforce RED-GREEN-REFACTOR, tests before code.
- `requesting-code-review` - Pre-commit review: security scan, quality gates, auto-fix.
- `simplify-code` - Parallel 4-agent cleanup of recent code changes.
- `dogfood` - Exploratory QA of web apps: find bugs, evidence, reports.
- `codebase-inspection` - Inspect codebases w/ pygount: LOC, languages, ratios.
- `spike` - Throwaway experiments to validate an idea before build.
- `plan` - Write a markdown plan to .hermes/plans/; no execution.
- `node-inspect-debugger` - Debug Node.js via --inspect + Chrome DevTools Protocol CLI.
- `python-debugpy` - Debug Python: pdb REPL + debugpy remote (DAP).
- `computer-use-windows-pitfalls` - Use when driving elevated or Electron windows on Windows.

### Dev - GitHub & CI (8)

- `github` - GitHub via gh CLI: PRs, issues, reviews, repos, auth.
- `github-auth` - GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login.
- `github-repo-management` - Clone/create/fork repos; manage remotes, releases.
- `github-pr-workflow` - GitHub PR lifecycle: branch, commit, open, CI, merge.
- `github-code-review` - Review PRs: diffs, inline comments via gh or REST.
- `github-issues` - Create, triage, label, assign GitHub issues via gh or REST.
- `github-issue-to-pr` - Carry a GitHub issue to a verified PR with honest CI state.
- `sdlc-review` - Review Kanban handoffs and route verified outcomes.

### Orchestration - deleguer a un autre agent (6)

- `claude-code` - Delegate coding to Claude Code CLI (features, PRs).
- `codex` - Delegate coding to OpenAI Codex CLI (features, PRs).
- `opencode` - Delegate coding to OpenCode CLI (features, PR review).
- `computer-use` - Drive the desktop background-first; escalate on signal.
- `user-browser-automation` - Use when driving the user's real browser via computer_use.
- `merge-reconciler` - Neutral third-party resolution of agent merge conflicts.

### Orchestration - Hermes lui-meme & skills (13)

- `hermes-agent` - Use, configure, theme, extend, and orchestrate Hermes Agent.
- `hermes-config-inspection` - Personnalité Hermes: config.yaml + cli.py. Espaces -> grep.
- `hermes-data-migration` - Récupérer/migrer les données Hermes (state.db, skills).
- `hermes-desktop-updates` - Use when a Hermes desktop update or crash misbehaves.
- `hermes-instance-activity-audit` - Use when asked what a Hermes instance did over a period.
- `hermes-reasoning-effort` - Use when setting or explaining Hermes reasoning effort.
- `hermes-twin-coordination` - Jumeaux Hermes en LAN : SSH, canal relais, sync .env.
- `regles-utilisateur` - Use when editing, propagating, or auditing user rules.
- `mirroring-skill-libraries` - Importer les skills d'un autre agent dans Hermes.
- `skill-library-mirroring` - Importer et aligner les skills d'un agent tiers dans Hermes.
- `hermes-agent-skill-authoring` - Author in-repo SKILL.md files: frontmatter and structure.
- `inspecting-hermes-desktop-dom` - Read the live Hermes desktop DOM/CSS over CDP.
- `hermes-messaging-platform-setup` - Connect and verify a Hermes messaging platform.

### Aide a la personne - cerveau & notes (7)

- `cerveau-obsidian` - Ranger sessions, essais et veille dans le vault Cerveau.
- `cerveau-vault` - Use when filing into Berry's cerveau vault (themed notes).
- `obsidian` - Read, search, create, and edit notes in the Obsidian vault.
- `knowledge-vault-workflow` - Filing & upkeep of Berry's Cerveau Obsidian vault.
- `sync-docs` - Use when 'sync' or '/sync': sync docs locales vers Z:.
- `vault-doc-pdf-export` - Export PDF d'un doc du vault Cerveau (md->html->chromium).
- `redaction-voix-utilisateur` - Rédiger à sa place (entretien, dossier) depuis le vault.

### Aide a la personne - bureautique & docs (19)

- `airtable` - Airtable REST API via curl. Records CRUD, filters, upserts.
- `box` - Box manages cloud files, sharing, search, and metadata.
- `chromium-browser-config` - Configurer Brave/Chrome/Edge : profils, langue, Shields.
- `document-to-action-items` - Extract cited obligations, deadlines, tasks from documents.
- `docx` - Create, read, edit, template, and review Word .docx files.
- `google-workspace` - Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.
- `maps` - Geocode, POIs, routes, timezones via OpenStreetMap/OSRM.
- `meeting-action-items` - Turn meeting notes into cited decisions, owners, tickets.
- `nano-pdf` - Edit text in existing PDFs via natural-language prompts.
- `notion` - Notion API + ntn CLI: pages, databases, markdown, Workers.
- `ocr-and-documents` - Extract text from PDFs/scans (pymupdf, marker-pdf).
- `pdf` - PDF files: create, read, merge, fill, OCR, edit text.
- `powerpoint` - Create, read, edit .pptx decks with python-pptx.
- `product-price-monitor` - Watch product, flight, or listing prices; alert on target.
- `session-librarian` - Organize sessions by prompt: find, rename, archive, prune.
- `teams-meeting-pipeline` - Teams meeting summaries, job replay, Graph subscriptions.
- `user-screen-guidance` - Guider l'utilisateur à l'écran : captures annotées.
- `weekly-review-planning` - Weekly reset: commitments, stalled work, next-week plan.
- `xlsx` - Create, read, edit Excel .xlsx workbooks and CSVs.

### Aide a la personne - mail (2)

- `email-inbox-triage` - Triage an inbox: prioritize threads, draft replies safely.
- `himalaya` - Himalaya CLI: IMAP/SMTP email from terminal.

### Recherche & veille - contenu web (13)

- `arxiv` - Search arXiv papers by keyword, author, category, or ID.
- `research-paper-writing` - Write ML papers for NeurIPS/ICML/ICLR: design→submit.
- `llm-wiki` - Karpathy's LLM Wiki: build/query interlinked markdown KB.
- `grounded-citations` - Ground answers and documents in cited, verifiable sources.
- `web-fact-verification` - Use when verifying facts online or searches are blocked.
- `blogwatcher` - Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.
- `competitor-news-monitor` - Watch named companies for material news; cited digests.
- `youtube-content` - YouTube transcripts to summaries, threads, blogs.
- `youtube-channel-transcripts` - Transcripts d'une chaîne YT en masse : recette, pièges.
- `youtube-vers-cerveau` - YouTube : pomper la vidéo au cerveau (hub, pépites).
- `video-text-extraction` - Extraire texte/UI d'une vidéo : yt-dlp + frames + vision.
- `gif-search` - Search/download GIFs from Tenor via curl + jq.
- `songsee` - Audio spectrograms/features (mel, chroma, MFCC) via CLI.

### Web & reseaux - acces & depannage (7)

- `blocked-page-recovery` - Use when a fetch fails: 403/429, paywall, WAF, bot wall.
- `service-outage-triage` - Use when a service seems down: provider vs local triage.
- `github-pages-site-update` - Use when updating his GitHub Pages site (ha.erodi-ha.com).
- `funnel-resource-recovery` - Use when recup ressources funnel : jetable + API Notion.
- `lead-magnet-recovery` - Récupérer un guide de funnel (opt-in, Notion) au cerveau.
- `xurl` - X/Twitter via xurl CLI: raw post search, posting, DM, media.
- `lan-network-inventory` - Scans réseau local : trouver et identifier les appareils.

### Creatif - design & maquettes HTML (8)

- `claude-design` - Design one-off HTML artifacts (landing, deck, prototype).
- `sketch` - Throwaway HTML mockups: 2-3 design variants to compare.
- `pretext` - Build creative browser demos with DOM-free text layout.
- `popular-web-designs` - 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.
- `design-md` - Author/validate/export Google's DESIGN.md token spec files.
- `humanizer` - Humanize text: strip AI-isms and add real voice.
- `affiches-imprimables` - Affiches A4 imprimables : HTML print CSS et PDF headless.
- `print-ready-documents` - Print-ready A4 docs/posters from markdown (HTML → PDF).

### Creatif - diagrammes & schemas (3)

- `architecture-diagram` - Dark-themed SVG architecture/cloud/infra diagrams as HTML.
- `excalidraw` - Hand-drawn Excalidraw JSON diagrams (arch, flow, seq).
- `ascii-art` - ASCII art: pyfiglet, cowsay, boxes, image-to-ascii.

### Creatif - video, image & son (7)

- `manim-video` - Manim CE animations: 3Blue1Brown math/algo videos.
- `ascii-video` - ASCII video: convert video/audio to colored ASCII MP4/GIF.
- `comfyui` - Generate images, video, and audio via diffusion workflows.
- `p5js` - p5.js sketches: gen art, shaders, interactive, 3D.
- `touchdesigner-mcp` - Control TouchDesigner via twozero MCP.
- `songwriting-and-ai-music` - Songwriting craft and Suno AI music prompts.
- `baoyu-infographic` - Infographics: 21 layouts x 21 styles (信息图, 可视化).

### Systeme - Windows (6)

- `windows-autostart-management` - Use when auditing/cleaning Windows startup items.
- `windows-openssh-server` - Set up or fix OpenSSH Server on Windows: keys, firewall.
- `windows-software-updates` - Audit and batch-update Windows software, drivers, WU.
- `renommage-fichiers-en-masse` - Renommer des fichiers en masse : convention et pieges.
- `audit-miroir-md5` - Use when auditing a local/Samba/Git doc mirror by MD5.
- `nvidia-driver-update` - Use when updating NVIDIA drivers via NVCleanstall.

### Systeme - Linux & dual-boot (6)

- `linux-usb-install` - Clé USB d'install Linux: ISO, sha256, Rufus, boot live.
- `linux-locale-fr` - Passer un Linux en francais : locale, locale-gen, verifs.
- `lineageos-flash` - LineageOS: support check, flash, GApps, Magisk, drivers.
- `bootloader-dual-boot` - Entrée OS absente du menu de démarrage (GRUB/Limine).
- `dual-boot-shared-storage` - Dual-boot : données partagées Win/Linux (fstab, symlink).
- `omarchy` - Omarchy Linux (DHH) : faits, IA, prépa migration.

### Systeme - materiel, RGB & audio (6)

- `hardware-spec-comparison` - Comparer des CPU/materiel avant achat, sources citees.
- `turing-smart-screen` - Ecran Turing 3.5 USB : udev, config, lancement sous Linux.
- `usb-smart-screen` - Écrans USB Turing/TURZX : identification et Linux.
- `linux-rgb-peripherals` - RGB clavier/souris Linux : OpenRGB + autostart.
- `openrgb-rgb-control` - Linux RGB control via OpenRGB (keyboards, autostart).
- `pipewire-audio-troubleshooting` - Audio Linux (PipeWire) : silences, qualité, égaliseur, BT.

### Apple (macOS) (4)

- `apple-notes` - Manage Apple Notes via memo CLI: create, search, edit.
- `apple-reminders` - Apple Reminders via remindctl: add, list, complete.
- `findmy` - Track Apple devices/AirTags via FindMy.app on macOS.
- `imessage` - Send and receive iMessages/SMS via the imsg CLI on macOS.

### Gaming & divers (5)

- `dlss5-swapper` - Use when installing DLSS 5 in games via DLSS5-Swapper.
- `firestorm-cleanup` - Use when purging Firestorm files or emptying its cache.
- `second-life-dlss5` - Use when relaunching/diagnosing Second Life DLSS5 viewer.
- `ip-protection-france` - Marques, e-Soleau, horodatage : proteger nom/oeuvre en FR.
- `philosophical-exchange` - Utiliser si l'utilisateur lance un échange philosophique.

---

## Recapitulatif par sujet

| Sujet | Nombre |
|---|---:|
| Communes Claude = Hermes | 14 |
| Home Assistant - prod & exploitation | 8 |
| Home Assistant - dashboards & pages | 3 |
| Home Assistant - clim & chauffage | 1 |
| Home Assistant - materiel zigbee/thread | 3 |
| Pont Hue (10.32.154.206) | 3 |
| Proxmox (.240-.246) | 2 |
| LLM local - stack llama.cpp / LM Studio | 8 |
| LLM local - OpenFox (8080) | 4 |
| LLM - bench, couts & fact checking | 8 |
| Dev - code, debug & qualite | 11 |
| Dev - GitHub & CI | 8 |
| Orchestration - deleguer a un autre agent | 6 |
| Orchestration - Hermes lui-meme & skills | 13 |
| Aide a la personne - cerveau & notes | 7 |
| Aide a la personne - bureautique & docs | 19 |
| Aide a la personne - mail | 2 |
| Recherche & veille - contenu web | 13 |
| Web & reseaux - acces & depannage | 7 |
| Creatif - design & maquettes HTML | 8 |
| Creatif - diagrammes & schemas | 3 |
| Creatif - video, image & son | 7 |
| Systeme - Windows | 6 |
| Systeme - Linux & dual-boot | 6 |
| Systeme - materiel, RGB & audio | 6 |
| Apple (macOS) | 4 |
| Gaming & divers | 5 |
| **Total actives** | **185** |
| Archivees (`.archive`) | 46 |
