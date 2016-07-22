import pymongo

class Database(object): #no es un bjeto del mundo real pero es una blueprint


    URI = "mongodb://127.0.0.1:27017"   #son variables estaticas
    DATABASE = None

    @staticmethod
    def initialize():   #no le ponemos self entre () porque es un metodo de clase, no de instancia, por eso es estatico
        client = pymongo.MongoClient(Database.URI)  #como uri es estatica tenemos que accederla desde la clase
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query) # devuelve un cursor

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query) # No trae un cursor. el cursor se usa para empezar al ppio de la collection y despues ir a cada uno.
                                                        # trae el primer elemento que devuelve el cursor
                                                        # devuelve un objeto json

