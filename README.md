# Projet Kafka Streamlit Météo

Ce projet permet de récupérer des données météo en temps réel et de les envoyer dans Kafka via un producteur, tout en consommant ces données via un consommateur, le tout avec une interface graphique développée avec **Streamlit**.

## Structure du projet

## 1. Configuration du fichier `.env`

Avant de déployer le projet, vous devez configurer les variables d'environnement pour le broker Kafka et les API météo.

Créez un fichier **`.env`** dans le répertoire METEO_KAFKA_STREAMLIT (ou configurez les valeurs dans `environment.py`) avec les informations suivantes :

```env
WEATHER_API_KEY = "votre_clé_API"
KAFKA_BROKER = "kafka:29092"
KAFKA_TOPIC = "weather_data"
KAFKA_GROUP_ID = "weather_consumer_group"
```

Vous pourrez créer une clé API Weather en allant sur [https://www.weatherapi.com/](https://www.weatherapi.com/), en vous créant un compte et en générant une clé API.

Une fois tout cela correctement configuré, RDV dans le répertoire METEO_KAFKA_STREAMLIT et exécuter la commande :

```bash
docker compose up --build
```

## 2 : Vérification des services

Une fois que tous les services sont démarrés, les éléments suivants devraient être accessibles :

- Interface du producteur Streamlit : [http://localhost:8501](http://localhost:8501)

- Interface du consommateur Streamlit : [http://localhost:8502](http://localhost:8502)

- Kafdrop (interface web pour visualiser Kafka) : [http://localhost:9000](http://localhost:9000)