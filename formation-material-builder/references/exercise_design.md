# Conception des exercices

## Principe : un exercice doit faire faire, pas faire écouter

Si l'apprenant peut résoudre l'exercice en regardant ses notes, ce n'est pas un exercice — c'est un récap. Un bon exercice **exige un transfert** : appliquer ce qu'on vient de voir à un cas légèrement différent.

## Cas fil rouge (standard par défaut)

Par défaut, les exercices d'une formation s'ancrent dans un **cas fil rouge unique** — voir `fil_rouge_design.md` pour la conception du cas et la structure de sortie (`livrables/atelier-N/` + `livrables/solutions/`). Les principes ci-dessous (structure d'un exercice, calibration, pyramide de Bloom) s'appliquent identiquement, que l'exercice soit un atelier fil rouge ou un exercice classique — seul le contexte change : au lieu d'un cas isolé par exercice, le **Contexte** de chaque atelier rappelle où en est le cas fil rouge et comment cet atelier le fait progresser.

## Structure standard d'un exercice

Pour chaque atelier (dans `enonce-atelier-N.md`, voir `fil_rouge_design.md`) ou exercice classique (dans `exercices.md`, voir « Sans cas fil rouge » plus bas) :

### Métadonnées en en-tête

- **Titre** — court, descriptif, sans jargon
- **Durée estimée** — temps réel passé par un stagiaire moyen (pas un stagiaire idéal)
- **Niveau** — débutant / intermédiaire / avancé, relatif au niveau global de la formation
- **Prérequis** — notions à maîtriser AVANT d'aborder l'exercice (slides X à Y, ou concept Z)
- **Format** — individuel / binôme / groupe / live coding suivi

### Énoncé

- **Contexte** (2-3 phrases) — situe le cas, donne du sens, ancre dans le métier. Avec un cas fil rouge : rappeler où en est le cas (ce que l'atelier précédent a produit) et ce que cet atelier lui fait faire progresser.
- **Objectif** — ce qu'on apprend (pas ce qu'on fait — on fait pour apprendre)
- **Consigne** — ce qu'il faut faire, en étapes claires et numérotées
- **Critères de réussite** — comment le stagiaire sait qu'il a terminé sans appeler le formateur

### Indices (optionnels mais recommandés)

3 niveaux d'indices, du plus subtil au plus explicite :
1. **Indice 1** — oriente sans révéler (« avez-vous regardé comment la fonction X gère le cas Y ? »)
2. **Indice 2** — donne une direction concrète (« utilisez `groupby` sur la colonne Z »)
3. **Indice 3** — quasi la solution (« la formule est `df.groupby('Z').agg({'X': 'mean'})` »)

Le formateur donne ces indices à la demande, gradués. Évite de spoiler tout le monde en donnant directement la solution.

## Calibrer la difficulté

**Cible** : 30-50% des stagiaires commettent une erreur typique en chemin. Pas zéro (exercice trop facile, n'apprend rien) ni 80% (frustration). Cette zone d'erreur productive est le **deuxième moment pédagogique** de l'exercice — celui du debrief.

Indicateurs concrets de difficulté bien calibrée :
- Au moins un stagiaire a une question pertinente pendant l'exercice
- Au moins un stagiaire produit un résultat différent et défendable
- Personne ne finit en 5 min si l'exercice est annoncé pour 20 min
- Personne ne plante complètement faute de pouvoir avancer

## Progression dans un module : la pyramide de Bloom

Un module bien construit suit cette progression :

1. **Rappel / Compréhension** — premier exercice : « applique la formule qu'on vient de voir »
2. **Application** — deuxième exercice : « résous ce cas légèrement différent du cours »
3. **Analyse** — troisième exercice : « compare deux approches et choisis-en une avec justification »
4. **Synthèse / Création** — exercice final : « conçois ta solution pour ce problème »

Tous les modules n'ont pas besoin d'aller jusqu'à la synthèse :
- **Niveau 100** (introduction) : objectifs maxi = Application
- **Niveau 200** (intermédiaire) : objectifs maxi = Analyse / Évaluation
- **Niveau 300** (expert) : objectifs maxi = Création

Si un exercice d'une formation 100 demande de « concevoir une architecture » — il est mal calibré.

## Pièges à éviter

| Piège | Symptôme | Antidote |
|---|---|---|
| Exercice trop ouvert | « Faites un projet GenAI complet en 30 min » | Borner le scope, donner un squelette de départ |
| Exercice trop guidé | « Tapez exactement ceci puis ceci » | Demander un choix, un raisonnement, un comparatif |
| Exercice hors périmètre | Utilise des concepts non couverts par les slides | Mapper chaque concept de l'exercice à un slide du module |
| Exercice non testé | Le formateur découvre les bugs en TP | Re-faire l'exercice soi-même la veille, à froid |
| Exercice trop long | 30 min sans avancer → décrochage | 2 exercices de 15 min > 1 exercice de 30 min |
| Exercice "moi je sais" | Le rapide finit en 5 min et s'ennuie | Prévoir un bonus / extension |

## Format des solutions

Les solutions sont pour le **formateur**, pas pour les stagiaires (sauf décision contraire du client). Elles sont incluses dans le guide-formateur.docx mais **pas** dans le livret-stagiaire.docx. Avec un cas fil rouge, chaque solution vit dans `livrables/solutions/solution-atelier-N.md` (voir `fil_rouge_design.md` pour la règle de distribution après-debrief) ; sans cas fil rouge, dans `solutions.md`.

Format par solution :

### Approche pédagogique
Comment aborder le problème, pas juste le résoudre. Quel raisonnement on espère voir naître chez le stagiaire. Quels concepts du module sont mobilisés.

### Solution complète
Le code / résultat / réponse fonctionnel et commenté. Code = commenté, pas brut.

### Variantes
1-2 autres façons de résoudre le problème, avec pour chacune :
- Pourquoi cette variante est légitime
- Quand on préfère cette variante à la solution principale
- Quels concepts différents elle mobilise

Permet au formateur de réagir intelligemment si un stagiaire produit une variante non prévue.

### Pièges fréquents
Erreurs récurrentes vues lors de TP précédents, et comment les diagnostiquer rapidement.

Exemple : 
> *« Le stagiaire oublie souvent que `groupby` ne renvoie pas un DataFrame mais un GroupBy object. Signe : il a une erreur "AttributeError: 'GroupBy' object has no attribute X". Solution : lui montrer qu'il faut chaîner avec `.agg()` ou `.mean()`. »*

### Pour aller plus loin
1 question de réflexion ou 1 amélioration possible, pour les stagiaires rapides ou pour le debrief collectif.

## Format pratique

Les exercices techniques (code, manipulation d'outils) devraient idéalement venir avec :
- Un notebook de départ (squelette pré-rempli avec les imports et la cellule "votre code ici")
- Un notebook solution
- Les données nécessaires dans un dossier `assets/exercices/M<n>/`, **un fichier par élément, au format réel du métier** (même principe que le corpus d'un cas fil rouge — voir `fil_rouge_design.md` § « Un fichier par élément de corpus, au format réel du métier » : un export tabulaire réel devient `.xlsx` s'il le serait chez le client, pas systématiquement du CSV/JSON générique)

Ces fichiers complémentaires doivent être listés dans `exercices.md` avec un lien relatif. Le script de compilation du livret peut les référencer (URL ou QR code vers le repo).

Pour les formations distancielles ou hybrides, prévoir un repo Git (ou un Drive partagé) qui centralise ces fichiers. Le lien va dans `prerequis-setup.md`.

## Sans cas fil rouge (mode alternatif, sur demande explicite)

Si le consultant demande explicitement de ne pas utiliser de cas fil rouge, revenir au format antérieur : un `exercices.md` par module, contenant tous les exercices du module à la suite (format ci-dessus, sans dossier dédié par exercice), et un `solutions.md` correspondant dans le même dossier de module. Chaque exercice est alors indépendant — le **Contexte** ancre dans le métier du client sans référence à un cas qui progresse d'un exercice à l'autre. Pas de conversion HTML/PDF dans ce mode (les exercices restent dans le livret stagiaire compilé, comme avant).
