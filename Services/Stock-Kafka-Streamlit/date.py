import requests
from environment import STOCK_API_KEY


# Define a function to fetch stock data for a specific month from Alpha Vantage API
def fetch_stock_data(month: str):
    stock_symbol = "IBM"

    if stock_symbol:
        # Define the API parameters
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": "IBM",
            "interval": "5min",
            "month": month,
            "outputsize": "full",
            "apikey": STOCK_API_KEY  # Replace with your actual API key
        }

        # Construct the API URL
        api_url = "https://www.alphavantage.co/query"

        # Send an API request to fetch the stock data
        response = requests.get(api_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the "Time Series" data and filter it by the specified month
            time_series_key = "Time Series (5min)"
            if time_series_key in data:
                time_series_data = data[time_series_key]

		# Loop through each timestamp in the time series
                for timestamp, values in time_series_data.items():
                    data[timestamp] = {
                        "open": values["1. open"],
                        "high": values["2. high"],
                        "low": values["3. low"],
                        "close": values["4. close"],
                        "volume": values["5. volume"]
                        }
                return data

    return None

