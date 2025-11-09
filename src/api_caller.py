import requests


def generate_url(lat, longi):
    return "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(longi) + "&hourly=temperature_2m"

def print_results(lat, longi):
    try:
        response = requests.get(generate_url(lat, longi))
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        print("Data:", data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

print_results(50, 50)