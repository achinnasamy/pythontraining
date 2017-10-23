from flask import Flask
app = Flask(__name__)

@app.route("/")
def rootrequest():
    return "Data-Ingestion Home Page"


@app.route("/data")
def data():
    return "Data-Ingestion Started"