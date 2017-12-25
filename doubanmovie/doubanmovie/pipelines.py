# -*- coding: utf-8 -*-
from pymongo import MongoClient
from .items import DoubanmovieItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

client = MongoClient('127.0.0.1',27017)
db = client['douban']

class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,DoubanmovieItem):
            collection = db['movies']
            collection.save(dict(item))
        # return item
