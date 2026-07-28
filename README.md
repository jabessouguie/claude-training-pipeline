# Skills — Pipeline de création de formation

Les quatre skills Claude Code utilisées pour préparer et produire le dossier complet d'une formation « Product Management augmenté », utilisables sur n'importe quelle formation.

## En deux mots

Ce dépôt fournit **quatre « skills »** — des modes d'emploi que Claude Code (l'assistant IA) suit automatiquement pour t'aider, étape par étape, à produire une formation client complète : de l'appel de cadrage jusqu'aux slides, au livret stagiaire, aux exercices et au quiz. Tu dialogues avec l'assistant **en français**, il fait le gros du travail.

- **Une fois installé** (voir « Mise en place technique » plus bas — c'est une étape technique ponctuelle, déléguable à un collègue), l'usage quotidien ne demande **aucune manipulation technique** : tu décris ta formation, l'assistant enchaîne les étapes et te demande de valider aux moments-clés.
- **Où commencer** : par la skill `cadrage-formation` (étape 0 ci-dessous), qui prépare les questions à poser au client. Chaque skill propose ensuite d'elle-même l'étape suivante.

### Comment l'assistant te guide

Tu n'as pas besoin de connaître le détail du pipeline pour t'en servir correctement — l'assistant s'en charge à trois moments :

- **Avant de commencer une étape** : si un paramètre important n'est pas clair (le format de sortie voulu, la densité des slides, la charte graphique du client…), l'assistant te le demande d'abord, plutôt que de deviner et de produire quelque chose qu'il faudra refaire.
- **En cours de route**, sur les étapes longues (produire tout le matériel d'une formation, ou faire un audit qualité complet) : l'assistant s'arrête à des moments clés — après le premier module produit, avant de compiler les gros documents finaux, avant d'appliquer des corrections importantes — pour vérifier que tu es d'accord avant de continuer sur le reste.
- **Après chaque étape** : l'assistant te dit explicitement ce qui a été produit et te propose la suite logique (« veux-tu que j'enchaîne sur X, ou préfères-tu d'abord relire Y ? ») — tu n'as jamais à deviner par toi-même quelle est l'étape suivante du pipeline.

Tu peux toujours répondre « continue sans t'arrêter » si tu préfères moins d'interruptions.

### Petit glossaire (pour cette page)

| Terme | Ce que c'est ici |
|---|---|
| **Skill** | Un mode d'emploi que l'assistant Claude Code charge et suit pour une tâche donnée (cadrer, produire le matériel, etc.). Tu l'appelles en tapant `/nom-de-la-skill` ou en décrivant ton besoin. |
| **Claude Code** | L'assistant IA dans lequel tournent les skills (dans l'éditeur VS Code / Antigravity, ou en ligne de commande). |
| **Claude Design** | Un outil séparé qui **compose la mise en page finale des slides**. Tu y colles le contenu préparé par le pipeline. |
| **Gemini** | Un outil séparé qui **génère les illustrations** des slides à partir d'une consigne texte. |
| **Prompt** | Une consigne en texte donnée à un générateur (ici, à Gemini pour obtenir une image). |
| **Placeholder** | Une zone grise réservée sur une slide, aux dimensions exactes de la future illustration — on y déposera l'image générée. |
| **Métaphore filée** | L'univers visuel commun à toute la formation (ex. « le chantier », « l'expédition »), pour que les illustrations forment un ensemble cohérent. |
| **Livret stagiaire / guide formateur** | Les deux documents Word produits : l'un pour les participants (sans les corrigés), l'autre pour le formateur (avec corrigés et minutage). |

Si un autre terme technique te bloque plus bas, ce n'est probablement pas une étape de ton ressort — voir « Mise en place technique ».

## Les 4 skills et leur enchaînement

Le pipeline s'exécute dans cet ordre — chaque skill consomme la sortie de la précédente :

### 0. `cadrage-formation` — préparer l'appel de cadrage client

Prépare le cadrage d'une formation client de bout en bout et livre une **grille de questions de cadrage priorisées dans un fichier Excel (.xlsx)**.
À utiliser dès qu'on doit préparer, cadrer ou animer une formation pour un client, qu'on partage un compte rendu de réunion commerciale ou une liste de participants, ou qu'on demande des « questions à poser au client », un « appel de cadrage » ou une analyse d'audience — même sans demander explicitement un Excel.
Dès le début, crée le dossier de la formation selon la convention `formations/<client>-<theme>/<AAAA-MM>/` (distingue plusieurs sessions d'une même formation dans le temps) et demande s'il existe une formation antérieure proche à réutiliser comme base (jamais sans validation explicite).
Pour les audiences de plus de 20 participants, bascule automatiquement d'une recherche nominative vers une analyse par profil type (évite un coût en temps/tokens disproportionné sur les masterclass).
Sortie : le `.xlsx` de questions priorisées (indispensables vs optionnelles) qui structure l'appel de cadrage, livré dans ce dossier ; les réponses obtenues alimentent le brief de la skill suivante. Propose systématiquement la prochaine étape une fois le fichier livré.

### 1. `formation-material-builder` — produire tout le matériel pédagogique

Entrées : un brief, une recherche, un plan de formation (idéalement issus de `formation-plan-builder`, sinon fournis directement).
Sorties, par phases avec points de validation :
- **Phase 0-1** : discovery des inputs + conception d'un **cas fil rouge** unique (`livrables/00-fil-rouge.md`, standard par défaut — façon `StockPilot`) + roadmap de production (`06-material-roadmap.md`), les deux à valider
- **Phase 2** : contenu markdown module par module — `slides.md`, `notes-formateur.md` — et, par atelier, `livrables/atelier-N/enonce-atelier-N.md` (+ corpus dédié si besoin) et `livrables/solutions/solution-atelier-N.md` (le 1er module validé sert de gabarit aux suivants)
- **Phase 3** : compilation — `M<n>-slides.pptx` (**brouillon du déroulé** ; le rendu visuel final des slides se fait à l'étape 2 ci-dessous via Claude Design), `enonce-atelier-N.html`/`.pdf` (charte par défaut, un dossier par atelier), `livret-stagiaire.docx` (sans solutions), `guide-formateur.docx` (avec solutions et timing minute par minute)
- **Phase 4** : `quiz-kahoot.md` (format Kahoot : une fiche par question avec type, réponses, bonne réponse, temps imparti, points, limite de réponse) + `prerequis-setup.md`

Références incluses : structure de module, design de slides, format d'outline, design d'exercices (indices gradués, bonus), conception d'un cas fil rouge et structure d'atelier (façon `StockPilot`), principes pédagogiques (Bloom, loi des 20 min), design de quiz Kahoot.
Mode alternatif sans cas fil rouge disponible sur demande explicite (retour au format `exercices.md`/`solutions.md` par module).
Propose systématiquement la prochaine étape à chaque point de validation (fil rouge + roadmap, après le 1er module, fin de chaque phase).

### 2. `slide-content-claude-design` — préparer le rendu visuel final des slides

**En clair** : cette étape prépare le contenu de tes diapositives pour deux outils séparés — **Claude Design** (qui compose la mise en page finale) et **Gemini** (qui génère les illustrations). Elle produit deux fichiers texte que tu colles ensuite dans ces outils. **C'est ici que se fait le deck final** : le `M<n>-slides.pptx` de l'étape 1 n'était qu'un brouillon, et il n'est plus maintenu une fois qu'on passe par Claude Design (on ne garde pas deux versions du même deck).

Entrée : les `slides.md` produits par la skill 1 (ou tout plan/markdown).
Sortie : **deux fichiers par module**, colocalisés dans `formations/<client>-<theme>/<AAAA-MM>/livrables/` :
- `M<n>-slides-content.md` — une fiche par slide (titre bicolore, accroche, contenu, composant du design system **entièrement dimensionné/positionné/colorisé** — pas une simple catégorie de composant, bloc texte à incruster, **placeholder d'illustration gris dimensionné et positionné** renvoyant au prompt correspondant, ou « Bloc » vectoriel pour tableaux/code/schémas) — à coller fiche par fiche dans Claude Design ;
- `M<n>-prompts.md` — un bloc **« Direction artistique »** unique en tête (style illustratif, déclinaison de la métaphore filée du module, contraintes récurrentes), puis les prompts d'illustration Gemini structurés par slide qui le référencent (palette par défaut, sans texte dans l'image) — garantit une cohérence visuelle professionnelle entre toutes les slides d'un même module.

Design system par défaut inclus (bleu marine #2C5F8A parcimonieux, encre #1F1F1F, beige #E8E2DA, data corail/vert sauge, Sora/Inter) — remplaçable par la charte du client.
Recommande un **audit UX/UI de `M<n>-slides-content.md` avant la génération visuelle** dans Claude Design, puis propose `comite-qualite` sur le rendu final.

### 3. `comite-qualite` — auditer jusqu'à convergence

Entrée : le dossier complet (ou n'importe quel livrable). Clarifie explicitement le périmètre d'audit avant de commencer (contenu markdown, présentation générée, ou les deux) si la cible n'est pas déjà sans ambiguïté.
Fonctionnement : compose dynamiquement une équipe de 3 à 6 relecteurs adaptée au livrable (pour une formation : directeur pédagogique, expert du domaine, directeur de mission, directeur artistique, praticien métier, directeur qualité inter-livrables, voix du client si des notes d'entretien sont disponibles), fait produire les constats classés 🔴/🟠/🟡, applique les corrections, puis ré-audite jusqu'à convergence sincère (règles anti-théâtre : pas de problèmes inventés, défaut ≠ préférence, pas plus de 3 itérations consécutives sans changement structurel).
Deux modes : **loop** (corrections appliquées en place) ou **annotations** (liste zone/commentaire pour édition externe). Le message final rappelle le périmètre audité et propose la prochaine étape du pipeline.

---

# Mise en place technique (une seule fois)

> **Cette partie est technique et ponctuelle.** Elle suppose que Claude Code est installé sur ton poste. **Si ce n'est pas le cas, ou si les termes ci-dessous (terminal, dépôt, extension, palette de commandes…) ne te parlent pas, fais-toi accompagner par un collègue technique pour cette étape unique.** Une fois en place, l'usage quotidien décrit plus haut se fait en français, sans manipulation technique.

## Où récupérer les skills (source de vérité)

**Ce dépôt est la référence unique** pour récupérer les 4 skills — ne pas se fier à un envoi ponctuel par e-mail ou par zip, qui peut être partiel ou périmé. Toute évolution des skills est poussée ici avant d'être considérée comme disponible.

## Installation des skills

**Les skills ne se synchronisent PAS automatiquement entre surfaces** (Claude Code, application Claude, Cowork) — c'est une contrainte du produit Anthropic, pas de ce dépôt : chaque surface a son propre mécanisme d'installation, et il faut répéter l'installation sur chaque surface qu'on veut utiliser. Choisir la section correspondant à l'outil utilisé.

### Sur Claude Code (extension VS Code/Antigravity ou CLI)

Copier chaque dossier dans `~/.claude/skills/` :

```
~/.claude/skills/
├── cadrage-formation/
│   ├── SKILL.md
│   └── scripts/             (générateur de la grille Excel)
├── formation-material-builder/
│   ├── SKILL.md
│   └── references/          (7 fichiers de référence)
├── slide-content-claude-design/
│   └── SKILL.md
└── comite-qualite/
    └── SKILL.md
```

**Détection** : si `~/.claude/skills/` existe déjà, l'ajout d'un dossier de skill est pris en compte **en direct, sans redémarrer la session en cours**. Un redémarrage n'est nécessaire que si `~/.claude/skills/` lui-même n'existait pas encore au lancement de la session (premier usage sur un poste neuf). Invocation : `/cadrage-formation`, `/formation-material-builder`, `/slide-content-claude-design`, `/comite-qualite` (ou en langage naturel — chaque SKILL.md décrit ses déclencheurs). Vérifier la détection en tapant `/` dans le chat : les 4 skills doivent apparaître dans la liste.

**Procédure de repli si une skill n'est pas détectée** (à utiliser en dernier recours, pas par défaut) :
- Ouvrir un nouveau chat plutôt que de réutiliser une session existante.
- Vérifier qu'aucun autre `~/.claude/skills/<nom>/SKILL.md` ne porte le même `name:` en frontmatter (conflit de nom).

#### Paramétrer l'extension Claude Code dans VS Code / Antigravity

Pour utiliser ce pipeline dans l'extension Claude Code de VS Code ou d'Antigravity plutôt qu'en ligne de commande :

1. Installer l'extension **Claude Code** depuis le marketplace de l'éditeur (icône Claude dans la barre d'activités verticale à gauche).
2. Ouvrir l'extension et démarrer une conversation (par exemple en tapant un message de test) pour déclencher l'écran de connexion.
3. Se connecter avec ton **compte professionnel** si tu en as un dédié : suivre le lien d'authentification affiché par l'extension. Un compte différent peut ne pas donner accès aux mêmes quotas ni aux mêmes skills partagées.
4. Si l'extension semble bloquée ou ne propose pas de lien d'authentification, utiliser la commande **"Restart extension"** (palette de commandes) plutôt que de désinstaller/réinstaller.

**Gestion des quotas** : un blocage ponctuel sur les quotas (cotas) a été observé avec certains comptes professionnels ; ce n'est pas systématique et n'a pas été observé de façon répétée. Si un blocage survient, patienter (les quotas se renouvellent) plutôt que de changer de compte ou de modèle par réflexe.

**Choix de l'éditeur** : l'extension Claude Code fonctionne aussi bien dans VS Code que dans Antigravity — le choix entre les deux est une préférence d'environnement, pas une contrainte du pipeline. Voir `BACKLOG.md` (item #7) pour l'arbitrage en cours sur l'harmonisation des outils utilisés en interne.

### Sur l'application Claude (claude.ai, app desktop/mobile)

L'application Claude installe les skills **une par une, par fichier ZIP**, via **Réglages → Personnaliser → Skills**. C'est un mécanisme différent de Claude Code (pas de simple copie de dossier).

1. **Activer d'abord** l'option « Exécution de code et création de fichiers » dans les réglages (nécessaire aux comptes Pro/Max/Team/Entreprise pour que les skills fonctionnent).
2. **Préparer le ZIP** pour chaque skill à installer : le ZIP doit contenir le **dossier de la skill à sa racine** (pas son contenu nu à la racine du zip), et le nom de ce dossier doit correspondre exactement au `name:` du frontmatter du `SKILL.md`. Les sous-dossiers (`references/`, `scripts/`) sont inclus tels quels. Depuis ce dépôt : `cd ~/.claude/skills && zip -r cadrage-formation.zip cadrage-formation/` (répéter pour chacune des 4 skills, ou zipper directement depuis une copie locale du dépôt).
3. **Réglages → Personnaliser → Skills → bouton "+" → Create skill → Upload a skill**, puis sélectionner le ZIP correspondant. Répéter pour les 4 skills.

**Par défaut, chaque personne importe son propre ZIP.** Mais sur un compte **Team ou Enterprise**, un **Owner** peut provisionner une skill pour toute l'organisation en une fois, sans que chaque membre ait à l'installer individuellement : *Réglages d'organisation → Skills → Organization skills → « + Add »*, en uploadant le même ZIP. La skill apparaît alors automatiquement chez chaque membre (activée par défaut, désactivable individuellement). Si un compte professionnel Team/Enterprise est disponible, **demander à la personne Owner de provisionner les 4 skills une seule fois** plutôt que de les faire installer individuellement. *(Point à vérifier : la documentation développeur Anthropic — platform.claude.com — affirme encore qu'aucune gestion centralisée n'existe sur claude.ai, ce qui contredit la doc support — support.claude.com/en/articles/13119606 — décrivant ce mécanisme de provisioning. Les deux pages ne semblent pas synchronisées ; se fier en priorité à la doc support, plus récente sur ce point, mais confirmer auprès d'un Owner du compte avant de compter dessus pour un déploiement d'équipe.)*

### Sur Claude Cowork

Cowork tourne dans l'application Claude. **Ce qui suit est une supposition raisonnable, pas un fait confirmé par une source Anthropic officielle** (aucune documentation trouvée ne détaille explicitement comment Cowork charge les skills) : Cowork chargerait les mêmes skills que celles installées sur le compte claude.ai (donc la procédure « Sur l'application Claude » ci-dessus s'appliquerait aussi à Cowork), sans lire `~/.claude/skills/` sur le poste. **À vérifier en conditions réelles** avant de s'y fier : installer une skill via la procédure ci-dessus, puis confirmer qu'elle apparaît bien dans une session Cowork.

## Ouvrir les fichiers `.xlsx` générés (`cadrage-formation`)

`cadrage-formation` produit un livrable `.xlsx`. Pour l'ouvrir sans quitter VS Code / Antigravity :

- Installer une extension de visualisation Excel pour VS Code (ex. « Excel Viewer » ou équivalent disponible sur le marketplace de l'éditeur).
- Une fois installée, ouvrir directement le fichier `.xlsx` généré depuis l'explorateur de fichiers de l'éditeur : il s'affiche en tableau dans un onglet, sans lancer d'application externe.
- Alternative sans extension : ouvrir le fichier directement depuis Google Drive si le dossier de formation y est synchronisé (cf. convention de rangement des livrables).

## Notes diverses

- Ces quatre skills fonctionnent aussi indépendamment les unes des autres.
- `cadrage-formation` : le script `scripts/generate_cadrage_xlsx.py` nécessite Python avec `openpyxl` (génération du fichier Excel).

Pour l'historique daté des évolutions du pipeline, voir [`CHANGELOG.md`](CHANGELOG.md).
