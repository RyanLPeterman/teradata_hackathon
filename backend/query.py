#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import json

def getrating(d):
	if "mischief".upper() in d:
		return 2
	if "possession".upper() in d or "firearm".upper() in d:
		return 3
	if "theft".upper() in d or "burglary".upper() in d:
			return 5
	if "rape".upper() in d or "abuse".upper() in d:
		return 8
	if "robbery".upper() in d:
		return 6
	if "auto".upper() in d or "moto".upper() in d or "truck".upper() in d:
		return 4
	if "battery".upper() in d or "assault".upper() in d or "violence".upper() in d or "injury".upper() in d:
		return 7
	if "arson".upper() in d:
		return 7
	return 1
		

def getdata():
	try:
		con = mdb.connect('localhost', 'root', 'root', 'crime');

		cur = con.cursor()
		cur.execute("select x, y, description from crime;")
		crime = cur.fetchall()
		cur.execute("select count(*) from crime;")
		count = len(crime)

	except mdb.Error, e:
	  
		print "Error %d: %s" % (e.args[0],e.args[1])
		sys.exit(1)
		
	finally:    
		#print crime
		data = []
		for x in enumerate(crime):
			temp = {}
			temp['lat'] = x[1][1]
			temp['lng'] = x[1][0]
			temp['count'] = getrating(x[1][2])
			data.append(temp)
		return  json.dumps({'max' : count , 'data': data})

		if con:    
			con.close()

print getdata()
