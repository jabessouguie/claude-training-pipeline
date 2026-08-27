# Gabarit — Fiche consultant

Ce gabarit est une **structure vide**. À l'Étape 1/4/5 de `consultants-references-extractor/SKILL.md`, il est recopié et rempli avec les seules informations réellement observées dans les documents sources — chaque champ non observable reste `NON DÉTERMINÉ`, jamais deviné.

Fichier produit : `consultants/<prenom-nom>.md` (dossier de premier niveau, à côté de `formations/`/`appels-offres/`/`references-missions/`/`design-systems/` — jamais à la racine du dépôt, jamais versionné).

```markdown
# Consultant — <Prénom Nom>

*Identifiant : <prenom-nom>*
*Dernière extraction automatique : <date> (source : <document(s) d'origine>)*
*Dernière modification manuelle : <date, ou "aucune">*

## Informations générales
- Poste / séniorité actuels : <valeur ou NON DÉTERMINÉ>
- Langues : <valeur ou NON DÉTERMINÉ>
- Certifications : <valeur ou NON DÉTERMINÉ>
- Disponibilité : <valeur ou NON DÉTERMINÉ>

## Compétences
- <compétence> (source : tag explicite)
- <compétence> (source : déduite de la mission <identifiant-référence>)

## Missions

### <Intitulé de la mission> (réf. `references-missions/<identifiant-référence>.md`)
- Période / durée : <valeur ou NON DÉTERMINÉ>
- Rôle sur cette mission : <valeur>
- Description : <texte fidèle à la source>
- Résultats chiffrés : <valeur ou NON DÉTERMINÉ>
- Compétences mobilisées : <liste>

<— une sous-section « ### » par mission, jamais fusionnées en un résumé de carrière —>
```

## Règles de remplissage (rappel pour l'agent qui exécute l'extraction)

- Un consultant peut apparaître sur plusieurs slides/documents sources, chacun avec une mission différente — regrouper sous une seule fiche via l'identifiant stable, jamais une fiche par slide.
- En cas d'homonymie apparente avec un consultant déjà présent dans le référentiel, ne jamais fusionner automatiquement — comparer un second signal (poste, mission déjà connue) et signaler pour arbitrage humain en cas de doute réel.
- Un champ non observable dans les documents sources reste `NON DÉTERMINÉ`, jamais complété par une valeur plausible.
