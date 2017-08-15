import pymysql
 
 #链接数据库
connect = pymysql.Connect(
     host='localhost',
     port=3306,
     user='root',
     passwd='897011805',
     db='yhj',
 )



cur = connect.cursor()

x = 100
for index in range(x):
    sql = "insert into hotTip (txt) values ('woshixiaohongjun%d')"
    cur.execute(sql%index)
    print (cur.fetchone())
    connect.commit()
    

cur.close()
connect.close()