# Principes de design des slides de formation

## Le principe fondamental : un slide = une idée

Si un slide contient plus d'une idée, il faut le scinder. C'est la première règle, la plus difficile à respecter, et celle qui change le plus la qualité d'une formation.

Les slides "wall of text" sont à proscrire. Les bullets en cascade sont à éviter (3 niveaux d'indentation = signal qu'on a tassé trop de contenu).

## Densité indicative

Pour de la théorie / transmission : **10-15 slides par heure** de présentation.

Pour un atelier ou du live coding : **3-5 slides par heure** (le reste du temps est dans la pratique, pas dans les slides).

Ces ratios sont indicatifs. Un sujet abstrait (gouvernance data, théorie ML) tolère plus de slides. Un sujet concret (commandes shell, Python) en demande moins (les slides sont juste des jalons entre des démos).

## Types de slides à utiliser

### `title` — Titre / section
Page de couverture, ouverture de partie. 1-2 lignes max.

### `agenda` — Plan
Plan de la journée ou du module. Idéalement réutilisé en fin de module pour montrer la progression accomplie.

### `content` — Concept / contenu
Présente UN concept. Format recommandé : le titre est la phrase à retenir (pas un mot-clé). Le corps : 3-4 puces concrètes ou un visuel qui éclaire.

### `image` ou `diagram` — Visuel
Un schéma vaut mieux que du texte sur les sujets architecturaux. Si on n'a pas le temps de produire un schéma propre, mieux vaut un croquis annoté qu'une liste à puces.

### `code` — Code / exemple
Du code à l'écran : doit être lisible au fond de la salle (minimum 18pt). Code visible = max 15 lignes. Si plus, c'est un fichier à part qu'on ouvre dans l'IDE, pas un slide.

### `exercise` — Atelier / exercice
Lance un atelier : énoncé court, durée affichée en gros, critères de réussite. Ce slide reste à l'écran pendant que les stagiaires travaillent.

### `recap` — Takeaways
Fin de module. 3-5 takeaways en **phrases complètes** (pas en mots-clés). C'est ce qu'on veut que le stagiaire retienne dans 6 mois — donc rédiger comme tel.

### `transition` — Respiration / question
Entre deux sections, un slide-question ou un slide-image pour faire respirer. Évite l'effet "tunnel" de slides denses qui s'enchaînent.

## Anti-patterns fréquents

- **Le slide "agenda" à 12 puces** → résumer en 4-5 blocs max
- **Le slide pollué de logos / decorations** → bruit visuel, distrait
- **Le slide à 3 niveaux d'indentation** → splitter ou simplifier
- **Le slide capture d'écran microscopique** → agrandir, recadrer, ou redessiner
- **Le slide qui résume le slide précédent** → en supprimer un
- **Le slide "Merci de votre attention"** → remplacer par une vraie conclusion avec les takeaways
- **Le titre générique "Introduction"** → titrer avec le message-clé du slide

## Tone of voice sur les slides

- **Phrases complètes** pour les messages-clés et les recap (un stagiaire qui revoit les slides 1 mois plus tard doit comprendre seul)
- **Listes à puces** OK pour des énumérations factuelles (caractéristiques, options, étapes)
- **Pas de jargon non défini** dans les premiers slides d'un sujet — introduire un terme, puis l'utiliser
- **Métaphores bienvenues**, même informelles — elles aident à l'ancrage mémoriel
- **Numéros et données concrètes** > généralités abstraites

## Cohérence visuelle

À travers tous les slides d'une même formation :

- **Une palette de couleurs** (3-4 couleurs max), commitée — un dominant, un secondaire, un accent
- **Une typographie cohérente** — 1 font pour les titres, 1 font pour le corps (peut être la même)
- **Une grille de mise en page** — titres au même endroit, footers identiques, marges constantes
- **Un motif visuel** discret mais reconnaissable — par exemple, un trait de couleur en haut/bas du slide, ou un cadre coloré pour les exercices
- **Footer minimal** — nom de la formation + numéro de slide. Pas de logos partout.

## Speaker notes

Les notes formateur (`Notes formateur:` dans `slides.md`) seront injectées comme **speaker notes** du slide dans le .pptx. Pour chaque slide, prévoir au minimum :
- Le message clé à passer en 1-2 phrases
- Le timing approximatif
- Une anecdote ou exemple à utiliser si pertinent
- Les transitions vers le slide suivant

Ces notes ne sont pas visibles par les stagiaires en mode présentation. Le formateur les voit en mode "écran formateur" pendant l'animation.
