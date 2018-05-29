# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/channel/teacher.shtml',]

    def parse(self, response):
#        filename = "teachers.html"
#        with open(filename,'w') as f:
#            f.write(response.body)
#        print(response.body)

        items = []
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            item = ItcastItem()
            
            item['name'] = node.xpath("./h3/text()").extract()[0]
            item['level'] = node.xpath("./h4/text()").extract()[0]
            item['info'] = node.xpath("./p/text()").extract()[0]

            items.append(item)

        return items
