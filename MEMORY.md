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

## Semaine du 2026-09-16

**5 articles publies (FR + EN), un par rubrique, en publication immediate.** Lot demande explicitement par Damien le 2026-09-16, produit en mode A de `/create-article-seo` (roadmap du blog, 5 entrees `todo` les plus anciennes) mais avec `publishDate` ramenee au jour meme au lieu des `scheduled_date` du 15 au 29 septembre. Les entrees passent donc directement en `status: done` dans la roadmap, leur `scheduled_date` d'origine etant conservee pour garder la trace de l'ecart.

**Troisieme ecart au repere hebdomadaire de 4 articles/semaine**, apres ceux du 2026-09-06 et du 2026-09-12 qui etaient annonces comme les deux derniers. Celui-ci est une demande directe, pas une decision de la skill. Le rythme de 2 par semaine reste la cible.

| Article FR | Categorie | Mot-cle cible | Volume |
|---|---|---|---|
| [Smoothie fruits rouges : les proportions](https://www.brunch-story.fr/blog/smoothie-fruits-rouges/) | Boissons du matin | `smoothie fruits rouges` | 2 769 |
| [Pain perdu sans œuf : la methode](https://www.brunch-story.fr/blog/pain-perdu-sans-oeuf/) | Oeufs et sale | `pain perdu sans oeuf` | 2 417 |
| [Petit dejeuner turc : ce qu'il y a dessus](https://www.brunch-story.fr/blog/petit-dejeuner-turc/) | Organiser un brunch | `petit dejeuner turc` | 1 600 |
| [Bienfaits des graines de chia : les faits](https://www.brunch-story.fr/blog/bienfaits-graines-de-chia/) | Petit dejeuner sain | `bienfaits des graines de chia` | 1 900 |
| [Recette brioche a l'ancienne : la methode](https://www.brunch-story.fr/blog/recette-brioche-a-l-ancienne/) | Pancakes et sucre | `recette brioche a l'ancienne` | 2 700 |

Les 5 versions EN sont publiees sous `/en/blog/` : `berry-smoothie`, `eggless-french-toast`, `turkish-breakfast`, `chia-seed-benefits`, `old-fashioned-brioche`. Maillage croise entre les 5 articles du lot, 4 a 5 liens internes contextuels par article, tous verifies sur le site genere.

**Analyse SERP en mode degrade assume** : le MCP `serpapi` n'est pas declare cote perso, donc l'analyse s'est faite par recherche web (titres et snippets), sans fetch des concurrents. Aucun geant ne tient le top 3 sur les 5 requetes.

**Images : 2 rejets sur 5 au controle visuel**, ce qui confirme la mesure du 2026-09-12. `berry smoothie` a remonte un gobelet McDonald's McCafe, et `brioche bread` un rayon de supermarche avec des sachets Reflets de France : deux visuels de marque qui contredisent en plus l'angle « ce qui se refait mieux chez soi ». Relancer le script avec une autre query ne suffit pas toujours : le registre `hero-sources.json` n'exclut que les photos utilisees par un AUTRE slug, donc un second passage sur le meme slug peut retomber sur la photo rejetee (c'est arrive pour la brioche). La parade est de chercher directement dans l'API Commons et de deposer l'image a la main, puis de corriger l'entree du registre.

**Piege de fuseau horaire sur `publishDate`** : une date seule (`"2026-09-16"`) est lue par Hugo comme minuit **UTC**. Ecrite depuis Paris entre minuit et 2 h du matin, elle est donc dans le futur et `buildFuture: false` masque l'article, sans aucune erreur au build. Le correctif applique est une date horodatee avec fuseau explicite (`"2026-09-15T23:00:00+02:00"`), `date` et `lastmod` restant au 2026-09-16 puisque c'est `.Date` que le theme affiche.

**A traiter, defaut anterieur au lot** : sur toutes les pages EN, les liens de tags pointent vers `/tags/<slug-en>/` au lieu de `/en/tags/<slug-en>/`, soit **63 liens internes en 404**. Les pages cibles existent bien sous `/en/tags/`. La cause est une URL ecrite en dur dans `themes/brunch-story/layouts/_default/single.html` ligne 92 (`{{ "/tags/" | relURL }}`), qui ignore la langue courante. Le defaut touchait deja les 10 articles EN publies avant ce lot, il n'a pas ete corrige ici pour ne pas melanger un changement de theme a une publication.
