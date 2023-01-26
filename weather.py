import os
import json
import requests as r
from dotenv import load_dotenv

load_dotenv()


class WeatherAPI:
    API_KEY = os.getenv('API_KEY')
    API_URL = 'http://api.weatherapi.com/v1/history.json?'

    def weather_information(self, lat: int, long: int, date: str):
        payload = {'q': f'{lat},{long}', 'dt': f'{date}'}
        headers = {'key': f'{self.API_KEY}'}
        location = r.get(self.API_URL, params=payload, headers=headers)
        output = json.loads(location.text)
        return output
