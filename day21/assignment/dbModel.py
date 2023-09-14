import pymongo

class NccAuctionModel:
    def __init__(self):
        pass

    def connect(self, col_name):
        connection = pymongo.MongoClient("localhost", 27017)
        database = connection["ncc_auction"]
        collection = database[col_name]
        return collection
    
#item collectionas
    def item(self):
        collection = self.connect("items_and_prices")
        return collection

#User collection
    def user(self):
        collection = self.connect("user")
        return collection
    
    def candidate(self):
        collection = self.connect("candidate")
        return collection   

    def info(self):
        collection = self.connect("info")
        return collection
