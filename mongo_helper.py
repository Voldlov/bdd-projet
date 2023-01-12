from pymongo import MongoClient

class MongoHelper:
    def __init__(self, connect, bdd) -> None:
        # Enregistrer le client mongo
        self.client = MongoClient(connect)
        # Enregistrer la bdd voulu
        self.bdd = self.client[bdd]

    def add(self, collection, data):
        # Ajouter des données.
        self.bdd[collection].insert_many(data)

    def update(self, collection, data):
        # Modifier des données.
        self.bdd[collection].update_many(data)

    def remove(self, collection, data):
        # Supprimer des données
        self.bdd[collection].delete_many(data)

    def get(self, collection, data):
        # Récuperer les données
        self.bdd[collection].find_many(data)
