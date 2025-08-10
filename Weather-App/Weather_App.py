# Import necessary libraries
import os, requests, json
from dotenv import load_dotenv, find_dotenv
load_dotenv()

# This script fetches weather data for a given city using the Weatherstack API.
api_key = os.getenv("weatherstack_api_key")  # Replace with your actual API key
if not api_key: # Check if the API key is set
    raise ValueError("API key is missing. Check .env file.")

# Get user input for the city
user_input = input("Enter city: ")

# Fetch weather data from Weatherstack API
weather_data = requests.get(f"http://api.weatherstack.com/current?query={user_input}&units=f&access_key={api_key}")

# Pull out relevant data from the JSON response
location = weather_data.json()['location']['name']
weather = weather_data.json()['current']['weather_descriptions'][0]
temperature = weather_data.json()['current']['temperature']
uv_index = weather_data.json()['current']['uv_index']

# Print the weather information
print(location, weather, temperature, "°F","UV Index",uv_index)

