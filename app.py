from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/test")
def test():
    return "test"

if __name__ == "__main__":
    app.run()
