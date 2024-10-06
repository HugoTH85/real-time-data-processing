import json
import threading
import time
from kafka import KafkaProducer
import streamlit as st
from weather import fetch_weather_data
from dashboards import dashboard
from environment import *
import logging
import requests

# Kafka producer function (no Streamlit calls inside)
def produce_kafka_messages(loc, stop_event, messages):
    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])

    while not stop_event.is_set():
        weather_data = fetch_weather_data(loc)
        if weather_data:
            res = json.dumps(weather_data).encode("utf-8")
            producer.send(KAFKA_TOPIC, res)
            # Append message to shared list instead of calling st.write

        time.sleep(2)

    producer.close()

if __name__ == '__main__':
    dashboard("producer")
    location = st.text_input('Location', autocomplete="off")
    action = st.button('Start producing weather data to Kafka')
    stop_action = st.button('Stop producing weather data to Kafka')

    if 'producer_thread' not in st.session_state:
        st.session_state.producer_thread = None
    if 'stop_event' not in st.session_state:
        st.session_state.stop_event = threading.Event()
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display messages produced by Kafka
    for message in st.session_state.messages:
        st.write(message)

    # Start the producer thread when action is clicked
    if action and location:
        st.write(f'Ma location est {location}')
        st.session_state.stop_event.clear()

        if st.session_state.producer_thread is None or not st.session_state.producer_thread.is_alive():
            st.session_state.producer_thread = threading.Thread(target=produce_kafka_messages, args=(location, st.session_state.stop_event, st.session_state.messages))
            st.session_state.producer_thread.start()
            st.success("Started producing weather data to Kafka.")
            with open("/tmp/mongo-sink-weather.json", 'r') as json_file:
                data = json_file.read()
            response = requests.post("http://kafka-connect:8083/connectors", headers={"Content-Type": "application/json"}, data=data)
        else:
            st.warning("Producer is already running.")

    # Stop the producer thread when stop_action is clicked
    if stop_action:
        st.session_state.stop_event.set()
        st.success("Stopped producing weather data to Kafka.")
