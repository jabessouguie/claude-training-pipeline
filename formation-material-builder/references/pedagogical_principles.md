# Principes pédagogiques transversaux

Ce fichier rappelle les principes d'apprentissage adulte qui doivent transparaître dans tous les livrables (slides, exercices, livret, quiz). Pas une théorie académique — des règles applicables.

## 1. Donner du sens avant tout

Un adulte n'apprend pas s'il ne comprend pas POURQUOI il apprend.

Chaque module doit commencer par :
- Un **cas concret** ou une **question ouverte** — pas par une définition
- Un **lien avec le métier** du stagiaire — pas avec "le programme de la formation"

Avant d'enseigner un concept, raconter une situation où l'absence de ce concept pose problème. La curiosité allumée par le manque est le meilleur moteur d'apprentissage.

**Application pratique** : le premier slide de chaque module doit contenir le « pourquoi » du module, pas son contenu.

## 2. Active learning > passive listening

**Loi des 20 minutes** : au-delà de 20 minutes de présentation continue, l'attention décroche.

Insérer toutes les 15-20 minutes :
- Une question ouverte à l'audience
- Un mini-exercice (3-5 min)
- Un retour collectif sur une expérience vécue
- Un changement de format (vidéo, schéma au tableau, démo, débat)

Si on n'a pas le temps pour un vrai exercice, une simple question ouverte à laquelle on attend une réponse de la salle suffit à relancer l'attention.

**Application pratique** : pour un module de 1h, prévoir au minimum 3 moments d'interaction avec la salle.

## 3. La pyramide de Bloom

Hiérarchie des niveaux cognitifs visés par chaque activité (slide, exercice, question de quiz) :

| Niveau | Verbe d'action | Exemple |
|---|---|---|
| 1. Mémoriser | Restituer | « Citez les 3 types de modèles de fondation » |
| 2. Comprendre | Reformuler, expliquer | « Expliquez la différence entre fine-tuning et RAG avec vos mots » |
| 3. Appliquer | Utiliser | « Écrivez un prompt pour cette tâche » |
| 4. Analyser | Décomposer, comparer | « Comparez 3 approches et choisissez avec justification » |
| 5. Évaluer | Juger, critiquer | « Évaluez si ce système doit passer en production » |
| 6. Créer | Produire du neuf | « Concevez votre propre architecture pour ce besoin » |

Le niveau visé doit être **cohérent avec le niveau de la formation** :

- **Niveau 100** (introduction) : objectifs maxi = Comprendre / Appliquer
- **Niveau 200** (intermédiaire) : objectifs maxi = Analyser / Évaluer
- **Niveau 300** (expert) : objectifs maxi = Créer

**Anti-pattern** : une formation niveau 100 dont les exercices demandent « concevez votre architecture » → mal calibrée, frustrante.

## 4. Espacement & retrieval practice

Mieux retenir = réactiver. Pour chaque module :

- **Ouverture** : 1 slide rappelant le lien avec le module précédent
- **Fin de module** : recap explicite des 3-5 idées clés
- **Début de jour 2 (sur formation multi-jour)** : quiz court (3-5 questions) sur ce qu'on a fait la veille

L'effet d'espacement (revoir une notion à intervalles) est l'un des leviers d'apprentissage les plus robustes selon la littérature en sciences cognitives.

## 5. Erreur = matière première pédagogique

**Un exercice où personne ne se trompe est inutile.**

Designer les exercices pour qu'environ 30-50% des stagiaires commettent une erreur typique, et provoquer le debrief sur cette erreur. Les erreurs prévisibles vont dans `notes-formateur.md` (section "Pièges anticipés").

Lors du debrief :
- Ne pas pointer du doigt qui s'est trompé
- Demander à un stagiaire d'expliquer son raisonnement (même quand il a juste — ça aide les autres)
- Faire ressortir l'erreur typique comme un piège auquel "beaucoup tombent", pas comme une faute individuelle
- Connecter l'erreur à un concept de fond qu'il faut consolider

## 6. Adapter à l'hétérogénéité

Dans un groupe, 20% galèrent, 60% suivent, 20% trouvent ça facile.

Pour chaque exercice :
- **Indices gradués** pour les bloqués (cf. `exercise_design.md`)
- **Bonus / extension** pour les rapides (variante, optimisation, cas plus complexe)
- **Le formateur passe dans les rangs** et calibre — le slide d'énoncé reste affiché pendant ce temps

Le bonus pour les rapides ne doit pas être un cadeau empoisonné : pas un piège insoluble, mais une vraie ouverture sur la suite.

## 7. Métaphores et analogies

Un concept technique abstrait s'ancre dans la mémoire via une métaphore concrète.

Pour chaque concept central, identifier en amont 1-2 métaphores du quotidien (cuisine, transport, sport, organisation, bricolage) à utiliser dans la présentation.

**Exemples :**

- *Un index de base de données* = la table des matières d'un livre
- *L'embedding* = donner des coordonnées à un mot dans l'espace du sens
- *Le fine-tuning* = apprendre à un chef cuisinier formé sur la cuisine française à faire de l'asiatique, sans le réapprendre à cuisiner
- *Un transformer* = un lecteur qui peut regarder en arrière (et en avant) dans la phrase pour comprendre chaque mot
- *La température d'un LLM* = le bouton « j'ose dire ce que je pense » : à 0, le modèle est prudent et répétitif ; à 1, il prend des risques
- *Un vector store* = un classement d'archives par similarité de contenu, pas par ordre alphabétique

Les bonnes métaphores deviennent du vocabulaire partagé entre formateur et stagiaires, et permettent de débloquer rapidement les incompréhensions.

## 8. Cohérence du fil narratif

Une formation n'est pas une juxtaposition de modules — c'est un récit. Le stagiaire doit pouvoir, à tout moment, répondre à : « où en sommes-nous, et pourquoi cet enchaînement ? »

Concrètement :
- **Transitions explicites** entre modules : « on a vu X, on va maintenant voir Y, parce que Y répond au manque de X »
- **Rappel du fil** en ouverture de chaque demi-journée
- **Mapping visible** entre les exercices et les objectifs pédagogiques du plan
- **Synthèse finale** qui relie tous les modules et trace le fil global

Un stagiaire qui sort en disant « j'ai vu beaucoup de choses mais je ne vois pas comment ça s'articule » → fil narratif raté.

## 9. Calibrer la profondeur — règle du « moins mais mieux »

Tentation classique : vouloir tout dire. Résultat : on dit beaucoup, le stagiaire retient peu.

Règle pratique : pour chaque module, identifier les **3 idées-clés** qu'on veut que le stagiaire retienne dans 6 mois. Tout le reste est de la matière de support. Si une idée n'aide pas à comprendre une des 3 idées-clés, elle est en option ou supprimable.

Cette discipline force à arbitrer en amont, ce qui paye en clarté pédagogique.

## 10. Rendre le silence productif

Quand on pose une question à la salle, **laisser le silence durer 10 secondes au moins**. La tentation est de combler par soi-même, mais ce silence est le temps de pensée des stagiaires.

Si vraiment personne ne répond, reformuler ou donner un point d'entrée — pas la réponse directement. Exemple : « regardez ce qu'on a écrit au slide précédent, qu'est-ce qui pourrait coincer ? »

Cette discipline est difficile mais transformatrice — elle change le rythme de la formation et engage la salle.
