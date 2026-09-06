---
name: formation-pipeline
description: Orchestre l'enchaînement complet cadrage-formation → formation-material-builder → slide-content-claude-design (mode manuel ou mode auto illustrations) → comite-qualite pour produire une formation client de bout en bout sans relancer chaque skill à la main. Déclenche cette skill quand l'utilisateur demande de "générer toute la formation", "lancer le pipeline complet", "faire toute la chaîne de bout en bout", "produire la formation sans que je repasse par chaque étape", ou tout équivalent explicite d'automatisation multi-étapes. Ne PAS invoquer si l'utilisateur demande une seule étape du pipeline (ex. "prépare le cadrage", "génère les slides du module 2") — les 4 autres skills restent utilisables et invocables indépendamment, cette skill est un mode d'usage additionnel, jamais un passage obligé.
---

# Formation Pipeline — orchestrateur du pipeline complet

Cette skill **ne refait pas** le travail des 4 skills existantes (`cadrage-formation`, `formation-material-builder`, `slide-content-claude-design`, `comite-qualite`). Elle détecte l'état du workspace, suit les instructions de la bonne skill au bon moment, transmet les paramètres de mode choisis une seule fois, et respecte les points de validation déjà écrits dans chaque `SKILL.md` — elle ne les redéfinit jamais.

**Contrats consommés** : voir [`PIPELINE_CONTRACTS.md`](../PIPELINE_CONTRACTS.md) pour le format exact de chaque fichier échangé entre les skills orchestrées ici. Cette skill ne définit aucun format de fichier — elle s'appuie uniquement sur ceux déjà spécifiés.

## Note technique importante

Une skill Claude Code n'est pas une fonction qu'on "appelle" — c'est un ensemble d'instructions chargé dans le contexte de l'agent. Concrètement, "invoquer `cadrage-formation`" depuis cette skill signifie : **lire et suivre maintenant les instructions du `SKILL.md` de `cadrage-formation`** comme si l'utilisateur l'avait demandée directement, avec les paramètres déjà établis en étape 0 ci-dessous. Ce comportement est à vérifier au premier usage réel (voir le smoke test prescrit par `CONTRIBUTING.md`).

## Étape 0 — Paramètres à établir avant de démarrer (jamais deviner)

Si non précisés spontanément par l'utilisateur, poser explicitement ces questions avant de commencer :

```
Cinq paramètres avant de lancer le pipeline complet :

1. Mode de validation : je m'arrête à chaque point de validation déjà prévu
   par chaque étape ("step-by-step", recommandé), ou j'enchaîne sans interruption
   sauf blocage réellement impossible à lever seul ("non-stop") ?

2. Génération des illustrations : je génère automatiquement les images via l'API
   Gemini ("auto" — nécessite une clé API disponible), ou je m'arrête avant
   Gemini/Claude Design pour que tu composes toi-même ("manuel", comme
   aujourd'hui) ?

3. Point de départ : on repart de zéro (cadrage), tu as déjà un dossier de
   formation existant à reprendre, ou tu es en mode standalone (pas de xlsx
   de cadrage — tu fournis toi-même un contexte et un plan de formation déjà
   arrêtés par ailleurs, cf. `formation-material-builder/SKILL.md` § « Mode
   standalone ») ?

4. Design system : la charte par défaut « Encre & Sauge » convient, ou le client
   a-t-il une charte propre à appliquer ? Si oui : existe-t-il déjà un
   `design-systems/<client>/design-system.md` (produit par
   `design-system-extractor`), ou faut-il l'extraire d'abord de documents de
   marque que tu fournirais (captures, PDF de charte, export Figma, site web…) ?

5. (Si standalone) : peux-tu fournir maintenant le contexte client et le plan
   de formation ? Ils seront transmis tels quels à `formation-material-builder`
   Phase 0, sans passer par l'ingestion d'un xlsx.
```

Ne jamais fixer ces paramètres par défaut silencieusement — ce sont des choix structurants (cf. le principe déjà appliqué dans `slide-content-claude-design/SKILL.md` § « Méthode », étape 0, pour densité/design system).

**Cas du design system à extraire (paramètre 4)** : si l'utilisateur annonce une charte client sans fichier `design-systems/<client>/design-system.md` existant, invoquer `design-system-extractor` **avant** d'atteindre `slide-content-claude-design`, en suivant sa spec telle quelle — y compris son point de validation structurant (l'utilisateur confirme les tokens extraits avant finalisation). Ce point de validation n'est **jamais levé par le mode non-stop** : il rejoint la liste des garde-fous non contournables ci-dessous, car un design system mal extrait se propage à toutes les slides produites ensuite. Si l'utilisateur ne dispose d'aucun document de marque exploitable, poursuivre avec « Encre & Sauge » et le signaler explicitement — jamais improviser une charte à partir d'une description orale.

Une fois établis, **ne jamais les redemander** à une sous-skill qui, invoquée seule, les demanderait normalement (ex. densité/design system de `slide-content-claude-design`) — les transmettre directement.

## Table de détection d'état

Reprend et étend le principe déjà en place dans `formation-material-builder/SKILL.md` § « Détection automatique de la phase ». Regarder ce qui existe dans `formations/<client>-<theme>/<AAAA-MM>/` (ou le workspace standalone) avant chaque transition :

**Limite de ce principe, à ne jamais perdre de vue** : un fichier ne porte, par sa seule présence, aucune information sur le fait qu'il ait déjà été validé par le consultant — un fichier existe ou n'existe pas, il n'est jamais « en attente » au sens du système de fichiers. Deux lignes ci-dessous (« produit, pas encore validé ») décrivent en réalité un état **conversationnel dans la session en cours** (l'orchestrateur vient de le produire, la question de validation est déjà posée, la réponse n'est pas encore arrivée) — jamais un état qu'on pourrait détecter en reprenant un workspace dans une nouvelle session où ce fichier existe déjà. **Sur reprise d'un workspace** où un tel fichier est déjà présent : ne jamais présumer qu'il a été validé (l'orchestrateur skipperait alors un garde-fou qu'il ne peut jamais lever lui-même) ni qu'il ne l'a pas été (il redemanderait une validation déjà obtenue) — **poser explicitement la question** : « Ce `<fichier>` existe déjà dans le workspace — as-tu déjà validé son contenu, ou dois-je te le présenter pour validation avant de continuer ? »

| État détecté | Action |
|---|---|
| Mode standalone déclaré à l'Étape 0 (pas de xlsx, contexte/plan fournis directement par le consultant) | Suivre `formation-material-builder/SKILL.md` Phase 0 en mode standalone (voir sa section dédiée) — ne jamais passer par `cadrage-formation` dans ce cas |
| Dossier de formation absent, mode standalone non déclaré | Suivre `cadrage-formation/SKILL.md` depuis l'Étape 0 |
| Dossier de formation présent, xlsx pas encore produit | Poursuivre `cadrage-formation/SKILL.md` à l'étape où le dossier en est (Étapes 1 à 6) — ne pas repartir de l'Étape 0, le dossier existe déjà |
| `cadrage_<client>.xlsx` présent, questions INDISPENSABLE non toutes répondues | **Stop** — demander les réponses client manquantes. Blocage que l'orchestrateur ne peut jamais lever lui-même, mode non-stop y compris ; seule issue : les réponses manquantes, ou une confirmation explicite du consultant d'avancer malgré tout (option prévue par `formation-material-builder/SKILL.md` § 0.1, auquel cas le point reste tracé comme vigilance ouverte dans `00-brief.md` — ce n'est pas l'orchestrateur qui décide d'avancer, c'est le consultant) |
| xlsx complet, pas de `00-brief.md`/`00-plan.md` | Suivre `formation-material-builder/SKILL.md` Phase 0 |
| `00-brief.md`/`00-plan.md` produits **dans l'échange en cours**, pas encore validés | **Stop, y compris en mode non-stop** — attendre la validation explicite prescrite par la Phase 0.2 de `formation-material-builder` (garde-fou dur, l'orchestrateur ne peut jamais le lever, voir « Gestion des points de validation » ci-dessous — ne pas confondre avec la règle de relance implicite de `comite-qualite` Phase C, qui ne s'applique qu'aux corrections 🟠/🟡, jamais à ce type de validation structurante). **Sur reprise d'un workspace** où ces fichiers existent déjà sans que l'orchestrateur les ait produits dans la session en cours : ne jamais présumer un sens ou l'autre, voir la limite du principe de détection ci-dessus. |
| Plan validé, pas de `06-material-roadmap.md`/`livrables/00-fil-rouge.md` | Suivre `formation-material-builder/SKILL.md` Phase 1 |
| Fil rouge/roadmap validés, modules incomplets | Suivre `formation-material-builder/SKILL.md` Phase 2 |
| Tous les modules validés, pas de livrables compilés | Suivre `formation-material-builder/SKILL.md` Phase 3-4 |
| Livrables compilés, pas de `M<n>-slides-draft.md` | Suivre `slide-content-claude-design/SKILL.md` jusqu'à l'étape 4 (brouillon texte seul) |
| `M<n>-slides-draft.md` produit **dans l'échange en cours**, pas encore validé | **Stop, y compris en mode non-stop** — garde-fou dur, l'orchestrateur ne peut jamais le lever (voir « Gestion des points de validation » ci-dessous). **Sur reprise d'un workspace** où ce fichier existe déjà sans que l'orchestrateur l'ait produit dans la session en cours : ne jamais présumer un sens ou l'autre, voir la limite du principe de détection ci-dessus. |
| Brouillon validé, pas de `M<n>-slides-content.md`/`M<n>-prompts.md` | Suivre `slide-content-claude-design/SKILL.md` à partir de l'étape 5 (enrichissement visuel du brouillon validé) |
| Fiches produites, mode illustrations = "auto", images non générées | Suivre `slide-content-claude-design/SKILL.md` § « Mode génération automatique des illustrations » (script `generate_illustrations.py`) |
| Images générées (mode auto) ou fiches prêtes (mode manuel) | **Stop — rendre la main** : la composition dans Claude Design reste une action humaine dans les deux modes (aucune API programmatique, voir `PIPELINE_CONTRACTS.md` Contrat 4) |
| Composition confirmée par l'utilisateur comme terminée | Suivre `comite-qualite/SKILL.md` sur le rendu produit |
| `comite-qualite` a convergé | Terminé — récapitulatif de bout en bout |

**Exception** : si l'utilisateur demande explicitement de régénérer/reprendre une étape précise ("refais les slides du module 3"), sauter la détection et exécuter la demande directement, comme le prescrit déjà `formation-material-builder/SKILL.md`.

## Gestion des points de validation

- **Mode step-by-step (défaut)** : à chaque transition du tableau ci-dessus, afficher ce que la sous-skill qui vient de tourner propose comme prochaine étape (elle l'écrit déjà elle-même en fin de section/phase dans son propre `SKILL.md`) — ne pas la reformuler, la relayer telle quelle — puis attendre confirmation avant de continuer.
- **Mode non-stop** : enchaîner automatiquement les transitions, **sauf** les blocages que les sous-skills elles-mêmes qualifient comme non contournables sans intervention humaine : réponses INDISPENSABLE manquantes (`cadrage-formation`/`formation-material-builder`), validation du plan/fil rouge/roadmap (`formation-material-builder`), validation des tokens extraits (`design-system-extractor` Étape 2, si ce détour a été déclenché par le paramètre 4 de l'Étape 0), validation du brouillon texte `M<n>-slides-draft.md` avant enrichissement visuel (`slide-content-claude-design` étape 4), 🔴 bloquant en synthèse (`comite-qualite` Phase C). L'orchestrateur **ne peut jamais** lever un de ces garde-fous lui-même — ils appartiennent à la sous-skill qui les a posés.
- Si une sous-skill signale une ambiguïté ou une information manquante qu'elle ne peut résoudre seule, basculer immédiatement en step-by-step pour cette transition, même si le mode général est non-stop.
- Après chaque transition, même en mode non-stop, produire un message court (une ligne) de ce qui vient d'être fait — pas seulement un récapitulatif final.

## Rétrocompatibilité

Cette skill est un mode d'usage **additionnel**. Chacune des 4 skills existantes reste invocable seule (`/cadrage-formation`, `/formation-material-builder`, `/slide-content-claude-design`, `/comite-qualite`) sans jamais nécessiter `formation-pipeline`. Rien dans les 4 `SKILL.md` existants ne doit référencer `formation-pipeline` comme un passage obligé — vérifier ce point à chaque modification future de l'une de ces skills.

## Proposer la prochaine étape

Comme les 4 autres skills du pipeline (US-4) : à la fin de chaque transition (step-by-step) ou à la toute fin du pipeline complet (non-stop), rappeler ce qui a été produit, où (chemin exact), et ce qui reste à faire — en particulier signaler explicitement quand la main revient à l'utilisateur pour une action non automatisable (composition Claude Design).

## Fichiers de référence

Cette skill n'a pas de `references/` propre : elle s'appuie exclusivement sur les `SKILL.md` des 4 skills orchestrées, sur celui de [`design-system-extractor`](../design-system-extractor/SKILL.md) quand le paramètre 4 de l'Étape 0 déclenche ce détour, et sur [`PIPELINE_CONTRACTS.md`](../PIPELINE_CONTRACTS.md).
