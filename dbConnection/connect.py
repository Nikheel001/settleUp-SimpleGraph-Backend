from pymongo.errors import ConnectionFailure
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')


def getDb(dbName): return client[dbName]


def getCollection(cName, dbName): return client[dbName][cName]


def closeDbConnection(): client.close()
