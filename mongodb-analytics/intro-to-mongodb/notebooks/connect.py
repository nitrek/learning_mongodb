def getMongoClient():
    from pymongo import MongoClient
    from dotenv import dotenv_values
    config = dotenv_values(".env")
    # Replace XXXX with your connection URI from the Atlas UI
    client = MongoClient(config['connection_url'])
    print(f"Connected to MongoDB Atlas with URI: {config['connection_url']}")
    return client