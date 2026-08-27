---
name: consultants-references-extractor
description: Extrait un référentiel de CV consultants et un référentiel de références/missions à partir de n'importe quel document fourni — decks avec une slide par CV ou par référence (format réel du cabinet), mais aussi PDF, Word, export LinkedIn, tableur RH, sans mise en page homogène d'un auteur à l'autre. Gère de gros volumes (plusieurs centaines d'entrées) par lots, avec point de contrôle après chaque lot. Un consultant peut apparaître sur plusieurs missions distinctes ; une mission peut réunir plusieurs consultants — le lien entre les deux référentiels est maintenu dans les deux sens. Ré-import régulier : fusionne avec l'existant, ne remplace jamais silencieusement une modification manuelle faite depuis la dernière extraction. Détecte les mentions de confidentialité (format variable) mais ne décide jamais elle-même qu'une référence est utilisable à l'externe — cette décision reste toujours humaine, au moment de la sélection dans `reponse-appel-offres`. Déclencher quand l'utilisateur demande d'"extraire les CV/le vivier de consultants", de "mettre à jour la base de références du cabinet", de "récupérer les CV depuis ce deck", ou fournit un ou plusieurs documents de CV/références sans plus de précision sur ce qu'il veut en faire.
---

# Extraction du référentiel consultants et références

Cette skill lit un ou plusieurs documents fournis par l'utilisateur (jamais devinés ni recherchés par elle-même) et en extrait **deux référentiels distincts**, réutilisables d'un appel d'offres à l'autre :

- `consultants/<identifiant>.md` — un fichier par consultant, avec ses missions.
- `references-missions/<identifiant>.md` — un fichier par mission/référence, avec les consultants y ayant contribué.

Les deux référentiels sont liés dans les deux sens (Contrats CR-1 et CR-2 de [`PIPELINE_CONTRACTS.md`](../PIPELINE_CONTRACTS.md)) et consommés par `reponse-appel-offres` pour la sélection d'équipe et de références (voir sa § « Étape 4bis » et « Étape 5bis »).

**Principe directeur, non négociable — identique à `design-system-extractor`** : cette skill ne décrit **que ce qu'elle observe réellement** dans les documents fournis. Un champ non observable est marqué `NON DÉTERMINÉ`, jamais deviné ni complété par une valeur plausible. Un référentiel incomplet mais fidèle a plus de valeur qu'un référentiel complet mais partiellement inventé, puisqu'il sert ensuite à sélectionner et présenter de vraies personnes et de vraies missions à un client réel.

**Second principe directeur, propre à cette skill** : la détection d'un niveau de confidentialité **documente ce qui a été trouvé**, elle **n'autorise jamais** un usage externe. Aucune étape de cette skill ne décide qu'une référence peut être citée à un client — cette décision reste toujours humaine, et toujours prise au moment de la sélection dans `reponse-appel-offres`, jamais ici.

## Étape 0 — Détecter les sources et le mode

1. Lister explicitement les documents fournis, avec leur type (deck, PDF, Word, export LinkedIn, tableur). Aucun format n'est imposé, mais chaque document annoncé sans être joint est signalé, jamais silencieusement ignoré.
2. Détecter le mode : si `consultants/` et/ou `references-missions/` contiennent déjà des fichiers, c'est un **ré-import** (Étape 4 s'applique) ; sinon, une **première extraction** (création directe, pas de fusion à faire).
3. Si le volume à traiter dépasse une trentaine d'entrées, prévenir explicitement que le traitement se fera par lots avec un point de contrôle après chacun — jamais un traitement silencieux de plusieurs centaines d'entrées d'un coup sans retour intermédiaire.

**Validation** : légère — confirmer la liste des sources et le mode détecté avant de commencer l'extraction.

## Étape 1 — Extraire les CV, par lots

Traiter les documents un par un (ou par petit lot cohérent, ex. un deck entier). Pour chaque slide/document représentant un CV :

1. **Identifier le consultant** : nom, prénom. Construire un identifiant stable (`prenom-nom` en kebab-case). En cas d'homonymie apparente avec un consultant déjà présent dans le référentiel, **ne jamais fusionner automatiquement** — comparer au moins un autre signal (poste, missions déjà connues) et, en cas de doute réel, signaler explicitement pour arbitrage humain plutôt que de deviner s'il s'agit de la même personne.
2. **Informations générales**, uniquement si explicitement présentes sur le document : poste/séniorité actuels, langues, certifications, disponibilité. Champ absent → `NON DÉTERMINÉ`.
3. **Compétences** : reprendre les tags explicites s'il y en a, **et** déduire des compétences supplémentaires du texte des missions décrites — en distinguant toujours la source (« tag explicite » vs « déduite de la mission X »), jamais mélangées sans distinction.
4. **Missions** : un consultant peut apparaître sur plusieurs slides, chacune avec une mission différente — traiter chaque mission séparément, jamais fusionnée en un résumé de carrière. Pour chaque mission : intitulé, période/durée si mentionnée, rôle sur cette mission, description, résultats chiffrés si mentionnés, compétences mobilisées.
5. **Rattacher chaque mission à une référence** (Étape 2) via l'identifiant de la référence correspondante — si la référence n'a pas encore été extraite à ce stade, noter l'intitulé de la mission et faire le lien à l'Étape 3.

**Point de contrôle** après chaque lot (chaque deck, ou tous les 20-30 CV traités) : nombre de consultants créés / mis à jour, nombre de champs `NON DÉTERMINÉ`, nombre de cas d'homonymie signalés — avant de poursuivre sur le lot suivant.

**Garde-fou** : jamais inventer une mission, un résultat chiffré, ou une compétence non écrite sur le document source.

## Étape 2 — Extraire les références/missions, par lots

Même logique que l'Étape 1, appliquée aux slides/documents de référence :

1. **Identifier la mission** : intitulé, client. Construire un identifiant stable (`client-objet` en kebab-case, cohérent avec la convention déjà utilisée par `formations/<client>-<thème>/` et `appels-offres/<client>-<objet>/`).
2. **Détecter la mention de confidentialité** — le format varie d'un document à l'autre (mot explicite, pictogramme, note en bas de slide), donc l'interpréter en contexte plutôt que chercher un mot-clé unique fixe. Classer :
   - `NOMMÉE` — le client est cité explicitement, rien n'indique une restriction.
   - `ANONYMISÉE` — mention explicite que le nom du client ne doit pas être cité, mais le secteur/contexte peut l'être.
   - `INTERNE_UNIQUEMENT` — mention explicite que cette référence ne doit jamais sortir du cabinet.
   - `NON PRÉCISÉ` — aucune mention trouvée, dans un sens ou dans l'autre. **Ne jamais interpréter une absence de mention comme une autorisation** : `NON PRÉCISÉ` déclenche la même exigence de confirmation humaine explicite que les trois autres niveaux avant tout usage externe (voir le second principe directeur en tête de ce document).
3. **Contexte, enjeux, approche, valeur ajoutée** : reformuler fidèlement le contenu du document source, sans readorner ni supprimer de nuance.
4. **Détails complémentaires**, si mentionnés : durée de mission, taille d'équipe mobilisée, technologies/méthodologies utilisées.
5. **Rattacher les consultants** ayant contribué, par leur identifiant (Étape 1) — une référence peut avoir plusieurs consultants.

**Point de contrôle** après chaque lot, incluant explicitement le décompte par niveau de confidentialité détecté.

**Garde-fou** : jamais inventer un résultat chiffré ou un contexte non écrit ; jamais reclasser silencieusement une référence `INTERNE_UNIQUEMENT` vers un niveau plus permissif, même si son contenu semble anodin.

**Le nom réel du client est toujours conservé**, quel que soit le niveau de confidentialité détecté — y compris `INTERNE_UNIQUEMENT`. Le référentiel est interne et jamais versionné : l'effacer n'apporterait aucune protection (l'identifiant du fichier est construit à partir du nom) tout en rendant impossible la sélection éclairée et le dédoublonnage au ré-import. La confidentialité se joue **à la sélection** (`reponse-appel-offres` Étape 5bis), qui décide ce qui sort du cabinet — jamais à l'extraction, qui se contente de documenter.

## Étape 3 — Lier les deux référentiels

Une fois l'Étape 1 et l'Étape 2 terminées pour un lot : vérifier que chaque mission listée dans un fichier consultant pointe vers un fichier référence existant (le créer si besoin, avec les seules informations déjà connues, complétées à l'extraction suivante), et que chaque fichier référence liste bien tous les consultants identifiés pour cette mission. Lien maintenu dans les deux sens, jamais un seul.

## Étape 4 — Fusionner avec l'existant (ré-import)

Ne s'applique qu'en mode ré-import (Étape 0).

Pour chaque consultant ou référence déjà présent dans le référentiel :

1. Comparer la date de **dernière extraction automatique** du fichier existant à sa date de **dernière modification manuelle** (les deux sont tracées en tête de chaque fichier, voir Contrats CR-1/CR-2).
2. **Si aucune modification manuelle n'a eu lieu depuis la dernière extraction** : mettre à jour les champs avec les nouvelles données extraites, sans confirmation nécessaire — c'est le cas nominal d'un ré-import régulier.
3. **Si une modification manuelle a eu lieu depuis**, et que la nouvelle extraction propose une valeur différente pour un champ déjà rempli manuellement : **ne jamais écraser silencieusement**. Signaler explicitement le conflit (champ, valeur actuelle, valeur nouvellement extraite) et laisser un humain trancher — trois options possibles : garder la valeur manuelle, adopter la nouvelle extraction, ou fusionner les deux.
4. Un champ marqué `NON DÉTERMINÉ` qui devient déterminable à cette extraction est toujours mis à jour directement — ce n'est jamais un conflit, seulement une amélioration.
5. Une mission ou une référence nouvellement trouvée qui n'existait pas encore : ajoutée directement, jamais de conflit possible.

**Point de contrôle** : récapitulatif des conflits identifiés à l'Étape 4, présenté avant de finaliser l'écriture des fichiers (Étape 5) — jamais résolu automatiquement dans un sens ou dans l'autre.

## Étape 5 — Produire ou mettre à jour les fichiers

Écrire `consultants/<identifiant>.md` (Contrat CR-1) et `references-missions/<identifiant>.md` (Contrat CR-2) dans les dossiers de premier niveau correspondants — **jamais à la racine du dépôt**, jamais versionnés (données personnelles et clients réelles, voir `.gitignore` et `GOVERNANCE.md`, même règle que `formations/`, `appels-offres/`, `design-systems/`).

Mettre à jour les dates de « dernière extraction automatique » sur chaque fichier touché ; ne jamais toucher à la date de « dernière modification manuelle » lors d'une extraction.

## Étape 6 — Proposer la prochaine étape

Résumer ce qui a été produit (nombre de consultants et de références créés/mis à jour, conflits restés en attente d'arbitrage, décompte par niveau de confidentialité) et proposer explicitement d'enchaîner sur `reponse-appel-offres` si un appel d'offres est en cours — sans jamais l'invoquer de force.

## Règles générales

- Toujours répondre et livrer en français, sauf demande contraire.
- Jamais deviner un nom, une mission, un résultat chiffré, ou un niveau de confidentialité non écrit explicitement dans le document source.
- Jamais fusionner deux consultants ou deux références différents sous prétexte de ressemblance — en cas de doute réel, signaler pour arbitrage humain.
- Jamais interpréter l'absence de mention de confidentialité comme une autorisation d'usage externe.
