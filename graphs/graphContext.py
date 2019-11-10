from pymongo.errors import ConnectionFailure
from contextlib import contextmanager
from dbConnection.connect import getCollection, closeDbConnection

@contextmanager
def getGraphContext():
    try:
        yield getCollection('graph', 'copy')
    except ConnectionFailure as e:
        print("ConnectionFailure" + e)
    except Exception as exc:
        print(exc)
    finally:
        closeDbConnection()