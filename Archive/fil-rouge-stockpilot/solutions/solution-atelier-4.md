# Solution suggérée — Atelier 4 — Lancement simulé

> Ce document est fait pour être lu **après** l'atelier, pour vous auto-évaluer. Si vous le consultez pendant l'exercice, vous vous privez de l'apprentissage principal : apprendre à lire des métriques ambivalentes et trancher vous-même.

## Ce que vous devriez avoir produit

À l'issue des 35 minutes de travail, vous devriez avoir quatre livrables :

**1. Les assets de lancement**
- Une annonce interne de généralisation d'environ 200 mots, sans jargon IT, avec un ton adapté au terrain (registre magasin, pas registre informatique — ex. « fini les appels pour trouver un transpalette » plutôt que « optimisation de la disponibilité des assets »).
- Une FAQ support de 5 questions (3 si vous étiez en retard) qui n'annonce **aucune fonctionnalité hors périmètre V1** — en particulier, si la géolocalisation temps réel ou la gestion du mobilier de rayonnage étaient dans vos non-objectifs de l'exercice 2, la FAQ ne doit pas les mentionner comme disponibles.

**2. Le marché synthétique**
Au moins **5 objections distinctes**, collectées en faisant réagir 3 personas (dont un franchement réfractaire) à votre annonce, avec la question systématique : « qu'est-ce qui ferait que tu n'utilises JAMAIS cet outil ? »

Des objections de bonne qualité ressemblent à :
- « Encore une app qui marchera pas sans réseau »
- « Qui met à jour quand une collègue prend le matériel sans passer par l'app ? »
- « Je signale une panne et après on me demande 3 formulaires »
- « Ça va servir à fliquer qui perd le matériel »

Les deux dernières touchent à la friction de saisie et à la défiance vis-à-vis du contrôle — ce sont typiquement celles qu'on n'anticipe pas avant de les avoir entendues.

**3. La lecture des métriques**
Un tableau structuré (signal | donnée source citée | pourquoi c'est préoccupant/encourageant | hypothèse d'explication), construit à partir du fichier `metriques-j30-stockpilot.md` et de vos objections simulées, avec :
- les 3 signaux les plus préoccupants
- les 3 signaux les plus encourageants
- chaque signal relié à un chiffre exact du fichier (pas d'approximation)

Les signaux **encourageants** que vous devriez retrouver : doubles réservations en baisse de 70 %, locations externes en baisse de 18 % (~775 €/mois économisés sur le pilote), responsables de magasin à 62 % d'actifs hebdomadaires avec 55 % de rétention J+30, 340 réservations en 30 jours.

Les signaux **préoccupants** que vous devriez retrouver : directeurs régionaux à seulement 28 % d'actifs hebdomadaires en semaine 4 et 12 % de rétention J+30 (en chute), seulement 9 signalements de panne en 30 jours (contre ~30 attendus), 8 % du parc « introuvable » dans l'app, verbatims sur la saisie pénible et les lenteurs en réseau magasin, NPS pilote à +12 (tiède).

**4. La décision**
Un **steelman des deux options** rédigé avant de trancher (le meilleur argumentaire pour Persevere, puis le meilleur pour Pivot), suivi de votre décision en 5 lignes maximum, citant au moins 3 données précises, avec une prochaine étape concrète.

La lecture experte attendue ici : la moyenne globale masque une réalité par segment — le produit **réussit** auprès des responsables de magasin (usage planification/back-office) et **échoue** auprès des directeurs régionaux (usage terrain, mobilité, réseau faible). Deux décisions sont défendables sur ces données :
- **Persevere corrigé** : la valeur économique est prouvée (−18 % de locations externes) ; on corrige la friction terrain (signalement en 2 taps + photo, mode hors-ligne, moins de notifications) et on re-mesure à J+60.
- **Pivot de segment/parcours** : on recentre la V1 sur responsables de magasin + responsables logistique (là où ça marche), et on repense de zéro le parcours directeur régional (QR code sur le matériel, zéro saisie).

« Arrêter le projet » n'est en revanche pas défendable sur ce fichier : la valeur économique est démontrée par les −18 % de locations externes.

## Guide de vérification — comparez votre réponse

| Critère de réussite | Question à vous poser | Ce que vous devez voir si c'est bon |
|---|---|---|
| Cohérence annonce ↔ FAQ ↔ non-objectifs | Ai-je relu mes non-objectifs de l'exercice 2 avant de valider l'annonce et la FAQ ? Une promesse hors périmètre V1 s'est-elle glissée quelque part ? | Aucune mention de fonctionnalité exclue (ex. géolocalisation temps réel) dans l'annonce ou la FAQ. |
| Richesse du marché synthétique | Ai-je bien 5 objections distinctes (pas 5 reformulations de la même idée) ? Au moins 2 me surprennent-elles vraiment ? | Une liste d'objections concrètes et variées, dont au moins 2 que vous n'auriez pas devinées seul(e) avant l'exercice. |
| Rigueur de la lecture des métriques | Chaque signal que j'ai retenu est-il accolé à un chiffre exact du fichier ? Ai-je vérifié au moins 2 de ces chiffres en rouvrant le fichier ? | Un tableau signal/donnée/raison où chaque ligne pointe vers un chiffre vérifiable, pas une impression générale. |
| Autonomie de la décision | Ma décision finale est-elle écrite par moi, ou est-ce une reformulation de ce que l'IA a suggéré quand je lui ai demandé son avis ? | Une décision en 5 lignes, avec au moins 3 données citées, que vous pouvez défendre à l'oral sans revenir au chat IA. |

## Ma réponse ne correspond pas — comment la corriger

**Vos personas disent tous que c'est génial, zéro friction remontée.**
Symptôme : votre liste d'objections est courte, vague, ou consensuelle (« c'est une bonne idée mais peut-être un peu cher »). Cause : c'est de la sycophancie — l'IA a tendance à faire plaisir, y compris quand vous lui demandez de jouer un persona hostile. Correction : durcissez le rôle explicitement (âge, vécu d'échecs avec d'autres outils, contrainte de temps réelle — « tu as 20 ans de terrain, les apps précédentes t'ont toutes déçu, tu n'as pas de temps à perdre ») et posez des questions fermées orientées friction plutôt qu'ouvertes : « qu'est-ce qui t'agace dans cette annonce ? », « à quel moment précis tu décroches et tu arrêtes de lire ? ». Ne demandez pas « qu'en penses-tu ? », demandez ce qui coince.

**Votre tableau de synthèse des métriques reste flou, du style « globalement mitigé » sans chiffres.**
Symptôme : vous ne pouvez pas répondre en 5 secondes à « où est ce chiffre dans le fichier ? » pour chacune de vos lignes. Cause : vous n'avez probablement pas imposé de format précis dans votre prompt, ou vous avez laissé l'IA résumer « à sa façon ». Correction : redemandez explicitement le format tableau « signal | donnée source citée | pourquoi c'est préoccupant/encourageant | hypothèse d'explication », puis reprenez le fichier `metriques-j30-stockpilot.md` et vérifiez à la main au moins 2 des chiffres cités — c'est le même réflexe de vérification que celui pratiqué le matin, et il s'applique aussi ici.

**Vous concluez sur une moyenne globale plutôt tiède (« ça va, on continue doucement »).**
Symptôme : votre décision ne mentionne aucun segment ni aucune différence entre profils d'utilisateurs — juste un chiffre agrégé du type « 33 % de rétention, moyen, on persévère mollement ». Cause : vous avez lu la performance globale sans la décomposer par profil, alors que la moyenne cache ici un segment clé en échec net (directeurs régionaux à 12 % de rétention) derrière un segment qui réussit très bien (responsables de magasin à 55 %). Correction : reprenez le fichier et isolez les chiffres par profil (responsables de magasin vs directeurs régionaux) avant de conclure — c'est souvent ce changement de regard qui fait basculer une décision de « on continue mollement » à une décision tranchée et argumentée.

**Vous avez demandé à l'IA « que ferais-tu, toi ? » et repris sa réponse presque telle quelle.**
Symptôme : votre décision finale utilise un vocabulaire ou un raisonnement qui n'est pas le vôtre, ou vous avez du mal à la reformuler avec vos propres mots quand on vous la redemande à l'oral. Cause : vous avez délégué l'arbitrage à l'IA au lieu de vous en servir pour éclairer les deux options (steelman) puis trancher vous-même. Correction : redemandez le steelman des deux camps séparément (« le meilleur argumentaire pour Persevere », puis dans un message distinct « le meilleur argumentaire pour Pivot ») sans jamais demander à l'IA laquelle choisir — la décision et sa formulation en 5 lignes doivent venir de vous, avec vos propres critères de priorité.

**Votre FAQ ou votre annonce mentionne une fonctionnalité qui n'existe pas encore en V1.**
Symptôme : en relisant vos non-objectifs de l'exercice 2, vous trouvez une promesse contradictoire dans l'annonce ou la FAQ (ex. géolocalisation temps réel évoquée alors qu'elle était explicitement exclue). Cause : l'IA a généré un contenu marketing « généreux » par défaut, sans que vous ayez vérifié la cohérence avec votre périmètre V1. Correction : reprenez votre document de non-objectifs et repassez l'annonce et la FAQ ligne par ligne ; redemandez à l'IA une version corrigée en lui fournissant explicitement la liste des non-objectifs comme contrainte.

## Pour aller plus loin

Si vous voulez pousser l'exercice, rédigez le message de 10 lignes au sponsor fictif de la direction Logistique annonçant votre décision : contexte, décision, 3 données clés, prochaine étape datée et mesurable (par exemple « correction du parcours signalement de panne + re-mesure à J+60 sur les mêmes 3 magasins » — pas un vague « on continue d'observer »). Puis demandez à l'IA de jouer ce sponsor et de vous poser 2 questions difficiles en retour — répondez-y vraiment. Ces questions tournent en général autour du coût de la correction proposée et du risque d'image si vous retirez ou limitez une fonctionnalité déjà annoncée : deux questions que tout PO doit savoir anticiper avant de présenter une décision Pivot or Persevere.
