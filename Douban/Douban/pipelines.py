# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import json

# class DoubanPipeline(object):

#     def __init__(self):
#     	self.f = open('Data/movie1.json','w')

#     def process_item(self, item, spider):
#     	content = json.dumps(dict(item),ensure_ascii = False) +'\n'
#     	self.f.write(content)
#     	return item

#     def close_spider(self,spider):
#     	self.f.close()

from scrapy.conf import settings
import pymongo

class DoubanPipeline(object):
	def __init__(self):
		host = settings['MONGODB_HOST']
		port = settings['MONGODB_PORT']
		dbname = settings['MONGODB_DBNAME']

		client = pymongo.MongoClient(host = host , port = port)

		mdb = client[dbname]
		self.post = mdb[settings['MONGODB_DOCNAME']]

	def process_item(self,item,spider):
		data = dict(item)
		self.post.insert(data)
		return item