from dotenv import load_dotenv
import os
import requests

def get_weather(city_name: str) -> str:
    """
    Fetches current weather information for a given city using OpenWeatherMap API.

    Args:
        city_name (str): City name and optional country code (e.g., "Paris,FR").

    Returns:
        str: A formatted weather summary string or an error message.
    """

    # Load environment variables from .env file
    load_dotenv()

    # Retrieve API key from environment
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "Error: OPENWEATHER_API_KEY not found in environment variables."

    # Base URL for OpenWeatherMap API
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API call
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",  # Use "imperial" for Fahrenheit
        "lang": "en",       # or "pt_br" if quiser em português
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx

        data = response.json()

        # Extract relevant information
        city = data.get("name", city_name)
        weather = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        return f"Weather in {city}: {weather}, {temperature}°C (feels like {feels_like}°C)."

    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except (KeyError, IndexError):
        return "Error: Unexpected response structure from weather API."