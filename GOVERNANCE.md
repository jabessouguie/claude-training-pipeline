# Gouvernance — Pipeline de skills de formation

Ce document définit qui décide quoi sur ce dépôt, et comment, pour une équipe restreinte (3 contributeurs) qui fait évoluer ce pipeline en parallèle de son activité de conseil.

## Rôles

### Product Owner (rôle, pas nécessairement titre)
Porte la priorisation du [BACKLOG.md](BACKLOG.md) et la cohérence de la [ROADMAP.md](ROADMAP.md). Tranche en cas de désaccord sur ce qui doit être fait en premier.
- **Actuellement** : la personne à l'origine des 4 skills historiques (`cadrage-formation`, `formation-material-builder`, `slide-content-claude-design`, `comite-qualite`), qui anime le pipeline — ce périmètre inclut aussi `formation-pipeline`, la skill orchestratrice additionnelle qui les enchaîne.
- Ce rôle est explicitement révisable — voir "Évolution de la gouvernance" ci-dessous.

### Contributeurs
Toute personne qui modifie une `SKILL.md`, ses `references/`, ou ses `scripts/` — chacun aussi utilisateur final du pipeline (dogfooding).

### Utilisateurs
Toute personne du cabinet qui utilise une ou plusieurs des 4 skills pour produire une formation, sans forcément contribuer au code. Leurs retours d'usage sont la source principale d'évolution du backlog.

### Périmètre de ce dépôt vs autres démarches de capitalisation
Ce dépôt couvre la capitalisation des **skills** (savoir-faire packagé et réutilisable), distincte de la capitalisation **projet** classique (retours d'expérience, livrables archivés par mission) — les deux sont complémentaires : un projet donne l'occasion d'extraire une skill réutilisable, qui peut ensuite être redéclinée dans d'autres process. Avant d'élargir le périmètre d'usage de ce dépôt à un autre process que la production de formation, un arbitrage explicite avec les porteurs de ce process est nécessaire.

## Comment une décision se prend

| Type de décision | Qui décide | Comment |
|---|---|---|
| Ajouter/prioriser un item du backlog | Product Owner | Sur la base d'un constat observé en usage réel (pas d'idée abstraite) — voir format des items dans `BACKLOG.md` |
| Choix technique interne à une skill (prompt, structure de fichier) | Le contributeur qui implémente | Revue légère par un 2e contributeur avant merge (cf. DoD dans `BACKLOG.md`) |
| Arbitrage d'outillage transverse (ex. quel environnement Claude Code utiliser) | Collectif des 3 | Discussion explicite, pas une décision unilatérale — impacte l'ensemble des utilisateurs |
| Changement de convention partagée (ex. rangement des livrables) | Product Owner, en concertation | Documenté dans le `SKILL.md` concerné avant d'être appliqué rétroactivement |
| Rejet d'une idée hors périmètre | Product Owner | Documenté dans la section "Non retenu" de `BACKLOG.md` avec la raison, pour ne pas la redébattre sans élément nouveau |

## Comment un retour d'usage devient une évolution

1. Un utilisateur rencontre un irritant ou identifie une amélioration en utilisant le pipeline.
2. Le constat est reformulé en item de `BACKLOG.md` : constat observé + valeur + action proposée + effort estimé + dépendances. Un ressenti seul ("ce serait bien si...") ne suffit pas sans un exemple concret d'usage qui l'illustre.
3. Le Product Owner priorise l'item (P0 à P3) et l'affecte à un horizon de la `ROADMAP.md`.
4. Si l'item est suffisamment cadré, il est reformulé en user story avec DoR/DoD (voir `BACKLOG.md`), sinon il reste en Horizon 4 (exploratoire) jusqu'à ce qu'un préalable soit levé.
5. Un contributeur implémente en suivant `CONTRIBUTING.md`.

## Cycle de vie d'une skill (SDLC léger)

Pour une équipe de 3 contributeurs, un cycle de vie léger suffit :

- **Création** : une skill naît d'un besoin observé en usage réel (jamais d'une idée abstraite), suit le format `SKILL.md` existant, et son premier usage réel sert de test.
- **Évolution** : toute modification suit le circuit décrit ci-dessus (retour d'usage → item de backlog → story → implémentation) et respecte la DoD (`BACKLOG.md`) — revue croisée obligatoire, test de fumée du pipeline complet.
- **Dépréciation** : si une skill ou un comportement documenté cesse d'être recommandé (ex. remplacement d'un format de sortie), le `README.md` racine est mis à jour dans le même changement pour ne pas laisser une documentation obsolète faire foi.
- **Repère de maturité** : la preuve de valeur de référence documentée dans `ROADMAP.md` (une formation multi-jours produite en une fraction du temps qu'elle demanderait en méthode manuelle) sert de repère — toute évolution significative du pipeline peut se mesurer à cette aune.

Ce cycle de vie est volontairement léger : il ne prévoit pas de versionnage sémantique formel (`v1.2.0`) tant que l'équipe reste à 3 contributeurs. À réévaluer si le nombre de contributeurs ou d'utilisateurs consommant ce dépôt augmente significativement.

## Cadence

Il n'y a pas de cérémonie fixe (pas de sprint planning, pas de daily) : l'équipe est restreinte et travaille sur ce pipeline en parallèle de missions client. La cadence naturelle est celle des sessions de démo/usage réel, qui servent à la fois de rétrospective et de collecte de besoins. Toute personne peut proposer un point de synchronisation dès qu'elle a un retour d'usage significatif à partager — pas besoin d'attendre une prochaine session planifiée.

## Évolution de la gouvernance

Ce document est lui-même un livrable du pipeline produit et peut évoluer. Toute modification (changement de rôle PO, ajout d'un contributeur, changement du mode de décision) se propose comme une modification de ce fichier, visible et commentable par les 3 contributeurs actuels avant d'être actée — au même titre qu'une évolution de skill.
