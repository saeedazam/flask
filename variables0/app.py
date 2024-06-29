from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "This is a text!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Bye nigga!"
    return render_template("index.html", headline=headline)
