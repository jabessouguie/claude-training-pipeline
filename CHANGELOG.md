# Changelog

Historique des évolutions du pipeline de skills, du plus récent au plus ancien. Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/) ; les dates correspondent aux jalons de livraison de spec dans ce dépôt, pas nécessairement à une vérification en usage réel (voir `BACKLOG.md` pour le statut de vérification de chaque item).

## 28/07/2026

**Ajouté**
- Installation multi-surface documentée dans le README : procédures distinctes pour Claude Code, l'application Claude (claude.ai) et Cowork — les skills Anthropic ne se synchronisent pas automatiquement entre surfaces. Structure de ZIP détaillée pour claude.ai/Cowork ([#23](BACKLOG.md)).
- Cadrage renforcé en début et en cours de skill longue (extension US-4, [#4](BACKLOG.md)) : `slide-content-claude-design` interroge densité et design system en étape 0 si non précisés ; `formation-material-builder` marque un point de vérification avant de compiler les `.docx` finaux ; `comite-qualite` marque une pause avant application des corrections s'il y a au moins un 🔴 bloquant. Le README explique cette logique de guidage (avant/pendant/après chaque étape).
- Extension de US-12 ([#22](BACKLOG.md)) : chaque élément du corpus d'atelier vit dans son propre fichier, au **format réel du métier client** (un e-mail en `.md` structuré comme un e-mail, un export tabulaire en `.xlsx` si le vrai outil du client exporte du tableur, une capture d'écran en `.png`…) plutôt qu'un format uniformisé pour la facilité de traitement. Production : markdown source d'abord, puis conversion vers le binaire réel (nouvelle sous-phase 3.1ter de `formation-material-builder`).
- Section « Où trouver la métaphore filée » dans `slide-content-claude-design/SKILL.md` : indique de la tirer de `livrables/00-fil-rouge.md` (cas fil rouge, US-12) en priorité.
- `LICENSE.md`, `CHANGELOG.md` (ce fichier).
- **`formation-pipeline`** ([#27](BACKLOG.md), US-15) : nouvelle skill orchestratrice qui enchaîne `cadrage-formation` → `formation-material-builder` → `slide-content-claude-design` → `comite-qualite` en respectant les points de validation déjà définis dans chacune, avec deux paramètres établis en amont (mode de validation step-by-step/non-stop, génération des illustrations auto/manuel). Mode d'usage additionnel — les 4 skills existantes restent invocables seules.
- **Mode génération automatique des illustrations** dans `slide-content-claude-design` ([#28](BACKLOG.md), US-16, réponse à [#9](BACKLOG.md)) : script `scripts/generate_illustrations.py` qui appelle l'API Gemini (modèle `gemini-2.5-flash-image`, "Nano Banana") à partir de `M<n>-prompts.md` déjà produit, et range les images générées par numéro de slide dans `livrables/assets/M<n>/`. La composition finale dans Claude Design reste manuelle dans tous les cas — vérifié le 28/07/2026 : Claude Design n'expose aucune API programmatique (le pont `/design-sync` avec Claude Code est un aller-retour interactif piloté par un humain).
- **`PIPELINE_CONTRACTS.md`** ([#26](BACKLOG.md), US-14) : nouveau fichier racine documentant le format exact de chaque fichier échangé entre les skills du pipeline (5 contrats), avec renvois ajoutés depuis les `SKILL.md` concernés plutôt qu'une duplication du format.

**Corrigé**
- `slide-content-claude-design` : le champ `Visuel` d'une fiche slide précise désormais systématiquement dimensions, position et couleurs exactes du composant (au lieu d'une simple catégorie type « matrice 2×2 »), avec un exemple rempli.
- Correction post-audit comité qualité : une affirmation catégorique sur l'absence de partage d'équipe (Team/Enterprise) sur l'application Claude s'est révélée fausse après vérification indépendante — corrigée avec la nuance nécessaire (deux pages Anthropic non synchronisées entre elles sur ce point).
- **Suppression des références à `formation-plan-builder`** ([#25](BACKLOG.md), US-13) : cette skill n'a jamais été implémentée ni spécifiée nulle part dans le dépôt (confirmé par grep exhaustif), en violation directe du principe spec-driven de `CONTRIBUTING.md`. `formation-material-builder` consomme désormais directement le `.xlsx` de cadrage rempli par `cadrage-formation`, et dérive elle-même `00-brief.md`/`00-plan.md` en Phase 0 (nouveau Contrat 2 de `PIPELINE_CONTRACTS.md`).

## 24/07/2026

**Ajouté**
- US-11 — Direction artistique cohérente par module ([#21](BACKLOG.md)) : bloc « Direction artistique » unique en tête de `M<n>-prompts.md`, cadrant style illustratif et déclinaison de la métaphore filée pour cohérence visuelle entre toutes les slides du module.
- US-12 — Cas fil rouge et ateliers structurés façon StockPilot ([#22](BACKLOG.md)) : `formation-material-builder` conçoit un **cas fil rouge** unique par formation comme standard par défaut, avec des ateliers structurés en dossiers dédiés (`livrables/atelier-N/`), des solutions séparées non distribuées en amont (`livrables/solutions/`), et une conversion des énoncés en HTML/PDF à la charte par défaut. Mode alternatif sans fil rouge disponible sur demande explicite.
- US-3, US-9 (Horizon 3 de `ROADMAP.md`) : `cadrage-formation` (désormais en 8 étapes, 0 à 7) demande systématiquement s'il existe une formation antérieure proche à réutiliser, avec validation explicite obligatoire ; bascule automatiquement vers une analyse par profil type au-delà de 20 participants.
- US-4, US-5, US-6, US-10 (Horizon 2 de `ROADMAP.md`) : `cadrage-formation` crée le dossier de formation selon une convention de nommage dès l'étape 0 ; les 4 skills proposent systématiquement la prochaine étape à chaque point de validation ; `comite-qualite` clarifie le périmètre d'audit avant de démarrer et peut inclure un rôle « voix du client » ; `slide-content-claude-design` produit deux fichiers distincts (`M<n>-slides-content.md` pour Claude Design, `M<n>-prompts.md` pour Gemini), avec un audit UX/UI prescrit avant la génération visuelle.
- US-1, US-2, US-7, US-8 (Horizon 1 de `ROADMAP.md`) : sections « Source de vérité », « Enregistrement fiable entre sessions », « Pré-requis : paramétrer l'extension Claude Code » et « Ouvrir les fichiers .xlsx générés ».

Voir `BACKLOG.md` pour les critères d'acceptation détaillés et leur statut de vérification (plusieurs comportements restent à valider sur un cas réel).

## 07/2026

**Ajouté**
- `formation-material-builder` : le quiz est produit au **format Kahoot** (§4.1 du SKILL.md + `references/quiz_design.md`) — chaque question précise type (quizz, vrai/faux, réponse libre, curseur, pins, puzzle), 2-6 réponses, bonne réponse, temps (5 s à 4 min), points (standard/double/aucun) et limite de réponse (une seule/plusieurs). Les énoncés de questions visent ≤ 120 caractères (limite Kahoot).
