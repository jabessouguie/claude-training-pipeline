# Skills — Pipelines de production de formation et de réponse à appel d'offres

Les skills Claude Code utilisées pour préparer et produire, d'une part, le dossier complet d'une formation « Product Management augmenté » (utilisable sur n'importe quelle formation), et d'autre part une réponse à appel d'offres commercial.

Ce dépôt couvre désormais **deux pipelines** : la production de formation (5 skills, détaillées ci-dessous) et la réponse à appel d'offres (voir « Pipeline réponse à appel d'offres » plus bas). Les deux partagent la même gouvernance, le même workflow Git, et le même fichier de contrats d'interface (`PIPELINE_CONTRACTS.md`) — voir `GOVERNANCE.md` pour l'arbitrage qui a permis cet élargissement.

**Nouveau sur ce dépôt ?** [ONBOARDING.md](ONBOARDING.md) donne une vue d'ensemble des deux pipelines en une page, à montrer avant d'installer quoi que ce soit.

## En deux mots

Ce dépôt fournit **quatre « skills »** de production de formation — des modes d'emploi que Claude Code (l'assistant IA) suit automatiquement pour t'aider, étape par étape, à produire une formation client complète : de l'appel de cadrage jusqu'aux slides, au livret stagiaire, aux exercices et au quiz. Tu dialogues avec l'assistant **en français**, il fait le gros du travail. Une **cinquième skill, `formation-pipeline`**, orchestre les quatre premières à la suite si tu préfères ne pas les relancer une par une (voir « Mode bout-en-bout » plus bas) — mais l'usage skill-par-skill décrit ci-dessous reste toujours possible et n'est jamais remplacé.

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

Entrées : la grille de cadrage remplie par le client (`.xlsx` produit par `cadrage-formation`), ou directement un contexte + un plan de formation en mode standalone. Il n'y a pas de skill intermédiaire entre le cadrage et cette skill : elle dérive elle-même, en Phase 0, un brief (`00-brief.md`) et un plan de formation (`00-plan.md`) à partir du xlsx rempli, fait valider les deux, puis poursuit.
Sorties, par phases avec points de validation :
- **Phase 0** : ingestion du cadrage + brief et plan dérivés (`00-brief.md`, `00-plan.md`), à valider
- **Phase 1** : conception d'un **cas fil rouge** unique (`livrables/00-fil-rouge.md`, standard par défaut — façon `StockPilot`) + roadmap de production (`06-material-roadmap.md`), les deux à valider
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

## Mode bout-en-bout (`formation-pipeline`)

Si tu préfères ne pas relancer chaque skill toi-même à chaque étape, la skill `formation-pipeline` enchaîne les 4 skills ci-dessus à la suite (cadrage → matériel → slides → qualité), en respectant les mêmes points de validation. C'est un mode d'usage **additionnel** : les 4 skills restent invocables indépendamment, comme décrit ci-dessus.

Avant de démarrer, elle te demande explicitement (jamais deviné) :
1. **Mode de validation** : elle s'arrête à chaque point déjà prévu par chaque skill (`step-by-step`, par défaut), ou elle enchaîne sans interruption sauf blocage réellement impossible à lever seul (`non-stop` — ex. réponses client indispensables manquantes, validation du plan/fil rouge, correction bloquante en comité qualité : ces arrêts-là, l'orchestrateur ne peut jamais les lever lui-même).
2. **Génération des illustrations** : automatique via l'API Gemini (`auto` — nécessite une clé API), ou manuelle comme aujourd'hui (`manuel` — tu copies-colles toi-même vers Gemini et Claude Design).

**Ce qui reste toujours manuel, quel que soit le mode choisi** : la composition finale dans **Claude Design**. Claude Design n'expose aujourd'hui aucune API programmatique (vérifié le 28/07/2026) — même en mode "auto", tu arrives dans Claude Design avec les images déjà générées et rangées par slide, mais c'est toi qui composes la slide.

---

# Pipeline réponse à appel d'offres

Second pipeline de ce dépôt : `reponse-appel-offres`, une skill unique qui pilote la réponse complète à un appel d'offres (AO) commercial, de la recherche méthodologique jusqu'au plan de présentation prêt à coller dans Claude Design — même logique spec-driven que le pipeline formation, adaptée aux spécificités de l'avant-vente (conformité stricte au cahier des charges, deadline non négociable, différenciation réelle, cohérence entre plusieurs contributeurs).

**Historique** : une première itération (`cadrage-appel-offres`) se limitait à l'analyse du dossier. Le 18/08/2026, le périmètre a été élargi en une seule skill bout-en-bout — voir `CHANGELOG.md` et `BACKLOG.md` #29.

## `reponse-appel-offres` — de la recherche méthodologique au plan de présentation

À utiliser dès qu'on reçoit un dossier d'AO, un CCTP, un règlement de consultation, ou qu'on veut préparer une réponse à appel d'offres.

Workflow en 8 étapes :

0. **Recherche méthodologique** — bonnes pratiques et erreurs à éviter en réponse à AO, pour ce type de client et de mission (mémoire générique, réponse point par point, spécificités de notation public/privé).
1. **Recherche étendue sur le client** émetteur de l'AO — détection du type de dossier (marché public vs privé, jamais deviné), activité, organisation, personnes liées.
2. **Analyse du besoin** — extraction exhaustive des exigences en checklist tracée (`OBLIGATOIRE`/`SOUHAITABLE`/`ÉLIMINATOIRE`), détection d'un éventuel **format de réponse imposé par le client** (trame, sommaire obligatoire, pagination — toujours prioritaire sur le format par défaut de l'étape 6), critères de notation.
3. **Analyse de l'adéquation cabinet/besoin** — via un profil cabinet (`profil-cabinet.md`, jamais un cabinet présupposé : chaque consultant renseigne le sien), croisé avec les exigences.
4. **Références du cabinet** — demandées au consultant ET complétées par une recherche web de références publiques, jamais l'une sans l'autre.
5. **Sélection des références pertinentes** — critères explicites (secteur, techno, taille de mission).
6. **Plan de présentation détaillé pour Claude Design** — même niveau de détail que `slide-content-claude-design` : une fiche par slide entièrement dimensionnée/positionnée/colorisée + un fichier de prompts séparé, prêts à coller dans Claude Design (composition toujours manuelle, Claude Design n'a pas d'API programmatique).
7. **Comité qualité** — proposition explicite d'enchaînement vers `comite-qualite`, sans modification nécessaire de cette skill (ses rôles existants couvrent déjà ce type de livrable).

**Sortie** : `exigences_<client>.xlsx` (livrable interne, Contrat AO-1) à la racine de `appels-offres/<client>-<objet>/<AAAA-MM>/`, et `plan-presentation-content.md`/`plan-presentation-prompts.md` (livrable final, Contrat AO-2 de `PIPELINE_CONTRACTS.md`) dans son sous-dossier `livrables/` — l'ensemble distinct du dossier `formations/` du premier pipeline.

---

# Skill transverse : `design-system-extractor`

Skill invoquée à la demande, en amont de `slide-content-claude-design` — pas une étape obligatoire d'aucun des deux pipelines ci-dessus.

Extrait le design system d'un client à partir de **n'importe quel document réellement fourni** (captures d'écran, PDF de charte graphique, export Figma, site web, logo seul...) — jamais un format d'entrée imposé au client. Un token non observé dans les sources fournies n'est jamais deviné : il est marqué explicitement `NON DÉTERMINÉ`, garde-fou anti-hallucination central de cette skill.

**Sortie** : `design-systems/<client>/design-system.md` (Contrat DS-1 de `PIPELINE_CONTRACTS.md`), au même format que la section "Design system par défaut" de `slide-content-claude-design/SKILL.md` — cette dernière l'applique directement à la place de sa palette par défaut « Encre & Sauge » quand il existe, en comblant les champs `NON DÉTERMINÉ` restants avec les valeurs par défaut correspondantes.

# Modèle et niveau d'effort recommandés

**En pratique** : dans Claude Code, choisis **Sonnet 5** et le niveau d'effort **`high`** au démarrage de ta session (menu/commande de sélection du modèle et de l'effort de ton installation — le nom exact de cette commande dépend de la version de l'outil ; dans l'application Claude ou Cowork, le réglage équivalent se trouve dans les paramètres de conversation). C'est la seule chose à retenir pour un usage quotidien du pipeline ; le reste de cette section est une justification détaillée, utile si tu veux comprendre le "pourquoi" ou si tu contribues au dépôt — pas une lecture nécessaire avant de lancer une skill.

**Recommandation** : **Sonnet 5**, niveau d'effort **`high`**, pour l'ensemble des skills de ce dépôt — les 5 du pipeline formation (y compris `formation-pipeline` en mode orchestration), `reponse-appel-offres` du pipeline réponse à AO, et la skill transverse `design-system-extractor`. Ces dernières partagent le même profil de difficulté (extraction exhaustive contrainte par un format, deep research à plusieurs volets, jugement de fit et de sélection) — pas de recommandation distincte tant qu'aucune divergence réelle n'a été observée en usage. Compte tenu de sa longueur (8 étapes, plusieurs deep research successives, un livrable détaillé slide par slide), monter à **`xhigh`** sur `reponse-appel-offres` est aussi défendable que sur `comite-qualite` en dossier complet ou `formation-pipeline` en formation multi-jours (même emplacement de réglage) — voir le détail par cas ci-dessous.

**Escalade conditionnelle vers Opus** : rester sur Sonnet par défaut, mais basculer ponctuellement sur Opus (même sélecteur de modèle que ci-dessus, changer juste le nom du modèle pour la session ou l'étape concernée) pour les décisions les plus coûteuses à défaire une fois prises — la conception du cas fil rouge et de la roadmap en Phase 1 de `formation-material-builder` (la spec elle-même les qualifie de coûteuses à corriger après coup : « Mieux vaut 10 min de cadrage que 2h de retravail »), la recherche de participants dans `cadrage-formation` si l'audience est nombreuse/senior/multi-entités (zone d'ambiguïté la plus exposée au risque d'hypothèse présentée à tort comme un fait), ou un audit `comite-qualite` sur un livrable client/contractuel à fort enjeu. Ce n'est pas un changement de modèle par défaut sur toute une skill, seulement sur son point de décision le plus structurant.

Cette recommandation est vérifiable, pas une préférence : elle découle de choses observables dans ce dépôt (le texte des `SKILL.md` eux-mêmes, leurs propres garde-fous explicites), pas d'une règle générique — voir « Sur quoi se base cette recommandation, et ses limites » en fin de section (cette dernière sous-section s'adresse surtout à un contributeur qui voudrait comprendre ou faire évoluer la recommandation, pas à l'usage courant).

## Ce qui, dans ces skills, exige ce choix précis

Les 5 `SKILL.md` de ce dépôt partagent un même profil de difficulté, différent d'un classement rapide ou d'un problème de code isolé :

- **Du texte long et cohérent sur la durée** — un module de formation complet (`slides.md`, `notes-formateur.md`, un atelier, sa solution) doit rester cohérent avec le fil rouge et le plan validés en Phase 0, potentiellement des dizaines de milliers de tokens plus tôt dans la session.
- **Des contrats de fichier stricts, au format imposé au caractère près** — `PIPELINE_CONTRACTS.md` fixe précisément ce que doit contenir `00-brief.md`, `00-plan.md`, `M<n>-slides-content.md` ; `slide-content-claude-design/SKILL.md` impose des dimensions et couleurs exactes par slide. Un résumé approximatif d'un format aussi précis casse l'interface avec la skill suivante.
- **Des garde-fous imbriqués qu'il ne faut jamais lever par erreur** — `formation-pipeline/SKILL.md` distingue explicitement les blocages que l'orchestrateur peut lever de ceux qu'il ne peut jamais lever, y compris en mode non-stop ; `comite-qualite/SKILL.md` a des règles anti-théâtre précises (ne pas inventer de problème, mais ne pas non plus déclarer une convergence hâtive). Une lecture trop rapide de ces règles en cascade est justement le type d'erreur qu'on a corrigée lors de l'audit qualité de ce dépôt (contradiction non-stop/garde-fou, voir [`CHANGELOG.md`](CHANGELOG.md)).
- **Un jugement pédagogique et éditorial réel, pas de la simple extraction** — calibrer un niveau 100/200/300 selon Bloom, juger si une réponse client est réellement actionnable ou évasive, composer une équipe de relecteurs pertinente pour un livrable donné : ce sont des décisions de fond, pas du classement de texte.

## Pourquoi pas un autre modèle

- **Haiku (4.5)** — Haiku est conçu et positionné pour la vitesse et le coût sur des tâches courtes et répétitives à grande échelle (classification, extraction simple, routing) : c'est explicitement le compromis qu'il assume, au prix d'une profondeur de raisonnement moindre sur des tâches longues et enchevêtrées. Rien dans ce dépôt ne relève de ce profil — même l'étape la plus mécanique (`cadrage-formation` Étape 3, recherche de profils) exige un jugement sur l'ambiguïté ("À confirmer" plutôt qu'inventer) que ce classement rapide ne priorise pas. Utiliser Haiku ici économiserait des tokens au prix d'un risque concret : un format de fichier mal respecté (Contrat 2, 3 ou 4 de `PIPELINE_CONTRACTS.md`) casserait silencieusement l'étape suivante du pipeline, ou une des règles anti-théâtre de `comite-qualite` serait appliquée de façon trop mécanique (inventer des problèmes pour "faire le travail", ou au contraire déclarer une convergence hâtive).
- **Opus (5)** — Opus vise les tâches où une réponse fausse coûte cher et où le raisonnement multi-étapes est la difficulté centrale (debugging profond, architecture complexe, preuve mathématique) — c'est le palier de raisonnement au-dessus de Sonnet dans la gamme, sous Fable (voir ci-dessous), pas le plafond absolu. Les skills de ce dépôt ne sont pas de ce registre : la difficulté n'est pas dans un raisonnement logique en profondeur, elle est dans le respect méticuleux et répété d'un format de spec déjà écrit, sur un grand volume de texte à produire. Opus n'apporterait pas un avantage identifiable sur ce type de tâche par rapport à Sonnet, pour un coût par token nettement supérieur — un delta de qualité qui ne se traduirait pas en meilleure conformité aux contrats de fichier ni en meilleure fidélité pédagogique, les deux vrais points de friction observés dans ce dépôt (voir l'audit qualité du [`CHANGELOG.md`](CHANGELOG.md), dont les corrections portaient sur la cohérence de spec, pas sur un raisonnement insuffisamment profond).
- **Fable (5)** — c'est le modèle le plus capable disponible, positionné pour les tâches qui justifient une prime de coût significative sur la sortie la plus soignée possible (contexte 1M token, mais facturé en conséquence). Le contenu produit ici (slides, ateliers, quiz) a une exigence de qualité réelle, mais elle est bornée par un format déjà écrit dans les `SKILL.md`/`PIPELINE_CONTRACTS.md` — la marge de progression qu'apporterait Fable au-delà de Sonnet 5 sur *ce type de tâche contrainte* n'est pas justifiée au vu du volume de contenu à produire sur une formation multi-jours (plusieurs modules × plusieurs livrables). Fable se justifierait si ce dépôt produisait, par exemple, un unique document stratégique très court où chaque phrase compte au maximum — ce n'est pas le profil de ce pipeline.

## Pourquoi pas un autre niveau d'effort

- **`low`** — pensé pour des tâches courtes, mécaniques, où la vitesse prime (voir la doc Anthropic sur les niveaux d'effort). Aucune des 5 skills n'est courte : même `cadrage-formation` seule enchaîne 8 étapes avec recherche web et synthèse. `low` produirait des livrables qui respectent la forme sans forcément le fond (ex. un plan de formation qui liste des modules sans la logique de progression qu'on vient d'exiger explicitement dans `formation-material-builder/SKILL.md`).
- **`medium`** — le niveau "tâches quotidiennes, coûts maîtrisés" est raisonnable pour un usage ponctuel et simple, mais sous-dimensionné pour un pipeline dont chaque étape peut réécrire un format de fichier lu par l'étape suivante : le risque de dérive de contrat (cf. § ci-dessus) est plus élevé qu'à `high`.
- **`xhigh` par défaut sur toutes les skills** — c'est le niveau recommandé pour les tâches exploratoires et les usages d'agent complets (appels d'outils répétés, recherche approfondie), mais l'appliquer par défaut à chaque étape du pipeline (y compris les plus courtes, comme relire un seul module déjà calibré) consommerait des tokens sans bénéfice mesurable — la plupart des étapes de ce pipeline suivent un format déjà écrit, elles n'ont pas besoin d'une exploration plus profonde que `high`. `xhigh` reste justifié spécifiquement sur `comite-qualite` en dossier complet et sur `formation-pipeline` en formation multi-jours (voir recommandation ci-dessus), où le volume d'allers-retours et de garde-fous à respecter simultanément est le plus élevé. Ceci tranche le choix de *modèle et d'effort* pour `comite-qualite` — distinct du point de vigilance encore ouvert dans `BACKLOG.md` (item #13) sur le *critère d'arrêt de sa boucle de convergence*, qui reste à observer empiriquement quel que soit le modèle utilisé.
- **`max`** — la documentation Anthropic est explicite sur ce niveau : il n'a pas de plafond de dépense de tokens, mais les gains sont marginaux au-delà de `xhigh` et il est sujet au sur-raisonnement ("overthinking"). Sur des skills dont la difficulté est le respect d'un format déjà écrit (pas une énigme à résoudre), `max` ferait dépenser des tokens sans lever la vraie contrainte du pipeline.
- **Ultracode (workflow multi-agents)** — Ultracode envoie `xhigh` au modèle tout en orchestrant un workflow multi-agents pour la tâche *(fonctionnalité de Claude Code, distincte des 5 niveaux d'effort standard — pas nécessairement documentée dans la même page que ceux-ci, à vérifier dans la doc Claude Code à jour si le comportement décrit ici semble avoir changé)*. C'est pertinent pour un audit exhaustif nécessitant des perspectives indépendantes qui se vérifient entre elles (exactement ce qui a été fait pour l'audit `comite-qualite` de ce dépôt, avec 7 relecteurs en parallèle) — mais ce n'est pas le mode par défaut pour produire un module de formation ou un cadrage : ce travail est une production cohérente et séquentielle (un fil rouge qui se déroule, un plan qui se construit progressivement), pas un problème qui bénéficie de plusieurs angles indépendants à faire converger. Réserver Ultracode à un usage explicite et ponctuel — un audit `comite-qualite` volontairement exhaustif — plutôt qu'un mode par défaut du pipeline.

## Mécanique vs jugement, à l'intérieur de chaque skill

`high` n'a pas besoin d'être appliqué avec la même intensité sur tout le déroulé d'une skill — chacune mélange des passages purement mécaniques (remplir un gabarit déjà entièrement spécifié, exécuter un script) et des passages de jugement ouvert où une dérive coûte cher. Si l'outil que tu utilises permet de faire varier l'effort en cours de route, voici où il compte le plus dans chaque skill :

- **`cadrage-formation`** — mécanique : créer le dossier (Étape 0), exécuter `generate_cadrage_xlsx.py` une fois le JSON validé (Étape 6) ; jugement : la lecture du contexte (Étape 1), la recherche par participant avec discipline de hedging (Étape 3 — la plus exigeante : marquer "à confirmer" plutôt qu'inventer), les recherches client/sujet (Étapes 4-5), la priorisation et justification des questions (Étape 6).
- **`formation-material-builder`** — mécanique : la génération du `.pptx` (Phase 3.1, un « brouillon jetable » assumé comme tel), la conversion HTML des énoncés (3.1bis, gabarit repris tel quel), la majeure partie de la conversion du corpus en formats réalistes (3.1ter) ; jugement : la construction du brief/plan en Phase 0 (calibrage Bloom, progression inter-modules — voir plus haut), la conception du fil rouge et de la roadmap (Phase 1), le module 1 comme gabarit de calibration, l'ancrage causal de chaque atelier dans le fil rouge.
- **`slide-content-claude-design`** — mécanique : le remplissage du gabarit `Slide N`, la reprise des tokens couleur déjà inlinés, la reprise à l'identique des dimensions entre les deux fichiers ; jugement : l'établissement de la métaphore filée globale (une seule fois, jamais réinventée en cours de route), le bloc Direction artistique par module, la décision de fallback image vs vectoriel par slide.
- **`comite-qualite`** — mécanique : la Phase C (application des corrections déjà décidées, dans l'ordre 🔴→🟠→🟡) ; jugement : la composition de l'équipe de relecteurs (Phase 0.1-0.3, y compris le garde-fou anti-hallucination du rôle "Voix du client"), les constats de chaque relecteur et le calibrage défaut-vs-préférence (Phases A/D) — ce dernier revient à chaque itération de la boucle, jusqu'à 3.
- **`formation-pipeline`** — mécanique : la détection d'état du workspace (table de détection, la plupart des transitions) ; jugement : reconnaître un garde-fou que la sous-skill a posé comme non contournable (voir la contradiction corrigée dans [`CHANGELOG.md`](CHANGELOG.md)) — c'est le point où une lecture trop rapide des règles en cascade a le plus de conséquences.

## Sur quoi se base cette recommandation, et ses limites

**Ceci est une analyse de tâche, pas un benchmark.** Aucun test A/B n'a été mené comparant Haiku, Sonnet, Opus ou Fable sur ces 5 skills, ni sur un cas de formation réel. Chaque affirmation ci-dessus vient de la lecture des `SKILL.md` eux-mêmes — leurs étapes explicites, leurs propres garde-fous déjà écrits dans les specs (la règle de hedging de `cadrage-formation`, la règle anti-théâtre de `comite-qualite`, le point de validation du module 1 de `formation-material-builder`, la distinction garde-fou-levable/non-levable de `formation-pipeline`) — croisée avec des paliers de capacité de modèle connus de façon générale (Haiku : rapide/économique, plus faible sur la cohérence longue durée et le jugement ouvert ; Sonnet : généraliste, palier par défaut pour la plupart des tâches agentiques de rédaction/code ; Opus : plafond de raisonnement le plus élevé ; Fable : profil différencié, pas le choix par défaut pour ce type de pipeline sauf demande explicite) et sur les niveaux d'effort tels que documentés par Anthropic à la date de rédaction (29/07/2026).

**Ce n'est pas un verdict permanent.** À affiner avec un retour d'usage réel : si un run Sonnet dérive visiblement sur la continuité du fil rouge d'un module à l'autre, si un run Haiku (testé malgré la recommandation ci-dessus) rate un appel de fallback évident, ou si une boucle `comite-qualite` brûle 3 itérations sur des constats cosmétiques — ce sont des signaux concrets à partir desquels ajuster cette recommandation, pas à traiter cette section comme figée. Si une évolution future du pipeline introduit une tâche de raisonnement multi-étapes réellement profond (ex. un calcul complexe dans un exercice), ou si une nouvelle génération de modèles change ces caractéristiques, réévaluer ce choix plutôt que de le considérer comme acquis indéfiniment. Chaque `SKILL.md` fonctionne techniquement avec n'importe quel modèle Claude compatible avec les skills Claude Code — un modèle moins capable ne bloque rien, mais demande probablement plus de relecture et de correction manuelle.

Le format exact de chaque fichier échangé entre les skills (celles orchestrées par `formation-pipeline` comme celles utilisées seules) est documenté dans [`PIPELINE_CONTRACTS.md`](PIPELINE_CONTRACTS.md) — utile si tu veux comprendre précisément ce que produit une étape avant de la passer à la suivante.

---

# Mise en place technique (une seule fois)

> **Cette partie est technique et ponctuelle.** Elle suppose que Claude Code est installé sur ton poste. **Si ce n'est pas le cas, ou si les termes ci-dessous (terminal, dépôt, extension, palette de commandes…) ne te parlent pas, fais-toi accompagner par un collègue technique pour cette étape unique.** Une fois en place, l'usage quotidien décrit plus haut se fait en français, sans manipulation technique.

## Où récupérer les skills (source de vérité)

**Ce dépôt est la référence unique** pour récupérer les skills des deux pipelines — ne pas se fier à un envoi ponctuel par e-mail ou par zip, qui peut être partiel ou périmé. Toute évolution des skills est poussée ici avant d'être considérée comme disponible.

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
│   ├── SKILL.md
│   └── scripts/             (génération auto des illustrations, optionnel)
├── comite-qualite/
│   └── SKILL.md
├── formation-pipeline/      (optionnel — orchestrateur du pipeline complet)
│   └── SKILL.md
├── reponse-appel-offres/    (pipeline réponse à AO)
│   ├── SKILL.md
│   ├── references/          (gabarit de profil cabinet)
│   └── scripts/             (générateur de la checklist d'exigences Excel)
└── design-system-extractor/ (transverse aux deux pipelines, à la demande)
    └── SKILL.md
```

**Détection** : si `~/.claude/skills/` existe déjà, l'ajout d'un dossier de skill est pris en compte **en direct, sans redémarrer la session en cours**. Un redémarrage n'est nécessaire que si `~/.claude/skills/` lui-même n'existait pas encore au lancement de la session (premier usage sur un poste neuf). Invocation : `/cadrage-formation`, `/formation-material-builder`, `/slide-content-claude-design`, `/comite-qualite`, `/formation-pipeline`, `/reponse-appel-offres`, `/design-system-extractor` (ou en langage naturel — chaque SKILL.md décrit ses déclencheurs). Vérifier la détection en tapant `/` dans le chat : les skills installées doivent apparaître dans la liste.

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

**Choix de l'éditeur** : l'extension Claude Code fonctionne aussi bien dans VS Code que dans Antigravity — le choix entre les deux est une préférence d'environnement, pas une contrainte du pipeline. Voir `BACKLOG.md` (item #7) : arbitrage rendu le 26/08/2026, les deux outils restent supportés en interne, pas de convergence vers un seul.

### Sur l'application Claude (claude.ai, app desktop/mobile)

L'application Claude installe les skills **une par une, par fichier ZIP**, via **Réglages → Personnaliser → Skills**. C'est un mécanisme différent de Claude Code (pas de simple copie de dossier).

1. **Activer d'abord** l'option « Exécution de code et création de fichiers » dans les réglages (nécessaire aux comptes Pro/Max/Team/Entreprise pour que les skills fonctionnent).
2. **Préparer le ZIP** pour chaque skill à installer : le ZIP doit contenir le **dossier de la skill à sa racine** (pas son contenu nu à la racine du zip), et le nom de ce dossier doit correspondre exactement au `name:` du frontmatter du `SKILL.md`. Les sous-dossiers (`references/`, `scripts/`) sont inclus tels quels. Depuis ce dépôt : `cd ~/.claude/skills && zip -r cadrage-formation.zip cadrage-formation/` (répéter pour chaque skill à installer, ou zipper directement depuis une copie locale du dépôt).
3. **Réglages → Personnaliser → Skills → bouton "+" → Create skill → Upload a skill**, puis sélectionner le ZIP correspondant. Répéter pour chaque skill à installer.

**Par défaut, chaque personne importe son propre ZIP.** Mais sur un compte **Team ou Enterprise**, un **Owner** peut provisionner une skill pour toute l'organisation en une fois, sans que chaque membre ait à l'installer individuellement : *Réglages d'organisation → Skills → Organization skills → « + Add »*, en uploadant le même ZIP. La skill apparaît alors automatiquement chez chaque membre (activée par défaut, désactivable individuellement). Si un compte professionnel Team/Enterprise est disponible, **demander à la personne Owner de provisionner les skills utilisées par l'équipe en une seule fois** plutôt que de les faire installer individuellement. *(Point à vérifier : la documentation développeur Anthropic — platform.claude.com — affirme encore qu'aucune gestion centralisée n'existe sur claude.ai, ce qui contredit la doc support — support.claude.com/en/articles/13119606 — décrivant ce mécanisme de provisioning. Les deux pages ne semblent pas synchronisées ; se fier en priorité à la doc support, plus récente sur ce point, mais confirmer auprès d'un Owner du compte avant de compter dessus pour un déploiement d'équipe.)*

### Sur Claude Cowork

Cowork tourne dans l'application Claude. **Ce qui suit est une supposition raisonnable, pas un fait confirmé par une source Anthropic officielle** (aucune documentation trouvée ne détaille explicitement comment Cowork charge les skills) : Cowork chargerait les mêmes skills que celles installées sur le compte claude.ai (donc la procédure « Sur l'application Claude » ci-dessus s'appliquerait aussi à Cowork), sans lire `~/.claude/skills/` sur le poste. **À vérifier en conditions réelles** avant de s'y fier : installer une skill via la procédure ci-dessus, puis confirmer qu'elle apparaît bien dans une session Cowork.

## Ouvrir les fichiers `.xlsx` générés (`cadrage-formation`)

`cadrage-formation` produit un livrable `.xlsx`. Pour l'ouvrir sans quitter VS Code / Antigravity :

- Installer une extension de visualisation Excel pour VS Code (ex. « Excel Viewer » ou équivalent disponible sur le marketplace de l'éditeur).
- Une fois installée, ouvrir directement le fichier `.xlsx` généré depuis l'explorateur de fichiers de l'éditeur : il s'affiche en tableau dans un onglet, sans lancer d'application externe.
- Alternative sans extension : ouvrir le fichier directement depuis Google Drive si le dossier de formation y est synchronisé (cf. convention de rangement des livrables).

## Notes diverses

- Ces quatre skills fonctionnent aussi indépendamment les unes des autres. `formation-pipeline` (mode bout-en-bout) est additionnelle et optionnelle.
- `cadrage-formation` : le script `scripts/generate_cadrage_xlsx.py` nécessite Python avec `openpyxl` (génération du fichier Excel).
- `slide-content-claude-design` : le script optionnel `scripts/generate_illustrations.py` (mode génération automatique des illustrations) nécessite Python avec `google-genai` et une clé d'API Gemini valide dans la variable d'environnement `GEMINI_API_KEY`.
- `reponse-appel-offres` : le script `scripts/generate_exigences_xlsx.py` nécessite Python avec `openpyxl`, même dépendance que `cadrage-formation`.

Pour l'historique daté des évolutions du pipeline, voir [`CHANGELOG.md`](CHANGELOG.md).
