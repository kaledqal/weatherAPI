import requests
from django.conf import settings


def get_weather_data(city):
    """Make an http request to weather api"""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.APIKEY}'
    try:
        response = requests.get(url)
    except Exception as e:
        print("Error: ", e)
    else:
        return {"status": response.status_code, "data": response.json()}



