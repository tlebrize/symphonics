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
J'approche les 4h et il me manque pas mal de choses. Je pense que c'est surtout due au temps perdu avec le setup et le learning sur GCP, j'avais jamais utiliser BigQuery tout seul comme ça.

Le plus gros manque c'est que l'api va surement pas tenir la benchmark de 1kkk requetes par jours, si j'avais eu le temps j'aurais mis en place une db tampon et j'aurais gérer la synchro avec un outil comme AirByte mais ça me semble hors sujet.

Le sujet mentionne plusieurs fois "Seulement les paramètres ayant changés doit être sauvegardés en base de données à chaque réception" et "Enregistrement des données dans Google BigQuery de manière optimisée" Sachant que la seule methode d'insert que me laisse utilise BigQuery en free plan est `load_table_from_json` je pense etre passé a coté de quelque chose a ce niveau la.

Mocker les libs GCP me semblait compliqué sans savoir comment elle fonctionne, sur une vrai implementation en test ça me semble etre une bonne idée.

J'ai pas fait de gestion d'erreurs, a choisir les tests me semblait plus importants.
