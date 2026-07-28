# Backlog — Pipeline de skills de formation

Sources :
- Sessions de démo internes du pipeline `cadrage-formation` → `formation-material-builder` → `slide-content-claude-design` → `comite-qualite`, retours d'usage recueillis auprès des contributeurs et utilisateurs du pipeline.
- Interviews de spécification menées avec le porteur du pipeline pour cadrer les stories US-10 à US-12 (séparation contenu Claude Design / prompts Gemini, direction artistique des illustrations, cas fil rouge et ateliers structurés) et audits comité qualité associés.
- Demande explicite du porteur du pipeline du 28/07/2026 (gouvernance du dépôt : licence, changelog, wiki ; documentation d'installation multi-surface).

Priorisation façon PO : `P0` = bloquant/dette qui casse la démo ou l'adoption, `P1` = valeur claire à court terme, `P2` = amélioration UX/confort, `P3` = exploratoire/à cadrer. Chaque item porte une estimation d'effort (S/M/L) et ses dépendances.

---

## P0 — Bloquants adoption

### 1. Fiabiliser l'enregistrement des skills en session Claude Code
**Constat** : un utilisateur ne parvient pas à faire persister les skills entre sessions — nécessite de recréer un nouveau chat pour que les skills soient détectées après chaque redémarrage.
**Valeur** : sans ça, chaque nouvel utilisateur bute sur l'onboarding avant même de commencer.
**Action** : documenter (ou automatiser) la procédure d'enregistrement des skills — `~/.claude/skills/` en mode "auto" — et vérifier qu'un restart de session suffit sans recréer un chat.
**Effort** : S — c'est en grande partie déjà écrit dans le `README.md` (section Installation) ; il manque un test de non-régression + un mot sur le mode "auto".

### 2. Réparer/vérifier l'accès aux ressources sur le dépôt partagé
**Constat** : un livrable de formation censé être disponible sur le dépôt partagé s'est avéré absent malgré un lien envoyé à plusieurs reprises par un autre canal — un contributeur confirme un accès au dépôt mais sans fichier visible initialement.
**Valeur** : bloque tout collaborateur qui n'a pas reçu le livrable par un canal parallèle — le dépôt doit être la source de vérité.
**Action** : pousser systématiquement les livrables de formation sur le dépôt partagé dès leur production ; vérifier ensuite l'accès depuis un compte tiers (pas seulement celui qui a poussé le fichier).
**Effort** : S.

---

## P1 — Valeur court terme (évolutions de skills demandées explicitement)

### 19. `slide-content-claude-design` — séparer le contenu Claude Design du prompt illustration Gemini
**Constat** (interview de spécification US-10, à la suite d'une démo interne) : actuellement les slides.md générées contiennent le contenu textuel et les prompts d'illustration mélangés, ce qui rend difficile de :
  - Fournir le contenu structuré à Claude Design (sans distraction des prompts Gemini)
  - Générer les prompts d'illustration via Gemini avec contexte d'un prompt structuré et validé
  - Auditer l'UX/UI des slides *avant* la génération visuelle (les placeholders n'ont pas de dimensions explicites)
**Valeur** : clarifie le flux de travail (slides.md → Claude Design / prompts.md → Gemini), permet un audit UX/UI préalable à la génération, et aligne les prompts d'illustration sur le design system avec tokens exacts et règles visuelles précises (pas de texte dans l'image, baisser complexité, pas de bleu marine (#2C5F8A) sauf accents clés).
**Action** :
  - Modifier `slide-content-claude-design/SKILL.md` pour produire deux fichiers par module : `M<n>-slides-content.md` (contenu Claude Design avec, par slide, un placeholder gris aux dimensions exactes et à la position de l'image attendue) et `M<n>-prompts.md` (prompts Gemini structurés par slide, respectant la palette par défaut exacte).
  - Chaque slide du `M<n>-slides-content.md` inclut un bloc de placeholder gris avec dimensions exactes, position sur la slide, et lien vers le prompt correspondant dans `M<n>-prompts.md`.
  - Les deux fichiers sont colocalisés dans `/livrables/` selon la convention de formation.
  - Les prompts Gemini intègrent les tokens par défaut exacts (bleu marine #2C5F8A, corail #D97757, vert sauge #4A8B6F) et les garde-fous visuels (aucun texte, pas de doublon texte/image, zéro faute).
**Effort** : M — refonte du format de sortie de la skill, mais la logique pédagogique reste inchangée.
**Dépend de** : rien (amélioration de workflow transverse à Horizon 1/2).

### 3. `cadrage-formation` — détecter et proposer les formations antérieures similaires
**Constat** : retour d'usage récurrent — un contributeur suggère d'intégrer une vérification automatique des formations existantes au sein du skill de cadrage. Objectif : que l'agent demande "as-tu une formation déjà faite qui est proche ?", puis, si on lui donne accès à un répertoire de formations passées, qu'il propose lui-même la plus pertinente — **à valider par l'utilisateur, jamais appliquée automatiquement** (risque de réutiliser un gabarit inadapté sans validation).
**Valeur** : accélère le cadrage de nouvelles sessions d'une formation récurrente (ex. une deuxième session du même client quelques mois plus tard) en réutilisant un gabarit existant au lieu de repartir from scratch, tout en évitant la dérive déjà constatée quand un profil non pertinent avait été réutilisé par erreur (ex. profils BA/UX proposés alors que l'audience réelle était BO).
**Enrichissement** : illustre l'enjeu plus large d'un cadrage mal validé, indépendamment de la réutilisation d'une formation passée — sur une formation réelle, un mismatch initial sur l'objectif pédagogique (compréhension confuse entre "apprendre à gérer des projets d'IA" et "apprendre à utiliser l'IA pour être plus efficace dans son rôle") a fait dériver tout le plan de formation, avec des reliquats de contenu mal orienté qui ont dû être corrigés après coup. Ceci renforce la nécessité, déjà actée dans `cadrage-formation`, de ne jamais présenter une hypothèse comme un fait et de faire valider explicitement le plan de formation par le client avant de lancer la production détaillée (comportement déjà en place selon les démos internes, à vérifier qu'il est bien systématique).
**Action** :
  - Ajouter une question explicite en début de `cadrage-formation` : "Existe-t-il une formation antérieure proche de ce besoin ?"
  - Si oui → l'agent scanne un répertoire de formations passées fourni par l'utilisateur et propose 1–3 candidats avec justification (profil participants, thématique, niveau).
  - L'utilisateur valide avant que l'agent ne s'en serve de base.
**Effort** : M — nécessite d'ajouter une étape de discovery + un prompt de scan de répertoire dans `cadrage-formation/SKILL.md`.
**Dépend de** : #2 (les formations passées doivent être accessibles quelque part de stable, pas juste dans des envois ponctuels).

### 4. Proposer systématiquement les prochaines étapes après génération de contenu
**Constat** : retour d'usage récurrent — plusieurs utilisateurs demandent que l'agent propose systématiquement les prochaines étapes de création après la génération du contenu. Observé concrètement : certains environnements le font spontanément (proposer un choix explicite entre plusieurs livrables possibles à produire ensuite) alors que d'autres ne le proposent pas nativement (comportement qui dépend du modèle et de l'environnement utilisés).
**Valeur** : réduit la charge cognitive de l'utilisateur (perte de repère sur la prochaine action quand plusieurs sessions tournent en parallèle) et rend le pipeline plus guidé pour un nouvel utilisateur — cœur du besoin d'onboarding exprimé par les utilisateurs.
**Action** : ajouter en fin de chaque skill du pipeline (`cadrage-formation`, `formation-material-builder`, `slide-content-claude-design`, `comite-qualite`) un bloc explicite proposant l'étape suivante (avec les options possibles), indépendamment du modèle utilisé.
**Effort** : M — un ajout de type "next steps" en fin de chaque `SKILL.md`, mais à répercuter sur 4 skills.
**Dépend de** : rien, mais complète naturellement #3.

### 5. Uniformiser le rangement des livrables par formation
**Constat** : rangement actuel non structuré — chaque formation est rangée manuellement dossier par dossier, sans convention partagée, notamment pour distinguer plusieurs sessions de la même formation dans le temps (ex. une même formation redonnée à quelques mois d'écart pour le même client).
**Valeur** : évite la perte de contexte en collaboratif (accès et versions dupliquées) et facilite la réutilisation par #3.
**Action** : définir une convention de nommage/arborescence (ex. `formations/<client>-<thème>/<AAAA-MM>/`) et l'intégrer comme étape de `cadrage-formation` (création du dossier dès le cadrage) plutôt qu'en fin de pipeline.
**Effort** : S/M — convention à documenter + petit ajustement du prompt de création de dossier dans la skill.
**Dépend de** : aucune, mais facilite #3 et #2.

### 14. Packager le workflow complet comme asset transmissible (skills + enchaînement + mode d'emploi)
**Constat** : retour d'usage — besoin exprimé d'un support récapitulatif du déroulé du pipeline (skill par skill, avec les points de validation) présentable en début de démo pour un nouvel arrivant, allant au-delà de la simple formation produite : le pipeline lui-même (les skills, leur combinaison, le processus) devient un actif à part entière. Le `README.md` actuel du dépôt couvre déjà une bonne partie de ce besoin (description des 4 skills et de leur enchaînement) mais n'est pas pensé comme un support de présentation/onboarding en tant que tel.
**Valeur** : transforme le pipeline d'un savoir-faire individuel (aujourd'hui largement documenté dans la tête du porteur du pipeline et démontré oralement) en un actif d'équipe réellement transmissible sans reproduire une session de démo à chaque nouvel arrivant.
**Action** : produire, à partir du `README.md` existant, un support visuel court (1 schéma + 1 page) du pipeline complet (skill par skill, entrées/sorties, points de validation humaine), destiné à être montré en 5 minutes à un nouvel arrivant avant qu'il n'installe quoi que ce soit.
**Effort** : S/M — capitalise sur le contenu déjà écrit dans le `README.md`, essentiellement un travail de mise en forme et de synthèse.
**Dépend de** : US-1/US-2 (Horizon 1) pour que ce support pointe vers un pipeline effectivement installable sans friction.

### 24. Standardiser les fichiers de gouvernance du dépôt (LICENSE, CHANGELOG, wiki) ✅ Fait le 28/07/2026
**Constat** (demande utilisateur du 28/07/2026) : le dépôt n'avait ni fichier de licence explicite (statut juridique du contenu non clarifié), ni historique de version au format standard (les évolutions étaient notées en prose libre dans une section « Notes de version » du `README.md`, mêlant contenu daté et notes intemporelles), ni point d'entrée pour un consultant qui ne clone pas le dépôt Git (le README suppose l'accès au dépôt).
**Valeur** : clarifie le statut d'usage du dépôt ; sépare l'historique daté (référence exhaustive) du README (guide d'usage) — chacun reste plus lisible pour son objectif ; donne un point d'entrée navigable (wiki) à quelqu'un qui n'a pas besoin de cloner le dépôt pour comprendre comment s'en servir, complémentaire à l'item #14 (support de présentation).
**Action** :
  - `LICENSE.md` : mention de propriété claire, clause de non-réalité des données client (cohérente avec `fil_rouge_design.md`).
  - `CHANGELOG.md` : extraction et réorganisation de l'ancienne section « Notes de version » du README au format Keep a Changelog (entrées datées, catégorisées Ajouté/Corrigé) ; le README ne garde que les 2 notes intemporelles et un lien vers ce fichier.
  - 4 pages de contenu pour un wiki (Accueil, Installation, Utiliser-le-pipeline, FAQ-et-depannage), rédigées à partir du contenu existant du README (pas de divergence de fond).
**Effort** : S — documentation uniquement, aucun changement de comportement des skills.
**Dépend de** : rien.

### 15. Formaliser un SDLC et une gouvernance de cycle de vie pour les skills (création, version, dépréciation, responsabilité)
**Constat** : retour d'usage relayant un besoin identifié ailleurs dans l'organisation, sur la nécessité d'un cycle de vie explicite par asset ("delivery life cycle" à monter sur les différents assets produits). Ce sujet est distinct de l'item #1 (qui porte sur la fiabilité *technique* de l'enregistrement d'une skill en session) : ici il s'agit de gouvernance organisationnelle — qui décide qu'une skill est mature, qui la fait évoluer, comment une version dépréciée est signalée aux utilisateurs.
**Valeur** : évite que le pipeline ne repose que sur la disponibilité d'une seule personne pour trancher toute évolution, et donne une réponse claire quand plusieurs contributeurs modifient une même skill en parallèle.
**Action** : ce sujet dépasse le scope d'un seul item de backlog produit — voir `GOVERNANCE.md`, qui documente désormais un cycle retour d'usage → item de backlog → story → implémentation ; à enrichir d'une notion explicite de version de skill si le nombre de contributeurs augmente.
**Effort** : M — davantage une clarification organisationnelle qu'un développement.
**Dépend de** : rien, mais conditionne la scalabilité de #14 et de l'ensemble de la gouvernance si l'équipe de contributeurs s'élargit au-delà des 3 actuels.

### 16. Intégrer le "personnage" (personnalité) d'un interlocuteur client au comité qualité ✅ Fait le 24/07/2026 (spec)
**Constat** : retour d'usage — proposition d'extraire, à partir des entretiens de cadrage, le "personnage" de l'interlocuteur client et de l'intégrer comme référence au comité qualité, pour vérifier que le contenu produit correspond bien à ce que cette personne a exprimé.
**Valeur** : renforce la fidélité du contenu final aux attentes exprimées par un interlocuteur spécifique, au-delà de la cohérence pédagogique générale déjà couverte par les rôles existants du comité (directeur pédagogique, expert technique, UX).
**Action** : évaluer l'ajout d'un rôle "voix du client" au comité qualité, alimenté par les notes d'entretien de cadrage (donc dépendant de la qualité des livrables de `cadrage-formation`).
**Effort** : M — ajout d'un rôle de relecteur dans `comite-qualite/SKILL.md`, mais nécessite de bien cadrer la source (entretien retranscrit ou résumé) pour éviter d'halluciner une personnalité à partir de peu d'éléments.
**Dépend de** : qualité et disponibilité des notes d'entretien produites par `cadrage-formation`.
**Statut** : rôle "Voix du client" ajouté dans `comite-qualite/SKILL.md` (table des rôles conditionnels + garde-fou explicite anti-hallucination : ne s'active que si des notes d'entretien réelles existent). Reste à vérifier sur un cas réel avec notes de cadrage disponibles.

### 6. Clarifier la source d'audit du `comite-qualite` avant lancement
**Constat** : question récurrente restée sans réponse ferme — "le quality check, il est basé sur quoi ? Les slides.md ou la présentation elle-même ?". Le porteur du pipeline confirme qu'aujourd'hui l'audit porte sur les `*.md` (slides, exercices, notes formateur) et non sur le rendu final en Claude Design.
**Valeur** : évite un audit "aveugle" au rendu visuel final (mise en page, respect charte) alors que le contenu textuel est déjà validé — actuellement une zone grise pour un nouvel utilisateur.
**Action** : ajouter en tête de `comite-qualite/SKILL.md` une question explicite : "Quel périmètre dois-je auditer : le contenu markdown, la présentation générée, ou les deux ?"
**Effort** : S.
**Dépend de** : rien.

---

## P2 — Confort / harmonisation outillage

### 7. Harmoniser Claude Code vs Claude Desktop en interne
**Constat** : clivage observé dans l'équipe entre utilisateurs "Claude Code only" et "Claude Desktop only" — action déjà assignée en interne pour évaluer des solutions d'harmonisation.
**Valeur** : réduit la friction d'onboarding et le nombre de chemins différents à documenter/maintenir pour un même pipeline de skills.
**Action** : évaluer les options (formation croisée, guide de choix par profil "dev vs non-dev", ou convergence vers un seul outil) — à formaliser suite à un retour d'usage terrain.
**Effort** : L — dépend de la décision d'outillage, hors du seul périmètre des skills.

### 8. Documenter le paramétrage de l'extension Claude Code dans un IDE
**Constat** : un utilisateur a perdu un temps significatif en démo pour connecter son compte pro à l'extension Claude Code dans son IDE (icône à utiliser, lien d'authentification, gestion des quotas) — souci récurrent de blocage sur les quotas côté comptes pro.
**Valeur** : cet irritant, non lié aux skills elles-mêmes, ralentit tout nouvel arrivant qui suit la démo comme onboarding — objectif explicite de l'enregistrement de cette session.
**Action** : ajouter un mini-guide (setup extension, compte pro vs perso, gestion des quotas) en complément du `README.md` du pipeline, ou en pré-requis du premier skill.
**Effort** : S.
**Dépend de** : #7 dans une certaine mesure (si l'outillage cible change, ce guide change aussi).

### 9. Explorer une génération d'illustrations moins manuelle
**Constat** : point de friction répété — la génération d'images reste la partie la plus chronophage et manuelle du pipeline. Le porteur du pipeline exporte vers Gemini avec un prompt fixe ("illustration éditoriale moderne et épurée"), jugé plus joli que les images générées nativement par Claude. Un autre outil de génération d'images est évoqué comme alternative pour générer un lot d'images cohérentes en une fois.
**Valeur** : gain de temps potentiel significatif sur le poste le plus manuel du pipeline actuel — mais reconnu comme nécessitant un vrai arbitrage qualité (le style "sketch/architecture" est valorisé).
**Action** : cadrer un petit spike de comparaison (Claude natif / Gemini / autre outil) sur un même jeu de slides, avec le prompt déjà capitalisé ("illustration éditoriale moderne et épurée" / "sketch, esquisse type Excalidraw" pour les schémas), avant de décider d'un outil par défaut.
**Effort** : M — nécessite un spike comparatif, pas juste une modif de skill.
**Dépend de** : rien, mais impacte potentiellement `slide-content-claude-design`.

### 10. Fiabiliser l'ouverture de fichiers Excel en environnement de développement
**Constat** : friction mineure observée en usage réel — un utilisateur doit s'y reprendre pour ouvrir le `.xlsx` généré par `cadrage-formation` (extension dédiée aux fichiers Excel suggérée pour l'environnement de développement utilisé).
**Valeur** : petit irritant UX répété à chaque exécution de `cadrage-formation`, qui produit justement un livrable `.xlsx`.
**Action** : documenter dans le `README.md` ou le `SKILL.md` de `cadrage-formation` l'extension recommandée pour visualiser un `.xlsx` sans sortir de l'environnement de travail.
**Effort** : S.
**Dépend de** : rien.

### 21. `slide-content-claude-design` — direction artistique cohérente et professionnelle des illustrations
**Constat** (interview de spécification US-11) : les illustrations générées via Gemini manquent aujourd'hui de deux choses à la fois — (1) une cohérence de style d'une slide à l'autre (chaque prompt est pensé isolément, sans référence à un standard visuel partagé), et (2) un ancrage systématique dans la métaphore filée de la formation quand elle existe. Résultat : des illustrations qui ont l'air de sorties indépendantes d'un générateur plutôt que d'un jeu cohérent conçu par un même directeur artistique.
**Valeur** : des slides visuellement plus professionnelles et mémorables, où l'illustration renforce l'arc narratif de la formation au lieu d'être un décor interchangeable — bénéfice direct sur la perception qualité par le client, sans coût de production supplémentaire (un seul bloc de contexte en plus par module).
**Action** :
  - Ajouter à `slide-content-claude-design/SKILL.md` un bloc **« Direction artistique »**, généré une fois par module et placé en tête de `M<n>-prompts.md`, qui fixe : le style illustratif (traits, texture, niveau de rendu), la déclinaison de la métaphore filée pour ce module, et les contraintes visuelles récurrentes (palette, absence de texte, niveau de détail).
  - Chaque prompt de slide référence ce bloc au lieu de répéter des instructions de style ad hoc, garantissant la même "patte" sur toutes les illustrations d'un module.
  - Le bloc peut varier légèrement d'un module à l'autre (ex. un sous-thème visuel propre au module) mais reste ancré dans la même métaphore filée globale de la formation.
**Effort** : M — ajout d'une section de gabarit + adaptation du template de prompt existant pour qu'il s'y réfère.
**Dépend de** : US-10 (#19), dont ce backlog item prolonge directement le format `M<n>-prompts.md`.

### 22. `formation-material-builder` — cas fil rouge unique et exercices structurés façon StockPilot
**Constat** (interview de spécification US-12, à partir du cas de référence `fil-rouge-stockpilot/`) : les exercices produits aujourd'hui par `formation-material-builder` (un `exercices.md` par module, sans fil narratif commun) fonctionnent mais perdent l'opportunité pédagogique d'un cas fictif filé sur toute la formation — un même produit/contexte qui se développe atelier après atelier, où chaque exercice s'appuie sur l'état du cas laissé par le précédent. Le cas `fil-rouge-stockpilot` (structure `atelier-N/` avec corpus dédié + `solutions/` séparé, non distribué en amont) illustre ce que ce standard doit généraliser.
**Valeur** : des exercices plus immersifs et cohérents entre eux (le stagiaire connaît déjà le contexte, l'énergie va dans l'exercice pas dans la compréhension du décor), un debrief facilité par la continuité narrative, et une distribution disciplinée des corrigés qui ne vide jamais un exercice de sa valeur avant l'heure.
**Action** :
  - `formation-material-builder` conçoit désormais, en Phase 1 (roadmap), un **cas fil rouge unique** (produit/contexte fictif, cohérent avec le domaine du client) qui sert de socle à tous les ateliers de la formation — intégré directement dans le flux existant, sans étape séparée.
  - Chaque atelier vit dans un dossier `atelier-N/` (énoncé + corpus de données dédié si l'atelier en a besoin) au lieu du fichier plat `exercices.md` actuel ; les solutions restent dans un dossier `solutions/` séparé, avec la même règle de non-distribution en amont que `fil-rouge-stockpilot/solutions/README.md`.
  - Ce standard devient le **mode par défaut** de production des exercices (remplace l'actuel `exercices.md` unique), sauf demande contraire explicite du consultant.
  - Les énoncés d'atelier, rédigés d'abord en markdown (`enonce-atelier-N.md`, réutilisant le format actuel), sont ensuite convertis en `enonce-atelier-N.html` avec le template de charte par défaut (bandeau d'en-tête bleu marine, métadonnées en tuiles, consigne numérotée, encadrés indices/bonus) — reprenant tel quel le template déjà éprouvé dans `fil-rouge-stockpilot/atelier-1/enonce-atelier-1.html`.
  - **Extension du 28/07/2026** : chaque élément du corpus d'atelier vit dans son propre fichier (pas un fichier fourre-tout par atelier), et le **format de ce fichier est celui que le stagiaire trouverait réellement dans son métier** (un e-mail en `.md` structuré comme un e-mail, un export tabulaire en `.xlsx` si le vrai outil du client exporte du tableur plutôt qu'en CSV générique, une capture d'écran en `.png`, etc.) plutôt qu'un format uniformisé pour la facilité de traitement. Méthode de production : markdown source d'abord (contenu revu facilement), puis conversion vers le binaire réel si la cible n'est pas du texte brut — même logique que la conversion HTML des énoncés.
**Effort** : L — refonte de la structure de sortie des exercices (Phase 1 + Phase 2 de `formation-material-builder`), nouveau template HTML/charte, mise à jour de `exercise_design.md` et `module_structure.md` ; extension du 28/07/2026 : ajout d'une sous-phase de conversion des éléments de corpus (3.1ter), sans nouvelle dépendance.
**Dépend de** : rien (améliore un livrable existant sans dépendance externe).

### 20. Ajouter la référence complète du design system au dépôt
**Constat** (audit comité qualité) : `slide-content-claude-design/SKILL.md` renvoie à la référence complète du design system, mais ces fichiers résident hors dépôt (dossier local). Un contributeur qui clone le dépôt — déclaré source de vérité unique — ne trouve pas la référence citée. L'impact est atténué par le fait que les tokens essentiels sont inlinés dans la spec.
**Valeur** : rend le dépôt réellement autoportant pour la partie design ; évite une divergence silencieuse entre les tokens inlinés dans la spec et la référence complète.
**Action** : ajouter au dépôt les deux fichiers de référence (sans les assets lourds type logo/template pptx), puis faire pointer `slide-content-claude-design/SKILL.md` vers ce chemin.
**Effort** : S.
**Dépend de** : #2 (le dépôt doit être effectivement poussé et accessible).

### 23. Documenter l'installation des skills sur les 3 surfaces (Claude Code, application Claude, Cowork) ✅ Fait le 28/07/2026
**Constat** (demande utilisateur du 28/07/2026) : le README ne documentait que l'installation sur Claude Code (copie de dossier dans `~/.claude/skills/`). Or les skills Anthropic ne se synchronisent PAS entre surfaces — c'est un fait produit documenté (`platform.claude.com/docs/en/agents-and-tools/agent-skills/overview` § « Cross-surface availability » : *"Custom Skills do not sync across surfaces"*) — donc un consultant qui utilise aussi l'application Claude ou Cowork ne trouvait aucune indication sur comment y installer les mêmes skills. Recherche complémentaire : sur claude.ai/Cowork, l'installation individuelle se fait par upload d'un fichier ZIP (Réglages → Personnaliser → Skills), avec une structure de zip précise (dossier de la skill à la racine, nommé comme le `name:` du frontmatter). **Correction post-audit comité qualité (28/07/2026)** : l'affirmation initiale « aucun partage d'équipe même en Team/Entreprise » était fausse — une source distincte (`support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization`, plus récente) confirme qu'un **Owner** Team/Enterprise peut provisionner une skill à toute l'organisation en une fois via *Réglages d'organisation → Skills → Organization skills*. Les deux pages Anthropic ne sont pas synchronisées entre elles sur ce point ; le README documente les deux avec la nuance nécessaire. Le comportement de Cowork lui-même (charge-t-il les skills du compte claude.ai ?) reste une supposition non confirmée par une source officielle — documenté comme tel, pas comme un fait acquis.
**Valeur** : évite qu'un consultant qui bascule vers l'app Claude ou Cowork découvre par lui-même (ou pense à tort que ça ne marche pas) que les skills n'y sont pas automatiquement disponibles ; documente la procédure exacte au lieu de laisser deviner.
**Action** : README restructuré en 3 sous-sections d'installation (Claude Code / application Claude / Cowork), avec la procédure de zip pour les deux dernières et le rappel explicite de non-synchronisation en tête de section.
**Effort** : S — documentation uniquement, aucun changement de comportement des skills elles-mêmes.
**Dépend de** : rien.

---

## P3 — Exploratoire / à cadrer davantage

### 11. Étudier un export/import direct des quiz vers Kahoot
**Constat** : `formation-material-builder` génère déjà les quiz en markdown structuré (type de question, durée, réponses, bonne réponse), mais le paramétrage dans Kahoot reste 100% manuel — aucun fichier importable disponible à ce jour.
**Valeur** : élimine une étape manuelle récurrente en fin de pipeline, sur un format déjà structuré.
**Action** : vérifier si Kahoot expose un format d'import (CSV/XLSX en marque blanche ou API) et, si oui, ajouter une étape de conversion en sortie de `formation-material-builder`.
**Effort** : M/L — dépend entièrement des capacités d'import exposées par Kahoot (à investiguer avant de chiffrer plus finement).
**Dépend de** : disponibilité d'un format d'import côté Kahoot (hors de notre contrôle).

### 12. Cadrer la limite de taille d'audience pour la recherche participants ✅ Fait le 24/07/2026 (spec) — voir US-9
**Constat** : la recherche automatique de profils (web + LinkedIn) devient très coûteuse en temps et en tokens au-delà d'un certain nombre de participants (testé jusqu'à 12 ; jugé non viable pour une audience de 60). Pour les grands groupes, l'équipe raisonne plutôt en "profil type" qu'en recherche nominative.
**Valeur** : évite un pipeline qui timeout ou consomme un budget de tokens disproportionné sur les formations à large audience (masterclass).
**Action** : ajouter dans `cadrage-formation` un seuil (ex. > 20 participants) au-delà duquel l'agent bascule automatiquement d'une recherche nominative vers une analyse par profil type / niveau d'hétérogénéité, sans attendre que l'utilisateur le lui demande.
**Effort** : M — logique conditionnelle à ajouter dans la skill, avec un seuil à valider avec les utilisateurs.
**Dépend de** : rien.
**Statut** : reformulé en story dès que le seuil de 20 a été fixé sans opposition — voir US-9 dans la section User stories pour le détail de l'implémentation.

### 13. Décider d'un mode par défaut (Loop vs Annotations) pour `comite-qualite` selon contexte collaboratif
**Constat** : le pipeline a jusqu'ici été surtout utilisé en solo, donc le mode "Annotations" (pensé pour le travail collaboratif via Google Docs) reste peu testé. Le choix du mode dépend de ce qui est réellement à auditer (cf. #6) et du fait qu'un tiers collabore ou non.
**Valeur** : clarifie un choix aujourd'hui laissé à l'intuition de l'utilisateur, alors qu'il a un vrai impact sur le flux de travail en équipe.
**Action** : capitaliser un retour d'usage réel en mode collaboratif (prochaine formation faite à plusieurs) avant de figer une recommandation par défaut dans `comite-qualite/SKILL.md`.
**Effort** : S pour la doc, mais nécessite d'attendre un cas d'usage réel avant de trancher — à ne pas développer à l'aveugle.
**Dépend de** : #6.
**Point de vigilance** : le critère d'arrêt de la boucle de correction dépend fortement du modèle utilisé — certains modèles convergent naturellement après quelques itérations, d'autres peuvent continuer à trouver de nouveaux points à corriger indéfiniment, avec un comportement qui évolue au fil des mises à jour de modèle. À surveiller lors du choix de modèle par défaut pour `comite-qualite` en mode loop — un modèle qui ne converge pas peut consommer un budget de tokens disproportionné sans intervention humaine pour l'arrêter (les règles anti-théâtre du `SKILL.md` limitent déjà les itérations — pas plus de 3 consécutives sans changement structurel — ce qui atténue le risque sans constituer un plafond absolu ; à vérifier empiriquement selon le modèle utilisé).

---

## P4 — Organisationnel / commercial (hors évolution directe des skills, mais issu des mêmes retours d'usage)

Ces items ne modifient aucune skill : ce sont des décisions d'organisation ou de positionnement commercial. Ils sont suivis ici parce qu'ils conditionnent le périmètre d'usage du pipeline, mais leur mise en œuvre relève d'un arbitrage managérial plutôt que produit — voir `GOVERNANCE.md`.

### 17. Aligner le dépôt de skills avec le processus d'avant-vente
**Constat** : retour d'usage — question de savoir si le pipeline peut s'intégrer au processus d'avant-vente, pas seulement à la production de formations déjà vendues. Proposition de centraliser l'ensemble des skills au sein d'un répertoire unique et d'établir une logique de responsabilité claire pour leur gestion, avec un arbitrage nécessaire sur qui porte la capitalisation projet vs la capitalisation skills. Nuance utile relevée en discussion : la capitalisation "projet" et la capitalisation "skills" sont complémentaires mais distinctes — le travail par projet permet d'extraire des skills réutilisables, qui peuvent ensuite être redéclinées dans d'autres process (dont l'avant-vente).
**Valeur** : élargit la valeur du pipeline au-delà de la seule production de formation déjà engagée, potentiellement vers la réponse à appel d'offres.
**Action** : clarifier, avec les porteurs du processus d'avant-vente, si et comment le dépôt de skills actuel (ou une extension) peut servir l'avant-vente, sans dilemme de responsabilité entre les deux usages.
**Effort** : L — dépend d'un arbitrage organisationnel hors du périmètre de ce dépôt.

### 18. Évaluer une offre commerciale externe (méthodologie proposée à des instituts de formation tiers)
**Constat** : retour d'usage — suggestion de proposer cette méthodologie modernisée de production de formation comme service à des instituts de formation externes.
**Valeur** : piste de revenu potentiellement significative, mais à un stade purement exploratoire — aucune validation de faisabilité ou de demande client à ce stade.
**Action** : ne pas engager de développement produit sur cette base ; à réévaluer si un sponsor commercial se manifeste explicitement pour cadrer cette offre.
**Effort** : non estimable en l'état — dépend entièrement d'une décision commerciale préalable, hors périmètre de ce backlog.
**Dépend de** : une décision de portage commercial, à l'extérieur de l'équipe des 3 contributeurs actuels.

---

## Hors backlog skills (actions individuelles déjà actées, suivi managérial plutôt que produit)

- Mettre à jour les skills en tenant compte des retours de démo (recoupait les items #3, #4, #6, #10 ci-dessus — tous désormais traités individuellement avec leur propre statut, voir US-3, US-4, US-6, US-8 : cette note est close, ne pas la traiter comme une action encore en attente).
- Créer des slides d'options suite à une démo (livrable de communication interne, pas une évolution de skill).

## Non retenu / hors périmètre pour l'instant

- **Génération de schémas d'architecture type Excalidraw** : mentionné comme besoin ("un schéma d'architecture, un truc qui ressemble à de l'Excalidraw") mais explicitement écarté pour l'instant côté outillage interne — à ne pas transformer en item tant qu'aucune piste d'outil n'est identifiée en interne.

---

## User stories

Rédigées pour les items suffisamment cadrés. Couverture actuelle : US-1→#1, US-2→#2, US-3→#3, US-4→#4, US-5→#5, US-6→#6, US-7→#8, US-8→#10, US-9→#12, US-10→#19, US-11→#21, US-12→#22. Items sans story, avec leur raison :
- **#7, #9, #11, #13** — dépendants d'un spike ou d'un retour d'usage préalable (Horizon 4) ; les storifier avant ce préalable serait prématuré.
- **#14** — story à rédiger lorsque US-1/US-2 seront closes (son livrable, un support d'onboarding, dépend d'un pipeline effectivement installable).
- **#15** — traité directement dans `GOVERNANCE.md` (clarification organisationnelle, pas un développement).
- **#16** — spécifié et clôturé directement au niveau item (voir son Statut) ; exception au circuit item→story assumée pour un changement de spec très localisé.
- **#17, #18** — P4, hors périmètre produit (arbitrage managérial).
- **#20** — dépend de #2 (dépôt effectivement poussé et accessible) ; à storifier une fois ce préalable levé — action documentaire S, triviale à cadrer.
- **#23** — spécifié et clôturé directement au niveau item (voir son Statut, même exception que #16) ; action purement documentaire (README), sans changement de comportement des skills à formaliser en critères d'acceptation séparés.
- **#24** — même exception que #16/#20/#23 ; fichiers de gouvernance du dépôt (LICENSE, CHANGELOG, wiki), sans changement de comportement des skills.

### Definition of Ready (DoR) — commune à toutes les stories

Une story n'entre en développement que si :
- Le besoin est rattaché à un item du backlog priorisé (constat + valeur déjà documentés ci-dessus).
- Les critères d'acceptation sont rédigés, vérifiables, et ne contiennent aucune ambiguïté sur le "fini".
- Les dépendances amont sont soit levées, soit explicitement actées comme non bloquantes pour démarrer (ex. US-3 ne démarre pas avant que US-2 soit "Done").
- Le fichier `SKILL.md` concerné est identifié (une story ne modifie jamais "toutes les skills" sans les lister nommément).
- Il n'y a pas de question ouverte structurante non tranchée (ex. seuil exact, format de convention) — une valeur par défaut proposée vaut acceptation tant qu'elle est écrite noir sur blanc dans la story.

### Definition of Done (DoD) — commune à toutes les stories

Une story est "Done" quand :
- Le(s) `SKILL.md` concerné(s) sont modifiés et committés, avec un message de commit qui référence la story (ex. `US-3`).
- Chaque critère d'acceptation a été rejoué manuellement au moins une fois (ce backlog ne dispose pas de suite de tests automatisés — la vérification est une exécution réelle de la skill sur un cas concret).
- Le comportement a été vérifié par une personne autre que celle qui a écrit la modification (revue croisée légère, cohérente avec une équipe de 3 personnes).
- La documentation impactée (`README.md` du pipeline et/ou section concernée du `SKILL.md`) est mise à jour en cohérence avec le nouveau comportement.
- Aucune régression constatée sur le comportement existant des 3 autres skills du pipeline (test de fumée rapide : lancer le pipeline complet une fois sur un cas déjà connu).
- Le `BACKLOG.md` est mis à jour : la story passe de "à faire" à "faite", avec la date de complétion.

Les critères d'acceptation propres à chaque story ci-dessous s'ajoutent à cette DoD commune ; ils n'ont pas besoin d'être répétés.

### US-1 — Enregistrement fiable des skills entre sessions ✅ Faite le 24/07/2026
*Rattaché à #1*

**En tant que** consultant qui découvre le pipeline de skills,
**je veux** que les skills installées restent détectées d'une session Claude Code à l'autre,
**afin de** ne pas avoir à recréer un nouveau chat à chaque fois pour qu'elles soient reconnues.

**Critères d'acceptation :**
- [x] Le `README.md` documente explicitement le mode "auto" d'enregistrement des skills et son emplacement (`~/.claude/skills/`).
- [ ] Un test manuel de non-régression confirme qu'après un simple restart de session (sans recréer de chat), les 4 skills (`cadrage-formation`, `formation-material-builder`, `slide-content-claude-design`, `comite-qualite`) sont bien détectées. *(à rejouer par un contributeur en session réelle — non vérifiable en dehors d'une session Claude Code active ; voir CONTRIBUTING.md pour la procédure de vérification)*
- [x] En cas d'échec de détection persistant, la documentation indique la procédure de contournement (ex. recréer un chat) comme solution de repli explicite, pas comme méthode par défaut.

**Statut** : spec écrite dans `README.md` (§ "Enregistrement fiable entre sessions"). Le critère d'exécution réelle reste à rejouer par un contributeur en session Claude Code — à cocher une fois testé.

---

### US-2 — Dépôt comme source de vérité accessible à tous 🟡 Partiellement faite le 24/07/2026
*Rattaché à #2*

**En tant que** membre de l'équipe qui n'a pas reçu le livrable par un canal parallèle,
**je veux** trouver les ressources de formation à jour sur le dépôt partagé,
**afin de** pouvoir démarrer sans dépendre d'un envoi manuel individuel.

**Critères d'acceptation :**
- [ ] Le livrable de formation est poussé sur le dépôt partagé. *(action assignée à un contributeur, hors de portée d'une modification de spec — non réalisable depuis ce dépôt)*
- [ ] Un utilisateur autre que celui qui a poussé le fichier confirme pouvoir cloner/accéder au dépôt et y retrouver les fichiers attendus. *(dépend du critère précédent)*
- [x] Le `README.md` référence le dépôt comme source unique, à la place des envois par un canal parallèle.

**Statut** : le volet documentaire est fait (`README.md`, § "Source de vérité", avec un encart signalant explicitement l'état d'attente). Les deux premiers critères restent ouverts et dépendent d'une action humaine hors du périmètre de ce dépôt — ne pas clôturer la story tant qu'ils ne sont pas cochés.

---

### US-3 — Réutilisation d'une formation antérieure proche dans `cadrage-formation` ✅ Faite le 24/07/2026 (spec)
*Rattaché à #3*

**En tant que** consultant qui cadre une nouvelle formation,
**je veux** que l'agent me demande s'il existe une formation antérieure proche et me propose les meilleurs candidats trouvés dans un répertoire donné,
**afin de** gagner du temps sur un besoin récurrent sans repartir from scratch ni risquer de réutiliser un gabarit inadapté (ex. mauvais profils de participants).

**Critères d'acceptation :**
- [x] En tout début d'exécution, `cadrage-formation` pose explicitement la question : "Existe-t-il une formation antérieure proche de ce besoin ?" (nouvelle Étape 1, avant la lecture détaillée du contexte).
- [x] Si l'utilisateur répond oui et fournit (ou a déjà fourni) l'accès à un répertoire de formations passées, l'agent propose 1 à 3 candidats avec une justification courte (thématique, profils de participants, niveau).
- [x] L'agent ne réutilise jamais un gabarit sans validation explicite de l'utilisateur au préalable.
- [x] Si l'utilisateur répond non, l'agent poursuit le cadrage from scratch sans blocage.

**Statut** : spec écrite dans `cadrage-formation/SKILL.md`. Dépend en pratique de US-2 (Horizon 1) pour qu'un répertoire de formations passées soit effectivement accessible à tous — reste à vérifier sur un cas réel une fois ce répertoire disponible.

---

### US-10 — Séparation du contenu Claude Design et des prompts Gemini ✅ Faite le 24/07/2026 (spec)
*Rattaché à #19*

**En tant que** consultant qui produit des slides de formation,
**je veux** que les slides destinées à Claude Design soient séparées des prompts d'illustration Gemini (deux fichiers distincts : `M<n>-slides-content.md` et `M<n>-prompts.md`),
**afin de** (1) fournir un contenu structuré à Claude Design sans distraction des prompts Gemini, (2) générer des illustrations via Gemini avec un prompt clarifié et validé, (3) auditer l'UX/UI des slides **avant** la génération visuelle.

**Critères d'acceptation :**
- [x] `slide-content-claude-design/SKILL.md` documente la production de deux fichiers par module, colocalisés dans `/livrables/`.
- [x] `M<n>-slides-content.md` contient le contenu pour Claude Design avec, pour chaque slide d'illustration, un bloc de placeholder **gris** (rectangle `#D6D6D6`/`#F7F7F7`) aux **dimensions exactes** et à la **position** de l'image attendue sur cette slide (jamais générique — gabarits types documentés dans la spec), lié au prompt correspondant dans `M<n>-prompts.md`.
- [x] `M<n>-prompts.md` contient les prompts d'illustration structurés par slide, respectant la palette par défaut exacte (bleu marine #2C5F8A, corail #D97757, vert sauge #4A8B6F) et les garde-fous (aucun texte dans l'image, zéro faute, pas de doublon texte/image).
- [x] La spec décrit le template de prompt Gemini (template canonique + règles d'adaptation).
- [x] Les deux fichiers sont générés selon la convention de rangement des formations (`formations/<client>-<thème>/<AAAA-MM>/livrables/`).
- [x] La spec prescrit un audit UX/UI de `M<n>-slides-content.md` **avant** toute génération visuelle dans Claude Design (étape 6 de la Méthode, formulation normative).

**Statut** : spec écrite dans `slide-content-claude-design/SKILL.md`, revue par le comité qualité (16 corrections appliquées, dont placeholder par slide et audit UX/UI normatif). Reste à vérifier sur un cas réel (création effective des deux fichiers et audit UX/UI en amont de Claude Design).

---

### US-11 — Direction artistique cohérente par module dans `M<n>-prompts.md` ✅ Faite le 24/07/2026 (spec)
*Rattaché à #21*

**En tant que** consultant qui prépare les illustrations d'une formation,
**je veux** qu'un bloc « Direction artistique » unique par module cadre le style et la métaphore filée de toutes les illustrations Gemini de ce module,
**afin d'** obtenir des slides visuellement cohérentes, professionnelles, et alignées sur l'arc narratif de la formation plutôt que des illustrations isolées.

**Critères d'acceptation :**
- [x] `slide-content-claude-design/SKILL.md` documente un bloc « Direction artistique » généré une fois par module, placé en tête de `M<n>-prompts.md`.
- [x] Le bloc fixe explicitement : le style illustratif, la déclinaison de la métaphore filée pour ce module, et les contraintes visuelles récurrentes (palette, absence de texte, niveau de détail).
- [x] Chaque prompt de slide référence ce bloc (au lieu de répéter des instructions de style ad hoc).
- [x] La spec autorise une légère variation du bloc d'un module à l'autre, tout en restant ancré dans la même métaphore filée globale de la formation.

**Statut** : spec écrite dans `slide-content-claude-design/SKILL.md`. Reste à vérifier sur un cas réel (cohérence visuelle perceptible entre plusieurs illustrations d'un même module généré en conditions réelles).

---

### US-12 — Cas fil rouge et ateliers structurés façon StockPilot ✅ Faite le 24/07/2026 (spec)
*Rattaché à #22*

**En tant que** consultant qui produit les exercices d'une formation,
**je veux** que `formation-material-builder` conçoive un cas fil rouge unique pour toute la formation et structure chaque atelier en dossier dédié (énoncé HTML + corpus + solutions séparées), comme le fait `fil-rouge-stockpilot/`,
**afin d'** offrir aux stagiaires une expérience immersive et cohérente d'atelier en atelier, avec une distribution disciplinée des corrigés qui ne vide jamais un exercice de sa valeur avant l'heure.

**Critères d'acceptation :**
- [x] `formation-material-builder/SKILL.md` documente la conception d'un cas fil rouge unique en Phase 1 (roadmap), intégré directement dans le flux existant (pas d'étape séparée).
- [x] Ce standard (cas fil rouge + dossiers `atelier-N/` + `solutions/` séparé) est le mode de production **par défaut** des exercices, remplaçant l'actuel `exercices.md` unique, sauf demande contraire explicite du consultant.
- [x] Chaque atelier est structuré en dossier `atelier-N/` contenant son énoncé et, si besoin, un corpus de données dédié — reprenant l'arborescence de `fil-rouge-stockpilot/`.
- [x] Le dossier `solutions/` est séparé des dossiers d'ateliers, avec la même règle de non-distribution en amont documentée (à distribuer uniquement après le debrief de l'atelier correspondant).
- [x] Les énoncés sont rédigés d'abord en markdown (`enonce-atelier-N.md`) puis convertis en `enonce-atelier-N.html` avec le template de charte par défaut (bandeau bleu marine, métadonnées en tuiles, consigne numérotée, encadrés indices/bonus).
- [x] `references/exercise_design.md` et `references/module_structure.md` sont mis à jour en cohérence avec ce nouveau standard.
- [x] *(Extension 28/07/2026)* Chaque élément du corpus vit dans un fichier distinct, au **format réel du métier client** (pas un format uniformisé par défaut) — méthode de production markdown source → conversion binaire, documentée dans `fil_rouge_design.md` et répercutée dans `formation-material-builder/SKILL.md` (nouvelle sous-phase 3.1ter) et `exercise_design.md`.

**Statut** : spec écrite dans `formation-material-builder/SKILL.md` + références mises à jour, y compris l'extension du 28/07/2026 sur le format réaliste du corpus. Reste à vérifier sur un cas réel (production complète d'une formation avec cas fil rouge, conversion HTML effective, et corpus en formats réalistes).

---

### US-4 — Proposition systématique de la prochaine étape après chaque skill ✅ Faite le 24/07/2026 (spec)
*Rattaché à #4*

**En tant qu'** utilisateur du pipeline, quel que soit le modèle ou l'environnement utilisé,
**je veux** qu'à la fin de chaque skill l'agent me propose explicitement les options d'étape suivante,
**afin de** savoir quoi faire ensuite sans avoir à connaître le pipeline par cœur, en particulier lors d'un premier onboarding.

**Critères d'acceptation :**
- [x] Chacune des 4 skills (`cadrage-formation`, `formation-material-builder`, `slide-content-claude-design`, `comite-qualite`) se termine par une proposition explicite d'étape suivante, formulée en options claires (ex. "veux-tu que je lance X ou Y ?"). *(`formation-material-builder` en propose une à chaque point de validation intermédiaire, pas seulement en fin de pipeline, car son workflow est déjà découpé en phases validées une à une.)*
- [ ] Ce comportement ne dépend pas du modèle utilisé (vérifié au moins sous deux modèles distincts) ni de l'environnement. *(à vérifier en usage réel — non testable depuis ce dépôt)*
- [x] La proposition mentionne l'output déjà produit et ce que l'étape suivante en ferait, pour que l'utilisateur décide en connaissance de cause.
- [x] *(Extension 28/07/2026)* Chaque skill demande les paramètres structurants non précisés **avant** de commencer à produire, pas seulement à la fin : `slide-content-claude-design` interroge densité et design system en étape 0 de sa méthode si non fournis.
- [x] *(Extension 28/07/2026)* Les skills à déroulé long posent un point de vérification **en cours de route**, pas seulement en fin de phase : `formation-material-builder` s'arrête après 3.1/3.1bis/3.1ter (avant de compiler les .docx, plus coûteux à refaire) ; `comite-qualite` marque une pause avant application (Phase C) si la synthèse contient au moins un constat 🔴 bloquant.
- [x] *(Extension 28/07/2026)* Le README explique cette logique de guidage (avant/pendant/après chaque étape) à l'utilisateur, au lieu de la laisser implicite dans le seul comportement des skills.

**Statut** : spec écrite dans les 4 `SKILL.md` et synchronisée dans `README.md`, y compris l'extension du 28/07/2026 sur le cadrage en début et en cours de skill longue. Reste à vérifier par exécution réelle sous différents modèles/environnements, conformément à la DoD.

---

### US-5 — Convention de rangement des livrables par formation ✅ Faite le 24/07/2026
*Rattaché à #5*

**En tant que** consultant qui gère plusieurs sessions d'une même formation dans le temps,
**je veux** que chaque formation soit rangée selon une convention de nommage/arborescence unique dès le cadrage,
**afin de** retrouver facilement la bonne version et éviter la confusion entre sessions (ex. une même formation redonnée à quelques mois d'écart).

**Critères d'acceptation :**
- [x] Une convention de nommage/arborescence est documentée (`formations/<client>-<thème>/<AAAA-MM>/`, `cadrage-formation/SKILL.md` § Étape 0).
- [x] `cadrage-formation` crée le dossier de la formation selon cette convention dès le début du cadrage (nouvelle Étape 0, avant la lecture du contexte), plutôt qu'un rangement manuel en fin de pipeline.
- [x] La convention distingue explicitement plusieurs sessions d'une même formation dans le temps (`<AAAA-MM>` = date de la session, pas du cadrage).

**Statut** : Done au sens de la spec — reste à vérifier par un premier usage réel (création effective du dossier lors d'un prochain cadrage), sans quoi le critère reste theoretical.

---

### US-6 — Périmètre d'audit explicite en début de `comite-qualite` ✅ Faite le 24/07/2026
*Rattaché à #6*

**En tant qu'** utilisateur qui lance un audit qualité,
**je veux** que l'agent me demande explicitement quel périmètre auditer (markdown, présentation générée, ou les deux),
**afin de** ne pas découvrir après coup que l'audit portait sur un contenu différent de celui que j'avais en tête.

**Critères d'acceptation :**
- [x] `comite-qualite` pose la question du périmètre d'audit avant de composer l'équipe de relecteurs (nouvelle section 0.0, avant 0.1).
- [x] Les options proposées couvrent au minimum : contenu markdown seul, présentation générée seule, les deux.
- [x] Le rapport d'audit final rappelle explicitement le périmètre qui a été couvert (Phase D et section "Sortie attendue").

**Statut** : Done au sens de la spec — reste à vérifier par un premier audit réel, conformément à la DoD.

---

### US-7 — Guide de paramétrage de l'extension Claude Code ✅ Faite le 24/07/2026 (documentation)
*Rattaché à #8*

**En tant que** nouvel utilisateur suivant la démo comme onboarding,
**je veux** disposer d'un mini-guide de paramétrage de l'extension Claude Code (connexion compte pro, gestion des quotas),
**afin de** ne pas perdre de temps en configuration avant de pouvoir utiliser le pipeline de skills.

**Critères d'acceptation :**
- [x] Un mini-guide (dans le `README.md`, § "Pré-requis : paramétrer l'extension Claude Code") couvre : emplacement de l'extension, connexion compte pro vs perso, comportement attendu en cas de blocage sur les quotas.
- [ ] Le guide est validé par au moins une personne ne l'ayant jamais paramétrée auparavant. *(à faire : reste un test humain, non exécutable depuis ce dépôt)*

**Statut** : spec écrite. Reste à faire valider par une personne n'ayant jamais paramétré l'extension, conformément à la DoD (vérification par exécution réelle).

---

### US-8 — Ouverture fluide des fichiers Excel générés ✅ Faite le 24/07/2026 (documentation)
*Rattaché à #10*

**En tant qu'** utilisateur de `cadrage-formation`,
**je veux** savoir comment ouvrir facilement le `.xlsx` généré directement depuis mon environnement de travail,
**afin de** ne pas perdre de temps à chercher comment visualiser le livrable à chaque exécution.

**Critères d'acceptation :**
- [x] Le `README.md` (§ "Ouvrir les fichiers `.xlsx` générés") recommande une extension pour visualiser un `.xlsx` sans sortir de l'environnement.
- [ ] L'instruction est testée par un utilisateur n'ayant pas cette extension déjà installée. *(à faire : reste un test humain, non exécutable depuis ce dépôt)*

**Statut** : spec écrite. Reste à faire tester par un utilisateur sans cette extension, conformément à la DoD.

---

### US-9 — Seuil de bascule vers une analyse par profil type au-delà d'une grande audience ✅ Faite le 24/07/2026 (spec)
*Rattaché à #12*

**En tant que** consultant qui cadre une formation à large audience (masterclass, 50+ participants),
**je veux** que l'agent bascule automatiquement d'une recherche nominative vers une analyse par profil type/niveau d'hétérogénéité au-delà d'un certain seuil,
**afin d'** éviter un temps d'exécution et une consommation de tokens disproportionnés sur une recherche individuelle non pertinente à cette échelle.

**Critères d'acceptation :**
- [x] Un seuil (20 participants) est défini et documenté dans `cadrage-formation` (Étape 3).
- [x] Au-delà du seuil, l'agent bascule automatiquement vers une analyse par profil type sans que l'utilisateur ait à le demander explicitement.
- [x] L'agent signale explicitement à l'utilisateur qu'il a basculé de mode et pourquoi (nombre de participants détecté vs seuil) — message-type inclus dans la spec.
- [x] En dessous du seuil, le comportement actuel (recherche nominative) est inchangé.

**Statut** : spec écrite dans `cadrage-formation/SKILL.md`, seuil fixé à 20 (valeur par défaut proposée dans la DoR, jamais contestée en usage réel). Reste à vérifier sur un cas réel dépassant ce seuil.
