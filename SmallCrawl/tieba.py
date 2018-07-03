from urllib import request

def tiebaSpider(url, beginPage, endPage):

	for page in range(beginPage, endPage + 1):
		pn = (page - 1 ) * 50

		filename = 'di' + str(page) + 'ye'
		fullurl = url + '&pn=' + str(pn)
		print('================')
		print(fullurl)
		html = loadPage(fullurl, filename)
		writeFile(html, filename)


def loadPage(url, filename):

	print(filename + ' is downloading')

	headers = {'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_3) AppleWebkit/537.36(KHTML,like Gecko) Chrome/48.0.2564.116 Safari537.36'}
	print(url)
	req = request.Request(url, headers = headers)
	response = request.urlopen(req)
	return response.read()


def writeFile(html, filename):
	print(filename + 'is saving')
	path = '/home/heaven/Desktop/crawler/SmallCrawl/Data/' + kw + '.txt'
	with open(path, 'wb') as f:
		f.write(html)



if __name__ == '__main__':
	kw = str(input('tiebaName:'))
	beginPage = int(input('beginPage:'))
	endPage = int(input('endPage:'))

	url = 'https://tieba.baidu.com/f?kw='

	url = url + kw

	tiebaSpider(url, beginPage, endPage)
