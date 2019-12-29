#coding=utf-8
import json
from flask import Flask
app = Flask(__name__)
@app.route("/")
def login():
    data = json.dumps({
        "username":"Mushishi_xu",
        "password":"111111"
    })
    return data

if __name__ == "__main__":
    app.run()
