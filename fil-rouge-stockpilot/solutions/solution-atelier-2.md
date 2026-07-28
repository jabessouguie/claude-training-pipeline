# Solution suggérée — Atelier 2 — De l'opportunité aux specs

> À lire **après** l'atelier, pour vérifier votre propre travail — pas un corrigé à consulter pendant l'exercice. L'objectif n'est pas de coller mot pour mot à ce qui suit, mais de vérifier que votre binôme a produit une matière du même calibre, avec les mêmes réflexes de contrôle.

## Ce que vous devriez avoir produit

L'atelier enchaîne trois gestes : **challenger** (Devil's Advocate), **cadrer** (mini-PRD, en particulier les non-objectifs), **spécifier** (US + Gherkin sous contrôle INVEST). Le fil conducteur à chaque étape : *l'IA produit la matière, vous produisez les décisions*.

**1. Devil's Advocate — des objections qui font mal, pas des remarques polies**

Un jeu d'objections solide ressemble à ceci (5 objections, sur les 5 angles demandés) :

1. *Adoption terrain* : « les équipes ne saisiront jamais les retours de matériel après une journée complète en magasin — votre inventaire sera faux en 3 semaines, comme les 2 tentatives Excel précédentes. »
2. *Réseau* : « une partie des réserves est en zone blanche — une app inutilisable sur place est une app morte. »
3. *Données initiales* : « votre stock de départ est faux (prêts informels, matériel fantôme) — vous digitalisez un mensonge. »
4. *Coût/bénéfice* : « le petit matériel coûte moins cher que le temps de gestion que vous ajoutez — pourquoi ne pas juste sur-équiper ? »
5. *Sécurité/RSSI* : « photos de magasin géolocalisées = données sensibles à encadrer. »

Vous deviez en retenir 3 et y répondre par écrit, de façon défendable — par exemple : mode hors-ligne avec synchronisation différée ; saisie réduite à 2 taps + photo (pas de formulaire) ; inventaire initial par campagne de scan avec les responsables logistique ; ROI chiffré sur les locations externes évitées (preuve corpus) ; cadrage données avec la DSI dès la V1.

**2. Mini-PRD — des non-objectifs qui sont vos choix**

Le premier jet vient de l'IA à partir de votre canevas amendé (Contexte · Objectif · Non-objectifs · Utilisateurs · Parcours clé · Critères de succès). Mais **les non-objectifs, vous les reformulez vous-mêmes**. Des non-objectifs typiques et défendables pour StockPilot V1 :

- Pas de géolocalisation IoT temps réel en V1 (c'est la V2 — lien avec la plateforme digitale du groupe).
- Pas de gestion du mobilier de rayonnage (processus et responsabilités différents).
- Pas d'intégration achat/location fournisseurs en V1.
- Pas de scoring individuel des utilisateurs (risque social).

**3. User stories — un exemple conforme INVEST, avec Gherkin complet (cas nominal + cas d'erreur)**

```text
En tant que responsable de magasin,
je veux voir en temps réel la disponibilité d'un type de matériel
sur les entrepôts et magasins à moins de 30 minutes,
afin de réserver au plus près et d'éviter une location externe.

Étant donné un transpalette électrique disponible à l'entrepôt de Rennes
Quand je recherche "transpalette" avec un rayon de 30 minutes
Alors je vois la liste triée par proximité avec le statut de chaque unité

Étant donné qu'aucune unité n'est disponible dans le rayon choisi
Quand je lance la recherche
Alors je vois les 3 prochaines dates de retour prévues
Et je peux créer une alerte de disponibilité
```

**4. Contrôle croisé — un verdict argumenté, dans un sens ou dans l'autre**

Une US recalée par le binôme relecteur n'est pas un échec : c'est un signal que la checklist INVEST a fait son travail. Un bon verdict de recalage cite un motif précis lié à INVEST (par exemple : « non testable : "interface intuitive" n'est pas un critère »), pas une impression générale.

## Guide de vérification — comparez votre réponse

| # | Question à se poser | Ce que vous devez voir si c'est réussi |
|---|---|---|
| 1 | Avez-vous une réponse **écrite** aux 3 objections retenues, et pourriez-vous la défendre devant votre hiérarchie sans relire vos notes ? | 3 réponses concrètes, chacune avec un début de solution ou d'arbitrage (pas juste « on va accompagner le changement ») |
| 2 | Vos non-objectifs contiennent-ils **au moins un** que l'IA n'avait pas proposé spontanément ? | Un non-objectif que vous pouvez justifier vous-même en une phrase, sans dire « c'est l'IA qui l'a suggéré » |
| 3 | Vos 3 US ont-elles chacune un rôle précis, une action et un bénéfice (pas « en tant qu'utilisateur, je veux une app simple ») ? | Un rôle métier identifiable (responsable de magasin, directeur régional...) et un bénéfice mesurable, pas une formulation vague |
| 4 | Chaque Gherkin couvre-t-il **au moins un cas nominal ET un cas d'erreur ou limite** ? | Au moins 2 blocs Étant donné/Quand/Alors par US, dont un qui traite un cas anormal (déjà réservé, hors réseau, taille dépassée...) |
| 5 | Avez-vous passé vos 3 US à la checklist INVEST vous-mêmes, avant l'échange ? | Une trace écrite (même informelle) de ce qui a été corrigé après relecture INVEST |
| 6 | Le binôme relecteur a-t-il déclaré **au moins 2** de vos US « prêtes pour l'équipe » ? | Un verdict par US, avec une raison si l'US est recalée — pas juste un « ok/pas ok » |

Si vous répondez « oui » aux 6 points, votre livrable est du calibre attendu.

## Ma réponse ne correspond pas — comment la corriger

**Vos objections sonnent poli, du genre « il faudra accompagner le changement »**
C'est le signe que le rôle donné à l'IA était trop vague. Une IA sans rôle incarné reste diplomate par défaut. Corrigez en redemandant avec un rôle dur et personnifié : « Tu es le directeur régional le plus réfractaire du réseau. Attaque mon projet StockPilot, sans concession. » ou « Tu es le DAF, tu détestes les projets IT qui ne prouvent pas leur ROI en 6 mois. » L'objection s'incarne et devient exploitable.

**Vos non-objectifs sont ceux que l'IA a proposés, mot pour mot**
Demandez-vous : « lequel est LE MIEN ? » Si vous ne pouvez pas répondre, c'est que la décision a été déléguée à l'IA — exactement l'anti-pattern que cet atelier veut vous faire repérer. Ce n'est pas grave en soi, mais corrigez-le maintenant : reprenez la liste de non-objectifs proposée, et pour au moins un, changez-le, durcissez-le ou ajoutez-en un que l'IA n'a pas vu (par exemple un choix strictement politique ou budgétaire que seul un PO qui connaît le terrain peut trancher).

**Vos US se ressemblent toutes et pourraient s'appliquer à n'importe quelle app**
Passez-les à la grille INVEST : elles échoueront presque systématiquement sur **Testable** (rien à vérifier concrètement) et **Small** (trop large, plusieurs fonctionnalités mélangées). La cause : un rôle générique (« en tant qu'utilisateur ») et un bénéfice non mesurable (« je veux une app simple »). Corrigez en redemandant à l'IA un rôle métier précis (responsable de magasin, magasinier, directeur régional) et un bénéfice quantifiable ou observable (« afin d'éviter une location externe », « afin de retrouver l'historique en moins de 10 secondes »).

**Vos scénarios Gherkin ne couvrent que le chemin heureux**
Un Gherkin uniquement nominal (« l'utilisateur cherche, ça marche ») est incomplet — c'est justement le genre de spec qui produit du code fragile en spec-driven development. Corrigez en demandant explicitement à l'IA : « génère aussi les cas d'erreur et les cas limites » — et en creusant vous-même : « Étant donné un équipement déjà réservé... », « Quand la photo dépasse la taille maximale... », « Étant donné une connexion hors réseau... ».

**Vous êtes repartis de zéro au lieu de réutiliser le canevas de l'atelier 1**
Si votre mini-PRD ne fait référence à aucun élément de votre canevas d'opportunité (pain points, personas, preuves), c'est un signal de rupture du fil rouge — vous avez perdu le lien entre le problème identifié et la solution spécifiée, et probablement du temps. Corrigez en relisant votre canevas d'opportunité avant de continuer, et en demandant à l'IA de reformuler le mini-PRD en s'appuyant explicitement sur les preuves et personas déjà identifiés.

**Le binôme relecteur a validé toutes vos US sans réserve, ou au contraire toutes recalées sans motif clair**
Une validation ou un rejet en bloc, sans justification précise par critère INVEST, n'est pas un vrai contrôle croisé — c'est un coup de tampon. Reprenez l'échange en demandant au binôme relecteur de citer, pour chaque US recalée, le critère INVEST précis qui échoue (« non testable », « pas Small », « pas Independent »...). Si le retour reste vague, redemandez-le : c'est cette précision qui fait progresser la qualité collective de vos specs.

## Pour aller plus loin

Question à vous poser (seul ou en débrief) : *votre US part chez un développeur qui la donne à un agent de codage. Qu'est-ce qui, dans votre Gherkin, va produire du mauvais code si c'est ambigu ?*

Réponse attendue : ce sont les termes non définis — « à proximité », « rapidement », « simple » — qui deviennent des choix arbitraires de la machine. En spec-driven development, l'ambiguïté ne coûte plus une question posée en daily à un collègue : elle coûte directement une implémentation fausse, livrée telle quelle. Plus votre Gherkin est précis et quantifié, moins vous laissez de place à l'improvisation de l'IA qui code à votre place.
