from datetime import datetime, timedelta

from bson import ObjectId
from pymongo import MongoClient

weather_collection = "weather"
earthquake_collection = "earthquake"
aggregate_collection = "aggregate"


class MongoHelper:
    """
        Constructor
    """

    def __init__(self, connect, bdd) -> None:
        # Enregistrer le client mongo
        self.client = MongoClient(connect)
        # Enregistrer la bdd voulu
        self.bdd = self.client[bdd]

    def drop(self, collection):
        # Drop a collection
        self.bdd[collection].drop()

    def index_earthquake_id_on_earthquake_and_weather(self):
        self.bdd[weather_collection].create_index("earthquake_id")
        self.bdd[earthquake_collection].create_index("id")

    """
        CRUD
    """

    def add(self, collection, data):
        # Ajouter des données.
        self.bdd[collection].insert_many(data)

    def update(self, collection, ids, data):
        # Modifier des données.
        self.bdd[collection].update_many(ids, data)

    def remove(self, collection, data):
        # Supprimer des données
        # S'il y a des documents importants, mettre des sécurités. 
        query = {'_id': ObjectId(data)}
        self.bdd[collection].delete_many(query)

    def get(self, collection, data):
        # Récuperer les données
        # Modifier pour faire en aggregate. 
        return self.bdd[collection].find(data)

    def get_all(self, collection):
        # Récuperer toutes les données
        return self.bdd[collection].find()

    def get_yesterday(self, collection):
        # recuperer les tremblements de terre d'hier
        return self.bdd[collection].find({'yesterday': True})

    """
        Agregate
    """

    def agregate(self, collection, trie):
        # Fonction de trie
        # Pipeline avec ce que l'agregate doit faire
        pipeline = [trie]
        # Affection l'agregate à une collection et le retourner
        return collection.aggregate(pipeline)

    def agregate_weather_and_earthquake(self):
        # agregate weather data the hour before and after an earthquake to the earthquake

        # filter earthquakes which time is not between 22:59:59 and 1:00:00
        project_timestamp_to_hour_in_earthquake = {
            "$project": {
                "id": 1,
                "_id": 0,
                "properties": 1,
                "geometry": 1,
                "yesterday": 1,
                "hour": {
                    # Here is the operator $hour to get the hour of the timestamp
                    "$hour": {
                        "$toDate": "$properties.time"
                    }
                }
            }
        }

        filter_earthquake_not_between_22_59_59_and_1_00_00 = {
            "$match": {
                "$and": [
                    {
                        "hour": {
                            "$lte": 22
                        }
                    },
                    {
                        "hour": {
                            "$gte": 1
                        }
                    }
                ]
            }
        }

        lookup = {
            "$lookup": {
                "from": weather_collection,
                "localField": "id",
                "foreignField": "earthquake_id",
                "as": "weather"
            }
        }
        unwind = {
            "$unwind": "$weather"
        }

        project_array_weather_forecast_forecastday_to_object = {
            "$project": {
                "id": 1,
                "properties": 1,
                "geometry": 1,
                "yesterday": 1,
                "hour": 1,
                "weather": {"$arrayElemAt": ["$weather.forecast.forecastday", 0]}
            }
        }

        project_weather_data_of_the_hour_before_and_after_the_earthquake = {
            "$project": {
                "id": 1,
                "properties": 1,
                "geometry": 1,
                "yesterday": 1,
                "weather_before": {"$arrayElemAt": ["$weather.hour", "$hour"]},
                "weather_after": {"$arrayElemAt": ["$weather.hour", {"$add": ["$hour", 1]}]},
            }
        }

        addObjectId = {
            "$addFields": {
                "_id": {
                    "$toString": "$id"
                }
            }
        }

        pipeline = [
            project_timestamp_to_hour_in_earthquake,
            filter_earthquake_not_between_22_59_59_and_1_00_00,
            lookup,
            unwind,
            project_array_weather_forecast_forecastday_to_object,
            project_weather_data_of_the_hour_before_and_after_the_earthquake,
            addObjectId
        ]

        agregate = self.bdd[earthquake_collection].aggregate(pipeline)
        self.bdd[aggregate_collection].insert_many(agregate)
