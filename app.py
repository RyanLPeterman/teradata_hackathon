from flask import Flask, render_template, redirect, url_for, request
import sys
import json
sys.path.insert(0, 'backend')
import query
app = Flask(__name__)

#data=query.getdata()
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/test")
def test():
    #data = getdata()
    return "yoo"

@app.route("/getdata")
def getdata():
	print "receive request"
    sdata = json.loads(request)
    data = query.getdata(sdata['bed'], sdata['low'], sdata['high'])
	return data

if __name__ == "__main__":
    app.run()
