"""
    Récupération des données de l'API | API data retrieval
"""
from datetime import datetime, date
import requests


class EarthquakeAPI:
    def __init__(self):
        self.base_url = "https://earthquake.usgs.gov/fdsnws/event/1/"

    def fetch_monthly_data(self):
        today = datetime.timestamp(datetime.now())
        begin = date.fromtimestamp(today - 2629800).strftime("%Y-%m-%d")
        end = date.fromtimestamp(today - 172800).strftime("%Y-%m-%d")

        url = self.base_url + "query?format=geojson&starttime=" + begin + "&endtime=" + end

        response = requests.get(url)
        return response.json()["features"]

    def fetch_yesterday_data(self):
        today = datetime.timestamp(datetime.now())
        begin = date.fromtimestamp(today - 86400).strftime("%Y-%m-%d")
        end = date.fromtimestamp(today).strftime("%Y-%m-%d")

        url = self.base_url + "query?format=geojson&starttime=" + begin + "&endtime=" + end

        response = requests.get(url)
        return response.json()["features"]
