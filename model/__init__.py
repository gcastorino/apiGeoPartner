import pymongo
import os
import ujson


class Mongo:

    def __init__(self):
        pass

    def db(self):
        try:
            MONGODB_DATABASE = os.getenv('DBAAS_MONGODB_DATABASE')
            DBAAS_MONGODB_ENDPOINT = os.getenv('DBAAS_MONGODB_ENDPOINT')
            client = pymongo.MongoClient(DBAAS_MONGODB_ENDPOINT)
            return client[MONGODB_DATABASE]
        except Exception as e:
            print(f"error {str(e)}")
            return False
