from urllib import request, parse
import json


'''
i=hello&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1530602886978
&sign=0569ca59b4c749008d7a9a05b548359f
&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_CLICKBUTTION&typoResult=false
'''

# TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.

print('Enter the word you want to translate below')
content = str(input('word: '))

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# translate_o --> translate

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_3) AppleWebkit/537.36(KHTML,like Gecko) Chrome/48.0.2564.116 Safari537.36'}

formdata = {
	'i': content,
	'from': 'AUTO',
	'to': 'AUTO',
	'smartresult': 'dict',
	'client': 'fanyideskweb',
	'salt': '1530602886978',
	'sign': '0569ca59b4c749008d7a9a05b548359f',
	'doctype': 'json',
	'version': '2.1',
	'keyfrom': 'fanyi.web',
	'action': 'FY_BY_CLICKBUTTION',
	'typoResult': 'false'
}

data = parse.urlencode(formdata).encode('utf-8')

req = request.Request(url, data=data, headers=headers)
response = request.urlopen(req)
html = response.read().decode('utf-8') 
#  {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":1,"translateResult":[[{"src":"hello","tgt":"你好"}]]}
target = json.loads(html)
print('result: %s' % (target['translateResult'][0][0]['tgt']))

