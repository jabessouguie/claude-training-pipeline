<!-- Page wiki GitHub : "Utiliser le pipeline". Sur GitHub, renommer sans le préfixe "02-". -->

# Utiliser le pipeline

Le pipeline s'exécute dans cet ordre — chaque skill consomme la sortie de la précédente. Tu n'as pas besoin de les invoquer explicitement une par une : décris ta formation à l'assistant, il détecte la skill pertinente et te propose la suite à chaque étape.

## 0. `cadrage-formation` — préparer l'appel de cadrage client

Prépare le cadrage d'une formation client de bout en bout et livre une **grille de questions de cadrage priorisées dans un fichier Excel (.xlsx)**.

À utiliser dès qu'il faut préparer, cadrer ou animer une formation pour un client — un compte rendu de réunion commerciale, une liste de participants, ou une demande de « questions à poser au client » suffisent à déclencher cette skill.

- Crée dès le début le dossier de la formation selon une convention de nommage, et demande s'il existe une formation antérieure proche à réutiliser (jamais sans validation explicite).
- Pour les audiences de plus de 20 participants, bascule automatiquement vers une analyse par profil type plutôt qu'une recherche nominative.
- **Sortie** : le `.xlsx` de questions priorisées ; les réponses obtenues alimentent l'étape suivante.

## 1. `formation-material-builder` — produire tout le matériel pédagogique

Entrées : un brief, une recherche, un plan de formation.

Produit, par phases avec points de validation à chaque étape :

| Phase | Sortie |
|---|---|
| 0-1 | Un **cas fil rouge** unique (un contexte fictif, ex. « StockPilot », qui traverse toute la formation) + une roadmap de production — les deux à valider |
| 2 | Le contenu markdown module par module (`slides.md`, `notes-formateur.md`), et pour chaque atelier son énoncé + corpus dédié + solution |
| 3 | La compilation : slides (brouillon — voir étape 2 ci-dessous pour le rendu final), énoncés d'ateliers en HTML/PDF, livret stagiaire, guide formateur |
| 4 | Le quiz d'évaluation (format Kahoot) et le document de prérequis/setup |

**Mode alternatif** disponible sur demande explicite : retour au format classique sans cas fil rouge (`exercices.md`/`solutions.md` par module).

## 2. `slide-content-claude-design` — préparer le rendu visuel final des slides

**En clair** : cette étape prépare le contenu de tes diapositives pour deux outils séparés — **Claude Design** (qui compose la mise en page finale) et **Gemini** (qui génère les illustrations). Elle produit deux fichiers texte que tu colles ensuite dans ces outils.

**C'est ici que se fait le deck final** : le brouillon `.pptx` de l'étape précédente n'est plus maintenu une fois qu'on passe par Claude Design.

Produit, par module, deux fichiers :
- **`M<n>-slides-content.md`** — une fiche par slide, à coller dans Claude Design (titre, contenu, composant visuel dimensionné/positionné/colorisé précisément, placeholder gris pour l'illustration).
- **`M<n>-prompts.md`** — un bloc « Direction artistique » unique en tête (ancré dans la métaphore filée de la formation), puis un prompt d'illustration par slide, à coller dans Gemini.

Un audit UX/UI de `M<n>-slides-content.md` est recommandé avant la génération visuelle dans Claude Design.

## 3. `comite-qualite` — auditer jusqu'à convergence

Peut auditer n'importe quel livrable — pas seulement une formation.

- Clarifie explicitement le périmètre d'audit avant de commencer (contenu markdown, rendu visuel généré, ou les deux).
- Compose dynamiquement une équipe de 3 à 6 relecteurs adaptée au livrable (ex. pour une formation : directeur pédagogique, expert du domaine, directeur artistique, praticien métier…).
- Produit des constats classés 🔴 bloquant / 🟠 important / 🟡 mineur, applique les corrections, puis ré-audite jusqu'à convergence sincère.

**Deux modes** : **loop** (corrections appliquées directement) ou **annotations** (liste zone/commentaire, pour édition dans un autre outil comme Google Docs).

---

## Mode bout-en-bout (`formation-pipeline`)

Une cinquième skill, `formation-pipeline`, enchaîne les 4 skills ci-dessus à la suite si tu ne veux pas les relancer une par une — c'est un mode additionnel, l'usage skill-par-skill décrit ci-dessus reste toujours possible.

Avant de démarrer, elle demande explicitement deux paramètres (jamais devinés) : le **mode de validation** (elle s'arrête à chaque point déjà prévu par chaque skill, par défaut ; ou elle enchaîne sans interruption sauf blocage réellement impossible à lever seul) et le **mode d'illustration** (génération automatique via l'API Gemini, ou manuel comme aujourd'hui).

**La composition finale dans Claude Design reste toujours manuelle**, quel que soit le mode choisi — Claude Design n'expose aucune API programmatique à ce jour. En mode automatique, tu arrives simplement dans Claude Design avec les images déjà générées et rangées par slide.

Le format exact des fichiers échangés entre les skills est documenté dans `PIPELINE_CONTRACTS.md` à la racine du dépôt.

---

Pour l'installation, voir [Installation](01-Installation/00-Sommaire). Pour un souci ou une question fréquente, voir [FAQ et dépannage](03-FAQ-et-depannage).
