import pymongo

class DB:

    __instance = None

    @staticmethod
    def getInstance(**kwargs):
        """ Static access method. """
        if DB.__instance == None:
            dbName = "testMongoDB"
            DB(dbName)

        return DB.__instance

    def __init__(self, dbName) -> None:
        """ Virtually private constructor. """
        if DB.__instance != None:
            raise Exception("This class is a ProcessController!")
        else:
            DB.__instance = self

            self.client = pymongo.MongoClient('mongodb://localhost:27017/')
            self.db = self.client[dbName]           #select db

    def create(self, collection, dataDictList):

        if len(dataDictList) == 1:
            insertDict = dataDictList[0]
            self.db[collection].insert_one(insertDict)
            return
        
        self.db[collection].insert_many(dataDictList)

    def read(self, collection, query, projection = None):
        resultList = list(self.db[collection].find(query, projection))
        return resultList

    def update(self, collection, filter, newvalues):
        newvalues = { "$set": newvalues }
        self.db[collection].update_many(filter, newvalues)

    
    def delete(self, collection):
        pass