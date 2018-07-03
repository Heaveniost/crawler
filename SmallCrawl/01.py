from urllib  import request

url = 'https://www.douban.com'
ua_header = {'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_3) AppleWebkit/537.36(KHTML,like Gecko) Chrome/48.0.2564.116 Safari537.36'}

req = request.Request(url, headers=ua_header)
response = request.urlopen(req)
html = response.read()
print(html)
