#!/usr/bin/python
import json
from flask import Flask, request
from create_historic_data import fetch_yesterday_api_data
from earthquake import EarthquakeAPI
from weather import WeatherAPI
from mongo_helper import MongoHelper

app = Flask(__name__)  # definir le nom de l'application "app"


def succes():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


weather_collection = "weather"
earthquake_collection = "earthquake"
aggregate_collection = "aggregate"

earthquakeAPI = EarthquakeAPI()

mongo_helper = MongoHelper("mongodb://localhost:27017", "earthquake")

#mongo_helper.add("tremble",data)

@app.route('/data', methods=['POST'])
def create_data():
    data = request.form["data"]
    result = mongo_helper.add(aggregate_collection, data)
    return result


@app.route('/data', methods=['GET'])
def result_data():
    _id = request.args.get('_id')
    if _id is None:
        data = mongo_helper.get_all(aggregate_collection)
        return data
    data = mongo_helper.get(aggregate_collection, _id)
    return data


@app.route('/data', methods=['PUT'])
def update_data():
    data = request.form["data"]
    mongo_helper.update(aggregate_collection, data)
    return succes()


@app.route('/data', methods=['DELETE'])
def delete_data():
    _id = request.args.get('_id')
    mongo_helper.remove(aggregate_collection, _id)
    return succes()


@app.route('/synchronize_live', methods=['POST'])
def synch():
    fetch_yesterday_api_data()
    data=mongo_helper.get_yesterday(aggregate_collection)
    return data


if __name__ == '__main__':  # appler les fonctions a l'interieur du script
    app.run(host='0.0.0.0', port=8080)
