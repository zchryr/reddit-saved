import pymongo

class MongoClient:
    def __init__(self, connectionURL, protocol, port,
                 username, password, name, ssl, tls_ca_file, reddit_username) -> None:
        self.client = pymongo.MongoClient(host=protocol + "://" + connectionURL,
                                          port=port,
                                          username=username,
                                          password=password,
                                          ssl=ssl,
                                          tlsCAFile=tls_ca_file)
        self.database = self.client[name]
        collection_name = 'saves - ' + reddit_username
        self.col = self.database[collection_name]

    def insert_one(self, document):
        self.col.insert_one(document)

    def insert_many(self, documents):
        self.col.insert_many(documents)
