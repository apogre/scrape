import pymongo
import mmh3
import sys

try:
	conn = pymongo.MongoClient()
	print "Connected!"
except pymongo.errors.ConnectionFailure, e:
	print "ConnectionFailure: %s" % e
conn

db = conn['scrapy-mongodb']

# for d in db.products.find():
# 	print d
# 	print mmh3.hash(str(d))
new_dict = {}	
cursor = db.posts.find({"hash":{"$exists": False}},{"scrapy-mongodb":False})
try:
	for d in cursor:
		print d
		id = d.pop("_id",None)
		print id
		new_dict = d
		print mmh3.hash(str(new_dict))
		db.posts.update({"_id" : id},{"$set" :{"hash":mmh3.hash(str(new_dict))}})


except pymongo.errors, e:
	print e

db.posts.ensure_index('hash', unique = True, dropDups =True, spare = True)
db.posts.drop_index('hash_1')
print "indexing complete"
