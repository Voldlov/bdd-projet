#!/usr/bin/python
from flask import Flask

app = Flask(__name__)  # definir le nom de l'application "app"


@app.route('/')  # initialiser un decorateur sur la route racine "/"
def bonjour():
    message = "Bonjour tout le monde \n"
    return message


if __name__ == '__main__':  # appler les fonctions a l'interieur du script
    app.run(host='0.0.0.0', port=8080)
