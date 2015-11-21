from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run()
