from flask import Flask, render_template, redirect, url_for, request
import sys
import json
sys.path.insert(0, 'backend')
import queryhousing
app = Flask(__name__)

#data=query.getdata()
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/test")
def test():
    #data = getdata()
    return "yoo"

@app.route("/getdata",methods=["GET"])
def getdata():
    print "receive request"
    
    bed = request.args['bed']
    low = request.args['low']
    high = request.args['high']
    print bed, low, high
    data = query.getdata(bed, low, high)
    #print data
    return data

if __name__ == "__main__":
    app.run()
