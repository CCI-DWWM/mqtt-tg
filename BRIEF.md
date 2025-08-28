# Python : gestion d'objets IoT

Vous voulez mettre à disposition une application présentant les mesures de capteurs IoT installés sur le Loire
En tant que prestataire, votre mission est de comprendre le besoin de l'entreprise et de mettre en place les fonctionnalités demandées.

## Ressources

- [Communauté TTN](https://www.thethingsnetwork.org/community)
- [wiki MQTT](https://fr.wikipedia.org/wiki/MQTT)
- [wiki LoRaWAN](https://fr.wikipedia.org/wiki/LoRaWAN)
- [lib python paho-mqtt](https://pypi.org/project/paho-mqtt/)
- [MQTT explorer](https://mqtt-explorer.com/)
- [MongoDB](https://www.mongodb.com/)
- [MongoDb on windows install](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)
- [GUI Compass](https://www.mongodb.com/fr-fr/products/tools/compass)

## Contexte du projet

Vous êtes chargés de créer une application python qui permette:
* de récupérer les données des capteurs, de les stocker
* de présenter ces mesures dans un service web

## Modalités pédagogiques

### Objectifs :

* Utilisation de MQTT pour récupérer les informations
* Utilisation de mongo pour stocker les informations
* Présentation des informations (de la BDD) dans un service web

### Étapes :

1. Créer un projet github (https://github.com/orgs/CCI-DWWM)
2. Utilisation de librairie paho-mqtt (connection MQTT) pour récupérer les messages des capteurs
3. Installation de mongo DB localement (si possible) et utilisation pour stocker les messages
4. Création d'appli web pour afficher les messages

## Modalités d'évaluation

Construction d'une application web fonctionnelle

## Livrables
Lien vers le code source sur GitHub avec README.md documenté

## Critères de performance
- Le site est fonctionnel
- L’affichage est lisible 
- Les données sont stockées en BDD mongoDB
- traitement des erreurs
- utilisation de dotenv
- respect TOP10 OWASP
- respect des règles RGPD
