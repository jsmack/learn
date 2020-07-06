import datetime

from pymongo import MongoClient
# mongod --dbpath ./data/db/


client = MongoClient('mongodb://localhost:27017/')

db = client['test_database']
stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}
stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks
#stack_id = db_stacks.insert_one(stack1).inserted_id
#print(stack_id, type(stack_id))

#print('###########')
#from bson.objectid import  ObjectId
#str_stack_id = '5efb218f7664599a6ca4a8c5'
#print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))

print(db_stacks.find_one({'name': 'customer1'}))
print(db_stacks.find_one({'pip': ['python', 'java'],}))


# stack_id = stack_id2 = db_stacks.insert_one(stack2).inserted_id
#print(stack_id)
print("################")
for stack in db_stacks.find():
    print(stack)

print("################")
now = datetime.datetime.utcnow()
for stack in db_stacks.find({'data': {'$lt': now}}):
    print(stack['name'])

print("################")

db_stacks.find_one_and_update(
    {'name': 'customer1'}, {'$set': {'name': 'YYYY'}}
)
print(db_stacks.find_one({'name': 'YYYY'}))
print("################")

db_stacks.delete_one({'name': 'costomer2'})
print(db_stacks.find_one({'name': 'costomer2'}))
