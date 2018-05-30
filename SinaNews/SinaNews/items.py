# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaNewsItem(scrapy.Item):

	#the title and urls of parent
	parentTitle = scrapy.Field()
	parentUrls  = scrapy.Field() # What's the function 

	#the title and urls of son
	subTitle = scrapy.Field()
	subUrls  = scrapy.Field()

	# store path
	subFilename = scrapy.Field()

	sonUrls = scrapy.Field()

	headline = scrapy.Field()
	content = scrapy.Field()


