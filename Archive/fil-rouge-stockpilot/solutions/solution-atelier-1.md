# Solution suggérée — Atelier 1 — Audit du dataset StockPilot

> Ce document est fait pour être consulté **après** l'atelier, pour comparer votre production à un résultat attendu et corriger ce qui doit l'être. Ce n'est pas un corrigé à appliquer mécaniquement : le corpus StockPilot est construit pour laisser de la place à des formulations différentes — ce qui compte, c'est la méthode et la traçabilité, pas le mot-pour-mot.

## Ce que vous devriez avoir produit

**Un prompt structuré en 5 blocs**, du type :

```text
Tu es analyste produit senior, spécialiste des outils digitaux
pour le retail.

Je te fournis un corpus brut sur la gestion du petit matériel
réutilisable d'un réseau de magasins de proximité : 12 extraits
d'interviews terrain, 15 tickets support, des verbatims NPS et des
statistiques d'usage du parc.

Tâche 1 : identifie les pain points récurrents.
Format : tableau — Pain point | Fréquence (nb de mentions) |
Impact estimé (H/M/B + justification) | 2 verbatims cités mot pour mot.
Tâche 2 : liste 3 problèmes rares mais potentiellement majeurs
(signaux faibles), avec ta justification.
Tâche 3 : signale toute contradiction entre les verbatims et les
statistiques d'usage.

Règles : n'invente aucun verbatim ni chiffre. Si une information
manque ou est ambiguë, dis-le explicitement.
```

Votre prompt n'a pas besoin d'être identique — mais il doit contenir les mêmes ingrédients : un **rôle**, un **contexte** court et précis, des **tâches** découpées, un **format** de sortie explicite (tableau, colonnes nommées, verbatims cités), et des **garde-fous** anti-hallucination.

**Un tableau de pain points** qui ressemble à ceci (le corpus est construit pour les faire émerger) :

| Pain point | Fréquence attendue | Impact |
|---|---|---|
| Temps perdu à localiser le matériel (appels en cascade) | Très élevée (interviews + tickets) | H — heures de vente ou de réassort perdues |
| Réservations en double / matériel indisponible à l'arrivée | Élevée | H — retards de réassort |
| Pannes non signalées, découvertes à l'usage | Élevée | H — sécurité + arrêt de tâche |
| Locations externes redondantes faute de visibilité sur le parc | Moyenne | H — coût direct mesurable |
| Saisies administratives pénibles (retours, états des lieux) | Moyenne | M — friction, données non remplies |

**2 signaux faibles**, présents mais peu visibles dans le corpus : un signal faible se reconnaît à deux traits — il repose sur très peu de mentions (1 à 2, jamais un pain point récurrent), et il révèle un problème structurel plutôt qu'un simple irritant. Si vous en avez trouvé deux qui remplissent ces deux critères, comparez-les à ceux ci-dessous ; sinon, la section suivante vous aide à les chercher sans vous les révéler directement.

**2 personas**, parmi : responsable de magasin (cherche, réserve, subit les doubles réservations), directeur régional (surstocke, signale peu les pannes), responsable logistique (aveugle sur l'état réel, subit les locations externes), technicien maintenance (découvre les pannes trop tard). Chaque trait doit être tracé vers un verbatim ou une statistique précise.

**Un canevas d'opportunité**, du type :
- **Problème** : les équipes magasin perdent du temps et de l'argent car l'état réel du parc de petit matériel (localisation, disponibilité, état) est invisible — l'information vit dans des appels et des fichiers locaux.
- **Cible** : responsables de magasin et directeurs régionaux (utilisateurs), responsable logistique (bénéficiaire économique).
- **Preuves** : mentions récurrentes du temps de recherche (interviews, tickets, verbatims NPS) ; tickets doublons de réservation ; au moins un écart identifié entre le déclaratif terrain et les données d'usage.
- **Impact estimé** : réduction des locations externes redondantes + heures de recherche récupérées + pannes détectées plus tôt.
- **Risques & inconnues** : adoption terrain (saisie = friction), zones sans réseau en réserve, fiabilité de l'inventaire initial, périmètre (petit matériel seulement vs mobilier de rayonnage).

## Guide de vérification — comparez votre réponse

Reprenez chaque ligne. Répondez honnêtement par oui/non, puis comparez avec ce que vous devriez voir.

| Point de contrôle | Question à se poser | Ce que vous devez voir si c'est bon |
|---|---|---|
| Prompt en 5 blocs | Votre prompt contient-il explicitement un rôle, un contexte, une tâche, un format ET des garde-fous ? | Les 5 blocs sont identifiables séparément dans votre prompt — pas fondus dans un seul paragraphe. |
| Ingestion complète | Avez-vous confirmé que l'IA a bien reçu les 4 fichiers avant de lui demander l'analyse ? | L'IA a accusé réception des 4 fichiers (ou vous avez vérifié le dernier élément reçu) avant de lancer la synthèse. |
| Tableau de pain points | Votre tableau contient-il au moins 5 lignes, toutes sourcées ? | Chaque ligne a un intitulé de pain point, une fréquence, un impact justifié, et 2 verbatims cités mot pour mot. |
| Vérification anti-hallucination | Avez-vous recherché au moins 2 verbatims cités directement dans les fichiers sources (`interviews.md`, `tickets-support.csv`, `verbatims-nps.md`) ? | Les 2 citations existent mot pour mot dans le corpus — ou vous avez détecté et corrigé une invention. |
| Signal faible pertinent | Avez-vous identifié au moins un signal faible qui n'est PAS dans votre top 3 des pain points évidents ? | Le signal repose sur peu de mentions (1 à 2) mais pointe un problème structurel — pas juste « un pain point un peu moins fréquent ». |
| Personas tracés | Chaque trait de vos 2 personas renvoie-t-il à un verbatim ou une statistique précis ? | Vous pouvez pointer du doigt, pour chaque caractéristique, la phrase ou le chiffre source — aucun trait n'est de la couleur locale inventée. |
| Canevas d'opportunité | Votre canevas tient-il en une page, avec Problème / Cible / Preuves (3 éléments sourcés) / Impact / Risques ? | Un tiers pourrait lire votre canevas et le défendre devant un comité sans vous, sans avoir besoin d'explications orales. |

## Ma réponse ne correspond pas — comment la corriger

**Le collage du corpus a été refusé ou tronqué.**
Symptôme : l'IA analyse un corpus visiblement incomplet, ou répond avec des trous étranges. Cause : le corpus est volontairement réparti en 4 fichiers pour rester sous les limites de la zone de saisie, et un collage en une seule fois peut être tronqué silencieusement. Action : collez fichier par fichier, en précisant à chaque envoi « voici le fichier X sur 4, attends d'avoir les 4 avant d'analyser ». Pour vérifier après coup si vous avez un doute : redemandez à l'IA « quel est le dernier élément du fichier que tu as reçu ? » et comparez avec la fin réelle du fichier.

**Votre tableau de pain points tient en deux lignes, ou la sortie est un long texte narratif.**
Symptôme : vous relisez de longs paragraphes plutôt qu'un tableau exploitable. Cause : vous n'avez probablement pas précisé de FORMAT explicite dans votre prompt — l'IA donne la structure qu'on lui demande, pas plus. Action : reprenez votre prompt et ajoutez un bloc FORMAT précis (« tableau — colonnes : Pain point | Fréquence | Impact estimé (H/M/B + justification) | 2 verbatims cités mot pour mot ») puis relancez.

**Vous avez recopié les verbatims sans les vérifier dans le corpus.**
Symptôme : vous ne pouvez pas dire avec certitude, pour au moins 2 citations de votre tableau, où elles se trouvent dans les fichiers sources. Cause : confiance accordée par défaut à la sortie de l'IA — le réflexe de vérification n'a pas encore été pris. Action : reprenez 2 verbatims de votre tableau et cherchez-les mot pour mot dans `interviews.md`, `tickets-support.csv` ou `verbatims-nps.md`. S'ils y sont, le réflexe est validé. S'ils n'y sont pas (paraphrase, fusion de deux phrases, invention), corrigez le verbatim ou redemandez à l'IA une citation exacte en insistant sur la règle « n'invente aucun verbatim ».

**Vous avez passé un temps long à peaufiner le prompt sans avoir encore ingéré le corpus.**
Symptôme : vous avez consacré une bonne partie du temps de l'atelier à la rédaction du prompt avant tout retour concret de l'IA. Cause : sur-ingénierie — chercher la perfection à vide plutôt que d'itérer sur une vraie sortie. Action : la prochaine fois, lancez le prompt dès qu'il couvre les 5 blocs de base, puis itérez à partir de ce que l'IA renvoie réellement — l'itération sur une sortie concrète est plus rapide et plus riche que la perfection théorique.

**Votre signal faible est en réalité un pain point un peu moins fréquent que les autres, ou vous n'en avez trouvé aucun.**
Symptôme : votre "signal faible" apparaît une dizaine de fois dans le corpus, ou ressemble au 4e/5e pain point de votre tableau principal — ou vous n'avez tout simplement rien de solide à proposer. Cause : confusion entre « rare » et « signal faible » — un signal faible est rare MAIS annonciateur d'un problème structurel, pas simplement moins fréquent que les autres. Action : redemandez explicitement à l'IA « qu'est-ce qui n'est mentionné que par 1 ou 2 personnes dans les interviews ou les tickets ? » et, séparément, « y a-t-il une incohérence entre ce que disent les gens sur la disponibilité du matériel et ce que montrent les statistiques d'usage ? ». Ces deux questions, posées explicitement, suffisent à faire émerger les deux signaux attendus — inutile de les chercher vous-même ligne par ligne dans le corpus, c'est le rôle de l'IA.

**Vos personas contiennent des traits qui semblent inventés ou "pour faire vrai".**
Symptôme : un trait de persona (âge précis, habitude, préférence) que vous ne pouvez rattacher à aucun verbatim ni aucune statistique du corpus. Cause : l'IA a « rempli les blancs » pour rendre le persona plus vivant, et vous ne l'avez pas challengée. Action : pour chaque trait, demandez-vous « à quel verbatim ou quelle stat est-ce que je peux le relier ? ». Si la réponse est aucune, supprimez le trait ou redemandez à l'IA de le justifier avec une source du corpus — sinon, retirez-le du persona.

**Votre contexte de conversation semble "oublier" le début du corpus après plusieurs itérations.**
Symptôme : l'IA contredit une information qu'elle avait pourtant donnée plus tôt, ou perd des détails du début du corpus. Cause : contexte de conversation saturé (corpus long + itérations successives). Action : rouvrez une conversation neuve et re-collez le corpus avec un prompt consolidé plutôt que de continuer à itérer sur une conversation déjà longue.

**Votre canevas d'opportunité dépasse largement une page, ou vous ne sauriez pas le défendre seul.**
Symptôme : le canevas s'étale sur plusieurs pages, ou contient des sections floues que vous ne pourriez pas justifier à l'oral. Cause : les preuves ou les risques n'ont pas été suffisamment synthétisés — souvent un signe que le tri entre "ce qui est solide" et "ce qui est accessoire" n'a pas été fait. Action : reprenez chaque section et demandez-vous « si je devais la défendre en 30 secondes devant un comité, qu'est-ce que je garde ? ». Éliminez ce qui n'est pas indispensable, en particulier dans les preuves — 3 éléments sourcés suffisent, pas plus.

## Pour aller plus loin

Question à vous poser maintenant que l'atelier est terminé : *votre responsable logistique conteste un chiffre agrégé calculé par l'IA à partir de `stats-usage.csv` — comment vérifieriez-vous qu'elle ne l'a pas mal calculé ?*

Réponse attendue : demander à l'IA le détail de son calcul, retracer ce calcul vers les lignes de statistiques sources dans `stats-usage.csv`, puis refaire le calcul à la main sur un sous-ensemble pour confirmer. C'est le même réflexe que la vérification des verbatims, appliqué cette fois à un chiffre agrégé plutôt qu'à une citation — un bon réflexe à généraliser dès que l'IA vous fournit un chiffre qui va peser dans une décision.

Si vous avez fini rapidement pendant l'atelier, vous avez peut-être testé la variante en deux passes séparées (quali seul, puis quanti seul, puis croisement demandé explicitement à l'IA) — si ce n'est pas le cas, c'est un excellent exercice à refaire seul après coup : la triangulation explicite fait souvent émerger des contradictions plus riches qu'une passe unique.
