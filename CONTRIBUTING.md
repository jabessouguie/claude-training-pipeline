# Contributing — Pipelines de skills (formation et réponse à appel d'offres)

Ce dépôt contient les skills Claude Code de **deux pipelines** : la production de formation (`cadrage-formation`, `formation-material-builder`, `slide-content-claude-design`, `comite-qualite`, plus l'orchestrateur optionnel `formation-pipeline`) et la réponse à appel d'offres (`reponse-appel-offres`). Ce document explique comment y contribuer, et s'applique à l'identique aux deux — ainsi qu'à toute skill transverse qui les sert. Pour comprendre qui décide quoi, voir [GOVERNANCE.md](GOVERNANCE.md) ; pour savoir quoi faire en premier, voir [BACKLOG.md](BACKLOG.md) et [ROADMAP.md](ROADMAP.md).

## Principe directeur : spec-driven

Ce dépôt suit un développement **piloté par la spécification** : le `SKILL.md` d'une skill n'est pas de la documentation écrite après coup, c'est **la source de vérité qui précède et gouverne le comportement**. Une skill Claude Code s'y prête naturellement, car le `SKILL.md` *est* littéralement les instructions exécutées par l'agent — spec et implémentation ne sont jamais deux artefacts séparés qui peuvent diverger silencieusement comme du code contre sa doc.

Conséquence directe sur le workflow :

1. **On écrit ou on modifie la spec avant de vérifier le comportement**, jamais l'inverse. Si vous constatez qu'une skill se comporte différemment de ce que dit son `SKILL.md`, la question à trancher en premier est : est-ce le comportement qui est faux, ou la spec qui est incomplète/obsolète ? Ne corrigez jamais l'un sans statuer sur l'autre.
2. **Les critères d'acceptation d'une story (voir DoR dans `BACKLOG.md`) sont écrits en amont, dans un langage vérifiable par exécution**, avant toute modification du `SKILL.md` — ce sont vos cas de test, faute de suite automatisée.
3. **La spec n'est jamais implicite.** Un comportement attendu qui n'est décrit nulle part dans le `SKILL.md` n'existe pas officiellement, même s'il a été démontré une fois à l'oral — voir "Remonter un nouveau besoin" en fin de document.

## Avant de contribuer

1. **Partir d'un usage réel, pas d'une idée abstraite.** Toute évolution de skill part d'un constat observé en utilisant réellement le pipeline sur une formation (comme lors des sessions de démo). Si vous avez une idée sans avoir buté dessus en usage réel, ouvrez d'abord un item dans `BACKLOG.md` plutôt que de modifier directement une skill.
2. **Vérifier qu'un item de backlog existe déjà.** Ne dupliquez pas un item déjà présent — si un constat proche existe, complétez-le plutôt que d'en créer un nouveau.
3. **S'assurer que la story respecte la Definition of Ready** (voir `BACKLOG.md`) avant d'écrire une seule ligne de spec : critères d'acceptation écrits et vérifiables, skill(s) concernée(s) identifiée(s) nommément, dépendances amont levées ou actées comme non bloquantes.
4. **Ne jamais commencer par éditer le comportement.** Vous n'avez pas le droit de "juste essayer un prompt différent" dans une session Claude Code pour voir si ça marche mieux, puis de reporter la modification dans le `SKILL.md` après coup — la spec se rédige en premier, le comportement en découle. Un prototypage exploratoire en session est acceptable pour valider une hypothèse, mais il ne remplace jamais l'écriture de la spec avant de considérer le changement comme fait.

## Structure d'une skill et statut de chaque fichier

```
<nom-de-la-skill>/
├── SKILL.md          # LA SPEC — instructions, déclencheurs, comportement attendu, format des livrables
├── scripts/           # implémentation mécanique dérivée de la spec (ex. génération .xlsx)
└── references/        # connaissance de fond citée par la spec, jamais une spec parallèle
```

- **`SKILL.md` est prescriptif** : c'est ce que l'agent doit faire. Toute divergence entre `SKILL.md` et le comportement observé est un bug — soit du comportement, soit de la spec — jamais un détail à ignorer.
- **`scripts/` est descriptif de la mécanique, pas du jugement** : un script gère une tâche déterministe (générer un `.xlsx`, un `.pptx`) que le `SKILL.md` délègue explicitement. Si un script encode une règle métier qui n'est écrite nulle part dans `SKILL.md`, c'est une spec cachée — remontez-la dans `SKILL.md`.
- **`references/` documente des connaissances stables** (structure pédagogique, principes de design) que la spec cite ; ce n'est jamais l'endroit où décrire un comportement attendu de l'agent — ce comportement va dans `SKILL.md`.

Consultez le `README.md` racine pour la description fonctionnelle à jour des skills et de leur enchaînement avant de modifier quoi que ce soit — il fait foi sur le comportement *actuel* des pipelines et doit rester en synchronisation stricte avec les `SKILL.md`. La même exigence de synchronisation vaut pour le `wiki/` (même contenu, formulé pour un utilisateur non contributeur) : une modification de comportement qui laisse le wiki en arrière crée exactement la divergence que ce principe interdit.

## Workflow Git : branches et pull requests

Ce dépôt reste simple à dessein (3 contributeurs à temps partiel, voir `GOVERNANCE.md`) — ce workflow n'est pas du process pour le process, il existe pour que la revue croisée déjà exigée par la DoD (`BACKLOG.md`) ait un support concret, et que `main` reste toujours dans un état que n'importe qui peut installer et faire tourner. Ce dépôt est hébergé sur **GitHub** (pas GitLab) : on y ouvre des **pull requests (PR)**, jamais des "merge requests" — c'est le terme GitLab, il ne correspond à aucun bouton de l'interface GitHub réellement utilisée ici.

### Prérequis : la mécanique Git de base

Si les commandes ci-dessous ne te sont pas familières, demande-toi d'abord si tu es la bonne personne pour ce changement (voir README.md § « Mise en place technique » — certaines contributions gagnent à être accompagnées par un collègue technique) ou fais-toi montrer ces quelques commandes une fois par un autre contributeur ; elles ne changent jamais d'un projet à l'autre.

```bash
git checkout main && git pull                     # partir d'un main à jour
git checkout -b feat/us-15-formation-pipeline      # créer la branche (convention ci-dessous)
# ... modifier le(s) fichier(s), git add, git commit ...
git push -u origin feat/us-15-formation-pipeline   # pousser la branche vers GitHub
```

Une fois la branche poussée, GitHub affiche un bandeau "Compare & pull request" sur la page du dépôt — cliquer dessus (ou, depuis l'onglet **Pull requests**, bouton **New pull request**) ouvre l'écran de création de la PR, où on renseigne le titre/la description (voir « Ouvrir une pull request » ci-dessous).

### `main` est toujours livrable

- `main` reflète l'état actuellement recommandé du pipeline : quelqu'un qui clone le dépôt à cet instant doit pouvoir installer les skills et les utiliser sans tomber sur une spec à moitié écrite.
- **On ne pousse jamais directement sur `main`.** Même une correction d'une ligne dans un `SKILL.md` passe par une branche + une pull request (PR) — la revue croisée porte autant sur la spec elle-même (non ambiguë ? vérifiable ?) que sur le comportement obtenu, et sauter cette étape revient à sauter la DoD.
- **Cette règle doit être appliquée techniquement, pas seulement suivie par discipline** : configurer une *branch protection rule* sur `main` (Settings → Branches → Branch protection rules sur GitHub) qui exige au moins une PR avant merge — sans ça, rien n'empêche techniquement un `git push origin main` direct, y compris par erreur. À vérifier/mettre en place si ce n'est pas déjà fait.
- **Une seule exception** : un correctif de pure forme sans changement de comportement (faute de frappe, lien cassé, formatage) peut être poussé directement, **et uniquement par le Product Owner** (voir `GOVERNANCE.md` pour qui occupe ce rôle) s'il n'y a personne d'autre disponible pour relire dans un délai raisonnable — cette dérogation n'est pas ouverte aux autres contributeurs, documentée comme exception, pas comme un mode par défaut.

### Nommer une branche

Une branche = une story ou un item de backlog, jamais un fourre-tout de plusieurs sujets sans rapport. Convention :

```
<type>/<référence-story-ou-item>-<slug-court>
```

- `<type>` : `feat` (nouvelle capacité d'une skill), `fix` (comportement qui ne correspond pas à sa spec), `docs` (README/wiki/gouvernance sans changement de comportement), `chore` (outillage : CI, scripts — inclut les fichiers de config comme `.gitignore`).
- `<référence>` : l'identifiant de `BACKLOG.md` concerné (ex. `us-13`, `item-25`) — permet de retrouver le constat et les critères d'acceptation sans les rechercher.
- `<slug-court>` : 2-4 mots, kebab-case.

Exemples : `feat/us-15-formation-pipeline`, `fix/item-6-perimetre-audit`, `docs/gouvernance-contributing`.

### Ouvrir une pull request

1. **La PR référence l'item/story de `BACKLOG.md`** dans son titre ou sa description (ex. `US-13 — combler le chaînon cadrage → material-builder`) — jamais une PR sans rattachement à un item existant (cf. « Avant de contribuer » ci-dessus : pas d'idée abstraite non passée par le backlog, sauf correctif de pure forme).
2. **La description de la PR remplit trois blancs** : quel `SKILL.md` (ou fichier de gouvernance) change et pourquoi ; comment le changement a été vérifié (quel cas concret rejoué, cf. DoD) ; ce qui reste à vérifier si tout ne peut pas l'être avant merge (ex. un appel API réel non testé faute de clé disponible).
3. **La CI doit être verte** avant toute demande de revue — `lint-python` et `secret-detection` (`.github/workflows/ci.yml`) tournent automatiquement dès l'ouverture de la PR (déclenchement `on: pull_request`) et leur statut s'affiche directement en bas de la page de la PR, dans l'onglet **Checks** ; ne pas demander une relecture sur une CI encore rouge, ça fait perdre du temps au relecteur sur un problème que l'outillage aurait signalé seul.
4. **Une seule approbation suffit** (équipe de 3 — voir `GOVERNANCE.md`), mais elle doit venir d'un contributeur qui n'a pas écrit le changement, conformément à la DoD ("pas de merge solo sur ce pipeline restreint"). **Appliquer ça techniquement** : cocher "Require pull request reviews before merging" (avec 1 review requise) dans la branch protection rule de `main` — sinon rien n'empêche l'auteur de merger sa propre PR sans review.
   - **Si les deux autres contributeurs sont indisponibles** (mission client, congés — cf. `GOVERNANCE.md`, l'équipe travaille ce pipeline en parallèle de son activité principale) au-delà d'un délai raisonnable, ne pas rester bloqué indéfiniment : le Product Owner peut approuver lui-même à titre exceptionnel si le changement est mineur (même logique que l'exception de poussée directe ci-dessus), ou la PR attend le retour d'un des deux — documenter ce choix dans un commentaire de la PR plutôt que de le laisser implicite.
5. **Le relecteur vérifie deux choses**, pas seulement la lisibilité du diff : la spec est-elle non ambiguë et vérifiable (cf. « Écrire ou modifier une spec » ci-dessous) ; et le comportement a-t-il été rejoué sur un cas concret comme l'exige la DoD — une PR "ça a l'air bien" sans cas de test rejoué n'est pas approuvable en l'état.
6. **Merge par "squash and merge"** de préférence, pour garder un historique de `main` lisible par story — sauf si la branche contient plusieurs commits atomiques qu'il est utile de garder séparés (rare sur ce dépôt, à motiver si c'est le cas). Pour que ce ne soit pas qu'une convention orale, restreindre les méthodes de merge autorisées dans Settings → General → Pull Requests (décocher "Allow merge commits", garder "Allow squash merging").
7. **Supprimer la branche après merge** — une branche qui traîne après fusion n'apporte rien et brouille la liste des branches actives pour les 2 autres contributeurs. Activer "Automatically delete head branches" (Settings → General) pour ne pas dépendre d'un geste manuel à chaque PR.

### Cas particulier : changement qui touche plusieurs skills

Si une story touche plusieurs `SKILL.md` à la fois (ex. l'ajout de `PIPELINE_CONTRACTS.md` avec ses renvois dans plusieurs skills), une seule branche/PR reste préférable à une PR par skill — le principe "une story = une ou plusieurs skills nommément identifiées" (voir plus bas) s'applique au contenu de la story, pas au découpage Git. Découper en plusieurs petites PR une story cohérente complique la revue (le relecteur doit reconstituer le puzzle) sans bénéfice réel pour une équipe de 3.

## Écrire ou modifier une spec (`SKILL.md`)

1. **Une story = une ou plusieurs skills nommément identifiées.** N'écrivez jamais une modification qui touche "toutes les skills" sans lister explicitement lesquelles et pourquoi chacune est concernée.
2. **Traduisez chaque critère d'acceptation de la story en un ajout ou une modification précise et localisable dans le `SKILL.md`** — une section, une règle, un exemple de déclencheur. Si un critère d'acceptation ne se traduit dans aucune phrase concrète de la spec, la story n'est pas prête à être implémentée : retournez la clarifier (DoR).
3. **Respectez le format existant** (sections, ton, niveau de détail des déclencheurs) plutôt que d'introduire une structure différente au sein du même fichier — une spec incohérente en interne est aussi coûteuse qu'une spec absente.
4. **Rendez la spec vérifiable, pas seulement lisible.** Préférez une formulation testable ("l'agent pose la question X avant de composer l'équipe") à une formulation d'intention ("l'agent doit bien clarifier le périmètre") qu'aucune exécution ne peut confirmer ou infirmer.
5. **Ne cassez pas la rétrocompatibilité silencieusement.** Si une modification change un comportement déjà documenté dans le `README.md` (ex. format de sortie d'un livrable), mettez à jour le `README.md` dans le même changement — deux sources de vérité qui divergent sont pires qu'une seule source incomplète.
6. **Pas de scope creep.** Une story ne doit couvrir que ce que décrivent ses critères d'acceptation — si vous repérez au passage une autre amélioration possible, ajoutez-la comme nouvel item dans `BACKLOG.md` plutôt que de l'ajouter à la spec en cours de modification.

## Vérifier la conformité comportement ↔ spec

Ce pipeline n'a pas de suite de tests automatisés : chaque critère d'acceptation de la DoR **est** un cas de test, et la vérification se fait par **exécution réelle de la skill contre sa propre spec**.

1. **Rejouez chaque critère d'acceptation comme un cas de test exécutable**, sur un cas concret déjà connu de l'équipe pour pouvoir comparer avant/après. Consignez pour chacun : entrée utilisée, comportement attendu (tel qu'écrit dans le `SKILL.md` modifié), comportement observé.
2. **Traitez tout écart entre le `SKILL.md` et le comportement observé comme bloquant**, jamais comme un détail — c'est la définition même d'une spec qui ne gouverne pas réellement le comportement. Ne clôturez pas la story tant que spec et comportement ne coïncident pas sur les critères d'acceptation testés.
3. **Faites relire votre changement de spec par un des deux autres contributeurs avant de le considérer terminé** — la relecture porte sur la spec elle-même (est-elle non ambiguë ? vérifiable ?) autant que sur le comportement obtenu. Pas de merge solo sur ce pipeline restreint (cf. DoD dans `BACKLOG.md`).
4. **Lancez un test de fumée du pipeline concerné par votre changement**, de bout en bout sur un cas déjà connu, pour vérifier qu'aucune spec non modifiée n'a vu son comportement dériver — une modification de `SKILL.md` peut changer le comportement d'une autre skill si elle consomme ses livrables.
   - **Pipeline formation** : `cadrage-formation`, `formation-material-builder`, `slide-content-claude-design`, `comite-qualite` à la suite (via `formation-pipeline` ou skill par skill).
   - **Pipeline réponse à AO** : `reponse-appel-offres` sur ses 8 étapes, puis l'enchaînement proposé vers `comite-qualite`.
   - **Skill transverse** : chaque pipeline qu'elle alimente réellement, puisqu'une régression s'y propage — les deux pour `design-system-extractor` (consommée par `slide-content-claude-design`, côté formation, et applicable côté AO) ; le seul pipeline AO pour `consultants-references-extractor` (consommée par `reponse-appel-offres`). Vérifier ce que la skill alimente vraiment avant de choisir le périmètre du test, plutôt que de supposer que « transverse » veut dire « les deux ».
   - Si le changement touche `comite-qualite` ou `PIPELINE_CONTRACTS.md`, les deux pipelines sont concernés — ces deux fichiers leur sont communs.
5. **Capitalisez les cas de test rejoués.** Si un cas concret a servi à vérifier un comportement de façon répétée, signalez-le dans le `SKILL.md` ou le `README.md` comme cas de référence — cela permet au prochain contributeur de rejouer le même scénario plutôt que d'en inventer un nouveau à chaque fois.
6. **Sécurité** : la CI (`.github/workflows/ci.yml`) exécute une détection de secrets sur chaque push — vérifiez qu'aucun contenu sensible (client, token, accès à un espace de stockage) n'est commité par erreur, notamment dans des fichiers d'exemple ou de cas de test.

## Commit et livraison

Voir « Workflow Git : branches et pull requests » ci-dessus pour la mécanique (branche, PR, revue, merge). Ici, ce que le contenu du commit et de la PR doivent respecter :

- Le message de commit référence l'identifiant de la story (ex. `US-3 — cadrage-formation propose une formation antérieure similaire`) et précise que c'est un changement de spec (`SKILL.md`) suivi de sa vérification comportementale.
- Une fois la story vérifiée selon la DoD, mettez à jour `BACKLOG.md` : marquez la story comme faite avec sa date de complétion.
- Si la modification change le comportement décrit dans le `README.md` racine (section décrivant les skills et leur enchaînement, ou tout autre comportement documenté) ou dans `PIPELINE_CONTRACTS.md` (format d'un fichier échangé entre deux skills), mettez-le à jour dans le même commit/la même MR — ce sont les références que les utilisateurs et les autres contributeurs consultent en premier, elles ne doivent jamais retarder derrière la spec réelle.

## Remonter un nouveau besoin sans contribuer de spec

Vous n'avez pas besoin de savoir écrire une spec pour contribuer : un retour d'usage précis (contexte, ce qui a bloqué ou surpris, ce qui aurait aidé) est la matière première de ce pipeline. Partagez-le au Product Owner (voir `GOVERNANCE.md`) pour qu'il devienne un item de `BACKLOG.md`, qui sera ensuite traduit en story puis en modification de spec suivant le processus ci-dessus. Un comportement démontré à l'oral ou en démo, tant qu'il n'est pas écrit dans un `SKILL.md`, n'est pas garanti de se reproduire — c'est précisément ce que ce processus vise à éliminer.
