import pymongo
import json
from pymongo import InsertOne

client = pymongo.MongoClient("""mongodb+srv://bensullivan2002:KSBEXHer8Kfo@cluster0.agh7uyn.mongodb.net/
?retryWrites=true&w=majority&appName=Cluster0""")
db = client.rcvs_webscraper
collection = db.test
requesting = []

with open('rcvs_scrape.json') as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))
