import pymongo
from logger import Logger
LOGGER = Logger

class MongoClient:
    def __init__(self, connection_url, protocol, port,
                 db_username, db_password, db_name, ssl, reddit_username) -> None:
        self.client = None

        try:
            self.client = pymongo.MongoClient(host=protocol + "://" + connection_url,
                                              port=port,
                                              username=db_username,
                                              password=db_password,
                                              ssl=ssl)
            self.client.server_info()
            LOGGER.info("Successfully connected to MongoDB!")
        except Exception as error:
            LOGGER.critical("Failed to connect go MongoDB.")
            LOGGER.critical("Exception: " + str(error))

        self.database = self.client[db_name]
        collection_name = 'saves - ' + reddit_username
        self.col = self.database[collection_name]

    def insert_one(self, document):
        self.col.insert_one(document)

    def insert_many(self, documents):
        self.col.insert_many(documents)
