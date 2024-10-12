from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def home_page(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'hyderabad'
    
    # API Keys
    API_KEY = os.getenv('DJANGO_WEATHER_API_KEY')  
    UNSPLASH_API_KEY = os.getenv('UNSPLASH_API_KEY')  
    
    # OpenWeather API URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    PARAMS = {'units': 'metric'}

    # Unsplash API URL
    unsplash_url = f'https://api.unsplash.com/search/photos?query={city}&client_id={UNSPLASH_API_KEY}'

    # Get image URL
    image_url = 'https://example.com/default-image.jpg'  

    # Fetch Unsplash image
    unsplash_response = requests.get(unsplash_url)
    if unsplash_response.status_code == 200:
        unsplash_data = unsplash_response.json()
        if unsplash_data.get("results") and len(unsplash_data["results"]) > 0:
            image_url = unsplash_data["results"][3]['urls']['regular']  
    else:
        messages.error(request, 'Failed to retrieve image data.')

    # Fetch weather data
    weather_response = requests.get(url, params=PARAMS)
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.date.today()

        return render(request, 'home.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })
    else:
        messages.error(request, 'Failed to retrieve weather data. Please check the city name.')
        day = datetime.date.today()

        return render(request, 'home.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 27,
            'day': day,
            'city': city,
            'exception_occurred': True,
            'image_url': image_url
        })
