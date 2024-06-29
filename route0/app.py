from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Deez nuts!"

@app.route("/test")
def test():
    return "This website is a test!"

@app.route("/fat")
def fat():
    return "Fat whale!"

@app.route("/HomeDepot")
def HomeDepot():
    return "Just home depot!"

@app.route("/EEE")
def EEE():
    return "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!"

