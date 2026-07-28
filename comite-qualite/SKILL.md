---
name: comite-qualite
description: Lance un audit multi-relecteurs sur n'importe quel type de livrable (docx, xlsx, pptx, md, py, html, formation, offre, spec, rapport…). Analyse d'abord le livrable et le contexte projet pour composer dynamiquement l'équipe de relecteurs la plus pertinente (3 à 6 membres, rôles et compétences sur mesure), la soumet à validation, puis lance la boucle d'audit jusqu'à convergence sincère. Deux modes : (a) loop de convergence — applique les corrections en place ; (b) annotations — liste de paires zone/commentaire pour édition externe. Déclenche cette skill quand l'utilisateur demande "passe X dans le comité qualité", "audit multi-relecteurs", "fais l'audit de…", "comité qualité", "relecture qualité", ou tout équivalent d'un audit cabinet sur livrable.
---

# Comité Qualité — audit multi-relecteurs à équipe dynamique

Compose une équipe de relecteurs sur mesure à partir du livrable et du contexte, puis audite sans complaisance jusqu'à convergence sincère.

---

## Phase 0 — Analyse du livrable et constitution de l'équipe

### 0.0 — Clarifier le périmètre d'audit

Avant de caractériser le livrable, si la cible n'est pas déjà sans ambiguïté (ex. un seul fichier explicitement désigné), demander :

```
Quel périmètre dois-je auditer ?
- Le contenu markdown (slides.md, notes-formateur.md, enonce-atelier-N.md, solution-atelier-N.md, ou exercices.md en mode alternatif sans fil rouge…)
- La présentation générée (le rendu visuel final, ex. dans Claude Design)
- Les deux
```

Ne pas supposer que « auditer la formation » signifie auditer uniquement le markdown ou uniquement le rendu visuel — les deux couvrent des défauts différents (cohérence de contenu vs respect de charte/lisibilité visuelle) et l'utilisateur doit trancher explicitement. Le rapport final (Phase D et Sortie attendue) rappelle systématiquement quel périmètre a été couvert.

### 0.1 — Lire et caractériser le livrable

Avant de constituer l'équipe, extraire les 4 dimensions du livrable :

| Dimension | Ce qu'on cherche |
|---|---|
| **Type formel** | Extension + structure (slides, document narratif, tableur, code, dashboard, formation, offre…) |
| **Domaine / secteur** | Formation, conseil stratégique, tech/IT, RH, finance, juridique, santé, marketing, réglementaire… |
| **Audience cible** | Qui va lire/utiliser ce livrable ? (direction client, stagiaires, développeurs, jury, grand public…) |
| **Enjeux et usage** | Présentation décisionnelle, livrable contractuel, support pédagogique, documentation interne, publication… |

### 0.2 — Composer l'équipe

À partir des 4 dimensions, sélectionner **3 à 6 relecteurs** selon les règles suivantes :

**Rôles invariants (toujours présents, 1 suffit si recouvrement) :**
- **Cohérence & structure** — quelqu'un qui vérifie le fil conducteur, la logique interne, l'absence de contradictions
- **Expert domaine** — quelqu'un qui valide l'exactitude technique/méthodologique du contenu

**Rôles conditionnels (à inclure si la dimension est présente) :**

| Condition | Rôle à ajouter | Compétence clé |
|---|---|---|
| Audience = direction / client / jury | Directeur de mission / Senior Partner | Valeur perçue, risques d'exposition, alignement enjeux client |
| Format visuel (pptx, dashboard, html) | UX / Directeur artistique | Hiérarchie visuelle, charte, lisibilité, 60-30-10 |
| Livrable pédagogique (formation, cours, e-learning) | Expert pédagogique | Taxonomie de Bloom, progression, ancrage, ateliers |
| Dimension réglementaire / légale / contractuelle | Expert juridique / Conformité | Exactitude, couverture des risques, langage précis |
| Dimension financière / chiffrage | Directeur financier / Analyste | Cohérence des chiffres, hypothèses, risques |
| Code destiné à être livré / lu par humains | Tech writer / Architecte | Lisibilité, structure, commentaires, conventions |
| Public opérationnel terrain | Manager opérationnel / Praticien | Faisabilité réelle, langage métier, manques pratiques |
| Inter-livrables (dossier complet) | Directeur qualité | Cohérence terminologique, synchronisation chiffres, charte |
| Notes d'entretien/cadrage disponibles avec un interlocuteur identifié (ex. sponsor, client) | Voix du client | Fidélité du contenu produit à ce que l'interlocuteur a exprimé en entretien — vérifie que le livrable répond aux attentes réellement formulées, pas à une interprétation générique |

**Règles de composition :**
- Minimum 3 relecteurs. Maximum 6 (au-delà, recouvrement parasite).
- Chaque relecteur a un angle principal distinct — pas de doublon.
- Les titres des relecteurs doivent résonner avec le domaine du livrable (pas "Manager" générique, mais "Directeur pédagogique", "Architecte solution", "Directeur commercial"…).
- Si un seul relecteur couvre naturellement deux rôles conditionnels, les fusionner.

**Rôle "Voix du client" — garde-fou** : ce rôle ne s'active que si des notes d'entretien ou de cadrage réelles sont disponibles (ex. `00-brief.md`, transcript de réunion, grille de cadrage remplie par `cadrage-formation`). Ne jamais inventer une personnalité ou des attentes à partir de peu d'éléments — si les notes disponibles sont trop minces pour caractériser un point de vue distinct, ne pas inclure ce rôle plutôt que de le fabriquer artificiellement.

### 0.3 — Présenter l'équipe et attendre confirmation

Afficher :

```
🔍 Analyse du livrable : [nom du fichier ou description]

Type      : [type formel]
Domaine   : [secteur/contexte]
Audience  : [cible]
Usage     : [ce à quoi sert ce livrable]

👥 Équipe proposée pour ce comité qualité :

| # | Relecteur | Angle principal | Pourquoi sur ce livrable |
|---|-----------|----------------|--------------------------|
| 1 | [Titre]   | [angle]        | [justification courte]   |
| 2 | [Titre]   | [angle]        | ...                      |
...

Mode : [Loop / Annotations]

Confirmez-vous cette équipe, ou souhaitez-vous ajuster un rôle ?
```

Ne pas démarrer l'audit avant confirmation explicite (« oui », « go », « c'est bon », ou liste d'ajustements).

---

## Phase 1 — Audit multi-relecteurs

### Phase A — Constats par relecteur

Chaque relecteur produit ses constats selon son angle et ses questions clés.

Les questions sont **générées dynamiquement** à partir du profil du relecteur et des dimensions du livrable. Elles ne sont pas figées — elles découlent de la logique suivante :

**Pour chaque relecteur, poser :**
1. *Est-ce que le livrable remplit sa mission principale vis-à-vis de son audience ?*
2. *Y a-t-il des erreurs ou lacunes dans mon domaine d'expertise ?*
3. *Qu'est-ce qu'un lecteur exigeant dans mon rôle reprocherait immédiatement ?*
4. *Qu'est-ce qui est absent et qui devrait y être ?*
5. *Qu'est-ce qui est présent mais devrait être supprimé ou reformulé ?*

**Questions systématiques par type de livrable :**

| Type | Questions supplémentaires |
|---|---|
| Slides / pptx | 1 idée par slide ? Titre = phrase-message ? Max 5 éléments accentués ? Charte respectée ? |
| Document narratif / docx | Hiérarchie H1/H2/H3 ? Longueur de ligne (70-90 car.) ? Gestion veuves/orphelines ? |
| Tableur / xlsx | En-têtes figés et en gras ? Formules documentées ? Pas de valeurs hardcodées silencieuses ? |
| Formation / pédagogie | Objectifs SMART ? Progression Bloom ? Ateliers ancrés dans le réel ? Timing réaliste ? |
| Code (livrable) | Lisibilité humaine ? Commentaires de section ? Organisation visuelle ? Pas de murs denses ? |
| Offre commerciale | Valeur différenciante visible dès la page 2 ? Chiffrage cohérent ? Risques couverts ? |
| Rapport réglementaire | Références exactes ? Périmètre d'applicabilité clair ? Recommandations actionnables ? |
| Dashboard | Hiérarchie des KPIs ? Lisibilité à distance ? Source et date des données visibles ? |
| Markdown | Échappements résiduels absents (`\_ \~ \& \) \.`) ? Cross-références exactes ? |

Chaque relecteur travaille **sans complaisance** mais aussi **sans inventer de problèmes**.

### Phase B — Synthèse des corrections

Liste numérotée, classée par priorité :

- 🔴 **Bloquant** : erreur factuelle, incohérence majeure, contre-sens, contradiction. Un lecteur exigeant refuserait ou perdrait confiance.
- 🟠 **Important** : manque de clarté, lacune, incohérence inter-livrable. Un lecteur attentif tique.
- 🟡 **Mineur** : forme, formulation, homogénéité. Invisible pour 90 % des lecteurs.

Format :
```
[N°] [PRIORITÉ] [RELECTEUR] — [localisation précise]
Problème : ...
Correction attendue : ...
```

### Phase C — Application (mode loop)

**Si la synthèse (Phase B) contient au moins un 🔴 bloquant**, marquer une pause avant d'appliquer : afficher la liste complète (Phase B) puis "Ces corrections vont être appliquées, dont [N] bloquantes qui peuvent réécrire des passages entiers — je continue, ou tu veux d'abord ajuster la liste ?" Ne pas bloquer en boucle : une réponse implicite de poursuite (l'utilisateur qui relance ou ne réagit pas dans le fil) vaut confirmation, ce n'est pas une porte à répéter à chaque itération de convergence. **S'il n'y a que du 🟠/🟡**, enchaîner directement sans pause — la friction n'est justifiée que pour les corrections lourdes.

Appliquer **toutes** les corrections, dans l'ordre 🔴 → 🟠 → 🟡.
Indiquer pour chacune : `✅ Correction [N°] appliquée`.

### Phase D — Vérification de convergence

Relancer un audit complet (retour Phase A).

**Critère d'arrêt** : tous les relecteurs produisent `Aucune correction`.

Afficher alors :
```
✅ LIVRABLE VALIDÉ — Itération [N]
Aucune correction identifiée par les [N] relecteurs.
Ce livrable est prêt pour [usage identifié en Phase 0].
Périmètre audité : [markdown / présentation générée / les deux — cf. 0.0]

Prochaine étape possible : [ex. "diffuser au client", "passer à la génération des slides dans Claude Design",
selon ce qui a été audité et ce qu'il reste à faire dans le pipeline]. Veux-tu que je t'aide sur ce point ?
```

---

## Mode annotations

Quand l'utilisateur édite le livrable ailleurs (Google Docs, Word avec suivi, copy-paste manuel), produire **une liste structurée** au lieu d'appliquer des corrections :

```
### 🔴/🟠/🟡 [N°] Titre court de l'item
Zone à surligner : "extrait exact du document — copié-collé sans paraphraser"
Commentaire à mettre : "rédigé prêt à coller dans la marge, ton consulting, concis, actionnable"
```

Règles du mode annotations :
- L'extrait à surligner doit être un **copié-collé fidèle**, pas une paraphrase.
- Le commentaire doit être **autoporteur** et **rédigé** (pas en télégraphe).
- Pour tableurs : pointer la cellule ou plage précisément (ex. `R12C7`).
- Pour slides ouvertes ailleurs : pointer le numéro et le titre du slide.
- Pour longs documents : regrouper par section.

Déclenchement : « annotations », « pour coller en commentaires », « j'édite dans Google Docs », « zone à surligner ».

---

## Cohérence inter-livrables (si dossier)

Quand la cible est un dossier de livrables :
1. Auditer chaque fichier individuellement.
2. Ajouter une revue transverse :
   - **Terminologie homogène** entre tous les livrables (un même rôle/concept ne doit pas avoir deux noms).
   - **Références croisées** correctes (les fichiers cités existent, noms exacts).
   - **Synchronisation des chiffres** (dates, FTE, périmètres, indicateurs identiques partout).
   - **Charte** appliquée à tous les visuels.
   - **Cohérence de niveau** (pas un livrable très détaillé à côté d'un autre superficiel sur le même sujet).

Inclure un rôle **Directeur qualité inter-livrables** dans l'équipe si la cible est un dossier.

---

## Règles d'honnêteté (anti-théâtre)

1. **Ne pas inventer de problèmes** pour justifier la boucle. Si les relecteurs ne trouvent rien après examen rigoureux, déclarer la convergence à l'itération 1.

2. **Différencier défaut et préférence.** Un défaut a un impact mesurable. Une préférence n'en a pas — ne pas la remonter comme correction.

3. **Matcher la sévérité à l'impact réel** :
   - 🔴 = un lecteur exigeant refuse ou perd confiance.
   - 🟠 = un lecteur attentif tique mais avance.
   - 🟡 = invisible pour 90 % des lecteurs.

4. **Idempotence** : un livrable repassé après convergence doit ressortir avec zéro retour.

5. **Cross-livrable** : une incohérence avec un livrable validé est un finding 🔴 ou 🟠 selon l'impact.

6. **Charte** : si un fichier de charte existe (`theme/*.json`, `charter.*`, `brand.*`), valider l'alignement systématiquement.

7. **Pas plus de 3 itérations consécutives** sans changement structurel. Si la 3ᵉ itération ne porte plus que sur des préférences, déclarer la convergence et expliquer pourquoi.

---

## Anti-patterns à éviter

- Empiler des corrections cosmétiques pour gonfler la liste.
- Citer trop souvent la nomenclature du protocole au lieu de produire la valeur.
- Ne corriger que pour relever d'autres défauts à l'itération suivante (cycle artificiel).
- Imposer des préférences de style sans rapport avec l'efficacité audience.
- Réécrire le livrable quand quelques retouches suffisent.
- Faire passer des contradictions inter-livrables comme « préférences ».
- Proposer une équipe trop large (>6) qui génère des recouvrements et du bruit.
- Garder des titres de relecteurs génériques quand le domaine permet d'être précis.

---

## Sortie attendue

**Mode loop** : livrable mis à jour + résumé des corrections appliquées par itération + message final actionnable.

**Mode annotations** : liste structurée prête à coller dans l'outil d'édition cible + indication de ce qui reste à faire + proposition de prochaine étape une fois les annotations traitées par l'utilisateur (ex. "une fois ces annotations reportées dans le document, relance-moi pour un nouveau tour d'audit ou pour passer à l'étape suivante du pipeline").

Dans les deux cas, le message final rappelle explicitement : le **périmètre audité** (cf. 0.0), et dit *ce livrable est prêt pour [usage] / voici ce qu'il reste à faire avant de l'envoyer à [audience]*, en proposant la suite logique du pipeline plutôt que de laisser l'utilisateur deviner.
