#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import json


def getdata(bed, low, high):
	houses = []
	count = 0
	try:
		con = mdb.connect('localhost', 'root', 'root', 'crime');
		cur = con.cursor()
		cur.execute("select * from housing where bedrooms=" + str(bed) + " and rent between " + str(low) + " and " + str(high)+ ";")
		houses = cur.fetchall()
		count = len(houses)

	except mdb.Error, e:
	  
		print "Error %d: %s" % (e.args[0],e.args[1])
		sys.exit(1)
		
	finally:    
		data = []
		for x in enumerate(houses):
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

print getdata(2, 1000, 5000)
