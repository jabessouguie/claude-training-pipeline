# Contributing — Pipeline de skills de formation

Ce dépôt contient 4 skills Claude Code (`cadrage-formation`, `formation-material-builder`, `slide-content-claude-design`, `comite-qualite`) formant un pipeline de production de formations. Ce document explique comment y contribuer. Pour comprendre qui décide quoi, voir [GOVERNANCE.md](GOVERNANCE.md) ; pour savoir quoi faire en premier, voir [BACKLOG.md](BACKLOG.md) et [ROADMAP.md](ROADMAP.md).

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

Consultez le `README.md` racine pour la description fonctionnelle à jour des 4 skills et de leur enchaînement avant de modifier quoi que ce soit — il fait foi sur le comportement *actuel* du pipeline et doit rester en synchronisation stricte avec les `SKILL.md`.

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
4. **Lancez un test de fumée du pipeline complet** (les 4 skills à la suite sur un cas déjà connu) pour vérifier qu'aucune spec non modifiée n'a vu son comportement dériver — une modification de `SKILL.md` peut changer le comportement d'une autre skill si elle consomme ses livrables.
5. **Capitalisez les cas de test rejoués.** Si un cas concret a servi à vérifier un comportement de façon répétée, signalez-le dans le `SKILL.md` ou le `README.md` comme cas de référence — cela permet au prochain contributeur de rejouer le même scénario plutôt que d'en inventer un nouveau à chaque fois.
6. **Sécurité** : la CI (`.github/workflows/ci.yml`) exécute une détection de secrets sur chaque push — vérifiez qu'aucun contenu sensible (client, token, accès à un espace de stockage) n'est commité par erreur, notamment dans des fichiers d'exemple ou de cas de test.

## Commit et livraison

- Le message de commit référence l'identifiant de la story (ex. `US-3 — cadrage-formation propose une formation antérieure similaire`) et précise que c'est un changement de spec (`SKILL.md`) suivi de sa vérification comportementale.
- Une fois la story vérifiée selon la DoD, mettez à jour `BACKLOG.md` : marquez la story comme faite avec sa date de complétion.
- Si la modification change le comportement décrit dans le `README.md` racine (section "Les 4 skills et leur enchaînement" ou "Notes de version"), mettez-le à jour dans le même commit — c'est la référence que les utilisateurs consultent en premier, elle ne doit jamais retarder derrière la spec réelle.

## Remonter un nouveau besoin sans contribuer de spec

Vous n'avez pas besoin de savoir écrire une spec pour contribuer : un retour d'usage précis (contexte, ce qui a bloqué ou surpris, ce qui aurait aidé) est la matière première de ce pipeline. Partagez-le au Product Owner (voir `GOVERNANCE.md`) pour qu'il devienne un item de `BACKLOG.md`, qui sera ensuite traduit en story puis en modification de spec suivant le processus ci-dessus. Un comportement démontré à l'oral ou en démo, tant qu'il n'est pas écrit dans un `SKILL.md`, n'est pas garanti de se reproduire — c'est précisément ce que ce processus vise à éliminer.
