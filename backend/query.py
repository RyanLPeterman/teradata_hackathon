#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import json


def getdata():
	try:
		con = mdb.connect('localhost', 'root', 'root', 'crime');

		cur = con.cursor()
		cur.execute("select x, y from crime;")
		crime = cur.fetchall()
		cur.execute("select count(*) from crime;")
		count = len(crime)

	except mdb.Error, e:
	  
		print "Error %d: %s" % (e.args[0],e.args[1])
		sys.exit(1)
		
	finally:    
		return json.dumps([ {'max' : count}, crime])
		if con:    
			con.close()

#print getdata()
