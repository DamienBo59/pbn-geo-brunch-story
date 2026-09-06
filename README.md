# Brunch Story

Blog Hugo bilingue FR/EN sur le brunch et le petit dejeuner, servi sur <https://www.brunch-story.fr/>.

Membre du **parc PBN GEO perso** de Damien (compte GitHub `DamienBo59`, domaines chez o2switch). Aucun lien avec le parc datashake. Doctrine, roots et regles propres a ce blog : lire le `CLAUDE.md`.

## En bref

| | |
|---|---|
| Domaine | `www.brunch-story.fr` (apex redirige, HTTPS Let's Encrypt) |
| Hebergement | GitHub Pages, deploiement par GitHub Actions |
| Generateur | Hugo extended 0.161.1 (CI) |
| Langues | FR a la racine, EN sous `/en/` |
| Auteur unique | Bastien Delorme (`bastien-delorme`), persona P03 du parc |
| Roadmap | `roadmap.yaml`, 2 publications par semaine (mardi et vendredi) |

## Developper en local

```bash
hugo server        # http://localhost:1313/
hugo               # build dans public/
```

## Deploiement

Push sur `main` : GitHub Actions build et deploie. Un **cron mardi et vendredi 4h UTC** relance le build pour reveler les articles dont la `publishDate` est future (`buildFuture = false`), sinon ils ne sortiraient jamais tout seuls.

Le build n'utilise **pas** `--baseURL` : le `baseURL` du `hugo.toml` fait foi, ce qui evite de generer des URLs `github.io` si la configuration du custom domain n'est pas encore lue par l'action.

## Points de vigilance

- **Un blog = un seul auteur.** Ne jamais ajouter `helene-vasseur` ou `marion-kieffer` dans `data/authors.yaml`.
- **Aucun lien** vers les autres sites du parc ni vers une cible, tant que Damien ne l'a pas decide explicitement.
- **Pages de categorie** : le dossier doit porter le terme accentue, l'URL sort sans accents (`removePathAccents`).
- **`llms.txt` est genere par Hugo** (output format `LLMS`), il se met a jour tout seul a chaque publication. Ne pas le recreer en fichier statique.
