# City Data Reporter

## Project Overview

City Data Reporter is a Python command-line application that retrieves live weather information for a city using the OpenWeatherMap API.

The program asks the user to enter a city name, retrieves current weather data from the API, processes the JSON response, displays the weather information, saves the data to a CSV file, and reads the CSV file to report the cities and their temperatures.

## Features

The program provides the following functionality:

* Prompts the user to enter a city name.
* Validates the city name and does not continue when the input is empty.
* Connects to the OpenWeatherMap API using the `requests` library.
* Uses the `json` library to parse the API response.
* Extracts the following information:

  * City name
  * Country code
  * Temperature in Celsius
  * Humidity percentage
  * Weather description
* Displays a formatted weather report in the terminal.
* Saves weather information to `city_data.csv`.
* Uses the Python `csv` module for CSV file operations.
* Uses `with` statements for safe file handling.
* Reads the stored CSV data and reports the number of cities and their temperatures.
* Handles common API, network, and invalid-input errors.

## Technologies Used

* Python 3
* `requests`
* `json`
* `csv`
* OpenWeatherMap API
* GitHub
* Visual Studio Code

## Project Files

```text
City_Data_Reporter/
│
├── reporter.py
├── city_data.csv
├── README.md
└── .gitignore
```

### reporter.py

Contains the main Python application. It handles user input, API requests, JSON processing, weather data extraction, CSV writing, and CSV reading.

### city_data.csv

Stores the weather information retrieved from the OpenWeatherMap API.

The CSV file contains the following columns:

* City
* Country
* Temperature (C)
* Humidity (%)
* Description

### README.md

Provides project documentation, setup instructions, API-key instructions, and information about how to run the application.

### .gitignore

Contains files and folders that should not be uploaded to GitHub, such as Python cache files and environment files.

## Getting an OpenWeatherMap API Key

The application requires an OpenWeatherMap API key to retrieve live weather information.

To obtain an API key:

1. Visit the official OpenWeatherMap website.
2. Create a free account.
3. Verify the email address associated with the account.
4. Sign in to the OpenWeatherMap account.
5. Open the API Keys section of the account.
6. Copy the API key.

The official OpenWeatherMap documentation is available here:

https://openweathermap.org/appid

**Important:** Never publish your personal API key on GitHub or include it directly in `reporter.py`.

The program asks for the API key when it starts, so the personal key does not need to be stored in the source code.

## Installation

Make sure Python is installed on your computer.

Open a terminal in the project directory and install the `requests` library:

```text
python -m pip install requests
```

To verify that the library is installed:

```text
python -c "import requests; print(requests.__version__)"
```

## How to Run the Program

Open the terminal in the project directory.

Run:

```text
python reporter.py
```

The program will ask for the OpenWeatherMap API key:

```text
=== City Data Reporter ===
Enter your OpenWeatherMap API key:
```

Enter the API key without adding it to the Python source code.

The program will then ask for a city name:

```text
Enter a city name:
```

Enter a valid city name, such as:

```text
Vijayawada
```

The program retrieves the current weather information and displays it in the terminal.

## Input Validation

The program checks whether the city name is empty.

For example:

```text
Enter a city name:
City name cannot be empty. Please try again.
```

The program continues asking for a city name until a non-empty value is provided.

## Example Program Output

An example of the program output is shown below:

```text
=== City Data Reporter ===
Enter your OpenWeatherMap API key: [API KEY]

Enter a city name: Vijayawada

--- Current Weather ---
City: Vijayawada
Country: IN
Temperature: 26.14 °C
Humidity: 94%
Description: overcast clouds

Weather data saved to city_data.csv.

--- CSV Report ---
Number of cities in file: 1
Cities and temperatures:
- Vijayawada: 26.14 °C
```

Weather values are retrieved from the live API and may change each time the program is executed.

## CSV File

After successfully retrieving weather information, the program creates or updates `city_data.csv`.

Example:

```text
City,Country,Temperature (C),Humidity (%),Description
Vijayawada,IN,26.14,94,overcast clouds
```

When additional cities are searched, their weather information is added to the CSV file.

The program then reads the CSV file and reports the number of stored cities and their temperatures.

## Error Handling

The program handles several possible problems, including:

* Empty city names
* City not found
* Invalid API key
* Network connection errors
* Invalid JSON responses
* Missing CSV file

For example, if an invalid city is entered, the program displays:

```text
Error: City not found.
```

If an invalid API key is entered, the program displays:

```text
Error: Invalid API key.
```

## Python Libraries

### requests

The `requests` library is used to send a GET request to the OpenWeatherMap API and retrieve live weather information.

### json

The `json` library is used to parse the JSON response received from the API.

### csv

The `csv` library is used to write weather information to `city_data.csv` and read the stored information.

## Program Structure

The program is divided into several functions to make the code organized and readable.

### `get_city_name()`

Prompts the user for a city name and validates that the input is not empty.

### `get_weather_data()`

Sends a request to the OpenWeatherMap API and retrieves the weather data.

### `extract_weather_data()`

Extracts the required weather information from the JSON response.

### `display_weather()`

Displays the city, country, temperature, humidity, and weather description.

### `save_to_csv()`

Writes the weather information to `city_data.csv`.

### `read_from_csv()`

Reads the CSV file and reports the number of cities and their temperatures.

### `main()`

Controls the overall execution of the City Data Reporter application.

## API Key Security

The personal OpenWeatherMap API key is not included in this repository.

Users should never commit their personal API key to GitHub.

If an API key is accidentally exposed, it should be revoked and replaced with a new key.

## Screencast

A 3–5 minute screencast demonstrates the functionality of the City Data Reporter application.

The screencast includes:

1. Opening the project in VS Code.
2. Running `reporter.py` from the terminal.
3. Entering an empty city name to demonstrate input validation.
4. Entering a valid city name.
5. Showing the live weather information retrieved from OpenWeatherMap.
6. Showing that `city_data.csv` was created or updated.
7. Showing the CSV report with the number of cities and temperatures.
8. Explaining the use of the `requests`, `json`, and `csv` libraries.
9. Briefly explaining the main functions in `reporter.py`.

### Screencast Link

Add the link to your completed screencast here:

**Screencast:** [Add your video link here]

## GitHub Repository

The completed project is available in the following GitHub repository:

**GitHub Repository:** [Add your GitHub repository link here]


## Conclusion

The City Data Reporter project demonstrates how Python can be used to interact with a live web API, process JSON data, collect and validate user input, and store and retrieve information using CSV files.

The project combines Python programming, API interaction, file handling, error handling, and basic software documentation in a command-line application.
