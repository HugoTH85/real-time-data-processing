# Projet Kafka Streamlit Météo

Ce projet permet de récupérer des données météo en temps réel et de les envoyer dans Kafka via un producteur, tout en consommant ces données via une base de données mongodb, le tout avec une interface graphique développée avec Grafana.

## Structure du projet

## Configuration du fichier `.yml`

Avant de déployer le projet, vous devez configurer les variables d'environnement pour le broker Kafka et les API météo.

Créez un fichier **`env.yml`** dans le répertoire Weather-Kafka-Streamlit (ou configurez les valeurs dans `environment.py`) avec les informations suivantes :

```yml
WEATHER_API_KEY : "apiKey"                  # A retrouver sur  [weatherapi](https://www.weatherapi.com)    
KAFKA_BROKER : "kafka:29092"                # Adresse du serveur Kafka
KAFKA_TOPIC : "weather_data"                # Nom du topic Kafka
KAFKA_GROUP_ID : "weather_consumer_group"   # Nom de l'identifiant de groupe Kafka
```

Vous pourrez créer une clé API Weather en allant sur [https://www.weatherapi.com/](https://www.weatherapi.com/), en vous créant un compte et en générant une clé API.

Une fois tout cela correctement configuré, RDV dans le répertoire root et exécuter la commande :

```bash
docker compose up --build
```

## Vérification des services

Une fois que tous les services sont démarrés, les éléments suivants devraient être up :

### Services Principaux

1. **Streamlit (Interface Producteur)**
   - **URL** : [http://localhost:8501](http://localhost:8501)
   - **Description** : Streamlit est utilisé comme interface de producteur pour l'entrée des données météorologiques dans le système. Les données sont envoyées dans Kafka via cette interface.
   
2. **Kafka**
   - **URL** : [http://localhost:9092](http://localhost:9092)
   - **Description** : Apache Kafka est la plateforme de streaming utilisée pour transmettre les données météorologiques en temps réel. Il agit comme le centre de la chaîne de traitement des données.

3. **ElasticSearch**
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
        docker exec -it mongo_id mongo
        ```
        - **Commandes utils**:
            ```bash
            show dbs
            use kafka_topics
            show collectitons
            db.${collection_name}.find().pretty()
            ```

### Interfaces Web et Outils de Monitoring

6. **Kafdrop**
   - **URL** : [http://localhost:9000](http://localhost:9000)
   - **Description** : Kafdrop est une interface web qui permet de visualiser les topics, les messages, et les consommateurs dans Kafka. Il fournit une vue d'ensemble du système Kafka en temps réel.

7. **Kibana**
   - **URL** : [http://localhost:5061](http://localhost:5061)
   - **Description** : Kibana est l'interface visuelle d'ElasticSearch, utilisée pour créer des tableaux de bord et visualiser les données. Il est souvent utilisé pour monitorer et analyser les données météorologiques ingérées. Ici il est utilisé pour visualiser les donénes de Mongodb.

8. **MongoDB Exporter**
   - **URL** : [http://localhost:9216](http://localhost:9216)
   - **Description** : MongoDB Exporter est utilisé pour exporter des métriques MongoDB afin qu'elles puissent être monitorées par Prometheus.

9. **Grafana**
   - **URL** : [http://localhost:3000](http://localhost:3000)
   - **Description** : Grafana est un outil de visualisation et de monitoring qui permet de créer des tableaux de bord pour monitorer les performances des systèmes, en récupérant les données depuis Prometheus, ElasticSearch, etc. Ici elle est utilisé pour des visualisation de monitoring de la base de données.
   - **Code de connection**:
        - **user**: admin
        - **password**: grafana

10. **Prometheus**
    - **URL** : [http://localhost:9090](http://localhost:9090)
    - **Description** : Prometheus est une solution de monitoring et d'alerting. Il recueille des métriques à partir de diverses sources, comme MongoDB Exporter, et les enregistre pour visualisation dans Grafana.

## Connecteurs et Extensions

11. **Kafka Connect**
    - **URL** : [http://localhost:35000](http://localhost:35000)
    - **Description** : Kafka Connect est une plateforme d'intégration permettant de connecter Kafka à d'autres systèmes comme MongoDB, Elasticsearch, etc., sans avoir à écrire de code.




## Suite du Projet

Le projet n'est pas encore terminé, et il reste trois parties importantes à finaliser.

### 1. Création des Dashboards

Pour cette étape, vous devrez créer un dashboard dans Kibana :

1. **Créer l'Index Pattern** : 
   - Rendez-vous dans Kibana pour définir un index pattern. Personnellement, j'ai utilisé le `timestamp` pour la création de l'index, ce qui était assez simple. Selon vos données, vous devrez peut-être choisir un autre champ.
   
2. **Créer des Visualisations** :
   - La partie la plus fastidieuse est la création des visualisations dans Kibana. Une fois les visualisations prêtes, ajoutez-les à un dashboard.

3. **Exporter le Dashboard** :
   - Après avoir terminé le dashboard, exportez-le avec la commande suivante :
     ```bash
     curl "localhost:5601/api/kibana/dashboards/export?dashboard=${dashboard_id}" > export.json
     ```
     Cette commande exportera votre dashboard au format JSON.

     Le `dashboard_id` se trouve dans l'URL du dashboard.

4. **Ajouter le Dashboard Exporté** :
   - Une fois le dashboard exporté, placez le fichier JSON dans le répertoire `Services/Weather-Kafka-Streamlit/Dashboard`. 

5. **Remettre en place le Script d'Import** :
   - Utilisez le script `kibana.py` pour réimporter automatiquement le dashboard dans Kibana. Il serait judicieux de factoriser des parties communes (comme le fichier `env.yml`, `environment.py`, etc.) pour optimiser le projet.

### 2. Automatisation des Tâches Manuelles

Il y a un fichier dans `Weather-Kafka` qui nécessite encore une intervention manuelle : `kibana.py`. Ce fichier permet d'importer un dashboard dans Kibana, et l'import inclut automatiquement l'index pattern.

#### Amélioration de l'Automatisation :
- Idéalement, ce processus pourrait être automatisé. Vous pourriez automatiser l'exécution de ce script après que Kibana soit entièrement démarré, pour éviter toute intervention manuelle.

### 3. Fusionner les Différents Producers

Cette étape est probablement la plus simple du projet :

1. **Créer un Nouveau Répertoire** : 
   - Créez un nouveau répertoire dans `Services` pour y placer vos fichiers spécifiques au producer que vous ajoutez.

2. **Dockerfile, Configuration Logstash et Mongo Sink** :
   - Ajoutez un `Dockerfile` dans le nouveau répertoire.
   - Modifiez le fichier de configuration Logstash dans `logstash/conf/` pour y inclure vos nouveaux topics. Vous trouverez déjà un exemple dans ce fichier existant.
   - Assurez-vous d'ajouter vos topics dans la configuration du `mongo-sink` comme suit :
     ```json
     "topics":"topic1,topic2"
     ```

### 4. Automatiser le dashboard grafana

Lorsque l'"on est dans grafana avec le suer: admin et password: grafana et qu'on veut crée un dashbord il suffit de trouver un moyen d'import le `2583_rev2.json` dans `Graphana_dashbord` avec comme data source prometheus et tout devrai marcher