# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy_mongodb.settings import mongodb_host, mongodb_dbname, mongodb_port, mongodb_collection

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyMongodbPipeline:
    def __init__(self):
        host = mongodb_host
        port = mongodb_port
        dbname = mongodb_dbname
        sheet_name = mongodb_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheet_name]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
