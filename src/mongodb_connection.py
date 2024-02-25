import pymongo


def push_to_mongodb(json_file):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    connection_string = f'mongodb+srv://{username}:{password}@cluster0.agh7uyn.mongodb.net/'
    print(connection_string)
    client = pymongo.MongoClient(connection_string)
    db = client.rcvs_webscraper
    collection = db.test

    collection.bulk_write(json_file)
    client.close()
