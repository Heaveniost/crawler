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


    def parse_item(self,response):

    	item = WenZhengItem()
    	
    	item['title'] = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract()[0]
    	item['number'] = item['title'].split(' ')[-1].split(':')[-1]    	
    	item['content'] = response.xpath("//div[@class='c1 text14_2']/text()").extract()[0]
    	item['url'] = response.url

    	yield item

 
