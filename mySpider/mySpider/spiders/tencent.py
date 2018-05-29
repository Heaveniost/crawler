# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import TencentItem
import re


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/position.php?&start='
    offset = 650
    start_urls = [base_url+str(offset)]

    def parse(self, response):

    	items = []
    	node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

    	for node in node_list:
    		item = TencentItem()
    		item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
    		item['detailLink'] = node.xpath("./td[1]/a/@href").extract()[0]
    		if len(node.xpath("./td[2]/text()")):
    			item['positionInfo'] = node.xpath("./td[2]/text()").extract()[0]
    		else :
    			item['positionInfo'] = ""
    		item['peopleNumber'] = node.xpath("./td[3]/text()").extract()[0]
    		item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]
    		item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]

    		yield item

    	abc = response.xpath("//div[@class='pagenav']/a[@id='next']")
    	if abc.xpath("./@href").extract()[0] != "javascript:;" :
    		self.offset += 10
    		url = self.base_url + str(self.offset)
    		yield scrapy.Request(url,callback = self.parse)

    	else:
    		print("The crawl is ending")