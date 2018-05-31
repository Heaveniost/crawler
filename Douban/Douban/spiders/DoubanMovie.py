# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem


class DoubanmovieSpider(scrapy.Spider):
    name = 'DoubanMovie'
    allowed_domains = ['movie.douban.com']
    url = 'http://movie.douban.com/top250?start='
    offset = 0
    end = "&filter="
    start_urls = [url + str(offset) + end]

    def parse(self, response):

    	node_list = response.xpath("//div[@class='info']")

    	for node in node_list:
    		item = DoubanItem()

    		title = ""
    		title_list = node.xpath("./div[1]/a/span/text()").extract()
    		for element in title_list:
    			title += element
    		print(title_list)
    		item['title'] = ''.join(title_list)

    		item['score'] = node.xpath("./div[2]//span[@class='rating_num']/text()").extract()[0]

    		info = ""
    		info_list = node.xpath("./div[2]/p[1]/text()").extract()
    		for element in info_list:
    			print(element.strip())
    			#element.strip()
    			info += element.strip()

    		item['info']  = info  #''.join(info_list.strip()) not useful

    		if len(node.xpath("./div[2]//span[@class='inq']/text()")):
    			item['content'] = node.xpath("./div[2]//span[@class='inq']/text()").extract()[0]
    		else:
    			item['content'] = 'None content'

    		yield item

    	if self.offset <= 225:
    		self.offset += 25
    		new_url = self.url + str(self.offset) + self.end
    		yield scrapy.Request(new_url,callback = self.parse)


