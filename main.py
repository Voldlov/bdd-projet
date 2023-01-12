#!/usr/bin/python
import json
from urllib import response

from flask import Flask, request, redirect,url_for

import mongo_helper

app = Flask(__name__)  # definir le nom de l'application "app"

def succes():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/')  # initialiser un decorateur sur la route racine "/"
def bonjour():
    message = "Bonjour tout le monde \n"
    return message

@app.route('/data', methods=['POST'])
def creat_data():
    data = request.form["data"]
    #mongo_helper.MongoHelper.add(data)
    return succes()

@app.route('/data', methods=['GET'])
def result_data():
    user = request.args.get('_id')
    #mongo_helper.MongoHelper.get(user)
    return succes()
@app.route('/data', methods=['PUT'])
def update_data():
    data_id = request.args.get('_id')
    data=request.form["data"]
    #mongo_helper.MongoHelper.update(data)
    return succes()

@app.route('/data', methods=['DELETE'])
def delete_data():
    user = request.args.get('_id')
    #mongo_helper.MongoHelper.remove(user)
    return succes()

if __name__ == '__main__':  # appler les fonctions a l'interieur du script
    app.run(host='0.0.0.0', port=8080)
