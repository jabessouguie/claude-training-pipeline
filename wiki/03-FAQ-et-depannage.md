<!-- Page wiki GitHub : "FAQ et dépannage". Sur GitHub, renommer sans le préfixe "03-". -->

# FAQ et dépannage

## Je ne trouve pas les 4 dossiers de skills dans le dépôt GitHub

**Ce dépôt GitHub est la référence unique** pour récupérer les skills — ne pas se fier à un envoi ponctuel par e-mail ou par zip, qui peut être partiel ou périmé. Si les dossiers ne sont pas là, contacte la personne responsable du dépôt (voir `CONTRIBUTING.md`) plutôt que de repartir d'un zip reçu par ailleurs.

## Une skill n'apparaît pas quand je tape `/` dans le chat (Claude Code)

1. Vérifie que le dossier de la skill est bien à la racine de `~/.claude/skills/` (pas dans un sous-dossier, pas encore sous forme de zip).
2. Ouvre un **nouveau chat** plutôt que de réutiliser une session existante.
3. Vérifie qu'aucun autre `~/.claude/skills/<nom>/SKILL.md` ne porte le même nom en frontmatter (conflit de nom) — deux skills avec le même nom, une seule sera détectée.

## J'utilise l'application Claude ou Cowork, les skills que j'ai installées sur Claude Code n'apparaissent pas

C'est normal : **les skills ne se synchronisent pas entre surfaces**. Il faut répéter l'installation sur chaque surface séparément — voir [Installation](01-Installation/00-Sommaire) pour la procédure propre à l'application Claude/Cowork (upload d'un fichier ZIP).

## Un blocage de quotas est apparu sur l'extension Claude Code

Un blocage ponctuel a été observé sur certains comptes professionnels, sans être systématique. Patiente (les quotas se renouvellent) plutôt que de changer de compte ou de modèle par réflexe.

## Je préfère VS Code ou Antigravity — lequel choisir ?

Les deux fonctionnent aussi bien l'un que l'autre pour ce pipeline — c'est une préférence d'environnement, pas une contrainte technique.

## Comment ouvrir le fichier `.xlsx` produit par `cadrage-formation` sans quitter mon éditeur ?

Installe une extension de visualisation Excel (ex. « Excel Viewer ») depuis le marketplace de l'éditeur, puis ouvre le fichier directement depuis l'explorateur de fichiers — il s'affiche en tableau dans un onglet. Alternative sans extension : ouvre-le depuis Google Drive si le dossier de formation y est synchronisé.

## L'assistant me pose beaucoup de questions, je veux qu'il aille plus vite

Dis-lui explicitement « continue sans t'arrêter » — il enchaînera les étapes sans attendre de validation à chaque point, sauf pour les décisions les plus structurantes (ex. le cas fil rouge d'une formation, qui coûte cher à corriger une fois les ateliers rédigés).

## Je veux auditer un livrable qui n'est pas une formation

`comite-qualite` fonctionne sur n'importe quel type de livrable — docx, xlsx, pptx, code, offre commerciale, rapport… Elle compose une équipe de relecteurs adaptée automatiquement selon le type et le domaine du livrable que tu lui donnes.

## Je ne trouve pas la réponse à ma question ici

Consulte le dépôt GitHub complet (les `SKILL.md` de chaque skill décrivent leur fonctionnement en détail), ou contacte l'équipe responsable du dépôt — voir `CONTRIBUTING.md` dans le dépôt.
