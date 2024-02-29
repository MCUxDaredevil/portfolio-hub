import os

from fastapi import FastAPI, Depends
from pymongo import MongoClient
from pymongo.results import InsertOneResult, InsertManyResult, UpdateResult, DeleteResult


class MongoDB:
    def __init__(self, db_name):
        """Initializes a MongoDB client and database."""

        self.__client = MongoClient(os.getenv('MONGO_URI'))
        self.__db = self.__client[db_name]

    def get_collection_names(self) -> list:
        """Returns a list of collection names."""
        return self.__db.list_collection_names()

    def find_one(self, collection, query) -> dict:
        """Returns a single document from the collection."""
        return self.__db[collection].find_one(query)

    def find(self, collection, query) -> list:
        """Returns a list of documents from the collection."""
        return list(self.__db[collection].find(query))

    def insert_one(self, collection, document) -> InsertOneResult:
        """Inserts a single document into the collection."""
        return self.__db[collection].insert_one(document)

    def insert_many(self, collection, documents) -> InsertManyResult:
        """Inserts a list of documents into the collection."""
        return self.__db[collection].insert_many(documents)

    def update_one(self, collection, query, update) -> UpdateResult:
        """Updates a single document in the collection."""
        return self.__db[collection].find_one_and_update(query, update)

    def update_many(self, collection, query, update) -> UpdateResult:
        """Updates multiple documents in the collection."""
        return self.__db[collection].update_many(query, update)

    def delete_one(self, collection, query) -> DeleteResult:
        """Deletes a single document from the collection."""
        return self.__db[collection].find_one_and_delete(query)

    def delete_many(self, collection, query) -> DeleteResult:
        """Deletes multiple documents from the collection."""
        return self.__db[collection].delete_many(query)


def get_db(app: FastAPI = Depends()):
    return app.mongodb
