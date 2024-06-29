from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is a text!"

@app.route("/<string:IPAdd>")
def IPAddress(IPAdd):
    IPAdd = IPAdd.capitalize()
    return f"<h1>Thank you for your IP address. Your IP address is: {IPAdd}. Downloading WinXPHorror.exe...<h1>"

