# -*- coding=utf-8 -*-
 
from threading import Thread
from Queue import Queue
import time
from lxml import etree
import requests
 
 
class DouBanSpider(Thread):
    def __init__(self, url, q, num=0):
        # 重写写父类的__init__方法
        super(DouBanSpider, self).__init__()
        self.url = url
        self.q = q
        self.num = num
        self.headers = {
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/top250?start=225&filter=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
        }
 
    def run(self):
        self.parse_page()
 
    def send_request(self,url):
        '''
        用来发送请求的方法
        :return: 返回网页源码
        '''
        # 请求出错时，重复请求３次,
        i = 0
        while i <= 3:
            try:
                print u"[INFO]请求url:"+url
                html = requests.get(url=url,headers=self.headers).content
            except Exception as e:
                print u'[INFO] %s%s'% (e,url)
                i += 1
            else:
                return html
 
    def parse_page(self):
        '''
        解析网站源码，并采用ｘｐａｔｈ提取　电影名称和平分放到队列中
        :return:
        '''
        response = self.send_request(self.url)
        html = etree.HTML(response)
        num = self.num
        #　获取到一页的电影数据
        node_list = html.xpath("//div[@class='info']")
        for k,move in enumerate(node_list):
            # 电影名称
            title = move.xpath('.//a/span/text()')[0]
            # 评分
            score = move.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]

            num = num + k + 1

            # 将每一部电影的名称跟评分加入到队列
            self.q.put(str(num) + '\t' +score + "\t" + title)
 
 
def main():
    # 创建一个队列用来保存进程获取到的数据
    q = Queue()
    base_url = 'https://movie.douban.com/top250?start='
    # 构造所有ｕｒｌ
    url_list = [base_url+str(num) for num in range(0,225+1,25)]
 
    # 保存线程
    Thread_list = []
    # 创建并启动线程
    for k,url in enumerate(url_list):
        num = k * 25 + 1
        p = DouBanSpider(url,q,num)
        p.start()
        Thread_list.append(p)
 
    # 让主线程等待子线程执行完成
    for i in Thread_list:
        i.join()
 
    while not q.empty():
        print q.get()
 
if __name__=="__main__":
 
    start = time.time()
    main()
    print '[info]耗时：%s'%(time.time()-start)