from pymongo import MongoClient
# from mathplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()
customers = db['customer']

events = customers.find({"ref": "events"}).count()
print("events: {}".format(events))
advertisements = customers.find({"ref": "advertisements"}).count()
print("advertisements: {}".format(advertisements))
word_of_mouth = customers.find({"ref": "word_of_mouth"}).count()
print("word_of_mouth: {}".format(word_of_mouth))

from matplotlib import pyplot

#prepare data
ref_counts = (ref["events"], ref["advertisements"], ref["word_of_mouth"])

#prepare labels
ref_names = ["events", "advertisements", "word_of_mouth"]

pyplot.pie(ref_counts, labels = ref_names, autopct="%.1f%%", shadow=True, explode=[0, 0.2, 0])
pyplot.title("The number of customers based on reference")
pyplot.axis("equal")

pyplot.show()

