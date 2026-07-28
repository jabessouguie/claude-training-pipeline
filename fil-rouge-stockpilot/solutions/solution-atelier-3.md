# Solution suggérée — Atelier 3 — Votre premier prototype cliquable

> Ce document est fait pour être consulté **après** l'atelier, pour comparer votre résultat au vôtre — pas pendant l'exercice. Il n'y a pas une seule "bonne" version : votre prototype doit refléter VOS choix de mini-PRD, pas recopier ce qui suit.

## Ce que vous devriez avoir produit

Un fichier `stockpilot.html` unique (HTML + CSS + JavaScript dans le même fichier, aucune dépendance externe) qui s'ouvre directement dans un navigateur et propose **3 écrans navigables par de vrais clics** :

1. **Recherche** : champ de recherche + filtres (type de matériel, distance) + liste de résultats avec un statut coloré (Disponible / Réservé / En panne).
2. **Fiche équipement** : photo (même en placeholder), localisation actuelle, statut, historique des 3 dernières utilisations, bouton "Réserver".
3. **Réservation** : dates début/fin, magasin de destination, récapitulatif, confirmation.

Avec des données d'exemple réalistes et cohérentes avec le vocabulaire retail (transpalettes électriques, scanners d'inventaire, chariots de réassort, bacs de manutention roulants…), réparties entre un entrepôt et plusieurs magasins.

**Résultat attendu en volume** : un fichier de l'ordre de 200 à 400 lignes. Un design basique est tout à fait normal et même souhaitable ici — l'objectif de l'atelier est de déclencher une conversation produit avec le métier, pas de produire une maquette esthétique.

Pour info, voici le type de prompt de génération qui produit ce résultat (utile si vous voulez comparer votre propre prompt, pas à copier après coup) :

```text
Tu es développeur front-end senior. Génère un prototype d'application
web pour la gestion du petit matériel réutilisable de magasin, destiné
à une démo auprès d'équipes retail.

Contraintes techniques :
- UN SEUL fichier HTML complet : CSS et JavaScript inclus dedans,
  aucune dépendance externe, aucun lien vers internet
- Fonctionne en ouvrant simplement le fichier dans un navigateur
- Design sobre et professionnel, adapté à une consultation mobile

3 écrans navigables entre eux :
1. RECHERCHE : champ de recherche + filtres (type de matériel,
   distance) + liste de résultats avec statut coloré
   (Disponible / Réservé / En panne)
2. FICHE ÉQUIPEMENT : photo (placeholder), localisation actuelle,
   statut, historique des 3 dernières utilisations, bouton Réserver
3. RÉSERVATION : dates début/fin, magasin de destination,
   récapitulatif, confirmation

Données d'exemple réalistes : transpalettes électriques, scanners
d'inventaire, chariots de réassort, bacs de manutention roulants —
répartis entre entrepôt de Rennes et 3 magasins.

Voici le PRD pour contexte : [coller le mini-PRD]
```

Deux exemples d'itérations qui répondent bien aux consignes de l'atelier (une amélioration visuelle/libellé, un cas d'erreur) :

- « Remplace le vocabulaire informatique par du vocabulaire magasin : "Matériel" pas "Assets", "Entrepôt" pas "Localisation par défaut" »
- « Quand un matériel est déjà réservé sur les dates choisies, affiche les 3 prochaines périodes libres et propose une alerte »
- « Les statuts en pastilles de couleur : vert disponible, orange réservé, rouge en panne »

## Guide de vérification — comparez votre réponse

| Critère de réussite | Question à vous poser | Ce que vous devez voir si c'est réussi |
|---|---|---|
| Fichier fonctionnel | Votre fichier `stockpilot.html` s'ouvre-t-il dans le navigateur (et pas comme du texte brut) ? | Une vraie page web avec mise en forme, pas du texte HTML affiché tel quel |
| Navigation réelle | Les 3 écrans (recherche, fiche équipement, réservation) s'enchaînent-ils par de **vrais clics** ? | Vous cliquez sur un résultat de recherche → vous atterrissez sur sa fiche ; vous cliquez sur "Réserver" → vous atterrissez sur l'écran de réservation |
| Itérations réalisées | Avez-vous fait au moins 2 itérations, dont une amélioration visuelle/libellé ET un cas d'erreur visible dans le prototype ? | Le cas d'erreur se déclenche réellement (ex : réserver un matériel déjà pris affiche bien une alternative) — pas juste décrit dans le prompt |
| Fidélité à votre PRD | Le prototype reflète-t-il VOS choix du matin (vocabulaire métier, périmètre V1, non-objectifs respectés) ? | Si vous aviez exclu la géolocalisation temps réel, elle n'apparaît pas ; le vocabulaire est celui de votre PRD, pas un vocabulaire générique |
| Compréhensible sans vous | En démo croisée, un autre binôme a-t-il compris le parcours sans que vous l'expliquiez ? | L'autre binôme retrouve seul le chemin recherche → fiche → réservation |
| Rendu mobile testé | Avez-vous testé le mode responsive (F12 ou réduction de fenêtre) et noté ce qui casse ? | Vous avez une liste concrète (même courte) d'éléments qui débordent ou se chevauchent en format téléphone |

## Ma réponse ne correspond pas — comment la corriger

**Vous obtenez du texte au lieu d'une app qui s'ouvre correctement**
→ Le fichier a probablement été enregistré en `.html.txt` au lieu de `.html` : le navigateur affiche alors le code source au lieu de l'exécuter. Vérifiez l'extension dans l'explorateur de fichiers (activez l'affichage des extensions si besoin). Corrigez en ré-enregistrant depuis le Bloc-notes avec "Type : Tous les fichiers", pour éviter que `.html` ne devienne `.html.txt` par défaut.

**Le code généré s'arrête en plein milieu, le prototype est incomplet**
→ La réponse de l'IA a été tronquée par une limite de longueur. Ce n'est pas une erreur de votre part, c'est mécanique. Corrigez en redemandant « continue exactement où tu t'es arrêté, sans rien répéter », puis recollez bout à bout — ou repartez en générant écran par écran (« donne-moi d'abord uniquement l'écran de recherche »), une approche plus robuste si vous subissez plusieurs troncatures d'affilée.

**Une itération a cassé tout le prototype**
→ C'est le piège le plus fréquent de cet atelier : l'IA a répondu avec seulement le fragment modifié, et ce fragment a remplacé l'intégralité du fichier au lieu de s'y insérer. Corrigez en demandant systématiquement « redonne-moi le fichier COMPLET incluant la modification ». En dernier recours, repartez de `prototype-fallback.html` (disponible dans `assets/fil-rouge-stockpilot/atelier-3/`) et itérez dessus.

**Vous avez passé la majorité du temps sur l'esthétique (couleurs, mise en page) et aucun cas d'erreur n'est visible dans le prototype**
→ C'est la dérive la plus tentante mais elle vous fait rater l'objectif pédagogique de l'itération obligatoire (b). Revenez aux critères de réussite : un cas d'erreur visible et cliquable (ex : matériel déjà réservé → affichage des prochaines disponibilités) est obligatoire, une itération purement visuelle ne suffit pas.

**Le prototype ne ressemble pas du tout à vos choix du matin (vocabulaire générique, périmètre différent de votre mini-PRD)**
→ Vous avez probablement re-décrit le besoin de zéro dans le prompt de génération, au lieu de coller votre mini-PRD complet comme contexte. Corrigez en régénérant (ou en itérant fortement) avec votre mini-PRD réellement collé dans le prompt — le prototype doit incarner vos décisions, pas une interprétation générique du sujet "gestion de matériel".

**Le mode responsive (F12) ne s'active pas sur votre poste**
→ Les outils de développement sont probablement désactivés par une politique de sécurité du poste (GPO), c'est fréquent et sans rapport avec votre prototype. Contournez simplement en réduisant la largeur de la fenêtre du navigateur au format téléphone : le prototype étant responsive, l'effet observé est identique à celui du mode responsive.

**Votre tableau de résultats ou vos données d'exemple sont peu réalistes ou peu nombreuses**
→ Le prompt de génération n'imposait probablement pas assez de contraintes de contenu. Corrigez en redemandant explicitement des données réalistes et variées (types de matériel, statuts différents, plusieurs sites/magasins) plutôt qu'un jeu de données minimal générique.

## Pour aller plus loin

Question à vous poser maintenant que le prototype existe : **ce prototype part en réunion métier demain et le responsable logistique dit "parfait, on le met en prod quand ?" — que répondez-vous ?**

Réponse attendue : ce prototype est jetable, pas un livrable de production. La mise en production passera par l'équipe de développement et la chaîne d'outils habituelle. Le prototype devient une **annexe** de la spécification remise aux développeurs — un support de conversation et d'alignement métier, pas le code qui sera réellement déployé.
