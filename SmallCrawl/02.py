from urllib import request
import random

url = 'http://www.itcast.cn'
ua_list = [
	'Mozilla/5.0 (Macintosh;U;IntelMacOSX10_6_8;en-us) AppleWebKit/534.50(KHTML,likeGecko) Version/5.1 Safari/534.50',

	'Mozilla/5.0 (Macintosh;IntelMacOSX10.6;rv:2.0.1) Gecko/20100101 Firefox/4.0.1',

	'Mozilla/5.0 (WindowsNT6.1;rv:2.0.1) Gecko/20100101 Firefox/4.0.1',

	'Opera/9.80 (Macintosh;IntelMacOSX10.6.8;U;en) Presto/2.8.131 Version/11.11',

	'Opera/9.80 (WindowsNT6.1;U;en) Presto/2.8.131 Version/11.11',
 
	'Mozilla/5.0 (Macintosh;IntelMacOSX10_7_0) AppleWebKit/535.11(KHTML,likeGecko) Chrome/17.0.963.56 Safari/535.11'
	]
user_agent = random.choice(ua_list)

req = request.Request(url)
req.add_header('User_Agent', user_agent)

req.get_header('User-agent')

response = request.urlopen(req)
html = response.read()
print(html)

