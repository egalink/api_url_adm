from pymongo import MongoClient
import os

class MongoDbClientSingleton:

    _instance = None
    _dbclient = None

    def __new__ (cls):

        if (cls._instance is None):
            cls._instance = super(MongoDbClientSingleton, cls).__new__(cls)

        return cls._instance

    def __init__ (self):
        host = os.environ.get('MONGODB_HOST', '127.0.0.1')
        port = os.environ.get('MONGODB_PORT', 27017)
        self._dbclient = MongoClient(f"mongodb://{host}:{port}/")

    def get_client (self):
        return self._dbclient

class MongoDb:

    _client = None

    def __init__ (self):
        self._client = MongoDbClientSingleton().get_client()

    def db (self, db_name='public'):
        self._db = self._client[db_name]
        return self

    def on (self, collection_name='default'):
        return self._db[collection_name]
