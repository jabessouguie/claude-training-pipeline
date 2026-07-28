# atelier-1/ — Corpus brut StockPilot

Matière première de l'atelier 1 (« Audit du dataset StockPilot »). Les stagiaires ingèrent ces 4 fichiers dans Copilot pour en extraire des pain points sourcés, des signaux faibles et des personas dynamiques.

## Fichiers

| Fichier | Format | Contenu |
|---|---|---|
| **enonce-atelier-1.pdf** | PDF (charte par défaut) | Énoncé imprimable de l'atelier : contexte, objectif, consigne, critères de réussite, indices et bonus |
| **enonce-atelier-1.html** | HTML | Source du PDF ci-dessus (à éditer puis regénérer si le contenu change) |
| **interviews.md** | Texte | 12 extraits d'interviews terrain (responsables de magasin, directeurs régionaux, responsables logistique, technicien maintenance) |
| **tickets-support.csv** | CSV (`numero,date,site,objet,detail`) | 15 tickets/incidents matériel (recherches, doubles réservations, pannes non signalées, locations externes…) |
| **verbatims-nps.md** | Texte | Extraits de verbatims libres d'une enquête NPS interne + score NPS global |
| **stats-usage.csv** | CSV (`indicateur,valeur,commentaire`) | Statistiques d'usage du parc de matériel (taux d'utilisation, écarts d'inventaire, dépenses de location externe…) |

La solution suggérée et le guide de vérification de cet atelier sont dans [../solutions/solution-atelier-1.md](../solutions/solution-atelier-1.md).

## Pourquoi 4 fichiers séparés (et pas un seul document)

- Chaque fichier reste court, ce qui réduit le risque de troncature au collage dans le chat (limite de taille de la zone de saisie sur certains tenants).
- Les tickets et les stats sont en **CSV** : format directement exploitable par l'IA pour du tri, du filtrage ou du calcul, plutôt qu'un tableau markdown à reparser.
- Le bonus de l'atelier (« deux passes séparées ») s'appuie naturellement sur cette séparation quali (`interviews.md` + `verbatims-nps.md`) / quanti (`tickets-support.csv` + `stats-usage.csv`).

⚠️ Données fictives, à des fins pédagogiques uniquement. Deux signaux faibles sont volontairement enfouis dans ce corpus — voir la solution de l'atelier (non fournie aux stagiaires) pour la clé de lecture.
