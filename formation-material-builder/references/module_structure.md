# Structure d'un module

Un module = un dossier dans `modules/`. Convention de nommage : `M<numéro>-<slug-kebab-case>`.

Exemples : `M1-introduction-ia-generative`, `M3-fine-tuning-llm`, `M5-evaluation-modeles`.

## Fichiers obligatoires par module

Chaque module contient exactement 2 fichiers markdown : `slides.md` et `notes-formateur.md`. Ne pas en ajouter ni en retirer — la compilation en Phase 3 dépend de cette structure.

Les **ateliers** du module ne vivent pas dans le dossier du module : ils vivent dans `livrables/atelier-N/` (énoncé + corpus dédié) avec leurs solutions dans `livrables/solutions/`, selon le standard **cas fil rouge** décrit dans `fil_rouge_design.md`. Un module peut avoir zéro, un, ou plusieurs ateliers ; la numérotation des ateliers suit l'ordre de passation global de la formation, pas le numéro du module.

**Mode sans fil rouge** (sur demande explicite uniquement) : le module contient alors aussi `exercices.md` et `solutions.md` — voir `exercise_design.md` § « Sans cas fil rouge ».

### `slides.md`

Outline structurée des slides du module en markdown. Voir `slide_outline_format.md` pour le format exact.

Chaque slide est un bloc séparé par `---`, avec un titre `## Slide N : …` et des métadonnées (Type, Timing, Layout, Code, Notes formateur, etc.).

Densité indicative : 10-15 slides par heure de théorie, 5-8 slides pour un atelier (le reste du temps est dans la pratique).

### `notes-formateur.md`

Notes d'animation. Structurées en sections fixes :

```markdown
# Notes formateur — Module M<n> : <titre>

## Timing du module
Découpage minute par minute du module :
- 9h00-9h05 : Ouverture / contexte
- 9h05-9h25 : Bloc 1 — théorie
- 9h25-9h55 : Atelier 1
- 9h55-10h00 : Debrief atelier
- ...

## Messages clés (à retenir absolument)
3-5 idées que le stagiaire doit retenir dans 6 mois, formulées en phrases complètes.

## Points d'attention
Passages où l'audience décroche habituellement, où les questions affluent, où il faut être lent et patient.

## Anecdotes & exemples
Récits, REX, métaphores à utiliser. Une bonne anecdote ancre un concept abstrait.

## Questions anticipées
Questions fréquentes du public, avec éléments de réponse courts.

## Variantes
- **Si -30min de timing** : qu'est-ce qu'on saute ? Qu'est-ce qu'on garde absolument ?
- **Si +30min de timing** : quel approfondissement ? Quel exercice bonus ?
- **Si public plus junior** : qu'est-ce qu'on simplifie ?
- **Si public plus senior** : quel angle d'approche en plus ?
```

---

## Structure du livret stagiaire compilé

Le `livrables/livret-stagiaire.docx` est compilé depuis les modules à la Phase 3.2.

Structure attendue :

1. **Page de garde** — titre formation, client, dates, formateur (mention sobre)
2. **Sommaire** automatique généré
3. **Introduction**
   - Objectifs pédagogiques généraux
   - Public cible
   - Modalités (durée, format présentiel/distanciel, prérequis)
   - Comment utiliser ce livret (référence, pas slides)
4. **Pour chaque module**, dans l'ordre :
   - Titre + durée + objectifs spécifiques
   - **Synthèse narrative du contenu** — pas un copier-coller des slides, mais un texte qui se tient seul, lisible 6 mois après. Environ 1-3 pages par module.
   - **Énoncés des ateliers** — repris depuis `livrables/atelier-N/enonce-atelier-N.md`, SANS les solutions
   - **Espace de notes personnelles** (1/2 page blanche entre modules)
5. **Bibliographie & ressources**
6. **Annexes**
   - Glossaire des termes techniques utilisés
   - Cheat sheets (si pertinent : commandes Git, API LLM, syntaxe SQL…)
   - Index des concepts

**Principe rédactionnel** : un slide ne se lit pas, il est complété par le discours du formateur. Le livret, lui, doit se lire de manière **autonome**. Cela veut dire reformuler, étoffer, ajouter les transitions implicites du discours oral. C'est un travail de réécriture, pas de copier-coller.

---

## Structure du guide formateur compilé

Le `livrables/guide-formateur.docx` reprend la structure du livret stagiaire mais l'enrichit substantiellement :

Pour chaque module :
- Tout ce que contient le livret stagiaire
- **Solutions complètes** des ateliers (depuis `livrables/solutions/solution-atelier-N.md`)
- **Notes d'animation** (depuis `notes-formateur.md`)
- **Timing minute par minute** affiché clairement
- **Anticipations & dépannage** : que faire si on a 30min de retard, si un atelier coince, si une question piège arrive
- **Liste matériel/setup** spécifique au module

Le guide formateur est confidentiel — réservé au formateur et au client (RH ou L&D). Ne JAMAIS l'inclure dans le livret stagiaire.
