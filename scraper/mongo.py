import pymongo

class mongoClient:
    def __init__(self, connectionURL, protocol, port, 
        username, password, name, ssl, tlsCAFile, redditUsername) -> None:
        self.client = pymongo.MongoClient(host=protocol + "://" + connectionURL,
            port=port,
            username=username,
            password=password,
            ssl=ssl,
            tlsCAFile=tlsCAFile)
        self.db = self.client[name]
        colName = 'saves - ' + redditUsername
        self.col = self.db[colName]

    def insertOne(self, document):
        self.col.insert_one(document)

    def insertMany(self, documents):
        self.col.insert_many(documents)
