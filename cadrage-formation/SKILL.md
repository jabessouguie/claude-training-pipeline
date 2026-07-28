---
name: cadrage-formation
description: Prépare le cadrage d'une formation client de bout en bout et livre une grille de questions de cadrage dans un fichier Excel. Utiliser cette skill dès que l'utilisateur mentionne qu'il doit préparer, cadrer ou animer une formation pour un client, qu'il partage un compte rendu de réunion commerciale, une liste de participants, ou qu'il demande des "questions à poser au client", un "appel de cadrage", ou une analyse de son audience — même s'il ne demande pas explicitement un Excel. Le livrable final est toujours un fichier .xlsx de questions de cadrage priorisées.
---

# Cadrage de formation

Cette skill guide la préparation complète du cadrage d'une formation client :
lecture du contexte, recherche sur les participants, sur le client et sur le
sujet, puis production d'une **grille de questions de cadrage priorisées au
format Excel** (livrable final obligatoire).

## Workflow en 8 étapes (0 à 7)

### Étape 0 — Créer le dossier de la formation (convention de rangement)

Avant toute recherche, créer (ou identifier s'il existe déjà) le dossier de la formation selon la convention :

```
formations/<client>-<theme>/<AAAA-MM>/
```

- `<client>` : nom court du client en kebab-case (ex. `alpha`, `nova-industries`)
- `<theme>` : thème court de la formation en kebab-case (ex. `po-augmente`)
- `<AAAA-MM>` : année-mois de la session de formation (pas de la date de cadrage), ex. `2026-09`

Exemple : `formations/alpha-po-augmente/2026-09/`. Cette date distingue explicitement plusieurs sessions d'une même formation dans le temps (ex. `2026-07/` vs `2026-09/` pour deux sessions successives du même client) — ne jamais réutiliser un dossier d'une session passée pour une nouvelle session, même identique dans le contenu.

Si un dossier proche existe déjà pour ce client/thème (session précédente), le signaler à l'utilisateur avant de continuer, sans le réutiliser automatiquement (voir la question de l'étape 1 sur la réutilisation d'une formation antérieure).

Le fichier Excel produit à l'étape 6 est livré dans ce dossier.

### Étape 1 — Lire le contexte fourni et vérifier l'existence d'une formation antérieure proche

Avant de creuser le contexte, demander explicitement : **« Existe-t-il une formation antérieure proche de ce besoin ? »**

- Si l'utilisateur répond oui et fournit (ou a déjà fourni) l'accès à un répertoire de formations passées (ex. `formations/`, voir Étape 0), scanner ce répertoire et proposer **1 à 3 candidats** avec une justification courte : thématique, profils de participants, niveau. Présenter les candidats à l'utilisateur et **attendre sa validation explicite avant de réutiliser quoi que ce soit** — ne jamais s'appuyer automatiquement sur une formation passée, même si elle semble évidente (une audience différente en séniorité ou en fonction, ex. BO vs BA/UX, suffit à rendre un gabarit inadapté).
- Si l'utilisateur répond non, ou si aucun répertoire n'est fourni, poursuivre le cadrage from scratch sans bloquer.

Cette question précède la lecture détaillée du contexte : une formation antérieure validée peut réorienter ce qu'il est utile de chercher ensuite.

Lire ensuite attentivement tous les documents fournis (compte rendu de réunion,
e-mails, brief). En extraire et noter :
- Le client final et son groupe d'appartenance
- Le sujet et le public cible de la formation (ex. PO/PM, développeurs)
- Les dates (formation, appel de cadrage) et les personnes impliquées
- Les contraintes budgétaires et de périmètre (ex. tarif/jour, modules
  existants vs sur-mesure)
- Les points de vigilance exprimés (ex. hétérogénéité de l'audience)

Si une information clé manque (client, sujet, public), la demander à
l'utilisateur avant de continuer.

### Étape 2 — Lire la liste des participants
Lire le fichier de participants (CSV/Excel). Ne jamais inventer de noms.

### Étape 3 — Recherches étendues sur les participants

**Seuil de bascule (au-delà de 20 participants)** : si la liste de participants dépasse 20 personnes, ne pas effectuer de recherche nominative individuelle (trop coûteux en temps et en tokens, non représentatif à cette échelle — ex. masterclass). Basculer automatiquement, sans attendre que l'utilisateur le demande, vers une **analyse par profil type** : identifier les grandes catégories de profils présentes (à partir des rôles/entités disponibles dans le fichier participants), estimer le niveau d'hétérogénéité du groupe, et le signaler explicitement à l'utilisateur :

```
La liste comporte <N> participants (seuil de recherche nominative : 20).
Je bascule sur une analyse par profil type plutôt qu'une recherche individuelle par participant.
```

En dessous de ce seuil, effectuer la recherche nominative complète ci-dessous, inchangée.

Pour chaque participant, rechercher sur le web (LinkedIn, theorg.com, presse,
posts d'entreprise) : poste actuel, rôle (PO, PM, manager, support, direction),
séniorité, background technique ou fonctionnel, entité exacte.

Règles strictes :
- **Signaler clairement les profils introuvables ou ambigus (homonymes)
  plutôt que d'inventer.** Marquer ces profils « À confirmer ».
- Synthétiser l'**hétérogénéité du groupe** (séniorité, technique vs
  fonctionnel, décideurs vs praticiens) : c'est le principal risque
  pédagogique à cadrer.

### Étape 4 — Recherches étendues sur le client
Rechercher : activité, taille, appartenance à un groupe, organisation
digitale/DSI, maturité sur le sujet de la formation (initiatives récentes,
outils déployés, programmes internes existants), culture produit/agile,
actualités récentes (2 dernières années). Identifier les outils autorisés en
interne si l'information est publique.

### Étape 5 — Recherches étendues sur le sujet de la formation
Rechercher l'état de l'art récent : cas d'usage typiques pour ce public, pain
points connus (maturité variable, confidentialité, résistance au changement,
outillage), bonnes pratiques pédagogiques, outils pertinents. Croiser avec le
contexte du client (étape 4) pour contextualiser.

### Étape 6 — Produire la grille de questions en Excel (obligatoire)
Construire des questions de cadrage organisées par thème, en couvrant au
minimum ces 7 thèmes (adapter les intitulés au contexte) :
1. Objectifs & attentes du sponsor
2. Profils & hétérogénéité des participants
3. Outillage & contraintes IT/sécurité
4. Cas d'usage métier prioritaires
5. Format & logistique
6. Budget & périmètre
7. Critères de succès & suivi

Chaque question a une priorité : **INDISPENSABLE** ou **OPTIONNEL**.
Ajouter pour chaque question une courte justification ("Pourquoi") issue des
recherches (ex. « ce profil semble appartenir à une autre entité — à
confirmer »).

Puis générer le fichier Excel :

1. Écrire les données dans un JSON (voir format ci-dessous)
2. Exécuter le script fourni, en écrivant le fichier dans le dossier de la formation créé à l'Étape 0 :
   ```bash
   python scripts/generate_cadrage_xlsx.py input.json formations/<client>-<theme>/<AAAA-MM>/cadrage_<client>.xlsx
   ```
3. Présenter le fichier à l'utilisateur avec `present_files`, accompagné
   d'une courte synthèse des points de vigilance majeurs (3-5 lignes max).

#### Format du JSON d'entrée

```json
{
  "titre": "Cadrage formation PO/PM augmentés — Client Alpha",
  "client": "Alpha Digital Solutions",
  "date_cadrage": "2026-07-06 14:30",
  "formation": "PO/PM augmentés par l'IA générative",
  "date_formation": "2026-09-08",
  "contexte": ["Ligne de contexte 1", "Ligne 2"],
  "points_vigilance": ["Point 1", "Point 2"],
  "participants": [
    {"nom": "DUPONT", "prenom": "Marie", "role": "Architecte Mobilité (?)",
     "entite": "Entité IT partenaire (?)", "profil": "À confirmer",
     "statut": "À confirmer"}
  ],
  "questions": [
    {"theme": "A. Objectifs & attentes du sponsor",
     "question": "Quel est l'objectif métier prioritaire ?",
     "priorite": "INDISPENSABLE",
     "pourquoi": "Oriente tout le contenu"}
  ]
}
```

Les clés `participants`, `contexte` et `points_vigilance` sont optionnelles
mais fortement recommandées : le script génère alors des onglets dédiés.

#### Ce que produit le script
Un classeur .xlsx professionnel avec :
- Onglet **Questions de cadrage** : Thème / Question / Priorité / Pourquoi /
  Réponse client (vide) / Statut (liste déroulante), avec filtres, volets
  figés, priorités en couleur — prêt à remplir pendant l'appel de cadrage
- Onglet **Participants** (si fourni)
- Onglet **Contexte** (si fourni) : synthèse + points de vigilance

Le script ne contient aucune formule, donc pas de recalcul nécessaire.

### Étape 7 — Proposer la prochaine étape

Une fois le fichier Excel livré, proposer explicitement à l'utilisateur la suite, sans attendre qu'il la demande :

```
La grille de cadrage est prête dans <chemin du .xlsx>.

Prochaine étape possible :
- Une fois les réponses du client obtenues, je peux les intégrer et lancer `formation-material-builder`
  pour produire le matériel pédagogique (plan puis contenu module par module).
- Si tu veux d'abord ajuster la grille ou revoir un point de vigilance, dis-le-moi.

Que veux-tu faire ?
```

Adapter le message à ce qui a réellement été produit (mentionner explicitement le fichier livré et son chemin) plutôt que d'utiliser un texte générique.

## Règles générales
- Toujours répondre et livrer en français, sauf demande contraire.
- Ne jamais présenter une hypothèse de recherche comme un fait : utiliser
  « probable », « à confirmer » et prévoir la question de vérification
  correspondante dans la grille.
- Le fichier Excel est le livrable final : ne pas se contenter d'une liste de
  questions dans la conversation.
