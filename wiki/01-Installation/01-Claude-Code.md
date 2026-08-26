<!-- Page wiki GitHub : "Installation — Claude Code". Sur GitHub, renommer sans le préfixe "01-". -->

# Installation — Claude Code (extension VS Code/Antigravity ou CLI)

Copier chaque dossier de skill (récupéré depuis le dépôt GitHub, voir [Accueil](../00-Accueil)) dans `~/.claude/skills/` :

```
~/.claude/skills/
├── cadrage-formation/
│   ├── SKILL.md
│   └── scripts/
├── formation-material-builder/
│   ├── SKILL.md
│   └── references/
├── slide-content-claude-design/
│   ├── SKILL.md
│   └── scripts/             (génération auto des illustrations, optionnel)
├── comite-qualite/
│   └── SKILL.md
├── formation-pipeline/      (optionnel — orchestrateur du pipeline formation complet)
│   └── SKILL.md
├── reponse-appel-offres/    (pipeline réponse à AO, indépendant)
│   ├── SKILL.md
│   ├── references/
│   └── scripts/
└── design-system-extractor/ (transverse aux deux pipelines, à la demande)
    └── SKILL.md
```

Copier uniquement les skills dont tu as besoin — les deux pipelines sont indépendants (voir [Utiliser le pipeline](../02-Utiliser-le-pipeline)).

**Détection** : si `~/.claude/skills/` existe déjà, l'ajout d'un dossier de skill est pris en compte **en direct, sans redémarrer la session en cours**. Un redémarrage n'est nécessaire que si `~/.claude/skills/` lui-même n'existait pas encore au lancement de la session (premier usage sur un poste neuf).

Invocation : `/cadrage-formation`, `/formation-material-builder`, `/slide-content-claude-design`, `/comite-qualite`, `/formation-pipeline`, `/reponse-appel-offres`, `/design-system-extractor` (ou en langage naturel — chaque skill décrit ses propres déclencheurs). Vérifier la détection en tapant `/` dans le chat : les skills installées doivent apparaître dans la liste.

**Si une skill n'est pas détectée** (dernier recours) :
- Ouvrir un nouveau chat plutôt que de réutiliser une session existante.
- Vérifier qu'aucun autre `~/.claude/skills/<nom>/SKILL.md` ne porte le même nom en frontmatter (conflit de nom).

## Paramétrer l'extension dans VS Code / Antigravity

1. Installer l'extension **Claude Code** depuis le marketplace de l'éditeur.
2. Ouvrir l'extension et démarrer une conversation pour déclencher l'écran de connexion.
3. Se connecter avec ton **compte professionnel** (pas un compte personnel) — un compte personnel ne donne pas accès aux mêmes quotas ni aux mêmes skills partagées.
4. Si l'extension semble bloquée, utiliser **"Restart extension"** (palette de commandes) plutôt que de désinstaller/réinstaller.

**Gestion des quotas** : un blocage ponctuel a été observé sur certains comptes professionnels, sans être systématique. Patienter (les quotas se renouvellent) plutôt que de changer de compte par réflexe.

## Ouvrir les fichiers `.xlsx` générés (`cadrage-formation`)

Pour ouvrir le fichier Excel produit sans quitter VS Code / Antigravity :

- Installer une extension de visualisation Excel (ex. « Excel Viewer »).
- Ouvrir directement le fichier depuis l'explorateur de fichiers de l'éditeur : il s'affiche en tableau dans un onglet.
- Alternative sans extension : ouvrir depuis Google Drive si le dossier de formation y est synchronisé.

---

Retour au [sommaire Installation](00-Sommaire).
