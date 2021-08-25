from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
mydatabase=client['Students']
collection=mydatabase['students_details']
data=[
    {"name":"Rahul","Marks":85},
    {"name":"Rohit","Marks":76}

]
collection.insert_many(data)