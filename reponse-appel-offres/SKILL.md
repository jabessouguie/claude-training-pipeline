---
name: reponse-appel-offres
description: Pilote la réponse complète à un appel d'offres (AO) commercial, de la recherche méthodologique jusqu'au plan de présentation prêt à coller dans Claude Design — en 8 étapes : recherche sur les bonnes pratiques de réponse à AO, recherche étendue sur le client émetteur, analyse du besoin (avec checklist d'exigences CCTP tracée et détection d'un éventuel format de réponse imposé), analyse de l'adéquation cabinet/besoin (profil cabinet), sourcing et sélection de références pertinentes, plan de présentation détaillé slide par slide, puis renvoi vers comite-qualite. Si un référentiel consultants-references-extractor existe, deux étapes conditionnelles s'ajoutent en parallèle des étapes 4/5 : sélection de l'équipe à mobiliser (CV reformulés, une slide par consultant) et sélection de références sourcées du référentiel plutôt que du seul web/consultant. Déclencher dès que l'utilisateur partage un dossier d'AO, un CCTP, un règlement de consultation, ou demande de "répondre à un appel d'offres", une "analyse de fit", une "checklist d'exigences", ou un "plan de présentation commerciale". Remplace l'ancienne skill cadrage-appel-offres, qui ne couvrait que l'analyse du dossier — voir CHANGELOG.md.
---

# Réponse à appel d'offres

Cette skill pilote la réponse complète à un appel d'offres commercial : de la recherche méthodologique en amont jusqu'au plan de présentation détaillé, prêt à coller dans **Claude Design**. Elle produit, en cours de route, une checklist d'exigences tracée (livrable interne) et un plan de présentation slide par slide (livrable final) — puis propose l'enchaînement vers `comite-qualite`.

## Avant de démarrer — deadline serrée (< 5 jours ouvrés)

Les 8 étapes s'exécutent normalement dans l'ordre, sans étape à sauter par défaut — chacune alimente la suivante (la recherche méthodologique de l'Étape 0 nourrit la relecture de l'Étape 6, la checklist de l'Étape 2 conditionne le fit de l'Étape 3, etc.). Sous une deadline très serrée, poser explicitement la question **avant** l'Étape 0 plutôt que de laisser le consultant découvrir en cours de route que le temps manque :

> *« Le délai avant la remise de l'offre est-il très court (moins d'une semaine) ? Si oui, veux-tu qu'on réduise la profondeur des Étapes 0 et 1 (recherche méthodologique et recherche client resserrées à l'essentiel plutôt qu'exhaustives), en gardant les Étapes 2, 3 et 6 pleinement structurantes — ce sont elles qui déterminent la conformité et la qualité réelle de la réponse ? »*

Si le consultant confirme un mode resserré : les Étapes 0 et 1 produisent une synthèse plus courte (2-3 points de vigilance méthodologique au lieu de 5-8, recherche client limitée aux informations rapidement disponibles) — jamais en dessous du garde-fou anti-invention (une information non trouvée reste "à confirmer", jamais devinée pour aller plus vite). Les Étapes 2 (checklist d'exigences), 3 (fit cabinet) et 6 (plan de présentation) **restent pleinement structurantes dans tous les cas** : ce sont elles qui déterminent si l'offre est conforme et vendable, jamais des étapes à raccourcir sous prétexte de délai. Ne jamais réduire la profondeur d'une étape sans que le consultant l'ait explicitement demandé pour celle-ci.

## Workflow en 8 étapes (0 à 7), plus deux étapes conditionnelles (4bis, 5bis)

Les Étapes 4bis et 5bis ne s'exécutent que si un référentiel produit par `consultants-references-extractor` existe (`consultants/` et/ou `references-missions/` non vides) — sinon le workflow reste exactement celui décrit depuis la création de cette skill, Étapes 4/5 comprises, sans aucune dépendance à cette skill transverse. Quand le référentiel existe, 4bis et 5bis **s'ajoutent** aux Étapes 4/5 plutôt que de les remplacer : une référence ou un profil hors référentiel (one-off, jamais catalogué) reste éligible via le circuit historique demande-consultant/recherche-web.

### Étape 0 — Recherche méthodologique (bonnes pratiques et erreurs à éviter)

Distincte de l'Étape 1 : ici, la recherche porte sur **la discipline de réponse à appel d'offres en général** pour ce type de client et de mission — pas sur ce client précis (ça, c'est l'Étape 1).

Rechercher et synthétiser, en fonction du type de client identifié (secteur public vs privé, taille, secteur d'activité) :
- Les pièges classiques d'un mémoire trop générique, non personnalisé (recopiage de plaquette institutionnelle sans lien avec le dossier réel)
- L'importance de répondre **point par point** au CCTP plutôt que par grandes masses thématiques — lien direct avec la checklist d'exigences de l'Étape 2
- Les écueils spécifiques d'une soutenance orale si le marché en prévoit une (temps de parole mal réparti, slides surchargées lues mot à mot, absence de mise en situation concrète)
- Les spécificités sectorielles de notation : marché public (grille de notation contractuelle stricte et vérifiable poste par poste, poids du critère prix, mémoire technique noté séparément de l'offre financière) vs marché privé (notation souvent plus qualitative et relationnelle)
- Les erreurs de forme qui coûtent des points sans lien avec le fond (non-respect du nombre de pages imposé, absence de réponse à une question précise du RC, incohérence entre l'équipe présentée et l'équipe réellement affectée)
- Le risque des éléments de langage génériques ("excellence", "sur-mesure") sans preuve associée, par opposition à une différenciation réelle et démontrée

**Garde-fou** : une pratique générale trouvée en ligne est marquée « pratique générale du secteur, à confirmer sur ce dossier spécifique » — jamais présentée comme une règle universelle de notation, qui varie énormément d'un acheteur à l'autre.

**Livrable** : synthèse courte (5 à 8 points de vigilance méthodologique), intégrée à la conversation — pas de fichier durable dédié : ce n'est pas une donnée client, c'est une note de cadrage interne qui nourrit la relecture de l'Étape 6 et l'audit de l'Étape 7.

**Validation** : légère — présenter la synthèse, proposer d'creuser un point si besoin, sans bloquer l'enchaînement vers l'Étape 1.

### Étape 1 — Recherche étendue sur le client (émetteur de l'AO)

Avant toute recherche, **détecter le type de dossier** (jamais deviné) : poser explicitement

```
Ce dossier est-il un marché public (zip avec règlement de consultation/CCTP/CCAP/DPGF)
ou un dossier privé/gré à gré (cahier des charges informel, e-mails compilés) ?
```

- **Mode marché public** : inventorier les pièces reçues par leur nom conventionnel (RC, CCTP, CCAP, DPGF, annexes, acte d'engagement), signaler explicitement toute pièce attendue mais absente — jamais supposée « fournie à part ».
- **Mode informel** : demander à l'utilisateur de confirmer qu'il a fourni l'ensemble du contexte disponible — le risque d'exigence « cachée » dans un e-mail est plus élevé qu'un dossier normalisé.

Puis rechercher sur le web, sur l'entité émettrice : activité, taille, appartenance à un groupe, organisation interne pertinente pour le marché (DSI, direction achats, maîtrise d'ouvrage...), maturité sur le sujet de l'AO, actualités récentes (2 dernières années), contexte budgétaire si public. Rechercher aussi les personnes nommées dans le dossier (contact marché, membres du jury si mentionnés, signataire) avec la même discipline que `cadrage-formation` Étape 3 : signaler clairement les profils introuvables ou ambigus plutôt que d'inventer, marquer « à confirmer » ; au-delà de 20 personnes identifiées, basculer vers une synthèse par fonction plutôt qu'une recherche nominative exhaustive, en le signalant explicitement.

**Garde-fou** : jamais inventer un profil, une actualité, ou une information non trouvée.

**Livrable** : synthèse intégrée au dossier de travail — alimentera l'onglet « Entité émettrice »/« Personnes liées à l'AO » du XLSX interne de l'Étape 2.

**Validation** : légère — signaler les profils « à confirmer » sans bloquer la suite.

### Étape 2 — Analyser le besoin du client

L'étape la plus dense : elle produit la checklist d'exigences (héritée de l'ancienne `cadrage-appel-offres`, conservée à l'identique) et détecte tout format de réponse imposé par le client.

1. **Créer le workspace** (si pas déjà fait) : `appels-offres/<client>-<objet>/<AAAA-MM>/`
   - `<client>` : kebab-case ; `<objet>` : objet du marché en kebab-case (ex. `refonte-si-rh`) ; `<AAAA-MM>` : mois de la **date de remise de l'offre** (pas la date de réception du dossier). Ne jamais réutiliser un dossier d'un AO passé.
2. **Détecter si une période de questions à l'acheteur est ouverte** (jamais deviné) : poser explicitement *« Ce marché prévoit-il une période de questions/réponses avec l'acheteur avant la remise des offres ? Si oui, veux-tu que je prépare une liste de questions à lui envoyer, et sous quel format ? »* — si oui, produire cette liste en plus de la checklist (dérivée de l'extraction ci-dessous, jamais une question dont la réponse est déjà dans le dossier).
   - **Le workflow ne s'arrête jamais en attendant la réponse de l'acheteur** : une réponse peut prendre plusieurs jours, incompatible avec une deadline déjà serrée. Poursuivre normalement les Étapes 3 à 6 sur la base des exigences telles que comprises à ce stade, en marquant explicitement dans la synthèse de vigilance les exigences dont l'interprétation dépend d'une réponse encore attendue.
   - **Reprise une fois les réponses obtenues** : demander au consultant de fournir les réponses reçues, mettre à jour les lignes concernées de `exigences_<client>.xlsx` (statut, texte de l'exigence si la réponse la précise) en régénérant le fichier à partir d'un JSON mis à jour (voir § Script et contrat interne — le script n'a pas de mode d'édition incrémentale, il régénère l'ensemble du classeur), puis vérifier si une slide déjà rédigée à l'Étape 6 est affectée par cette clarification et la corriger si besoin — jamais silencieusement, signaler explicitement quelles slides ont été impactées.
3. **Détecter tout format de réponse imposé par le client** (jamais deviné) — trame/gabarit fourni par l'acheteur, sommaire obligatoire, nombre de pages maximum, ordre de présentation des pièces, contrainte de mise en page. Si le RC/CCTP ne précise rien explicitement, **poser la question** : *« Le client impose-t-il un format ou une trame de réponse ? »* — ne jamais supposer qu'aucun format n'est imposé faute de l'avoir vérifié. **Ce constat est central : il sera appliqué en priorité à l'Étape 6.**
4. **Lire l'intégralité du dossier** et en extraire le contexte (client, objet, dates, contraintes de forme/périmètre).
5. **Extraire chaque exigence individuellement** (jamais résumée collectivement) : source exacte (article/page), thème, texte reformulé fidèlement (jamais édulcoré), catégorie :
   - `OBLIGATOIRE` — à traiter, son absence dégraderait la note ou la crédibilité de l'offre
   - `SOUHAITABLE` — un plus valorisé, non bloquant
   - `ÉLIMINATOIRE` — rejet automatique si non respectée
6. **Extraire les critères de notation et pondération** si le RC les précise (vide si non applicable, jamais deviné).
7. **Synthétiser les points de vigilance** : ambiguïtés du CCTP, exigences contradictoires, compétences manquantes repérées, délai serré vs charge estimée.

**Garde-fous** : jamais deviner une exigence non écrite ; jamais fusionner deux exigences distinctes pour aller plus vite ; toute pièce attendue mais absente devient un point de vigilance explicite, jamais une hypothèse silencieuse.

**Livrable** : `exigences_<client>.xlsx` (Contrat AO-1 de [`PIPELINE_CONTRACTS.md`](../PIPELINE_CONTRACTS.md)) — **livrable interne** de cette étape, produit via :
```bash
python scripts/generate_exigences_xlsx.py input.json appels-offres/<client>-<objet>/<AAAA-MM>/exigences_<client>.xlsx
```
Voir le format JSON d'entrée et la structure du classeur produit en fin de document (§ Script et contrat interne). Si une période de questions est ouverte : liste de questions à l'acheteur dans le format demandé, en plus de ce fichier.

**Validation** : **structurante** — présenter la checklist, la synthèse de vigilance, et le format de réponse imposé détecté (ou son absence confirmée) avant de poursuivre vers l'Étape 3. Une exigence mal catégorisée ou un format imposé raté fausserait toute la suite (fit, sélection de références, plan de présentation).

### Étape 3 — Analyser l'adéquation entre le cabinet et le besoin (profil cabinet)

**Le cabinet n'est jamais présupposé** : il varie selon le consultant et la mission — ne jamais assumer un nom de cabinet par défaut.

1. Vérifier si `profil-cabinet.md` existe déjà **dans le workspace de l'AO en cours** (`appels-offres/<client>-<objet>/<AAAA-MM>/profil-cabinet.md`).
2. **S'il n'existe pas** : demander explicitement si le consultant dispose déjà d'un profil rempli pour un AO précédent. **Cette skill ne maintient aucun registre central des profils passés** — elle ne recherche jamais elle-même dans d'autres dossiers `appels-offres/`. Si le consultant répond oui, lui demander de **fournir directement le chemin du fichier ou de coller son contenu** (il connaît son propre historique de dossiers, l'agent ne le devine ni ne le parcourt) ; le copier dans le workspace en cours après confirmation. Sinon, créer le profil interactivement à partir du gabarit [`references/profil_cabinet_gabarit.md`](references/profil_cabinet_gabarit.md), section par section — jamais deviné, y compris le nom du cabinet.
3. **S'il existe déjà** dans ce workspace : le relire, proposer une mise à jour si une section semble datée, jamais l'écraser sans confirmation.
4. **Validation par une personne habilitée** : lors du **premier remplissage** d'un profil cabinet (que ce soit à partir du gabarit ou par copie d'un profil antérieur jamais revalidé depuis), demander explicitement si une personne senior/associée du cabinet a validé les sections "Différenciateurs" et "Domaines d'expertise" — ce ne sont pas de simples données factuelles, elles engagent le positionnement commercial du cabinet dans un document potentiellement contractuel. Si le consultant confirme qu'il remplit seul, sans validation senior, **le signaler explicitement comme point de vigilance** dans la synthèse de fit (jamais un silence qui laisserait croire à une validation qui n'a pas eu lieu) — ne jamais bloquer la suite pour autant, la décision de poursuivre reste au consultant.
5. Croiser chaque exigence `OBLIGATOIRE`/`ÉLIMINATOIRE` de la checklist (Étape 2) avec les domaines d'expertise et méthodologies du profil : produire une évaluation de fit **par grand thème du CCTP** (couvert / partiellement couvert / non couvert), pas une impression globale.

**Garde-fous** : l'analyse de fit ne conclut jamais à une adéquation sur un thème que le profil ne couvre pas explicitement — une section du profil marquée « non renseigné » ne peut jamais devenir un "couvert" par optimisme. Un profil jamais validé par une personne habilitée reste utilisable (ne bloque pas le travail), mais ce point de vigilance doit être visible jusqu'à l'Étape 6 et rappelé avant l'enchaînement vers `comite-qualite` (Étape 7).

**Livrable** : `profil-cabinet.md` rempli dans le workspace de l'AO (jamais un fichier partagé à la racine du dépôt) + synthèse de fit intégrée à la conversation, réutilisée à l'Étape 6 (slide APPROCHE).

**Validation** : **structurante** pour le remplissage initial du profil (réutilisé pour toute la suite de cet AO, coûteux à mal remplir) ; légère pour l'analyse de fit elle-même.

### Étape 4 — Demander les références et l'équipe pressentie

Deux matières distinctes sont collectées ici, toutes deux nécessaires à l'Étape 6 : les **références** du cabinet et l'**équipe** qu'il compte mobiliser.

**4.a — Références.** Demander explicitement au consultant sa liste de références à mettre en avant (client, objet de la mission, résultats, secteur, année). **Compléter systématiquement** par une recherche web de références **publiques** du cabinet (études de cas publiées, mentions presse, témoignages clients publiés, site du cabinet) — toujours les deux sources, sauf impossibilité signalée explicitement (ex. cabinet sans présence web).

**4.b — Équipe pressentie.** Demander explicitement au consultant qui il compte mobiliser sur la mission et, pour chaque personne, ce qui justifie sa présence : rôle proposé, missions antérieures pertinentes vis-à-vis de cet AO, compétences utiles. **Ne jamais composer l'équipe soi-même à partir du seul CCTP** — le cabinet seul sait qui est disponible et qui il engage. Une personne annoncée sans élément justifiant sa présence reste dans la liste, mais son manque est signalé explicitement comme point de vigilance : une slide `ÉQUIPE-MEMBRE` (Étape 6) ne peut pas être rédigée sans ces éléments, et ils ne s'inventent pas.

Si un référentiel de consultants existe, l'Étape 4bis enrichit cette collecte à partir de `consultants/` plutôt que de tout redemander de mémoire — mais 4.b reste le socle : c'est elle qui garantit qu'une équipe existe même sans référentiel.

**Garde-fous stricts** :
- Jamais inventer un membre d'équipe, un rôle, ou une mission antérieure non fournis par le consultant ou présents dans `consultants/`.
- Jamais inventer une référence non confirmée par au moins une des deux sources.
- Une référence mentionnée par le consultant mais non trouvée en ligne reste valide (mission confidentielle, fréquente en conseil) — marquée « source : consultant, non publique ».
- Une référence trouvée en ligne mais non confirmée par le consultant est marquée « source : recherche web publique, à confirmer avant utilisation » — **jamais utilisée telle quelle** dans le plan de présentation (Étape 6) sans cette confirmation.
- Jamais attribuer au cabinet cible une référence d'un homonyme ou d'une entité différente sans vérification croisée explicite (nom exact, activité cohérente).

**Livrable** : liste de références consolidée (Client / Secteur / Objet / Année / Taille approximative / Source / Lien si public) **et** liste de l'équipe pressentie (Nom / Rôle proposé / Missions antérieures pertinentes / Compétences utiles / éléments manquants signalés).

**Validation** : légère pour les références fournies directement par le consultant (déjà maîtrisées) ; **une confirmation verbale rapide ("oui, ok") ne suffit pas** pour une référence "à confirmer" issue de la recherche web — demander explicitement au consultant s'il a vérifié que le client est toujours d'accord pour être cité et que l'information reste d'actualité, pas seulement qu'il "connaît" cette référence. Si cette vérification active ne peut pas être faite dans le délai disponible, la référence reste marquée "à confirmer" et **n'est pas éligible à la sélection de l'Étape 5** — jamais retenue par défaut faute de temps pour vérifier.

### Étape 5 — Analyser et sélectionner les références pertinentes

Appliquer des critères de pertinence **explicites** à la liste consolidée de l'Étape 4 :
1. **Secteur similaire** (ou adjacent, enjeux comparables) au client émetteur de l'AO (Étape 1)
2. **Techno/méthodologie similaire** aux technologies/méthodologies mentionnées dans le CCTP (Étape 2)
3. **Taille de mission comparable** (budget, durée, taille d'équipe) — évite de présenter une référence disproportionnée

Retenir 3 à 5 références, chacune justifiée par au moins un des trois critères explicités.

**Garde-fou** : jamais sélectionner une référence encore « à confirmer » ; signaler explicitement une référence qui ne coche qu'un seul critère faiblement (« proximité sectorielle forte, mais taille de mission très inférieure »).

**Livrable** : sélection finale justifiée, alimente directement les slides `RÉFÉRENCE` de l'Étape 6 (une par référence retenue, voir Étape 6).

**Validation** : légère.

### Étape 4bis — Sélectionner l'équipe à mobiliser (si un référentiel de consultants existe)

Ne s'exécute que si `consultants/` (produit par `consultants-references-extractor`) contient des fiches. **Enrichit l'Étape 4.b**, ne la remplace pas : 4.b garantit qu'une équipe existe dans tous les cas (elle est demandée au consultant) ; 4bis évite de tout ressaisir de mémoire quand le référentiel est disponible, et permet une sélection argumentée parmi plusieurs candidats. Si le consultant a déjà nommé son équipe en 4.b, croiser avec `consultants/` pour compléter les fiches plutôt que de reprendre la sélection à zéro — ne jamais écarter silencieusement quelqu'un que le consultant a explicitement désigné.

1. **Déterminer les profils requis** à partir des exigences de l'Étape 2 (compétences, technologies, méthodologies attendues) et du volume/de la durée de la mission si connus.
2. **Rechercher dans `consultants/`** les consultants correspondant aux profils requis, sur la base de leurs compétences (tags explicites et déduites), de leur séniorité, et de leur disponibilité si renseignée.
3. **Pour chaque profil requis où plusieurs consultants sont candidats** : ne jamais trancher seul — présenter toutes les options viables (y compris, si pertinent, mettre en avant deux candidats concurrents dans la sélection provisoire) et laisser le consultant/rédacteur choisir.
4. **Pour chaque consultant retenu, sélectionner ses missions les plus pertinentes** vis-à-vis de l'AO (même logique à deux niveaux que la sélection de références : d'abord quels consultants, puis quelles missions de ces consultants mettre en avant) — un consultant peut avoir plusieurs missions candidates, n'en retenir que les plus pertinentes au regard des exigences de l'Étape 2.
5. **Reformuler strictement factuellement** le rôle, la valeur ajoutée, et les compétences utiles de chaque consultant retenu pour cet AO précis — jamais une compétence ou un résultat non présent dans sa fiche `consultants/`.

**Garde-fou** : aucun nombre cible de consultants à retenir — dépend entièrement de ce que l'AO demande (nombre de profils exigés, taille d'équipe attendue). Jamais gonfler artificiellement l'équipe présentée au-delà du besoin réel.

**Livrable** : sélection d'équipe justifiée + fiches reformulées, alimentent directement les slides `ÉQUIPE-MEMBRE` de l'Étape 6.

**Validation** : **structurante** — chaque fiche reformulée doit être validée par le consultant concerné avant d'être considérée finale (même logique que la validation senior du profil cabinet, Étape 3) ; ne jamais proposer l'enchaînement vers l'Étape 6 tant qu'une fiche retenue n'a pas été validée par la personne qu'elle décrit.

### Étape 5bis — Sélectionner des références depuis le référentiel (si `references-missions/` existe)

Ne s'exécute que si `references-missions/` (produit par `consultants-references-extractor`) contient des fiches. S'ajoute à l'Étape 5, ne la remplace pas — une référence catalogée et une référence one-off (Étape 4/5) peuvent cohabiter dans la même sélection finale.

1. Appliquer les **mêmes trois critères qu'à l'Étape 5** (secteur, techno/méthodologie, taille de mission) aux fiches de `references-missions/`.
2. **Vérifier la confidentialité de chaque référence candidate avant de la retenir** : le niveau documenté dans la fiche (`NOMMÉE`/`ANONYMISÉE`/`INTERNE_UNIQUEMENT`/`NON PRÉCISÉ`) ne suffit **jamais** à autoriser un usage externe — **toujours demander une confirmation humaine explicite** avant qu'une référence catalogée n'entre dans la sélection finale, quel que soit son niveau documenté. Une référence dont la confidentialité n'a pas pu être confirmée dans le délai disponible n'est pas éligible, exactement comme une référence web « à confirmer » à l'Étape 4.
3. **Reformuler strictement factuellement** le contexte, l'approche et la valeur ajoutée pour cet AO précis — jamais une donnée non présente dans la fiche `references-missions/`.

**Garde-fou** : aucun nombre cible fixe — dépend du besoin de l'AO, comme pour l'Étape 4bis.

**Livrable** : sélection justifiée (avec, pour chaque référence retenue, la confirmation de confidentialité obtenue), alimente directement les slides `RÉFÉRENCE` de l'Étape 6 aux côtés des références one-off de l'Étape 5.

**Validation** : **structurante** — la confirmation de confidentialité est un préalable bloquant à l'inclusion dans la sélection, jamais une formalité a posteriori.

### Étape 6 — Plan de présentation détaillé pour Claude Design

**Priorité absolue au format imposé** : si l'Étape 2 a détecté un format de réponse imposé par le client (trame, sommaire obligatoire, pagination, ordre des pièces), **le plan de présentation s'y conforme** — la structure imposée remplace le vocabulaire de blocs par défaut ci-dessous. Ne jamais imposer la structure par défaut de cette skill par-dessus une contrainte contractuelle explicite du client. Si le format imposé ne couvre qu'une partie de la présentation (ex. un sommaire obligatoire pour le mémoire écrit mais aucune contrainte sur un éventuel support de soutenance orale distinct), appliquer le format imposé là où il s'applique et le vocabulaire par défaut ailleurs — jamais un mélange silencieux non signalé.

**Mécanique de transformation d'un format imposé en fiches slide** : chaque section/article du sommaire imposé (y compris une numérotation imbriquée type « 3.2.1 Méthodologie de pilotage ») devient un `TYPE` propre, nommé d'après l'intitulé exact de la section imposée — pas d'après le vocabulaire par défaut. Une sous-partie numérotée du sommaire imposé peut correspondre à une ou plusieurs slides selon son volume réel de contenu (jamais une seule slide forcée si le contenu déborde, jamais plusieurs slides artificielles pour une sous-partie courte) — la colonne vertébrale (liste numérotée de slides avant rédaction détaillée) sert précisément à trancher ce découpage et à le faire valider avant d'investir dans les fiches détaillées. Les blocs COUVERTURE et SOMMAIRE restent nécessaires même si le sommaire imposé ne les mentionne pas explicitement (une présentation a toujours une page de garde et une table des matières) — les ajouter en dehors de la structure imposée, en le signalant explicitement comme un ajout non contraint par le client. Si la pagination maximale imposée par le client rend impossible de couvrir toutes les sections avec le niveau de détail habituel, le signaler explicitement comme point de vigilance avant de rédiger, plutôt que de dépasser silencieusement la limite ou de sacrifier une section sans le dire.

**Sinon (aucun format imposé détecté)**, reprendre la méthode de `slide-content-claude-design/SKILL.md` : établir la colonne vertébrale (liste numérotée de slides : type + titre + objectif d'une ligne) et la faire valider avant de rédiger, puis produire fiche et prompt en parallèle, slide par slide.

**Vocabulaire de blocs par défaut** :
```
TYPE ∈ {COUVERTURE, SOMMAIRE, COMPRÉHENSION-ENJEUX, APPROCHE, ÉQUIPE-MEMBRE, RÉFÉRENCE, PLANNING, CONFORMITÉ, SYNTHÈSE}
```
- **COUVERTURE** : titre, client, objet du marché, cabinet, date
- **SOMMAIRE** : structure de la présentation
- **COMPRÉHENSION-ENJEUX** : reformulation du besoin (Étape 2), preuve de lecture réelle du dossier — répond au piège du mémoire générique (Étape 0)
- **APPROCHE** : méthodologie proposée, différenciateurs (issus du profil cabinet, Étape 3)
- **ÉQUIPE-MEMBRE** : **une slide par consultant retenu** — jamais plusieurs consultants regroupés sur une seule slide, quel que soit leur nombre. Contenu issu de l'Étape 4.b (équipe demandée au consultant, socle toujours présent), enrichi par l'Étape 4bis si un référentiel existe. Gabarit dédié ci-dessous.
- **RÉFÉRENCE** : **une slide par référence retenue** (Étape 5, complétée par 5bis si un référentiel existe) — jamais plusieurs références regroupées sur une seule slide. Gabarit dédié ci-dessous.
- **PLANNING** : jalons, macro-planning de la mission
- **CONFORMITÉ** : réponse point par point aux exigences `OBLIGATOIRE`/`ÉLIMINATOIRE` majeures — répond explicitement au piège « grandes masses plutôt que point par point » (Étape 0)
- **SYNTHÈSE** : rappel de la valeur différenciante, appel à l'action

**Garde-fous** : chaque champ `Visuel` entièrement dimensionné/positionné/colorisé — jamais une catégorie vague. Aucun chiffre cité ne doit être inventé — chaque chiffre est ancré dans le CCTP (Étape 2), le profil cabinet (Étape 3) ou une référence confirmée (Étape 4/5). **Claude Design n'expose aucune API programmatique** (vérifié le 28/07/2026, voir `PIPELINE_CONTRACTS.md`) — la composition reste manuelle dans tous les cas, cette skill ne promet aucun mode automatique de composition.

**Point de vigilance — engagement contractuel implicite** : un mémoire de réponse à AO n'est pas qu'un document de communication, il peut engager le cabinet une fois l'offre remise (planning annoncé, taux d'engagement, garantie de résultat). Un chiffre exact au sens factuel (ancré dans une source réelle) peut néanmoins être imprudent au sens commercial/contractuel s'il est présenté sans la nuance appropriée (ex. un planning présenté comme un engagement ferme plutôt qu'une estimation). Cette skill vérifie l'exactitude factuelle des chiffres, **pas leur prudence contractuelle** — ce n'est pas son rôle de trancher ce point. Signaler explicitement à l'utilisateur, avant de proposer l'enchaînement vers `comite-qualite` (Étape 7), que les chiffres d'engagement (planning, garanties, SLA) méritent une relecture par une personne habilitée à engager le cabinet, distincte de la relecture de cohérence de `comite-qualite`.

**Livrable — deux fichiers** (Contrat AO-2 de [`PIPELINE_CONTRACTS.md`](../PIPELINE_CONTRACTS.md)), rangés dans `appels-offres/<client>-<objet>/<AAAA-MM>/livrables/` :

`plan-presentation-content.md` — une fiche par slide :
````
### Slide N — TYPE — Titre court
- **Titre à l'écran** : <titre ; bicolore possible : MOT **mot-clé accent**>
- **Accroche / sous-titre** : <une phrase choc, courte>
- **Contenu** :
  - <3 à 5 puces concises, orientées jury/décideur>
- **Chiffre / preuve clé** : <donnée + (source : CCTP | profil cabinet | référence confirmée | consultants/references-missions)>   ← omettre si non pertinent
- **Visuel <design system>** :
  - **Composant** : <UN type précis, pas une liste : 3 cartes | tableau comparatif | matrice 2×2 | timeline | citation | KPI tiles>
  - **Dimensions et position sur le canevas** : <L × H px + emplacement exact>
  - **Couleurs** : <tokens exacts appliqués à CE composant>
  - **Contenu du composant** : <ce qui remplit chaque partie — pas de placeholder vague>
- **Bloc texte (si besoin)** : <texte à incruster proprement, HORS image>
- **Bloc (si fallback vectoriel)** : <composant à construire en couche vectorielle/texte>
- **Placeholder image** :
  ```
  [PLACEHOLDER GRIS — IMAGE GÉNÉRÉE GEMINI]
  Dimensions exactes : <L × H px de la zone réservée sur CETTE slide>
  Position : <ex. moitié droite / bandeau inférieur / pleine largeur sous le titre>
  Voir prompt détaillé → plan-presentation-prompts.md § Slide N
  ```
````
Si un format imposé s'applique, adapter le champ `TYPE` aux sections réellement exigées par le client plutôt qu'au vocabulaire par défaut ci-dessus — documenté explicitement dans le fichier produit (ex. « TYPE conforme au sommaire imposé par le RC art. X »).

**Gabarit dédié `ÉQUIPE-MEMBRE`** (une slide par consultant retenu, en plus des champs génériques ci-dessus) :
````
### Slide N — ÉQUIPE-MEMBRE — <Nom du consultant>
- **Rôle proposé sur cette mission** : <valeur>
- **Pourquoi ce profil est indispensable** : <reformulation strictement factuelle de ce qu'a fourni le consultant (Étape 4.b) ou de sa fiche consultants/<identifiant>.md si elle existe — jamais une compétence ou une justification absente des deux>
- **Missions pertinentes vis-à-vis de l'AO** :
  - <Intitulé mission 1> — valeur ajoutée : <texte>
  - <Intitulé mission 2> — valeur ajoutée : <texte>   ← autant que de missions retenues à l'Étape 4bis
- **Compétences utiles pour cette mission** : <liste, issue de l'Étape 4.b ou de consultants/<identifiant>.md>
- **Résultats chiffrés** (si disponibles sur une mission mise en avant) : <donnée + (source : Étape 4.b | consultants/<identifiant>.md)>   ← omettre si non pertinent
````

**Gabarit dédié `RÉFÉRENCE`** (une slide par référence retenue, en plus des champs génériques ci-dessus) :
````
### Slide N — RÉFÉRENCE — <Intitulé de la mission, ou "Référence sectorielle" si anonymisée>
- **Secteur du client** : <valeur>
- **Nom du client** : <valeur si niveau NOMMÉE et confirmation obtenue (Étape 5bis) ; sinon "non cité — anonymisé à la demande du client">
- **Contexte et enjeux** : <reformulation factuelle depuis references-missions/<identifiant>.md ou depuis la source consultant/web de l'Étape 4>
- **Notre approche** : <texte>
- **Notre valeur ajoutée / résultats** : <texte, avec chiffres si confirmés>
- **Durée / taille d'équipe / technologies** (si disponibles) : <valeurs>   ← omettre si non pertinent
````
Pour une référence issue du référentiel (Étape 5bis), ces deux gabarits ne sont renseignés qu'une fois la confidentialité confirmée par un humain — jamais avant.

**Règle** : ne jamais laisser « Visuel » comme une simple catégorie de composant sans dimensions ni couleurs — le lecteur qui colle la fiche dans Claude Design doit pouvoir construire le composant sans deviner un seul paramètre visuel. Règles du placeholder d'illustration, gabarits d'emplacement types, et fallback « hors compétences du générateur d'image » : identiques à `slide-content-claude-design/SKILL.md` (mêmes règles, non dupliquées ici).

`plan-presentation-prompts.md` — même structure que `M<n>-prompts.md` de `slide-content-claude-design` :
- Bloc « Direction artistique » unique en tête (style illustratif — souvent plus sobre/corporate qu'en formation, une présentation commerciale n'a pas nécessairement de métaphore filée ; contraintes récurrentes).
- Une section `## Slide N — Illustration` par slide illustrée (Contenu clé / Dimensions-position / Prompt pour Gemini).
- Règle anti-texte-dans-l'image et fallback vectoriel repris à l'identique de `slide-content-claude-design`.
- Design system par défaut : **Encre & Sauge** (tokens identiques : bleu marine `#2C5F8A`, corail `#D97757`, vert sauge `#4A8B6F`, encre `#1F1F1F`, gris `#F7F7F7`, beige `#E8E2DA`) — sauf si le cabinet a sa propre charte à appliquer manuellement, même question posée explicitement qu'ailleurs (« la charte par défaut convient, ou une charte propre à appliquer ? »).

*Note (corrigée le 27/08/2026)* : `design-system-extractor` existe désormais et est branchée dans `slide-content-claude-design/SKILL.md` (§ Design system par défaut) — mais pas encore ici. Une future itération pourra la brancher aussi à cette étape ; non implémenté dans cette version, la charte propre du cabinet reste appliquée manuellement pour le pipeline AO à ce jour.

**Mise à jour de la checklist d'exigences après rédaction** : une fois les fiches produites, mettre à jour `exigences_<client>.xlsx` pour chaque exigence traitée : renseigner la colonne "Partie du mémoire" (quel `TYPE`/slide y répond) et "Page de réponse" (numéro de slide, en l'absence de pagination réelle avant composition dans Claude Design), et faire passer le statut à `Traité`. Le script `generate_exigences_xlsx.py` n'a pas de mode de mise à jour incrémentale : régénérer l'intégralité du classeur à partir d'un JSON mis à jour reprenant toutes les données déjà saisies à l'Étape 2, avec ces deux colonnes complétées. Avant de proposer l'enchaînement vers l'Étape 7, vérifier qu'aucune exigence `OBLIGATOIRE`/`ÉLIMINATOIRE` ne reste au statut `Non traité` — sinon le signaler explicitement comme blocage réel (voir Contrat AO-1, règle de complétude), jamais un oubli silencieux.

**Validation** : **structurante** à deux niveaux — colonne vertébrale validée avant rédaction détaillée des fiches ; audit UX/UI (ou directement l'Étape 7) proposé avant toute génération visuelle dans Claude Design, jamais l'inverse.

### Étape 7 — Comité qualité

Proposer explicitement l'enchaînement vers `comite-qualite` en fin d'Étape 6 : lire et suivre maintenant les instructions de `comite-qualite/SKILL.md` sur le mémoire/plan de présentation produit — mécanique identique à celle de `formation-pipeline`, jamais un appel programmatique. Aucune invocation forcée : cette skill **propose**, elle n'enchaîne pas automatiquement.

**Sous une deadline serrée (rappelée comme risque n°1 dès l'Étape 0), sauter cette étape est le point de risque le plus élevé de tout le processus** — au même titre que les points de validation structurants des Étapes 2, 3 et 6 : un plan non relu est le stade où une incohérence entre contributeurs (ton, chiffres, promesses contradictoires entre slides) a le plus de chances de passer inaperçue avant l'envoi. Le signaler explicitement au consultant plutôt que de le laisser deviner l'importance relative de cette étape.

`comite-qualite/SKILL.md` couvre déjà ce type de livrable via ses rôles conditionnels existants : « Directeur de mission / Senior Partner » (déclenché par une audience direction/client/jury — un jury de sélection d'AO en relève) et « UX/Directeur artistique » (déclenché par un format visuel — un plan de présentation en relève). Ces rôles n'ont pas été conçus nommément pour un « mémoire de réponse à AO » et l'analogie reste à faire par la personne qui compose l'équipe de relecteurs à la Phase 0.2 de `comite-qualite` — signaler explicitement ce contexte (mémoire de réponse à AO, audience = jury de sélection) au moment de déclencher `comite-qualite`, pour que cette analogie soit faite consciemment plutôt que supposée automatique.

**Validation** : celle déjà définie par `comite-qualite/SKILL.md` lui-même — cette skill ne redéfinit rien.

## Script et contrat interne — `exigences_<client>.xlsx` (Étape 2)

Produit par `scripts/generate_exigences_xlsx.py` (mêmes conventions visuelles que `cadrage-formation/scripts/generate_cadrage_xlsx.py` : en-tête bleu marine, priorités en couleur, filtres + volets figés, pas de formule).

### Format du JSON d'entrée

```json
{
  "titre": "Analyse AO — Refonte SI RH — Client Alpha",
  "client": "Alpha Digital Solutions",
  "objet": "Refonte du SI RH",
  "type_dossier": "marche_public",
  "date_remise": "2026-09-12 16:00",
  "contexte": ["Ligne de contexte 1", "Ligne 2"],
  "points_vigilance": ["Point 1", "Point 2"],
  "exigences": [
    {"numero": "EX-001", "source": "CCTP art. 4.2", "theme": "Sécurité",
     "exigence": "Hébergement souverain en France requis.",
     "categorie": "OBLIGATOIRE", "critere_notation": "Critère technique 40%",
     "statut": "Non traité", "partie_memoire": "", "page_reponse": "", "commentaire": ""}
  ],
  "jalons": [
    {"jalon": "Remise offre", "date": "2026-09-12 16:00", "contrainte": "Dépôt dématérialisé"}
  ],
  "entite_emettrice": ["Ligne de synthèse 1 sur l'entité", "Ligne 2"],
  "personnes": [
    {"nom": "DUPONT", "prenom": "Marie", "role_ao": "Contact marché",
     "poste_actuel": "Directrice SI (?)", "seniorite": "Direction",
     "profil": "À confirmer", "statut": "À confirmer"}
  ],
  "secteur_industrie": ["Ligne de synthèse 1 sur le secteur"],
  "technologies": [
    {"techno": "SAP SuccessFactors", "citee_ou": "CCTP art. 3.1",
     "etat_de_lart": "Solution mature", "maturite": "Élevée",
     "alternatives": "Workday, Cegid RH", "vigilance": ""}
  ],
  "go_no_go": [
    {"critere": "Charge estimée vs capacité", "constat": "...", "poids": "Élevé"}
  ],
  "questions_acheteur": [
    {"question": "Le délai d'astreinte s'applique-t-il hors horaires ouvrés ?",
     "article": "CCTP art. 6.3", "justification": "Ambiguïté RC/CCTP"}
  ],
  "format_reponse_impose": "Sommaire imposé par le RC art. 5 : Compréhension / Méthodologie / Équipe / Prix. Pagination maximale 30 pages hors annexes."
}
```

Les clés `personnes`, `entite_emettrice`, `secteur_industrie`, `technologies`, `jalons`, `go_no_go`, `contexte`, `points_vigilance`, `format_reponse_impose` sont optionnelles mais fortement recommandées. La clé `questions_acheteur` n'est utilisée qu'en cas de période de questions ouverte avec format tableau demandé.

### Ce que produit le script

- Onglet **Exigences CCTP** (toujours présent) : N° / Source / Thème / Exigence / Catégorie / Critère de notation lié / Statut de traitement / Partie du mémoire / Page de réponse / Commentaire, avec filtres, volets figés, `ÉLIMINATOIRE` en rouge vif.
- Onglets conditionnels : Deadline & jalons, Entité émettrice, Personnes liées à l'AO, Secteur & industrie, Technologies mentionnées, Go-No-go, Questions à l'acheteur, Format de réponse imposé (rempli si `format_reponse_impose` est renseigné).

**Règle de complétude** : toute exigence de catégorie `OBLIGATOIRE`/`ÉLIMINATOIRE` doit atteindre le statut `Traité` (avec une `Page de réponse` renseignée une fois le plan de présentation produit) ou `Non applicable (à justifier)` — jamais un choix laissé filer silencieusement.

## Proposer la prochaine étape

Adapter le message à ce qui a réellement été produit à chaque étape structurante (2, 3, 6), sur ce modèle pour l'Étape 6 :

```
Les fiches slide-par-slide du plan de présentation sont prêtes dans
<chemin>/livrables/plan-presentation-content.md et plan-presentation-prompts.md.

Avant de générer visuellement dans Claude Design, je recommande un audit UX/UI
rapide de plan-presentation-content.md — ou de passer directement par
comite-qualite, qui couvre déjà cet angle avec un rôle "UX/Directeur artistique"
et un rôle "Directeur de mission" pertinents pour ce type de livrable.

Rappel : la composition finale dans Claude Design reste manuelle (pas d'API
programmatique disponible à ce jour).

Veux-tu que j'enchaîne sur comite-qualite maintenant, ou préfères-tu d'abord
relire le plan toi-même ?
```

## Règles générales
- Toujours répondre et livrer en français, sauf demande contraire.
- Ne jamais présenter une hypothèse de recherche comme un fait : utiliser « probable », « à confirmer ».
- Ne jamais deviner une exigence, une référence, un CV, un nom de cabinet, ou un format de réponse imposé non écrit explicitement dans le dossier, dans `consultants/`/`references-missions/`, ou confirmé par l'utilisateur.
- Une référence issue de `references-missions/` n'est jamais incluse dans un livrable envoyé au client sans confirmation humaine explicite de sa confidentialité, quel que soit le niveau documenté dans sa fiche (Étape 5bis).
- Le fichier Excel de l'Étape 2 et les deux fichiers de l'Étape 6 sont les livrables structurants : ne jamais se contenter d'une synthèse dans la conversation pour ceux-ci.
