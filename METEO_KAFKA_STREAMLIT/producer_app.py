import json
import threading
import time
from kafka import KafkaProducer
import streamlit as st
from weather import fetch_weather_data
from dashboards import dashboard
from environment import *
import logging

# Kafka producer
def produce_kafka_messages(loc, stop_event):
    # Create a Kafka producer
    st.write(f'Broker = {KAFKA_BROKER}')
    st.write(f'Topic = {KAFKA_TOPIC}')

    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])

    while not stop_event.is_set():
        weather_data = fetch_weather_data(loc)

        if weather_data:
            res = json.dumps(weather_data).encode("utf-8")

            # Send weather data to Kafka topic
            producer.send(KAFKA_TOPIC, res)
            st.write("Weather data produced to Kafka.")

        # Wait 2-3 seconds before the next request
        time.sleep(2)

    producer.close()


if __name__ == '__main__':
    dashboard("producer")

    # Display input field
    location = st.text_input('Location', autocomplete="off")

    # Display call-to-action button
    action = st.button('Start producing weather data to Kafka')
    stop_action = st.button('Stop producing weather data to Kafka')

    # To handle stopping the thread
    if 'producer_thread' not in st.session_state:
        st.session_state.producer_thread = None
    if 'stop_event' not in st.session_state:
        st.session_state.stop_event = threading.Event()

    # Start the producer thread when action is clicked
    if action and location:
        st.write(f'Ma location est {location}')
        
        # Clear any previous stop event
        st.session_state.stop_event.clear()

        if st.session_state.producer_thread is None or not st.session_state.producer_thread.is_alive():
            st.session_state.producer_thread = threading.Thread(target=produce_kafka_messages, args=(location, st.session_state.stop_event))
            st.session_state.producer_thread.start()
            st.success("Started producing weather data to Kafka.")
        else:
            st.warning("Producer is already running.")

    # Stop the producer thread when stop_action is clicked
    if stop_action:
        st.session_state.stop_event.set()
        st.success("Stopped producing weather data to Kafka.")
