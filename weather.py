import os
import requests


def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENWEATHER_API_KEY environment variable is missing."
        )

    url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(
            url,
            params={"q": city, "appid": api_key},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

    except requests.RequestException as exc:
        raise RuntimeError(
            f"Weather API request failed: {exc}"
        ) from exc

    if "main" not in data:
        raise RuntimeError(
            f"Weather API returned an unexpected response: "
            f"{data.get('message', 'Missing weather data')}"
        )

    temp = data["main"]["temp"] - 273.15
    humidity = data["main"]["humidity"]

    rainfall = data.get("rain", {}).get("1h", 0)

    return temp, humidity, rainfall
