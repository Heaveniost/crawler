# -*- coding: utf-8 -*-
import scrapy


# class TestSpider(scrapy.Spider):
#     name = 'test'
#     allowed_domains = ['renren.com']
#     start_urls = ['http://renren.com/']

#     def parse(self, response):
#         pass
 
# 导入items中的数据项定义模块
#
 
class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/913043576/profile?v=info_timeline']
 
    def start_requests(self):
        return [scrapy.FormRequest('http://www.renren.com/PLogin.do',
                                   formdata={'email':'15201417639','password':'kongzhagen.com'},
                                   callback=self.login)]
 
    def login(self,response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
 
    def parse(self, response):
        # item = RenrenItem()
        # basicInfo = response.xpath('//div[@id="basicInfo"]')
        # sex = basicInfo.xpath('div[2]/dl[1]/dd/text()').extract()[0]
        # birthday = basicInfo.xpath('div[2]/dl[2]/dd/a/text()').extract()
        # birthday = ''.join(birthday)
        # addr = basicInfo.xpath('div[2]/dl[3]/dd/text()').extract()[0]
        # item['sex'] = sex
        # item['addr'] = addr
        # item['birthday'] =birthday
        with open('Data/renren.html','w') as f:
             f.write(response.body.decode('utf-8'))

        # return  item