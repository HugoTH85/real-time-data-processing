import json
from kafka import KafkaConsumer
import streamlit as st
from dashboards import dashboard
from environment import *
from time import time

# Function to process weather data from Kafka message
def process_weather_data(message, placeholder):
    placeholder.empty()  # Clear the previous content
    with placeholder.container():
        # Set the message value
        st.write(f'time: {time()}')

        data = message.value

        # Update the Streamlit app with the weather data
        col1, col2, col3 = st.columns(3)
        col1.metric("Location", data['location_name'], f"{data['region']}, {data['country']}")
        col2.metric("Weather", data['condition_text'])
        col3.metric("UV Index", data['uv_index'])

        col1.metric(label="Temperature (°C)", value=f"{data['temperature_c']} °C", delta=f"Feels like {data['feelslike_c']} °C")
        col2.metric(label="Temperature (°F)", value=f"{data['temperature_f']} °F", delta=f"Feels like {data['feelslike_f']} °F")
        col3.metric("Wind", f"{data['wind_kph']} kph / {data['wind_mph']} mph", f"Direction: {data['wind_dir']} ({data['wind_degree']}°)")

        col1.metric("Pressure", f"{data['pressure_mb']} mb / {data['pressure_in']} in")
        col2.metric("Precipitation", f"{data['precipitation_mm']} mm / {data['precipitation_in']} in")
        col3.metric("Humidity", f"{data['humidity']}%")

        col1.metric("Cloud Coverage", f"{data['cloud']}%")
        col2.metric("Dew Point (°C)", f"{data['dewpoint_c']} °C / {data['dewpoint_f']} °F")
        col3.metric("Visibility", f"{data['visibility_km']} km / {data['visibility_miles']} miles")

        col1.metric("Wind Gust", f"{data['gust_kph']} kph / {data['gust_mph']} mph")
        col2.metric("Is Day?", "Yes" if data['is_day'] == 1 else "No")
        col3.metric("Local Time", data['localtime'])

        st.success(f"Last updated: {data['last_updated']}")

# Function to consume messages from Kafka topic
def consume_kafka_messages():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )

    placeholder = st.empty()  # Create a placeholder for dynamic updates

    for message in consumer:
        process_weather_data(message, placeholder)

# Update the Streamlit app with data from the background thread
if __name__ == '__main__':
    # Streamlit dashboard
    dashboard("consumer")

    # Consume Kafka messages
    consume_kafka_messages()
