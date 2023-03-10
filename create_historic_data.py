from earthquake import EarthquakeAPI
from mongo_helper import MongoHelper
from weather import WeatherAPI
from functions import fetch_data

earthquakeAPI = EarthquakeAPI()
weatherApi = WeatherAPI()

mongo_helper = MongoHelper("mongodb://localhost:27017", "earthquake")

mongo_helper.drop("weather")
mongo_helper.drop("earthquake")
mongo_helper.drop("aggregate")
fetch_data(mongo_helper, weatherApi, earthquakeAPI)
mongo_helper.index_earthquake_id_on_earthquake_and_weather()
mongo_helper.agregate_weather_and_earthquake()
