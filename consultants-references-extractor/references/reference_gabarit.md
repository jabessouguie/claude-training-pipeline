# Gabarit — Fiche référence / mission

Ce gabarit est une **structure vide**. À l'Étape 2/4/5 de `consultants-references-extractor/SKILL.md`, il est recopié et rempli avec les seules informations réellement observées dans les documents sources — chaque champ non observable reste `NON DÉTERMINÉ`, jamais deviné.

Fichier produit : `references-missions/<client-objet>.md` (dossier de premier niveau, à côté de `formations/`/`appels-offres/`/`consultants/`/`design-systems/` — jamais à la racine du dépôt, jamais versionné).

```markdown
# Référence — <Intitulé de la mission>

*Identifiant : <client-objet>*
*Dernière extraction automatique : <date> (source : <document(s) d'origine>)*
*Dernière modification manuelle : <date, ou "aucune">*

## Confidentialité
- Niveau : NOMMÉE | ANONYMISÉE | INTERNE_UNIQUEMENT | NON PRÉCISÉ
- Mention trouvée dans la source : « <texte exact, ou "aucune mention trouvée"> »
- **Rappel** : ce niveau documente ce qui a été trouvé à l'extraction — il n'autorise jamais, à lui seul, un usage externe. Toute inclusion dans un livrable envoyé à un client exige une confirmation humaine explicite au moment de la sélection (voir `reponse-appel-offres/SKILL.md`), quel que soit le niveau ci-dessus.

## Client
- Nom : <valeur, ou "non citable — niveau ANONYMISÉE/INTERNE_UNIQUEMENT">
- Secteur : <valeur ou NON DÉTERMINÉ>

## Contexte et enjeux
<texte fidèle à la source>

## Notre approche
<texte fidèle à la source>

## Valeur ajoutée / résultats
<texte, avec résultats chiffrés si mentionnés dans la source>

## Détails complémentaires
- Durée de la mission : <valeur ou NON DÉTERMINÉ>
- Taille d'équipe mobilisée : <valeur ou NON DÉTERMINÉ>
- Technologies / méthodologies utilisées : <valeur ou NON DÉTERMINÉ>

## Consultants ayant contribué
- `consultants/<identifiant-consultant>.md` — <rôle sur cette mission>
```

## Règles de remplissage (rappel pour l'agent qui exécute l'extraction)

- La détection de confidentialité s'interprète en contexte (le format varie d'un document à l'autre) — jamais un mot-clé unique attendu.
- Une absence de mention de confidentialité se classe `NON PRÉCISÉ`, jamais interprétée comme une autorisation implicite.
- Un champ non observable dans les documents sources reste `NON DÉTERMINÉ`, jamais complété par une valeur plausible.
