---
name: slide-content-claude-design
description: Transforme un plan de formation / un rapport de recherche / des notes en CONTENU DE SLIDES prêt à générer dans Claude Design — DEUX fichiers par module, M<n>-slides-content.md (une fiche par slide : titre, accroche, contenu, visuel dimensionné/positionné/colorisé précisément, bloc texte, placeholder d'illustration dimensionné et positionné) et M<n>-prompts.md (bloc « Direction artistique » ancré dans la métaphore filée globale de la formation + prompts d'illustration Gemini structurés par slide, palette par défaut, sans texte dans l'image). Applique le design system fourni (par défaut celui décrit ci-dessous, nom de code « Encre & Sauge »). Déclenche cette skill quand l'utilisateur demande de "générer le contenu des slides", "préparer les slides pour Claude Design", "transformer ce plan/markdown en slides", "faire le déroulé slide par slide", ou tout équivalent de mise en forme de contenu présentation optimisé pour une génération visuelle. Peut, en option, produire aussi le script formateur et les quiz associés.
---

# Slide Content for Claude Design

Produit, pour chaque module, **deux fichiers colocalisés** : `M<n>-slides-content.md`, le contenu slide par slide optimisé pour être copié-collé dans **Claude Design** (avec un placeholder d'illustration dimensionné et positionné par slide), et `M<n>-prompts.md`, les prompts d'illustration à donner à **Gemini** — le tout en respectant un **design system**.

## Quand l'utiliser
- L'utilisateur a un plan de formation, un rapport, des notes ou un markdown et veut le **contenu des slides**.
- Le rendu final passera par **Claude Design** (contenu + composants) et **Gemini** (illustrations) → il faut un format découpé, une suggestion de composant par slide, et un prompt image par slide dans un fichier séparé.

> **Articulation avec le `.pptx` de `formation-material-builder`.** Si les slides viennent de `formation-material-builder`, un `M<n>-slides.pptx` a déjà été compilé par code en Phase 3.1 — mais ce n'est qu'un **brouillon du déroulé**, pas le livrable visuel. **Claude Design est la voie du deck final** : cette skill prépare le contenu, Claude Design le compose, et le `.pptx` brouillon cesse d'être maintenu dès qu'on entre ici. On ne fait pas coexister deux decks à jour des mêmes slides — le rendu Claude Design fait foi.

## Inputs attendus
| Input | Statut | Rôle |
|---|---|---|
| Source de contenu (plan, recherche, brief, .md) | requis | matière des slides ; **ancrer les chiffres dessus, ne rien inventer** |
| Design system (tokens couleurs/typo/composants) | recommandé | cohérence visuelle ; défaut = **Encre & Sauge** (voir plus bas) |
| Métaphore filée / fil rouge | recommandé | renforce l'arc narratif — voir « Où trouver la métaphore filée » ci-dessous |
| Plage de numérotation des slides | optionnel | utile pour aligner avec un script ou un découpage multi-blocs |

### Où trouver la métaphore filée

Avant de rédiger le bloc « Direction artistique » d'un module (étape 4 ci-dessous), établir la métaphore filée **globale** de la formation, dans cet ordre de priorité :

1. **`livrables/00-fil-rouge.md`** — si `formation-material-builder` a produit un cas fil rouge pour cette formation (standard par défaut, voir US-12), le nom du produit/contexte fictif et son univers **sont** la métaphore filée globale. Ex. un cas fil rouge « StockPilot » (gestion de matériel de chantier) donne une métaphore filée d'atelier/chantier — pas besoin d'en inventer une autre.
2. **Métaphore explicite fournie par le consultant** — si le brief ou la conversation mentionne une métaphore filée (ex. « l'expédition », « le chantier »), la reprendre telle quelle.
3. **Aucune des deux** — proposer une métaphore filée cohérente avec le domaine du client (2-3 phrases) et la faire valider avant de produire le premier bloc Direction artistique. Ne jamais improviser une métaphore différente à chaque module : elle se fixe une fois, globalement, puis se **décline** par module.

Cette métaphore filée globale est ce que chaque bloc « Direction artistique » (un par module, voir plus bas) décline localement — elle doit être identifiable en une phrase avant de commencer à écrire des prompts.

## Méthode (étapes)
0. **Si la densité et le design system n'ont pas été précisés spontanément**, les demander avant de commencer à produire : *« Deux paramètres avant de commencer : (1) densité — une idée par slide ("complet") ou plusieurs idées regroupées par slide ("condensé") ? (2) design system — la charte par défaut par défaut convient, ou le client a-t-elle une charte propre à appliquer ? »* Ne pas deviner ces deux paramètres ni les fixer par défaut sans les avoir posés — ce sont des choix structurants qui coûtent cher à corriger après coup (toutes les slides déjà rédigées).
1. **Lire la/les source(s)** et en extraire l'arc : modules → idées-clés. Une **idée = une slide** (densité « complet »), ou regrouper (densité « condensé ») selon la réponse à l'étape 0.
2. **Établir la métaphore filée globale** de la formation (voir « Où trouver la métaphore filée » ci-dessus) — une seule fois, avant le premier module, jamais réinventée en cours de route.
3. **Construire la colonne vertébrale** : liste numérotée de slides (type + titre + objectif d'une ligne) AVANT de rédiger. La faire valider si la formation est longue.
4. **Avant la première slide d'un module**, rédiger le bloc **« Direction artistique »** en tête de `M<n>-prompts.md` (style illustratif, déclinaison de la métaphore filée globale pour ce module, contraintes récurrentes). **Rédiger chaque slide** au format imposé (ci-dessous, avec le champ `Visuel` entièrement dimensionné/positionné/colorisé) **et sa section `§ Slide N` dans `M<n>-prompts.md`**, qui référence ce bloc (les deux fichiers avancent ensemble, slide par slide).
5. **Vérifier l'ancrage** : chaque chiffre cité existe dans la source ; ROI fournisseurs = ordres de grandeur.
6. **Pour de gros volumes** : paralléliser par bloc/module (un agent par bloc avec la même colonne vertébrale + le même brief design + métaphore filée globale) — chaque agent produit ses fiches **et** ses sections de prompts — puis assembler les **deux** fichiers en gardant la numérotation globale.
7. **Avant toute génération visuelle dans Claude Design** : proposer un audit UX/UI de `M<n>-slides-content.md` (hiérarchie visuelle, densité de contenu par slide, dimensions/positions/couleurs des visuels et placeholders, cohérence inter-slides). L'audit précède la génération — pas l'inverse.

## Format de sortie — deux fichiers par module

**Livrables et emplacement** : pour chaque module, **deux fichiers colocalisés** dans le workspace de la formation s'il existe (racine `formations/<client>-<theme>/<AAAA-MM>/` selon la convention de `cadrage-formation`, sous-dossier `livrables/` selon la structure de workspace de `formation-material-builder` — ainsi les fichiers restent dans le périmètre qu'auditera `comite-qualite` lors d'un audit de dossier complet, revue inter-livrables) :

1. **`M<n>-slides-content.md`** — Contenu pour Claude Design (fiches structurées par slide, avec placeholders dimensionnés pour l'illustration)
2. **`M<n>-prompts.md`** — Prompts d'illustration pour Gemini (un prompt par slide, respectant le design system par défaut « Encre & Sauge »)

Sans workspace identifiable, livrer les deux fichiers là où se trouvent les sources fournies.

````
### Slide N — TYPE — Titre court
- **Titre à l'écran** : <titre ; bicolore possible : MOT **mot-clé accent**>
- **Accroche / sous-titre** : <une phrase choc, courte>
- **Contenu** :
  - <3 à 5 puces concises, orientées audience>
- **Chiffre / preuve clé** : <donnée + (source)>   ← omettre si non pertinent
- **Visuel <design system>** :
  - **Composant** : <UN type précis, pas une liste : 3 cartes | tableau comparatif | matrice 2×2 | timeline | citation | KPI tiles>
  - **Dimensions et position sur le canevas** : <L × H px + emplacement exact, ex. « 3 cartes de 380×420 px chacune, alignées horizontalement, centrées à 80 px sous le titre »>
  - **Couleurs** : <tokens par défaut exacts appliqués à CE composant, ex. « bordure bleu marine #2C5F8A 2px sur la carte du milieu (mise en avant), fond blanc, texte encre #1F1F1F, labels en pilule vert sauge #4A8B6F »>
  - **Contenu du composant** : <ce qui remplit chaque partie — pas de placeholder vague, le texte réel ou sa structure exacte>
- **Bloc texte (si besoin)** : <texte à incruster proprement dans la slide, HORS image>
- **Bloc (si fallback vectoriel)** : <composant à construire en couche vectorielle/texte>   ← remplace le Placeholder image, voir Fallback plus bas
- **Placeholder image** :
  ```
  [PLACEHOLDER GRIS — IMAGE GÉNÉRÉE GEMINI]
  Dimensions exactes : <L × H px de la zone réservée sur CETTE slide>
  Position : <ex. moitié droite / bandeau inférieur / pleine largeur sous le titre>
  Voir prompt détaillé → M<n>-prompts.md § Slide N
  ```
````
`TYPE ∈ {TITRE, SECTION, CONTENU, COMPARATIF, DONNÉES, CAS, ATELIER, MATRICE, SYNTHÈSE, TRANSITION}`

**Exemple rempli** (slide CONTENU, comparatif de 3 offres) :
```
- **Visuel Encre & Sauge** :
  - **Composant** : 3 cartes
  - **Dimensions et position** : 3 cartes de 380×420 px, alignées horizontalement avec 40 px d'espacement, centrées à 100 px sous le titre, jusqu'à 620 px de hauteur de canevas
  - **Couleurs** : carte du milieu (offre recommandée) — bordure bleu marine #2C5F8A 2px, bandeau d'en-tête bleu marine plein ; cartes latérales — bordure gris #E8E2DA 1px, bandeau encre #1F1F1F ; fond des 3 cartes blanc ; label en pilule vert sauge #4A8B6F en coin haut-droit de chaque carte
  - **Contenu** : titre de l'offre (bandeau), 3 critères avec icône, prix en gros chiffre bas de carte
```

**Règle** : ne jamais laisser « Visuel » comme une simple catégorie de composant sans dimensions ni couleurs — le lecteur qui colle la fiche dans Claude Design doit pouvoir construire le composant sans deviner un seul paramètre visuel.

### Règles du placeholder d'illustration

Le placeholder n'est **jamais générique** : ses dimensions et sa position sont **spécifiques à chaque slide** et découlent du composant/layout suggéré dans le champ `Visuel`. Dans Claude Design, il se matérialise par un **rectangle gris neutre** (`#D6D6D6` ou fond `#F7F7F7`) aux dimensions exactes de l'image attendue — c'est la zone verrouillée où l'illustration Gemini sera insérée telle quelle, sans recadrage ni déformation.

Gabarits d'emplacement types (canevas de référence 1280 × 720 px) :

| Emplacement | Dimensions indicatives | Usage typique |
|---|---|---|
| Pleine slide | 1280 × 720 px | slides TITRE / SECTION (image de couverture) |
| Moitié droite (ou gauche) | 600 × 560 px | slide CONTENU avec puces à côté de l'illustration |
| Bandeau inférieur | 1280 × 280 px | illustration d'ambiance sous le contenu |
| Vignette | 420 × 320 px | slide dense où l'image n'est qu'un appui |

Ces gabarits sont des points de départ : ajuster aux marges du layout réel (padding 12 px du canevas de référence) et reporter **les mêmes dimensions et le même cadrage** dans la section correspondante de `M<n>-prompts.md`, pour que l'image générée tombe juste dans la zone réservée.

## Fichier `M<n>-prompts.md` — Prompts Gemini structurés

Le fichier s'ouvre par un bloc **« Direction artistique »** unique, puis une **section dédiée** par slide illustrée.

### Bloc « Direction artistique » (obligatoire, en tête de fichier)

Généré **une fois par module**, ce bloc cadre le style et la cohérence de toutes les illustrations du module — les prompts individuels le référencent au lieu de répéter des instructions de style. Sans lui, chaque slide reste une génération isolée et le rendu final ressemble à un patchwork plutôt qu'à un jeu d'illustrations pensé par un même directeur artistique.

```markdown
# Direction artistique — Module M<n>

**Style illustratif** : illustration éditoriale moderne et épurée, traits nets, formes géométriques douces, aplats de couleur (pas de dégradés complexes ni de texture photoréaliste), niveau de détail volontairement bas pour rester lisible en projection.

**Métaphore filée du module** : <déclinaison, pour ce module, de la métaphore filée globale de la formation — ex. si la métaphore globale est « l'expédition », ce module peut la décliner en « préparer le campement » ; si aucune métaphore n'existe, décrire l'univers visuel cohérent adopté par défaut (ex. scènes de bureau/atelier contemporain)>

**Contraintes récurrentes (s'appliquent à CHAQUE prompt du module)** :
- Palette par défaut : bleu marine `#2C5F8A` (accent principal, usage parcimonieux) / corail `#D97757` / vert sauge `#4A8B6F`, fond blanc, formes douces
- Aucun texte dans l'image (titres, labels, chiffres → en couche texte sur la slide)
- Cadrage paysage 16:9, dimensions reprises du placeholder de chaque slide
- Complexité volontairement basse pour faire ressortir les phrases chocs ou mises en situation, pas la richesse du dessin
- Zéro faute d'orthographe, aucun doublon de texte entre slide et illustration
```

La **métaphore filée** est la clé de la cohérence perçue : deux illustrations d'un même module doivent donner l'impression de sortir du même univers visuel, pas de deux générateurs différents. Le bloc peut varier légèrement d'un module à l'autre (ex. un sous-thème visuel propre au module), mais reste ancré dans la **même métaphore filée globale de la formation** — ne pas changer d'univers visuel en cours de route.

### Section par slide

```markdown
## Slide N — Illustration

**Contenu clé** : <ce qui doit être illustré, en 1-2 phrases>

**Dimensions / position** : <reprises à l'identique du placeholder de la fiche Slide N — ex. 600 × 560 px, moitié droite>

**Prompt pour Gemini** :

Illustration conceptuelle : <scène centrale concrète et évocatrice, ancrée dans la métaphore filée du bloc Direction artistique ci-dessus>

Style : voir bloc « Direction artistique » en tête de ce fichier — même style illustratif, même métaphore, mêmes contraintes récurrentes. Cadrage <dimensions exactes du placeholder de cette slide, ex. paysage 16:9 (1280×720) pour une image pleine slide>.
```

Chaque prompt de slide **référence** le bloc Direction artistique plutôt que de répéter la liste de contraintes — cela garantit qu'une modification de style se fait à un seul endroit et se propage à toutes les slides du module.

**Tokens exacts (pour le bloc Direction artistique)** :
- **Bleu marine (accent principal, usage parcimonieux)** : `#2C5F8A`
- **Corail (accent secondaire, data viz)** : `#D97757`
- **Vert sauge (accent tertiaire, data viz)** : `#4A8B6F`
- **Neutres** : encre `#1F1F1F`, gris `#F7F7F7`, beige/warm `#E8E2DA`

### Règle critique « texte dans l'image »
Les générateurs d'image (dont Claude Design) **ne garantissent pas l'orthographe** dans les visuels. Donc :
- **Jamais de texte dans le prompt image.** Le prompt décrit une scène/illustration, pas un poster (la ligne « sans texte dans l'image » + « zéro faute d'orthographe » du template le verrouille).
- Tout texte nécessaire (chiffre choc, label, titre) → le mettre dans **`Bloc texte :`**, ajouté comme **élément texte par-dessus** l'image dans l'outil (police du design system), pas généré dans l'image.

### Fallback « hors compétences du générateur d'image »
Si la slide demande un visuel que le générateur d'image **ne saura pas rendre correctement** (schéma précis avec étiquettes, diagramme technique, graphe chiffré, capture d'écran d'outil, tableau…), **ne pas forcer un prompt image** : à la place, remplir le champ **`Bloc (si fallback vectoriel) :`** de la fiche en décrivant le composant à construire directement dans Claude Design en couche vectorielle/texte (ex. « Bloc : matrice 2×2 vectorielle, axes Valeur × Faisabilité, 4 cas Galec positionnés »). Dans ce cas :
- le champ **`Placeholder image`** est **omis** de la fiche (le `Bloc` le remplace) ;
- dans `M<n>-prompts.md`, conserver la numérotation continue avec une ligne courte : `## Slide N — pas d'illustration : composant vectoriel` (aucun prompt à générer).

Le bitmap généré est réservé aux **illustrations conceptuelles** sans texte ; tout ce qui porte de l'information précise se fait en couche texte/vecteur.

## Design system par défaut — Encre & Sauge
Si aucun design system n'est fourni, utiliser « Encre & Sauge ». Les tokens essentiels sont inlinés ci-dessous ; une référence complète séparée (fichier de tokens + spécimen de composants) peut être ajoutée au dépôt si besoin (cf. `BACKLOG.md`, item #20).

**Pour les fiches `M<n>-slides-content.md` (Claude Design)** :
- **Accent unique** : bleu marine `#2C5F8A` (avec parcimonie). Neutres : encre `#1F1F1F`, gris `#4A4A4A`/`#6B6B6B`, fonds blanc/`#F7F7F7`, beige chaud `#E8E2DA`. Accents data : corail `#D97757`, vert sauge `#4A8B6F`.
- **Typo** : titres **Sora** (bicolores : encre + mot-clé bleu marine, souligné bleu marine) ; corps **Inter**.
- **Composants** : cartes (bordure accent / bandeau d'en-tête bleu marine / label en pilule), tableaux (en-tête bleu marine + zébrage pêche), matrice 2×2, KPI tiles, bandeau de message-clé pleine largeur, timeline, citation.

**Pour les prompts `M<n>-prompts.md` (Gemini)** : palette et règles strictes = celles du template canonique au § « Fichier `M<n>-prompts.md` — Prompts Gemini structurés » (source unique, ne pas dupliquer la liste ici).

## Conseils d'usage dans Claude Design
- Coller **slide par slide** (une fiche = une demande) pour garder le contrôle, ou par module.
- Demander explicitement le composant indiqué + la palette ; rappeler « pas de texte dans l'image, j'ajoute les blocs texte moi-même ».
- Réutiliser le `Bloc texte` tel quel pour l'incrustation (évite les fautes).

## Conseils d'usage avec Gemini
- **Coller AUSSI le bloc « Direction artistique » avant chaque prompt de slide** (ou le fusionner dedans) : Gemini ne reçoit que le texte collé, jamais le reste du fichier — la ligne « voir bloc Direction artistique en tête de ce fichier » ne se résout pas toute seule une fois isolée du document.
- **Générer les illustrations par lots, pas slide par slide** : ouvrir UNE session Gemini pour le module, y coller le bloc « Direction artistique » **une seule fois** en tête, puis enchaîner les prompts `## Slide N` à la suite pour produire toutes les images du module d'affilée. On collecte le lot d'illustrations en une passe, au lieu de rouvrir Gemini à chaque slide.

## Ordre de travail recommandé — par lots (par défaut)

Le rendu final combine trois manipulations manuelles (fiche → Claude Design, prompt → Gemini, image → placeholder). Les enchaîner **slide par slide** multiplie les changements de contexte entre les deux outils autant de fois qu'il y a de slides. Les deux fichiers sont déjà structurés pour un traitement par lots (bloc « Direction artistique » unique, dimensions de placeholder reprises à l'identique côté fiche et côté prompt) — donc **travailler par phases, pas par slide** :

- **Phase A — toutes les illustrations d'abord (Gemini).** Générer en une session Gemini l'ensemble des images du module (voir « Conseils d'usage avec Gemini » ci-dessus), et les nommer par numéro de slide pour les retrouver.
- **Phase B — une seule passe dans Claude Design.** Coller les fiches `M<n>-slides-content.md` et déposer, dans chaque placeholder gris, l'image déjà prête de la Phase A.

Ce mode réduit les allers-retours sans changer d'outil ni attendre l'automatisation de la génération d'illustrations (piste de fond au backlog, item #9). Le collage **slide par slide** reste un repli légitime quand on veut valider visuellement chaque slide avant de passer à la suivante.

## Extensions optionnelles
- **Script formateur** : produire en parallèle un script slide par slide (verbatim « À dire / À faire / Transition »), idéalement avec une **métaphore filée**.
- **Quiz (Kahoot)** : un quiz par module ; pour chaque question préciser type, temps, points, limite de réponse, question, bonne réponse, distracteurs.
- Garder la **numérotation des slides cohérente** entre slides, script et quiz.

## Proposer la prochaine étape

Une fois les deux fichiers (`M<n>-slides-content.md` et `M<n>-prompts.md`) livrés pour un module (ou l'ensemble), proposer explicitement la suite :

> Les fiches slide-par-slide du module <n> sont prêtes.
> 
> **Avant de générer visuellement dans Claude Design**, je recommande de passer `M<n>-slides-content.md` par un **audit UX/UI rapide** (respect de la hiérarchie visuelle, densité de contenu par slide, dimensions/positions des placeholders, cohérence entre slides) pour s'assurer que le contenu textuel est bien structuré.
> 
> **Ensuite, travaille par lots (recommandé — évite les allers-retours entre outils) :**
> 1. **Phase A — Gemini d'abord** : dans une seule session Gemini, colle le bloc « Direction artistique » une fois, puis enchaîne les prompts `## Slide N` de `M<n>-prompts.md` pour générer toutes les illustrations du module d'affilée. Nomme chaque image par son numéro de slide.
> 2. **Phase B — Claude Design ensuite** : en une passe, colle les fiches de `M<n>-slides-content.md` (avec la palette par défaut) et dépose chaque illustration de la Phase A dans son placeholder gris.
> 
> (Pour un contrôle fin, tu peux aussi faire slide par slide — fiche → Gemini → image — mais c'est plus lent.)
> 
> Une fois le rendu visuel complet dans Claude Design (le deck final ; le `M<n>-slides.pptx` de `formation-material-builder` n'était qu'un brouillon et n'est plus maintenu), je recommande de passer l'ensemble par `comite-qualite` pour vérifier la cohérence visuelle et le respect de la charte.
> 
> Préfères-tu que je prépare aussi le script formateur ou le quiz de ce module avant, ou préfères-tu générer les slides d'abord ?

Adapter selon ce qui a déjà été produit (module unique vs formation complète, audit en solo vs collaboratif) plutôt que d'utiliser un texte figé.
