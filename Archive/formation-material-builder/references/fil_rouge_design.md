# Concevoir un cas fil rouge

## Principe : un seul cas fictif, filé sur toute la formation

Au lieu d'exercices isolés module par module, la formation s'appuie sur **un unique produit/contexte fictif** qui traverse tous les ateliers. Le stagiaire endosse un rôle vis-à-vis de ce cas (souvent : le professionnel missionné dessus) et le fait progresser atelier après atelier — l'atelier 2 reprend l'état laissé par l'atelier 1, etc.

**Référence** : le cas `StockPilot` (gestion de petit matériel réutilisable dans une chaîne de magasins de proximité, formation « Product Management augmenté ») illustre ce standard — voir `fil-rouge-stockpilot/` s'il est disponible dans le workspace ou le dépôt. **Ce gabarit est antérieur à l'extension du 28/07/2026 sur le format réaliste du corpus** (son `interviews.md` regroupe plusieurs interviews dans un seul fichier générique) — le reprendre pour la conception narrative du cas et la conversion HTML des énoncés (voir plus bas), mais **ne pas reproduire sa structure de corpus telle quelle** : appliquer la règle « un fichier par élément, format réel du métier » ci-dessous plutôt que ce qui est fait dans ce gabarit.

## Pourquoi un cas fil rouge plutôt que des exercices isolés

- **Économie cognitive** : le stagiaire connaît déjà le contexte dès l'atelier 2 — l'énergie va dans l'exercice, pas dans la compréhension d'un nouveau décor à chaque fois.
- **Continuité narrative** : le debrief d'un atelier prépare naturellement le suivant (« vous avez identifié ce pain point à l'atelier 1, voyons comment le prioriser à l'atelier 2 »).
- **Immersion** : un cas cohérent avec le domaine du client (même secteur, mêmes contraintes métier) rend l'exercice plus crédible qu'un cas générique.
- **Mesure de progression** : le formateur peut évaluer objectivement si le stagiaire a progressé sur UN cas, plutôt que sur N cas déconnectés.

## Concevoir le cas fil rouge (en Phase 1, avec la roadmap)

Le cas fil rouge se conçoit **en même temps que la roadmap de production**, avant de rédiger le premier atelier — il doit être fixé avant que les ateliers ne s'y ancrent.

### Ce que le cas doit fixer

1. **Un produit/contexte fictif**, cohérent avec le domaine du client (ex. client dans le BTP → produit de gestion de chantier ; client en assurance → produit de gestion de sinistres). Nommer le produit (ex. « StockPilot ») — un nom facilite les références dans les slides, les ateliers, les debriefs.
2. **Un rôle stagiaire** clair et constant (ex. « vous êtes le PO missionné sur ce produit »).
3. **Un fil narratif entre ateliers** : ce qui progresse d'un atelier à l'autre (ex. Atelier 1 = découverte/discovery → Atelier 2 = definition/specs → Atelier 3 = prototype → Atelier 4 = lancement). Chaque atelier consomme la production de l'atelier précédent.
4. **Des données fictives mais crédibles** par atelier qui en a besoin (voir plus bas) : interviews, tickets, statistiques, métriques — toujours inventées, jamais des données réelles du client.
5. **Une clause de non-réalité explicite** : rappeler dans chaque README de corpus que toutes les données sont inventées à des fins pédagogiques, sans lien avec un système ou produit réel du client — **cette clause s'applique même quand le format d'un élément est réaliste** (un e-mail qui a l'apparence d'un vrai e-mail, un export `.xlsx` qui ressemble à un vrai export) : le réalisme porte sur la FORME, jamais sur le fond, qui reste entièrement fictif.

### Présentation au consultant

Présenter le cas fil rouge conçu (nom du produit, rôle stagiaire, fil narratif entre ateliers) et **valider explicitement avant de produire les données/corpus** — au même titre que la roadmap de production. Un cas fil rouge mal calibré (trop éloigné du métier réel du client, ou trop proche au point de sembler réel) est coûteux à corriger une fois les 4 ateliers rédigés.

## Structure de sortie par atelier

Chaque atelier vit dans un dossier dédié, à la racine de `livrables/` :

```
livrables/
├── atelier-1/
│   ├── enonce-atelier-1.md       # rédigé d'abord (contenu, structure)
│   ├── enonce-atelier-1.html     # converti ensuite (charte par défaut, voir plus bas)
│   ├── enonce-atelier-1.pdf      # exporté depuis le HTML (impression/distribution)
│   └── <corpus dédié si nécessaire, un fichier par élément au format réel du métier :
│        email-reclamation-client.md, ticket-support-042.md, export-tickets-atelier-1.xlsx, ...>
├── atelier-2/
│   └── ...
├── atelier-N/
│   └── ...
└── solutions/
    ├── solution-atelier-1.md
    ├── solution-atelier-2.md
    ├── ...
    └── README.md                 # rappelle la règle de non-distribution en amont
```

**Un atelier n'a pas toujours besoin de corpus dédié** (ex. un atelier qui part du canevas produit de l'atelier précédent, sans nouvelles données à ingérer) — ne pas forcer un corpus artificiel si l'atelier n'en a pas l'usage.

### Un fichier par élément de corpus, au format réel du métier

Chaque élément du corpus (un e-mail, une interview, un ticket, un extrait de tableur, une capture d'écran…) vit dans **son propre fichier**, séparé des autres éléments. Deux raisons à séparer :

- Chaque fichier reste court : réduit le risque de troncature au collage dans un chat.
- Séparer qualitatif (interviews, verbatims) et quantitatif (tickets, statistiques) permet des exercices en plusieurs passes (analyse séparée puis triangulation) — un bonus pédagogique naturel.

**Le format de chaque fichier est celui que le stagiaire trouverait réellement dans son métier** — pas un format uniformisé pour la facilité de traitement. Le réalisme du format prime sur la commodité d'exploitation : un stagiaire s'entraîne à travailler avec les pièces telles qu'il les rencontrera en poste, pas avec des données pré-nettoyées pour un outil d'analyse. Concrètement :

| Élément de corpus | Format réel du métier | Ne PAS faire |
|---|---|---|
| E-mail (réclamation, demande, échange) | `.md` mis en forme comme un e-mail (`De:`, `À:`, `Objet:`, `Date:` en en-tête, corps en dessous) — ou `.eml` si l'atelier demande d'ouvrir un vrai client mail | Fondre l'e-mail dans un fichier `interviews.md` générique |
| Interview / verbatim stagiaire | `.md` transcript brut, avec disfluences et hésitations si le réalisme du debrief en dépend | Résumer ou lisser le verbatim |
| Ticket support / Jira / réclamation client | `.md` mis en forme comme un export de ticket (ID, statut, priorité, description, historique) | Le noyer dans une liste markdown de puces |
| Export de données tabulaires — si le vrai outil du client exporte du CSV | `.csv` | — (le CSV est légitime ici : c'est le format réel) |
| Export de données tabulaires — si le vrai outil du client exporte un tableur | `.xlsx` (voir méthode de production ci-dessous) | Convertir en CSV « pour que ce soit plus simple à traiter » |
| Document de référence interne (procédure, guide, brief) | `.docx` s'il circulerait en Word chez le client, sinon `.md` | Toujours choisir `.md` par défaut sans se poser la question du format réel |
| Capture d'écran d'un outil (dashboard, extranet, appli) | Image (`.png`) — voir méthode de production | Décrire la capture en texte au lieu de la produire |

Si le vrai format du métier client **est** un `.md`/`.txt`/`.csv` brut (ex. un export CLI, un log), le garder tel quel — la règle n'impose pas de complexifier un format qui serait de toute façon simple dans la réalité. La question à se poser pour chaque élément : *« si ce stagiaire recevait vraiment cette pièce demain matin, sous quelle forme l'aurait-il ? »*, pas *« quel format est le plus simple à générer ou à faire lire par l'IA ? »*.

### Produire les éléments en format réaliste (méthode : markdown source → conversion binaire)

Même méthode que la conversion HTML des énoncés d'atelier (voir plus bas) : **rédiger d'abord en markdown, valider le contenu, puis convertir** vers le binaire réel si le format cible n'est pas du texte brut.

1. **Rédiger le contenu en `.md`** dans `livrables/atelier-N/`, même si la cible finale est un binaire — permet de réviser et valider le contenu facilement avant conversion (ex. `email-reclamation-client.md`, `export-tickets-support.md`).
2. **Convertir selon le format cible** une fois le contenu validé :
   - `.xlsx` → même méthode que `cadrage-formation` (script Python + `openpyxl`), ou la skill `xlsx` si disponible dans l'environnement.
   - `.docx` → skill `docx` publique, même mécanisme que `livret-stagiaire.docx`/`guide-formateur.docx`.
   - `.png` (capture d'écran simulée) → composer un visuel simple représentant l'interface décrite (peut passer par le même canal que les illustrations de `slide-content-claude-design` si la fidélité visuelle importe, ou par un rendu HTML→image pour un mockup d'écran).
   - `.eml` → gabarit texte au format e-mail brut (en-têtes `From`/`To`/`Subject`/`Date` conformes RFC 822 minimal), pas de conversion outillée nécessaire.
3. **Nommer chaque fichier explicitement** par son contenu et son type (`email-reclamation-client.md`, `export-tickets-atelier-2.xlsx`), pas par un nom générique (`corpus.md`, `data.csv`) — le nom doit permettre au stagiaire de savoir ce qu'il ouvre avant de l'ouvrir, comme dans la vraie vie.

### Solutions séparées, distribution disciplinée

Le dossier `solutions/` contient un fichier par atelier, format identique à `solutions.md` (voir `exercise_design.md`) : approche pédagogique, solution complète, variantes, pièges fréquents, pour aller plus loin.

**Règle de distribution, à documenter dans `solutions/README.md`** : ne jamais transmettre une solution avant le debrief de l'atelier correspondant — jamais en amont, jamais en bloc avec le reste du fil rouge, même sur un espace partagé en accès libre. Consulter une solution avant l'atelier vide l'exercice de sa valeur pédagogique, en particulier pour un atelier de découverte où l'objectif est justement de laisser le stagiaire chercher.

## Conversion HTML avec la charte par défaut

Une fois `enonce-atelier-N.md` rédigé et validé (contenu : contexte, objectif, consigne, critères de réussite, indices, bonus — voir `exercise_design.md`), le convertir en `enonce-atelier-N.html` avec le gabarit de charte ci-dessous.

### Gabarit de page (à reprendre tel quel, adapter le contenu)

Structure HTML avec CSS inline (`<style>` en tête de fichier), format A4 portrait imprimable :

- **Polices** : Sora (titres) + Inter (corps), importées via Google Fonts.
- **Bandeau d'en-tête** pleine largeur, fond bleu marine `#2C5F8A`, texte blanc : eyebrow (module/contexte, petites majuscules), titre H1 (Sora bold), sous-titre.
- **Grille de métadonnées** (2 colonnes) : tuiles fond beige `#E8E2DA`, coins arrondis 4px — Durée, Niveau, Format, Prérequis, Matériel (celle-ci en pleine largeur).
- **Sections** : titre H2 Sora avec soulignement bleu marine (`border-bottom: 2px solid #2C5F8A`).
- **Consigne numérotée** : puces rondes bleu marine avec numéro blanc à l'intérieur, pas de puces classiques.
- **Critères de réussite** : coche bleu marine (`✓`) avant chaque item.
- **Encadré Indices** : fond gris clair `#F7F7F7`, bordure pointillée grise, à consulter seulement si bloqué — ton discret.
- **Encadré Bonus** : bordure gauche bleu marine épaisse (4px), fond beige, pour les stagiaires rapides.
- **Pied de page** : nom formation à gauche, référence atelier/module à droite, séparateur fin beige au-dessus.

Voir `fil-rouge-stockpilot/atelier-1/enonce-atelier-1.html` comme gabarit de référence complet pour **cette conversion HTML uniquement** (CSS entier réutilisable presque tel quel, ne changer que le contenu) — cela ne concerne pas la structure de son corpus, voir la mise en garde en tête de ce document.

### Export PDF

Générer le PDF depuis le HTML (impression navigateur en PDF, ou outil de conversion HTML→PDF disponible). Le PDF est le format de distribution final aux stagiaires (imprimable, table des métadonnées lisible sans exécuter de JS).

## Rôle du fil rouge dans les slides et illustrations

Le cas fil rouge, une fois conçu, devient aussi la **métaphore filée** que `slide-content-claude-design` décline en bloc « Direction artistique » par module (voir son `SKILL.md`) — cohérence narrative de bout en bout, du contenu théorique jusqu'aux illustrations générées.
