# Contrats d'interface du pipeline de formation

Ce fichier est la **source de vérité unique** du format exact de chaque fichier échangé entre deux skills du pipeline de production de formation. Les `SKILL.md` n'y renvoient que par référence courte ("voir Contrat N ci-dessous") — ils ne dupliquent jamais ce format. Toute divergence constatée entre ce fichier et le comportement réel d'une skill est un bug spec-driven à corriger immédiatement (voir [CONTRIBUTING.md](CONTRIBUTING.md) : la spec n'est jamais implicite, une seule source fait foi).

Ce document ne décrit pas *pourquoi* chaque skill fait ce qu'elle fait (ça reste dans son `SKILL.md`) — seulement *ce qui passe d'une skill à l'autre* et sous quelle forme exacte.

## Vue d'ensemble du pipeline

```
cadrage-formation
   │  (Contrat 1 : cadrage_<client>.xlsx rempli)
   ▼
formation-material-builder ── Phase 0 (interne, Contrat 2 : 00-brief.md / 00-plan.md)
   │  (Contrat 3 : modules/M<n>-<slug>/slides.md, livrables/00-fil-rouge.md)
   ▼
slide-content-claude-design
   │  (Contrat 4 : M<n>-slides-content.md, M<n>-prompts.md)
   │
   ├── mode manuel ──────────────► copier-coller humain vers Gemini + Claude Design
   │                                (composition finale toujours manuelle — Claude Design
   │                                n'expose aucune API programmatique, voir SKILL.md)
   │
   └── mode auto illustrations ──► script generate_illustrations.py (API Gemini)
                                    → livrables/assets/M<n>/slide-N.png
                                    → puis composition manuelle dans Claude Design
                                      (les images sont prêtes, la composition ne l'est pas)
   │
   ▼ (tout livrable, Contrat 5 : pas de format imposé)
comite-qualite
```

`formation-pipeline` (skill orchestratrice, voir son `SKILL.md`) enchaîne ces étapes en respectant les points de validation définis dans chacune — elle ne redéfinit aucun contrat, elle les fait respecter dans l'ordre.

---

## Contrat 1 — `cadrage-formation` → `formation-material-builder`

**Fichier** : `formations/<client>-<theme>/<AAAA-MM>/cadrage_<client>.xlsx`

**Structure** (produite par `cadrage-formation/scripts/generate_cadrage_xlsx.py`) :

| Onglet | Statut | Colonnes |
|---|---|---|
| Questions de cadrage | Toujours présent | Thème / Question / Priorité (`INDISPENSABLE`\|`OPTIONNEL`) / Pourquoi / **Réponse client** / Statut (`À poser`\|`Posée`\|`Répondu`\|`Non pertinent`) |
| Participants | Si fourni à la génération | Nom / Prénom / Rôle / Entité / Profil / Statut |
| Contexte | Si fourni à la génération | Synthèse contexte + points de vigilance |

**Règle de complétude (consommée par `formation-material-builder` Phase 0.1)** : toutes les questions de priorité `INDISPENSABLE` doivent avoir Statut = "Répondu" avant que `formation-material-builder` ne poursuive sans confirmation explicite du consultant. Une question INDISPENSABLE non répondue est un blocage, jamais un défaut silencieusement ignoré.

**Version de contrat** : v1 (28/07/2026).

---

## Contrat 2 — `formation-material-builder` Phase 0 (interne)

Ce contrat n'est pas inter-skills : c'est l'interface entre la sous-étape 0.1 (ingestion) et le reste de `formation-material-builder` (Phase 1 et suivantes) au sein de la même skill. Documenté ici car c'est l'endroit exact où le chaînon auparavant manquant (`formation-plan-builder`, jamais implémentée) a été comblé — voir [CHANGELOG.md](CHANGELOG.md).

**Fichiers** : `00-brief.md`, `00-plan.md`, à la racine du workspace.

Format exact et règles de rédaction : voir `formation-material-builder/SKILL.md` § « Phase 0 — Discovery », qui fait foi. Résumé structurel :

- `00-brief.md` : Contexte / Objectifs (réponses client) / Audience (structurée : mode d'analyse, hétérogénéité technique/fonctionnel, séniorité, profils à confirmer) / Contraintes / Points de vigilance.
- `00-plan.md` : Niveau global, durée totale, format, section « Logique de progression », puis un bloc par module (durée, niveau, prérequis, objectifs pédagogiques).

**Origine des données** : dérivées du xlsx (Contrat 1) en mode nominal ; fournies directement par le consultant en mode standalone (pas de xlsx disponible).

**Version de contrat** : v2 (28/07/2026 — ajout de la structure Audience et de la logique de progression inter-modules, suite à audit comité qualité ; v1 même date couvrait la première version du format).

---

## Contrat 3 — `formation-material-builder` → `slide-content-claude-design`

**Fichiers** :
- `modules/M<n>-<slug>/slides.md` — format exact dans `formation-material-builder/references/slide_outline_format.md`.
- `livrables/00-fil-rouge.md` — format exact dans `formation-material-builder/references/fil_rouge_design.md` ; sert de métaphore filée globale par défaut pour `slide-content-claude-design` (voir sa section « Où trouver la métaphore filée »).

**Version de contrat** : v1 (24/07/2026, US-10/US-12).

---

## Contrat 4 — `slide-content-claude-design` → (mode manuel | mode auto illustrations)

**Fichiers**, colocalisés dans `livrables/` :
- `M<n>-slides-content.md` — une fiche par slide (titre, accroche, contenu, composant visuel dimensionné/positionné/colorisé, bloc texte, placeholder d'illustration dimensionné et positionné). Format exact dans `slide-content-claude-design/SKILL.md`.
- `M<n>-prompts.md` — bloc « Direction artistique » unique en tête + un prompt d'illustration par slide. Format exact dans `slide-content-claude-design/SKILL.md`.

Les deux modes consomment **exactement les mêmes fichiers**, sans variante de format :
- **Mode manuel** : le consultant copie-colle `M<n>-prompts.md` dans Gemini et `M<n>-slides-content.md` dans Claude Design, image par image.
- **Mode auto illustrations** : `slide-content-claude-design/scripts/generate_illustrations.py` lit `M<n>-prompts.md`, appelle l'API Gemini, écrit les images dans `livrables/assets/M<n>/slide-N.png`. La composition dans Claude Design reste manuelle dans les deux modes (voir Contrat 5 et la note ci-dessous).

**Note sur Claude Design** : à la date de rédaction (28/07/2026), Claude Design n'expose aucune API programmatique (le pont `/design-sync` avec Claude Code est un aller-retour interactif piloté par un humain, pas un point d'intégration scriptable) — la composition visuelle finale reste donc toujours une action humaine, quel que soit le mode d'illustration choisi.

**Version de contrat** : v2 (28/07/2026 — ajout du mode auto illustrations ; v1 du 24/07/2026 couvrait le mode manuel seul, US-10/US-11).

---

## Contrat 5 — (tout livrable) → `comite-qualite`

Aucun format imposé en entrée : `comite-qualite` s'adapte au livrable qu'on lui soumet (voir sa Phase 0.1 « Lire et caractériser le livrable »). Ce contrat existe dans ce document pour la complétude de la vue d'ensemble, pas parce qu'il impose une contrainte de format.

**Version de contrat** : v1 (24/07/2026, US-6).

---

## Journal des versions de contrat

| Contrat | Version | Date | Changement |
|---|---|---|---|
| 1 | v1 | 28/07/2026 | Consolidation (format déjà en vigueur depuis `cadrage-formation` v1, formalisé ici) |
| 2 | v1 | 28/07/2026 | Création — comble le chaînon `formation-plan-builder` jamais implémenté |
| 2 | v2 | 28/07/2026 | Audience structurée + logique de progression inter-modules (post-audit comité qualité) |
| 3 | v1 | 24/07/2026 | Consolidation (US-10/US-12) |
| 4 | v1 | 24/07/2026 | Mode manuel (US-10/US-11) |
| 4 | v2 | 28/07/2026 | Ajout du mode auto illustrations (script Gemini) |
| 5 | v1 | 24/07/2026 | Consolidation (US-6) |
