#!/usr/bin/python
import json
from urllib import response
from pprint import pprint
from flask import Flask, request, redirect, url_for
from pymongo import MongoClient

from earthquake import EarthquakeAPI
from mongo_helper import MongoHelper

app = Flask(__name__)  # definir le nom de l'application "app"


def succes():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


earthquakeAPI = EarthquakeAPI()
mongo_helper = MongoHelper("mongodb://localhost:27017", "Tremblement")
#data = earthquakeAPI.fetch_monthly_data()
mongo_helper.remove("tremblement","63c02d8d47216614313c850d")


@app.route('/')  # initialiser un decorateur sur la route racine "/"
def bonjour():
    message = "Bonjour tout le monde \n"
    return message


@app.route('/data', methods=['POST'])
def create_data():
    data = request.form["data"]
    mongo_helper.add("tremble", data)
    return succes()


@app.route('/data', methods=['GET'])
def result_data():
    user = request.args.get('_id')
    # mongo_helper.get(user)
    return succes()


@app.route('/data', methods=['PUT'])
def update_data():
    data_id = request.args.get('_id')
    data = request.form["data"]
    # mongo_helper.update(data)
    return succes()


@app.route('/data', methods=['DELETE'])
def delete_data():
    user = request.args.get('_id')
    mongo_helper.remove([user])
    return succes()


if __name__ == '__main__':  # appler les fonctions a l'interieur du script
    app.run(host='0.0.0.0', port=8080)
