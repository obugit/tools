#!/usr/bin/env python
import MySQLdb
try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='lin',db='zhanghao',port=3306)
	cur=conn.cursor()
	cur.execute('select * from jianliwang')
	value=['www.dajiewang.com','linshaobode@163.com','a159147']
	cur.execute('insert into jianliwang values('www.dajiewang.com','linshaobode@163.com','a159147')')
	cur.execute('select * from jianliwang')
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
				
