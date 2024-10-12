# Weather App

A simple web application that fetches and displays weather information based on user-inputted city names. The app also retrieves relevant images from Unsplash to enhance the visual experience.

## Features

- Fetches current weather data from OpenWeather API
- Displays weather information, including temperature and weather description
- Fetches relevant images from Unsplash API based on the entered city
- Responsive design for optimal viewing on various devices

## Technologies Used

- Django: Web framework for building the application
- OpenWeather API: For retrieving weather data
- Unsplash API: For fetching images related to the specified city
- dotenv: For managing environment variables
- HTML/CSS: For front-end development

## Installation

### Prerequisites

- Python 3.x
- Django
- Requests library

### Steps

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-name>
    ```
2. install dependencies

3. Create a .env file in the root directory and add your API keys: 

   ```bash
   DJANGO_WEATHER_API_KEY=<your_openweather_api_key>
   UNSPLASH_API_KEY=<your_unsplash_api_key>
    ```
4. Run the Django development server: 

    ```bash
   python manage.py runserver
     ```
