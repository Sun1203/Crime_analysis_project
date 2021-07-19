from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import *


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/info', methods=['GET', 'POST'])
def about():
    if request.method == "GET":
        return render_template('info.html')
    else:
        pass

@app.route('/join', methods=['GET','POST'])
def join():
    return render_template('join.html')



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5000')
