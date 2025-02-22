import mongodb_connector
import config

# db_pool = mongodb_connector.MongoDBPoolManager(config.MONGO_URI)
users_collection = mongodb_connector.MongoDBPoolManager(config.MONGO_URI, "flight_booking","user_info")
booking_collection = mongodb_connector.MongoDBPoolManager(config.MONGO_URI, "flight_booking","booking_info")

def connect_db():
    try :
        users_collection.connect()
        booking_collection.connect()
    except Exception as e:
        print(e)

def close_db():
    try:
        users_collection.close_connection()
        booking_collection.close_connection()
    except Exception as e:
        print(e)

