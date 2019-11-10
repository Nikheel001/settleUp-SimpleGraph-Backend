from graphs.graphContext import getGraphContext

def ReplaceGraphDB(graph, graphCollection):
    graphCollection.replaceOne({'_id':graph['_id']},graph)

def addGraphToDB(graph, graphCollection):
    graphCollection.insert_one(graph)

# def loadGraphFromDb():
#     with getGraphContext() as graphCollection:
#         graphCollection.find_one({'_id':})
#         pass
#     pass