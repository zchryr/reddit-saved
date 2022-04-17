import pymongo
from logger import Logger
logger = Logger

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
            logger.info("Successfully connected to MongoDB!")
        except Exception as error:
            logger.critical("Failed to connect go MongoDB.")
            logger.critical("Exception: " + str(error))

        # TODO Write checks in here to see if DB already exists and such.
        self.database = self.client[db_name]
        collection_name = 'saves - ' + reddit_username
        self.col = self.database[collection_name]

    def insert_one(self, document):
        self.col.insert_one(document)

    def insert_many(self, documents):
        self.col.insert_many(documents)
