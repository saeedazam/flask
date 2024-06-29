from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "<h1>Error: Please submit the form to continue.</h1>"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)
