<!-- Page wiki GitHub : "Accueil". Sur GitHub, renommer sans le préfixe "00-" — le préfixe numérique sert uniquement à garder l'ordre de lecture visible dans un explorateur de fichiers local (Finder, VS Code), il n'a aucun rôle sur GitHub. -->

# Pipelines de production de formation et de réponse à appel d'offres

Bienvenue sur le wiki des pipelines de skills Claude Code de ce dépôt. Ce dépôt couvre **deux pipelines** : la production d'une formation client complète (de l'appel de cadrage jusqu'aux slides, au livret stagiaire, aux exercices et au quiz), et la réponse à un appel d'offres commercial (de la recherche méthodologique jusqu'au plan de présentation).

**Tu dialogues avec l'assistant en français, il fait le gros du travail.** Tu n'as pas besoin de connaître le détail technique du pipeline pour t'en servir — l'assistant te guide à chaque étape (voir [Comment l'assistant te guide](#comment-lassistant-te-guide) plus bas).

## Par où commencer ?

0. **Vue d'ensemble en 5 minutes**, avant d'installer quoi que ce soit → [ONBOARDING.md](../ONBOARDING.md) (schéma + une page, pour une démo à un nouvel arrivant)
1. **Installer les skills** sur l'outil que tu utilises → [Installation](01-Installation/00-Sommaire)
2. **Utiliser le pipeline** au quotidien → [Utiliser le pipeline](02-Utiliser-le-pipeline)
3. **Un souci, une question ?** → [FAQ et dépannage](03-FAQ-et-depannage)

## Les skills, en un coup d'œil

### Pipeline formation — 4 skills, dans cet ordre (chaque étape consomme la sortie de la précédente)

| # | Skill | Ce qu'elle produit |
|---|---|---|
| 0 | `cadrage-formation` | La grille de questions à poser au client (fichier Excel) |
| 1 | `formation-material-builder` | Tout le matériel pédagogique : slides, livret stagiaire, guide formateur, ateliers, quiz |
| 2 | `slide-content-claude-design` | Le contenu prêt à générer visuellement dans Claude Design + les prompts d'illustration pour Gemini |
| 3 | `comite-qualite` | Un audit multi-relecteurs du dossier complet, jusqu'à convergence |

Une cinquième skill optionnelle, `formation-pipeline`, enchaîne les 4 ci-dessus à la suite sans avoir à les relancer une par une.

### Pipeline réponse à appel d'offres — une skill unique

`reponse-appel-offres` pilote la réponse complète à un appel d'offres (AO) commercial en 8 étapes internes : recherche méthodologique, recherche client, analyse du besoin (checklist d'exigences CCTP tracée), fit cabinet/client, sourcing et sélection de références, plan de présentation détaillé pour Claude Design, renvoi vers `comite-qualite`.

### Skill transverse — `design-system-extractor`

Extrait la charte graphique d'un client à partir de n'importe quel document fourni (captures, PDF, export Figma, site web...), pour que `slide-content-claude-design` l'applique à la place de sa palette par défaut. À la demande, pas une étape obligatoire.

Détail complet de chaque skill → [Utiliser le pipeline](02-Utiliser-le-pipeline).

## Comment l'assistant te guide

- **Avant de commencer une étape** : si un paramètre important n'est pas clair (le format de sortie voulu, la densité des slides, la charte graphique du client…), l'assistant te le demande d'abord, plutôt que de deviner.
- **En cours de route**, sur les étapes longues : l'assistant s'arrête à des moments clés (après le premier module produit, avant de compiler les gros documents finaux, avant d'appliquer des corrections importantes) pour vérifier que tu es d'accord avant de continuer.
- **Après chaque étape** : l'assistant te dit ce qui a été produit et te propose la suite logique — tu n'as jamais à deviner par toi-même quelle est l'étape suivante.

Tu peux toujours répondre « continue sans t'arrêter » si tu préfères moins d'interruptions.

## Petit glossaire

| Terme | Ce que c'est |
|---|---|
| **Skill** | Un mode d'emploi que l'assistant Claude charge et suit pour une tâche donnée. Tu l'appelles en tapant `/nom-de-la-skill` ou en décrivant ton besoin. |
| **Claude Code** | L'assistant IA dans lequel tournent les skills (éditeur VS Code / Antigravity, ou en ligne de commande). |
| **Claude Design** | Un outil séparé qui compose la mise en page finale des slides. |
| **Gemini** | Un outil séparé qui génère les illustrations des slides à partir d'une consigne texte. |
| **Placeholder** | Une zone grise réservée sur une slide, aux dimensions exactes de la future illustration. |
| **Métaphore filée** | L'univers visuel commun à toute la formation, pour que les illustrations forment un ensemble cohérent. |
| **Cas fil rouge** | Un cas fictif unique (ex. « StockPilot ») qui traverse tous les ateliers d'une formation, pour une expérience immersive et cohérente. |
| **Livret stagiaire / guide formateur** | Les deux documents Word produits : l'un pour les participants (sans corrigés), l'autre pour le formateur (avec corrigés et minutage). |

## Pour aller plus loin

- Le dépôt GitHub complet (specs détaillées, code source des skills) : voir le lien du dépôt en tête de ce wiki.
- Historique des évolutions du pipeline : `CHANGELOG.md` dans le dépôt.
- Pour proposer une évolution ou signaler un problème : voir `CONTRIBUTING.md` dans le dépôt.
