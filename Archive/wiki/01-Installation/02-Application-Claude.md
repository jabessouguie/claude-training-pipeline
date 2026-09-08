<!-- Page wiki GitHub : "Installation — Application Claude". Sur GitHub, renommer sans le préfixe "02-". -->

# Installation — Application Claude (claude.ai, app desktop/mobile)

L'application Claude installe les skills **une par une, par fichier ZIP**, via **Réglages → Personnaliser → Skills**.

1. **Activer d'abord** l'option « Exécution de code et création de fichiers » dans les réglages (Pro/Max/Team/Entreprise).
2. **Préparer le ZIP** pour chaque skill : le ZIP doit contenir le **dossier de la skill à sa racine** (pas son contenu nu), et le nom de ce dossier doit correspondre exactement au nom de la skill. Depuis une copie locale du dépôt : `cd ~/.claude/skills && zip -r cadrage-formation.zip cadrage-formation/` (répéter pour chacune des 4 skills).
3. **Réglages → Personnaliser → Skills → "+" → Create skill → Upload a skill**, puis sélectionner le ZIP. Répéter pour les 4 skills.

**Si ton compte professionnel est en Team/Enterprise** : demande à la personne **Owner** de provisionner les 4 skills en une seule fois pour toute l'équipe, via *Réglages d'organisation → Skills → Organization skills → « + Add »* — plutôt que chaque consultant les installe individuellement. *(Point signalé pour vérification : la documentation développeur Anthropic affirme encore qu'aucune gestion centralisée n'existe sur claude.ai, ce qui contredit la doc support décrivant ce mécanisme de provisioning. Les deux pages ne sont pas synchronisées entre elles — se fier en priorité à la doc support, plus récente, mais confirmer auprès d'un Owner du compte.)*

---

Retour au [sommaire Installation](00-Sommaire). Utilises-tu aussi Cowork ? Voir [Installation — Cowork](03-Cowork).
