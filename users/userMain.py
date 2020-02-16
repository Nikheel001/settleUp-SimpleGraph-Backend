from users.userContext import getUserContext
from users.User import User

# For oneline function no need to pass collections and query
# call them directly
# def addUser(user, userCollection):
#     userCollection.insert_one(user)
#
# def fetchOneUser(query, userCollection):
#     return userCollection.find_one(query)
#
# def findAllUser(query, userCollection):
#     return userCollection.find(query)


def testOp():
    with getUserContext() as users:
        # headshot = User.fromDict(fetchOneUser({"name": "Headshot"}, users))
        headshot = User.fromDict(users.find_one({"name": "Headshot"}))
        print(headshot)
        headshot = User.fromDict(users.find_one({"name": "Anil"}))
        print(headshot)

def findByCellNo(cellNo):
    '''
    Identifies user from phone number
    '''
    with getUserContext() as users:
        try:
            return User.fromDict(users.find_one({"no": cellNo}))
        except expression as identifier:
            return None

# Testing to fetch user from db
# headshot = User.fromDict(fetchOneUser({"name": "Headshot"}))
# print(headshot)

# Testing to insert user into db
# headshot = User()
# headshot.Name = 'Anil'
# headshot.Owed = 100
# addUser(headshot.userAsDict())
