from flask import Flask, render_template, redirect, url_for, request
import sys
import json
sys.path.insert(0, 'backend')
import query
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/test")
def test():
    #data = getdata()
    print "hi"
    return str(1)

if __name__ == "__main__":
    app.run()
