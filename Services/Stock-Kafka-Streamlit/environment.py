# from dotenv import load_dotenv
# import os

# # take environment variables from .env
# load_dotenv()

# # AccuWeather API key
# WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# # Alpha Vantange API key
# STOCK_API_KEY = os.getenv("STOCK_API_KEY")

# # Kafka broker address
# KAFKA_BROKER = os.getenv("KAFKA_BROKER")

# # Kafka topic
# KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# # Kafka topic finance
# KAFKA_TOPIC_FINANCE = os.getenv("KAFKA_TOPIC_FINANCE")

# # Kafka Group Id
# KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")

import yaml

with open('env.yml', 'r') as file:
    prime_service = yaml.safe_load(file)

WEATHER_API_KEY = prime_service["WEATHER_API_KEY"]
STOCK_API_KEY = prime_service["STOCK_API_KEY"]
KAFKA_BROKER = prime_service["KAFKA_BROKER"]
KAFKA_TOPIC = prime_service["KAFKA_TOPIC"]
KAFKA_TOPIC_FINANCE = prime_service["KAFKA_TOPIC_FINANCE"]
KAFKA_GROUP_ID = prime_service["KAFKA_GROUP_ID"]




