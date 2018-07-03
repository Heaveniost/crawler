# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']

    def start_requests(self):
    	url = 'http://www.renren.com'
    	yield scrapy.FormRequest(
    		url = url,
    		formdata = {"email":'18071215757','password':'qq123456'},
    		callback = self.login)

    def login(self,reponse):
    	yield self.make_requests_from_url('http://renren.com/')


    # def parse_page(self, response):
    # 	with open('Data/renren.html','w') as f:
    # 		f.write(response.body)

    def parse(self,reponse):
    	with open('Data/renren.html','w') as f:
    		f.write(response.body)


