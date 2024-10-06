import json
from kafka import KafkaConsumer
import streamlit as st
from dashboards import dashboard
from environment import *
from time import time
from itertools import islice

# Function to process weather data from Kafka message
def process_stock_data(message, placeholder):
    placeholder.empty()  # Clear the previous content
    with placeholder.container():
        # Set the message value
        st.write(f'time: {time()}')

        data = message.value
        
        time_series_data = data.get("Time Series (5min)", {})
        
        time_series_items = list(time_series_data.items())

        for timestamp, stock_values in islice(time_series_items, 1, None):  # Start from the second item
            st.write(f"Stock data for {timestamp}")

            # Display key stock data metrics
            col1, col2, col3 = st.columns(3)
            col1.metric("Open Price", stock_values.get('1. open', 'N/A'))
            col2.metric("High Price", stock_values.get('2. high', 'N/A'))
            col3.metric("Low Price", stock_values.get('3. low', 'N/A'))

            col1.metric("Close Price", stock_values.get('4. close', 'N/A'))
            col2.metric("Volume", stock_values.get('5. volume', 'N/A'))
		


# Function to consume messages from Kafka topic
def consume_kafka_messages():
    consumer = KafkaConsumer(
        KAFKA_TOPIC_FINANCE,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )

    placeholder = st.empty()  # Create a placeholder for dynamic updates

    for message in consumer:
        process_stock_data(message, placeholder)

# Update the Streamlit app with data from the background thread
if __name__ == '__main__':
    # Streamlit dashboard
    dashboard("consumer")

    # Consume Kafka messages
    consume_kafka_messages()
