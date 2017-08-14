#coding=utf-8

import urllib2
import re
import MySQLdb

#connect方法获取用于创建的数据库链接，里面可以指定参数，这一步只是连接到数据库，操作数据库还是需要下面的游标
conn = MySQLdb.connect(host='localhost', db='yhj', root='root', passwd='897011805', charset='utf8')

#通过获取的conn获取cursor方法创建游标
cur = conn.cursor()

url = 'http://www.zhihu.com/topic/19607535/top-answers'
netthings = urllib2.urlopen(url).read()

#re模块的findall方法可以以列表的形式返回匹配的字符串，re.S表示多行匹配
list = re.findall('<a class="question_link"(.*?)/a>', netthings, re.S)

p = '>(.*?)<'
for x in list:
    title = re.search(p, x, re.S).group(1)
    sql = "insert into hotTip (title) values ('%s')" % title
    print (sql)
    cur.execute(sql)
    conn.commit()
conn.close()