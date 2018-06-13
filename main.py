# -*- encoding: utf-8 -*-
from flask import Flask
from config import DevConfig


app = Flask(__name__)


app.config.from_object(DevConfig)



@app.route("/")
def home():
    return "<h1>Hello World!</h1>"


@app.route("/test")
def test():
    return "test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
