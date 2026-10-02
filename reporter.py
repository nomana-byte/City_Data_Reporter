"""
City Data Reporter

This program asks the user for a city name, retrieves current weather
information from the OpenWeatherMap API, displays the information,
saves it to a CSV file, and reads the CSV file to report stored cities.
"""

import csv
import json

import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_city_name():
    """Ask the user for a non-empty city name."""
    while True:
        city = input("Enter a city name: ").strip()

        if city:
            return city

        print("City name cannot be empty. Please try again.")


def get_weather_data(city, api_key):
    """Retrieve weather data for the specified city."""
    parameters = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(API_URL, params=parameters, timeout=10)

        # Raise an exception for HTTP errors such as 401 or 404.
        response.raise_for_status()

        # Parse the API response using the json library.
        data = json.loads(response.text)

        return data

    except requests.exceptions.HTTPError as error:
        if response.status_code == 404:
            print("Error: City not found.")
        elif response.status_code == 401:
            print("Error: Invalid API key.")
        else:
            print(f"API error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")

    except json.JSONDecodeError:
        print("Error: Could not read the API response.")

    return None


def extract_weather_data(data):
    """Extract the required weather information from API data."""
    return {
        "City": data["name"],
        "Country": data["sys"]["country"],
        "Temperature (C)": data["main"]["temp"],
        "Humidity (%)": data["main"]["humidity"],
        "Description": data["weather"][0]["description"]
    }


def display_weather(weather):
    """Display the weather information in a formatted summary."""
    print("\n--- Current Weather ---")
    print(f"City: {weather['City']}")
    print(f"Country: {weather['Country']}")
    print(f"Temperature: {weather['Temperature (C)']} °C")
    print(f"Humidity: {weather['Humidity (%)']}%")
    print(f"Description: {weather['Description']}")


def save_to_csv(weather, filename="city_data.csv"):
    """Write weather data to the CSV file."""
    fieldnames = [
        "City",
        "Country",
        "Temperature (C)",
        "Humidity (%)",
        "Description"
    ]

    with open(filename, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Add the header only when the file is empty.
        if csv_file.tell() == 0:
            writer.writeheader()

        writer.writerow(weather)

    print(f"\nWeather data saved to {filename}.")


def read_from_csv(filename="city_data.csv"):
    """Read the CSV file and report stored cities and temperatures."""
    try:
        with open(filename, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        print("\n--- CSV Report ---")
        print(f"Number of cities in file: {len(rows)}")

        if rows:
            print("Cities and temperatures:")

            for row in rows:
                print(
                    f"- {row['City']}: "
                    f"{row['Temperature (C)']} °C"
                )
        else:
            print("No cities are currently stored.")

    except FileNotFoundError:
        print(f"{filename} does not exist yet.")


def main():
    """Run the City Data Reporter application."""
    print("=== City Data Reporter ===")

    # Enter the API key without storing it in the source code.
    api_key = input("Enter your OpenWeatherMap API key: ").strip()

    if not api_key:
        print("API key cannot be empty.")
        return

    city = get_city_name()

    data = get_weather_data(city, api_key)

    if data is None:
        return

    weather = extract_weather_data(data)

    display_weather(weather)

    save_to_csv(weather)

    read_from_csv()


if __name__ == "__main__":
    main()