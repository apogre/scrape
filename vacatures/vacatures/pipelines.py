# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class MongoDBPipeline(object):
	def __init__(self):
		self.server = settings['MONGODB_SERVER']
		self.port = settings['MONGODB_PORT']
		self.db = settings['MONGODB_DB']
		self.col = settings['MONGODB_COLLECTION']
		connection = pymongo.Connection(self.server,self.port)
        db = connection[self.col]
        self.collection = db[self.col]

	def process_item(self, item, spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Data Missing")

		if valid:
			self.collection.insert(dict(item))
			log.msg("done")
		return item

        
    