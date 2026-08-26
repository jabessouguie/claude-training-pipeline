# Roadmap — Pipelines de skills (formation et réponse à appel d'offres)

Vision produit : **faire des pipelines de skills de ce dépôt l'outillage par défaut de tout consultant sur ses deux productions les plus coûteuses en temps** —

- **Produire une formation client** (`cadrage-formation` → `formation-material-builder` → `slide-content-claude-design` → `comite-qualite`), du premier appel de cadrage jusqu'au dossier livrable complet, en réduisant le temps manuel à l'appropriation finale (anecdotes, ajustements visuels, quiz).
- **Répondre à un appel d'offres** (`reponse-appel-offres` → `comite-qualite`), de la recherche méthodologique jusqu'au plan de présentation, en sécurisant la conformité au cahier des charges et la différenciation réelle de l'offre.

Les horizons 1 à 5 ci-dessous portent la trajectoire du pipeline formation (le plus ancien et le plus abouti) ; l'horizon 6 celle du pipeline réponse à AO. Les acquis transverses (gouvernance, workflow Git, `PIPELINE_CONTRACTS.md`, `comite-qualite`, skills transverses comme l'extraction de design system) servent les deux sans être dupliqués.

Cette roadmap découle directement du backlog priorisé dans [BACKLOG.md](BACKLOG.md). Elle raisonne par horizon plutôt que par date fixe : une équipe de 3 contributeurs à temps partiel sur ce sujet ne peut pas s'engager sur des sprints classiques, mais peut s'engager sur un **ordre** et sur ce qui définit le passage d'un horizon à l'autre.

**Preuve de valeur de référence** : une formation multi-jours a été produite en une fraction du temps qu'elle aurait demandé en méthode manuelle, sur un référentiel historique de conseil où une slide de qualité représentait environ une heure de production. C'est le cas d'usage qui justifie l'investissement continu dans ce pipeline et sert de repère pour évaluer l'impact des horizons ci-dessous.

---

## Horizon 1 — Fiabiliser le socle (adoption sans friction) ✅ Spec livrée (vérification en usage réel en attente)

**Objectif** : n'importe qui dans l'équipe peut installer le pipeline, le lancer, et obtenir un premier livrable sans bloquer sur un problème d'outillage ou d'accès.

**Contenu** (backlog associé) :
- US-1 — Enregistrement fiable des skills entre sessions (#1)
- US-7 — Guide de paramétrage de l'extension Claude Code (#8)
- US-8 — Ouverture fluide des fichiers Excel générés (#10)

*US-2 — Dépôt comme source de vérité accessible à tous (#2) — retirée le 26/08/2026 (voir `BACKLOG.md` § « Non retenu ») : l'incident qui l'avait motivée ne s'est pas reproduit. Ne conditionne plus cet horizon.*

**Condition de sortie** : une personne de l'équipe qui n'a jamais utilisé le pipeline peut, seule, à partir du seul dépôt, installer les 4 skills et produire un premier plan de formation sans intervention orale d'un tiers.

**Pourquoi en premier** : tout le reste de la roadmap suppose que le socle technique ne bloque pas — améliorer le contenu des skills (Horizon 2) est inutile si personne d'autre que le porteur du pipeline ne peut les faire tourner de façon fiable.

**Complète le socle** : #14 — Packager le workflow complet comme asset transmissible (schéma + mode d'emploi de présentation, à produire à partir du `README.md` existant). Bien que ce ne soit pas un correctif technique, cet item conditionne la même condition de sortie : un nouvel arrivant doit pouvoir comprendre le pipeline en 5 minutes sans reproduire une session de démo complète.

**Complète aussi le socle** : #24 — Standardiser les fichiers de gouvernance du dépôt (LICENSE, CHANGELOG, wiki), pour la même raison : un point d'entrée navigable (wiki) qui ne suppose pas de cloner le dépôt.

**Complète aussi le socle** : #20 — `design-system-extractor` (US-19) ✅ Fait le 26/08/2026 : plutôt qu'une référence statique supposée exister hors dépôt, une skill qui extrait le design system client à partir de n'importe quel document réellement fourni, consommée par `slide-content-claude-design`.

---

## Horizon 2 — Guider le parcours utilisateur ✅ Spec livrée (vérification en usage réel en attente)

**Objectif** : le pipeline guide activement l'utilisateur d'une étape à l'autre, au lieu de dépendre de sa connaissance implicite du workflow.

**Contenu** :
- US-4 — Proposition systématique de la prochaine étape après chaque skill (#4)
- US-6 — Périmètre d'audit explicite en début de `comite-qualite` (#6)
- US-5 — Convention de rangement des livrables par formation (#5)
- US-10 — Séparation du contenu Claude Design et des prompts Gemini (#19) — nouvelle fonctionnalité : `slide-content-claude-design` produit deux fichiers (`M<n>-slides-content.md` pour Claude Design avec, par slide, un placeholder gris dimensionné et positionné ; `M<n>-prompts.md` pour Gemini structuré selon le design system par défaut), avec un audit UX/UI prescrit avant la génération visuelle
- US-11 — Direction artistique cohérente par module (#21) — un bloc « Direction artistique » unique par module en tête de `M<n>-prompts.md`, cadrant style et métaphore filée pour toutes les illustrations du module
- US-12 — Cas fil rouge et ateliers structurés façon StockPilot (#22) — `formation-material-builder` conçoit un cas fictif unique filé sur toute la formation, avec des ateliers en dossiers dédiés (énoncé HTML + corpus + solutions séparées), nouveau standard par défaut des exercices

**Condition de sortie** : un utilisateur qui suit le pipeline de bout en bout (cadrage → matériel → slides → audit) est à chaque étape informé de ce qu'il peut faire ensuite, sans avoir à consulter cette roadmap ou à demander à un collègue.

**Dépendance** : suppose Horizon 1 terminé. US-5 (convention de rangement) est indépendante de US-2 (retirée le 26/08/2026) ; la réutilisation de formations passées (Horizon 3, US-3) présuppose toujours un stockage fiable des formations, besoin qui persiste sans être porté par un item de backlog dédié depuis le retrait de US-2.

**Renforce cet horizon** : #16 — Intégrer le "personnage" d'un interlocuteur client au comité qualité, pour vérifier la fidélité du contenu produit à ce qui a été exprimé en entretien de cadrage. Rattaché à Horizon 2 plutôt qu'à Horizon 4 car il ne dépend d'aucun préalable externe, seulement de la qualité des notes déjà produites par `cadrage-formation`.

**Renforce aussi cet horizon** : #23 — Documenter l'installation des skills sur les 3 surfaces (Claude Code, application Claude, Cowork) : les skills ne se synchronisent pas entre surfaces (fait produit Anthropic), donc un utilisateur qui bascule d'un outil à l'autre doit savoir répéter l'installation — sans cette clarté, "guider le parcours utilisateur" s'arrête à la porte de Claude Code.

---

## Horizon 3 — Capitaliser sur l'historique ✅ Spec livrée (vérification en usage réel en attente)

**Objectif** : chaque nouvelle formation bénéficie des formations précédentes au lieu de repartir from scratch, sans reproduire une erreur de réutilisation aveugle constatée en usage réel (mauvais profil de référence réutilisé pour un public différent).

**Contenu** :
- US-3 — Réutilisation d'une formation antérieure proche dans `cadrage-formation` (#3)
- US-9 — Seuil de bascule vers une analyse par profil type au-delà d'une grande audience (#12)

**Condition de sortie** : sur au moins 2 formations réelles consécutives pour un même client (à quelques mois d'écart), la seconde bénéficie effectivement du cadrage de la première via la skill, avec validation explicite de l'utilisateur à chaque réutilisation. **Non atteinte à ce stade** : la spec de US-3 et US-9 est écrite dans `cadrage-formation/SKILL.md`, mais US-3 reste bloquée en pratique tant qu'un répertoire de formations passées n'est pas effectivement accessible à tous — c'est le prérequis concret pour tester ce comportement en conditions réelles. Ce prérequis n'est plus porté par un item de backlog dédié depuis le retrait de US-2/#2 le 26/08/2026 (voir `BACKLOG.md` § « Non retenu » — l'incident qui l'avait motivé ne s'est pas reproduit) ; à réouvrir comme item si le besoin redevient bloquant en pratique.

**Dépendance** : nécessite un stockage stable des formations passées comme prérequis dur pour sa condition de sortie — non couvert par un item de backlog actif depuis le retrait de US-2/#2 (26/08/2026, voir « Non retenu »). US-3 (#3) reste donc formellement sans dépendance backlog bloquante, mais son critère de test en conditions réelles ne peut être vérifié tant que ce stockage n'existe pas.

---

## Horizon 4 — Explorer et arbitrer (sans engagement de résultat)

**Objectif** : ce sont des pistes dont la valeur est plausible mais qui nécessitent un arbitrage (outillage, décision d'équipe, ou capacité d'un outil tiers) avant de devenir des stories engageables. Ne pas les développer avant d'avoir la réponse au préalable identifié.

**Contenu** :
- #7 — Harmoniser les environnements Claude Code utilisés en interne *(préalable : retour d'un contributeur sur son usage terrain)*
- #11 — Export/import direct des quiz vers Kahoot *(préalable : vérifier si Kahoot expose un format d'import)*
- #13 — Mode par défaut Loop vs Annotations pour `comite-qualite` *(préalable : un cas d'usage réel en collaboratif)*

*(#9 — génération d'illustrations moins manuelle — est sorti de cet horizon le 28/07/2026 : le préalable a été levé directement par une demande explicite de l'utilisateur, sans passer par un spike comparatif formel. Voir Horizon 5.)*

**Condition de passage en roadmap engagée** : dès qu'un préalable est levé, l'item correspondant est reformulé en user story (DoR/DoD) et entre dans l'horizon 2, 3 ou 5 selon sa dépendance réelle — pas automatiquement en fin de liste.

---

## Horizon 5 — Automatisation bout-en-bout (spec-driven + orchestration) 🟡 Spec livrée (vérification en usage réel en attente)

**Objectif** : un utilisateur disposant d'un accès Claude Code ou Cowork (et, s'il choisit le mode d'illustration automatique, d'une clé API Gemini distincte — voir note ci-dessous) peut produire une formation complète — du cadrage jusqu'à la composition finale des slides — sans relancer chaque skill à la main ni deviner l'étape suivante, tout en gardant intact l'usage skill-par-skill existant.

**Note sur les accès nécessaires** (précision post-audit comité qualité, 28/07/2026) : "muni d'une clé API" est ambigu et mérite d'être détaillé pour éviter toute confusion coûteuse. Claude Code/Cowork s'utilisent généralement via un abonnement Claude (Pro/Max/Team/Enterprise), pas une clé API développeur au sens strict. Le mode d'illustration **automatique**, lui, nécessite une **clé API Gemini distincte** (`GEMINI_API_KEY`, compte Google AI Studio séparé, quota et facturation propres à Google) — ce n'est pas la même clé, ni le même fournisseur, que l'accès à Claude Code/Cowork. Un utilisateur qui veut uniquement le mode manuel (composition et illustrations à la main, comme aujourd'hui) n'a besoin d'aucune clé API Gemini.

**Contenu** (backlog associé) :
- US-13 — Combler le chaînon `cadrage-formation` → `formation-material-builder` (#25)
- US-14 — Contrats d'interface explicites entre les skills (`PIPELINE_CONTRACTS.md`, #26)
- US-15 — Skill orchestratrice `formation-pipeline` (#27)
- US-16 — Génération automatique des illustrations via l'API Gemini (#28, réponse à #9, sorti de l'Horizon 4 le 28/07/2026)

**Condition de sortie** : une formation complète produite via `formation-pipeline`, mode illustrations "auto", jusqu'à la composition manuelle dans Claude Design puis convergence via `comite-qualite`, validée sur un cas réel (smoke test du pipeline complet prescrit par `CONTRIBUTING.md`).

**Pourquoi après les horizons 1-3** : cet horizon suppose un socle fiable (Horizon 1 : le dépôt lui-même comme source de vérité installable) et un parcours déjà guidé (Horizon 2 : proposition systématique de l'étape suivante, que l'orchestrateur relaie plutôt que redéfinit) — automatiser un enchaînement dont chaque maillon serait encore instable ou mal documenté aurait juste industrialisé la friction existante.

**Ce que cet horizon n'a pas tenté de résoudre** : la composition finale dans Claude Design reste manuelle — recherche menée le 28/07/2026 confirmant que Claude Design n'expose aucune API programmatique (le pont `/design-sync` avec Claude Code est un aller-retour interactif piloté par un humain, pas un point d'intégration scriptable). Seule la génération d'image (API Gemini) a été automatisée. Si Claude Design expose un jour une intégration programmatique, réévaluer #27/#28 à cette aune plutôt que de forcer une automatisation qui n'existe pas encore côté outil.

**Dépendance** : suppose Horizon 1 et Horizon 2 substantiellement en place (le pipeline doit être installable et déjà guidé pour qu'orchestrer ses étapes ait du sens).

---

## Horizon 6 — Pipeline avant-vente (réponse à appel d'offres) 🟡 Refondu (US-18 livrée, périmètre élargi jusqu'au plan de présentation)

**Objectif** : un consultant peut analyser un dossier d'appel d'offres et produire un plan de présentation détaillé optimisé pour Claude Design, en une seule skill bout-en-bout — recherche méthodologique, recherche client, analyse du besoin (avec checklist d'exigences CCTP tracée), analyse de fit cabinet/client, sourcing et sélection de références, plan de présentation, comité qualité. Même logique spec-driven que le pipeline formation, adaptée aux spécificités de l'avant-vente (conformité CCTP exhaustive, deadline dure, différenciation réelle, cohérence multi-contributeurs).

**Contenu** (backlog associé) :
- US-18 — `reponse-appel-offres` produit un mémoire de réponse à AO complet jusqu'au plan de présentation Claude Design (#29)

**Révision du 18/08/2026** : après la première itération (`cadrage-appel-offres`, US-17, limitée à l'analyse du dossier), l'utilisateur a redéfini le périmètre en un workflow explicite à 8 étapes bien plus large. Décision actée : élargissement direct en une skill unique `reponse-appel-offres`, plutôt que la trajectoire initialement prévue en 4 skills séquentielles (`memoire-technique-builder`, `memoire-content-claude-design`, `appel-offres-pipeline` — abandonnées, jamais écrites). Ce changement de stratégie reste cohérent avec le principe itératif de départ : la première itération a servi à valider le mécanisme le plus critique (la checklist d'exigences, conservée à l'identique dans la nouvelle skill) avant d'investir dans un périmètre plus large.

**Condition de sortie** : un premier AO réel traité de bout en bout via `reponse-appel-offres` (recherche → analyse → plan de présentation → composition Claude Design), sans jamais nommer cet AO dans le dépôt (cohérence avec la règle de gouvernance des données déjà actée côté formation — `formations/` et `appels-offres/` ne sont jamais versionnés pour un cas réel).

**Pourquoi un nouvel horizon plutôt qu'un sous-horizon** : ce pipeline sert un métier distinct (avant-vente, pas formation) — un horizon séquentiel propre reste plus lisible qu'un "Horizon 1 bis" mélangé à la trajectoire du pipeline formation.

**Dépendance** : aucune dépendance dure sur les horizons 1-5 (pipeline distinct), mais réutilise leurs acquis transverses (`CONTRIBUTING.md`, workflow Git, format `PIPELINE_CONTRACTS.md`, rôles conditionnels déjà existants de `comite-qualite`) sans les dupliquer.

---

## Hors trajectoire produit — organisationnel et commercial

Ces items (#15, #18 dans `BACKLOG.md`) ne suivent pas la logique d'horizon ci-dessus parce qu'ils ne dépendent pas de l'avancement technique du pipeline, mais d'arbitrages hors du périmètre des 3 contributeurs actuels :

- **#15 — SDLC et gouvernance de cycle de vie des skills** : traité directement dans `GOVERNANCE.md` plutôt que planifié comme un horizon ; à réévaluer si le nombre de contributeurs augmente significativement.
- **#18 — Offre commerciale externe à des instituts tiers** : purement exploratoire, sans sponsor commercial identifié à ce stade — à ne pas confondre avec une priorité produit.

*(#17 — Alignement avec le processus d'avant-vente — est sorti de cette section le 29/07/2026 : l'arbitrage a été rendu, l'item est clos, et sa suite opérationnelle vit désormais dans l'Horizon 6 ci-dessus.)*

## Ce qui n'est pas dans cette roadmap

- **Génération de schémas type Excalidraw** : explicitement écartée faute de piste d'outil interne identifiée (voir "Non retenu" dans `BACKLOG.md`). À ne réintroduire que si un outil concret émerge.
- **Toute évolution des skills non tracée dans `BACKLOG.md`** : cette roadmap ne planifie que ce qui est déjà objectivé par un constat et une valeur écrits. Une demande orale ("il faudrait aussi...") doit d'abord devenir un item de backlog avant d'apparaître ici.

## Mise à jour de cette roadmap

Cette roadmap est révisée à chaque fois qu'un horizon atteint sa condition de sortie, ou qu'un préalable de l'Horizon 4 est levé — pas selon un calendrier fixe. Voir [GOVERNANCE.md](GOVERNANCE.md) pour qui a la main sur ces décisions.
