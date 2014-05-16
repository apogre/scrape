# Scrapy settings for vacatures project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'vacatures'

SPIDER_MODULES = ['vacatures.spiders']
NEWSPIDER_MODULE = 'vacatures.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'vacatures (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['scrapy_mongodb.MongoDBPipeline',]

MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DB = "vacatures"
MONGODB_COLLECTION = "posts"
MONGODB_ADD_TIMESTAMP = True


