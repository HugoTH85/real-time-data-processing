import socket
import json
import threading
import time
import requests
from kafka import KafkaProducer
import streamlit as st
from dashboards import dashboard
from environment import *
import logging

# Fonction pour obtenir l'adresse IP à partir d'un domaine DNS
def get_ip_from_dns(domain: str) -> str:
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        st.error(f"Erreur lors de la récupération de l'IP pour le domaine {domain}: {e}")
        return None

# Fonction pour obtenir les informations de localisation à partir de l'adresse IP
def get_location_from_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}?token={API_KEY}")
        return response.json()
    except Exception as e:
        st.error(f"Erreur lors de la récupération de la localisation pour l'IP {ip}: {e}")
        return None

# Fonction principale pour récupérer les données DNS
def fetch_data_from_dns(dns_address: str):
    ip = get_ip_from_dns(dns_address)
    location_info = get_location_from_ip(ip) if ip else None
    coordinates = list(map(float, location_info["loc"].split(",")))
    data = {
        "dns_address": dns_address,
        "ip_address": ip,
        "hostname": location_info.get("hostname", "Unknown") if location_info else "Unknown",
        "coordinates":coordinates,
        "city": location_info.get("city", "Unknown") if location_info else "Unknown",
        "country": location_info.get("country", "Unknown") if location_info else "Unknown",
        "postal": location_info.get("postal", "Unknown") if location_info else "Unknown",
        "region": location_info.get("region", "Unknown") if location_info else "Unknown",
        "zone": location_info.get("timezone", "Unknown") if location_info else "Unknown",
        "isp": location_info.get("org", "Unknown") if location_info else "Unknown",
    }
    
    return data

# Kafka producer
def produce_kafka_messages(dns_address):
    st.write(f'Broker = {KAFKA_BROKER}')
    st.write(f'Topic = {KAFKA_TOPIC}')

    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    dns_data = fetch_data_from_dns(dns_address)
    if dns_data:
         # Send DNS data to Kafka topic
        producer.send(KAFKA_TOPIC, dns_data)
        st.write("DNS data produced to Kafka:", dns_data)
    # Wait 10 seconds before the next request
    time.sleep(10)
    producer.close()

if __name__ == '__main__':
    dashboard("producer")

    # Display input field
    dns_address = st.text_input('DNS Address', autocomplete="off")

    # Display call-to-action buttons
    action = st.button('Start producing DNS data to Kafka')

    if action:
        message = produce_kafka_messages(dns_address)
        with open("/tmp/mongo-sink-log.json", 'r') as json_file:
            data = json_file.read()
        response = requests.post("http://kafka-connect:8083/connectors", headers={"Content-Type": "application/json"}, data=data)
        if message:
            st.success("DNS data produced to Kafka.")
        else:
            st.error("Error producing data to Kafka.")

