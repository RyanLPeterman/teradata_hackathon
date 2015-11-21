from flask import Flask, render_template, redirect, url_for, request
import sys
import json
sys.path.insert(0, 'backend')
import query
app = Flask(__name__)

data=query.getdata()
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/test")
def test():
    #data = getdata()
    return data

if __name__ == "__main__":
    app.run()
