from pymongo import MongoClient 

class mongoHelper:
    def __init__(self, connect, bdd) -> None:
        # Enregistrer le client mongo
        self.client = MongoClient(connect)
        # Enregistrer la bdd voulu
        self.bdd = self.client[bdd]

    def collect(self, collection, donnees):
        
        pass

    def add(self, collection, donnees):
        # Ajouter des données.
        collection.insert_one({donnees})
        pass

    def update(self, collection, donnees):
        # Moficier des données.
        collection.update_one({donnees})
        pass

    def remove(self, collection, donnees):
        # Supprimer des données
        collection.delete_one({donnees})
        pass