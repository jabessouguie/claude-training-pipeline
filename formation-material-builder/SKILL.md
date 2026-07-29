---
name: formation-material-builder
description: Produit l'ensemble du matériel pédagogique d'une formation — slides .pptx, livret stagiaire .docx, guide formateur .docx, énoncés et solutions d'exercices, quiz d'évaluation, prérequis & setup — à partir de la grille de cadrage remplie par le client et (optionnellement) des réponses/notes additionnelles. Déclenche cette skill dès qu'un utilisateur mentionne la création du matériel de formation, des supports de formation, des slides de formation, des exercices d'une formation, un livret stagiaire, un guide formateur, le matériel pédagogique, le contenu d'une formation, un quiz d'évaluation, ou tout livrable post-cadrage. Elle chaîne naturellement après `cadrage-formation`, mais peut fonctionner en standalone si on lui fournit directement un contexte et un plan de formation. Workflow itératif module par module pour rester gérable sur des formations multi-jours et donner au consultant des points de validation réguliers.
---

# Formation Material Builder

Construit l'ensemble du matériel pédagogique d'une formation à partir du cadrage client validé : la grille de cadrage remplie (`.xlsx`), à partir de laquelle cette skill dérive elle-même, en Phase 0, un brief et un plan de formation.

## Inputs attendus

| Fichier | Statut | Origine |
|---|---|---|
| `cadrage_<client>.xlsx` rempli (colonne "Réponse client" renseignée) | Obligatoire | `cadrage-formation` — voir Contrat 1 de [`PIPELINE_CONTRACTS.md`](../PIPELINE_CONTRACTS.md) |
| Notes additionnelles de cadrage (texte libre, e-mails, compte rendu complémentaire) | Optionnel mais recommandé | collées/uploadées par le consultant |

Il n'y a pas de skill intermédiaire entre `cadrage-formation` et celle-ci : c'est cette skill, en Phase 0, qui lit le xlsx rempli et en dérive elle-même `00-brief.md` et `00-plan.md` (voir Phase 0 ci-dessous). Ces deux fichiers ne sont donc jamais un input attendu de l'extérieur — ce sont des livrables internes que la Phase 0 produit et fait valider.

Si un dossier `formations/<client>-<theme>/<AAAA-MM>/` existe (créé par `cadrage-formation`, voir sa convention de rangement), l'utiliser comme workspace en priorité — y chercher le xlsx rempli avant de considérer qu'aucun input n'est disponible.

**Mode standalone** (pas de workspace `cadrage-formation` existant) : demander au consultant de fournir directement (a) le contexte client et (b) un plan de formation déjà arrêté par ailleurs (ex. négocié en avant-vente hors pipeline). Dans ce cas, `00-brief.md` et `00-plan.md` sont écrits directement à partir de ce que fournit le consultant, sans ingestion de xlsx (voir Phase 0). Créer alors le workspace avec les bons noms de fichiers, en réutilisant le slug `<client>-<theme>` de `cadrage-formation` (même convention de nommage) si le client et le thème sont identifiables.

## Livrables produits

**Cas fil rouge** (dans `livrables/`, conçu en Phase 1 avant les ateliers) :
- `00-fil-rouge.md` — cas fictif unique filé sur toute la formation (produit/contexte, rôle stagiaire, fil narratif entre ateliers)

**Par module** (dans `modules/M<n>-<slug>/`) :
- `slides.md` — outline structurée des slides en markdown
- `notes-formateur.md` — animation, timing, anticipations

**Par atelier** (dans `livrables/atelier-N/`, standard par défaut — voir `references/fil_rouge_design.md`) :
- `enonce-atelier-N.md` — énoncé rédigé en markdown (contexte, objectif, consigne, critères de réussite, indices, bonus)
- `enonce-atelier-N.html` — conversion charte par défaut (bandeau bleu marine, métadonnées en tuiles, consigne numérotée)
- `enonce-atelier-N.pdf` — export imprimable depuis le HTML
- corpus de données dédié si l'atelier en a besoin — un fichier par élément, au format réel du métier (ex. `email-reclamation-client.md`, `export-tickets-atelier-2.xlsx` — voir `references/fil_rouge_design.md`)

**Solutions** (dans `livrables/solutions/`, séparées des ateliers, non distribuées en amont) :
- `solution-atelier-N.md` — un fichier par atelier : approche pédagogique, solution complète, variantes, pièges fréquents
- `README.md` — rappelle la règle de non-distribution avant le debrief de chaque atelier

**Transverses** (dans `livrables/`) :
- `M<n>-slides.pptx` — slides PowerPoint par module
- `livret-stagiaire.docx` — compilation pour les stagiaires (SANS solutions)
- `guide-formateur.docx` — compilation complète pour le formateur (AVEC solutions et notes)
- `quiz-kahoot.md` — quiz final au format Kahoot (une fiche par question : type, réponses, temps, points, limite de réponse) + grille de correction récapitulative
- `prerequis-setup.md` — ce que les stagiaires doivent préparer en amont

**Mode alternatif** : si le consultant demande explicitement de ne pas utiliser un cas fil rouge, produire à la place un `exercices.md` et un `solutions.md` classiques par module (format antérieur, voir `references/exercise_design.md` § « Sans cas fil rouge »).

## Structure du workspace

Structure interne, quel que soit le workspace racine retenu en Phase 0 (`formations/<client>-<theme>/<AAAA-MM>/` ou `/home/claude/projets/<slug-client>/` en mode standalone) :

```
<workspace-racine>/
├── cadrage_<client>.xlsx                             # input (cadrage-formation), absent en mode standalone
├── 00-brief.md                                        # dérivé en Phase 0 (Contrat 2, voir PIPELINE_CONTRACTS.md)
├── 00-plan.md                                         # dérivé en Phase 0 (Contrat 2, voir PIPELINE_CONTRACTS.md)
├── 06-material-roadmap.md                            # roadmap de production validée
├── modules/
│   ├── M1-<slug>/
│   │   ├── slides.md
│   │   └── notes-formateur.md
│   ├── M2-<slug>/
│   └── ...
└── livrables/
    ├── 00-fil-rouge.md
    ├── M1-slides.pptx
    ├── M2-slides.pptx
    ├── ...
    ├── atelier-1/
    │   ├── enonce-atelier-1.md
    │   ├── enonce-atelier-1.html
    │   ├── enonce-atelier-1.pdf
    │   └── <corpus dédié si nécessaire, un fichier par élément au format réel du métier>
    ├── atelier-2/
    │   └── ...
    ├── solutions/
    │   ├── solution-atelier-1.md
    │   ├── solution-atelier-2.md
    │   ├── ...
    │   └── README.md
    ├── livret-stagiaire.docx
    ├── guide-formateur.docx
    ├── quiz-kahoot.md
    └── prerequis-setup.md
```

---

## Workflow par phases

### Phase 0 — Discovery : ingestion du cadrage, brief et plan

1. **Localiser le workspace** :
   ```bash
   ls formations/ 2>/dev/null
   ls /home/claude/projets/ 2>/dev/null
   ```
   Chercher en priorité un dossier `formations/<client>-<theme>/<AAAA-MM>/` (convention de `cadrage-formation`) contenant un `cadrage_<client>.xlsx`. Si plusieurs workspaces, demander lequel utiliser. Si aucun xlsx trouvé, basculer en mode standalone (cf. plus bas).

#### 0.1 — Ingestion du xlsx de cadrage (Contrat 1, voir `PIPELINE_CONTRACTS.md`)

1. Lire `cadrage_<client>.xlsx` : onglet **Questions de cadrage** (colonnes Thème/Question/Priorité/Réponse client/Statut), onglet **Participants** si présent, onglet **Contexte** si présent.
2. **Vérifier la complétude** : toutes les questions de priorité `INDISPENSABLE` doivent avoir Statut = "Répondu". Si ce n'est pas le cas, **ne jamais avancer silencieusement** : lister les questions INDISPENSABLE non répondues et demander explicitement au consultant de les compléter, ou de confirmer qu'on avance malgré tout (dans ce cas, le signaler dans `00-brief.md` comme un point de vigilance ouvert). **Une réponse non actionnable** (ex. "peu importe", "comme vous voulez" à une question sur les objectifs métier) a le même effet délétère qu'une absence de réponse pour calibrer la formation — la traiter de la même façon : signaler ce point de vigilance au consultant plutôt que de l'accepter silencieusement comme une réponse exploitable.
3. Lire les notes additionnelles de cadrage si le consultant en fournit (texte libre, e-mails, compte rendu complémentaire).
4. Produire `00-brief.md` (format ci-dessous, Contrat 2) — une synthèse structurée dérivée du xlsx et des notes additionnelles. Ce fichier est un livrable **interne** à cette skill : il n'est jamais attendu comme input externe.

#### 0.2 — Construction du plan de formation (Contrat 2)

1. À partir de `00-brief.md`, proposer une **structure de modules** : titre, durée, niveau (100/200/300), objectifs pédagogiques, pour chacun — **en calibrant chaque niveau selon `references/pedagogical_principles.md` § 3 « La pyramide de Bloom »** (100 → Se souvenir/Comprendre/Appliquer, 200 → Analyser/Évaluer, 300 → Créer ; ne pas assigner un objectif de niveau supérieur à un module marqué d'un niveau inférieur) et en explicitant les **prérequis entre modules** (quel module suppose acquis le contenu d'un module précédent) — lire cette référence avant de proposer le plan, pas seulement en Phase 2.
2. **Présenter au consultant un résumé court** (~15 lignes max) avant de continuer :
   - Client + sujet
   - Niveau de la formation (100/200/300)
   - Durée totale + format (présentiel/distanciel/hybride)
   - **Liste numérotée des modules proposés** avec durée de chacun
   - Points de vigilance issus du cadrage (dont, le cas échéant, les questions INDISPENSABLE restées sans réponse)
3. **Attendre la validation explicite du consultant avant de continuer** — c'est le même principe que la validation du fil rouge/roadmap en Phase 1 : un plan mal calibré coûte cher à corriger une fois le contenu produit.
4. Une fois validé, écrire `00-plan.md` (format ci-dessous, Contrat 2).

**Mode standalone** (pas de workspace `cadrage-formation` existant) : demander au consultant de fournir directement (a) le contexte client et (b) un plan de formation déjà arrêté par ailleurs (ex. négocié en avant-vente hors pipeline). Créer alors `/home/claude/projets/<slug>/` où `<slug>` suit la même convention que `cadrage-formation` (`<client>-<theme>` en kebab-case, ex. `alpha-po-augmente`) à partir du nom client et du sujet fournis — jamais un slug ad hoc, pour rester alignable avec un éventuel dossier `formations/<client>-<theme>/` existant ou futur. Écrire directement `00-brief.md` et `00-plan.md` à partir de ce que fournit le consultant (sans étape 0.1 d'ingestion xlsx), puis les faire valider comme au point 0.2.3 avant de poursuivre.

#### Format de `00-brief.md`

```markdown
# Brief — <Client> · <Thème formation>

## Contexte
<synthèse du contexte client + onglet Contexte du xlsx, ou notes fournies en mode standalone>

## Objectifs (réponses client)
- <Question INDISPENSABLE> → <Réponse client>
- ...

## Audience
- **Mode d'analyse** : nominatif (recherche individuelle) | par profil type (au-delà du seuil de 20 participants, cf. `cadrage-formation` Étape 3) — préciser le nombre de participants
- **Hétérogénéité technique/fonctionnel** : <ratio ou description — repris de l'analyse de `cadrage-formation`, jamais reformulé en une phrase générique type "public hétérogène">
- **Séniorité** : <répartition décideurs/managers/praticiens, si disponible>
- **Profils "à confirmer"** : <repris tels quels du xlsx, ne pas les faire disparaître dans la synthèse>

## Contraintes
<outillage, budget, format, logistique — depuis les réponses>

## Points de vigilance
<repris du xlsx + tout ajout du consultant, y compris les questions INDISPENSABLE restées sans réponse ou non actionnables si l'utilisateur a choisi d'avancer malgré tout>
```

Le § Audience reprend explicitement les axes déjà produits par `cadrage-formation` (Étape 3 : seuil de 20 participants, hétérogénéité technique/fonctionnel, séniorité) — ne jamais les aplatir en une phrase de synthèse libre, c'est la seule passerelle entre l'analyse d'audience du cadrage et la calibration pédagogique du plan (0.2) et du contenu (Phase 2).

#### Format de `00-plan.md`

```markdown
# Plan de formation — <Client> · <Thème>

**Niveau global** : 100 | 200 | 300
**Durée totale** : <ex. 2 jours>
**Format** : présentiel | distanciel | hybride

## Logique de progression
<2-4 phrases : comment le niveau/les objectifs montent en compétence d'un module à l'autre
(ex. "M1-M2 posent les bases niveau 100 (Comprendre/Appliquer), M3-M4 montent en Analyser/Évaluer
niveau 200") — jamais une simple liste de modules sans lien explicite entre eux>

## Modules
### M1 — <titre>
- Durée : <ex. 2h>
- Niveau : 100 | 200 | 300
- Prérequis : <module(s) dont celui-ci suppose le contenu acquis, ou "aucun" si c'est un point d'entrée>
- Objectifs pédagogiques : <liste>

### M2 — ...
```

Le § « Logique de progression » et le champ « Prérequis » par module ne sont pas optionnels : un plan qui traite chaque module comme une fiche isolée, sans lien de progression explicite, produit l'anti-pattern documenté dans `references/pedagogical_principles.md` § 8 « Cohérence du fil narratif » (le stagiaire qui "a vu beaucoup de choses mais ne voit pas comment ça s'articule").

Voir aussi `references/module_structure.md` § « Format du brief et du plan dérivés » et le Contrat 2 de [`PIPELINE_CONTRACTS.md`](../PIPELINE_CONTRACTS.md) pour le détail et les règles de rédaction de ces deux fichiers.

### Phase 1 — Roadmap de production et cas fil rouge

Lire `references/module_structure.md` ET `references/fil_rouge_design.md` AVANT de proposer la roadmap.

**1. Concevoir le cas fil rouge** (standard par défaut, voir `references/fil_rouge_design.md`) : un produit/contexte fictif unique, cohérent avec le domaine du client, qui sert de socle à tous les ateliers de la formation. Fixer : le nom du produit, le rôle stagiaire, le fil narratif entre ateliers (ce qui progresse d'un atelier à l'autre). Rédiger ce cas dans `livrables/00-fil-rouge.md`.

Si le consultant demande explicitement de ne pas utiliser de cas fil rouge, passer directement à l'étape 2 en note mentale et produire des exercices classiques indépendants par module (voir `exercise_design.md` § « Sans cas fil rouge »).

**2. Pour chaque module**, produire dans `06-material-roadmap.md` une fiche courte avec :
- **Slug du module** (ex: `M1-fondamentaux-llm`)
- **Estimation nombre de slides** : ~10-15 slides par heure de théorie, ~5-8 slides pour un atelier
- **Liste des ateliers** prévus avec format (notebook, papier, live coding, par binôme…) et **comment chacun s'ancre dans le cas fil rouge** (quel atelier précédent il prolonge, quelle progression du cas il fait avancer)
- **Concepts à approfondir vs survoler** — calibré sur le niveau (100/200/300) du plan
- **Points d'attention pédagogique** — passages où on anticipe des difficultés, des questions, des décrochages

**Présenter au consultant, dans cet ordre** : le cas fil rouge d'abord (nom, rôle, fil narratif), puis la roadmap par module — et **valider EXPLICITEMENT les deux avant de produire du contenu**. Un cas fil rouge mal calibré coûte cher à corriger une fois les ateliers rédigés.

C'est l'étape qui évite de découvrir à la fin qu'on a produit 200 slides quand le consultant en voulait 80, ou un cas fil rouge trop éloigné du métier réel du client. Mieux vaut 10 min de cadrage que 2h de retravail.

**Proposer la prochaine étape** en présentant le cas fil rouge et la roadmap : "Une fois le cas fil rouge et cette roadmap validés, je peux démarrer la génération du contenu du premier module (`slides.md`, `notes-formateur.md`) et de son premier atelier (`enonce-atelier-1.md` + corpus si besoin + solution), qui serviront ensuite de gabarit pour la suite. Veux-tu que je commence, ou souhaites-tu ajuster le cas fil rouge ou la roadmap d'abord ?"

### Phase 2 — Génération du contenu pédagogique (markdown)

Production module par module, dans l'ordre du plan.

**Avant de commencer**, lire :
- `references/slide_design.md` — principes de design des slides
- `references/slide_outline_format.md` — format markdown attendu pour `slides.md`
- `references/exercise_design.md` — comment concevoir des exercices
- `references/fil_rouge_design.md` — comment structurer un atelier fil rouge (énoncé, corpus, solution, conversion HTML)
- `references/pedagogical_principles.md` — principes transversaux à respecter

Pour chaque module, produire dans `modules/M<n>-<slug>/` :

1. **`slides.md`** — outline détaillée au format défini dans `slide_outline_format.md`. Chaque slide a un type (title/content/code/exercise/recap…), un timing, des notes formateur.

2. **`notes-formateur.md`** — timing module, messages clés (3-5 idées à retenir), points d'attention, anecdotes, questions anticipées, variantes si on a -30min ou +30min.

Et, pour chaque atelier du module, dans `livrables/atelier-N/` (voir `references/fil_rouge_design.md`) :

3. **`enonce-atelier-N.md`** — énoncé structuré, ancré dans le cas fil rouge : contexte (comment ce qui précède dans le fil rouge amène à cet atelier), objectif, consigne, critères de réussite, indices gradués (cf. `exercise_design.md`). Corpus de données dédié à côté de l'énoncé si l'atelier en a besoin.

4. **`livrables/solutions/solution-atelier-N.md`** — pour chaque atelier : approche pédagogique, solution complète, variantes, pièges fréquents, pour aller plus loin. **C'est un document formateur, pas un corrigé brut.** Ne pas le distribuer avant le debrief.

**Mode sans fil rouge** (seulement si demandé explicitement) : produire à la place `exercices.md` et `solutions.md` classiques par module (format antérieur, voir `exercise_design.md` § « Sans cas fil rouge »).

**Itération critique** : après le PREMIER module (et son premier atelier), présenter au consultant et demander un retour :
- Niveau de détail OK ?
- Style/ton OK ?
- Profondeur technique calibrée ?
- Le fil rouge s'intègre-t-il naturellement, ou force-t-il le propos ?

Le premier module sert de gabarit pour les autres. Ajuster avant de produire les 7 suivants. Pour les modules 2 à N, présenter à mesure mais pas besoin de bloquer entre chaque (sauf si le consultant le demande).

**Proposer la prochaine étape** après le premier module : "Le module 1 est prêt en markdown (`slides.md`, `notes-formateur.md`) avec son premier atelier (`enonce-atelier-1.md` + corpus si besoin + solution). Si ce gabarit te convient, je continue avec les modules suivants. Sinon, dis-moi ce qu'il faut ajuster avant que je poursuive." Après le dernier module : "Tous les modules et ateliers sont produits en markdown. Je peux maintenant compiler les livrables finaux (.pptx, énoncés HTML/PDF des ateliers, livret stagiaire, guide formateur) — veux-tu que je lance la Phase 3, ou veux-tu d'abord relire certains modules ?"

### Phase 3 — Génération des fichiers livrables

Déclenchée quand TOUS les modules sont validés en markdown.

#### 3.1 — Slides (.pptx) — brouillon de travail, pas le deck final

> **Ce `.pptx` est un brouillon jetable, pas le livrable visuel final.** Le rendu final des slides passe par `slide-content-claude-design` puis **Claude Design** (voir la note ci-dessous). Ce `.pptx` compilé par code sert seulement à : (a) relire vite le déroulé complet hors ligne, (b) donner un repli présentable si Claude Design n'est pas mobilisable pour une formation donnée. **Ne pas l'entretenir en parallèle du rendu Claude Design** — dès que les slides passent par Claude Design, c'est ce rendu-là qui fait foi, et ce `.pptx` cesse d'être maintenu (sinon on maintient deux decks divergents des mêmes slides).

Lire `/mnt/skills/public/pptx/SKILL.md` AVANT de générer le premier .pptx, puis `/mnt/skills/public/pptx/pptxgenjs.md` pour la syntaxe.

Stratégie : **un .pptx par module** (`livrables/M<n>-slides.pptx`). Plus maniable que un mega-deck, et les formateurs préfèrent souvent ce découpage. Si le consultant veut un deck unique, concaténer en post-traitement.

Pour la traduction `slides.md` → `.pptx`, écrire un script JS qui parse le markdown et produit un .pptx via `pptxgenjs`. Le script doit :
- Parser les blocs `## Slide N : …` séparés par `---`
- Mapper le champ `Type:` au layout pptxgenjs adapté
- Injecter les `Notes formateur:` en speaker notes du slide
- Préserver la structure visuelle décrite dans `slide_design.md`

**Format graphique par défaut** : sobre, lisible, projetable. Si le client a une charte propre, demander au consultant et adapter les tokens (couleurs, fonts, logo) dans le script ; sinon utiliser la charte par défaut « Encre & Sauge » (voir `slide-content-claude-design/SKILL.md`).

**Le rendu visuel final n'est pas ce `.pptx`.** Il se prépare avec `slide-content-claude-design` (qui transforme `slides.md` en fiches à générer dans Claude Design + prompts d'illustration Gemini), puis se compose dans **Claude Design**. Les deux voies partent du même `slides.md` : ce `.pptx` est le brouillon, Claude Design est le livrable. Ne pas les faire coexister comme deux decks à jour.

#### 3.1bis — Énoncés d'ateliers (.html + .pdf)

Pour chaque atelier produit en Phase 2, convertir `enonce-atelier-N.md` en `enonce-atelier-N.html` avec le gabarit de charte par défaut décrit dans `references/fil_rouge_design.md` § « Conversion HTML avec la charte par défaut » (bandeau bleu marine, métadonnées en tuiles, consigne numérotée, encadrés indices/bonus) — reprendre le CSS du gabarit tel quel, n'adapter que le contenu. Exporter ensuite `enonce-atelier-N.pdf` depuis le HTML.

**Mode sans fil rouge** : si la formation utilise le format classique (`exercices.md`), ignorer cette sous-phase.

#### 3.1ter — Corpus d'ateliers (conversion vers le format réel du métier)

Pour chaque élément de corpus rédigé en `.md` en Phase 2 dont le format cible réel n'est pas du texte brut, convertir selon `references/fil_rouge_design.md` § « Produire les éléments en format réaliste » — `.xlsx` par script Python (`openpyxl`, même méthode que `cadrage-formation`), `.docx` par la skill `docx` publique, `.png` pour une capture d'écran simulée, `.eml` par gabarit texte. Un élément déjà réaliste en `.md` brut (le vrai format du métier client) n'a pas besoin de conversion.

**Mode sans fil rouge** : si la formation utilise le format classique (`exercices.md`), cette sous-phase reste applicable aux fichiers complémentaires du dossier `assets/exercices/M<n>/` (voir `references/exercise_design.md` § « Format pratique »).

**Point de vérification avant d'enchaîner sur les .docx** : une fois 3.1/3.1bis/3.1ter produits, proposer un arrêt avant les compilations 3.2/3.3 (plus longues et plus coûteuses à refaire) : "Les slides (.pptx brouillon), les énoncés d'ateliers (HTML/PDF) et le corpus (formats réalistes) sont produits. Avant de compiler le livret stagiaire et le guide formateur — plus longs à régénérer en cas d'ajustement — veux-tu vérifier un aperçu, ou je continue directement ?" Ne pas bloquer si le consultant a déjà signalé vouloir tout enchaîner sans interruption.

#### 3.2 — Livret stagiaire (.docx)

Lire `/mnt/skills/public/docx/SKILL.md` AVANT.

Compiler tous les modules en `livrables/livret-stagiaire.docx`. Structure :

1. **Page de garde** — titre formation, client, dates, formateur
2. **Sommaire** automatique
3. **Introduction** — objectifs pédagogiques, modalités, calendrier
4. **Pour chaque module** :
   - Titre + objectifs + durée
   - Contenu narratif (synthèse écrite des slides, pas dump du markdown)
   - Énoncés des ateliers du module (repris depuis `enonce-atelier-N.md`, SANS solutions) — rappeler le fil rouge en 2-3 phrases si le stagiaire n'a pas suivi les ateliers précédents dans l'ordre
   - Espace pour notes du stagiaire
5. **Bibliographie & ressources**
6. **Annexes** (cheat sheets, glossaire si pertinent)

**Important** : le livret stagiaire est un document de **référence**, pas une copie des slides. Le texte doit se lire de manière autonome, ce qui n'est pas le cas du contenu d'un slide qui est complété par le discours du formateur.

#### 3.3 — Guide formateur (.docx)

Compiler en `livrables/guide-formateur.docx`. Reprend la structure du livret stagiaire, ENRICHIE de :

- **Solutions complètes** des ateliers (depuis `livrables/solutions/solution-atelier-N.md`)
- **Rappel du cas fil rouge** (depuis `livrables/00-fil-rouge.md`) en préambule, pour que le formateur ait la vue d'ensemble du fil narratif entre ateliers
- **Notes d'animation** par module (depuis `notes-formateur.md`)
- **Timing détaillé** par bloc
- **Anticipations** : questions fréquentes, blocages typiques, comment debrief les erreurs
- **Variantes de scénario** (si -30min / +30min / niveau plus faible / plus fort)

**Proposer la prochaine étape** une fois les livrables de Phase 3 produits (slides, énoncés d'ateliers HTML/PDF, livret stagiaire, guide formateur) : "Les slides, les énoncés d'ateliers (HTML/PDF), le livret stagiaire et le guide formateur sont générés. Je peux enchaîner sur le quiz d'évaluation (format Kahoot) et le document de prérequis/setup — veux-tu que je continue, ou préfères-tu d'abord relire ces livrables ?"

### Phase 4 — Livrables transverses

#### 4.1 — Quiz d'évaluation (format Kahoot)

Lire `references/quiz_design.md` AVANT.

Produire `livrables/quiz-kahoot.md` — le quiz final au **format Kahoot**, une fiche structurée par question (pas un simple QCM narratif). Pour CHAQUE question, préciser explicitement :

- **Question** — l'énoncé, **≤ 120 caractères** (limite de saisie Kahoot : reformuler plutôt que couper)
- **Type** — `quizz` (QCM classique) | `vrai/faux` | `réponse libre` | `curseur` (slider numérique) | `réponse par pins` (pointer une zone sur une image) | `puzzle` (remettre dans l'ordre)
- **Réponses possibles** — entre 2 et 6 options (obligatoire pour quizz/vrai-faux/pins/puzzle ; sans objet pour réponse libre/curseur — préciser alors la valeur ou la plage attendue)
- **Bonne réponse** — laquelle des options ci-dessus (ou plusieurs si limite de réponse = multiple)
- **Temps imparti** — entre 5 secondes et 4 minutes, calibré à la difficulté réelle (rappel court = 10-20s, application/cas = 45-90s, question ouverte = jusqu'à 2-4 min)
- **Points** — `standard` | `double` | `aucun` (aucun = question de sondage/discussion, ne compte pas au score)
- **Limite de réponse** — `une seule` (single select) | `plusieurs possibles` (multi-select)

Type par défaut : `quizz` à 4 réponses, limite de réponse unique, points standard — ne diversifier (vrai/faux, curseur, pins, puzzle) que si ça sert vraiment la question (ex. un ordre d'étapes → puzzle ; une estimation chiffrée → curseur), pas pour la variété en soi.

Composition du jeu de questions (inchangée) :
- 15-25 questions couvrant l'ensemble des modules, proportionnellement à leur durée
- Mix Bloom : ~30% rappel, ~50% application, ~20% transfert
- Les anciennes « questions ouvertes courtes » deviennent des questions **type `réponse libre`** (avec la ou les réponses acceptées listées) ou, si elles s'y prêtent, des `quizz`/`puzzle` reformulés à choix fermés — Kahoot n'a pas de correction manuelle différée, donc préférer les formats auto-corrigibles chaque fois que le fond le permet.
- Terminer par une **grille de correction récapitulative** (tableau question → bonne réponse → explication courte → référence module/slide) et un **récap de notation** (seuils excellent/acquis/à revoir), utiles au formateur pour le debrief même si Kahoot note déjà en direct.

Format de sortie attendu, une fiche par question :
```
### Question N
- **Question** : <énoncé, ≤ 120 caractères>
- **Type** : quizz | vrai/faux | réponse libre | curseur | réponse par pins | puzzle
- **Réponses possibles** : <2 à 6 options ; ou valeur/plage si curseur ; ou réponse(s) acceptée(s) si réponse libre>
- **Bonne réponse** : <option(s) correcte(s)>
- **Temps imparti** : <5s à 4min>
- **Points** : standard | double | aucun
- **Limite de réponse** : une seule | plusieurs possibles
- **Référence** : <module/slide, pour la grille de correction>
```

#### 4.2 — Prérequis & setup

Produire `livrables/prerequis-setup.md` (markdown suffit, pas besoin de .docx) :
- **Connaissances attendues** — prérequis cognitifs (sait faire X, a déjà vu Y…)
- **Environnement technique** — versions, libs, comptes, accès, droits IT à demander à la DSI
- **Datasets/fichiers** à télécharger en amont, avec liens et taille
- **Checklist auto-vérifiable** par le stagiaire avant le jour J

À envoyer aux stagiaires **3-5 jours avant** la formation.

#### 4.3 — Bibliographie (optionnel)

Si pertinent (formations niveau 200/300 ou si demandé par le client), produire `livrables/bibliographie.md` avec ressources par thème : livres, articles, MOOCs, conférences, repos GitHub.

**Proposer la prochaine étape** une fois tous les livrables de Phase 4 produits : "Le dossier de formation est complet en contenu (markdown, livret stagiaire, guide formateur, quiz, prérequis, énoncés d'ateliers HTML/PDF). Les `M<n>-slides.pptx` générés ici sont un **brouillon** du déroulé : le rendu visuel final des slides se prépare avec `slide-content-claude-design` puis se compose dans **Claude Design** — c'est l'étape suivante normale du pipeline pour les slides, pas une simple option (le `.pptx` brouillon n'est alors plus maintenu). Ensuite, `comite-qualite` audite l'ensemble. Veux-tu que je lance `slide-content-claude-design` pour préparer le rendu des slides, que je passe directement à `comite-qualite` sur le contenu markdown, ou souhaites-tu d'abord ajuster certains livrables toi-même ?"

---

## Conventions importantes

- **Workspace unique** : tout dans le workspace localisé en Phase 0 (`formations/<client>-<theme>/<AAAA-MM>/` si issu de `cadrage-formation`, sinon `/home/claude/projets/<slug-client>/`). Ne jamais éparpiller entre les deux une fois le workspace choisi.
- **Markdown-first** : tout le contenu est rédigé en markdown avant compilation. Permet itération facile.
- **Un module = un dossier** dans `modules/`. Nommage strict : `M<numéro>-<slug-kebab>`.
- **Un cas fil rouge, jamais plusieurs** : toute la formation partage le même cas fictif (`livrables/00-fil-rouge.md`). Ne jamais introduire un second cas en cours de route, même pour un module qui semble s'y prêter mieux — décliner plutôt le cas existant.
- **Un atelier = un dossier** dans `livrables/atelier-N/`, numéroté dans l'ordre de passation (pas par module). Solutions toujours dans `livrables/solutions/`, jamais à côté de l'énoncé.
- **Itération module par module** : NE JAMAIS produire les 8 modules d'un coup au premier essai. Toujours valider le premier pour calibrer style et niveau de détail.
- **Langue** : français pour tous les livrables, sauf si le brief précise explicitement anglais ou bilingue.
- **Pas d'invention** : si un point pédagogique n'est pas clair dans le plan ou la recherche, **demander au consultant** — ne jamais combler avec du générique vague.
- **Sources** : si le contenu d'un slide ou exercice s'appuie sur une référence externe, la citer dans `notes-formateur.md` (URL ou DOI).
- **Présenter chaque livrable** via `present_files` à la fin de chaque sous-phase, pour téléchargement.

## Détection automatique de la phase

Au démarrage, regarder ce qui existe déjà dans le workspace :

| État du workspace | Phase actuelle | Action |
|---|---|---|
| Pas de workspace, ou xlsx/contexte absent | Phase 0.1 | Localiser le workspace, ingérer le xlsx (ou récupérer le contexte en mode standalone) |
| xlsx ingéré (ou contexte fourni), pas de `00-brief.md`/`00-plan.md` | Phase 0.2 | Produire et faire valider le brief et le plan |
| `00-brief.md`/`00-plan.md` validés, pas de `06-material-roadmap.md` | Phase 1 | Produire le cas fil rouge (`livrables/00-fil-rouge.md`) et la roadmap |
| Fil rouge et roadmap présents, pas de `modules/` ou modules vides | Phase 2 | Produire le contenu pédagogique et les ateliers |
| Tous les modules/ateliers en markdown, pas de `livrables/M<n>-slides.pptx` | Phase 3 | Compiler en .pptx/.html/.pdf/.docx |
| Slides + énoncés HTML + livret + guide présents, pas de quiz | Phase 4 | Produire quiz, prérequis, biblio |
| Tout présent | Terminé | Proposer `comite-qualite` sur le dossier complet, ou demander au consultant ce qu'il veut itérer |

**Exception** : si le consultant dit explicitement "régénère le module 3", "refais les slides", "ajoute un atelier au module 2", on saute la détection et on exécute la demande.

---

## Fichiers de référence

- `references/module_structure.md` — Structure standard d'un module et conventions de nommage.
- `references/slide_design.md` — Principes de design de slides de formation efficaces.
- `references/slide_outline_format.md` — Format markdown pour structurer `slides.md`.
- `references/exercise_design.md` — Comment concevoir des exercices pédagogiques.
- `references/fil_rouge_design.md` — Comment concevoir un cas fil rouge et structurer les ateliers qui s'y ancrent (énoncé, corpus, solutions, conversion HTML charte par défaut).
- `references/pedagogical_principles.md` — Principes d'apprentissage adulte transversaux.
- `references/quiz_design.md` — Conception d'un quiz d'évaluation efficace.
