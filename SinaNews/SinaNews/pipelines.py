# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import os,sys


class SinaNewsPipeline(object):

    def process_item(self, item, spider):
    	headline  = item['headline']

    	filename = headline + ".txt"

    	whole_filename = item['subFilename'] + '/' + filename

    	#print(whole_filename)

    	# print("This is pipeline ")
    	# print("---------------------")
    	# print(item['content'])
    	# a = os.path.exists(whole_filename)
    	# print(a)

    	f = open(whole_filename,'w')
    	f.write(item['content'])
    	# print("write the content successfully")
    	f.close()

    	return item


