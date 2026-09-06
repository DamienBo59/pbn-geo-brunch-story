# Prompts avatars des auteurs du parc perso

Style unifie pour tous les avatars : **flat illustration portrait, vector style, soft pastel palette, centered headshot, clean neutral background, friendly expression, shoulders up, 1:1 square ratio**.

Conventions :
- Taille cible : 512x512 px
- Format final : WebP (convertir avec `cwebp -q 85`)
- Chemin de destination : `static/images/authors/[id].webp`

⚠️ **Trois auteurs seulement, et ils ne sont pas interchangeables.** Chacun est un persona du parc qui signe UN blog et porte AUSSI un compte Reddit. Les avatars doivent rester **coherents avec la fiche persona** (age, region, milieu) : un avatar de cadre en costume pour une professeure des ecoles de 35 ans decredibilise la signature. Fiches dans le Drive perso, `100 Areas/seo_freelance/Reddit/parc-reddit/personas/`.

**Ne pas donner un air de photographie.** Le style flat illustration est volontaire : un faux portrait photo-realiste d'une personne qui n'existe pas est le genre de detail qui se retourne contre le site, et une illustration ne pretend rien.

## Hélène Vasseur — Thé et infusions (P01, mamie-the.fr)

Femme de 41 à 48 ans, bibliothécaire dans le Nord. Doit avoir l'air posé et chaleureux, pas expert.

```
Flat vector illustration portrait, headshot of a calm woman in her mid-forties, shoulder-length wavy auburn hair with a few grey strands, fine reading glasses pushed up on her head, gentle closed-lip smile, wearing a soft moss-green knitted cardigan over a cream blouse, warm pastel palette with sage and terracotta tones, clean neutral background with a faint suggestion of a teapot silhouette, centered composition, shoulders up, 1:1 square ratio, modern editorial style, quietly warm expression.
```

Destination : `static/images/authors/helene-vasseur.webp`

## Marion Kieffer — Pâtisserie et goûter (P02, gouter-gourmand.fr)

Femme de 33 à 40 ans, professeure des écoles en Alsace, pâtissière amateur. Doit avoir l'air accessible et actif, jamais chef étoilé.

```
Flat vector illustration portrait, headshot of a friendly woman in her mid-thirties, dark brown hair tied back in a loose bun with a few loose strands, open smile showing warmth, wearing a soft coral apron strap over a light chambray shirt, warm pastel palette with butter yellow and coral tones, clean neutral background with a faint suggestion of a round cake tin, centered composition, shoulders up, 1:1 square ratio, modern editorial style, approachable everyday expression.
```

Destination : `static/images/authors/marion-kieffer.webp`

## Bastien Delorme — Brunch et petit déjeuner (P03, brunch-story.fr)

Homme de 26 à 32 ans, citadin lyonnais. Doit avoir l'air jeune actif décontracté, jamais critique gastronomique.

```
Flat vector illustration portrait, headshot of a relaxed young man in his late twenties, short dark hair with a light beard trimmed close, easy half-smile, wearing a mustard crewneck sweater over a white t-shirt, warm pastel palette with mustard and soft teal tones, clean neutral background with a faint suggestion of a coffee cup seen from above, centered composition, shoulders up, 1:1 square ratio, modern editorial style, casual confident expression.
```

Destination : `static/images/authors/bastien-delorme.webp`

## Si un quatrieme auteur devient necessaire

Il faut d'abord creer le persona en suivant `../../../100 Areas/seo_freelance/Reddit/parc-reddit/personas/_METHODE.md` (9 etapes, dont le controle anti-doublon ecrit). **Ne jamais ajouter un avatar sans fiche persona** : un auteur sans persona devient mecaniquement un auteur fourre-tout, et c'est exactement ce qui a tue les premiers comptes du parc pro.
