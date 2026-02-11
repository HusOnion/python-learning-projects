# Weather App (PyQt5)

## Description
This is a simple GUI-based Weather App built with Python and PyQt5.  
It allows the user to enter a city name and fetches the current weather, temperature, description, and an emoji representing the weather condition.

## Features
- Input city name
- Fetch current temperature (°C)
- Show weather description
- Display weather emoji (sun, clouds, rain, snow, etc.)
- Error handling for invalid city names, connection issues, and server errors

## API
This app uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch real-time weather data.

### How it works:
1. User enters city name and clicks "Get Weather"
2. App sends a request to OpenWeatherMap API
3. Receives JSON response
4. Displays temperature, description, and emoji

## What I Learned
- PyQt5 GUI development (widgets, layouts, signals)
- Making HTTP requests with `requests`
- Handling JSON responses
- Exception handling for API calls
- Mapping data to visual elements (like emojis)
- Structuring a small project using OOP
