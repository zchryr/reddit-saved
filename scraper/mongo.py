"""Library for using MongoDB from python"""
from asyncio.log import logger
import sys
import pymongo
from logger import Logger
LOGGER = Logger

class MongoClient:
    """Class to interact with a MongoDB server"""
    def __init__(self, connection_url, protocol, port,
                 db_username, db_password, ssl, reddit_username) -> None:
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
            sys.exit(1)

        self.database = self.client[reddit_username]

    def insert_one(self, save_type, document):
        """Insert one document (py dict) into collection."""
        col = None

        if save_type == 'submission':
            col = self.database['submissions']
        elif save_type == 'comment':
            col = self.database['comments']


        try:
            col.insert_one(document)
            LOGGER.info("Saved " + save_type + " ID: " + document['reddit_id'] +
                        " to the DB successfully!")
        except Exception as e:
            LOGGER.error("Error while inserting document into database: " + str(e))

    def insert_many(self, save_type, documents):
        """Insert many documents (py dicts) into collection."""
        col = None

        if save_type == 'submission':
            col = self.database['submissions']
        elif save_type == 'comment':
            col = self.database['comments']

        try:
            col.insert_many(documents)
            LOGGER.info("Saved posts/comments to the DB successfully!")
        except Exception as e:
            LOGGER.error("Error while inserting document into database: " + str(e))

    def check_existing(self, save_type, save_id):
        """Checks if a submission/comment already exists in DB."""
        if save_type == 'submission':
            COL = self.database['submissions']
        elif save_type == 'comment':
            COL = self.database['comments']

        filter = {
            'reddit_id': save_id
        }

        project = {
            '_id': 1
        }

        RESULTS = COL.find_one(
            filter=filter,
            projection=project
        )

        if RESULTS == None:
            return False
        else:
            LOGGER.info(save_type.capitalize() + " already exists in the database.")
            return True