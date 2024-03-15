# hello.py
from flask import Flask
app = Flask(__name__)

@app.route("/ping", methods = ['GET'])
def piing():
    return "pong"

app.run()