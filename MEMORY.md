# Suivi des publications — Brunch Story

Journal des articles publies, classes par semaine. Mis a jour par `/create-article-geo` et `/create-article-seo`.

Repere indicatif : 4 articles par semaine, jamais bloquant.

## Semaine du 2026-09-06

Lancement du blog, 5 articles publies le meme jour (FR + EN). Ecart assume au repere hebdomadaire : un site neuf n'a aucune position a proteger, et il lui faut un socle par categorie pour que la home et les rubriques ne soient pas vides. **A ne pas reproduire** une fois le site lance, le rythme passe a 2 par semaine via la roadmap.

| Article FR | Categorie | Mot-cle cible |
|---|---|---|
| [Cafe brunch : quelle quantite prevoir et comment le reussir](https://www.brunch-story.fr/blog/cafe-brunch/) | Boissons du matin | `cafe brunch` |
| [C'est quoi un brunch : definition, horaires et composition](https://www.brunch-story.fr/blog/c-est-quoi-un-brunch/) | Organiser un brunch | `c'est quoi un brunch` |
| [Petit dejeuner sans gluten : quoi manger vraiment le matin](https://www.brunch-story.fr/blog/petit-dejeuner-sans-gluten/) | Petit dejeuner sain | `petit dejeuner sans gluten` |
| [Pancakes legers : les proportions et les gestes qui marchent](https://www.brunch-story.fr/blog/pancakes-legers/) | Pancakes et sucre | `pancakes legers` |
| [Oeuf poche : temps de cuisson exact et methode sans ratage](https://www.brunch-story.fr/blog/oeuf-poche-temps-de-cuisson/) | Oeufs et sale | `oeuf poche temps` |

Les 5 versions EN correspondantes sont publiees sous `/en/blog/`.

Suite : voir la semaine du 2026-09-12, la roadmap de 49 entrees a ete remplacee.

## Semaine du 2026-09-12

**Roadmap reconstruite sur le corpus de septembre.** Les 49 entrees baties sur le corpus d'aout (87 mots-cles) sont remplacees par **60 entrees** issues du corpus de septembre (1 906 mots-cles, 632 en longue traine ciblable), soit **72 006 de volume mensuel cible** contre des entrees a 200-700 auparavant. 12 entrees par rubrique, du 2026-09-12 au 2027-03-23, mardi et vendredi.

Filtres : 3 mots ou plus, volume 150 a 3 000, KGR sous 0,6 ; frontiere `gouter-gourmand.fr` respectee (gateaux, cookies, tartes et galette des rois laisses a P02, brioche et pain perdu gardes ici) ; requetes produit a SERP de marques ecartees en frontal ; garde-fou cannibalisation passe contre les 9 articles publies, les 49 anciennes entrees et les 60 nouvelles entre elles. Controles : 0 couple cannibalisant, 0 paire consecutive de meme categorie, au moins 3 categories sur toute fenetre de 5.

**5 articles publies (FR + EN), un par rubrique.** Deuxieme et dernier ecart au repere hebdomadaire, pour la meme raison qu'au lancement : chaque rubrique gagne un second article et sort de l'etat a un seul papier. Le rythme revient ensuite a 2 par semaine.

| Article FR | Categorie | Mot-cle cible | Volume |
|---|---|---|---|
| [Comment faire un smoothie : methode et proportions](https://www.brunch-story.fr/blog/comment-faire-un-smoothie/) | Boissons du matin | `comment faire un smoothie` | 2 636 |
| [Recette avocado toast : la methode et les proportions](https://www.brunch-story.fr/blog/recette-avocado-toast/) | Oeufs et sale | `recette avocado toast` | 1 455 |
| [Plateau petit dejeuner : quantites et composition](https://www.brunch-story.fr/blog/plateau-petit-dejeuner/) | Organiser un brunch | `plateau petit dejeuner` | 1 600 |
| [Petit dejeuner IG bas : les aliments et les valeurs](https://www.brunch-story.fr/blog/petit-dejeuner-ig-bas/) | Petit dejeuner sain | `petit dejeuner IG bas` | 1 900 |
| [Gaufres croustillantes et moelleuses : la methode](https://www.brunch-story.fr/blog/gaufres-croustillantes-moelleuses/) | Pancakes et sucre | `gaufres croustillantes et moelleuses` | 3 000 |

Les 5 versions EN correspondantes sont publiees sous `/en/blog/`. 72 liens internes verifies, aucun casse. Maillage croise entre les 5 articles du lot.

**Images : source changee.** `api.openverse.org` est injoignable depuis le Mac (timeout, et 403 sur `openverse.org`), donc `.claude/scripts/fetch-image.sh` echoue en code 28. Les 5 images viennent de **Wikimedia Commons**, l'une des sources federees par Openverse, via l'API `commons.wikimedia.org/w/api.php`, avec filtrage sur les licences autorisant l'usage commercial (CC0, CC BY, CC BY-SA, domaine public) et exclusion de `-nc` et `-nd`.
