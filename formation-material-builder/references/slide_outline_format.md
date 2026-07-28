# Format markdown pour `slides.md`

Le fichier `slides.md` est l'outline structurée des slides du module. Il sera converti en `.pptx` à la Phase 3 par un script qui parse ce format.

## Convention de structure

- Le fichier commence par un titre `# Module M<n> : <titre>`
- Chaque slide est un bloc `## Slide N : <titre slide>` suivi de ses métadonnées
- Les blocs sont **séparés par `---`** (trois tirets sur leur propre ligne)
- Les métadonnées sont des paires `Clé: valeur` en début de bloc (avant le contenu)
- Les sections du contenu utilisent des `### Sous-titres` quand utile

## Champs reconnus

### Obligatoires

- `Type:` — `title` | `agenda` | `content` | `image` | `code` | `exercise` | `recap` | `transition`
- `Timing:` — durée prévue (`3min`, `5-7min`)

### Optionnels

- `Layout:` — `title` | `content` | `two-columns` | `image-right` | `full-image` | `code-block`
- `Image:` — chemin vers une image si on en utilise une
- `Langue:` — `python` | `bash` | `sql` | `javascript` | etc. (pour les slides `code`)
- `Notes formateur:` — texte multiligne (devient les speaker notes du slide dans le .pptx)

## Exemples par type

### Slide de titre

```markdown
## Slide 1 : Bienvenue
Type: title
Timing: 2min
Layout: title

Titre principal: Formation IA Générative
Sous-titre: Acme Corp · 14-15 novembre 2025

Notes formateur: Énergie haute, accueil chaleureux. Tour de table express : nom, rôle, attente principale (1 phrase chacun).

---
```

### Slide agenda

```markdown
## Slide 2 : Programme des deux journées
Type: agenda
Timing: 3min

Corps:
- **Jour 1 matin** — Fondamentaux des LLMs
- **Jour 1 après-midi** — Atelier prompt engineering
- **Jour 2 matin** — RAG et bases vectorielles
- **Jour 2 après-midi** — Cas d'usage métier + plan d'action

Notes formateur: Montrer qu'on alterne théorie et pratique. Pas de "trop théorique" prévu. Annoncer les pauses (10h30 et 15h30).

---
```

### Slide de contenu standard

```markdown
## Slide 5 : Les 3 paradigmes de l'IA
Type: content
Timing: 5min

Titre: Trois grandes vagues, un même objectif

Corps:
- **IA symbolique (1950-2010)** — règles explicites, "si X alors Y", limité par la difficulté à encoder le bon sens
- **ML classique (2010-2017)** — apprentissage statistique sur features, nécessite feature engineering manuel
- **Deep learning + LLMs (2017+)** — représentations apprises de bout en bout, performances spectaculaires sur le langage et la vision

Notes formateur: Insister sur la rupture 2017 = paper "Attention is all you need" de Google. Anecdote : ce papier de 8 pages a déclenché tout l'écosystème actuel. Avant lui, GPT et ChatGPT n'auraient pas existé.

---
```

### Slide avec code

````markdown
## Slide 12 : Premier appel API OpenAI
Type: code
Timing: 4min
Langue: python

Titre: 5 lignes pour appeler GPT-4

Code:
```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Explique-moi le RAG en 2 phrases."}]
)
print(response.choices[0].message.content)
```

Notes formateur: Si l'environnement est prêt et que la clé API est disponible, faire un live coding. Sinon, montrer le résultat attendu. Mentionner que `OpenAI()` lit la variable d'env `OPENAI_API_KEY` automatiquement.

---
````

### Slide exercice (lance un atelier)

```markdown
## Slide 15 : Atelier 1 — Variations de prompt
Type: exercise
Timing: 25min

Titre: Atelier 1 — Comment formuler change tout

Énoncé: Vous avez un paragraphe de 200 mots. Faites 3 prompts différents pour le résumer :
1. Un prompt minimaliste ("résume ce texte")
2. Un prompt avec contexte et contrainte (ex: "résume en 2 phrases pour un public non-technique")
3. Un prompt avec un format de sortie imposé (ex: JSON, bullet list, tweet)

Comparez les 3 résultats et notez ce qui change.

Durée: 20 min individuel + 5 min debrief collectif

Notes formateur: Passer dans les rangs. Identifier 2 prompts intéressants (un très bon, un qui produit un résultat inattendu) pour le debrief collectif. Demander au stagiaire d'expliquer pourquoi son prompt a marché ou pas.

---
```

### Slide recap

```markdown
## Slide 20 : Ce qu'on retient de ce module
Type: recap
Timing: 4min

Titre: Trois choses à garder en tête

Corps:
- Un LLM, fondamentalement, est un modèle qui **prédit le mot suivant** à partir d'un contexte — il ne "raisonne" pas comme un humain
- La **qualité de la réponse dépend de la qualité du prompt** — c'est une compétence apprenable, et ça vaut le coup d'y consacrer du temps
- L'API est un outil parmi d'autres — pour 80% des usages quotidiens, l'interface chat (ChatGPT, Claude, Mistral Le Chat) est suffisante et plus rapide

Notes formateur: Demander une question de compréhension ouverte avant la pause : "Si je vous donne une tâche où le LLM dérape, comment vous diagnostiquez si c'est le prompt ou le modèle ?". Si la salle est silencieuse, donner la réponse soi-même.

---
```

### Slide transition / question

```markdown
## Slide 21 : Question pour amorcer
Type: transition
Timing: 1min

Titre: Maintenant qu'on sait appeler un LLM…

Corps: Comment lui donner accès à VOS données ?

Notes formateur: Slide-question, on s'arrête 30 secondes, on laisse la question résonner. Pas besoin d'attendre une réponse — l'objectif est l'amorce du module suivant sur le RAG.

---
```

## Règles de conversion `slides.md` → `.pptx`

La conversion se fait via un script JS qui utilise `pptxgenjs`. Le script doit :

1. Parser le markdown en blocs séparés par `---`
2. Pour chaque bloc :
   - Lire le titre `## Slide N : …`
   - Extraire les métadonnées (Type, Timing, etc.)
   - Mapper le `Type:` au layout approprié
   - Injecter les contenus dans les zones du layout
   - Ajouter les `Notes formateur:` en speaker notes
3. Numéroter les slides automatiquement
4. Ajouter un footer cohérent (nom formation + numéro de slide / total)

Si le client a une charte graphique spécifique, adapter le mapping des couleurs et fonts dans le script.

## Cas particuliers

### Slide avec image

```markdown
## Slide 8 : Architecture RAG
Type: image
Timing: 4min
Image: assets/schema-rag.png

Titre: Comment un LLM accède à vos documents

Notes formateur: Décrire le schéma de gauche à droite — ingestion → embeddings → vector store → retrieval → augmentation du prompt → génération. Insister sur le fait que le LLM ne "voit" jamais vos documents bruts, seulement les chunks retrouvés.

---
```

### Slide à deux colonnes

```markdown
## Slide 10 : Avantages et limites du RAG
Type: content
Layout: two-columns
Timing: 4min

Titre: Le RAG est-il toujours la solution ?

Colonne gauche:
**Avantages**
- Données fraîches et personnalisées
- Source citable (auditabilité)
- Pas besoin de re-train le modèle
- Coût maîtrisé

Colonne droite:
**Limites**
- Qualité dépendante des chunks
- Performance limitée par le retrieval
- Coût d'infrastructure (vector store)
- Complexité de mise en œuvre

Notes formateur: Ne pas vendre le RAG comme la solution miracle. Cas où ça ne marche pas bien : quand l'info utile est dispersée dans plusieurs documents et qu'il faut synthétiser.

---
```

### Slide notes-uniquement (gabarit minimal)

Si on a un slide simple sans contenu complexe :

```markdown
## Slide 22 : Pause
Type: transition
Timing: 15min

Titre: Pause — Reprise à 10h45

Notes formateur: Annoncer le timing précis de reprise. Recharger l'écran formateur.

---
```
