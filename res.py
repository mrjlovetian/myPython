import re
import urllib

def getHtml(url):
	resopnse = urllib.urlopen(url)
	html = resopnse.read()

def readHtml(html):
	r = r'src="(.*\.jpg)'
	res = re.compile(r)
	print (html)
	urlList = re.findall(res, html)
	print urlList

html = getHtml("http://www.19lou.com/")
readHtml(html)