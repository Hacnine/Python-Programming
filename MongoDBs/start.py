from pymongo import MongoClient

my_client = MongoClient("mongodb://localhost:27017/")

my_db = my_client['mydatabse']
column = my_db['customer']

mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
]
# column.drop()
# x = column.insert_many(mylist)
# print(column.find_one({}, {"name": "Betty"}))


# insert data into exiting column
mylist2 = [
    {"name": "Tushar", "address": "Khilkhet 444"},
]
# x = column.insert_many(mylist2)

# print(column.find_one_and_delete({"name": "Tushar"},))
# print(column.find_one_and_replace({"name": "Tushar", "address": "Khilkhet 444"},))
# print(column.find_one_and_update({"name": "Betty"},))

# stored_data = column.find()
# for data in stored_data:
#     print(data)

# Find documents where the address starts with the letter "M" or higher:
myquery = {"address": {"$gt": "M"}}

# Find documents with regex where the address starts with the letter "M" :
# myquery = {"address": {"$regex": "^M"}}

mydoc = column.find(myquery)

for x in mydoc:
    # print(x)
    pass

# Sort the result alphabetically by name:
mydoc = column.find().sort("name", -1)

for x in mydoc:
  # print(x)
    pass

myquery = { "address": "Mountain 21" }

# column.delete_one(myquery)

myquery = { "address": {"$regex": "^M"} }

delete_manys = column.delete_many(myquery)
# print(delete_manys.deleted_count, " documents deleted.")

results = column.find().limit(3)

for result in results:
    print(result)

