---
name: design-system-extractor
description: Extrait un design system client (couleurs, typographie, motifs de composants, ton) à partir de n'importe quel document fourni par l'utilisateur — captures d'écran, PDF de charte graphique, export Figma, page web, logo seul, etc. — jamais un format d'entrée imposé. Produit un dossier de référence réutilisable design-systems/<client>/, au même format que la section "Design system par défaut" de slide-content-claude-design/SKILL.md, pour que ce dernier puisse l'appliquer directement à la place de sa palette par défaut. Déclencher quand l'utilisateur demande d'"extraire la charte graphique du client", de "récupérer le design system à partir de ces captures/ce PDF/ce site", de "styliser les slides selon l'identité visuelle du client", ou fournit un ou plusieurs documents de marque sans plus de précision sur ce qu'il veut en faire.
---

# Extraction de design system client

Cette skill lit un ou plusieurs documents fournis par l'utilisateur (jamais devinés ni recherchés par elle-même) et en extrait un design system structuré — couleurs, typographie, motifs de composants récurrents, ton général — au même niveau de détail que la section "Design system par défaut — Encre & Sauge" de [`slide-content-claude-design/SKILL.md`](../slide-content-claude-design/SKILL.md), pour qu'il puisse s'y substituer directement.

**Principe directeur, non négociable** : cette skill ne décrit **que ce qu'elle observe réellement** dans les documents fournis. Un token non observé n'est jamais deviné, complété par une valeur "plausible", ni interpolé depuis une impression esthétique générale — voir § Garde-fou anti-hallucination ci-dessous. Une charte graphique incomplète produit un design system incomplet, explicitement signalé comme tel, jamais un design system inventé pour combler les trous.

## Étape 0 — Détecter les sources fournies

Ne jamais commencer l'extraction sans avoir listé explicitement ce qui a été transmis. Les formats acceptés sont volontairement ouverts — capture(s) d'écran, PDF de charte graphique ou de brand book, export ou lien Figma, URL d'un site web existant du client, logo seul, gabarit PowerPoint/Keynote existant, ou toute combinaison de ce qui précède.

1. Lister les documents effectivement reçus, avec leur type.
2. Si l'utilisateur annonce une source sans l'avoir jointe (« j'ai un PDF de charte, je te l'envoie » puis rien ne suit), le signaler explicitement plutôt que de poursuivre sur les seules sources reçues sans le mentionner.
3. Si une seule source est fournie et qu'elle est pauvre en information visuelle (ex. un logo seul, sans palette ni typographie visibles), le dire clairement et proposer de continuer avec un design system partiel plutôt que de bloquer — voir Étape 2.

**Validation** : légère — confirmer la liste des sources avant de commencer l'extraction proprement dite.

## Étape 1 — Extraire les tokens visuels observés

Pour chaque source fournie, identifier et noter, **uniquement ce qui est visible ou explicitement écrit dans le document** :

- **Couleurs** : code hexadécimal si affiché explicitement dans le document (ex. un brand book qui liste ses tokens), sinon estimation visuelle la plus précise possible **marquée comme telle** (`≈ #xxxxxx, estimé visuellement — à vérifier avec une pipette couleur avant usage en production`). Classer par rôle observé : accent principal, accents secondaires, neutres (texte, fonds), accents de data visualisation si présents.
- **Typographie** : nom de police si explicitement identifiable (métadonnées d'un export Figma, mention écrite dans un brand book, police système reconnaissable avec un haut degré de confiance) — sinon `NON DÉTERMINÉ`, jamais une police devinée à partir d'un rendu visuel dans une image, qui ne permet pas d'identifier une police avec fiabilité. Distinguer police de titre / police de corps si les deux sont identifiables séparément.
- **Motifs de composants récurrents** : formes observées à travers plusieurs pages/écrans du même document (cartes avec bordure, bandeaux d'en-tête colorés, tableaux zébrés, pastilles/labels, style d'icônes, rayon des coins, épaisseur de bordures) — un motif vu une seule fois n'est signalé qu'avec cette réserve, jamais généralisé en "règle" du design system sans récurrence observée.
- **Ton et mood général** : qualificatif descriptif court fondé sur ce qui est visible (ex. « sobre et institutionnel », « coloré et ludique »), jamais une évaluation de qualité.

**Garde-fou anti-hallucination** (le cœur de cette skill) : si une information n'est pas observable dans les sources fournies, la case correspondante du design system produit porte explicitement `NON DÉTERMINÉ` — jamais une valeur par défaut, une couleur "qui irait bien", ou une police standard choisie par convenance. Un design system partiel mais fidèle a plus de valeur qu'un design system complet mais partiellement inventé, puisqu'il sera utilisé tel quel pour produire un rendu visuel réellement montré au client.

**Validation** : aucune à ce stade — l'extraction brute alimente l'Étape 2.

## Étape 2 — Valider avec l'utilisateur avant de finaliser

Présenter la synthèse extraite (couleurs, typographie, composants, ton, et la liste des champs `NON DÉTERMINÉ`) et demander explicitement confirmation ou correction — en particulier :
- Toute couleur marquée « estimée visuellement » : proposer que l'utilisateur la vérifie avec un outil de pipette couleur sur le document source si la précision hexadécimale est critique pour l'usage prévu.
- Tout champ `NON DÉTERMINÉ` : demander si l'utilisateur dispose d'une information complémentaire (ex. la police exacte, connue par ailleurs) avant de la laisser non déterminée dans le livrable final.

Ne jamais finaliser le dossier de sortie (Étape 3) avant cette validation — une extraction non confirmée qui atterrit directement dans `slide-content-claude-design` propagerait une erreur potentielle à toutes les slides produites ensuite.

**Validation** : **structurante** — ce design system sera réutilisé tel quel pour toute la production visuelle du client, une erreur ici coûte cher à corriger une fois plusieurs modules déjà produits.

## Étape 3 — Produire le dossier de sortie

Créer un dossier de premier niveau `design-systems/<client>/`, **à côté** des workspaces `formations/` et `appels-offres/` plutôt qu'à l'intérieur de l'un d'eux : un design system client est réutilisable d'une formation à l'autre **et** entre formation et appel d'offres pour le même client — l'enfermer dans le workspace d'une session de formation obligerait à le recopier à chaque fois. Comme `formations/` et `appels-offres/`, ce dossier n'est **jamais versionné** (données client — voir `.gitignore` et `GOVERNANCE.md`) :

```
design-systems/<client>/
├── design-system.md      # tokens structurés (voir gabarit ci-dessous)
└── assets/                # logo(s) ou captures fournies telles quelles, si applicable — jamais retravaillées
```

`<client>` : kebab-case, cohérent avec la convention déjà utilisée par `formations/<client>-<thème>/` et `appels-offres/<client>-<objet>/` — sans suffixe de thème ni de date, puisque le design system vaut pour le client entier et non pour une session donnée.

`design-system.md` reprend **exactement** la structure de la section "Design system par défaut — Encre & Sauge" de `slide-content-claude-design/SKILL.md`, pour rester directement substituable :

```markdown
# Design system — <nom du client>

Source(s) : <liste des documents fournis à l'Étape 0>
Extrait le : <date>

## Couleurs
- Accent principal : <hex ou NON DÉTERMINÉ>
- Accents secondaires : <hex ou NON DÉTERMINÉ>
- Neutres (texte, fonds) : <hex ou NON DÉTERMINÉ>
- Accents data visualisation : <hex ou NON DÉTERMINÉ>

## Typographie
- Titres : <nom de police ou NON DÉTERMINÉ>
- Corps : <nom de police ou NON DÉTERMINÉ>

## Composants observés
<liste des motifs récurrents identifiés à l'Étape 1, avec mention "observé une seule fois" si applicable>

## Ton
<qualificatif court>

## Champs non déterminés
<liste explicite des informations non observables dans les sources fournies — jamais omise silencieusement>
```

**Livrable** : `design-systems/<client>/design-system.md` (+ `assets/` si des fichiers de marque ont été fournis).

**Validation** : déjà couverte à l'Étape 2 — cette étape est mécanique (écriture du fichier), aucun nouveau jugement introduit.

## Étape 4 — Proposer l'enchaînement vers `slide-content-claude-design`

Une fois le dossier produit, proposer explicitement d'enchaîner sur `slide-content-claude-design` en indiquant le chemin du `design-system.md` produit — cette dernière skill lit ce fichier à la place de sa palette par défaut « Encre & Sauge » quand il existe (voir sa § Design system par défaut). Ne jamais invoquer `slide-content-claude-design` de force ; ne jamais supposer que l'utilisateur veut enchaîner immédiatement.

Si des champs `NON DÉTERMINÉ` subsistent après l'Étape 2 (l'utilisateur n'a pas pu les compléter), le rappeler explicitement à ce moment : `slide-content-claude-design` devra alors combiner ce design system partiel avec des valeurs par défaut pour les champs manquants, jamais deviner ce que ce design system extrait ne dit pas.
