# Conception du quiz d'évaluation

Le quiz final sert deux usages : **valider l'acquisition** des objectifs pédagogiques, et **donner au stagiaire un sentiment de progression** mesurable. Ce n'est pas un examen, c'est un outil pédagogique.

## Format général

Le quiz final est produit au **format Kahoot** (animation live en salle) : une fiche structurée par question, pas un QCM narratif. Voir `SKILL.md` §4.1 pour le format de sortie exact.

- **15 à 25 questions** au total
- **Mix de types** : majorité de `quizz` (QCM), quelques `vrai/faux` pour les notions tranchées, `réponse libre` pour ce qui validait la compréhension (à défaut de correction manuelle en direct, formuler la question pour qu'une réponse courte et précise suffise), `curseur` pour une estimation chiffrée, `puzzle` pour un ordre d'étapes, `réponse par pins` seulement si un visuel s'y prête vraiment
- **Couverture proportionnelle** : un module de 1/2 journée → 25-30% des questions ; un module d'1h → 10-15%
- **Temps imparti par question** : calibré à la difficulté, pas uniforme — rappel direct 10-20s, application/cas 45-90s, transfert ou réponse libre jusqu'à 2-4 min. Total de passation visé : 20-30 min pour rester dans l'attention.
- **Points** : `standard` par défaut ; `double` pour les questions de transfert (le plus de valeur pédagogique) ; `aucun` réservé aux questions de sondage/discussion qui ne valident pas un objectif (rare, à utiliser avec parcimonie).
- **Limite de réponse** : `une seule` par défaut ; `plusieurs possibles` seulement pour des questions explicitement à choix multiples (le formuler alors clairement dans l'énoncé : « cochez toutes les réponses correctes »).

## Calibrer la difficulté

Cible de réussite moyenne : **70-80%**.

- En dessous de 70% : quiz mal calibré (questions piège, sujet pas couvert) ou formation mal calibrée
- Au dessus de 90% : quiz trop facile, ne mesure rien

Mix idéal de difficulté :
- **30% questions de rappel direct** — un point clé d'un module
- **50% questions d'application** — cas concret mobilisant plusieurs notions
- **20% questions de transfert** — cas légèrement nouveau, non vu en formation

## Bonnes pratiques QCM

### Distracteurs (mauvaises réponses)

Les distracteurs doivent être **plausibles**. Une mauvaise réponse "évidemment fausse" ne teste rien.

Un bon distracteur correspond à une **erreur typique** que le formateur a vu lors de précédentes formations.

Trois distracteurs + 1 bonne réponse = 4 options par QCM. 2 ou 3 options suffisent pour les questions très tranchées.

### Formulation des questions

- **Énoncé ≤ 120 caractères** — limite de saisie de Kahoot : un énoncé plus long sera tronqué ou refusé lors du paramétrage manuel. Reformuler plutôt que couper.
- **Pas de double négation** : « Lequel n'est PAS une raison de NE PAS utiliser X » → trop confus
- **Pas de "toutes les réponses ci-dessus" ni "aucune"** en option (loophole pédagogique qui vide la question)
- **Questions affirmatives** plutôt que négatives quand possible (« Quel est… » > « Quel n'est pas… »)
- **Une seule bonne réponse claire**, sauf si c'est explicitement un QCM à choix multiples
- **Pas de questions piège** sur des subtilités hors objectifs pédagogiques

### Variantes utiles (types Kahoot)

- **Vrai/Faux** — utile pour valider des notions précises (1-2 dans le quiz suffisent)
- **Quizz à choix multiples** — préciser « limite de réponse : plusieurs possibles » et le dire dans l'énoncé quand pertinent
- **Réponse libre** — remplace les anciennes questions ouvertes ; formuler pour qu'une réponse courte (un mot, un chiffre, une expression) suffise, et lister toutes les variantes orthographiques/formulations acceptées dans « Bonne réponse »
- **Curseur** — pour une estimation chiffrée (un pourcentage, une durée, un ordre de grandeur) ; préciser la plage tolérée
- **Puzzle** — pour remettre dans l'ordre les étapes d'un processus vu en formation
- **Réponse par pins** — pour pointer une zone sur un schéma/screenshot projeté ; n'y recourir que si un visuel du support s'y prête vraiment, pas par défaut

## Questions à réponse libre (ex-questions ouvertes)

Pour les niveaux 200/300, garder 3-5 questions qui valident la compréhension réelle plutôt que la mémorisation — mais les reformuler en `réponse libre` Kahoot (pas de correction manuelle différée en direct) :
- « En un mot : qu'est-ce qui distingue X de Y ? »
- « Citez UNE erreur à éviter en faisant Z » (plutôt que « décrivez... en 2-3 phrases »)
- Si la question appelle vraiment une réponse longue et nuancée (analyse, justification), la reformuler en `quizz` à distracteurs plausibles construits sur les erreurs typiques, ou l'assumer en discussion orale post-Kahoot (`points: aucun`) plutôt qu'en `réponse libre` qui serait mal corrigée par l'auto-matching.

Dans la grille de correction, prévoir pour ces questions les **réponses acceptées** (toutes les formulations valides) plutôt qu'une réponse-modèle unique.

## Format du fichier `quiz-kahoot.md`

Voir le gabarit de fiche par question dans `SKILL.md` §4.1. Structure du fichier complet :

1. **En-tête** — titre de la formation, nombre de questions, durée de passation totale estimée, note pédagogique (« ce quiz n'a pas de note officielle au-delà du jeu, il sert à mesurer la progression »)
2. **Les N fiches de question**, dans l'ordre de passation (généralement l'ordre des modules)
3. **Grille de correction récapitulative** — tableau question → bonne réponse → explication courte (1-3 phrases, utile au debrief) → référence module/slide → points
4. **Récap notation** (repère informel puisque Kahoot note déjà en direct) :
   - **> 80%** : excellent — objectifs atteints
   - **60-80%** : acquis — quelques notions à revoir, identifiées dans le quiz
   - **< 60%** : à revoir — débrief individuel recommandé avec le formateur

Le fichier est un seul markdown (pas de .docx à splitter) : les questions/réponses sont de toute façon saisies dans l'outil Kahoot par le formateur, qui ne les projette jamais en clair aux stagiaires avant le jeu — la question de la fuite du corrigé ne se pose donc pas comme pour un questionnaire papier.

## Stratégie de répartition par module

Construire le quiz en respectant la couverture :

| Module | Durée | % du quiz | Nb questions (sur 20) |
|---|---|---|---|
| M1 | 2h | 15% | 3 |
| M2 | 4h | 30% | 6 |
| M3 | 3h | 22% | 4-5 |
| M4 | 4h | 30% | 6 |
| Transverse | — | 3% | 1 |

Pour chaque module, choisir les questions qui valident les **objectifs pédagogiques explicites** du plan (« à la fin de cette formation, le participant sera capable de… »). Si un objectif n'est testé par aucune question → quiz incomplet, ajouter.

## Exemples de questions par niveau Bloom

### Niveau Mémorisation
> **Question 3** — Parmi les modèles suivants, lequel a été développé par Anthropic ?
> 
> a) GPT-4
> b) Claude 3
> c) Gemini
> d) LLaMA

### Niveau Compréhension
> **Question 7** — En un mot : qu'est-ce que le RAG ajoute au modèle, que le fine-tuning ne modifie pas ?
>
> *(type `réponse libre` — réponses acceptées : « contexte », « documents », « connaissances externes »)*

### Niveau Application
> **Question 12** — Un chatbot interne répond mal sur la politique RH publiée il y a 3 mois. Quelle approche en priorité ?
> 
> a) Fine-tuner le modèle sur les documents RH
> b) Ajouter un système RAG sur les documents RH
> c) Réentraîner le modèle from scratch
> d) Changer de modèle de fondation

### Niveau Analyse
> **Question 18** — API cloud (OpenAI, Anthropic) vs modèle self-hosted (Mistral, LLaMA) : lequel gagne sur la confidentialité ?
>
> *(type `quizz` à 2 options ; la comparaison complète coût/latence/confidentialité se traite en discussion orale post-Kahoot — si on tient à la poser dans Kahoot, l'étiqueter `points : aucun` comme question de sondage/débat)*

## Pièges à éviter

- **Le quiz qui ne teste que la mémorisation** — Le stagiaire qui a bien dormi gagne, celui qui a compris perd. Mauvais signal.
- **Le quiz qui surpondère un module accessoire** — vérifier la répartition AVANT de finaliser.
- **Le quiz sans questions de transfert** — manque la dimension la plus importante de l'évaluation : est-ce que le stagiaire peut appliquer demain ?
- **Le quiz noté de façon trop "scolaire"** — sentiment d'examen, stress, contre-productif. Insister sur la dimension « auto-diagnostic ».
- **Le quiz trop long** — au-delà de 30-40 min, la fatigue prend le pas sur la réflexion.
