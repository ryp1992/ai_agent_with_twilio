from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from time import sleep


class MongoDBPoolManager:
    def __init__(self, uri, db_name, collection_name, max_pool_size=10, min_pool_size=1):
        """
        Initialize the MongoDB connection pool.

        :param uri: MongoDB Atlas connection URI
        :param max_pool_size: Maximum number of connections in the pool
        :param min_pool_size: Minimum number of connections in the pool
        """
        self.uri = uri
        self.max_pool_size = max_pool_size
        self.min_pool_size = min_pool_size
        self.client = None
        self.db_name = db_name
        self.collection_name = collection_name
        self.db = None
        self.collection = None

    def connect(self, ):
        """
        Establish the connection to MongoDB Atlas with connection pooling.
        """
        try:
            # Create a MongoClient with connection pooling
            self.client = MongoClient(self.uri, maxPoolSize=self.max_pool_size, minPoolSize=self.min_pool_size)
            # Access the database and collection
            self.db = self.client[self.db_name]  # Replace with your database name
            self.collection = self.db[self.collection_name]  # Replace with your collection name
            print("Connection to MongoDB Atlas established successfully.")
        except ConnectionFailure as e:
            print(f"Could not connect to MongoDB: {e}")
            return False
        return True

    def insert_document(self, document):
        """
        Insert a document into the collection.

        :param document: Dictionary object to insert into the MongoDB collection
        """
        try:
            self.collection.insert_one(document)
            print(f"Inserted document: {document}")
        except Exception as e:
            print(f"Error inserting document: {e}")

    def fetch_documents(self, query=None):
        """
        Fetch documents from the collection.

        :param query: Optional query dictionary to filter the documents
        :return: List of documents
        """
        try:
            query = query or {}
            result = self.collection.find(query)
            return list(result)
        except Exception as e:
            print(f"Error fetching documents: {e}")
            return []

    def update_document(self, query, update_values):
        """
        Update a document in the collection.

        :param query: Dictionary object for filtering the document to update
        :param update_values: Dictionary object with the new values to update
        """
        try:
            self.collection.update_one(query, {'$set': update_values})
            print(f"Updated document where {query} with {update_values}")
        except Exception as e:
            print(f"Error updating document: {e}")

    def delete_document(self, query):
        """
        Delete a document from the collection.

        :param query: Dictionary object to filter the document to delete
        """
        try:
            self.collection.delete_one(query)
            print(f"Deleted document where {query}")
        except Exception as e:
            print(f"Error deleting document: {e}")

    def close_connection(self):
        """
        Close the connection to MongoDB Atlas.
        """
        if self.client:
            self.client.close()
            print("Connection closed.")
