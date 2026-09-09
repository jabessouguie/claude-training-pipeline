#!/usr/bin/env python3
"""Génère les illustrations d'un module via l'API Gemini, à partir d'un
fichier M<n>-prompts.md déjà produit par slide-content-claude-design.

Ce script est purement mécanique (parsing + appel API + écriture fichier) :
il n'encode aucune règle de style, de palette ou de choix créatif — tout cela
vit dans M<n>-prompts.md (déjà écrit par la skill) et dans le bloc
« Direction artistique » qu'il contient. Voir slide-content-claude-design/SKILL.md
§ « Mode génération automatique des illustrations » et PIPELINE_CONTRACTS.md
Contrat 4 pour le contrat d'entrée/sortie complet.

Usage: python generate_illustrations.py M<n>-prompts.md assets_dir/

Nécessite la variable d'environnement GEMINI_API_KEY. Modèle utilisé :
gemini-2.5-flash-image ("Nano Banana") — jamais l'ancien nom Imagen, déprécié
(fin de vie annoncée le 17/08/2026).
"""
import os
import re
import sys

MODEL = "gemini-2.5-flash-image"

# Une section par slide illustrée : "## Slide 3 — Illustration" suivi du
# contenu jusqu'à la section suivante ou la fin de fichier. Les slides
# marquées "pas d'illustration : composant vectoriel" (fallback) sont
# ignorées : aucun prompt à générer pour elles (voir SKILL.md § Fallback).
SLIDE_SECTION_RE = re.compile(
    r"^## Slide (\d+) — Illustration\s*$(.*?)(?=^## Slide \d+|\Z)",
    re.MULTILINE | re.DOTALL,
)
PROMPT_RE = re.compile(
    r"\*\*Prompt pour Gemini\*\*\s*:\s*\n+(.*?)(?=\n##|\Z)",
    re.DOTALL,
)


def extract_direction_artistique(text):
    match = re.search(
        r"^# Direction artistique.*?(?=^## Slide \d+|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError(
            "Bloc « Direction artistique » introuvable en tête du fichier — "
            "vérifier que M<n>-prompts.md respecte le format prescrit par "
            "slide-content-claude-design/SKILL.md."
        )
    return match.group(0).strip()


def extract_slide_prompts(text):
    slides = []
    for slide_match in SLIDE_SECTION_RE.finditer(text):
        slide_num = int(slide_match.group(1))
        section_body = slide_match.group(2)
        prompt_match = PROMPT_RE.search(section_body)
        if not prompt_match:
            print(f"AVERTISSEMENT : Slide {slide_num} sans prompt Gemini détecté, ignorée.")
            continue
        slides.append((slide_num, prompt_match.group(1).strip()))
    return slides


def generate_image(client, direction_artistique, slide_prompt):
    full_prompt = f"{direction_artistique}\n\n{slide_prompt}"
    response = client.models.generate_content(
        model=MODEL,
        contents=full_prompt,
    )
    for part in response.candidates[0].content.parts:
        if getattr(part, "inline_data", None) is not None:
            return part.inline_data.data
    return None


def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_illustrations.py M<n>-prompts.md assets_dir/")
        sys.exit(1)

    prompts_path, assets_dir = sys.argv[1], sys.argv[2]

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERREUR : GEMINI_API_KEY absente ou invalide.")
        sys.exit(1)

    try:
        from google import genai
    except ImportError:
        print("ERREUR : dépendance manquante — installer avec `pip install google-genai`.")
        sys.exit(1)

    with open(prompts_path, encoding="utf-8") as f:
        text = f.read()

    direction_artistique = extract_direction_artistique(text)
    slides = extract_slide_prompts(text)

    if not slides:
        print("Aucune slide illustrée trouvée dans ce fichier (toutes en fallback vectoriel ?).")
        sys.exit(0)

    os.makedirs(assets_dir, exist_ok=True)
    client = genai.Client(api_key=api_key)

    succeeded, failed = [], []
    for slide_num, slide_prompt in slides:
        try:
            image_bytes = generate_image(client, direction_artistique, slide_prompt)
        except Exception as exc:
            failed.append(slide_num)
            print(f"ÉCHEC (appel API) : slide {slide_num} — {exc} (placeholder resté vide, à générer à la main)")
            continue

        if image_bytes is None:
            failed.append(slide_num)
            print(f"ÉCHEC (réponse sans image, quota ou contenu probablement refusé) : slide {slide_num} (placeholder resté vide, à générer à la main)")
            continue

        try:
            out_path = os.path.join(assets_dir, f"slide-{slide_num}.png")
            with open(out_path, "wb") as f:
                f.write(image_bytes)
        except OSError as exc:
            failed.append(slide_num)
            print(f"ÉCHEC (écriture fichier — vérifier l'espace disque/les permissions) : slide {slide_num} — {exc}")
            continue

        succeeded.append(slide_num)
        print(f"OK : slide {slide_num} → {out_path}")

    print(f"\nRésumé : {len(succeeded)} image(s) générée(s), {len(failed)} échec(s).")
    if failed:
        print(f"Slides en échec : {', '.join(str(n) for n in failed)}")


if __name__ == "__main__":
    main()
