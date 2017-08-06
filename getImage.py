# -*- coding:utf-8 -*-

import urllib, urllib2
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url = 'http://www.pythontab.com/html/2014/pythonhexinbiancheng_1128/928.html'
request = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(request)
result = response.read()
# print ('lalal', result)

resultHtml = BeautifulSoup(result)

for hh in resultHtml.find_all('p'):
	print hh.text