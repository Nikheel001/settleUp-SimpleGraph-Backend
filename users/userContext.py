# import pymongo
from pymongo.errors import ConnectionFailure
from dbConnection.connect import getCollection, closeDbConnection
from contextlib import contextmanager

@contextmanager
def getUserContext():
    try:
        yield getCollection('users', 'copy')
        # yield getCollection('users', 'copy')
    except ConnectionFailure as e:
        print("ConnectionFailure" + e)
    except Exception as exc:
        print(exc)
        # notify Headshot
    finally:
        closeDbConnection()