import pymongo

class DB:

    __instance = None

    @staticmethod
    def getInstance(**kwargs):
        """ Static access method. """
        if DB.__instance == None:
            #select db
            dbName = "users"
            DB(dbName)

        return DB.__instance

    def __init__(self, dbName) -> None:
        """ Virtually private constructor. """
        if DB.__instance != None:
            raise Exception("This class is a DB!")
        else:
            DB.__instance = self

            self.client = pymongo.MongoClient('mongodb://localhost:27017/')
            self.db = self.client[dbName]           

    def create(self, collection, dataDict):
        
        self.db[collection].insert_one(dataDict)
        return


    def readAll(self, collection):
        users = self.db[collection].find()
        usersDict = {}
        for user in users:
            usersDict[user['account']] = {
                'account' : user['account'],
                'password': user['password']
            }
        
        return usersDict

    def read(self, collection, queryData, projection = None):
        query = {'account':queryData}
        userDict = self.db[collection].find_one(query)
        userData = {
            'account' : userDict['account'],
            'password': userDict['password']
        }
        return userData

    def update(self, collection, filterData, newvalues):
        filter = {'account': filterData}
        newvalues = { "$set": {'password' : newvalues} }
        self.db[collection].update_one(filter, newvalues)

    
    def delete(self, collection, filterData):
        filter = {'account': filterData}
        self.db[collection].delete_one(filter)
