# Symphonics

## TODO
- [x] project setup
- [x] router
- [x] gcp setup
- [x] database
- [x] pub/sub
- [x] report
- [ ] benchmarks
- [ ] optimisations

## Notes
J'approche des 4 heures et il me manque pas mal de choses. Je pense que c'est surtout dû au temps perdu avec le setup et l'apprentissage sur GCP. Je n'avais jamais utilisé BigQuery tout seul comme ça.

Le plus gros manque, c'est que l'API ne va sûrement pas tenir le benchmark de 1 milliard de requêtes par jour. Si j'avais eu le temps, j'aurais mis en place une base de données tampon et j'aurais géré la synchronisation avec un outil comme Airbyte, mais cela me semble hors sujet.

Le sujet mentionne plusieurs fois : "Seulement les paramètres ayant changé doivent être sauvegardés en base de données à chaque réception" et "Enregistrement des données dans Google BigQuery de manière optimisée". Sachant que la seule méthode d'insertion que me laisse utiliser BigQuery en free plan est load_table_from_json, je pense être passé à côté de quelque chose à ce niveau-là.

Mocker les bibliothèques GCP me semblait compliqué sans savoir comment elles fonctionnent. Sur une vraie implémentation en test, cela me semble être une bonne idée.

Je n'ai pas fait de gestion d'erreurs ; à choisir, les tests me semblaient plus importants.