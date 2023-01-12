from pymongo import MongoClient

class MongoHelper:
    def __init__(self, connect, bdd) -> None:
        # Enregistrer le client mongo
        self.client = MongoClient(connect)
        # Enregistrer la bdd voulu
        self.bdd = self.client[bdd]

    def add(self, collection, donnees):
        # Ajouter des données.
        collection.insert({donnees})

    def update(self, collection, donnees):
        # Modifier des données.
        collection.update_one({donnees})

    def remove(self, collection, donnees):
        # Supprimer des données
        collection.delete_one({donnees})

    def get(self, collection, donnees):
        # Récuperer les données
        collection.find({donnees})

