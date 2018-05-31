# -*- coding: utf-8 -*-
import scrapy
from SinaNews.items import SinaNewsItem
import os


class SinaSpider(scrapy.Spider):
    name = 'Sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):

    	items = []

    	parentTitle = response.xpath("//div[@id='tab01']//h3/a/text()").extract()
    	parentUrls  = response.xpath("//div[@id='tab01']//h3/a/@href").extract()

    	
    	for i in range(len(parentUrls)):#len(parentUrls)-18

    		parentFilename = './Data/' + parentTitle[i]

    		if(not os.path.exists(parentFilename)):
    			os.makedirs(parentFilename)
    		j = i+1
    		int(j)
    		print("===========================")
    		print(j)
    		subTitle = response.xpath("//div[@id='tab01']/div[{}]//li/a/text()".format(i+1)).extract()
    		subUrls  = response.xpath("//div[@id='tab01']/div[{}]//li/a/@href".format(i+1)).extract()
    		print(subTitle)

    		for j in range(len(subUrls)):
    	
    			item = SinaNewsItem()

    			subFilename = parentFilename + '/' + subTitle[j]

    			if(not os.path.exists(subFilename)):
    				os.makedirs(subFilename)

    			item['parentTitle'] = parentTitle[i]
    			item['parentUrls']  = parentUrls[i]
    			item['subTitle'] = subTitle[j]
    			item['subUrls']  = subUrls[j]
    			item['subFilename'] = subFilename

    			items.append(item)

    	for item in items:
    		yield scrapy.Request(url=item['subUrls'],meta = {'meta_1':item},callback = self.second_parse)


    def second_parse(self,response):
    	meta_1 = response.meta['meta_1']

    	sonUrls = response.xpath("//a/@href").extract()

    	items = []

    	for i in range(len(sonUrls)):
    		if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])

    		if  if_belong:
    			item = SinaNewsItem()
    			item['parentTitle'] = meta_1['parentTitle']
    			item['parentUrls']  = meta_1['parentUrls']
    			item['subTitle']  = meta_1['subTitle']
    			item['subUrls']   = meta_1['subUrls']
    			item['subFilename'] = meta_1['subFilename']
    			item['sonUrls']  = sonUrls[i]
    			items.append(item)

    	for item in items:
    		yield scrapy.Request(url=item['sonUrls'],meta = {'meta_2':item},callback = self.detail_parse)


    def detail_parse(self,response):
    	item = response.meta['meta_2']
    	content= ""
    	headline = response.xpath("//h1[@class='main-title']/text()").extract()[0]
    	content_list = response.xpath("//div[@class='article']/p/text()").extract()

    	for i in content_list:
    		content += i

    	item['headline'] = headline
    	item['content']  = content

    	yield item