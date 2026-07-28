# Roadmap — Pipeline de skills de formation

Vision produit : **faire du pipeline de 4 skills (`cadrage-formation` → `formation-material-builder` → `slide-content-claude-design` → `comite-qualite`) l'outil par défaut de tout consultant pour produire une formation client**, du premier appel de cadrage jusqu'au dossier livrable complet, en réduisant le temps manuel à l'appropriation finale (anecdotes, ajustements visuels, quiz).

Cette roadmap découle directement du backlog priorisé dans [BACKLOG.md](BACKLOG.md). Elle raisonne par horizon plutôt que par date fixe : une équipe de 3 contributeurs à temps partiel sur ce sujet ne peut pas s'engager sur des sprints classiques, mais peut s'engager sur un **ordre** et sur ce qui définit le passage d'un horizon à l'autre.

**Preuve de valeur de référence** : une formation multi-jours a été produite en une fraction du temps qu'elle aurait demandé en méthode manuelle, sur un référentiel historique de conseil où une slide de qualité représentait environ une heure de production. C'est le cas d'usage qui justifie l'investissement continu dans ce pipeline et sert de repère pour évaluer l'impact des horizons ci-dessous.

---

## Horizon 1 — Fiabiliser le socle (adoption sans friction) 🟡 Majoritairement livré (US-2 en attente d'action humaine)

**Objectif** : n'importe qui dans l'équipe peut installer le pipeline, le lancer, et obtenir un premier livrable sans bloquer sur un problème d'outillage ou d'accès.

**Contenu** (backlog associé) :
- US-1 — Enregistrement fiable des skills entre sessions (#1)
- US-2 — Dépôt comme source de vérité accessible à tous (#2)
- US-7 — Guide de paramétrage de l'extension Claude Code (#8)
- US-8 — Ouverture fluide des fichiers Excel générés (#10)

**Condition de sortie** : une personne de l'équipe qui n'a jamais utilisé le pipeline peut, seule, à partir du seul dépôt, installer les 4 skills et produire un premier plan de formation sans intervention orale d'un tiers.

**Pourquoi en premier** : tout le reste de la roadmap suppose que le socle technique ne bloque pas — améliorer le contenu des skills (Horizon 2) est inutile si personne d'autre que le porteur du pipeline ne peut les faire tourner de façon fiable.

**Complète le socle** : #14 — Packager le workflow complet comme asset transmissible (schéma + mode d'emploi de présentation, à produire à partir du `README.md` existant). Bien que ce ne soit pas un correctif technique, cet item conditionne la même condition de sortie : un nouvel arrivant doit pouvoir comprendre le pipeline en 5 minutes sans reproduire une session de démo complète.

**Complète aussi le socle** : #24 — Standardiser les fichiers de gouvernance du dépôt (LICENSE, CHANGELOG, wiki), pour la même raison : un point d'entrée navigable (wiki) qui ne suppose pas de cloner le dépôt.

**Complète aussi le socle** : #20 — Ajouter la référence du design system au dépôt (dépend de #2/US-2) : le dépôt n'est réellement autoportant pour la partie design qu'une fois ces deux fichiers de référence poussés à côté des skills.

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

**Dépendance** : suppose Horizon 1 terminé (US-2 en particulier, car US-5 et la réutilisation de formations passées présupposent un stockage fiable).

**Renforce cet horizon** : #16 — Intégrer le "personnage" d'un interlocuteur client au comité qualité, pour vérifier la fidélité du contenu produit à ce qui a été exprimé en entretien de cadrage. Rattaché à Horizon 2 plutôt qu'à Horizon 4 car il ne dépend d'aucun préalable externe, seulement de la qualité des notes déjà produites par `cadrage-formation`.

**Renforce aussi cet horizon** : #23 — Documenter l'installation des skills sur les 3 surfaces (Claude Code, application Claude, Cowork) : les skills ne se synchronisent pas entre surfaces (fait produit Anthropic), donc un utilisateur qui bascule d'un outil à l'autre doit savoir répéter l'installation — sans cette clarté, "guider le parcours utilisateur" s'arrête à la porte de Claude Code.

---

## Horizon 3 — Capitaliser sur l'historique ✅ Spec livrée (vérification en usage réel en attente)

**Objectif** : chaque nouvelle formation bénéficie des formations précédentes au lieu de repartir from scratch, sans reproduire une erreur de réutilisation aveugle constatée en usage réel (mauvais profil de référence réutilisé pour un public différent).

**Contenu** :
- US-3 — Réutilisation d'une formation antérieure proche dans `cadrage-formation` (#3)
- US-9 — Seuil de bascule vers une analyse par profil type au-delà d'une grande audience (#12)

**Condition de sortie** : sur au moins 2 formations réelles consécutives pour un même client (à quelques mois d'écart), la seconde bénéficie effectivement du cadrage de la première via la skill, avec validation explicite de l'utilisateur à chaque réutilisation. **Non atteinte à ce stade** : la spec de US-3 et US-9 est écrite dans `cadrage-formation/SKILL.md`, mais US-3 reste bloquée en pratique tant que US-2 (dépôt source de vérité) n'est pas pleinement close — un répertoire de formations passées accessible à tous est le prérequis concret pour tester ce comportement en conditions réelles.

**Dépendance** : nécessite Horizon 1 (US-2, un stockage stable des formations passées) comme prérequis dur — documenté aussi comme dépendance directe dans le backlog (#3 dépend de #2).

---

## Horizon 4 — Explorer et arbitrer (sans engagement de résultat)

**Objectif** : ce sont des pistes dont la valeur est plausible mais qui nécessitent un arbitrage (outillage, décision d'équipe, ou capacité d'un outil tiers) avant de devenir des stories engageables. Ne pas les développer avant d'avoir la réponse au préalable identifié.

**Contenu** :
- #7 — Harmoniser les environnements Claude Code utilisés en interne *(préalable : retour d'un contributeur sur son usage terrain)*
- #9 — Génération d'illustrations moins manuelle *(préalable : spike comparatif Claude natif / Gemini / autre outil de génération)*
- #11 — Export/import direct des quiz vers Kahoot *(préalable : vérifier si Kahoot expose un format d'import)*
- #13 — Mode par défaut Loop vs Annotations pour `comite-qualite` *(préalable : un cas d'usage réel en collaboratif)*

**Condition de passage en roadmap engagée** : dès qu'un préalable est levé, l'item correspondant est reformulé en user story (DoR/DoD) et entre dans l'horizon 2 ou 3 selon sa dépendance réelle — pas automatiquement en fin de liste.

---

## Hors trajectoire produit — organisationnel et commercial

Ces items (#15, #17, #18 dans `BACKLOG.md`) ne suivent pas la logique d'horizon ci-dessus parce qu'ils ne dépendent pas de l'avancement technique du pipeline, mais d'arbitrages hors du périmètre des 3 contributeurs actuels :

- **#15 — SDLC et gouvernance de cycle de vie des skills** : traité directement dans `GOVERNANCE.md` plutôt que planifié comme un horizon ; à réévaluer si le nombre de contributeurs augmente significativement.
- **#17 — Alignement avec le processus d'avant-vente** : dépend d'un arbitrage interne sur le périmètre du dépôt de skills — pas engageable tant que cet arbitrage n'a pas eu lieu.
- **#18 — Offre commerciale externe à des instituts tiers** : purement exploratoire, sans sponsor commercial identifié à ce stade — à ne pas confondre avec une priorité produit.

## Ce qui n'est pas dans cette roadmap

- **Génération de schémas type Excalidraw** : explicitement écartée faute de piste d'outil interne identifiée (voir "Non retenu" dans `BACKLOG.md`). À ne réintroduire que si un outil concret émerge.
- **Toute évolution des skills non tracée dans `BACKLOG.md`** : cette roadmap ne planifie que ce qui est déjà objectivé par un constat et une valeur écrits. Une demande orale ("il faudrait aussi...") doit d'abord devenir un item de backlog avant d'apparaître ici.

## Mise à jour de cette roadmap

Cette roadmap est révisée à chaque fois qu'un horizon atteint sa condition de sortie, ou qu'un préalable de l'Horizon 4 est levé — pas selon un calendrier fixe. Voir [GOVERNANCE.md](GOVERNANCE.md) pour qui a la main sur ces décisions.
