import pymongo


class linkedListModel:
    def __init__(self):
        pass

    def connect(self, col_name):
        connection = pymongo.MongoClient("localhost", 27017)
        database = connection["linked_list"]
        collection = database[col_name]
        return collection
    
#User collection
    def user(self):
        collection = self.connect("user")
        return collection 

    # def info(self):
    #     collection = self.connect("info")
    #     return collection
