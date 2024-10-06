# Projet Kafka Streamlit Météo

Ce projet permet de récupérer des données météo, des informations concernant un nom de domaine sur l'Internet et les données OHLCV du marché américain sur un mois en temps réel et de les envoyer dans Kafka via un producteur, les affiche sur une interface Kibana, tout en consommant ces données via une base de données mongodb, le tout avec une interface graphique développée avec Grafana.

## Structure du projet

### Configuration du fichier `env.yml`

Vous devez configurer les variables d'environnement pour le broker Kafka et les API météo.
Rendez-vous sur les sites indiqués pour générer vos propres clés API pour les producers Weather et Log.
Créez un fichier **`env.yml`** dans le répertoire **`./Services/Producers/`** avec les informations suivantes :

```yml
WEATHER_API_KEY : "your_api_key"            # A retrouver sur https://www.weatherapi.com    
STOCK_API_KEY : "demo"                      # API de test pour le producer stock
KAFKA_BROKER : "kafka:29092"                # Adresse du serveur Kafka
KAFKA_TOPIC : "weather_data"                # Nom du topic Kafka
KAFKA_TOPIC_FINANCE : "stock_data"          # Nom du topic Kafka
KAFKA_TOPIC_LOG : "log_data"                # Nom du topic Kafka
LOG_API_KEY : "your_api_key"                # A retrouver sur ipinfo.io
```

### Producer Weather-Kafka-Streamlit

Ce producer permet la génération de données météorologiques d'une ville.
Les fichiers de configuration du producer se trouve dans le répertoire **`./Services/Producers/Weather-Kafka-Streamlit`**.
Pour accéder à ce service : **`localhost:8501`**

### Producer Stock-Kafka-Streamlit

Ce producer permet la génération de données
Les fichiers de configuration du producer se trouve dans le répertoire **`./Services/Producers/Stock-Kafka-Streamlit`**.
Pour accéder à ce service : **`localhost:8502`**

### Producer Log-Kafka-Streamlit

Les fichiers de configuration du producer se trouve dans le répertoire **`./Services/Producers/Log-Kafka-Streamlit`**.
Pour accéder à ce service : **`localhost:8503`**

### Exécution du projet

Dans un terminal pointant sur la racine du projet, exécutez la commande :

```bash
docker compose up -d
```

### Accès aux autres services

Après avoir exécuté la commande précédente, vous pouvez commencer à manipuler les interfaces et environnements ci-dessous :

1. **Kafka**
   - **URL** : [http://localhost:9092](http://localhost:9092)
   - **Description** : Accessible par navigateur, Apache Kafka est la plateforme de streaming utilisée pour transmettre les données des producers en temps réel. Il agit comme le centre de la chaîne de traitement des données.

2. **ElasticSearch**
   - **URL** : [http://localhost:9200](http://localhost:9200)
   - **Description** : ElasticSearch est utilisé pour stocker les données indexées. Les données transmises à partir de Kafka sont ingérées par ElasticSearch pour permettre des recherches efficaces.

4. **Logstash**
   - **URL** : [http://localhost:5044](http://localhost:5044)
   - **Description** : Logstash est utilisé pour ingérer des données de différentes sources, ici de MongoDB, et les envoyer vers ElasticSearch pour l'indexation.

5. **MongoDB**
   - **URL** : [http://localhost:27017](http://localhost:27017)
   - **Description** : MongoDB stocke les données météorologiques recuillis avec kafka. C'est une base de données NoSQL.
   
   - **Acceder à la db**: 
        ```bash
        docker exec -it <container_id> mongo
        ```
   - **Commandes utiles**:
      ```bash
      show dbs                                  # Afficher les bases de données
      use kafka_topics                          # Sélectionner la base de données kafka_topics
      show collectitons                         # Afficher les collections de la base de données
      db.<collection_name>.find().pretty()      # Afficher les données d'une collection
      ```

6. **Kafdrop**
   - **URL** : [http://localhost:9000](http://localhost:9000)
   - **Description** : Kafdrop est une interface web qui permet de visualiser les topics, les messages, et les consommateurs dans Kafka. Il fournit une vue d'ensemble du système Kafka en temps réel.

7. **Kibana**
   - **URL** : [http://localhost:5061](http://localhost:5061)
   - **Description** : Kibana est l'interface web visuelle d'ElasticSearch, utilisée pour créer des tableaux de bord et visualiser les données. Il est souvent utilisé pour monitorer et analyser les données météorologiques ingérées. Dans le cadre de ce projet, il est utilisé pour visualiser les donénes de Mongodb.

8. **MongoDB Exporter**
   - **URL** : [http://localhost:9216](http://localhost:9216)
   - **Description** : MongoDB Exporter est utilisé pour exporter des métriques MongoDB afin qu'elles puissent être monitorées par Prometheus. A noter qu'il peut être accessible sur navigateur.

9. **Grafana**
   - **URL** : [http://localhost:3000](http://localhost:3000)
   - **Description** : Grafana est un outil de visualisation et de monitoring qui permet de créer des tableaux de bord pour monitorer les performances des systèmes, en récupérant les données depuis Prometheus, ElasticSearch, etc. Ici elle est utilisé pour des visualisation de monitoring de la base de données.
   - **Code de connection**:
        - **user**: admin
        - **password**: grafana

10. **Prometheus**
    - **URL** : [http://localhost:9090](http://localhost:9090)
    - **Description** : Prometheus est une solution de monitoring et d'alerting. Il recueille des métriques à partir de diverses sources, comme MongoDB Exporter, et les enregistre pour visualisation dans Grafana.

11. **Kafka Connect**
    - **URL** : [http://localhost:35000](http://localhost:35000)
    - **Description** : Kafka Connect est une plateforme d'intégration permettant de connecter Kafka à d'autres systèmes comme MongoDB, Elasticsearch, etc., sans avoir à écrire de code.