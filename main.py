#!/usr/bin/python
import json

import flask
from bson import json_util
from flask import Flask, request, json, Response
from flask_cors import CORS, cross_origin
from functions import fetch_data
from earthquake import EarthquakeAPI
from weather import WeatherAPI
from mongo_helper import MongoHelper

app = Flask(__name__)  # definir le nom de l'application "app"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def succes():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


def build_response(data):
    response = flask.jsonify(list(data))
    return response


weather_collection = "weather"
earthquake_collection = "earthquake"
aggregate_collection = "aggregate"

earthquakeAPI = EarthquakeAPI()

mongo_helper = MongoHelper("mongodb://localhost:27017", "earthquake")


# mongo_helper.add("tremble",data)

@app.route('/data', methods=['POST'])
@cross_origin()
def create_data():
    data = request.form["data"]
    result = mongo_helper.add(aggregate_collection, data)
    return result


@app.route('/data', methods=['GET'])
@cross_origin()
def result_data():
    print("get")
    _id = request.args.get('_id')
    if _id is None:
        data = mongo_helper.get_all(aggregate_collection)
        return build_response(data)
    data = mongo_helper.get(aggregate_collection, _id)
    print("get")
    return build_response(data)


@app.route('/data', methods=['PUT'])
@cross_origin()
def update_data():
    data = request.form["data"]
    mongo_helper.update(aggregate_collection, data)
    return succes()


@app.route('/data', methods=['DELETE'])
@cross_origin()
def delete_data():
    _id = request.args.get('_id')
    mongo_helper.remove(aggregate_collection, _id)
    return succes()


@app.route('/synchronize_live', methods=['POST'])
@cross_origin()
def synch():
    fetch_data(mongo_helper, WeatherAPI(), earthquakeAPI)
    data = mongo_helper.get_yesterday(aggregate_collection)
    return build_response(data)


if __name__ == '__main__':  # appler les fonctions a l'interieur du script
    app.run(host='0.0.0.0', port=8080)
