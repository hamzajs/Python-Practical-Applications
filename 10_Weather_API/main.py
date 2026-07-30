"""Weather API Client.

This script retrieves the current weather information for a city using the
OpenWeatherMap API. It asks the user for a city name, builds a request URL,
fetches the JSON response, extracts key weather metrics, and displays them in
metric units.

Features:
- Search by city name
- Fetch current weather data from an external API
- Display temperature, humidity, pressure, and weather description
- Handle invalid city names gracefully
"""

import json
import requests

# API configuration for OpenWeatherMap
# Replace this value with your real API key from OpenWeatherMap.
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Validate that the API key was actually configured before running the request.
if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
    print("Please replace 'YOUR_API_KEY_HERE' with your OpenWeatherMap API key.")
    raise SystemExit

# Ask the user for a city name and normalize the input for a cleaner request.
city_name = input("Enter the city you want to its weather? ").lower().strip()

# Build the final request URL with the city name, metric units, and API key.
complete_url = f"{BASE_URL}q={city_name}&units=metric&appid={API_KEY}"

# Send the HTTP GET request to the weather API.
response = requests.get(complete_url)
response.raise_for_status()

# Convert the JSON response text into a Python dictionary.
weather_data = json.loads(response.text)

# Check whether the API reports the city as not found.
if weather_data["cod"] != "404":
    # Extract the main weather metrics from the API response.
    main_metrics = weather_data["main"]
    current_temperature = main_metrics["temp"]
    current_pressure = main_metrics["pressure"]
    current_humidity = main_metrics["humidity"]

    # Extract the weather description from the list of conditions.
    weather_details = weather_data["weather"]
    weather_description = weather_details[0]["description"]

    # Display weather information for the user.
    print(f"Temperature (in metric unit): {current_temperature}")
    print(f"Atmospheric pressure (in hPa unit): {current_pressure}")
    print(f"Humidity (in percentage): {current_humidity}")
    print(f"Description: {weather_description}")
else:
    # Handle the invalid city case.
    print("City Not Found")