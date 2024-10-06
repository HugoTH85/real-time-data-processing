import streamlit as st


# Streamlit app
def dashboard(dashboard_type: str):
    # Default settings
    st.set_page_config(
        page_title="Domain name data retriever",
        page_icon="",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Run the Streamlit app
    st.title(str.upper(dashboard_type) + " : Domain Name Data Retriever")

    # Add Logo
    st.sidebar.image("images/logo.png", width=250)

    # Sidebar with user instructions
    st.sidebar.markdown(
        """
        This app fetches domain name data from IPinfo APIs.
        This produce messages to the Kafka topic and consume messages from the Kafka topic, 
        then displays real-time weather data from Kafka messages.
        """
    )

    # Display weather data in the main section
    st.header("Domain Name Data Retriever with Kafka + Streamlit")
