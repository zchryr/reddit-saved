"""Library for using MongoDB from python"""
import sys
import pymongo
from logger import Logger
LOGGER = Logger

class MongoClient:
    """Class to interact with a MongoDB server"""
    def __init__(self, connection_url, protocol, port,
                 db_username, db_password, db_name, ssl, reddit_username) -> None:
        self.client = None
        self.existing_ids = set()

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
            sys.exit(1)

        self.database = self.client[db_name]
        collection_name = 'saves - ' + reddit_username
        self.col = self.database[collection_name]

    def insert_one(self, document):
        """Insert one document (py dict) into collection."""
        self.col.insert_one(document)

    def insert_many(self, documents):
        """Insert many documents (py dicts) into collection."""
        self.col.insert_many(documents)

    def get_existing(self):
        """Get Reddit submission/comment ids that have already been saved to DB."""
        mongo_filter = {}
        mongo_project = {
            'id': True
        }

        result = self.col.find(
            filter=mongo_filter,
            projection=mongo_project
        )
        for existing_id in result:
            self.existing_ids.add(existing_id['id'])

    def check_existing(self, save_id):
        """Checks if a submission/comment already exists in DB."""
        return save_id in self.existing_ids
