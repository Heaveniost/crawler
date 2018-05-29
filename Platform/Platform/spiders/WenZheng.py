# -*- coding: utf-8 -*-
import scrapy
from Platform.items import WenZhengItem


class WenzhengSpider(scrapy.Spider):
    name = 'WenZheng'
    allowed_domains = ['wz.sun0769.com']
    base_url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        
        links = response.xpath("//a[@class='news14']/@href").extract()

        for link in links:
        	yield scrapy.Request(link,callback = self.parse_item)

        if self.offset <= 3000:
        	self.offset += 30
        	yield scrapy.Request(self.base_url + str(self.offset),callback = self.parse)


    def parse_item(self,response):

    	item = WenZhengItem()
    	
    	headline = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract()[0] 
    	#[' 提问：希望规划局能关注下东坑\xa0\xa0编号:186732\xa0\xa0'] liang ge mao hao bu yiyang 
    	# scrapy shell "http://wz.sun0769.com/html/question/201805/3723028.shtml
    	# print(headline.split('  ')[1])
    	# print(headline.split(' ')[1].split(':'))
    	item['title'] = headline.split('\xa0')[0]
    	item['number'] = headline.split(' ')[-1].split(':')[-1]  

    	# content = response.xpath("//div[@class='c1 text14_2']/text()").extract()
    	# print(len(content))
    	# if len(content) == 0:
    	# 	content = response.xpath("//div[@class='contentext']/text()").extract()
    	# 	item['content'] = ''.join(content).strip()
    	# else:
    	# 	item['content'] = ''.join(content).strip()

    	content = response.xpath("//div[@class='contentext']/text()").extract()
    	# print(len(content))
    	if len(content) == 0:
    		content = response.xpath("//div[@class='c1 text14_2']/text()").extract()
    		item['content'] = ''.join(content).strip()
    	else:
    		item['content'] = ''.join(content).strip()

    	item['url'] = response.url

    	yield item

 
