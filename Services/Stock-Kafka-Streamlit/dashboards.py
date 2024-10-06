import streamlit as st


# Streamlit app
def dashboard(dashboard_type: str):
    # Default settings
    st.set_page_config(
        page_title="Historic Finance Data App",
        page_icon="$$",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Run the Streamlit app
    st.title(str.upper(dashboard_type) + " : Weather Data")

    # Add Logo
    st.sidebar.image("images/logo.png", width=250)

    # Sidebar with user instructions
    st.sidebar.markdown(
        """
        This app fetches historic finance data from Alpha Vantage APIs.
        This produce messages to the Kafka topic and consume messages from the Kafka topic, 
        then displays historic finance data from Kafka messages.
        This works by month (you enter the wanted month with format YYYY-MM)
        """
    )

    # Display weather data in the main section
    st.header("Historic Finance Data with Kafka + Streamlit")
