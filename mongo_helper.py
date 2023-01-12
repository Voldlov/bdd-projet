from pymongo import MongoClient

class MongoHelper:
    def __init__(self, connect, bdd) -> None:
        # Enregistrer le client mongo
        self.client = MongoClient(connect)
        # Enregistrer la bdd voulu
        self.bdd = self.client[bdd]

    def add(self, collection, data):
        # Ajouter des données.
        collection.insert({data})

    def update(self, collection, data, one):
        # Modifier des données.
        if one == True:
            collection.update_one({data})
        else :
            collection.update_many({data})

    def remove(self, collection, data, one):
        # Supprimer des données
        if one == True :
            collection.delete_one({data})
        else :
            collection.delete_many({data})

    def get(self, collection, data, one):
        # Récuperer les données
        if one == True :
            collection.find_one({data})
        else :
            collection.find_many({data})

    def readData(self, data):
        one = False
        if data == "" :
            one = True
        return one

