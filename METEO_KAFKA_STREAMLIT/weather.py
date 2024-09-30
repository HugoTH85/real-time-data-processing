import requests
from environment import WEATHER_API_KEY


# Define a function to fetch location key from AccuWeather API
def fetch_location_key(location: str):
    params = {
        "key": WEATHER_API_KEY,
        "q": location,
    }
    # Construct the API URL
    loc_api = "http://api.weatherapi.com/v1/search.json"

    # Send an API request
    response = requests.get(loc_api, params=params)

    loc_api_data = response.json()

    if response.status_code == 200:
        return loc_api_data

    return False


# Define a function to fetch weather data from AccuWeather API
def fetch_weather_data(location: str):

    loc_api_data = fetch_location_key(location)

    if loc_api_data:
        loc_name = loc_api_data[0]["name"]

        params = {
            "key": WEATHER_API_KEY,
            "q": loc_name,
            "aqi": "no",
        }
        w_api = "http://api.weatherapi.com/v1/current.json"

        # Send another API request
        w_response = requests.get(w_api, params=params)

        # Check if the request was successful
        if w_response.status_code == 200:
            # Parse the JSON response
            data = w_response.json()

            # Extract relevant weather data
            weather_data = {
                "location_name": data['location']['name'],
                "region": data['location']['region'],
                "country": data['location']['country'],
                "latitude": data['location']['lat'],
                "longitude": data['location']['lon'],
                "timezone": data['location']['tz_id'],
                "localtime": data['location']['localtime'],
                "last_updated": data['current']['last_updated'],
                "temperature_c": data['current']['temp_c'],
                "temperature_f": data['current']['temp_f'],
                "is_day": data['current']['is_day'],
                "condition_text": data['current']['condition']['text'],
                "condition_icon": data['current']['condition']['icon'],
                "wind_mph": data['current']['wind_mph'],
                "wind_kph": data['current']['wind_kph'],
                "wind_degree": data['current']['wind_degree'],
                "wind_dir": data['current']['wind_dir'],
                "pressure_mb": data['current']['pressure_mb'],
                "pressure_in": data['current']['pressure_in'],
                "precipitation_mm": data['current']['precip_mm'],
                "precipitation_in": data['current']['precip_in'],
                "humidity": data['current']['humidity'],
                "cloud": data['current']['cloud'],
                "feelslike_c": data['current']['feelslike_c'],
                "feelslike_f": data['current']['feelslike_f'],
                "windchill_c": data['current']['windchill_c'],
                "windchill_f": data['current']['windchill_f'],
                "heatindex_c": data['current']['heatindex_c'],
                "heatindex_f": data['current']['heatindex_f'],
                "dewpoint_c": data['current']['dewpoint_c'],
                "dewpoint_f": data['current']['dewpoint_f'],
                "visibility_km": data['current']['vis_km'],
                "visibility_miles": data['current']['vis_miles'],
                "uv_index": data['current']['uv'],
                "gust_mph": data['current']['gust_mph'],
                "gust_kph": data['current']['gust_kph']
            }
            return weather_data

    return None
