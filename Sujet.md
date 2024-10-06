# TP (noté) : Plateforme de Streaming de Données en Temps Réel avec Apache Kafka 

## Introduction

Le ***TP*** vise à concevoir et mettre en œuvre une plateforme de streaming de données en temps réel à l'aide d'***Apache Kafka***. La plateforme permettra la collecte, le traitement, le stockage et l'analyse de flux de données provenant de diverses sources, avec un accent sur la scalabilité, la résilience et les performances.

## Objectifs

- Déployer un ***cluster Kafka*** pour la gestion des flux de données.
- Développer des producteurs de données pour simuler différentes sources de données.
- Implémenter des consommateurs pour traiter les données en temps réel.
- Intégrer des outils pour le stockage, l'analyse et la visualisation des données.

## Architecture

### Composants du TP

### 1. Cluster Kafka

***Installation et Configuration :*** Installer ***Apache Kafka*** sur un ensemble de ***machines virtuelles*** ou ***conteneurs Docker***. Configurer le ***cluster Kafka*** avec ***plusieurs brokers*** pour garantir la redondance et la scalabilité.

***Gestion des Topics :*** Créer des ***topics Kafka*** pour représenter les différentes sources de données à surveiller. Configurer les partitions et les réplicas pour chaque topic en fonction des besoins de scalabilité et de tolérance aux pannes.

***Sécurité :*** Configurer la sécurité dans ***Kafka*** en utilisant ***SSL/TLS*** pour le chiffrement des communications et ***SASL*** pour l'authentification des clients.

### 2. Producteurs de Données

***Simulation de Sources de Données :*** Développer des producteurs de données pour simuler différents types de flux de données :

- Un producteur pour simuler des journaux d'accès web avec des informations sur les requêtes ***HTTP***, ***les adresses IP***, les temps de réponse, etc.
- Un producteur pour simuler des données de capteurs ***IoT*** avec des mesures de température, d'humidité, etc.
- Un producteur pour simuler des transactions financières avec des informations sur les montants, les comptes concernés, etc.

***Envoi de Données à Kafka :*** Configurer les producteurs pour envoyer les données générées aux ***topics Kafka*** correspondants. Utiliser la bibliothèque ***Kafka Producer API*** pour garantir la fiabilité et la haute performance de l'envoi des données.

### 3. Consommateurs de Données

***Traitement en Temps Réel :*** Implémenter des consommateurs de données pour effectuer des opérations de traitement en temps réel :

- Utiliser ***Kafka Streams*** pour effectuer des transformations, des agrégations et des fenêtrages sur les flux de données.

- Appliquer des filtres et des opérations de jointure pour enrichir les données avec des informations supplémentaires.

- Intégration avec des Bases de Données : Intégrer des bases de données ***NoSQL*** comme ***Apache Cassandra*** ou ***MongoDB*** pour stocker les données traitées :

  - Configurer ***les connecteurs Kafka*** pour synchroniser les données entre ***Kafka*** et les bases de données de stockage.

### 4. Analyse et Visualisation

***Analyse en Temps Réel :*** Utiliser des outils d'analyse de données comme ***Apache Spark Streaming*** ou ***Apache Flink*** pour effectuer des analyses en temps réel sur les flux de données :

- Calculer des statistiques en temps réel telles que les moyennes, les maxima, les minima, etc.
- Détecter des modèles et des anomalies dans les flux de données.

***Tableaux de Bord Interactifs :*** Créer des tableaux de bord interactifs avec des outils de visualisation comme ***Grafana*** ou ***Kibana*** :

- Afficher des graphiques en temps réel des métriques surveillées.
- Configurer des alertes pour notifier les utilisateurs en cas de conditions anormales ou critiques.

### Déploiement et Documentation

***Configuration et Déploiement :*** Fournir des scripts de configuration et de déploiement pour faciliter le déploiement de la plateforme sur différents environnements (local, cloud, etc.). Automatiser autant que possible les tâches de configuration et de déploiement à l'aide d'outils d'infrastructure-as-code comme ***Ansible*** ou ***Terraform***.

***Documentation :*** Rédiger une documentation détaillée sur l'architecture de la plateforme, les composants utilisés et les flux de données. Inclure des guides d'installation, des tutoriels et des exemples de code pour aider les utilisateurs à comprendre et à utiliser la plateforme.

## Quelques API pour la collecte de données

### 1. API REST pour les Données de Capteurs IoT

***API IoT Weather:*** Fournit des données météorologiques en temps réel, telles que la température, l'humidité, la pression atmosphérique, etc.

- Site Web : https://www.weatherapi.com/

- Exemple d'endpoint : https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London

***API OpenAQ:*** Fournit des données sur la qualité de l'air provenant de stations de surveillance dans le monde entier.

- Site Web : https://openaq.org

- Exemple d'endpoint : https://api.openaq.org/v1/latest?city=Paris&parameter=pm25

### 2. API REST pour les Données de Trafic Routier

***API TomTom Traffic:*** Fournit des informations sur le trafic routier en temps réel, y compris les temps de trajet, les incidents, les embouteillages, etc.

- Site Web : https://developer.tomtom.com/traffic-api/traffic-api-documentation

- Exemple d'endpoint : https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key=YOUR_API_KEY&point=48.77538,9.165247

***API Google Maps Traffic:*** Fournit des données sur le trafic routier en temps réel à partir de ***Google Maps***.

- Site Web : https://developers.google.com/maps/documentation/traffic-data

- Exemple d'endpoint : https://maps.googleapis.com/maps/api/distancematrix/json?origins=Chicago,IL&destinations=Los+Angeles,CA&departure_time=now&traffic_model=best_guess&key=YOUR_API_KEY

### 3. API REST pour les Données de Réseaux Sociaux

***Twitter API:*** Permet d'accéder aux tweets en temps réel ainsi qu'à diverses informations sur les utilisateurs, les tendances, etc.

- Site Web : https://developer.twitter.com/en/docs/twitter-api

- Exemple d'endpoint : https://api.twitter.com/2/tweets/sample/stream

***Facebook Graph API:*** Permet d'accéder aux publications, aux commentaires, aux likes, etc., sur ***Facebook***.

- Site Web : https://developers.facebook.com/docs/graph-api

- Exemple d'endpoint : https://graph.facebook.com/{user-id}/posts?access_token=YOUR_ACCESS_TOKEN

### 4. API REST pour les Données de Finance

***Alpha Vantage API:*** Fournit des données sur les marchés financiers, y compris les prix des actions, les volumes de négociation, etc.

- Site Web : https://www.alphavantage.co/documentation/

- Exemple d'endpoint : https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=YOUR_API_KEY

***Yahoo Finance API:*** Permet d'accéder à diverses informations financières, telles que les cours des actions, les indices boursiers, etc.

- Site Web : https://finance.yahoo.com/

- Exemple d'endpoint : https://query1.finance.yahoo.com/v8/finance/chart/GOOG?period1=0&period2=9999999999&interval=1d

## Exemple d'aplication

[Cliquez ici SVP](./METEO_KAFKA_STREAMLIT/)

## Conclusion

Ce ***TP*** vous permettra de développer une solide compréhension des concepts de streaming de données en temps réel et de leur mise en œuvre pratique à l'aide d'***Apache Kafka***. Ils acquerront également des compétences précieuses en matière de configuration, de développement et de déploiement de solutions de streaming de données dans des environnements réels.

***Good Luck*** 🙂