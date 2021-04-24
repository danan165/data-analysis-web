import flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/watertemp', methods=['GET'])
def watertemp():
    return render_template("watertemp.html")

if __name__=="__main__":
    app.run()
