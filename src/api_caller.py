import openmeteo_requests

import pandas as pd
import requests_cache
import requests
from retry_requests import retry


class Meteo_Caller:  
    def request(self, lat, longi):
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
        	"latitude": lat,
        	"longitude": longi,
        	"hourly": "temperature_2m",
        }
        responses = openmeteo.weather_api(url, params=params)
        return responses
    
    def print_first_response(self, responses):
        response = responses[0]
        print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation: {response.Elevation()} m asl")
        print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
	        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	        end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	        freq = pd.Timedelta(seconds = hourly.Interval()),
	        inclusive = "left"
        )}

        hourly_data["temperature_2m"] = hourly_temperature_2m

        hourly_dataframe = pd.DataFrame(data = hourly_data)
        print("\nHourly data\n", hourly_dataframe)

class WeatherBit_Caller:
    def request(self, lat, longi):
        api_url = "https://api.weatherbit.io/v2.0/alerts?lat=" + str(lat) + "&lon=" + str(longi) + "&key=c07bcff2ac0b470b9f392f724847331c"
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")  
            return None;




# Setup the Open-Meteo API client with cache and retry on error


# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below



# Process first location. Add a for-loop for multiple locations or weather models
