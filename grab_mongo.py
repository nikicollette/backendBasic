# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://nikicollette10:BOHtQa4tt6OowO27@cluster0.ptt55ak.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
#
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:from pymongo.mongo_client import MongoClient
# # from pymongo.server_api import ServerApi
# # uri = "mongodb+srv://nikicollette10:BOHtQa4tt6OowO27@cluster0.ptt55ak.mongodb.net/?retryWrites=true&w=majority"
# # # Create a new client and connect to the server
# # client = MongoClient(uri, server_api=ServerApi('1'))
# #
# # try:
# #     client.admin.command('ping')
# #     print("Pinged your deployment. You successfully connected to MongoDB!")
# # except Exception as e:
# #     print(e)
#
# from pymongo import MongoClient
#
#
# def get_database():
#     # Provide the mongodb atlas url to connect python to mongodb using pymongo
#     CONNECTION_STRING = "mongodb+srv://nikicollette10:BOHtQa4tt6OowO27@cluster0.ptt55ak.mongodb.net/?retryWrites=true&w=majority"
#
#     # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#     client = MongoClient(CONNECTION_STRING)
#
#     print(client['clothing_db'])
#     return client['clothing_db']
#
#
# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#     # Get the database
#     dbname = get_database()
#     print(e)

from pymongo import MongoClient

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://nikicollette10:BOHtQa4tt6OowO27@cluster0.ptt55ak.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # print(f"connected to db {client['clothing_db']}")
    return client['clothing_db']


# This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#     # Get the database
#     dbname = get_database()

