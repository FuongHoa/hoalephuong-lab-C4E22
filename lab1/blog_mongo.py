from pymongo import MongoClient

uri = "mongodb://conhoadien1:hoaxinhvcl678@ds235251.mlab.com:35251/c4e22-lab"

# Connect to db:
client = MongoClient(uri)
db = client.get_default_database()

# Collection:
posts = db['posts']

post_list = posts.find()
# p = post_list[0]
for p in post_list:
    print(p["Author"])
    print(p["Content"])
    print(p["Title"])

# Document:
# Create a document
# post = {
#     "Title":"Hom nay toi that tinh",
#     "Content":"Toi dau kho",
#     "Author":"me",
# }
# Insert created document
# posts.insert_one(post)

