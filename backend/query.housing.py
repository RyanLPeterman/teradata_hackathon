#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import json


def getdata():
	try:
		con = mdb.connect('localhost', 'root', 'root', 'crime');

		cur = con.cursor()
		cur.execute("select * from housing;")
		crime = cur.fetchall()
		cur.execute("select count(*) from housing;")
		count = len(crime)

	except mdb.Error, e:
	  
		print "Error %d: %s" % (e.args[0],e.args[1])
		sys.exit(1)
		
	finally:    
		data = []
		for x in enumerate(crime):
			temp = {}
			temp['id'] = x[0]
			temp['bed'] = x[1][0]
			temp['rent'] = x[1][1]
			temp['lat'] = x[1][2]
			temp['lng'] = x[1][3]
			data.append(temp)
		return  json.dumps({'max' : count , 'data': data})

		if con:    
			con.close()

print getdata()
