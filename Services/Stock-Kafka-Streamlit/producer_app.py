import json
import threading
import time
from kafka import KafkaProducer
import streamlit as st
from date import fetch_stock_data
from dashboards import dashboard
from environment import *
import logging
import requests

# Kafka producer
def produce_kafka_messages(date):
    # Create a Kafka producer
    st.write(f'Broker = {KAFKA_BROKER}')
    st.write(f'Topic = {KAFKA_TOPIC_FINANCE}')

    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
    stock_data = fetch_stock_data(date)

    if stock_data:
        # Extracting the time series data from the stock data
        time_series = stock_data.get("Time Series (5min)", {})
        
        for timestamp, data in time_series.items():
            # Reformat the data to match Elasticsearch and Kibana expected format
            formatted_data = {
                "timestamp": timestamp,  # Use the timestamp from the stock data
                "open": float(data["1. open"]),
                "high": float(data["2. high"]),
                "low": float(data["3. low"]),
                "close": float(data["4. close"]),
                "volume": int(data["5. volume"])
            }

            # Convert to JSON and encode for Kafka
            message = json.dumps(formatted_data).encode("utf-8")

            # Send the message to Kafka
            producer.send(KAFKA_TOPIC_FINANCE, message)

        st.write("Stock data produced to Kafka.")

    # Close the producer after sending all messages
    producer.close()
return 1;


if __name__ == '__main__':

    dashboard("producer")

    # Display input field
    month = st.text_input('Month (YYYY-MM)', autocomplete="off")

    # Display call-to-action button
    action = st.button('Start producing finance data to Kafka')
    stop_action = st.button('Stop producing finance data to Kafka')

    if action:
        message = produce_kafka_messages(month)
        with open("/tmp/mongo-sink-stock.json", 'r') as json_file:
            data = json_file.read()
        response = requests.post("http://kafka-connect:8083/connectors", headers={"Content-Type": "application/json"}, data=data)
        if message:
            st.success("Finance data produced to Kafka.")
        else:
            st.error("Error producing data to Kafka.")
