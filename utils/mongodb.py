import os

import motor.motor_asyncio as motor


class MongoDB:
    def __init__(self, db_name):
        self.__client = motor.AsyncIOMotorClient(os.getenv('MONGODB_URI'))
        self.__db = self.__client[db_name]
        for collection_name in self.__db.list_collection_names():
            setattr(self, collection_name, self.__db[collection_name])

    def __getitem__(self, item):
        return getattr(self, item)

    def insert(self, collection_name, data):
        return self[collection_name].insert_one(data)

    def find(self, collection_name, query):
        return self[collection_name].find(query)

    def find_one(self, collection_name, query):
        return self[collection_name].find_one(query)

    def update(self, collection_name, query, data):
        return self[collection_name].update_one(query, data)

    def delete(self, collection_name, query):
        return self[collection_name].delete_one(query)

    def delete_many(self, collection_name, query):
        return self[collection_name].delete_many(query)