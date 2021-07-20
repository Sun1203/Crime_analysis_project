from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import *
from memo import memo

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/info', methods=['GET', 'POST'])
def about():
    if request.method == "GET":
        return render_template('info.html')

        # <iframe src="http://localhost:5601/goto/9bc00ce7159558ceb9864d06d845b86f" height="600" width="800"></iframe>
    elif request.method == "POST":
        return '{"img01" : "http://localhost:5601/goto/9bc00ce7159558ceb9864d06d845b86f"}'

@app.route('/info1', methods=['GET', 'POST'])
def about1():

        # <iframe src="http://localhost:5601/goto/e660241fa417e58a78414d910c158ac0" height="600" width="800"></iframe>
    if request.method == "POST":
        return '{"img02" : "http://localhost:5601/goto/e660241fa417e58a78414d910c158ac0"}'

@app.route('/join', methods=['GET','POST'])
def join():
    return render_template('join.html')

@app.route('/map', methods=['GET'])
def map():
    return render_template('map.html')

@app.route('/memo', methods=['POST'])
def parse():
    return memo()



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5000')
