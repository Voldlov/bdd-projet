"""
    Récupération des données de l'API | API data retrieval
"""
from datetime import datetime, date
import requests


class EarthquakeAPI:
    def __init__(self):
        pass

    def recup_date_mois(self):
        aujourdhui = datetime.timestamp(datetime.now())
        debut = date.fromtimestamp(aujourdhui - 2629800).strftime("%Y-%m-%d")
        fin = date.fromtimestamp(aujourdhui - 172800).strftime("%Y-%m-%d")

        self.url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=" + debut + "&endtime=" + fin

        reponse = requests.get(self.url)
        return reponse.json()["features"]

    def recup_date_hier(self):
        aujourdhui = datetime.timestamp(datetime.now())
        debut = date.fromtimestamp(aujourdhui - 86400).strftime("%Y-%m-%d")

        fin = date.fromtimestamp(aujourdhui).strftime("%Y-%m-%d")

        self.url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=" + debut + "&endtime=" + fin

        reponse = requests.get(self.url)
        return reponse.json()["features"]

"""
    Stockage des données dans MongoDB | Storing data in MongoDB
"""

tremblement = EarthquakeAPI()
#tremblement.recup_date_mois()
tremblement.recup_date_hier()
