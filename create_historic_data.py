from datetime import datetime

from earthquake import EarthquakeAPI
from main import succes
from mongo_helper import MongoHelper
from weather import WeatherAPI

weather_collection = "weather"
earthquake_collection = "earthquake"
aggregate_collection = "aggregate"

earthquakeAPI = EarthquakeAPI()
weatherApi = WeatherAPI()

mongo_helper = MongoHelper("mongodb://localhost:27017", "earthquake")


def fetch_and_store_api_data():
    # Fetch data from the API
    earthquake_data = earthquakeAPI.fetch_monthly_data()
    weather_data = []
    for earthquake in earthquake_data:
        date_from_timestamp = datetime.fromtimestamp(earthquake["properties"]["time"] / 1000)
        weather_data = weatherApi.weather_information(
            earthquake["geometry"]["coordinates"][1],
            earthquake["geometry"]["coordinates"][0],
            date_from_timestamp.strftime("%Y-%m-%d"))
        if weather_data is not None:
            weather_data["earthquake_id"] = earthquake["id"]
            print(str(earthquake["geometry"]["coordinates"][1]) + " " + str(earthquake["geometry"]["coordinates"][0]))
            print(weather_data)
            mongo_helper.add(weather_collection, [weather_data])
    # Store data in the database
    mongo_helper.add(earthquake_collection, earthquake_data)


fetch_and_store_api_data()

def fetch_yesterday_api_data():
    earthquake_data = earthquakeAPI.fetch_yesterday_data()
    weather_data = []
    for earthquake in earthquake_data:
        date_from_timestamp = datetime.fromtimestamp(earthquake["properties"]["time"] / 1000)
        weather_data = weatherApi.weather_information(
            earthquake["geometry"]["coordinates"][1],
            earthquake["geometry"]["coordinates"][0],
            date_from_timestamp.strftime("%Y-%m-%d"))
        if weather_data is not None:
            weather_data["earthquake_id"] = earthquake["id"]
            weather_data["yesterday"] = True
            print(str(earthquake["geometry"]["coordinates"][1]) + " " + str(earthquake["geometry"]["coordinates"][0]))
            print(weather_data)
            mongo_helper.add(weather_collection, [weather_data])
    # Store data in the database
    mongo_helper.add(earthquake_collection, earthquake_data)


