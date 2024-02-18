import pymongo
from pymongo import MongoClient

client = MongoClient()
client.drop_database("twitter")
db = client.twitter

julia = {
    "userid" : 7777,
    "name" : "Julia Geller",
    "follows" : [1000, 2000, 3000],
}

db.users.insert_one(julia)
print(db.users.show())