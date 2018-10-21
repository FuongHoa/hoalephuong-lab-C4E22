from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db["post"]
post = {
    "title": "Reason why I choose Techkids",
    "author": "Phng Hoaaaaa",
    "content": "I signed up for C4E22 because I would prefer wasting 4.000.000VND to try whether IT suits me rather than spending 4 years in University studying the wrong one. But Techkids is fun and professional so I guess I don't waste 4.000.000VND :D"
}

posts.insert_one(post)
