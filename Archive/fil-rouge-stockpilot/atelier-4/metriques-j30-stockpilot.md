# StockPilot V1 — Tableau de bord à J+30 (document de formation, données fictives)

> Déploiement pilote : 3 magasins (Rennes-Centre, Nantes-Sud, Quimper) + 2 entrepôts régionaux (Nord, Sud).
> Population cible : 45 utilisateurs (12 responsables de magasin, 18 directeurs régionaux, 9 responsables logistique/maintenance, 6 encadrement).
> Période : 30 premiers jours après mise en service.
> ⚠️ Données inventées à des fins pédagogiques (atelier 4).

## 1. Adoption & rétention

| Indicateur | Global terrain* | Responsables de magasin | Directeurs régionaux | Responsables logistique / maintenance |
|---|---|---|---|---|
| Comptes activés | 76 % | 90 % | 66 % | 100 % |
| Actifs hebdomadaires (semaine 4) | 44 % | **62 %** | **28 %** | 89 % |
| Rétention J+7 | 57 % | 71 % | 44 % | 100 % |
| Rétention J+14 | 43 % | 63 % | 24 % | 89 % |
| Rétention J+30 | **33 %** | **55 %** | **12 %** | 89 % |

\* Colonne « Global terrain » : responsables de magasin + directeurs régionaux (30 utilisateurs), les segments visés par le déploiement terrain ; activité et rétention exprimées en % des comptes activés du périmètre, arrondies au point. Responsables logistique/maintenance (9) et encadrement (6) sont suivis séparément compte tenu de leurs effectifs réduits.

Tendance : la rétention des directeurs régionaux chute chaque semaine depuis le lancement (44 % → 24 % → 16 % → 12 %).

## 2. Usage des fonctionnalités (30 jours)

| Fonctionnalité | Volume | Référence / attendu | Écart |
|---|---|---|---|
| Recherches de matériel | 1 870 | — | — |
| Réservations créées | **340** | — | — |
| Doubles réservations constatées | 4 | 13/mois recensées par les entrepôts avant StockPilot (sites pilotes) | **−70 %** |
| Signalements de panne | **9** | ~30/mois attendus (historique maintenance des sites pilotes, anomalies mineures incluses) | **−70 % vs attendu** |
| Retours de matériel saisis dans l'app | 41 % des retours réels | Cible : 90 % | Très en deçà |
| Équipements « introuvables » dans l'app (état ≠ réalité) | **8 % du parc pilote** | Cible : < 2 % | Écart persistant |

## 3. Impact économique (périmètre pilote, 30 jours)

| Indicateur | Valeur | Comparaison |
|---|---|---|
| Dépenses de location externe | 3 525 €/mois constaté | **−18 %** vs moyenne des 3 mois précédents (≈ 4 300 €/mois) — soit ~775 €/mois économisés, ~9 300 € en rythme annualisé sur le périmètre |
| Temps de recherche de matériel (sondage flash, 12 répondants) | ~40 min/semaine/responsable de magasin | **÷ 4** vs mesure discovery (2 h 40) — déclaratif |
| Demandes non satisfaites (entrepôts) | 14/mois | 23/mois avant pilote |

## 4. Satisfaction

- **NPS pilote à J+30 : +12** (18 répondants) — promoteurs surtout responsables de magasin et responsables logistique, détracteurs surtout directeurs régionaux.
- Support : 31 tickets ouverts, dont 19 « aide à la première connexion », 7 « lenteur / connexion en magasin », 5 divers.

## 5. Verbatims collectés (canal support + sondage flash)

- « Pour réserver depuis le bureau, nickel. En magasin avec les mains prises, c'est une autre histoire. » (responsable de magasin)
- « L'appli rame dès que je suis en réserve, il n'y a pas de réseau là-bas. » (directeur régional)
- « Signaler une panne, c'est encore 6 champs à remplir. Au retour à l'entrepôt, je n'ai pas le courage. » (directeur régional)
- « Enfin je vois où sont mes transpalettes. Ça m'a évité deux locations ce mois-ci, du concret. » (responsable logistique)
- « Je reçois trop de notifications, j'ai tout coupé au bout d'une semaine. » (responsable de magasin)
- « La moitié du matériel que je cherche est marqué "à l'entrepôt" alors qu'il n'y est pas. Du coup je rappelle, comme avant. » (directeur régional)
- « Mes équipes ne saisissent pas les retours, et je ne vais pas les fliquer pour ça. » (directeur régional)
- « Franchement bien pour préparer la semaine. Le lundi matin, je sais ce que j'ai. » (responsable de magasin)

---

*Document remis pour l'atelier 4 de la formation « Product Management augmenté » — décision attendue : Pivot ou Persevere, argumentée sur ces données.*
